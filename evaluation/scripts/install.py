import os
import platform
import subprocess
import sys

def detect_environment():
    """Detecta el sistema operativo y el hardware disponible."""
    os_name = platform.system()
    print(f" Sistema Operativo detectado: {os_name}")

    if os_name == "Darwin":
        print(" Hardware: Apple Silicon / Intel Mac detectado.")
        return "mac"

    try:
        result = subprocess.run(
            ["nvidia-smi", "--query-gpu=name", "--format=csv,noheader"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        gpu_name = result.stdout.strip().lower()
        print(f" Tarjeta gráfica detectada: {result.stdout.strip()}")
        
        if "rtx 50" in gpu_name or "blackwell" in gpu_name:
            return "cu129"
        else:
            return "cu124"
            
    except (subprocess.SubprocessError, FileNotFoundError):
        print(" Hardware: No se detectó GPU NVIDIA. Configurando modo CPU.")
        return "cpu"

def main():
    os.makedirs("./data/dataset-naranjas/valid/images", exist_ok=True)
    os.makedirs("./data/dataset-naranjas/valid/labels", exist_ok=True)
    os.makedirs("./data/dataset-naranjas/test/images", exist_ok=True)
    os.makedirs("./data/dataset-naranjas/test/labels", exist_ok=True)
    
    os.makedirs("./data/dataset-limones/test/images", exist_ok=True)
    os.makedirs("./data/dataset-limones/test/labels", exist_ok=True)
    
    os.makedirs("./data/dataset-unificado/test/images", exist_ok=True)
    os.makedirs("./data/dataset-unificado/test/labels", exist_ok=True)
    
    os.makedirs("./weights/hf_cache", exist_ok=True)
    os.makedirs("./results", exist_ok=True)
    print("="*50)
    print("   ASISTENTE DE INSTALACIÓN")
    print("="*50)
    
    env_type = detect_environment()
    
    if env_type == "cpu" or env_type == "mac":
        torch_cmd = [sys.executable, "-m", "pip", "install", "torch", "torchvision", "torchaudio"]
    else:
        index_url = f"https://download.pytorch.org/whl/{env_type}"
        torch_cmd = [
            sys.executable, "-m", "pip", "install", 
            "torch", "torchvision", "torchaudio", 
            "--index-url", index_url, 
            "--no-cache-dir"
        ]
    
    print(f"\n[1/2] Instalando la suite de PyTorch adecuada para tu entorno ({env_type.upper()})...")
    subprocess.run(torch_cmd, check=True)
    
    print("\n[2/2] Instalando librerías secundarias del proyecto...")
    requirements_cmd = [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"]
    subprocess.run(requirements_cmd, check=True)
    
    print("\n ¡CONFIGURACIÓN COMPLETADA CON ÉXITO!")
    print("El entorno se ha adaptado a tu hardware. Ya puedes ejecutar 'python evaluate.py'.")

if __name__ == "__main__":
    main()