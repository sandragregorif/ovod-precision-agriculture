import os
import sys
import time

try:
    from roboflow import Roboflow
except ImportError:
    print("\n[X] Error: La librería 'roboflow' no está instalada en el entorno.")
    print("Por favor, asegúrate de tenerla instalada en tu máquina local o entorno virtual mediante:\n")
    print("pip install roboflow\n")
    print("O bien, instala directamente todas las dependencias:\n")
    print("pip install -r requirements.txt\n")
    sys.exit(1)

def main():
    print("="*65)
    print("      ASISTENTE DE DESCARGA AUTOMÁTICA DE DATASETS")
    print("="*65)
    print("Para descargar los datos necesitas tu Private API Key de Roboflow.")
    print("Puedes obtenerla en: https://app.roboflow.com/settings/api")
    print("-"*65)
    
    # Solicitar la clave de forma segura en la terminal
    api_key = input(">> Introduce tu Roboflow Private API Key: ").strip()
    if not api_key:
        print("[X] Error: El API Key no puede estar vacío.")
        sys.exit(1)
        
    try:
        print("\n[1/4] Autenticando con el servidor de Roboflow...")
        rf = Roboflow(api_key=api_key)
    except Exception as e:
        print(f"[X] Fallo en la autenticación: {e}")
        sys.exit(1)

    # Configuración de los proyectos mapeados desde Roboflow Universe
    # Se fuerza la descarga estructurada en formato 'yolov8' directo a su destino
    datasets_pipeline = [
        {
            "project_id": "dataset-naranjas",
            "version": 1,
            "target_dir": "./data/dataset-naranjas"
        },
        {
            "project_id": "dataset-limones-ymuhf",
            "version": 1,
            "target_dir": "./data/dataset-limones"
        },
        {
            "project_id": "dataset-unificado-3hthh",
            "version": 1,
            "target_dir": "./data/dataset-unificado"
        }
    ]

    # Asegurar que el contenedor base 'data/' existe
    os.makedirs("./data", exist_ok=True)

    print("\n[2/4] Iniciando descarga secuencial de los datasets...")
    
    workspace_name = "sandragregorif"

    datasets_fallidos = []
    max_retries = 3
    
    for idx, ds in enumerate(datasets_pipeline, start=1):
        p_id = ds["project_id"]
        version = ds["version"]
        dest = ds["target_dir"]
        
        print(f"\n[{idx}+3] Descargando: {p_id} (v{version}) -> Destino: {dest}")

        exito_dataset = False

        for intento in range(1, max_retries + 1):
            try:
                if intento > 1:
                    print(f"Reintentando descarga ({intento}/{max_retries})...")
                
                project = rf.workspace(workspace_name).project(p_id)
                project.version(version).download("yolov8", location=dest)
                
                print(f" [✓] Completado con éxito: {p_id}")
                exito_dataset = True
                break  
                
            except Exception as e:
                print(f"Error en intento {intento}/{max_retries} para {p_id}: {e}")
                if intento < max_retries:
                    time.sleep(3)
        
        if not exito_dataset:
            print(f" [X] Error crítico: No se pudo descargar {p_id} tras {max_retries} intentos.")
            datasets_fallidos.append(p_id)

    print("\n" + "="*65)
    if datasets_fallidos:
        print(" PROCESO FINALIZADO CON ERRORES")
        print(f" No se pudieron descargar los siguientes datasets: {', '.join(datasets_fallidos)}")
        print(" Por favor, comprueba tu conexión e inténtalo de nuevo.")
        print("="*65 + "\n")
        sys.exit(1)  
    else:
        print(" ¡PROCESO DE AUTOMATIZACIÓN COMPLETADO CON ÉXITO!")
        print(" Toda la estructura de datos está lista en formato YOLOv8.")
        print("="*65 + "\n")

if __name__ == "__main__":
    main()