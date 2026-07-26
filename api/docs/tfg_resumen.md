# Resumen Ejecutivo y Métricas Oficiales - TFG Sandra Gregori Fernández

Este documento contiene una síntesis de los datos y resultados fundamentales del Trabajo de Fin de Grado (TFG) titulado **"Detección de Objetos con Vocabulario Abierto (OVOD) en Agricultura de Precisión"**, realizado por **Sandra Gregori Fernández**. 

El objetivo es servir de referencia de alta precisión para el asistente conversacional RAG (Naranjito).

---

## 1. Datos Generales de la Investigación
* **Autora:** Sandra Gregori Fernández
* **Título:** Detección de Objetos con Vocabulario Abierto (OVOD) en Agricultura de Precisión
* **Modelos Evaluados:** OWLv2, YOLO-World, YOLOE, Grounding DINO, SAM 3
* **Caso de Estudio:** Detección de cítricos (naranjas maduras y naranjas verdes o inmaduras) en entornos de cultivo reales en condiciones de iluminación variables.

---

## 2. Tabla Base de Rendimiento Global (Dataset de Test)
Esta tabla resume las métricas oficiales obtenidas en la evaluación de los modelos sobre el dataset global unificado:

| Modelo | Precision | Recall | F1-Score | mAP@50 | mAP@50-95 | Velocidad (FPS) | Enfoque Principal |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **OWLv2** | 0.565 | 0.485 | **0.519** | 0.391 | 0.201 | 0.340 | Máxima Precisión (Inviable en tiempo real) |
| **YOLO-World** | 0.668 | 0.346 | **0.456** | 0.286 | 0.175 | 8.100 | Excelente Balance y Velocidad Promedio |
| **YOLOE** | 0.662 | 0.338 | **0.447** | 0.277 | 0.166 | **8.990** | Máxima Velocidad (Tiempo Real en Edge) |
| **Grounding DINO** | 0.387 | 0.286 | **0.311** | 0.150 | 0.083 | 1.790 | Detector basado en query lingüístico descriptivo |
| **SAM 3** | 0.292 | 0.103 | **0.150** | 0.065 | 0.017 | 4.190 | Segmentación generalista (Bajo rendimiento en cítricos) |

---

## 3. Estrategias de Formulación de Prompts (Prompting Engineering)
Para los modelos basados en vocabulario abierto (OVOD), se evaluaron 6 estrategias de prompts diferentes en inglés para comprobar cómo afecta el lenguaje al reconocimiento de objetos:

| ID | Estrategia de Prompting | Texto del Prompt Utilizado | Descripción / Propósito |
| :--- | :--- | :--- | :--- |
| **P1** | Básicos de Clase | `['orange', 'green orange']` | Nombres directos de clases sin adjetivos adicionales. |
| **P2** | Estado de Maduración | `['ripe orange', 'unripe orange']` | Especificación semántica del estado fenológico de la fruta. |
| **P3** | Identificador Botánico | `['ripe orange citrus fruit']` | Denominación taxonómica del fruto. |
| **P4** | Descriptor Geométrico | `['spherical orange', 'oval lemon']` | Incorporación de la morfología espacial característica. |
| **P5** | Contexto de Escena | `['spherical ripe orange on a tree']` | Integración del entorno natural donde se encuentra el fruto. |
| **P6** | Enfoque de Exclusión | `['orange, not a leaf, not a branch']` | Filtros de exclusión explícitos mediante negación lingüística. |

---

## 4. Conclusiones y Retos Técnicos Identificados

### A. El Desafío de las Naranjas Verdes
* **Camuflaje Cromático:** Las naranjas verdes (o inmaduras) presentan un F1-score significativamente más bajo en comparación con las naranjas maduras. Esto se debe a que comparten el mismo rango cromático (color verde) de las hojas del árbol.
* **Reflejos Especulares (Leaf Specularities):** La luz del sol directa sobre las hojas brillantes genera reflejos y brillos de luz que simulan formas circulares de color verde claro, induciendo a errores de falsos positivos (detección errónea de hojas/reflejos como si fuesen naranjas inmaduras).
* **Oclusiones:** El follaje denso tapa físicamente los frutos, dificultando su detección visual por cualquier modelo supervisado o de vocabulario abierto.

### B. Compromiso entre Precisión y Velocidad (Trade-offs)
* **OWLv2** (basado en Vision Transformers - ViT) obtiene la puntuación de detección y F1-score más altos del estudio, pero su complejidad hace que funcione a solo 0.34 FPS, haciéndolo inadecuado para su montaje en vehículos agrícolas autónomos.
* **YOLO-World** y **YOLOE** demuestran un rendimiento excelente corriendo a más de 8 FPS, lo que permite su despliegue en tiempo real en dispositivos embebidos localizados en el campo ("Edge Computing").

### C. La Técnica de Tiling (Procesamiento por Parches)
* Aunque la técnica de **Tiling** (dividir la imagen original en parches o cuadrículas solapadas más pequeñas) se planteó inicialmente para mejorar la detección de frutos pequeños y lejanos, **se determinó que no fue viable (falló) en esta investigación** debido a tres limitaciones críticas:
  1. **Pérdida de Contexto Global (Aumento de Falsos Positivos):** Al recortar la imagen en parches independientes, las redes OVOD pierden la información del entorno completo de la planta. Esto provoca que el modelo confunda formas circulares de hojas secas, sombras y reflejos verdes en el follaje con naranjas reales, **disparando drásticamente el número de errores (Falsos Positivos - FP)** y arruinando la precisión global.
  2. **Elevado Coste Computacional (Pérdida de Tiempo Real):** El procesamiento secuencial de cada parche multiplica el tiempo total de inferencia. Modelos veloces como YOLO-World (8.10 FPS) o YOLOE (8.99 FPS) pierden sus propiedades en tiempo real y caen a velocidades de procesamiento inviables para vehículos autónomos en campo.
  3. **Detecciones Duplicadas en el Solape:** Los frutos situados en los bordes divisorios de los parches son detectados por duplicado o fragmentados en mitades, lo que induce a errores graves en la estimación del conteo total del cultivo.
