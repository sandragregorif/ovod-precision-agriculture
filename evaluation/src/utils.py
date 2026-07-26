import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

def yolo_to_xyxy(yolo_box, image_width, image_height):
    """
    Transforma una caja de coordenadas en formato YOLO (normalizada respecto al centro)
    a coordenadas absolutas en píxeles [x1, y1, x2, y2] (esquinas superior-izquierda e inferior-derecha).

    Parámetros:
    - yolo_box: Lista o tupla con [centro_x, centro_y, ancho, alto] en rango 0-1.
    - image_width: Ancho de la imagen en píxeles.
    - image_height: Alto de la imagen en píxeles.
    """
    cx, cy, bw, bh = yolo_box
    return [
        (cx - bw / 2) * image_width,
        (cy - bh / 2) * image_height,
        (cx + bw / 2) * image_width,
        (cy + bh / 2) * image_height,
    ]

def load_groundtruth(label_path, image_width, image_height):
    """
    Carga y procesa un archivo de anotaciones de texto (Ground Truth) en formato YOLO.
    Lee línea por línea, extrae el ID de clase y convierte las coordenadas normalizadas
    a píxeles absolutos usando 'yolo_to_xyxy'.

    Parámetros:
    - label_path: Ruta del archivo .txt que contiene las etiquetas.
    - image_width: Ancho de la imagen correspondiente.
    - image_height: Alto de la imagen correspondiente.
    """
    groundtruth = []
    if not os.path.exists(label_path):
        return groundtruth
    with open(label_path) as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) < 5:
                continue
            class_id = int(parts[0])
            box = yolo_to_xyxy([float(x) for x in parts[1:5]], image_width, image_height)
            groundtruth.append((class_id, box))
    return groundtruth

def get_label_path(image_path, labels_dir):
    """
    Construye la ruta del archivo de etiquetas de texto (.txt) asociado a una imagen.
    Extrae el nombre base (stem) de la imagen y lo concatena con el directorio de etiquetas.

    Parámetros:
    - image_path: Ruta completa del archivo de imagen.
    - labels_dir: Carpeta donde se almacenan las etiquetas de ese dataset.
    """
    stem = os.path.splitext(os.path.basename(image_path))[0]
    return os.path.join(labels_dir, stem + ".txt")

def compute_iou(box_a, box_b):
    """
    Calcula el índice de Intersección sobre Unión (IoU) entre dos cajas delimitadoras
    en formato plano [x1, y1, x2, y2]. Retorna un valor flotante entre 0.0 y 1.0.

    Parámetros:
    - box_a: Coordenadas de la primera caja.
    - box_b: Coordenadas de la segunda caja.
    """
    inter_x1 = max(box_a[0], box_b[0])
    inter_y1 = max(box_a[1], box_b[1])
    inter_x2 = min(box_a[2], box_b[2])
    inter_y2 = min(box_a[3], box_b[3])

    intersection = max(0.0, inter_x2 - inter_x1) * max(0.0, inter_y2 - inter_y1)
    if intersection == 0.0:
        return 0.0

    area_a = (box_a[2] - box_a[0]) * (box_a[3] - box_a[1])
    area_b = (box_b[2] - box_b[0]) * (box_b[3] - box_b[1])
    return intersection / (area_a + area_b - intersection)

def match_predictions_to_gt(predictions, groundtruth_boxes, iou_threshold):
    """
    Empareja las cajas predichas por el modelo con las cajas reales (Ground Truth) de la escena.
    Ordena las predicciones por confianza de forma descendente y asigna un flag binario (1 o 0)
    indicando si la predicción es un Verdadero Positivo (TP) según el umbral IoU y la clase.

    Parámetros:
    - predictions: Lista de detecciones del modelo [(score, class_id, box), ...].
    - groundtruth_boxes: Lista de objetos reales [(class_id, box), ...].
    - iou_threshold: Umbral mínimo de solapamiento para validar un emparejamiento.
    """
    matched = [False] * len(groundtruth_boxes)
    results = []

    for score, class_id, pred_box in sorted(predictions, key=lambda x: -x[0]):
        best_iou, best_idx = 0.0, -1
        for j, (gt_class_id, gt_box) in enumerate(groundtruth_boxes):
            if matched[j]:
                continue
            iou = compute_iou(pred_box, gt_box)
            if iou > best_iou:
                best_iou, best_idx = iou, j

        is_tp = 0
        if best_iou >= iou_threshold and best_idx >= 0:
            matched[best_idx] = True
            if groundtruth_boxes[best_idx][0] == class_id:
                is_tp = 1
                
        results.append((score, is_tp))
    return results

def compute_ap(scored_tp_list, total_groundtruth):
    """
    Calcula la Precisión Media (AP) utilizando la interpolación formal de 101 puntos
    (común en benchmarks como COCO). Retorna la Precisión final, el Recall final y el AP interpolado.

    Parámetros:
    - scored_tp_list: Lista de tuplas [(score, is_tp), ...] procesadas por imagen.
    - total_groundtruth: Cantidad total de objetos reales existentes para esa clase.
    """
    if total_groundtruth == 0 or not scored_tp_list:
        return 0.0, 0.0, 0.0

    sorted_preds = sorted(scored_tp_list, key=lambda x: -x[0])
    cum_tp = np.cumsum([p[1] for p in sorted_preds])
    cum_fp = np.cumsum([1 - p[1] for p in sorted_preds])

    precision_curve = cum_tp / (cum_tp + cum_fp)
    recall_curve = cum_tp / total_groundtruth

    ap = sum(
        precision_curve[recall_curve >= t].max() if (recall_curve >= t).any() else 0.0
        for t in np.linspace(0, 1, 101)
    ) / 101

    return float(precision_curve[-1]), float(recall_curve[-1]), float(ap)

def _build_pr_curve(scored_tp_list, total_groundtruth):
    """
    Método auxiliar interno que construye los vectores acumulados de precisión, recall
    y umbrales de confianza para poder graficar posteriormente las curvas macro y por clase.

    Parámetros:
    - scored_tp_list: Lista de emparejamientos [(score, is_tp), ...].
    - total_groundtruth: Cantidad total de cajas reales.
    """
    if total_groundtruth == 0 or not scored_tp_list:
        return np.array([]), np.array([]), np.array([])

    sorted_preds = sorted(scored_tp_list, key=lambda x: -x[0])
    scores = np.array([p[0] for p in sorted_preds])
    cum_tp = np.cumsum([p[1] for p in sorted_preds])
    cum_fp = np.cumsum([1 - p[1] for p in sorted_preds])
    precision_curve = cum_tp / (cum_tp + cum_fp)
    recall_curve = cum_tp / total_groundtruth

    return precision_curve, recall_curve, scores

def compute_map50_95(per_class_raw_predictions, per_class_groundtruth, class_names):
    """
    Calcula la métrica rigurosa mAP@[0.50:0.95]. Evalúa el Average Precision (AP) de cada clase
    en un rango de 10 umbrales de IoU diferentes (desde 0.50 hasta 0.95 con saltos de 0.05) y
    realiza la media geométrica para obtener el valor global.

    Parámetros:
    - per_class_raw_predictions: Diccionario de predicciones crudas indexadas por ID de clase.
    - per_class_groundtruth: Diccionario de anotaciones reales indexadas por ID de clase.
    - class_names: Diccionario o lista con los nombres textuales de las clases.
    """
    iou_thresholds = np.arange(0.50, 1.00, 0.05)
    per_class_ap50_95_lists = {c: [] for c in class_names}

    all_preds = []
    for c_id, pred_list in per_class_raw_predictions.items():
        for score, box, img_id in pred_list:
            all_preds.append({'score': score, 'class': c_id, 'box': box, 'img_id': img_id})
            
    all_gts = []
    for c_id, gt_list in per_class_groundtruth.items():
        for box, img_id in gt_list:
            all_gts.append({'class': c_id, 'box': box, 'img_id': img_id, 'matched': False})
            
    for iou_thr in iou_thresholds:
        for gt in all_gts:
            gt['matched'] = False
            
        sorted_preds = sorted(all_preds, key=lambda x: x['score'], reverse=True)
        tp_flags = {c: [] for c in class_names}
        
        for p in sorted_preds:
            best_iou = 0.0
            best_gt = None
            
            for gt in all_gts:
                if gt['img_id'] == p['img_id'] and not gt['matched']:
                    iou = compute_iou(p['box'], gt['box'])
                    if iou > best_iou:
                        best_iou = iou
                        best_gt = gt
                        
            is_tp = 0
            if best_iou >= iou_thr and best_gt is not None:
                best_gt['matched'] = True
                if best_gt['class'] == p['class']:
                    is_tp = 1
                    
            tp_flags[p['class']].append(is_tp)
            
        for c_id in class_names:
            flags = tp_flags[c_id]
            n_gt = sum(1 for gt in all_gts if gt['class'] == c_id)
            
            if n_gt == 0 or not flags:
                per_class_ap50_95_lists[c_id].append(0.0)
                continue
                
            cum_tp = np.cumsum(flags)
            cum_fp = np.cumsum([1 - t for t in flags])
            precision_curve = cum_tp / (cum_tp + cum_fp)
            recall_curve = cum_tp / n_gt
            
            ap = sum(
                precision_curve[recall_curve >= t].max() if (recall_curve >= t).any() else 0.0
                for t in np.linspace(0, 1, 101)
            ) / 101
            per_class_ap50_95_lists[c_id].append(ap)

    final_ap50_95 = {c_id: float(np.mean(per_class_ap50_95_lists[c_id])) for c_id in class_names}
    map50_95 = float(np.mean(list(final_ap50_95.values()))) if final_ap50_95 else 0.0
    return final_ap50_95, map50_95

def get_tiles(image_width, image_height, tile_size, overlap):
    """
    Genera una cuadrícula de coordenadas de ventanas deslizantes (parches) para la estrategia
    de Tiling. Calcula las esquinas [x1, y1, x2, y2] asegurando que las ventanas de los bordes
    no sobresalgan del límite real de la imagen.

    Parámetros:
    - image_width: Ancho completo de la imagen en píxeles.
    - image_height: Alto completo de la imagen en píxeles.
    - tile_size: Tamaño cuadrado o ancho de la ventana de inferencia (ej. 1280).
    - overlap: Píxeles de solapamiento o intersección entre parches vecinos (ej. 256).
    """
    step = tile_size - overlap
    xs = list(range(0, image_width, step))
    ys = list(range(0, image_height, step))
    tiles = []
    for y in ys:
        for x in xs:
            x2 = min(x + tile_size, image_width)
            y2 = min(y + tile_size, image_height)
            tiles.append((x, y, x2, y2))
    return tiles

def predict_with_tiling(evaluator, img, prompts, thresh, use_tiling=False, tile_size=1280, tile_overlap=256):
    """
    Orquesta la inferencia adaptativa sobre una imagen. Si el Tiling está desactivado, realiza
    una inferencia global estándar. Si está activado, recorta la imagen en parches, invoca al
    evaluador en cada parche y desplaza las coordenadas resultantes al plano coordenado de la imagen original.

    Parámetros:
    - evaluator: Instancia de la clase del modelo cargado (YOLO, OWLv2, DINO, etc.).
    - img: Imagen en formato PIL en espacio de color RGB.
    - prompts: Diccionario de prompts asignados para la búsqueda.
    - thresh: Umbral de confianza inicial (score threshold).
    - use_tiling: Booleano para activar/desactivar la división por parches.
    - tile_size: Tamaño en píxeles de los parches.
    - tile_overlap: Solape entre ventanas adyacentes.
    """
    if not use_tiling:
        return evaluator.predict(img, prompts, thresh)

    W, H = img.size
    raw_dets = []
    for x1, y1, x2, y2 in get_tiles(W, H, tile_size, tile_overlap):
        tile = img.crop((x1, y1, x2, y2))
        for score, cid, box in evaluator.predict(tile, prompts, thresh):
            raw_dets.append((score, cid, [box[0] + x1, box[1] + y1, box[2] + x1, box[3] + y1]))
    return raw_dets

def nms_global(detections, iou_threshold=0.40):
    """
    Aplica el algoritmo de Supresión No Máxima (NMS) a nivel de imagen completa. Filtra y descarta
    aquellas cajas redundantes o duplicadas que tengan un IoU mayor al umbral establecido con una
    caja de mayor confianza, evitando detecciones repetidas sobre el mismo objeto.

    Parámetros:
    - detections: Lista con todas las detecciones acumuladas de los parches [(score, cid, box), ...].
    - iou_threshold: Límite máximo de solapamiento permitido entre dos objetos distintos.
    """
    if not detections:
        return []
    dets = sorted(detections, key=lambda x: x[0], reverse=True)
    kept = []
    for det in dets:
        score, class_id, box = det
        if any(compute_iou(box, k_box) > iou_threshold for _, _, k_box in kept):
            continue
        kept.append(det)
    return kept

def save_annotated_image(image_path, predictions, groundtruth, output_dir, class_names, class_colors):
    """
    Dibuja y guarda en disco una copia visual de la imagen evaluada. Pinta cajas gruesas de colores
    específicos con su respectiva etiqueta de score para las predicciones del modelo, y cajas blancas
    delgadas de fondo para representar el Ground Truth real del dataset.

    Parámetros:
    - image_path: Ruta del archivo de imagen original.
    - predictions: Predicciones finales tras NMS.
    - groundtruth: Cajas reales del dataset.
    - output_dir: Directorio de destino para guardar las imágenes resultantes.
    - class_names: Mapeo de nombres de clases.
    - class_colors: Mapeo de colores RGB asignado a cada ID de clase.
    """
    os.makedirs(output_dir, exist_ok=True)
    img = Image.open(image_path).convert("RGB")
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", size=14)
    except IOError:
        font = ImageFont.load_default()

    for s, cid, box in predictions:
        color = class_colors.get(cid, (255, 255, 255))
        draw.rectangle(box, outline=color, width=4)
        label = f"{class_names.get(cid, str(cid))} {s:.2f}"
        draw.text((box[0], max(0, box[1] - 16)), label, fill=color, font=font)

    if groundtruth:
        for _, box in groundtruth:
            draw.rectangle(box, outline=(255, 255, 255), width=2)
    img.save(os.path.join(output_dir, os.path.basename(image_path)))

def print_metrics(model_name, per_class_scored_tp, per_class_total_gt, per_class_raw_predictions, per_class_groundtruth, class_names):
    """
    Genera e imprime en la consola una tabla formateada con los resultados globales y detallados por clase.
    Calcula de manera dinámica la Precisión, Recall, F1-Score, AP50 y mAP50-95, concluyendo con una
    fila de promedios MACRO general de todo el experimento.

    Parámetros:
    - model_name: Nombre de la arquitectura evaluada.
    - per_class_scored_tp: Estructuras de TP/FP por clase.
    - per_class_total_gt: Cantidad total de GT por clase.
    - per_class_raw_predictions: Predicciones brutas para mAP50-95.
    - per_class_groundtruth: Ground Truth por clase para mAP50-95.
    - class_names: Nombre de las frutas o clases evaluadas.
    """
    per_class_ap50_95, map50_95 = compute_map50_95(per_class_raw_predictions, per_class_groundtruth, class_names)
    print(f"\n{'═' * 78}")
    print(f"  Resultados del Experimento – {model_name.upper()}")
    print(f"{'═' * 78}")
    print(f"  {'Clase':<24} {'GT':>5} {'Precision':>10} {'Recall':>8} {'F1':>8} {'AP50':>8} {'AP50-95':>9}")
    print(f"  {'-'*24} {'-'*5} {'-'*10} {'-'*8} {'-'*8} {'-'*8} {'-'*9}")

    all_p, all_r, all_f1, all_ap50 = [], [], [], []
    for class_id, class_name in class_names.items():
        p, r, ap50 = compute_ap(per_class_scored_tp[class_id], per_class_total_gt[class_id])
        ap50_95 = per_class_ap50_95[class_id]
        f1 = 2 * p * r / (p + r) if (p + r) > 0 else 0.0
        all_p.append(p); all_r.append(r); all_f1.append(f1); all_ap50.append(ap50)
        print(f"  {class_name:<24} {per_class_total_gt[class_id]:>5} {p:>10.4f} {r:>8.4f} {f1:>8.4f} {ap50:>8.4f} {ap50_95:>9.4f}")

    print(f"  {'-'*24} {'-'*5} {'-'*10} {'-'*8} {'-'*8} {'-'*8} {'-'*9}")
    print(f"  {'MACRO / TOTAL':<24} {sum(per_class_total_gt.values()):>5} {np.mean(all_p):>10.4f} {np.mean(all_r):>8.4f} {np.mean(all_f1):>8.4f} {np.mean(all_ap50):>8.4f} {map50_95:>9.4f}")
    print(f"{'═' * 78}\n")

def plot_metrics(model_name, per_class_scored_tp, per_class_total_gt, output_dir, class_names, per_class_raw_predictions, per_class_groundtruth):
    """
    Dibuja y guarda en la carpeta de resultados toda la suite de gráficas de evaluación para la memoria del TFG.
    Genera de forma automática:
    1. Curva F1 vs Confidence (identificando el punto óptimo macro).
    2. Curva Precision vs Confidence.
    3. Curva Precision-Recall (PR curve) con su leyenda de AP50.
    4. Matriz de Confusión Absoluta.
    5. Matriz de Confusión Normalizada por filas (incluyendo la clase Background).

    Parámetros:
    - Todos los diccionarios de acumulación de detecciones y estructuras del Ground Truth del dataset.
    """
    os.makedirs(output_dir, exist_ok=True)
    palette = ["#E07B00", "#00A050", "#1F77B4", "#D62728", "#9467BD", "#8C564B"]
    class_ids = list(class_names.keys())
    colors = [palette[i % len(palette)] for i in range(len(class_ids))]
    conf_range = np.linspace(0, 1, 200)

    pr_data = {}
    for cid in class_ids:
        pr_data[cid] = _build_pr_curve(per_class_scored_tp[cid], per_class_total_gt[cid])

    # 1. boxF1_curve
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title(f"{model_name} – F1 Confidence Curve", fontsize=13)
    ax.set_xlabel("Confidence"); ax.set_ylabel("F1")
    ax.set_xlim(0, 1); ax.set_ylim(0, 1.05)
    f1_global_curves = []
    for class_id, color in zip(class_ids, colors):
        p_curve, r_curve, scores = pr_data[class_id]
        if len(scores) == 0:
            f1_global_curves.append(np.zeros_like(conf_range))
            continue
        f1_per_conf = []
        for conf in conf_range:
            if not (scores >= conf).any():
                f1_per_conf.append(0.0)
                continue
            idx = np.searchsorted(-scores, -conf)
            p = float(p_curve[min(idx, len(p_curve) - 1)])
            r = float(r_curve[min(idx, len(r_curve) - 1)])
            f1_per_conf.append(2 * p * r / (p + r) if (p + r) > 0 else 0.0)
        ax.plot(conf_range, f1_per_conf, label=class_names[class_id], color=color)
        f1_global_curves.append(np.array(f1_per_conf))

    if f1_global_curves:
        macro_f1 = np.mean(f1_global_curves, axis=0)
        ax.plot(conf_range, macro_f1, label="Macro F1", color="#555555", linestyle="--", linewidth=2)
        best_idx = int(np.argmax(macro_f1))
        ax.plot(conf_range[best_idx], macro_f1[best_idx], 'ro', markersize=5)
        ax.text(0.97, 0.78, f"conf={conf_range[best_idx]:.3f}\nF1={macro_f1[best_idx]:.3f}",
                transform=ax.transAxes, fontsize=9, color="darkred", va="top", ha="right",
                bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="darkred", alpha=0.8))
    ax.legend(loc="upper right"); fig.tight_layout()
    fig.savefig(os.path.join(output_dir, "boxF1_curve.png"), dpi=150); plt.close(fig)

    # 2. boxP_curve
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title(f"{model_name} – Precision Confidence Curve", fontsize=13)
    ax.set_xlabel("Confidence"); ax.set_ylabel("Precision")
    ax.set_xlim(0, 1); ax.set_ylim(0, 1.05)
    for class_id, color in zip(class_ids, colors):
        p_curve, _, scores = pr_data[class_id]
        if len(scores) == 0: continue
        p_per_conf = []
        for conf in conf_range:
            if not (scores >= conf).any():
                p_per_conf.append(0.0)
                continue
            idx = np.searchsorted(-scores, -conf)
            p_per_conf.append(float(p_curve[min(idx, len(p_curve) - 1)]))
        ax.plot(conf_range, p_per_conf, label=class_names[class_id], color=color)
    ax.legend(); fig.tight_layout()
    fig.savefig(os.path.join(output_dir, "boxP_curve.png"), dpi=150); plt.close(fig)

    # 3. boxPR_curve
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title(f"{model_name} – Precision-Recall Curve", fontsize=13)
    ax.set_xlabel("Recall"); ax.set_ylabel("Precision")
    ax.set_xlim(0, 1); ax.set_ylim(0, 1.05)
    for class_id, color in zip(class_ids, colors):
        p_curve, r_curve, _ = pr_data[class_id]
        if len(p_curve) == 0: continue
        _, _, ap50 = compute_ap(per_class_scored_tp[class_id], per_class_total_gt[class_id])
        ax.plot(r_curve, p_curve, label=f"{class_names[class_id]} (AP50={ap50:.3f})", color=color)
    ax.legend(); fig.tight_layout()
    fig.savefig(os.path.join(output_dir, "boxPR_curve.png"), dpi=150); plt.close(fig)

    # 4. Matrices de Confusión
    n_classes = len(class_names)
    class_labels = [class_names[i] for i in range(n_classes)] + ["Background"]
    cm = np.zeros((n_classes + 1, n_classes + 1), dtype=int)

    gt_by_img, pred_by_img = {}, {}
    for c, gts in per_class_groundtruth.items():
        for box, i in gts: gt_by_img.setdefault(i, []).append({"class": c, "box": box, "matched": False})
    for c, preds in per_class_raw_predictions.items():
        for score, box, i in preds: pred_by_img.setdefault(i, []).append({"score": score, "class": c, "box": box})

    for i in set(gt_by_img) | set(pred_by_img):
        gts, preds = gt_by_img.get(i, []), sorted(pred_by_img.get(i, []), key=lambda x: x["score"], reverse=True)
        for p in preds:
            best_iou, best_idx = 0.0, -1
            for j, gt in enumerate(gts):
                if not gt["matched"]:
                    iou = compute_iou(p["box"], gt["box"])
                    if iou > best_iou: best_iou, best_idx = iou, j
            if best_iou >= 0.50 and best_idx >= 0:
                cm[gts[best_idx]["class"], p["class"]] += 1
                gts[best_idx]["matched"] = True
            else: cm[n_classes, p["class"]] += 1
        for gt in gts:
            if not gt["matched"]: cm[gt["class"], n_classes] += 1

    def _save_cm(matrix, title, filename, norm):
        fig, ax = plt.subplots(figsize=(6, 5))
        im = ax.imshow(matrix, interpolation="nearest", cmap=plt.cm.Blues)
        plt.colorbar(im, ax=ax)
        ax.set_title(f"{model_name} – {title}", fontsize=12)
        ax.set_xlabel("Predicted"); ax.set_ylabel("Ground Truth")
        ticks = np.arange(len(class_labels))
        ax.set_xticks(ticks); ax.set_yticks(ticks)
        ax.set_xticklabels(class_labels, rotation=45, ha="right", fontsize=9)
        ax.set_yticklabels(class_labels, fontsize=9)
        fmt = ".2f" if norm else "d"
        thresh = matrix.max() / 2.0
        for r_idx in range(matrix.shape[0]):
            for c_idx in range(matrix.shape[1]):
                ax.text(c_idx, r_idx, format(matrix[r_idx, c_idx], fmt), ha="center", va="center",
                        color="white" if matrix[r_idx, c_idx] > thresh else "black", fontsize=8)
        fig.tight_layout(); fig.savefig(os.path.join(output_dir, filename), dpi=150); plt.close(fig)

    _save_cm(cm, "Confusion Matrix", "confusion_matrix.png", False)
    cm_norm = cm.astype(float)
    row_sums = cm_norm.sum(axis=1, keepdims=True); row_sums[row_sums == 0] = 1
    _save_cm(cm_norm / row_sums, "Confusion Matrix (Normalised)", "confusion_matrix_normalized.png", True)
    print(f"  Graficas guardadas en: {output_dir}")