import torch
import os
import numpy as np
from PIL import Image

from transformers import AutoProcessor, AutoModelForZeroShotObjectDetection, Owlv2Processor, Owlv2ForObjectDetection
from ultralytics import YOLOWorld, YOLOE
from ultralytics.models.sam import SAM3SemanticPredictor

WEIGHTS_DIR = "./weights"
os.makedirs(WEIGHTS_DIR, exist_ok=True)
os.environ["HF_HOME"] = os.path.join(WEIGHTS_DIR, "hf_cache")

def get_best_device():
    """Selecciona dinámicamente el mejor hardware de cómputo disponible en la máquina actual."""
    if torch.cuda.is_available():
        try:
            _ = torch.zeros(1, device="cuda")
            return "cuda"
        except Exception as e:
            print(f"\n[WARNING] GPU detectada pero no compatible con los kernels de PyTorch ({e}).")
            print("Conmutando automáticamente a modo CPU para garantizar la ejecución.")
            return "cpu"
    elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
        try:
            _ = torch.zeros(1, device="mps")
            return "mps"
        except Exception:
            return "cpu"
    else:
        return "cpu"                                   


class GroundingDinoEvaluator:
    """Evaluador para Grounding DINO (detección Open-Vocabulary mediante texto)."""

    def __init__(self, version="base"):
        """Carga el modelo adaptándose de forma agnóstica al hardware."""
        self.dev = get_best_device()
        print(f"[Grounding DINO] Inicializando modelo en dispositivo: {self.dev.upper()}")
        
        model_id = "IDEA-Research/grounding-dino-tiny" if version == "tiny" else "IDEA-Research/grounding-dino-base"
        self.proc = AutoProcessor.from_pretrained(model_id)
        self.model = AutoModelForZeroShotObjectDetection.from_pretrained(model_id).to(self.dev)
        self.model.eval()

    def predict(self, img, prompts, thresh):
        """Doble pasada secuencial por clase para no alterar la matriz de cross-attention interna."""
        W, H = img.size
        dets = []
        for cid, p in prompts.items():
            ins = self.proc(images=img, text=p, return_tensors="pt").to(self.dev)
            with torch.no_grad(): 
                out = self.model(**ins)
            res = self.proc.post_process_grounded_object_detection(
                out, ins.input_ids, threshold=thresh, text_threshold=thresh, target_sizes=[(H, W)]
            )[0]
            for s, b in zip(res["scores"].cpu(), res["boxes"].cpu()): 
                dets.append((float(s), cid, b.tolist()))
        return dets


class Owlv2Evaluator:
    """Evaluador para OWLv2 (basado en parches de atención ViT)."""

    def __init__(self, model_id="google/owlv2-base-patch16-ensemble"):
        """Fuerza resolución nativa de 960x960 px para de-estabilizar los parches de atención."""
        self.dev = get_best_device()
        print(f"[OWLv2] Inicializando modelo en dispositivo: {self.dev.upper()}")
        
        self.proc = Owlv2Processor.from_pretrained(model_id, size={"height":960, "width":960})
        self.model = Owlv2ForObjectDetection.from_pretrained(model_id).to(self.dev)
        self.model.eval()
        
    def predict(self, img, prompts, thresh):
        """Doble pasada por prompt con interpolación activa de codificación posicional."""
        W, H = img.size
        dets = []
        for cid, q in prompts.items():
            ins = self.proc(text=[[q]], images=img, return_tensors="pt").to(self.dev)
            with torch.no_grad(): 
                out = self.model(**ins, interpolate_pos_encoding=True)
            res = self.proc.post_process_grounded_object_detection(
                out, threshold=thresh, target_sizes=torch.tensor([[H, W]], device=self.dev)
            )[0]
            for s, b in zip(res["scores"].cpu(), res["boxes"].cpu()): 
                dets.append((float(s), cid, b.tolist()))
        return dets


class YoloWorldEvaluator:
    """Evaluador para YOLO-World v2 (detección zero-shot acoplada con CLIP)."""

    def __init__(self, size="x"): 
        """Configura el entorno de ejecución dinámico para Ultralytics."""
        self.dev = get_best_device()
        print(f"[YOLO-World] Inicializando modelo en dispositivo: {self.dev.upper()}")
        
        model_path = os.path.join(WEIGHTS_DIR, f"yolov8{size}-worldv2.pt")
        self.model = YOLOWorld(model_path)
        self.cached_classes = None

    def predict(self, img, prompts, thresh):
        """Inferencia forzando de forma explícita el hardware mapeado en la inicialización."""
        ordered_ids = sorted(prompts.keys())
        classes_list = [prompts[i] for i in ordered_ids]
        
        if classes_list != self.cached_classes:
            self.model.set_classes(classes_list)
            self.cached_classes = classes_list
            
        res = self.model.predict(
            source=img, imgsz=1280, conf=thresh, iou=1.0, verbose=False, device=self.dev
        )[0]
        return [(float(b.conf), int(b.cls), b.xyxy[0].tolist()) for b in res.boxes]


class YoloeEvaluator:
    """Evaluador para YOLOE (segmentación zero-shot guiada por texto)."""

    def __init__(self, version="11m"):
        """Configura el entorno de ejecución dinámico para el backend de YOLOE."""
        self.dev = get_best_device()
        print(f"[YOLOE] Inicializando modelo en dispositivo: {self.dev.upper()}")
        
        model_path = os.path.join(WEIGHTS_DIR, f"yoloe-{version}-seg.pt")
        self.model = YOLOE(model_path)
        self.cached_classes = None
        
    def predict(self, img, prompts, thresh):
        """Inferencia forzando de forma explícita el hardware detectado."""
        ordered_ids = sorted(prompts.keys())
        p = [prompts[i] for i in ordered_ids]
        
        if p != self.cached_classes:
            self.model.set_classes(p, self.model.get_text_pe(p))
            self.cached_classes = p
            
        res = self.model.predict(
            source=img, imgsz=1280, conf=thresh, iou=1.0, verbose=False, device=self.dev
        )[0]
        return [(float(b.conf), int(b.cls), b.xyxy[0].tolist()) for b in res.boxes] if res.boxes else []


class Sam3Evaluator:
    """Evaluador para SAM 3 (Segment Anything Model 3 guiado por texto)."""

    def __init__(self): 
        """Ajusta dinámicamente la precisión y el hardware del predictor semántico."""
        self.dev = get_best_device()
        print(f"[SAM 3] Inicializando modelo en dispositivo: {self.dev.upper()}")
        
        use_half = True if self.dev == "cuda" else False
        
        model_path = os.path.join(WEIGHTS_DIR, "sam3.pt")
        self.pred = SAM3SemanticPredictor(overrides=dict(
            task="segment", mode="predict", model=model_path, 
            half=use_half, save=False, verbose=False, device=self.dev
        ))
        
    def predict(self, img, prompts, thresh):
        """Redimensiona la imagen a un máximo de 644 px por limitaciones del codificador de imágenes de SAM."""
        W, H = img.size
        scale = min(644/W, 644/H, 1.0)
        img_r = img.resize((int(W*scale), int(H*scale)), Image.BILINEAR)
        self.pred.set_image(np.array(img_r))
        dets = []
        for cid, q in prompts.items():
            res = self.pred(text=[q])
            if res and res[0].boxes:
                for b in res[0].boxes:
                    bx = b.xyxy[0].tolist()
                    dets.append((float(b.conf), cid, [bx[0]/scale, bx[1]/scale, bx[2]/scale, bx[3]/scale]))
        return dets