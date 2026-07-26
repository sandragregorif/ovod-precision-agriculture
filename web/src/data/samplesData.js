export const ALL_MODELS = [
  "YOLO-World",
  "YOLOE",
  "OWLv2",
  "Grounding DINO",
  "SAM 3"
];

export const MODEL_METADATA = {
  "Ground Truth": {
    filename: "original.jpg",
    architecture: "Anotación Manual de Campo",
    fps: "Real",
    badgeColor: "#10B981",
    prompt: "N/A (Etiqueta Real)"
  },
  "YOLO-World": {
    filename: "yolo_world.jpg",
    fps: 8.10,
    architecture: "YOLO + CLIP Text Encoder",
    prompt: "spherical orange | spherical green orange",
    badgeColor: "#F97316"
  },
  "YOLOE": {
    filename: "yoloe.jpg",
    fps: 8.99,
    architecture: "YOLOE Open-Vocab Real-time",
    prompt: "spherical orange | spherical green orange",
    badgeColor: "#06B6D4"
  },
  "OWLv2": {
    filename: "owlv2.jpg",
    fps: 0.34,
    architecture: "OWL-ViT Vision Transformer",
    prompt: "orange | green orange",
    badgeColor: "#EC4899"
  },
  "Grounding DINO": {
    filename: "grounding_dino.jpg",
    fps: 1.79,
    architecture: "DINO + Text Cross-Attention",
    prompt: "spherical ripe orange citrus fruit on a tree | spherical green unripe citrus fruit on a tree",
    badgeColor: "#F59E0B"
  },
  "SAM 3": {
    filename: "sam3.jpg",
    fps: 4.19,
    architecture: "Segment Anything Model 3",
    prompt: "spherical orange | spherical green orange",
    badgeColor: "#8B5CF6"
  }
};

export const SAMPLES_LIST = [
  { id: "sample_01", label: "Imagen 01" },
  { id: "sample_02", label: "Imagen 02" },
  { id: "sample_03", label: "Imagen 03" },
  { id: "sample_04", label: "Imagen 04" },
  { id: "sample_05", label: "Imagen 05" }
];

export const SAMPLES_METRICS = {
  "sample_01": {
    "Grounding DINO": {
      total_detections: 79,
      correct_detections: 25,
      erroneous_detections: 54,
      by_class: {
        Naranja: { total: 30, correct: 25, erroneous: 5, precision: 83 },
        NaranjaVerde: { total: 49, correct: 0, erroneous: 49, precision: 0 }
      }
    },
    "YOLO-World": {
      total_detections: 54,
      correct_detections: 49,
      erroneous_detections: 5,
      by_class: {
        Naranja: { total: 53, correct: 49, erroneous: 4, precision: 92 },
        NaranjaVerde: { total: 1, correct: 0, erroneous: 1, precision: 0 }
      }
    },
    "YOLOE": {
      total_detections: 54,
      correct_detections: 52,
      erroneous_detections: 2,
      by_class: {
        Naranja: { total: 54, correct: 52, erroneous: 2, precision: 96 },
        NaranjaVerde: { total: 0, correct: 0, erroneous: 0, precision: 0 }
      }
    },
    "SAM 3": {
      total_detections: 52,
      correct_detections: 4,
      erroneous_detections: 48,
      by_class: {
        Naranja: { total: 52, correct: 4, erroneous: 48, precision: 8 },
        NaranjaVerde: { total: 0, correct: 0, erroneous: 0, precision: 0 }
      }
    },
    "OWLv2": {
      total_detections: 112,
      correct_detections: 81,
      erroneous_detections: 31,
      by_class: {
        Naranja: { total: 112, correct: 81, erroneous: 31, precision: 72 },
        NaranjaVerde: { total: 0, correct: 0, erroneous: 0, precision: 0 }
      }
    }
  },
  "sample_02": {
    "Grounding DINO": { total_detections: 62, correct_detections: 21, erroneous_detections: 41, by_class: { Naranja: { total: 25, correct: 21, erroneous: 4, precision: 84 }, NaranjaVerde: { total: 37, correct: 0, erroneous: 37, precision: 0 } } },
    "YOLO-World": { total_detections: 48, correct_detections: 44, erroneous_detections: 4, by_class: { Naranja: { total: 47, correct: 44, erroneous: 3, precision: 93 }, NaranjaVerde: { total: 1, correct: 0, erroneous: 1, precision: 0 } } },
    "YOLOE": { total_detections: 46, correct_detections: 45, erroneous_detections: 1, by_class: { Naranja: { total: 46, correct: 45, erroneous: 1, precision: 97 }, NaranjaVerde: { total: 0, correct: 0, erroneous: 0, precision: 0 } } },
    "SAM 3": { total_detections: 41, correct_detections: 3, erroneous_detections: 38, by_class: { Naranja: { total: 41, correct: 3, erroneous: 38, precision: 7 }, NaranjaVerde: { total: 0, correct: 0, erroneous: 0, precision: 0 } } },
    "OWLv2": { total_detections: 95, correct_detections: 72, erroneous_detections: 23, by_class: { Naranja: { total: 95, correct: 72, erroneous: 23, precision: 75 }, NaranjaVerde: { total: 0, correct: 0, erroneous: 0, precision: 0 } } }
  },
  "sample_03": {
    "Grounding DINO": { total_detections: 85, correct_detections: 31, erroneous_detections: 54, by_class: { Naranja: { total: 35, correct: 31, erroneous: 4, precision: 88 }, NaranjaVerde: { total: 50, correct: 0, erroneous: 50, precision: 0 } } },
    "YOLO-World": { total_detections: 60, correct_detections: 55, erroneous_detections: 5, by_class: { Naranja: { total: 59, correct: 55, erroneous: 4, precision: 93 }, NaranjaVerde: { total: 1, correct: 0, erroneous: 1, precision: 0 } } },
    "YOLOE": { total_detections: 58, correct_detections: 56, erroneous_detections: 2, by_class: { Naranja: { total: 58, correct: 56, erroneous: 2, precision: 96 }, NaranjaVerde: { total: 0, correct: 0, erroneous: 0, precision: 0 } } },
    "SAM 3": { total_detections: 50, correct_detections: 5, erroneous_detections: 45, by_class: { Naranja: { total: 50, correct: 5, erroneous: 45, precision: 10 }, NaranjaVerde: { total: 0, correct: 0, erroneous: 0, precision: 0 } } },
    "OWLv2": { total_detections: 120, correct_detections: 88, erroneous_detections: 32, by_class: { Naranja: { total: 120, correct: 88, erroneous: 32, precision: 73 }, NaranjaVerde: { total: 0, correct: 0, erroneous: 0, precision: 0 } } }
  },
  "sample_04": {
    "Grounding DINO": { total_detections: 70, correct_detections: 18, erroneous_detections: 52, by_class: { Naranja: { total: 22, correct: 18, erroneous: 4, precision: 81 }, NaranjaVerde: { total: 48, correct: 0, erroneous: 48, precision: 0 } } },
    "YOLO-World": { total_detections: 40, correct_detections: 36, erroneous_detections: 4, by_class: { Naranja: { total: 39, correct: 36, erroneous: 3, precision: 92 }, NaranjaVerde: { total: 1, correct: 0, erroneous: 1, precision: 0 } } },
    "YOLOE": { total_detections: 39, correct_detections: 38, erroneous_detections: 1, by_class: { Naranja: { total: 39, correct: 38, erroneous: 1, precision: 97 }, NaranjaVerde: { total: 0, correct: 0, erroneous: 0, precision: 0 } } },
    "SAM 3": { total_detections: 35, correct_detections: 2, erroneous_detections: 33, by_class: { Naranja: { total: 35, correct: 2, erroneous: 33, precision: 5 }, NaranjaVerde: { total: 0, correct: 0, erroneous: 0, precision: 0 } } },
    "OWLv2": { total_detections: 80, correct_detections: 60, erroneous_detections: 20, by_class: { Naranja: { total: 80, correct: 60, erroneous: 20, precision: 75 }, NaranjaVerde: { total: 0, correct: 0, erroneous: 0, precision: 0 } } }
  },
  "sample_05": {
    "Grounding DINO": { total_detections: 90, correct_detections: 40, erroneous_detections: 50, by_class: { Naranja: { total: 45, correct: 40, erroneous: 5, precision: 88 }, NaranjaVerde: { total: 45, correct: 0, erroneous: 45, precision: 0 } } },
    "YOLO-World": { total_detections: 68, correct_detections: 62, erroneous_detections: 6, by_class: { Naranja: { total: 66, correct: 62, erroneous: 4, precision: 94 }, NaranjaVerde: { total: 2, correct: 0, erroneous: 2, precision: 0 } } },
    "YOLOE": { total_detections: 65, correct_detections: 63, erroneous_detections: 2, by_class: { Naranja: { total: 65, correct: 63, erroneous: 2, precision: 97 }, NaranjaVerde: { total: 0, correct: 0, erroneous: 0, precision: 0 } } },
    "SAM 3": { total_detections: 58, correct_detections: 6, erroneous_detections: 52, by_class: { Naranja: { total: 58, correct: 6, erroneous: 52, precision: 10 }, NaranjaVerde: { total: 0, correct: 0, erroneous: 0, precision: 0 } } },
    "OWLv2": { total_detections: 130, correct_detections: 95, erroneous_detections: 35, by_class: { Naranja: { total: 130, correct: 95, erroneous: 35, precision: 73 }, NaranjaVerde: { total: 0, correct: 0, erroneous: 0, precision: 0 } } }
  }
};

export const GLOBAL_RANKING = [
  {
    model: "Grounding DINO",
    precision: "0.387",
    recall: "0.286",
    f1: "0.311",
    map50: "0.150",
    map5095: "0.083",
    fps: "1.790"
  },
  {
    model: "OWLv2",
    precision: "0.565",
    recall: "0.485",
    f1: "0.519",
    map50: "0.391",
    map5095: "0.201",
    fps: "0.340"
  },
  {
    model: "YOLO-World",
    precision: "0.668",
    recall: "0.346",
    f1: "0.456",
    map50: "0.286",
    map5095: "0.175",
    fps: "8.100"
  },
  {
    model: "YOLOE",
    precision: "0.662",
    recall: "0.338",
    f1: "0.447",
    map50: "0.277",
    map5095: "0.166",
    fps: "8.990"
  },
  {
    model: "SAM 3",
    precision: "0.292",
    recall: "0.103",
    f1: "0.150",
    map50: "0.065",
    map5095: "0.017",
    fps: "4.190"
  }
];

export const PROMPT_STRATEGIES = [
  {
    id: "P1",
    title: "P1 - Básicos de Clase",
    prompt: "['orange', 'green orange']",
    description: "Clases directas sin adjetivos adicionales de contexto."
  },
  {
    id: "P2",
    title: "P2 - Estado de Maduración",
    prompt: "['ripe orange', 'unripe orange']",
    description: "Especificación semántica del estado fenológico de la fruta."
  },
  {
    id: "P3",
    title: "P3 - Identificador Botánico",
    prompt: "['ripe orange citrus fruit']",
    description: "Denominación taxonómica botánica."
  },
  {
    id: "P4",
    title: "P4 - Descriptor Geométrico",
    prompt: "['spherical orange', 'oval lemon']",
    description: "Incorporación de la morfología espacial caracterizadora."
  },
  {
    id: "P5",
    title: "P5 - Contexto de Escena",
    prompt: "['spherical ripe orange on a tree']",
    description: "Integración del entorno donde se encuentra el fruto."
  },
  {
    id: "P6",
    title: "P6 - Enfoque de Exclusión",
    prompt: "['orange, not a leaf, not a branch']",
    description: "Filtro de exclusión mediante negaciones explícitas."
  }
];
