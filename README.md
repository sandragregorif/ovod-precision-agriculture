# Detección de Objetos de Vocabulario Abierto (OVOD) en Agricultura de Precisión

Este repositorio contiene los scripts desarrollados para respaldar la evaluación y comparativa de resultados, así como la implementación de una demostración web interactiva (frontend de visualización de métricas y backend conversacional RAG), pertenecientes al Trabajo de Fin de Grado (TFG) sobre detección de objetos de vocabulario abierto (OVOD) en **agricultura de precisión** (detección de naranjas y limones).

## Requisitos Previos y Clonación

Antes de comenzar, asegúrate de cumplir con los siguientes requisitos en tu máquina local:
* **Git** (para control de versiones y clonado)
* **Python 3.11+** (para despliegue local de la demo y los scripts)
* **Docker** (para despliegue e inicio automatizado por contenedores)

Para empezar, abre una terminal, clona el repositorio y sitúate dentro de la carpeta raíz del proyecto:

```bash
git clone https://github.com/sandragregorif/ovod-precision-agriculture.git
cd ovod-precision-agriculture
```

## Acceso a la Demo en Vivo (Despliegue Híbrido: GitHub Pages + Google Cloud)

La demostración interactiva del proyecto integra ambos sistemas en un **despliegue híbrido**:
* **Frontend (Interfaz de Usuario):** Alojado públicamente en **GitHub Pages**.
* **Backend (Servidor API RAG):** Desplegado de manera serverless sobre **Google Cloud Platform (GCP - Cloud Run)**.

> **[ACCEDER A LA DEMO WEB INTERACTIVA](https://sandragregorif.github.io/ovod-precision-agriculture/)** : Portal web interactivo para explorar las comparativas de modelos, visualizar las detecciones, consultar métricas de precisión/recall y chatear en tiempo real con el asistente conversacional **Naranjito**.

## Demo Web Interactiva (Dashboard y Chatbot RAG)

Además del pipeline de evaluación en consola CLI, el repositorio cuenta con una interfaz gráfica y un asistente inteligente de visión y lenguaje que enlazan el frontend (React) con el backend (FastAPI).

### Propósito de la Demo
* **Backend API (`api/`):** Servidor rápido basado en **FastAPI** y **LangChain** que expone un endpoint vectorial alimentado por embeddings de Hugging Face (`multilingual-e5-small`) y LLMs (**Gemma 4 31B** a través de **Ollama Cloud**) consultando la memoria del TFG y la guía de funcionamiento de la demo indexadas sobre Pinecone. Soporta el chat del asistente **Naranjito**.
* **Frontend Dashboard (`web/`):** Cliente web interactivo basado en **React** y **Vite**, servido por producción a través de **Nginx**. Permite comparar las predicciones visuales de los modelos frente al etiquetado real (*Ground Truth*), analizar métricas por imagen y chatear con la API del asistente.

### Ejecución Local de la Demo Completa

> **Recomendación:** Para una experiencia inmediata libre de configuraciones de bases de datos vectoriales, APIs externas o contenedores locales, se aconseja acceder directamente a la **[Demo Web en Vivo](https://sandragregorif.github.io/ovod-precision-agriculture/)**.

Si deseas correr toda la infraestructura del panel web (Frontend + Backend) de forma local y automatizada en tu máquina, puedes hacerlo desde la raíz del proyecto usando Docker Compose.

1. **Variables de entorno:** Desde la raíz del proyecto, crea el archivo `./api/.env` agregando tus credenciales de servicios externos:
   ```env
   HUGGINGFACEHUB_API_TOKEN=tu_token_de_huggingface
   PINECONE_API_KEY=tu_api_key_de_pinecone
   PINECONE_INDEX_NAME=ovod-tfg
   OLLAMA_API_KEY=tu_api_key_de_ollama
   OLLAMA_BASE_URL=https://ollama.com/v1
   ```

2. **Indexación de los Documentos en Pinecone:**
   El repositorio ya incluye directamente el contenido completo del TFG estructurado en Markdown (`api/docs/tfg.md`), el resumen de métricas oficiales del TFG en español (`api/docs/tfg_resumen.md`) y la guía de la demo interactiva (`api/docs/guia_demo.md`). De esta forma, la base de datos se indexa de forma limpia sin ruidos de formato de página o tablas inválidas.
   * **Lectura del TFG (Opcional):** Si deseas leer o descargar el manuscrito de investigación original en PDF, puedes acceder a él en [este enlace de Google Drive](https://drive.google.com/file/d/1J17j2dLcabe-jr5-lRW-YQ6UqXoOMr-0/view?usp=sharing).
   * Regístrate gratis en [Pinecone](https://www.pinecone.io/) y obtén tu API Key.
   * Crea un índice con el nombre que prefieras (por ejemplo, `ovod-tfg`) seleccionando la opción de configuración personalizada (*custom setup*). **Muy importante:** Este nombre de índice debe coincidir exactamente con el valor definido en `PINECONE_INDEX_NAME` en tu archivo `.env`. Configura el índice con una dimensión de **384** (la dimensión del modelo de embeddings del proyecto `multilingual-e5-small`) y la métrica de distancia **Cosine**.
   * Levanta un entorno virtual local e instala las dependencias de la carpeta `api/` para lanzar el script de indexación automática:
     ```bash
     cd api
     python -m venv venv
     # En macOS / Linux:
     source venv/bin/activate
     # En Windows (PowerShell):
     .\venv\Scripts\activate
     
     pip install -r requirements.txt
     python app/index_data.py
     ```
     *Nota:* Tras la ejecución exitosa del script, los vectores con el contenido del TFG se habrán subido a tu base de datos de Pinecone y estarán listos para las consultas del chatbot. A continuación, vuelve al directorio raíz (`cd ..`).

3. **Ejecutar con Docker Compose:** Desde el directorio raíz del proyecto (`ovod-precision-agriculture`), ejecuta:
   ```bash
   docker compose up -d --build
   ```
   Una vez listos los contenedores:
   * **Frontend (Dashboard):** Accede mediante navegador web en [http://localhost:8501](http://localhost:8501)
   * **Backend (API / Swagger Docs):** Consulta y prueba los endpoints en [http://localhost:8000/docs](http://localhost:8000/docs)

## Guía Secuencial de Ejecución (Pipeline de Evaluación CLI)

Este pipeline permite ejecutar pruebas cuantitativas de rendimiento entre modelos como **YOLO-World (v2)**, **YOLOE**, **OWLv2**, **Grounding DINO** y **SAM 3** a través de la terminal o consola.

### 1. Entrar al directorio de evaluación
Todas las operaciones relativas al pipeline de consola CLI se realizan dentro de la subcarpeta `evaluation`:
```bash
cd evaluation
```

### 2. Obtención y Configuración de los Datasets

La evaluación utiliza tres conjuntos de datos agrícolas alojados en Roboflow Universe en formato **YOLOv8**:

* 🍊 **Dataset Naranjas:** [Roboflow Universe - Dataset Naranjas](https://universe.roboflow.com/sandragregorif/dataset-naranjas)
* 🍋 **Dataset Limones:** [Roboflow Universe - Dataset Limones](https://universe.roboflow.com/sandragregorif/dataset-limones-ymuhf)
* 🔄 **Dataset Unificado:** [Roboflow Universe - Dataset Unificado](https://universe.roboflow.com/sandragregorif/dataset-unificado-3hthh)

### Descarga Automatizada de los Datasets (Recomendado)

El script `download_data.py` (ubicado en `scripts/download_data.py` dentro de la carpeta `evaluation`) descarga y estructura los tres datasets automáticamente usando el SDK de Roboflow. Necesitas tu Private API Key gratuita, disponible en el [panel de configuración de Roboflow](https://app.roboflow.com/settings/api).

Una vez situado en el directorio `evaluation/`, ejecuta el script y te pedirá la clave por consola:

```bash
python scripts/download_data.py
# >> Introduce tu Roboflow Private API Key: ********
```

***Nota: Si aún no has instalado las dependencias del archivo `requirements.txt` (ubicado dentro de la carpeta `evaluation/`) en tu entorno virtual, deberás ejecutar el siguiente comando en la terminal:***
```
pip install roboflow
```

### Descarga Manual de los Datasets
Si prefieres descargarlos manualmente, accede a los enlaces de Roboflow anteriores, descarga cada dataset en formato **YOLOv8** y colócalos dentro del subdirectorio `evaluation/` siguiendo esta estructura de carpetas:
```text
evaluation/
└── data/
    ├── dataset-limones/
    │   └── test/
    │       ├── images/
    │       └── labels/
    ├── dataset-naranjas/
    │   ├── valid/
    │   │   ├── images/
    │   │   └── labels/
    │   └── test/
    │       ├── images/
    │       └── labels/
    └── dataset-unificado/
        └── test/
            ├── images/
            └── labels/
```

### 3. Despliegue y Ejecución

Al ejecutar el proyecto se crean automáticamente los siguientes directorios dentro de la carpeta `evaluation/`:
* `data/` — Datasets (Creado en el paso previo)
* `weights/` — Pesos de los modelos (se descargan en la primera ejecución):
  * Archivos `.pt` de Ultralytics (YOLO-World, YOLOE, SAM 3).
  * Caché `hf_cache/` de Hugging Face (Grounding DINO, OWLv2).
* `results/` — Imágenes anotadas y métricas

A continuación, se muestran dos distintas maneras de instalar las dependencias y preparar el proyecto. Elige A o B según tus preferencias.

### Opción A: Despliegue Local (Entorno Virtual)

1. Entra en el directorio de evaluación, crea y activa el entorno virtual (si no lo has hecho ya):
   ```bash
   cd evaluation
   python -m venv venv
   # En macOS / Linux:
   source venv/bin/activate
   # En Windows (PowerShell):
   .\venv\Scripts\activate
   ```
   > ⚠️ **Windows (PowerShell):** Si te sale el error `UnauthorizedAccess`, ejecuta primero:
   > ```powershell
   > Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
   > ```

2. Instala las dependencias (el asistente detecta tu hardware automáticamente):
   ```bash
   python scripts/install.py
   ```
   Si prefieres hacerlo a mano:
   * *Solo CPU / macOS:*
     ```bash
     pip install torch torchvision torchaudio
     ```
   * *GPU NVIDIA Estándar (RTX Serie 20, 30, 40):*
     ```bash
     pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
     ```
   * *GPU NVIDIA Blackwell (RTX Serie 50):*
     ```bash
     pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu129 --no-cache-dir
     ```
   * *Resto de dependencias (obligatorio):*
     ```bash
     pip install -r requirements.txt
     ```

3. Tras tener los datasets y todas las dependencias instaladas, ya podemos ejecutar el proyecto:
   ```bash
   python evaluate.py
   ```

### Opción B: Despliegue con Docker

1. Entra en la carpeta de evaluación en caso de no estar en ella:
   ```bash
   cd evaluation
   ```

2. Construye la imagen (ejecuta desde el directorio `evaluation/`):
   ```bash
   docker build -t ovod-tfg-pipeline .
   ```

3. Ejecuta el contenedor:
   * *Con GPU NVIDIA (ejecutando desde el directorio `evaluation/`):*
     ```bash
     docker run --gpus all -it `
       -v ${PWD}/data:/app/data `
       -v ${PWD}/results:/app/results `
       -v ${PWD}/weights:/app/weights `
       ovod-tfg-pipeline
     ```
   * *Sin GPU (CPU). Tarjetas AMD o dispositivos Mac (ejecutando desde el directorio `evaluation/`):*
     ```bash
     docker run -it `
       -v ${PWD}/data:/app/data `
       -v ${PWD}/results:/app/results `
       -v ${PWD}/weights:/app/weights `
       ovod-tfg-pipeline
     ```

> ⚠️ **Problemas con GPU en Docker (Windows / WSL2):**
> Si te aparece el error `could not select device driver "" with capabilities: [[gpu]]`:
> 1. **Docker Desktop en Windows:** Ejecuta el comando sin anteponer `wsl` y comprueba que tienes activa la opción *"Use the WSL 2 based engine"* en Docker Desktop.
> 2. **Docker nativo en WSL2:** Instala el **NVIDIA Container Toolkit**:
> ```bash
> curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg; \
> curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
> sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
> sudo nvidia-container-toolkit runtime configure --runtime=docker
> sudo service docker restart
> ```

## Menú Interactivo del Pipeline CLI

Al arrancar `evaluate.py` se abre un menú interactivo en terminal con 5 bloques de configuración:
1. **Modelo:** YOLO-World, YOLOE, OWLv2, Grounding DINO o SAM 3 (con selección de escala: Small, Medium, Large, Extra-large. Esto varía según el modelo seleccionado).
2. **Dataset y Subset:** Naranjas, Limones o Unificado (`valid` o `test`).
3. **Estrategia de Prompts (P1 a P6):** Nivel de abstracción del lenguaje para evaluar la respuesta del codificador de texto (descriptores morfológicos, de estado, botánicos, espaciales o de exclusión).
4. **Tiling:** Inferencia por parches solapados para la detección precisa de frutos pequeños o muy agrupados en imágenes extensas de dosel vegetal.
5. **Umbrales:** Ajuste dinámico de los coeficientes de NMS IoU y Score Threshold.

Los resultados (mAP@50, mAP@50:95, precisión, recall e imágenes visuales anotadas) se vuelcarán en la carpeta `results/`.

## Autoría e Información Institucional
* **Proyecto:** Trabajo de Fin de Grado (TFG) - Grado en Ingeniería Informática.
* **Institución:** Universitat Politècnica de València (UPV).
* **Autora:** Sandra Gregori Fernández.
* **Año:** 2026.
