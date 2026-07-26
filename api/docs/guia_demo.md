# Guía de Uso e Interfaz de la Aplicación Demo (TFG Citricultura)

## Información General
La aplicación web interactiva está desarrollada en Streamlit y se divide en dos secciones principales accesibles desde la barra lateral:
1. **Comparador Visual de Modelos OVOD**
2. **Chatbot Asistente (Naranjito 🍊)**

---

## Seccion 1: Comparador Visual

### ¿Cómo funciona?
El comparador utiliza un conjunto de test estático con inferencias precomputadas para garantizar cero coste computacional y una respuesta instantánea. Dispone de 5 imágenes de ejemplos
reales obtenido del conjunto de test utilizado en el TFG.

### Funcionalidades disponibles:
- **Selección de tipo de comparativa:** El usuario puede elegir entre comparar la imagen real (Ground Truth) con las detecciones realizadas por un modelo de vocabulario abierto evaluado en el TFG (Grounding DINO, OWLv2, Yolo-World, YOLOE o SAM3) o bien comparar directamente las detecciones realizadas por dos arquitecturas de vocabulario abierto sobre la misma imagen (las arquitecturas mencionadas anteriormente).
- **Comparativa Ground Truth vs. modelo de vocabulario abierto**: Si el usuario selecciona esta opción en la barra lateral, se le mostrará un desplegable con todas las arquitecturas de vocabulario abierto disponibles. Podrá seleccionar en cualquier momento cualquiera. En la pantalla principal, a la izquierda se mostrará la imagen con sus respectivas anotaciones originales. A la derecha, se mostrará la imagen inferida por el modelo de vocabulario abierto seleccionado.
- **Comparativa modelo de vocabulario abierto vs. modelo de vocabulario abierto**: Si el usuario selecciona esta opción en la barra lateral, se le mostrarán dos desplegables con todas las arquitecturas de vocabulario abierto disponibles (No se podrá seleccionar la misma arquitectura en ambos desplegables). Podrá seleccionar en cualquier momento cualquiera. En la pantalla principal, a la izquierda se mostrará la imagen con las detecciones realizadas por el modelo seleccionado en el desplegable A. A la derecha, se mostrará la imagen inferida por el modelo de vocabulario abierto seleccionado en el desplegable B.
- **Leyendas de colores de bounding boxes**: Los colores de las anotaciones representan las siguientes clases: Las anotaciones de color rojo representan la clase "Naranja", las anotaciones de color azul representan la clase "Naranja Verde" y finalmente las blancas representan la etiqueta original (el Ground Truth de la imagen).
-- **Estadísticas globales**: Encima de cada imagen que represente inferencia de una arquitectura de vocabulario abierto, se mostrará un resumen de las estadísticas globales de la imagen: Velocidad del modelo seleccionado, total de detecciones realizada sobre la imagen, total de detecciones que fueron correctas y total de detecciones que fueron erróneas.
-- **Estadísticas por clase**: Debajo de cada imagen que represente inferencia de una arquitectura de vocabulario abierto, se mostrará un resumen de las estadísticas por clases ("Naranja" y "Naranja Verde") de la imagen: Velocidad del modelo seleccionado, total de detecciones realizada sobre la imagen (por clase), total de detecciones que fueron correctas (por clase) y total de detecciones que fueron erróneas (por clase).


---

## Sección 2: Chatbot Naranjito 🍊

### ¿Cómo funciona?
Naranjito es un chatbot RAG (Retrieval-Augmented Generation) integrado con Pinecone y modelos abiertos de Hugging Face (`Qwen2.5-7B-Instruct`).

### Qué se le puede preguntar a Naranjito:
- Dudas sobre cualquier contenido relevante de la memoria del TFG.
- Resultados cuantitativos del TFG (métricas, comparativa de velocidad vs precisión).
- Ayuda sobre cómo navegar o usar la propia demo visual.