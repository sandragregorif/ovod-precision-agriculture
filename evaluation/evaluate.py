import os
import glob
import argparse
import sys
import time
from PIL import Image
from src.utils import *
from src.evaluators import *

# Umbrales estándar por defecto para todos los modelos en el TFG
DEFAULT_NMS = 0.50
DEFAULT_CONF = 0.01

def get_input(prompt_text, default=None):
    """
    Lee la entrada de consola y comprueba si el usuario quiere retroceder.
    Retorna "BACK" si detecta el comando de retroceso 'b'.
    """
    val = input(prompt_text).strip()
    if val.lower() == 'b':
        return "BACK"
    if not val and default is not None:
        return default
    return val

def run_wizard():
    print("\n" + "="*50)
    print("      ASISTENTE DE EVALUACIÓN INTERACTIVO - TFG")
    print("  (Escribe 'b' en cualquier paso para retroceder)")
    print("="*50)
    
    state = 1
    
    # Variables de estado
    op_m, m_sel, v_sel = None, None, None
    d_sel, dataset, subset = None, None, "test"
    p_lvl = None
    use_tiling, tile_size, tile_overlap = False, 1280, 256
    nms, conf = None, None

    while True:
        # -------------------------------------------------------------------
        # PASO 1: SELECCIÓN DE MODELO
        # -------------------------------------------------------------------
        if state == 1:
            print("\n[1] SELECCIÓN DE MODELO:")
            print("    1. YOLO-World | 2. YOLOE | 3. OWLv2 | 4. Grounding DINO | 5. SAM 3")
            op_m = get_input(">> Opción: ")
            if op_m == "BACK":
                print("    * Ya estás en el primer paso del asistente.")
                continue
            
            if op_m not in ["1", "2", "3", "4", "5"]:
                print("    * Opción no válida. Inténtalo de nuevo.")
                continue
            
            if op_m == "1":
                m_sel = "yolo_world"
                v_ans = get_input("    [YOLO-World] Ver (1:s, 2:m, 3:l, 4:x) [defecto: 4]: ", "4")
                if v_ans == "BACK":
                    continue  # Reinicia el paso 1
                v_sel = {"1":"s", "2":"m", "3":"l", "4":"x"}.get(v_ans, "x")
                
            elif op_m == "2":
                m_sel = "yoloe"
                print("\n    [YOLOE] SELECCIÓN DE FAMILIA:")
                print("    1. Familia v8 (Tallas: s, m, l)")
                print("    2. Familia 11 (Tallas: s, m, l)")
                print("    3. Familia 26 (Tallas: n, s, m, l, x)")
                
                fam_idx = get_input("    >> Seleccione familia (Escriba 1, 2 o 3) [defecto: 1]: ", "1")
                if fam_idx == "BACK":
                    continue
                
                fam = {"1": "v8", "2": "11", "3": "26"}.get(fam_idx, "v8")
                
                print(f"\n    [YOLOE {fam}] SELECCIÓN DE TAMAÑO:")
                if fam in ["v8", "11"]:
                    print("    1. s (Small) | 2. m (Medium) | 3. l (Large)")
                    tam_idx = get_input("    >> Seleccione tamaño (Escriba 1, 2 o 3) [defecto: 2]: ", "2")
                    if tam_idx == "BACK":
                        continue
                    tam = {"1": "s", "2": "m", "3": "l"}.get(tam_idx, "m")
                else:  # Familia 26
                    print("    1. n (Nano) | 2. s (Small) | 3. m (Medium) | 4. l (Large) | 5. x (Extra Large)")
                    tam_idx = get_input("    >> Seleccione tamaño (Escriba 1, 2, 3, 4 o 5) [defecto: 3]: ", "3")
                    if tam_idx == "BACK":
                        continue
                    tam = {"1": "n", "2": "s", "3": "m", "4": "l", "5": "x"}.get(tam_idx, "m")
                
                v_sel = f"{fam}{tam}"
                
            elif op_m == "4":
                m_sel = "grounding_dino"
                v_ans = get_input("    [DINO] Ver (1:base, 2:tiny) [defecto: 1]: ", "1")
                if v_ans == "BACK":
                    continue
                v_sel = "tiny" if v_ans == "2" else "base"
                
            else:
                m_sel = "sam3" if op_m == "5" else "owlv2"
                v_sel = "default"
            
            state = 2  # Avanza con éxito
            continue

        # -------------------------------------------------------------------
        # PASO 2: SELECCIÓN DE DATASET
        # -------------------------------------------------------------------
        elif state == 2:
            print("\n[2] SELECCIÓN DE DATASET:")
            print("    1. Naranjas | 2. Limones | 3. Unificado")
            d_sel = get_input(">> Opción: ")
            if d_sel == "BACK":
                state = 1  # Retrocede al modelo
                continue
            
            if d_sel not in ["1", "2", "3"]:
                print("    * Opción no válida.")
                continue
            
            dataset = "naranjas" if d_sel == "1" else "limones" if d_sel == "2" else "unificado"
            subset = "test"
            if dataset == "naranjas":
                sub_ans = get_input("    Subset (1:Valid, 2:Test) [defecto: 2]: ", "2")
                if sub_ans == "BACK":
                    continue  # Reinicia el Paso 2
                subset = "valid" if sub_ans == "1" else "test"
                
            state = 3
            continue

        # -------------------------------------------------------------------
        # PASO 3: ESTRATEGIA DE PROMPTS
        # -------------------------------------------------------------------
        elif state == 3:
            print("\n[3] ESTRATEGIA DE PROMPTS (P1-P6):\n")
            print("    1. P1 - Básicos de clase y color")
            print("       Ejemplos: ['orange', 'green orange'] | ['lemon', 'green lemon']\n")
            print("    2. P2 - Estado de maduración explícito")
            print("       Ejemplos: ['ripe orange', 'unripe orange'] | ['ripe lemon', 'unripe lemon']\n")
            print("    3. P3 - Identificador botánico (Citrus Fruit)")
            print("       Ejemplos: ['ripe orange citrus fruit'] | ['green unripe lemon citrus fruit']\n")
            print("    4. P4 - Incorporación de forma geométrica (Esférico / Oval)")
            print("       Ejemplos: ['spherical orange'] | ['oval lemon', 'oval green lemon']\n")
            print("    5. P5 - Contextualización de escena completa (En el árbol)")
            print("       Ejemplos: ['spherical ripe orange citrus fruit on a tree']\n")
            print("    6. P6 - Enfoque de exclusión mediante negaciones")
            print("       Ejemplos: ['orange, not a leaf, not a branch']\n")
            
            p_lvl = get_input(">> Seleccione nivel (Escriba un número del 1 al 6) [defecto: 4]: ", "4")
            if p_lvl == "BACK":
                state = 2  # Retrocede al dataset
                continue
                
            if p_lvl not in ["1", "2", "3", "4", "5", "6"]:
                print("    * Nivel no válido. Inténtalo de nuevo.")
                continue
                
            state = 4
            continue

        # -------------------------------------------------------------------
        # PASO 4: CONFIGURACIÓN DE TILING (PARAMETRIZACIÓN AUTOMÁTICA)
        # -------------------------------------------------------------------
        elif state == 4:
            print("\n[4] CONFIGURACIÓN DE TILING:")
            tile_ans = get_input("    ¿Activar inferencia por parches solapados (Tiling)? (1: Sí, 2: No) [defecto: 2]: ", "2")
            if tile_ans == "BACK":
                state = 3  # Retrocede a la estrategia de prompts
                continue
            
            use_tiling = (tile_ans == "1")
            tile_size = 1280
            tile_overlap = 256
                    
            state = 5
            continue

        # -------------------------------------------------------------------
        # PASO 5: AJUSTE DE UMBRALES
        # -------------------------------------------------------------------
        elif state == 5:
            print("\n[5] AJUSTE DE UMBRALES (Deje en blanco para usar los umbrales estándar):")
            
            nms_ans = get_input(f"    NMS IoU (defecto {DEFAULT_NMS}): ", "")
            if nms_ans == "BACK":
                state = 4  # Retrocede al Tiling
                continue
                
            conf_ans = get_input(f"    Score Threshold (defecto {DEFAULT_CONF}): ", "")
            if conf_ans == "BACK":
                continue  # Reinicia el Paso 5
            
            try:
                nms = float(nms_ans) if nms_ans else DEFAULT_NMS
            except ValueError:
                print(f"    * Valor no válido. Usando predeterminado: {DEFAULT_NMS}")
                nms = DEFAULT_NMS
                
            try:
                conf = float(conf_ans) if conf_ans else DEFAULT_CONF
            except ValueError:
                print(f"    * Valor no válido. Usando predeterminado: {DEFAULT_CONF}")
                conf = DEFAULT_CONF
                
            break

    return m_sel, v_sel, dataset, subset, p_lvl, use_tiling, tile_size, tile_overlap, nms, conf

def main():
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser(description="Evaluación directa vía Terminal para TFG.")
        parser.add_argument("--model", required=True, choices=["yolo_world", "yoloe", "owlv2", "grounding_dino", "sam3"])
        parser.add_argument("--version", default="default", help="Variante del peso (s, m, l, x, base, tiny, etc.)")
        parser.add_argument("--dataset", required=True, choices=["naranjas", "limones", "unificado"])
        parser.add_argument("--subset", default="test", choices=["valid", "test"])
        parser.add_argument("--prompt-level", default="4")
        parser.add_argument("--tiling", action="store_true")
        parser.add_argument("--tile-size", type=int, default=1280)
        parser.add_argument("--tile-overlap", type=int, default=256)
        parser.add_argument("--nms-iou", type=float, default=None)
        parser.add_argument("--score-thresh", type=float, default=None)
        
        args = parser.parse_args()
        m_sel, v_sel, dataset, subset = args.model, args.version, args.dataset, args.subset
        p_lvl, use_tiling, tile_size, tile_overlap = args.prompt_level, args.tiling, args.tile_size, args.tile_overlap
        nms = args.nms_iou if args.nms_iou is not None else DEFAULT_NMS
        conf = args.score_thresh if args.score_thresh is not None else DEFAULT_CONF
    else:
        m_sel, v_sel, dataset, subset, p_lvl, use_tiling, tile_size, tile_overlap, nms, conf = run_wizard()

    # --- CONFIGURACIÓN DE RUTA DEL DATASET ---
    if dataset == "naranjas":
        path = f"./data/dataset-naranjas/{subset}"
        mode = "naranja"
    elif dataset == "limones":
        path = "./data/dataset-limones/test"
        mode = "limon"
    else:
        path = "./data/dataset-unificado/test"
        mode = "unificado"

    # --- COMPROBACIÓN DE SEGURIDAD (RUTAS) ---
    images = glob.glob(os.path.join(path, "images", "*.*"))
    if not images:
        print(f"\nERROR DE RUTA: No se encontró ninguna imagen en la carpeta:")
        print(f"   --> {os.path.abspath(os.path.join(path, 'images'))}")
        print("   Verifica la ortografía de tus carpetas (mayúsculas/minúsculas) o si las fotos están ahí.\n")
        return

    # --- RUTA DE SALIDA REPRESENTATIVA ---
    output_dir = f"./results/{m_sel}_{v_sel}_{dataset}"

    # --- DICCIONARIO DE PROMPTS P1-P6 ---
    temps = {
        "1": {"naranja": ["orange", "green orange"], "limon": ["lemon", "green lemon"], "unificado": ["orange", "green orange", "lemon", "green lemon"]},
        "2": {"naranja": ["ripe orange", "unripe orange"], "limon": ["ripe lemon", "unripe lemon"], "unificado": ["ripe orange", "unripe orange", "ripe lemon", "unripe lemon"]},
        "3": {"naranja": ["ripe orange citrus fruit", "green unripe citrus fruit"], "limon": ["ripe lemon citrus fruit", "green unripe lemon citrus fruit"], "unificado": ["ripe orange citrus fruit", "green unripe citrus fruit", "ripe lemon citrus fruit", "green unripe lemon citrus fruit"]},
        "4": {"naranja": ["spherical orange", "spherical green orange"], "limon": ["oval lemon", "oval green lemon"], "unificado": ["spherical orange", "spherical green orange", "oval lemon", "oval green lemon"]},
        "5": {"naranja": ["spherical ripe orange citrus fruit on a tree", "spherical green unripe citrus fruit on a tree"], "limon": ["oval ripe lemon citrus fruit on a tree", "oval green unripe lemon citrus fruit on a tree"], "unificado": ["spherical ripe orange citrus fruit on a tree", "spherical green unripe citrus fruit on a tree", "oval ripe lemon citrus fruit on a tree", "oval green unripe lemon citrus fruit on a tree"]},
        "6": {"naranja": ["orange, not a leaf, not a branch", "green orange, not a leaf, not a branch"], "limon": ["lemon, not a leaf, not a branch", "green lemon, not a leaf, not a branch"], "unificado": ["orange, not a leaf, not a branch", "green orange, not a leaf, not a branch", "lemon, not a leaf, not a branch", "green lemon, not a leaf, not a branch"]}
    }
    prompts = temps.get(p_lvl, temps["1"])[mode]

    # --- INICIALIZACIÓN DEL EVALUADOR ---
    if m_sel == "yolo_world":
        ev = YoloWorldEvaluator(size=v_sel) 
    elif m_sel == "yoloe":
        ev = YoloeEvaluator(version=v_sel) 
    elif m_sel == "grounding_dino":
        ev = GroundingDinoEvaluator(version=v_sel) 
    elif m_sel == "sam3":
        ev = Sam3Evaluator() 
    else:
        ev = Owlv2Evaluator() 

    # --- EJECUCIÓN DEL PIPELINE ---
    print("\n>>> Lanzando evaluación seleccionada...")
    c_names = {i: p for i, p in enumerate(prompts)}
    c_cols = {0: (255, 0, 0), 1: (0, 200, 0)} if mode == "naranja" else {0: (0, 0, 255), 1: (255, 0, 255)} if mode == "limon" else {0: (255, 0, 0), 1: (0, 200, 0), 2: (0, 0, 255), 3: (255, 0, 255)}
    
    p_tp, p_total, p_raw, p_gt = {i:[] for i in range(len(prompts))}, {i:0 for i in range(len(prompts))}, {i:[] for i in range(len(prompts))}, {i:[] for i in range(len(prompts))}

    total_inference_time = 0.0
    num_images = len(images)

    for img_id, img_p in enumerate(images):
        img = Image.open(img_p).convert("RGB")
        gt = load_groundtruth(get_label_path(img_p, os.path.join(path, "labels")), *img.size) 
        for cid, b in gt: 
            p_total[cid] += 1
            p_gt[cid].append((b, img_id))
        
        # --- MEDICIÓN DEL TIEMPO DE INFERENCIA PURO ---
        start_time = time.time()
        raw_dets = predict_with_tiling(ev, img, c_names, conf, use_tiling=use_tiling, tile_size=tile_size, tile_overlap=tile_overlap) 
        preds = nms_global(raw_dets, nms) 
        end_time = time.time()
        
        total_inference_time += (end_time - start_time)
        # ---------------------------------------------
        
        save_annotated_image(img_p, preds, gt, output_dir, c_names, c_cols) 
        
        for s, cid, b in preds: 
            if cid in p_raw: p_raw[cid].append((s, b, img_id))
        for (s, is_tp), (_, cid, _) in zip(match_predictions_to_gt(preds, gt, 0.5), sorted(preds, key=lambda x: -x[0])): 
            if cid in p_tp: p_tp[cid].append((s, is_tp))

    # --- IMPRIMIR TABLA DE MÉTRICAS ---
    print_metrics(m_sel, p_tp, p_total, p_raw, p_gt, c_names) 

    # --- DESGLOSE DE TIEMPOS Y RENDIMIENTO ---
    if total_inference_time > 0:
        avg_time = total_inference_time / num_images
        fps = num_images / total_inference_time
        print(f"RENDIMIENTO DE INFERENCIA:")
        print(f"   - Imágenes evaluadas: {num_images}")
        print(f"   - Tiempo total invertido: {total_inference_time:.3f} segundos")
        print(f"   - Tiempo medio por imagen: {avg_time:.3f} segundos")
        print(f"   - Tasa de procesamiento (FPS): {fps:.2f} frames/segundo")
        print(f"{'═' * 78}\n")

    # --- IMPRIMIR CURVAS Y MATRICES ---
    plot_metrics(m_sel, p_tp, p_total, output_dir, c_names, p_raw, p_gt) 

if __name__ == "__main__":
    main()