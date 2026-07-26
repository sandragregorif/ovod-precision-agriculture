---
abstract:
- |
  El present treball té com a objectiu l'avaluació comparativa de models
  de visió artificial de vocabulari tancat enfront d'arquitectures
  modernes de vocabulari obert (*OVOD*), analitzant el seu rendiment en
  el context de l'agricultura de precisió.

  La investigació es divideix en dos blocs. En el primer, s'estableix un
  *baseline* utilitzant *YOLO*, entrenat específicament per a la
  detecció i classificació de taronges (madures i verdes) en entorns
  reals. Sobre aquest mateix escenari, s'avalua el rendiment de models
  *OVOD* com *YOLO-World*, que permet una comparació directa en una
  tasca específica: determinar si un model generalista pot aconseguir o
  superar la precisió d'un model especialista en un domini acotat.

  En la segona fase, l'estudi aborda el principal avantatge competitiu
  dels models OVOD: la seua capacitat de generalització zero-shot.
  Mentre que el *baseline* de *YOLO* queda limitat a les classes apreses
  durant el seu entrenament, es testa l'habilitat dels models de
  vocabulari obert per a identificar nous elements agrícoles mitjançant
  l'ús de *prompts* de text, sense necessitat de reentrenament ni
  etiquetatge previ.

  Finalment, l'estudi integra una anàlisi comparativa del rendiment
  predictiu dels models avaluats en un entorn experimental unificat. En
  general, l'objectiu és avaluar si la detecció d'objectes de vocabulari
  obert pot proporcionar una alternativa més flexible per a escenaris
  d'agricultura de precisió en els quals les categories objectiu poden
  canviar al llarg del temps, la qual cosa podria reduir la necessitat
  d'anotacions repetides i el reentrenament del model.
- |
  \[spanish\] El presente trabajo tiene como objetivo la evaluación
  comparativa de modelos de visión artificial de vocabulario cerrado
  frente a arquitecturas modernas de vocabulario abierto (*OVOD*),
  analizando su rendimiento en el contexto de la agricultura de
  precisión.

  La investigación se divide en dos bloques. En el primero, se establece
  un *baseline* utilizando *YOLO*, entrenado específicamente para la
  detección y clasificación de naranjas (maduras y verdes) en entornos
  reales. Sobre este mismo escenario, se evalúa el rendimiento de
  modelos *OVOD* como *YOLO-World*, permitiendo una comparativa directa
  en una tarea específica: determinar si un modelo generalista puede
  alcanzar o superar la precisión de un modelo especialista en un
  dominio acotado.

  En la segunda fase, el estudio aborda la principal ventaja competitiva
  de los modelos OVOD: su capacidad de generalización zero-shot.
  Mientras que el *baseline* de *YOLO* queda limitado a las clases
  aprendidas durante su entrenamiento, se evalúa la capacidad de los
  modelos de vocabulario abierto para identificar nuevos elementos
  agrícolas mediante el uso de *prompts* de texto, sin necesidad de
  reentrenamiento ni etiquetado previo.

  Finalmente, el estudio integra un análisis comparativo del rendimiento
  predictivo de los modelos evaluados bajo un entorno experimental
  unificado. En general, el objetivo es evaluar si la detección de
  objetos de vocabulario abierto puede proporcionar una alternativa más
  flexible para escenarios de agricultura de precisión en los que las
  categorías objetivo pueden cambiar con el tiempo, reduciendo
  potencialmente la necesidad de anotaciones repetidas y el
  reentrenamiento del modelo.
- |
  \[english\] The present work aims at the comparative evaluation of
  closed-vocabulary computer vision models versus modern open-vocabulary
  architectures (OVOD), analyzing their performance in the context of
  precision agriculture.

  The research is divided into two blocks. In the first one, a baseline
  is established using YOLO, specifically trained for the detection and
  classification of oranges (ripe and green) in real-world environments.
  Under this same scenario, the performance of OVOD models such as
  YOLO-World is evaluated, allowing for a direct comparison in a
  specific task: determining whether a generalist model can reach or
  exceed the precision of a specialist model in a restricted domain.

  In the second phase, the study addresses the main competitive
  advantage of OVOD models: their zero-shot generalization capability.
  While the YOLO baseline remains limited to the classes learned during
  its training, the ability of open-vocabulary models to identify new
  agricultural elements is tested through the use of text prompts,
  without the need for prior model re-training or labeling.

  Finally, the study integrates a comparative analysis of the predictive
  performance of the evaluated models under a unified experimental
  setting. Overall, the objective is to assess whether open-vocabulary
  object detection can provide a more flexible alternative for precision
  agriculture scenarios in which target categories may change over time,
  potentially reducing the need for repeated annotation and model
  retraining.
author:
- Sandra Gregori Fernández
bibliography:
- references.bib
title: Open-Vocabulary Object Detection in Precision Agriculture
---

# Introduction

Computer vision is currently experiencing massive-scale adoption. Its
applications range from autonomous vehicles and medical diagnostic
imaging to facial recognition. In the field of precision agriculture,
real-time fruit detection and classification are fundamental for
optimizing harvesting and resource management. This thesis evaluates the
feasibility of transitioning from traditional detection models to
open-vocabulary architectures, aiming to achieve greater flexibility in
dynamic agricultural environments.

## Motivation

The primary motivation for this study stems from the limitations
inherent in closed-vocabulary object detection models, such as the YOLO
(You Only Look Once) family. Although Deep Learning has facilitated
milestones that seemed unattainable just a decade ago, traditional
models face a significant barrier: their reliance on predefined classes
and the requirement for large volumes of task-specifically labeled data.

To address this limitation, open-vocabulary object detection (OVOD)
models were developed. Unlike their closed-vocabulary predecessors,
these models leverage the semantic knowledge embedded in Vision-Language
Models (VLMs) to identify object categories not explicitly present
during training. This project stems from the need to evaluate whether
the flexibility provided by open-vocabulary object detection models
compensates for the potential loss of metrics that a closed-vocabulary
model can optimally offer when using zero-shot learning.

## Objectives

The primary objective of this thesis is to evaluate to what extent
open-vocabulary object detection (OVOD) can serve as a flexible
alternative to classical closed-vocabulary pipelines in precision
agriculture. To structure this analysis, the work is organized around
the following specific objectives:

- **Dataset Curation and Annotation Refinement**: To curate and
  re-annotate an open-field citrus dataset in order to obtain a
  geometrically consistent and contextually coherent ground truth for
  evaluation.

- **Supervised Baseline Construction**: To develop a strong
  closed-vocabulary reference model using state-of-the-art detectors for
  ripe and unripe orange detection.

- **Zero-Shot Evaluation of OVOD Architectures**: To systematically
  evaluate multiple open-vocabulary models (Grounding DINO, OWLv2,
  YOLO-World, YOLOE, and SAM 3), analyzing the effect of prompt design
  and spatial post-processing choices.

- **Exploratory Taxonomic Extension**: To examine the zero-shot
  generalization of the selected OVOD models to a novel fruit category
  (lemons) under exploratory evaluation conditions.

The research is guided by the following questions:

- How large is the performance gap between a task-specific supervised
  detector and current open-vocabulary detectors in dense real-world
  citrus orchard scenes?

- How sensitive are the evaluated OVOD architectures to prompt
  formulation and post-processing choices such as tiling, NMS
  thresholding, and confidence selection?

- Which open-vocabulary architecture offers the most favorable trade-off
  between predictive performance and inference efficiency under the
  evaluated experimental setting?

- To what extent can the selected OVOD models generalize zero-shot to a
  novel citrus category under an exploratory class-extension scenario?

The main contributions of this work are threefold: first, the curation
and re-annotation of a challenging citrus dataset under explicit
contextual and geometric criteria; second, an extensive empirical
evaluation of supervised and open-vocabulary detection models in dense
canopy scenes; and third, the development of a dedicated interactive
dataset curation tool (detailed in
Appendix [11](#appendix:refinement_tool){reference-type="ref"
reference="appendix:refinement_tool"}) that supported the large-scale
manual refinement and contextual alignment of the target agricultural
images.

## Structure of the Document

The present thesis is organized into eight primary chapters, in addition
to the bibliography and corresponding appendices, structured as follows:

- **Chapter 1: Introduction**: Defines the general context of the
  research, the underlying motivation driving the study, and the primary
  objectives to be achieved.

- **Chapter 2: State of the Art**: Reviews the evolution of computer
  vision applied to agricultural environments, from traditional methods
  to modern Deep Learning architectures. It presents a detailed analysis
  of the YOLO algorithm family and establishes the theoretical
  foundations of open-vocabulary object detection (OVOD) models, along
  with an assessment of existing domain-specific datasets.

- **Chapter 3: The Dataset**: Describes the original citrus dataset and
  details the exhaustive data curation, class redefinition, and manual
  re-annotation processes required to establish a robust and
  contextually consistent ground truth.

- **Chapter 4: Closed-Vocabulary Object Detection: YOLO11**: Focuses on
  the development of the supervised baseline model. It describes the
  hyperparameter optimization strategy and provides a quantitative and
  visual performance analysis of the selected YOLO11s architecture
  alongside alternative detectors like RT-DETR and YOLO26.

- **Chapter 5: Evaluation of Open-Vocabulary Object Detection (OVOD)
  Models**: Presents the zero-shot experimental evaluation of
  state-of-the-art architectures (Grounding DINO, OWLv2, YOLO-World,
  YOLOE, and SAM 3) on the validation set, systematically analyzing the
  impact of prompt engineering, tiling strategies, and spatial
  Non-Maximum Suppression (NMS) tuning.

- **Chapter 6: Global Comparison on the Test Set**: Presents a
  comprehensive evaluation on a held-out test split drawn from the same
  curated dataset. It establishes a performance stratification across
  all optimized open-vocabulary candidates against the supervised
  baseline through per-class metrics and confusion matrix analyses.

- **Chapter 7: Generalization to Novel Classes**: Examines the zero-shot
  taxonomic scalability and semantic flexibility of the preselected
  open-vocabulary architectures by introducing a fruit category unseen
  in the task-specific orange dataset (lemons) under unified multi-class
  and isolated crop-specific deployment strategies.

- **Chapter 8: Conclusions**: Synthesizes the primary empirical findings
  of the research, assesses the fulfillment of the initial objectives,
  and outlines future lines of work for open-vocabulary paradigms in
  precision agriculture.

# State of the Art

This chapter presents a chronological review ranging from traditional
object detection methods to open-vocabulary detection models for
computer vision, while also covering advances related to precision
agriculture environments. It also describes the architectures used in
this work, the datasets examined, the innovative proposal of the
project, and a critical synthesis of the state of the art.

## Computer Vision in Agricultural Environments {#subsec:cv_agri}

Unlike standard benchmarks, which evaluate models with generic objects
in controlled environments, computer vision in real agricultural
settings faces three critical challenges:

- **Occlusion:** Fruit is often hidden behind branches and leaves.

- **Lighting changes:** Variations in light throughout the day alter the
  actual color perceived by the camera.

- **Chromatic mimicry:** Immature green fruit has a color that is almost
  identical to that of the vegetative background.

For these reasons, research has evolved from classical color analysis
towards advanced Deep Learning detectors capable of operating in real
time directly in the
field [@mirhaji2021orangeorchardyolo; @chen2022orangeyolo]. The
following sections analyze this evolution chronologically.

### Traditional Methods Prior to Deep Learning

Before the advent of Deep Learning, fruit detection was typically
divided into two steps: an initial color-based separation followed by
geometric classification using classical algorithms. These classical
methods can be grouped into two main strategies:

1.  **Color and geometry segmentation:** This consists of isolating
    fruit by transforming the image into color spaces such as HSV or
    OHTA and searching for differences with the leaves. When fruit was
    partially occluded, the Circular Hough Transform was used to
    reconstruct its spherical shape.

    - Dorj et al. [@qadeer2021yield] combined the HSV color space with
      Hough to count oranges, achieving a precision close to 87% under
      favorable conditions, although the system failed under severe
      occlusion.

    - Wang et al. [@GLJH202309031] applied a similar technique for a
      harvesting robot. They achieved 97% accuracy with isolated fruit,
      but precision dropped to 90% with obstructing leaves and to 80.6%
      when citrus fruits overlapped one another.

2.  **Classical supervised classifiers:** This involves manually
    extracting texture, shape, and color histogram features, and then
    training models such as Support Vector Machines (SVM) or Random
    Forests [@zawbaa2014automatic; @astuti2018automatic].

    - Cubero et al. [@cubero2011citrusinspection] reviewed post-harvest
      systems that used texture descriptors combined with SVM to
      separate healthy from defective fruit, achieving accuracies
      between 80% and 90% in laboratory settings.

    - Aherwadi et al. [@aherwadi2019citrusquality] reached 97.3%
      accuracy classifying commercial citrus using fixed RGB features,
      although always dependent on homogeneous lighting and artificial
      backgrounds.

In summary, these traditional methods proved useful in controlled
environments, but their performance dropped rapidly in real orchards due
to their high sensitivity to lighting changes and ambient shadows.

### The Impact of Deep Learning Architectures (Closed Vocabulary)

The advent of convolutional neural networks (CNNs) changed everything by
eliminating the need to manually design descriptors; the network layers
themselves automatically learn to identify shapes, textures, and colors
directly from pixels [@wang2022application; @naranjo2020review]. In
precision agriculture, the deployment of these closed-vocabulary models
has developed across three technological stages:

- **Two-stage models (high precision):** Based primarily on
  architectures such as Faster R-CNN [@girshick2015fast], these
  prioritize accuracy over speed. One example is the *DeepFruits* system
  developed by Bargoti and Underwood [@bargoti2017deepfruits], which
  achieved F1 scores above 0.9 when detecting apples and mangoes in real
  environments with densities of up to 1,000 fruits per image.

- **Single-stage models (real time):** To process video on small devices
  directly in the field (*Edge AI*), faster models such as SSD and the
  YOLO family were adopted. Mirhaji et
  al. [@mirhaji2021orangeorchardyolo] compared YOLOv2, YOLOv3, and
  YOLOv4 under different lighting conditions (sunlight, clouds, and
  night light), concluding that YOLOv4 offered the best balance for
  estimating harvest load. In industrial moving environments, Chen et
  al. [@chen2021deep] integrated a CNN with the SORT tracking algorithm
  on a conveyor belt, classifying citrus with 93.6 % precision.

- **Custom variants for citrus:** In recent years, researchers have
  modified the YOLO architecture by adding attention modules to better
  capture small or occluded fruit:

  - *OrangeYolo* [@chen2022orangeyolo]: Based on YOLOv3 and combined
    with the OrangeSort tracker, it achieved a mAP of 0.957,
    outperforming YOLOv4 and YOLOv5 standards by avoiding
    double-counting of oranges hidden behind branches.

  - *YOLO-CIT* [@zhao2024yolocit]: Uses texture analysis (R-LBP, a
    rotation-sensitive version of Local Binary Patterns) to identify
    ripeness levels in complex environments, achieving a mAP@0.5 of
    85.88% with a response time of only 6.1 ms per image.

  - *AC-YOLO* [@xiao2024ac]: Adds lightweight separable convolutions to
    YOLOv4, reaching 96.19% precision under natural orchard conditions.

As a general assessment, current closed-vocabulary models achieve
outstanding precision in citrus counting and detection in the field.
However, they suffer from an important limitation: they are bound to the
classes seen during training. Adding a new fruit or variety to the
system requires the costly process of labeling thousands of new images
and retraining the model from scratch. This rigidity is what justifies
the search for alternatives in open-vocabulary models.

## The YOLO Family

YOLO [@redmon2016you] reformulated object detection as a single
regression problem over the full image, replacing the multi-stage
proposal-and-classify pipeline used by earlier detectors. This design
greatly improved inference speed and made YOLO especially attractive for
applications that require real-time processing.

### Architecture and Detection Mechanics

In its original formulation, YOLO divides the image into a grid and lets
each cell predict bounding boxes and confidence scores. Because the full
image is processed in a single pass, the model benefits from global
context and reduces many of the background errors observed in
region-based detectors, although early versions still suffered from
weaker localization accuracy [@girshick2014rich].

### Historical Evolution of the YOLO Family

YOLO has evolved through successive versions that progressively improved
detection accuracy, feature aggregation, and deployment efficiency. The
main trajectory of the family has been a gradual shift toward lighter,
faster, and more practical detectors, while keeping competitive
predictive performance.

**YOLOv2** [@redmon2017yolo9000] introduced batch normalization, anchor
boxes defined by k-means, and multi-scale training, which improved
training stability and robustness across resolutions. This version
marked an important step in making YOLO more stable and more accurate
than its original release.

**YOLOv3** [@redmon2018yolov3] focused on improving the detection of
small objects through multi-scale predictions and adopted the Darknet-53
backbone together with independent logistic classifiers. This design
helped the model better handle objects at different sizes, which is
especially relevant in dense scenes such as orchards.

**YOLOv4** [@bochkovskiy2020yolov4] organized architectural improvements
into Bag of Freebies and Bag of Specials, combining data augmentation
and optimization techniques with modules such as CSPDarknet53, Mish
activation, and SPP blocks. Bag of Freebies refers to changes that
improve accuracy without adding inference cost, while Bag of Specials
includes modules that improve precision at some computational expense.
**YOLOv5** [@yolov5] later consolidated a PyTorch-based workflow that
increased accessibility and practical adoption without abandoning the
efficiency that characterizes the family.

**YOLOv6** [@li2023yolov6] introduced a decoupled head and RepVGG
re-parameterization to reduce inference latency.
**YOLOv7** [@wang2022yolov7] then incorporated E-ELAN to improve
gradient flow in deeper networks. These versions continued the same
trend: preserving accuracy while making inference more efficient and
deployment-friendly.

More recent releases further reinforced this direction.
**YOLOv8** [@yolov8_ultralytics] adopted an anchor-free formulation and
the C2f module, **YOLOv9** [@wang2024yolov9] introduced PGI and GELAN to
mitigate information loss, and **YOLO10** [@THU-MIGyolov10] reduced
post-processing overhead by eliminating NMS at inference through dual
label assignment.

Taken together, these versions show a clear trajectory: the YOLO family
has progressively moved toward lighter, faster, and more
deployment-oriented detectors while preserving competitive predictive
performance. This trend is particularly relevant in agricultural
scenarios, where latency and hardware constraints are often as important
as raw accuracy.

### YOLO11: Efficiency and Spatial Attention

YOLO11 [@yolo11_ultralytics] combines strong predictive performance with
relatively low computational cost. Its design aims to improve mAP while
reducing parameter count, making it especially attractive in scenarios
where accuracy and deployment feasibility must be balanced.

Architecturally, YOLO11 introduces three main refinements. First, the
C3k2 block replaces C2f in the backbone and neck, reducing parameters
while preserving representational capacity. Second, the C2PSA module
introduces parallel spatial attention after the SPPF block, allowing the
model to emphasize the most relevant image regions under partial
occlusion. Third, the head is refined through C3k2 and CBS blocks to
improve multi-scale feature processing.

Beyond standard detection, YOLO11 also supports segmentation, pose
estimation, classification, and oriented bounding boxes within the same
framework. In the context of this work, however, the main reason for
choosing it is more specific: it provides a mature and efficient
supervised reference model against which the behavior of open-vocabulary
architectures can be fairly assessed.

### YOLO26: The Most Recent Release from Ultralytics

Although this thesis uses YOLO11 as its baseline, it is relevant to
mention one of the most recent developments in the YOLO family. YOLO26
[@jocher2026ultralyticsyolo26unifiedrealtime] was introduced as an Edge
AI-oriented proposal, with a particular emphasis on balancing accuracy,
inference speed, and deployability on resource-constrained devices.

Rather than introducing a radical redesign, YOLO26 simplifies several
components of the architecture. In particular, it removes the
Distribution Focal Loss module and offers an end-to-end inference mode
that eliminates the need for Non-Maximum Suppression, thereby reducing
post-processing overhead. It also incorporates refinements such as
Progressive Loss Balancing, Small-Target-Aware Label Assignment, and the
MuSGD optimizer to improve convergence and small-object detection.

From a practical perspective, these changes make YOLO26 a lighter and
more deployment-friendly model. However, YOLO11 remains the most
appropriate baseline for this work because it offers a stronger
combination of maturity, experimental stability, and consistency with
the scope originally defined for the thesis.

## Open-Vocabulary Object Detection

Traditional detectors such as Faster R-CNN, SSD, and YOLO can only
recognise the categories present in their training set. If a new class
appears at inference time, the detector will either ignore it or force
it into the most visually similar known category. In dynamic
agricultural environments, where cultivars, fruit conditions, or target
categories may change over time, this rigidity becomes a major
limitation.

### Limitations of Closed-Vocabulary Models

Closed-vocabulary detectors suffer from three main problems. First,
their category space is fixed, so adding a new class requires new
annotations and retraining. Second, bounding-box annotation is costly,
which limits scalability and produces long-tail effects in real-world
datasets. Third, class labels are treated as numerical categories rather
than semantic concepts, so the model cannot infer visual relationships
between unseen and seen categories.

These limitations are especially important in agriculture. A detector
trained only on oranges cannot be expected to recognize a new citrus
variety or another fruit type without additional supervision, even if
the visual similarity between categories is high.

### Zero-Shot Object Detection: The First Semantic Leap

Zero-shot object detection [@bansal2018zero] addresses this limitation
by projecting visual regions and class labels into a shared semantic
space. In these methods, detection no longer depends exclusively on a
fixed set of class indices, but on the similarity between region
embeddings and textual representations.

This was an important conceptual step, but early zero-shot methods had
clear limitations. They relied on static embeddings such as Word2Vec or
GloVe, obtained low mAP values compared with supervised detectors, and
showed a strong bias toward classes seen during training. As a result,
they remained of limited practical use in deployment-oriented evaluation
scenarios.

### CLIP and Large-Scale Multimodal Learning

A major shift occurred with CLIP [@radford2021learning], which
demonstrated that image-text pairs collected from the web could be used
to learn a shared visual-linguistic representation at scale. Instead of
learning a fixed classifier, CLIP trains an image encoder and a text
encoder jointly so that corresponding image-text pairs become close in a
shared embedding space.

This has an important consequence for open vocabulary. At inference
time, new classes can be introduced simply by changing the text prompt,
without retraining the model. While early zero-shot methods leaned
heavily on contrastive text encoders derived from architectures like
CLIP, modern open-vocabulary models employ a wider variety of textual
encoders (including BERT-based models or lightweight language models).

### Consolidation of OVOD: OVR-CNN and ViLD

The first mature open-vocabulary detectors were built on this idea in
two different ways. OVR-CNN [@zareian2021open] learned semantic
representations from image-caption pairs and transferred them to a
detector, while ViLD [@gu2021open] distilled the knowledge of CLIP into
a Mask R-CNN-style architecture.

These approaches showed that open-vocabulary detection could
substantially outperform earlier zero-shot methods. However, they also
exposed an important trade-off: stronger semantic alignment often came
with greater architectural complexity or reduced inference efficiency.

### Current Frontier: Grounding, Transformers, and Web-Scale Scaling

More recent approaches moved beyond late fusion and integrated language
earlier in the detection process. In these models, text does not simply
classify proposed regions at the end of the pipeline; instead, it
conditions how visual regions are represented and selected from the
beginning.

**Grounding DINO** [@liu2024grounding] is one of the clearest examples
of this paradigm. It extends the DINO detector with a text encoder and
cross-modal interactions at multiple stages, allowing language to
influence region proposal, query initialization, and final prediction.
This makes the architecture particularly strong for phrase grounding and
semantically rich prompts, although at the cost of higher latency.

**OWLv2** [@NEURIPS2023_e6d58fc6] follows a different strategy. Instead
of relying primarily on architectural novelty, it scales training
through web self-training with pseudo-annotations generated from large
image-text corpora. This data scaling, paired with a patch-based Vision
Transformer (ViT) backbone (typically operating on a 16x16 pixel
tokenization scale, such as the ViT-B/16 architecture), gives it strong
generalization capacity, especially on rare categories.

### Real-Time Open-Vocabulary Detection: YOLO-World and YOLOE

Grounding DINO and OWLv2 provide strong open-vocabulary capabilities,
but their latency can be problematic in real agricultural environments.
This motivated a new line of work within the YOLO family aimed at
preserving real-time efficiency while incorporating open-vocabulary
behavior.

**YOLO-World** [@cheng2024yolo] follows a prompt-then-detect paradigm.
It introduces a reparameterisable vision-language path aggregation
network that injects text information during training and allows prompt
embeddings to be fused into the classification head before inference.
Once the vocabulary is fixed, the model behaves operationally like a
closed-vocabulary detector, with the corresponding efficiency benefits.

**YOLOE** [@Wang_2025_ICCV] extends this idea further by unifying
detection and segmentation and by supporting multiple prompt modalities,
including text, visual exemplars, and prompt-free scenarios. In
practice, it represents one of the most efficient current approaches
within the open-vocabulary YOLO paradigm, which makes it especially
relevant for deployment-oriented agricultural experiments.

### Promptable Segmentation and Unified Perception: SAM3

SAM 3 [@sam3_2025] differs from the previous models because it is not
designed only as a detector, but as a broader promptable perception
system. Given a text prompt, a visual exemplar, or both, it can detect,
segment, and track object instances in images or videos.

Its architecture extends the capabilities of SAM 2 [@ravi2024sam2] and
introduces promptable concept segmentation, combining localization and
mask prediction with a dedicated mechanism for reasoning about whether
the concept is present in the image. In the context of this work, SAM 3
is not treated as a standard bounding-box detector, but as a flexible
perception model whose promptable nature may be useful in changing
agricultural scenarios.

### Comparative Analysis of the Evaluated Architectures

Table [\[tab:ovod_comparison\]](#tab:ovod_comparison){reference-type="ref"
reference="tab:ovod_comparison"} summarises the six architectures
evaluated in this work, along with their main characteristics from the
perspective of deployment in precision agriculture.

Taken together, the models analyzed in this chapter represent three
major design strategies for open-vocabulary perception. Grounding DINO
and OWLv2 prioritize semantic richness and generalization, YOLO-World
and YOLOE prioritize real-time deployment, and SAM3 extends the problem
toward promptable segmentation and video-aware perception.

This diversity is valuable for the objectives of the thesis. It allows
the study to compare not only different levels of predictive
performance, but also different trade-offs between speed, flexibility,
prompt sensitivity, and suitability for real agricultural deployment.

## Datasets for Evaluating Detectors in Real Agricultural Environments

Evaluating object detectors in agriculture is not equivalent to
evaluating them on generic benchmarks such as COCO [@lin2014microsoft].
In orchards, backgrounds are visually dense, illumination changes
constantly, branches create irregular occlusions, and fruits at
different ripeness stages may coexist within the same canopy.

### Taxonomy of Reviewed Agricultural Datasets

Nine representative agricultural datasets were reviewed.
Table [\[tab:datasets_agricolas\]](#tab:datasets_agricolas){reference-type="ref"
reference="tab:datasets_agricolas"} organizes them by acquisition
environment and object type, the two factors that most strongly affect
their usefulness for evaluating citrus detection in real field settings.

### Exclusion Criteria

Three reasons explain why the reviewed datasets were not sufficient for
the objective of this work. First, many were acquired under laboratory,
greenhouse, or semi-controlled conditions, which do not reflect the
complexity of real orchards. Second, several are focused on leaves or
diseases rather than fruit detection. Third, even the most promising
citrus datasets do not align semantically with the type of evaluation
required for open-vocabulary models.

CitDet illustrates this problem clearly. Although it contains real
orchard imagery, it distinguishes between fruit on the tree and fruit on
the ground. That distinction is meaningful from an agronomic
perspective, but difficult to encode consistently with open-vocabulary
prompts, since current text encoders operate primarily on categorical
identity rather than precise spatial ontology.

### Identified Gap: Absence of Datasets for Field OVOD {#ausencia_datasets}

The review reveals three concrete gaps. There is no sufficiently large
open-field dataset for tree fruit that combines real orchard conditions,
dense foliage, and enough scale to stress open-vocabulary detectors.
Standard OVOD benchmarks do not reflect the visual challenges of citrus
orchards. Finally, there is no practical reference showing how generic
pre-trained open-vocabulary models behave in this domain without
retraining.

## Identification of the Opportunity and Proposed Work

This gap defines the opportunity addressed by the thesis.
Open-vocabulary detectors have shown promising generalization on generic
benchmarks, but they have not been systematically evaluated in real
citrus orchards under the conditions that matter most for deployment:
occlusion, foliage confusion, illumination variability, and multiple
ripeness stages.

### Need for Evaluation in Real Environments

The central question is not whether open-vocabulary models are generally
effective, but whether they remain useful in a specific orchard scenario
without retraining. More concretely, four issues remain open:

- Whether current OVOD models maintain their semantic capacity under
  strong fruit-background similarity.

- Whether prompt choice substantially alters performance.

- Whether real-time open-vocabulary detectors remain competitive against
  stronger but slower architectures.

- Whether the flexibility of open vocabulary compensates for the
  precision gap with respect to a supervised baseline.

## Critical Synthesis of the State of the Art

The literature reviewed in this chapter shows a clear transition from
fixed-category detection toward language-conditioned perception.
Classical computer vision methods and early supervised detectors were
effective only within the limits of their annotated categories.
Large-scale multimodal learning, especially through CLIP, introduced the
possibility of generalising through language rather than through
exhaustive class-specific supervision.

From that point onward, different architectural families made different
trade-offs. Some, such as Grounding DINO and OWLv2, prioritized semantic
richness and large-scale generalization. Others, such as YOLO-World and
YOLOE, attempted to preserve the deployment efficiency required in real
applications. SAM3 extended the paradigm toward promptable segmentation
and broader scene understanding.

However, the current literature still leaves an unresolved question: how
these models behave in real orchard conditions, where the target object
is not visually isolated from the background and prompt design may
become a critical factor. This is precisely the contribution of the
present work. Rather than proposing a new architecture, the thesis
performs a systematic evaluation of representative open-vocabulary
models on real citrus orchard imagery, using YOLO11 as a supervised
closed-vocabulary baseline.

# The Dataset {#dataset}

This chapter describes the dataset selected to address the first
objective of this work: establishing a baseline using a
closed-vocabulary object detection model. This initial model focuses on
detecting and classifying two primary categories: ripe oranges and
unripe (green) oranges. Once this baseline is consolidated, the selected
OVOD (Open-Vocabulary Object Detection) architectures will be evaluated
on the same dataset, enabling a direct performance comparison against
the baseline model. Finally, the detection of novel classes will be
assessed to examine the generalization capabilities of the
open-vocabulary models.

To fulfill this first objective, the *NaranjasFinal* dataset
[@naranjasfinal_dataset] was selected. This dataset was developed by the
*Institut Valencià d'Investigacions Agràries* (IVIA) and distributed
through the Roboflow platform. This resource is of particular relevance
to the present work, as it provides images of orange trees captured in
real agricultural environments. These characteristics enable a
significantly more robust evaluation since the model is trained under
the same real-world conditions it would encounter during deployment,
confronting challenges such as foliage occlusions, illumination
variations, and different maturation stages.

The following sections detail the original characteristics of this
dataset and present a comprehensive analysis to assess its suitability
and quality regarding the demanding objectives of this project.

## The Original Dataset

The original dataset is designed for comprehensive phenological
monitoring of citrus trees, classifying their elements into three main
categories:

- ***Flor (Flower)***: Represents orange blossom flowers at various
  stages of bloom.

- ***Naranja (Ripe orange)***: Ripe fruits exhibiting their
  characteristic orange coloration, ready for harvest.

- ***NaranjaVerde (Unripe orange)***: Fruits in an immature state or
  early stages of development.

The original dataset is partitioned into 1,148 training images, 395
validation images, and 210 test images. These captures present several
challenges for computer vision systems, including severe foliage
occlusion, environmental illumination variability depending on the time
of day, and a high degree of chromatic camouflage with the surrounding
environment. This last challenge is particularly pronounced in the
*NaranjaVerde* class, where immature fruit can be easily confused with
the surrounding foliage.

The significance of this dataset lies in its versatility. A robust
implementation would enable the automation of critical processes, such
as quality control and real-time yield estimation.

The following section presents a comprehensive analysis of the dataset
to assess its quality regarding the requirements of this work.

## Comprehensive Dataset Analysis and Curation

To ensure robust model training and evaluation, the selected dataset
must meet high-quality standards. This is essential for accurately
simulating real-world environments and guaranteeing the expected model
behavior in a hypothetical deployment scenario.

To this end, a thorough analysis was conducted and a series of
modifications were applied to the original dataset to align it as
closely as possible with the objectives of this project. The following
subsections describe the distinct phases of this curation process.

### Class Redefinition

Since the primary objective of this work focuses on fruit detection, the
*Flor* class was deemed redundant. To avoid potential noise that this
class could introduce into the models, all images containing exclusively
flower instances were removed from the dataset. Images containing
instances of the *Flor* class alongside *Naranja* or *NaranjaVerde*
instances were retained, with only the flower annotations being
discarded.

Following this modification, the dataset is strictly defined by two
final classes: class 0 (*Naranja*) and class 1 (*NaranjaVerde*).

### Class Imbalance Analysis {#desbalance}

To ensure that model evaluations are robust and that results are not
biased toward a majority class, the number of instances per class was
assessed across each dataset split. These distributions are shown in
Table [3.1](#tab:distribucion_completa_original){reference-type="ref"
reference="tab:distribucion_completa_original"}.

+----------------+----------------------------+----------------------------+----------------------------+
|                | **Training Set**           | **Validation Set**         | **Test Set**               |
+:===============+===========:+==============:+===========:+==============:+===========:+==============:+
| 2-7 **Class**  | **Images** | **Instances** | **Images** | **Instances** | **Images** | **Instances** |
+----------------+------------+---------------+------------+---------------+------------+---------------+
| All            | 1,133      | 43,324        | 369        | 5,387         | 183        | 2,587         |
+----------------+------------+---------------+------------+---------------+------------+---------------+
| *Naranja*      | 732        | 20,087        | 126        | 1,315         | 137        | 2,298         |
+----------------+------------+---------------+------------+---------------+------------+---------------+
| *NaranjaVerde* | 636        | 23,237        | 335        | 4,072         | 63         | 289           |
+----------------+------------+---------------+------------+---------------+------------+---------------+

: Class distribution in the original training, validation, and test
sets. {#tab:distribucion_completa_original}

The class imbalance in the training set is not particularly significant
(20,087 instances of the *Naranja* class versus 23,237 instances of the
*NaranjaVerde* class). However, the imbalance becomes more critical in
the remaining two splits. In the validation set, the *NaranjaVerde*
class comprises 4,072 instances compared to only 1,315 instances of the
*Naranja* class, which is a pronounced imbalance that may influence
hyperparameter selection in closed-vocabulary models or the choice of
optimal configuration in open-vocabulary architectures. Conversely, in
the test set, the *Naranja* class contains 2,298 instances versus only
289 instances of the *NaranjaVerde* class, which may skew the final
evaluation metrics on this held-out split.

As a result, it is concluded that the dataset must undergo a class
rebalancing process. However, since a full image review has yet to be
completed, this step is deferred to a later stage, as the dataset may
still be subject to image removal and re-annotation, making it
inefficient to perform rebalancing at this point. Nevertheless,
conducting this analysis is relevant given the potential issues
discussed above, and it serves as a reminder to carry out this process
as a final curation step.

### Identification of Weaknesses in the Original Images and Annotations

To align the images with the objectives of this work and ensure
high-quality annotations that enable rigorous evaluation, a
comprehensive review of all dataset images and their corresponding
bounding boxes was conducted. During this process, several defects were
identified that, if left unaddressed, would severely compromise the
validity of the experimental results:

- **Contextual inconsistency**: In certain images, oranges that had
  fallen to the ground or belonged to background trees were annotated,
  while in others they were ignored and left unlabeled. As illustrated
  in Figures [3.1](#fig:inconsistencia_contextual1){reference-type="ref"
  reference="fig:inconsistencia_contextual1"},
  [3.2](#fig:inconsistencia_contextual2){reference-type="ref"
  reference="fig:inconsistencia_contextual2"} and
  [3.3](#fig:inconsistencia_contextual3){reference-type="ref"
  reference="fig:inconsistencia_contextual3"} (bounding boxes shown in
  red), this ambiguity confuses the model during training, as it is
  exposed to contradictory criteria regarding whether it should detect
  oranges on background trees, on the ground, or exclusively on the
  primary foreground tree. This issue has a distinct impact on
  open-vocabulary architectures, as these models do not inherently
  incorporate task-specific contextual constraints, leading them to
  strictly detect requested semantic concepts regardless of their
  situational relevance.

- **False positives due to missing labels**: A significant number of
  oranges were not annotated in the original dataset. During evaluation,
  unannotated regions are treated as background. Therefore, valid
  detections made by the model on unlabeled fruit instances are
  erroneously counted as false positives. This defect degrades system
  precision and distorts the true assessment of the model's
  fruit-counting capability. In Figure
  [3.5](#fig:fp1){reference-type="ref" reference="fig:fp1"}, (where
  original annotations are shown in blue and missing annotations in
  red), several unannotated fruits are clearly visible on the tree.

- **Imprecise bounding box fitting**: Many annotations exhibited
  excessive slack relative to the actual fruit contour, causing the
  bounding box area to include large portions of surrounding foliage.
  This poor fit, illustrated in Figures
  [3.6](#fig:holgado1){reference-type="ref" reference="fig:holgado1"}
  (original image) and [3.7](#fig:holgado2){reference-type="ref"
  reference="fig:holgado2"} (enlarged view), hinders the model's ability
  to accurately learn the morphological features and precise boundaries
  of the orange.

- **Noise due to lack of realism**: Multiple images exhibited aggressive
  preprocessing or were partial captures of the tree taken at an
  excessively close range. These samples are not representative of real
  use cases, in which the entire tree would be processed. Representative
  examples of each case are shown in Figures
  [3.9](#fig:realismo1){reference-type="ref" reference="fig:realismo1"}
  and [3.10](#fig:realismo2){reference-type="ref"
  reference="fig:realismo2"}.

- **Rotated images with misaligned labels**: Some images contained
  bounding boxes entirely displaced from their corresponding fruits. It
  was determined that these images were most likely rotated post-hoc by
  the original annotators without applying the corresponding
  mathematical transformation to the annotation coordinates, resulting
  in a complete desynchronization between the image and its labels.
  Figure [3.12](#fig:rotado){reference-type="ref"
  reference="fig:rotado"} clearly illustrates an example of this
  anomaly.

<figure id="fig:inconsistencias_contextuales_todas"
data-latex-placement="H">
<figure id="fig:inconsistencia_contextual1">
<img src="images/dataset/inconsistencia1.jpg" />
<figcaption>All background fruits annotated.</figcaption>
</figure>
<figure id="fig:inconsistencia_contextual2">
<img src="images/dataset/inconsistencia2.jpg" />
<figcaption>Some background fruits annotated.</figcaption>
</figure>
<figure id="fig:inconsistencia_contextual3">
<img src="images/dataset/inconsistencia3.jpg" />
<figcaption>No background fruits annotated.</figcaption>
</figure>
<figcaption>Examples of contextual inconsistencies in the annotation of
background fruits.</figcaption>
</figure>

<figure id="fig:fp1" data-latex-placement="H">
<img src="images/dataset/fp1.jpg" style="width:80.0%" />
<figcaption>Examples of missing labels causing false positives. Red
labels indicate unannotated oranges.</figcaption>
</figure>

<figure id="fig:bounding_boxes_holgadas" data-latex-placement="H">
<figure id="fig:holgado1">
<img src="images/dataset/holgado1.jpg" />
<figcaption>Original image.</figcaption>
</figure>
<figure id="fig:holgado2">
<img src="images/dataset/holgado2.jpg" />
<figcaption>Enlarged image showing loose bounding boxes.</figcaption>
</figure>
<figcaption> Example of loose bounding box fitting.</figcaption>
</figure>

<figure id="fig:realismo_todos" data-latex-placement="H">
<figure id="fig:realismo1">
<img src="images/dataset/realismo1.jpg" />
<figcaption>First example.</figcaption>
</figure>
<figure id="fig:realismo2">
<img src="images/dataset/realismo2.jpg" />
<figcaption>Second example.</figcaption>
</figure>
<figcaption>Examples of images that are not representative of the
real-world conditions required by the problem.</figcaption>
</figure>

<figure id="fig:rotado" data-latex-placement="H">
<img src="images/dataset/rotado.jpg" style="width:80.0%" />
<figcaption>Example of an image that was rotated after its
annotation.</figcaption>
</figure>

### Dataset Analysis and Curation: Concluding Remarks

Following the exhaustive analysis of the dataset in its entirety, it was
determined that the original collection did not meet the quality
standards required by the problem at hand. Given that, as noted in
Section [2.4.3](#ausencia_datasets){reference-type="ref"
reference="ausencia_datasets"}, no publicly available datasets
satisfying the specific requirements of this project exist, a decision
was made to subject the images to a manual cleaning and re-annotation
process. To support this task, a dedicated Python script was developed
(detailed in Appendix
[11](#appendix:refinement_tool){reference-type="ref"
reference="appendix:refinement_tool"}), whose functionalities
facilitated the manipulation of annotation files.

The following criteria were strictly applied during the dataset
modification process:

- **Contextual inconsistency and missing labels**: Oranges that had
  fallen to the ground or belonged to background trees were excluded
  from annotation. Only oranges belonging exclusively to the primary
  tree (defined by whichever tree predominantly occupies most or all of
  the image frame and is situated closest to the camera lens) in the
  foreground were annotated. Regarding visibility, no fixed pixel-area
  threshold was enforced; instead, a fruit was annotated whenever a
  human annotator could reliably identify it as a single distinct fruit
  instance, as omitting it would introduce a systematic bias with
  respect to the true fruit count that a human observer would perform.
  This criterion ensures a consistent count of harvestable fruit per
  tree while also avoiding statistical duplication by excluding fruit
  from background trees that will be analyzed in their own corresponding
  captures. This exclusion criterion is also consistent with the
  intended counting scenario assumed in this work: in a real harvesting
  scenario, only the fruit belonging to the tree being actively
  processed is operationally relevant, making background fruit a source
  of noise rather than a valid detection target.

- **Imprecise bounding box fitting:** All annotations exhibiting
  excessive slack or including surrounding foliage were removed and
  redrawn, adjusted precisely to the actual morphological boundaries of
  each fruit. For partially visible oranges, the bounding box was
  required to span the full estimated perimeter of the fruit (from
  corner to corner of its visible extent) even when intermediate foliage
  partially interrupted its surface. This ensures that the annotated
  region reflects the true spatial footprint of the fruit rather than
  only its unoccluded portion. Annotating only the visible patches would
  risk splitting a single fruit into multiple detections, as a leaf
  bisecting the fruit could lead the model to treat the two exposed
  segments as separate objects. Including the intervening foliage within
  the bounding box instead conveys to the model that the occluded fruit
  is a single whole object, helping it learn what a partially hidden
  fruit looks like in a real orchard setting.

- **Noise due to lack of realism**: Heavily preprocessed images or those
  captured at an excessively close range were discarded entirely.
  However, to prevent excessive reduction of the final dataset size,
  images in which the tree was not fully visible but the majority of it
  was clearly discernible were retained.

- **Rotated images**: The necessary geometric transformations were
  applied to affected images to revert their rotation and realign the
  original bounding boxes with their corresponding fruits.

After processing all images using the developed tool and applying the
criteria described above, a final curated set of 546 images was
obtained. Visual examples contrasting the final annotations with the
original defects are presented below. Figure
[3.13](#fig:inc_arreglada){reference-type="ref"
reference="fig:inc_arreglada"} (corresponding to the original Figure
[3.1](#fig:inconsistencia_contextual1){reference-type="ref"
reference="fig:inconsistencia_contextual1"}) illustrates how contextual
inconsistency was corrected to isolate the primary tree. Figure
[3.14](#fig:fp_arreglado){reference-type="ref"
reference="fig:fp_arreglado"} (corresponding to original Figure
[3.5](#fig:fp1){reference-type="ref" reference="fig:fp1"}) shows how all
visible oranges on the tree were annotated to prevent false positives
among correctly labeled instances. Finally, Figure
[3.17](#fig:bounding_boxes_holgadas_arregladas){reference-type="ref"
reference="fig:bounding_boxes_holgadas_arregladas"} (corresponding to
the original Figure
[3.8](#fig:bounding_boxes_holgadas){reference-type="ref"
reference="fig:bounding_boxes_holgadas"}) demonstrates how annotations
were precisely fitted to the fruit boundaries, compelling the model to
focus exclusively on the texture and shape of the orange.

<figure id="fig:inc_arreglada" data-latex-placement="H">
<img src="images/dataset/inconsistencia_arreglada.jpg"
style="width:80.0%" />
<figcaption>Example of an image with corrected contextual
inconsistency.</figcaption>
</figure>

<figure id="fig:fp_arreglado" data-latex-placement="H">
<img src="images/dataset/fp_arreglado.jpg" style="width:80.0%" />
<figcaption>Example of an image with corrected missing
labels.</figcaption>
</figure>

<figure id="fig:bounding_boxes_holgadas_arregladas"
data-latex-placement="H">
<figure id="fig:holg_arreglada1">
<img src="images/dataset/holgura_arreglada.jpg" />
<figcaption>Original image.</figcaption>
</figure>
<figure id="fig:holg_arreglada2">
<img src="images/dataset/holg_ampliada.jpg" />
<figcaption>Enlarged image showing loose bounding boxes
fixed.</figcaption>
</figure>
<figcaption>Example of an image with corrected loose bounding
boxes.</figcaption>
</figure>

The final step of this process, as specified in Section
[3.2.2](#desbalance){reference-type="ref" reference="desbalance"},
consisted of performing an equitable redistribution of images to ensure
that each dataset split maintains a balanced class distribution. Given
the significant reduction in the total dataset volume, a partition of
60% for the training set, 20% for the validation set, and 20% for the
test set was adopted. The final class distribution, which will serve as
the official basis for all subsequent experiments in this work, is
detailed in Table [3.2](#tab:distribucion_completa){reference-type="ref"
reference="tab:distribucion_completa"}.

+----------------+----------------------------+----------------------------+----------------------------+
|                | **Training Set**           | **Validation Set**         | **Test Set**               |
+:===============+===========:+==============:+===========:+==============:+===========:+==============:+
| 2-7 **Class**  | **Images** | **Instances** | **Images** | **Instances** | **Images** | **Instances** |
+----------------+------------+---------------+------------+---------------+------------+---------------+
| All            | 327        | 21,502        | 109        | 7,181         | 110        | 7,122         |
+----------------+------------+---------------+------------+---------------+------------+---------------+
| *Naranja*      | 210        | 11,520        | 70         | 3,255         | 71         | 3,570         |
+----------------+------------+---------------+------------+---------------+------------+---------------+
| *NaranjaVerde* | 210        | 9,982         | 70         | 3,926         | 70         | 3,552         |
+----------------+------------+---------------+------------+---------------+------------+---------------+

: Class distribution in the final training, validation, and test sets.
{#tab:distribucion_completa}

# Closed-Vocabulary Object Detection: YOLO11 {#baseline_ch}

This chapter describes all experiments conducted in the process of
identifying the optimal closed-vocabulary model to serve as the baseline
for this work. Using this optimal configuration, inference will be
performed on the held-out test set in Chapter
[6](#comparativa_test){reference-type="ref"
reference="comparativa_test"} to evaluate the model's performance and
generalization capabilities on unseen data drawn from the same source.
These results will establish a task-specific supervised reference for
the open-vocabulary models detailed in that same chapter, from which
conclusions regarding the OVOD architectures will be drawn.

The model selected to establish the baseline is YOLO, specifically
version 11 [@yolo11_ultralytics]. This choice is justified by its
ability to strike an effective balance between accuracy and inference
speed, a critical requirement in real-world scenarios involving a high
density of fruit instances to be detected.

The following sections of this chapter specify the experimental
environment, the discarded configurations, and the final chosen setup.
Additionally, experiments involving other architectures are presented,
including RT-DETR [@lv2023detrs], a Transformer-based detector, and
YOLO26 [@jocher2026ultralyticsyolo26unifiedrealtime], the latest version
released by Ultralytics during this research. These experiments aim to
assess how this use case would perform under alternative architectures.
Nevertheless, the primary focus of this work remains on YOLO11; this
project was initiated using this architecture as the reference standard,
and maintaining it as the baseline ensures a well-defined project scope
centered on the comparison of OVOD architectures.

## Experiments

The first experiments described below were conducted using the
re-annotated dataset presented in Chapter
[3](#dataset){reference-type="ref" reference="dataset"}. For the
training configuration, 200 epochs were set (defined as the number of
complete passes through the entire dataset), along with an early
stopping patience of 30 epochs, after which training is halted if no
improvement is observed. To ensure reproducibility, the default
deterministic random seed (seed=0) of the Ultralytics framework was
maintained.

Regarding input resolution, YOLO was natively trained at 640 px;
however, a resolution of 1280 px was adopted for this work, given the
complexity of the task: orange trees in real agricultural environments
with a high density of fruit instances, including small oranges and
those partially occluded by foliage. The batch size (defined as the
exact number of images processed simultaneously per iteration before
updating the model parameters) was set to -1, enabling YOLO to
automatically determine the optimal value based on the available
hardware. Finally, the optimizer was set to *auto* mode, though YOLO
typically defaults to the AdamW optimizer for smaller datasets such as
this one.

Regarding the data augmentation parameters implemented by default in
YOLO, these were left unmodified in the initial experiments.
Subsequently, the same models were retrained with slight adjustments to
these parameters to assess their impact on performance.

The full computational platform, including library versions and hardware
details, is thoroughly documented in
Appendix [10](#execution_environment){reference-type="ref"
reference="execution_environment"}.

### Global Comparative Study of Architectures

A scalability study was carried out evaluating the complete YOLO11
architecture family (nano, small, medium, large, and extra-large
variants). The objective of this global comparison is to analyze the
trade-off between predictive performance (accuracy) and computational
cost (number of parameters and inference speed) to technically justify
the selection of the baseline model.

To this end, all models were trained under identical conditions and with
default hyperparameters. Regarding the evaluation protocol, validation
was conducted using a standardized Intersection over Union threshold of
0.50 ($IoU = 0.50$) . Furthermore, the confidence threshold during this
phase was intentionally restricted to 0.01. This approach ensures the
generation of complete Precision-Recall and F1 curves across the entire
confidence spectrum, enabling the empirical determination of the optimal
confidence threshold on the validation set. This optimal threshold is
later utilized during test inference to prevent data leakage and
guarantee unbiased generalization metrics. The overall results on the
validation set are presented in Table
[4.1](#tab:yolos_defecto){reference-type="ref"
reference="tab:yolos_defecto"}.

  **Model**     **Precision**   **Recall**   **F1-score**   **mAP@0.50**   **mAP@0.50:95**   **Parameters**   **FPS**   **Batch size**
  ----------- --------------- ------------ -------------- -------------- ----------------- ---------------- --------- ----------------
  YOLO11n               0.804        0.679          0.736          0.735             0.405             2.6M     9.660                3
  YOLO11s               0.814        0.705          0.756          0.769             0.431             9.4M     4.420                2
  YOLO11m               0.819        0.710          0.761          0.766             0.437            20.1M     1.860                1
  YOLO11l               0.816        0.709          0.759          0.771             0.442            25.3M     1.440                1
  YOLO11x               0.814        0.729          0.769          0.788             0.450            56.9M     0.776                1

  : Results of YOLO11 models on the validation set ($conf=0.01$,
  $IoU=0.50$). {#tab:yolos_defecto}

As shown in Table [4.1](#tab:yolos_defecto){reference-type="ref"
reference="tab:yolos_defecto"}, increasing architectural capacity does
not translate into a proportionally significant improvement in
performance.

The transition from the nano variant (YOLO11n) to the small variant
(YOLO11s) represents the most substantial relative improvement in the
comparison, with the F1-score increasing by 0.02 and mAP@0.50 by 0.034.
This suggests that the 2.6M parameters of the nano variant are
insufficient to capture complex visual patterns such as severe occlusion
and chromatic camouflage of the fruit. Beyond the small architecture,
predictive gains stabilize considerably. Moving from YOLO11m to YOLO11l
adds over 5 million additional parameters (+26%), yet the F1-score
marginally decreases from 0.761 to 0.759, and mAP@0.50 increases by only
0.005.

The extra-large variant (YOLO11x) achieves the highest mAP@0.50 (0.788)
and best F1-score (0.769) in the study. However, these gains come at the
cost of scaling the model to 56.9M parameters, with a severe
computational impact: inference speed drops to 0.776 FPS (less than one
image per second), demonstrating that saturating the network with
parameters is neither viable nor efficient for this problem.

Given the diminishing performance returns as model size increases, it is
concluded that YOLO11s represents the optimal trade-off between
predictive capacity and computational cost. This compact architecture,
with only 9.4M parameters, achieves a mAP@0.50 of 0.769 (surpassing the
medium variant (0.766) and approaching the large variant (0.771)) and a
F1-score of 0.756 (approaching the medium (0.761) and the large (0.759)
variants), while maintaining an inference speed of 4.42 FPS, more than
twice as fast as intermediate-sized alternatives. Compared to the upper
extreme (YOLO11x), the marginal mAP@0.50 and F1-score difference is
entirely acceptable given that YOLO11s is six times lighter and nearly
six times faster. Consequently, YOLO11s is provisionally designated as
the chosen reference model for all subsequent experiments involving the
OVOD architectures in this work

### Hyperparameter Optimization and Data Augmentation

Once the baseline performance of each architecture was established, a
fine-tuning process was carried out on the training hyperparameters.
YOLO's default configuration is designed to maximize performance on
large, highly diverse datasets such as COCO. However, the application
scenario in this work presents highly specific morphological and
environmental challenges: dense occlusion, extreme natural illumination
variability, and severe chromatic camouflage between the *NaranjaVerde*
class and the surrounding foliage.

To improve model robustness against these conditions, a data
augmentation and learning optimization strategy tailored to the
characteristics of the agricultural environment was designed. The
modifications applied are as follows:

- **cos_lr = True**: The Cosine Learning Rate Scheduler was enabled.
  This technique gradually reduces the learning rate in a smooth,
  non-linear fashion toward the end of training, allowing the model to
  converge more stably into local minima, a particularly beneficial
  property for datasets with high visual variability.

- **cls = 1.0**: The classification loss weight was increased, imposing
  stricter penalties when the model confuses classes and forcing it to
  learn the subtle differences in texture and hue between ripe and
  unripe oranges.

- **close_mosaic = 15**: Data augmentation is disabled during the final
  15 epochs, reducing the noise introduced by this technique in the
  later stages of training.

- **hsv_s = 0.5**: The random saturation variation range was reduced.
  Excessive saturation shifts could cause *NaranjaVerde* instances to
  acquire vivid tones visually resembling the *Naranja* class, thereby
  confusing the model during feature extraction.

- **hsv_v = 0.6**: The brightness (value) variation range was increased
  to more aggressively simulate the natural illumination changes typical
  of outdoor environments, such as overcast conditions versus direct
  sunlight exposure.

- **translate = 0.05**: The spatial translation parameter was
  significantly reduced. Excessive image displacement could cause
  oranges originally located on background trees (and deliberately left
  unannotated according to the curation criteria) to shift into the
  foreground, inducing erroneous model predictions.

- **mosaic = 0.7**: The probability of applying the mosaic augmentation
  technique (which combines four images into one) was reduced for the
  same contextual reason: to avoid generating artificial patches that
  incoherently mix foreground and background trees.

The results of applying this updated configuration across the full
YOLO11 family are detailed in Table
[4.2](#tab:yolos_modificado){reference-type="ref"
reference="tab:yolos_modificado"}:

  **Model**     **Precision**   **Recall**   **F1-score**   **mAP@0.50**   **mAP@0.50:95**   **Parameters**   **FPS**   **Batch size**
  ----------- --------------- ------------ -------------- -------------- ----------------- ---------------- --------- ----------------
  YOLO11n               0.823        0.683          0.746          0.741             0.409             2.6M     9.890                4
  YOLO11s               0.810        0.726          0.766          0.772             0.436             9.4M     4.480                2
  YOLO11m               0.831        0.701          0.760          0.769             0.438            20.1M     1.870                1
  YOLO11l               0.815        0.724          0.767          0.777             0.441            25.3M     1.460                1
  YOLO11x               0.822        0.725          0.770          0.777             0.441            56.9M     0.749                1

  : Results of YOLO11 models with modified parameters on the validation
  set ($conf=0.01$, $IoU=0.50$). {#tab:yolos_modificado}

A comparative analysis between Table
[4.2](#tab:yolos_modificado){reference-type="ref"
reference="tab:yolos_modificado"} and the baseline configuration (Table
[4.1](#tab:yolos_defecto){reference-type="ref"
reference="tab:yolos_defecto"}) reveals that the training modifications
did not yield a significant overall performance improvement. While
slight gains in the precision-recall balance are observed, global
metrics such as mAP@0.50 remain highly stable across all architectures.

For the selected model, YOLO11s, the improvement is nearly negligible:
mAP@0.50 increases from 0.769 to 0.772, and the F1-score rises
marginally from 0.756 to 0.766. These findings suggest that, under the
evaluated configurations, architectural capacity may be a more
influential factor than explored hyperparameter modifications.

Modern network default configurations already exhibit exceptional
robustness, meaning that final performance depends primarily on network
depth and its internal feature extraction mechanisms. This phenomenon
becomes even more evident when examining the best result from the table:
after applying all chromatic and geometric modifications, the large and
extra-large variants converge to an identical predictive ceiling
(mAP@0.50 of 0.777).

To visually corroborate these findings, Figure
[4.1](#fig:yolos_comparison){reference-type="ref"
reference="fig:yolos_comparison"} illustrates the empirical behavior of
the macro F1-score across the entire YOLO11 architectural spectrum,
directly contrasting the default training configurations against the
custom-tailored agricultural hyperparameter set.

<figure id="fig:yolos_comparison" data-latex-placement="H">
<img src="images/YOLOS.jpg" style="width:100.0%" />
<figcaption>Comparison of the YOLO models: default parameters vs.
modified parameters.</figcaption>
</figure>

In summary, these results reaffirm that the structural complexity of the
problem (characterized by high fruit density, occlusion, and chromatic
camouflage) cannot be resolved simply by forcing data augmentation
parameters or injecting tens of millions of additional parameters. Given
this architectural performance ceiling, computational efficiency becomes
an even more decisive factor, further consolidating YOLO11s as the most
logical, well-reasoned, and justified baseline model for the final
comparison against open-vocabulary detectors. It must be explicitly
noted that due to the computational constraints of the project, these
results are derived from a single training execution per configuration.
Consequently, the small numerical variations observed between the models
(such as the 0.005 mAP@0.50 delta between YOLO11m and YOLO11l) should be
interpreted with caution, as they lack a multi-run statistical
evaluation to confirm their significance.

## Detailed Analysis of the Winning Model

Having established that the small variant offers the most well-balanced
trade-off between predictive capacity and computational cost, this
architecture is consolidated as the reference baseline. Although the
customized hyperparameter configuration yielded marginally superior
metrics (an increase of 0.010 in F1-score and 0.003 in mAP@0.50), the
default parameter set was selected to establish the baseline. This
decision is justified by the fact that the performance differential is
small enough to be considered within the margin of experimental
variance, and adhering to the standard configuration minimizes the risk
of hyperparameter overfitting to the training split, thereby ensuring a
more robust and generalizable reference model. Table
[4.3](#tab:baseline_results){reference-type="ref"
reference="tab:baseline_results"} presents the model results, now broken
down by class:

  **Class**          **Precision**   **Recall**   **F1-score**   **mAP@0.50**   **mAP@0.50:95**
  ---------------- --------------- ------------ -------------- -------------- -----------------
  All                        0.814        0.705          0.756          0.769             0.431
  *Naranja*                  0.790        0.678          0.730          0.751             0.421
  *NaranjaVerde*             0.837        0.733          0.782          0.787             0.442

  : Results of the YOLO11s model on the validation set ($conf=0.01$,
  $IoU=0.50$). The best model weights were achieved at epoch 65.
  {#tab:baseline_results}

At first glance, the results reveal a strong overall performance, with a
high global precision of 0.814 and a mAP@0.50 of 0.769. However, the
per-class breakdown presents an interesting finding: the model performs
better at detecting the *NaranjaVerde* class (mAP@0.50 of 0.787,
F1-score of 0.782) than the *Naranja* class (mAP@0.50 of 0.751, F1-score
of 0.730). While this may appear counterintuitive given the severe
chromatic camouflage that immature fruit shares with the surrounding
foliage, the explanation lies in the characteristics of the dataset
itself. Instances of the *NaranjaVerde* class are generally more
visually salient than those of the *Naranja* class, which contains many
instances that are nearly imperceptible to the human eye and
consequently highly challenging for the model to detect.

Nevertheless, while these metrics provide a useful quantitative summary
of model performance, they do not shed light on the model's internal
dynamics or the nature of its errors. For instance, the global recall of
0.705 suggests that a significant proportion of instances are being
missed. To fully understand how the model behaves under the uncertainty
of unseen images, and to identify the specific types of failures being
made (such as confusion with the background or inter-class
misclassification) it is necessary to further examine its performance
curves and confusion matrix.

### Precision-Recall (PR) Curve Analysis

The Precision-Recall curve illustrates the model's ability to maintain
accurate predictions as it is required to detect a progressively larger
proportion of objects. As shown in Figure
[4.2](#fig:pr_baseline){reference-type="ref"
reference="fig:pr_baseline"}, the curve remains high and stable (close
to 1.0 on the Y-axis) up to approximately a recall of 0.6, at which
point a notable drop is observed. This indicates that the model is
highly precise when detecting the most visible or largest fruit
instances but struggles to detect all instances present in the dataset.

<figure id="fig:pr_baseline" data-latex-placement="H">
<img src="images/yolo/BoxPR_curve.jpg" style="width:80.0%" />
<figcaption>PR curve of the baseline model.</figcaption>
</figure>

### F1-Confidence Curve Analysis

This metric identifies the optimal trade-off between avoiding incorrect
predictions (precision) and ensuring that no fruit instances go
undetected (recall). As shown in Figure
[4.3](#fig:f1_baseline){reference-type="ref"
reference="fig:f1_baseline"}, this global optimum (F1-score of 0.76) is
reached at a confidence threshold of 0.337, revealing that the model
assigns relatively conservative confidence scores. Beyond thresholds
exceeding 0.4, a sharp performance drop occurs as the model begins to
discard correct but uncertain detections, a behavior typically
associated with partially occluded fruit.

This confidence threshold of 0.337 will be used in Chapter
[6](#comparativa_test){reference-type="ref"
reference="comparativa_test"} to evaluate the model's behavior on the
test set, assessing its overall performance on this independent
evaluation partition.

<figure id="fig:f1_baseline" data-latex-placement="H">
<img src="images/yolo/BoxF1_curve.jpg" style="width:80.0%" />
<figcaption>F1-Confidence curve of the baseline model.</figcaption>
</figure>

### Confusion Matrix Analysis

The confusion matrix reveals the types of errors committed by the model.
As shown in Figure [4.4](#fig:matriz_baseline){reference-type="ref"
reference="fig:matriz_baseline"}, the system demonstrates a strong
ability to distinguish between ripe and unripe fruit. Out of thousands
of predictions, only 232 *Naranja* instances are misclassified as
*NaranjaVerde* and only 79 *NaranjaVerde* instances are misclassified as
*Naranja*, demonstrating that the network has effectively addressed the
chromatic camouflage challenge.

On the other hand, examining the background column reveals the model's
primary limitation: numerous background regions were predicted as fruit,
generating a high volume of false positives. However, this is expected
given the low confidence threshold applied during validation, which
forces the model to report any minimal detection signal. As will be
detailed in Chapter [6](#comparativa_test){reference-type="ref"
reference="comparativa_test"}, once the definitive operational
confidence threshold is applied, this noise should be substantially
reduced and uncertain detections filtered out.

Conversely, false negatives (real fruit instances classified as
background) are notably low (384 of *Naranja* and 499 of
*NaranjaVerde*), indicating that the model is quite robust in terms of
fruit recall, missing very few instances overall.

<figure id="fig:matriz_baseline" data-latex-placement="H">
<img src="images/yolo/confusion_matrix.jpg" style="width:100.0%" />
<figcaption>Confusion matrix of the baseline model (absolute instance
counts).</figcaption>
</figure>

## Evaluation of Alternative Architectures: RT-DETR and YOLO26

To further validate the selection of YOLO11 as the baseline
architecture, experiments were conducted on two additional object
detection architectures: RT-DETR, a Transformer-based detector, and
YOLO26, one of the most recent proposals from Ultralytics. The objective
of these secondary experiments is to assess whether either alternative
would offer a competitive advantage over YOLO11 for this agricultural
use case.

### RT-DETR (Real-Time Detection Transformer) Evaluation

Both available variants of this model were evaluated: large and
extra-large. The same default training criteria applied to YOLO11 were
used. The results obtained on the validation set are presented in Table
[4.4](#tab:detr_baseline_valid){reference-type="ref"
reference="tab:detr_baseline_valid"}. The large variant achieves a
mAP@0.50 of 0.745 and an F1-score of 0.749, while the extra-large
variant yields a mAP@0.50 of 0.697 and an F1-score of 0.712, both
falling below the metrics obtained with YOLO11. One possible explanation
is that architectures relying exclusively on attention mechanisms may
struggle with local feature extraction in this scenario.

  **Model**     **Precision**   **Recall**   **F1-score**   **mAP@0.50**   **mAP@0.50:95**   **FPS**   **Batch size**
  ----------- --------------- ------------ -------------- -------------- ----------------- --------- ----------------
  RT-DETR-l             0.803        0.702          0.749          0.745             0.429     0.885                1
  RT-DETR-x             0.775        0.658          0.712          0.697             0.401     0.525                1

  : Results of the RT-DETR model on the validation set ($conf=0.01$,
  $IoU=0.50$). {#tab:detr_baseline_valid}

### YOLO26 Evaluation

Ultralytics recently released YOLO26, a new iteration of the YOLO family
that promises more efficient performance for edge computing devices, a
characteristic well-aligned with the objectives of this work. However,
given its recent release and the fact that the project was already in an
advanced stage of development, a decision was made not to adopt this
model as the baseline. Nevertheless, it was deemed relevant to evaluate
it to assess how it would have performed on this use case.

All available variants were tested (nano, small, medium, large, and
extra-large), as shown in Table
[4.5](#tab:yolos26_defecto){reference-type="ref"
reference="tab:yolos26_defecto"}. The results demonstrate generally
strong performance, comparable to that of YOLO11. While these figures
marginally exceed the peak performance achieved by YOLO11 (mAP@0.50 of
0.777), the performance differential does not justify an architectural
change at this stage of the project. In fact, a direct comparison at the
small variant level (selected as the YOLO11 baseline) reveals that
YOLO26s exhibits a drop of 0.020 in both F1-score and mAP@0.50.

  **Model**     **Precision**   **Recall**   **F1-score**   **mAP@0.50**   **mAP@0.50:95**   **Parameters**   **FPS**   **Batch size**
  ----------- --------------- ------------ -------------- -------------- ----------------- ---------------- --------- ----------------
  YOLO26n               0.789        0.657          0.717          0.713             0.395               2M    10.000                3
  YOLO26s               0.799        0.682          0.736          0.749             0.428              10M     4.260                1
  YOLO26m               0.825        0.711          0.764          0.782             0.447              20M     1.830                1
  YOLO26l               0.804        0.716          0.757          0.778             0.447              25M     1.460                1
  YOLO26x               0.810        0.731          0.768          0.792             0.457              55M     0.750                1

  : Results of YOLO26 models on the validation set ($conf=0.01$,
  $IoU=0.50$). {#tab:yolos26_defecto}

### Conclusions

The results presented in this section reaffirm the viability of the
initial architectural decision. RT-DETR is discarded due to its lower
accuracy and greater complexity for this specific problem. YOLO26, while
promising, offers only marginal gains that do not justify restructuring
the work around a new architecture. As a result, YOLO11 is firmly
maintained as the closed-vocabulary reference model, providing an ideal
balance between library stability, predictive accuracy, and operational
feasibility for establishing the supervised reference against the OVOD
models.

# Evaluation of Open-Vocabulary Object Detection (OVOD) Models {#cap:ovod}

This chapter analyzes the performance of various open-vocabulary object
detection (OVOD) models on the validation set of the dataset described
in Chapter [3](#dataset){reference-type="ref" reference="dataset"}, the
same dataset used for baseline model selection in Chapter
[4](#baseline_ch){reference-type="ref" reference="baseline_ch"}. The
purpose of this analysis is to evaluate the generalization capabilities
of these architectures under a zero-shot paradigm (without any prior
task-specific training). Subsequently, in Chapter
[6](#comparativa_test){reference-type="ref"
reference="comparativa_test"}, .a direct comparative evaluation of these
models against the baseline will be conducted on the held-out test set,
in order to assess their performance on unseen data drawn from the same
source. To ensure a controlled and unbiased comparative analysis, all
model evaluations were conducted using the identical infrastructure
described in Appendix [10](#execution_environment){reference-type="ref"
reference="execution_environment"}.

## Introduction to OVOD Architectures

The critical analysis in Section
[2.4.3](#ausencia_datasets){reference-type="ref"
reference="ausencia_datasets"} identified a clear gap in the current
literature: while closed-vocabulary detectors such as YOLO11
[6.3](#fig:mc-yolo11){reference-type="ref" reference="fig:mc-yolo11"}
achieve strong performance within a fixed label space, they are
fundamentally constrained by the categories seen during training. This
makes them highly inflexible when encountering new crop varieties or
seasonal shifts. Open-vocabulary architectures address this limitation
by aligning visual features with natural language representations,
enabling zero-shot recognition of arbitrary concepts. However, the
landscape of OVOD models is heterogeneous: architectures differ
substantially in their design, from real-time CNN-based detectors to
heavy Vision Transformer pipelines and from native bounding-box
regressors to segmentation-derived detectors. This diversity makes a
direct empirical comparison not only valuable but necessary to determine
which family of approaches is best suited for precision agriculture
deployment.

For this study, five architectures were selected to represent the
principal technical lineages identified in Chapter
[2](#state-of-the-art){reference-type="ref"
reference="state-of-the-art"}, ensuring that the comparison spans the
full design space of contemporary OVOD systems:

- **YOLO-World [@cheng2024yolo]**: Built on a real-time CNN
  architecture, it employs a conventional detection head for coordinate
  regression. By integrating text labels into the model weights through
  the Reparameterizable Vision-Language Path, the model directly
  predicts tensors with values $[x,y,w,h]$, enabling inference speeds
  equivalent to those of a closed-vocabulary model.

- **YOLOE [@Wang_2025_ICCV]**: A direct evolution of YOLO-World that
  unifies detection and segmentation under three prompt mechanisms:
  text, visual, and prompt-free. Through RepRTA reparameterization, it
  processes large text vocabularies at zero additional inference cost,
  operating as a standard closed detector once the vocabulary is
  defined. Its SAVPE visual prompt encoder further enables object
  detection from image exemplars, making it particularly useful when a
  concept is difficult to describe linguistically.

- **Grounding DINO [@liu2024grounding]**: Combines the DINO detector
  with grounding pre-training to establish visual-linguistic
  correspondence. Unlike CNN-based models, it employs a
  Transformer-based decoder to predict a fixed set of candidate boxes
  aligned with text phrases, exhibiting strong robustness to occlusion
  and complex spatial relationships.

- **OWLv2 [@NEURIPS2023_e6d58fc6]**: Leverages a Vision Transformer
  (ViT) and large-scale web pre-training on billions of examples, using
  N-grams extracted from image alt-text as detection queries. It
  incorporates optimizations such as token dropping and objectness
  heads, which halve the computational cost by prioritizing the
  processing of regions with a high likelihood of containing objects.

- **SAM 3 [@sam3_2025]**: Does not operate as a traditional bounding box
  detector, but rather as a Promptable Concept Segmentation (PCS)
  system. Given a text prompt (short noun phrases) or visual exemplars
  (positive or negative boxes), it detects, segments, and tracks all
  instances of a concept while preserving their identity across frames
  in both images and video. Its Presence Token decouples recognition
  from localization, substantially reducing false positives when the
  target concept is absent from the scene.

## Analysis Strategy {#sec:metodologia_experimental}

To ensure that the comparison across architectures is consistent and
reproducible, all models are evaluated following the same experimental
sequence. Each stage introduces a single controlled change relative to
the previous one, so that the effect of each decision is isolated and
can be interpreted independently.

The base configuration shared across all stages is as follows: minimum
confidence threshold of $0.01$, model-internal NMS disabled (except in
SAM 3, where it is not configurable). To establish a starting point, an
initial baseline global NMS threshold of $0.50$ is enforced during the
first two stages before dynamic optimization. Applying this global NMS
in a standardized manner ensures that the metrics at each stage remain
comparable; without it, the same object could be counted multiple times,
distorting the results.

The input resolution is fixed to the native resolution of each model,
except for YOLO-World and YOLOE, for which a resolution of $1280$ px is
used (their native resolution being 640 px). This choice is justified by
the fact that these models demonstrably benefit from higher input
resolutions.

The primary evaluation metrics are Precision, Recall, F1-score, mAP@0.50
and mAP@0.50:95, computed both per class (*Naranja*, *NaranjaVerde*) and
globally. The F1-score is prioritized as the selection metric across all
stages, as it combines precision and recall into a single measure,
making it particularly well-suited for a problem whose core objective is
fruit counting alongside ripeness classification. Furthermore, running
all stages with $conf = 0.01$ ensures that the evaluator receives the
full set of possible detections, capturing the complete precision-recall
spectrum before operational thresholding, in alignment with evaluation
protocols in standardized benchmarks. However, executing this parameter
optimization (specifically prompt selection, tiling choices, and NMS
thresholds) sequentially under this fixed confidence baseline introduces
a distinct methodological limitation. This sequential approach prevents
a combinatorial explosion but may inherently favor model configurations
whose native confidence scores happen to be better calibrated at this
low threshold.

### Algorithmic Evaluation Pipeline and Post-Processing Mechanics

To ensure an unbiased and standardized comparative evaluation across all
open-vocabulary candidates, a rigorous evaluation pipeline was
developed. The operational mechanics of the predictions, spatial
filtering, and ground truth matching are defined as follows:

- **Prediction-to-Annotation Matching**: The matching mechanism between
  the predicted bounding boxes and the manually curated ground truth
  labels is executed via a greedy assignment algorithm. A prediction is
  validated as a True Positive ($TP$) if and only if its spatial overlap
  with an unassigned ground truth instance satisfies a strict
  Intersection over Union threshold of $0.50$.

- **Class-Agnostic Non-Maximum Suppression (NMS)**: Due to the high
  density of the orchard canopy, a major operational risk is semantic
  duplication, where a single fruit instance is simultaneously labeled
  under multiple categories. To actively mitigate this issue, the
  spatial filtering step applies a global, class-agnostic NMS layer.
  Predictions from all target vocabularies are consolidated into a
  single candidate pool prior to suppression; if two overlapping boxes
  compete for the same physical coordinates, the bounding box with the
  lower absolute confidence score is discarded regardless of its
  categorical index, effectively preventing multi-class overlapping
  anomalies.

- **Grounding DINO Dual-Pass and Profiling Integration**: To eliminate
  linguistic ambiguity within the text encoder, Grounding DINO is
  executed via two sequential independent forward passes per image (one
  optimized for the mature fruit prompt and another for the unripe green
  fruit prompt). The outputs of both passes are concatenated into a
  unified tensor immediately before the global NMS stage. Crucially, the
  inference throughput metrics (FPS) reported for this architecture
  encompass the entire cumulative workload, as the hardware timing block
  is wrapped around both sequential visual inferences and the spatial
  consolidation layer, fully synchronized via CUDA stream checkpoints to
  guarantee precise latency profiling.

- **SAM 3 Mask-to-BBox Conversion**: To evaluate the promptable concept
  segmentation outputs of SAM 3 alongside native bounding-box
  regressors, a geometric conversion layer was implemented. For every
  isolated pixel-wise binary mask generated by the segmentation head,
  the algorithm extracts the exact spatial boundaries by computing its
  axis-aligned minimum bounding rectangle, defined by the extreme
  horizontal and vertical coordinates
  $[x_{\min}, y_{\min}, x_{\max}, y_{\max}]$.

### Stage 1 --- Prompt Ablation {#niveles_prompt}

Six prompt levels, shown in Table
[5.1](#tab:prompts){reference-type="ref" reference="tab:prompts"}, are
evaluated on the validation set in order of increasing descriptive
complexity. The objective is to identify which type of textual
description yields the best performance for each architecture, given
that open-vocabulary models are highly sensitive to this choice.

An important consideration in this stage is that long, conversational,
or instruction-heavy prompts (of the kind typically used with VLM models
such as Qwen-VL) were deliberately avoided. This decision is purely
architectural in nature. Unlike VLMs, which rely on a large language
model (LLM) capable of reasoning over extended text, OVOD models employ
contrastive encoders such as CLIP. These encoders are trained for a
considerably simpler and more direct task: matching image regions to
short phrases. Providing an excessively long description or
syntactically complex phrasing causes the resulting embedding (the
mathematical representation of the text) to become diluted, leading to
degraded model performance. Furthermore, doing so makes it easy to
exceed the token limit supported by these encoders, causing detection
accuracy to drop sharply. For this reason, the prompts designed for
these experiments are concise and direct, restricted to precise
adjective variations, specific visual characteristics, and minimal
negative context where applicable.

  **Prompt**   **Class 0 (*Naranja*)**                          **Class 1 (*NaranjaVerde*)**
  ------------ ------------------------------------------------ -------------------------------------------------
  P1           `orange`                                         `green orange`
  P2           `ripe orange`                                    `unripe orange`
  P3           `ripe orange citrus fruit`                       `green unripe citrus fruit`
  P4           `spherical orange`                               `spherical green orange`
  P5           `spherical ripe orange citrus fruit on a tree`   `spherical green unripe citrus fruit on a tree`
  P6           `orange, not a leaf, not a branch`               `green orange, not a leaf, not a branch`

  : The six prompt levels evaluated in Stage 1. {#tab:prompts}

The prompt that maximizes the F1-score is adopted as the reference
configuration for the subsequent stages.

### Stage 2 --- Tiling Evaluation

Once the optimal prompt is established in the previous stage, the next
logical step is to assess whether processing images in a grid-based
fashion (a technique known as tiling) improves detection performance.

The technical justification for introducing this evaluation lies in the
inherent nature of the dataset. The problem is visually complex,
characterized by an extremely high instance density: numerous oranges
clustered together, often small relative to the total image size. When
the full image is fed to the model in a single pass, it must typically
be downscaled to fit the model's native input resolution, causing
fine-grained details to be lost and heavily occluded fruit to be
overlooked

To assess whether the model performs better when focusing on smaller
image regions, a tiling strategy was implemented that divides the
original image into patches of 1280 $\times$ 1280 pixels. To mitigate
the classic boundary problem, where an object located at the edge of a
patch is split across two tiles and goes undetected, an overlap of 256
pixels was configured between adjacent patches.

This stage, therefore, compares model performance when processing the
full image in a single forward pass against processing it through these
overlapping patches, while keeping all remaining configuration
parameters strictly identical in order to precisely isolate the impact
of this technique.

### Stage 3 --- NMS Threshold Sweep

With the optimal prompt and tiling configuration already established,
the third stage focuses on analyzing the model's sensitivity to the
global NMS IoU threshold. Rather than performing a sweep over a fixed
set of predefined values, an iterative search strategy was adopted to
locate the performance peak more efficiently.

Three evenly spaced reference values are initially evaluated: 0.4, 0.5,
and 0.6 (with confidence fixed at 0.01). Based on the results of this
first evaluation, the trend of the F1-score metric is analyzed. If
performance shows an upward trend toward the lower bound (0.4), the
search continues by testing progressively lower values. Conversely, if
the metric improves toward the upper bound (0.6), the search expands
toward higher thresholds. This process is repeated until the exact
inflection point at which the F1-score reaches its empirical peak is
identified, at which point that value is adopted as the definitive NMS
threshold for all final inferences.

### Stage 4 --- Confidence Threshold Selection

Once the optimal configuration from the preceding stages has been
consolidated (combining the appropriate prompt, tiling strategy, and
tuned NMS threshold), the final step before the definitive evaluation
consists of determining the model's operating confidence threshold. To
this end, the F1-Confidence curve is generated on the validation set.

A real-world deployment scenario requires a single fixed cutoff value.
Consequently, the confidence threshold that maximizes the macro F1-score
is established as the definitive operational threshold for inference on
the test set, as it provides the best balance between Precision and
Recall across both classes under a deployment-oriented setting. It
should be noted, however, that the F1-scores reported in the previous
stages are computed with a fixed confidence threshold of 0.01 to ensure
methodological comparability across prompt, tiling, and NMS analyses,
whereas this final step determines the model's true operating point.
This optimal value is derived analytically from the predictions already
generated in the previous stage and, as a result, requires neither
additional experiments nor extra computational cost.

### Experimental Workflow Summary

Figure [5.1](#fig:flujo_experimentos){reference-type="ref"
reference="fig:flujo_experimentos"} summarizes the complete
methodological sequence. Architecture-specific experiments are added as
sub-stages within the corresponding phase and are documented in their
dedicated sections.

<figure id="fig:flujo_experimentos" data-latex-placement="H">

<figcaption>Sequential experimental workflow applied to each model.
Stages 1–3 are executed with <span
class="math inline"><em>c</em><em>o</em><em>n</em><em>f</em> = 0.01</span>.
Stage 4 determines the operational threshold for the final evaluation on
the <em>test</em> set.</figcaption>
</figure>

## Grounding DINO

This section presents the evaluation of the Grounding DINO model
following the experimental workflow described in Section
[5.2](#sec:metodologia_experimental){reference-type="ref"
reference="sec:metodologia_experimental"}. Since this Transformer-based
architecture is highly sensitive to variations in input resolution, its
original native resolution ($\sim 800 \times 800$ pixels) was preserved
throughout all experiments. Two architectural variants are evaluated in
this study: Tiny and Base. The configuration yielding the highest
performance will be selected for the final comparative evaluation in
Chapter [6](#comparativa_test){reference-type="ref"
reference="comparativa_test"}.

##### **Dual-pass inference strategy:**

As fundamentally defined in our algorithmic pipeline section, Grounding
DINO requires specific operational handling due to text-encoder
constraints. By default, if the model receives prompts for all classes
simultaneously, shared vocabulary tokens (such as the word \"orange\"
appearing in both \"spherical orange\" and \"spherical green orange\")
can saturate the visual-linguistic alignment matrix, inducing high
inter-class overlap. To bypass this linguistic ambiguity, the dual-pass
inference strategy is strictly executed, isolating the channels into
separate forward passes before spatial consolidation. As a consequence
of this architectural safeguarding, the absolute computational
throughput is halved

### Grounding DINO Tiny

Grounding DINO Tiny is the lightest variant of the model, employing a
Swin-Tiny backbone with 86M parameters. Its design prioritizes
efficiency, achieving higher inference speed and lower computational
resource consumption.

#### Prompt Ablation: Grounding DINO Tiny

As shown in Table [5.2](#tab:prompts_gdt){reference-type="ref"
reference="tab:prompts_gdt"}, although the quantitative differences
across the evaluated prompts are minimal, configuration P6 ("orange, not
a leaf, not a branch", "green orange, not a leaf, not a branch")
slightly outperforms the rest, achieving the highest F1-score of 0.067.
The results indicate that, rather than benefiting from functionally
descriptive phrases, the architecture performs most effectively when
provided with restrictive, negative context. In a highly dense and
occluded agricultural dataset, purely morphological or standard
descriptive prompts tend to generate confusion with the surrounding
foliage. By supplying negative constraints (P6), the model's
cross-modality alignment is guided to better discriminate the actual
fruit from the background, thereby maximizing both Precision (0.038) and
Recall (0.294) within this narrow margin. Therefore, P6 is established
as the reference prompt for the subsequent experiments.

  **Prompt**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  ------------ --------------- ------------ -------- -------------- -----------------
  P1                     0.034        0.278    0.060          0.078             0.046
  P2                     0.034        0.273    0.060          0.078             0.046
  P3                     0.027        0.272    0.048          0.086             0.049
  P4                     0.031        0.272    0.056          0.070             0.042
  P5                     0.024        0.267    0.044          0.079             0.045
  P6                     0.038        0.294    0.067          0.073             0.040

  : Prompt ablation on the validation set. Model: Grounding DINO Tiny.
  {#tab:prompts_gdt}

Figure [5.2](#fig:prompt-gdt){reference-type="ref"
reference="fig:prompt-gdt"} provides a visual representation of the
performance variations across the evaluated prompts. As illustrated,
configuration P6 exhibits a notably higher peak, reaching a maximum
F1-score of 0.067. In contrast, other descriptive configurations
experience considerable drops in performance, with P3 and P5 falling to
0.048 and 0.044, respectively. Consequently, P6 is definitely
established as the reference prompt for all subsequent experiments.

<figure id="fig:prompt-gdt" data-latex-placement="H">
<img src="images/groundingDino/gdt-prompts.jpg" style="width:100.0%" />
<figcaption>Prompt comparison for the Grounding DINO Tiny
model.</figcaption>
</figure>

#### Tiling Evaluation: Grounding DINO Tiny

The introduction of the tiling strategy reveals a critical behavioral
characteristic of this architecture. As shown in Table
[5.3](#tab:tiling_gdt){reference-type="ref" reference="tab:tiling_gdt"},
the patches cause a severe performance collapse, where the F1-score
drops drastically from 0.067 to 0.008, despite a significant improvement
in Recall. This degradation is accompanied by an unacceptable inference
speed penalty, reducing performance from 1.49 FPS to 0.05 FPS. This
suggests that Grounding DINO relies heavily on global self-attention
mechanisms, inherent to Vision Transformers, to establish the complete
visual context before grounding it to the text. By fragmenting the image
into patches, the global context is destroyed, preventing the model from
correctly relating the size and spatial distribution of objects. Thus,
the tiling strategy is discarded for this architecture.

  **Configuration**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**   **FPS**
  ------------------- --------------- ------------ -------- -------------- ----------------- ---------
  No tiling                     0.038        0.294    0.067          0.073             0.040     1.490
  Tiling                        0.004        0.436    0.008          0.067             0.038     0.050

  : Tiling evaluation on the validation set. Prompt P6. Model: Grounding
  DINO Tiny. {#tab:tiling_gdt}

#### NMS Threshold Sweep: Grounding DINO Tiny

The model's sensitivity to the Non-Maximum Suppression (NMS) threshold
was subsequently analyzed. Table
[5.4](#tab:nms_gdt){reference-type="ref" reference="tab:nms_gdt"}
reveals a clear performance improvement trend as the threshold becomes
increasingly restrictive, reaching an empirical peak at an NMS of 0.01
(F1 = 0.156).

An NMS threshold of 0.01 is exceptionally low and indicates that the
model tends to generate multiple highly overlapping bounding boxes over
the same fruit instance. By applying an almost zero NMS threshold,
redundant predictions are aggressively suppressed. This explains the
qualitative improvement observed: Precision nearly triples (from 0.038
to 0.120) without a critical penalty in Recall (0.224). This
configuration is consolidated as the definitive setup for comparison
against the Base variant.

  **NMS**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**          
  --------- --------------- ------------ -------- -------------- ----------------- -- -- -- --
  0.01                0.120        0.224    0.156          0.072             0.039          
  0.1                 0.095        0.258    0.138          0.076             0.041          
  0.2                 0.074        0.273    0.117          0.076             0.041          
  0.3                 0.060        0.280    0.098          0.076             0.041          
  0.4                 0.048        0.288    0.082          0.075             0.041          
  0.5                 0.038        0.294    0.067          0.073             0.040          
  0.6                 0.031        0.298    0.056          0.071             0.039          

  : NMS threshold sweep on the validation set. Prompt P6, tiling
  disabled. Model: Grounding DINO Tiny. {#tab:nms_gdt}

### Grounding DINO Base

This variant employs a higher-capacity Swin-Base backbone, reaching 145M
parameters. Its increased architectural depth enables the extraction of
more complex visual features and provides higher accuracy in detecting
challenging objects, at the cost of greater computational demand.

#### Prompt Ablation: Grounding DINO Base

The results presented in Table
[5.5](#tab:prompts_gdb){reference-type="ref"
reference="tab:prompts_gdb"} reveal a significant shift in behavior
compared to the Tiny version. For the Base architecture, the optimal
configuration is P5 ("spherical ripe orange citrus fruit on a tree\",
"spherical green unripe citrus fruit on a tree"), which achieves the
highest overall F1-score of 0.135. Compared to the lighter model, the
Base architecture demonstrates a strong sensitivity to vocabulary,
resulting in sharp performance contrasts across the different prompts.

Interestingly, the model also shows high proficiency with the concise P2
prompt (achieving an F1-score of 0.130). This indicates that its more
powerful backbone has the representational capacity to associate the
visual concept directly with the fruit's ripeness state. However, to
reach its optimal performance, the model requires exhaustive spatial
context. By introducing the environmental cue (\"on a tree\") in P5, the
architecture's cross-modality alignment is significantly enhanced,
boosting Recall to its peak value of 0.399. This spatial grounding
allows the model to identify heavily occluded fruits that are deeply
embedded in the background, which simpler prompts miss.

  **Prompt**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  ------------ --------------- ------------ -------- -------------- -----------------
  P1                     0.051        0.305    0.066          0.134             0.071
  P2                     0.099        0.289    0.130          0.138             0.075
  P3                     0.048        0.312    0.067          0.135             0.074
  P4                     0.049        0.315    0.073          0.142             0.076
  P5                     0.084        0.399    0.135          0.190             0.100
  P6                     0.058        0.348    0.099          0.153             0.081

  : Prompt ablation on the validation set. Model: Grounding DINO Base.
  {#tab:prompts_gdb}

Figure [5.3](#fig:prompt-gdb){reference-type="ref"
reference="fig:prompt-gdb"} visually illustrates this distinct prompt
sensitivity. The F1-score trend exhibits two clear peaks at P2 and P5,
demonstrating that the Base model is better on highly direct
descriptions or on exhaustive, spatially contextualized ones.
Conversely, applying purely negative constraints (P6) or unbalanced
intermediate descriptions (P3, P4) disrupts the semantic alignment,
causing sharp drops in performance. Consequently, P5 is established as
the chosen reference prompt for the Grounding DINO Base architecture in
all subsequent experiments.

<figure id="fig:prompt-gdb" data-latex-placement="H">
<img src="images/groundingDino/gdb-prompts.jpg" style="width:100.0%" />
<figcaption>Prompt comparison for the Grounding DINO Base
model.</figcaption>
</figure>

#### Tiling Evaluation: Grounding DINO Base

With the prompt P5 fixed, the tiling strategy was evaluated. As shown in
Table [5.6](#tab:tiling_gdb){reference-type="ref"
reference="tab:tiling_gdb"}, applying tiling drastically reduces the
overall F1-score from 0.135 to 0.014, while concurrently incurring a
severe inference speed penalty (dropping from 1.49 FPS to an inoperable
0.05 FPS).

A closer inspection of the metric breakdown reveals that, although
Recall increases (from 0.399 to 0.556), indicating an improved detection
of smaller or occluded fruits within the cropped patches, Precision
completely collapses (from 0.084 to just 0.007). This confirms the
hypothesis established in the Tiny variant: fragmenting the image
severely disrupts the Transformer's global self-attention mechanism.
Deprived of the full environmental context, which is especially critical
for a spatially grounded prompt like P5 (\"on a tree\"), the model loses
its discriminative capacity and generates a massive number of false
positives across the foliage. Thus, the tiling strategy remains disabled
for this architecture.

  **Configuration**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**   **FPS**
  ------------------- --------------- ------------ -------- -------------- ----------------- ---------
  **No tiling**                 0.084        0.399    0.135          0.190             0.100     1.490
  Tiling                        0.007        0.556    0.014          0.140             0.074     0.050

  : Tiling evaluation on the validation set. Prompt P5. Model: Grounding
  DINO Base. {#tab:tiling_gdb}

#### NMS Threshold Sweep: Grounding DINO Base {#subsec:gd_nms}

Finally, the model's sensitivity to the NMS threshold was analyzed. As
shown in Table [5.7](#tab:nms_gdb){reference-type="ref"
reference="tab:nms_gdb"}, peak performance is achieved at an extremely
restrictive NMS threshold of 0.01, yielding the highest overall F1-score
of 0.249.

Interestingly, this optimal threshold perfectly mirrors the behavior
observed in the Tiny variant. This suggests that, despite possessing a
stronger backbone and improved representational capacity, the Base
architecture still generates a massive volume of highly overlapping
bounding boxes per instance when operating in a dense agricultural
environment. The metric breakdown clearly illustrates this phenomenon:
as the NMS threshold relaxes (increasing from 0.01 to 0.6), Recall
experiences a moderate increase (from 0.319 to 0.402), indicating that
more heavily occluded fruits are being detected. However, this comes at
the cost of a severe collapse in Precision (dropping abruptly from 0.237
to 0.067). Therefore, ultra-aggressive redundancy filtering remains a
critical requirement for this architecture to effectively mitigate false
positives and reach its optimal performance peak.

  **NMS**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**          
  --------- --------------- ------------ -------- -------------- ----------------- -- -- -- --
  0.01                0.237        0.319    0.249          0.171             0.090          
  0.1                 0.197        0.364    0.234          0.191             0.100          
  0.2                 0.159        0.378    0.208          0.195             0.101          
  0.3                 0.128        0.383    0.182          0.192             0.101          
  0.4                 0.104        0.392    0.158          0.192             0.100          
  0.5                 0.084        0.399    0.135          0.190             0.100          
  0.6                 0.067        0.402    0.113          0.185             0.099          

  : NMS threshold sweep on the validation set. Prompt P5, tiling
  disabled. Model: Grounding DINO Base. {#tab:nms_gdb}

### Optimal Configuration Analysis: Grounding DINO {#subsec:gd_optimo}

Table [5.8](#tab:gd_modelos){reference-type="ref"
reference="tab:gd_modelos"} summarizes the final validation results for
the optimal configurations of both variants. The comparative analysis
reveals a clear superiority of the Base version, which achieves an
F1-score of 0.249, significantly outperforming the Tiny variant (0.156).
Notably, this substantial improvement in predictive capacity, driven
primarily by an increase in Precision from 0.120 to 0.237, does not
incur a perceptible penalty in inference speed (1.66 FPS versus 1.51
FPS, respectively).

This parity in inference time suggests that, for the given resolution
and Grounding DINO architecture, the computational bottleneck does not
lie in the complexity of the visual backbone, but rather in other stages
of the pipeline, such as text embedding extraction, multimodal
alignment, and post-processing. Consequently, the Base variant is
definitively selected as the representative model of this family for the
testing phase.

  **Model**               **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**   **FPS**       
  --------------------- --------------- ------------ -------- -------------- ----------------- --------- -- -- --
  Grounding DINO Tiny             0.120        0.224    0.156          0.072             0.039     1.660       
  Grounding DINO Base             0.237        0.319    0.249          0.171             0.090     1.510       

  : Comparison of Grounding DINO models. {#tab:gd_modelos}

#### Per-Class Breakdown and Analysis of F1-Confidence Curve: Grounding DINO {#zero-shot-justificacion}

The per-class analysis of the optimal configuration (Table
[5.9](#tab:conf_gd){reference-type="ref" reference="tab:conf_gd"})
reveals an asymmetric yet highly informative behavior across categories.

On one hand, the *NaranjaVerde* class exhibits a stronger overall
detection capability, achieving a Recall of 0.444 and a mAP@0.50 of
0.239. These values indicate that the model is particularly effective at
localizing *NaranjaVerde* instances and delineating their bounding
boxes, thereby minimizing false negatives for this category.

On the other hand, the *Naranja* class displays a more conservative
behavior; while the Recall (0.195) and localization accuracy (mAP@0.50
of 0.102) are notably lower, this class achieves a higher Precision
(0.284) compared to the *NaranjaVerde* class (0.190). From an
operational standpoint, this means that the model detects fewer ripe
oranges, but its predictions are more reliable and exhibit a lower false
positive rate.

  **Class**          **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  ---------------- --------------- ------------ -------- -------------- -----------------
  All                        0.237        0.319    0.249          0.171             0.090
  *Naranja*                  0.284        0.195    0.231          0.102             0.051
  *NaranjaVerde*             0.190        0.444    0.266          0.239             0.130

  : Optimal configuration of Grounding DINO. {#tab:conf_gd}

Figure [5.4](#fig:f1-gd){reference-type="ref" reference="fig:f1-gd"}
presents the F1-Confidence curve obtained for the Base model, which
serves to determine the optimal operational confidence threshold for
final inference. As observed, the global performance (Macro F1) reaches
its peak (0.325) at a confidence threshold of $conf = 0.020$.

From a technical perspective, this behavior reflects a common
characteristic of open-vocabulary detection models operating under a
zero-shot paradigm. Since the model is not fine-tuned on the specific
domain of real-world agricultural environments, the cosine similarity
scores between visual features (foliage and fruit) and the text
embeddings produced by the language encoder tend to be numerically low.
As a result, although the model correctly distributes relative
probabilities among objects, its absolute confidence remains low. This
necessitates the use of a highly permissive confidence threshold
($conf = 0.020$) to preserve Recall, while relying on NMS-based spatial
filtering to suppress false positives.

<figure id="fig:f1-gd" data-latex-placement="H">
<img src="images/groundingDino/boxF1_curve.jpg" style="width:80.0%" />
<figcaption>F1-Confidence curve of the Grounding DINO
model.</figcaption>
</figure>

## OWLv2

This section presents the evaluation of OWLv2, an architecture based on
Vision Transformers (ViT) aligned with large-scale linguistic
representations. As in previous experiments, the geometric nature of
Transformers discourages modifying the input resolution; therefore,
images are processed at their native size ($\sim 960 \times 960$
pixels). For this study, only the 16-base-patch variant (ViT-B/16) was
selected, corresponding to the lightest available configuration.
Nevertheless, as shown below, its architectural design introduces
computational bottlenecks that significantly penalize inference speed,
justifying the exclusion of heavier variants.

### Prompt Ablation: OWLv2

The prompt analysis, summarized in Table
[5.10](#tab:prompts_owl){reference-type="ref"
reference="tab:prompts_owl"}, reveals a specific behavioral
characteristic: Recall remains relatively stable across all prompt
levels, ranging between 0.594 and 0.659. This suggests that OWLv2
initially functions as a class-agnostic object proposer, identifying any
region that significantly deviates from the background as a potential
object candidate. The primary performance variation is observed in
Precision. Prompt P1 (\"orange\", \"green orange\") achieves the best
performance with an F1-score of 0.106. This indicates that, due to its
patch-based tokenization (16×16), OWLv2 performs optimally with direct
morphological descriptions, while the inclusion of additional spatial
context in other prompts does not yield a proportional improvement in
visual-textual alignment for this specific architecture.

  **Prompt**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  ------------ --------------- ------------ -------- -------------- -----------------
  P1                     0.058        0.659    0.106          0.490             0.241
  P2                     0.043        0.615    0.080          0.428             0.209
  P3                     0.046        0.594    0.086          0.412             0.214
  P4                     0.056        0.654    0.102          0.481             0.242
  P5                     0.057        0.610    0.104          0.331             0.170
  P6                     0.041        0.650    0.077          0.054             0.021

  : Prompt ablation on the validation set. Model: OWLv2.
  {#tab:prompts_owl}

Figure [5.5](#fig:prompt-owl){reference-type="ref"
reference="fig:prompt-owl"} illustrates these performance variations
visually. The model demonstrates a clear sensitivity to the input
lexicon, where the concise P1 prompt achieves the empirical peak with an
F1-score of 0.106. While performance remains relatively stable across
intermediate configurations (P3 through P5), the introduction of
negative context in prompt P6 leads to a sharp degradation in the
F1-score, dropping to 0.077. This trend highlights that, unlike other
architectures, OWLv2 does not benefit from complex spatial grounding or
negative constraints, but rather relies on direct and morphologically
simple descriptors to maintain optimal visual-textual alignment.

<figure id="fig:prompt-owl" data-latex-placement="H">
<img src="images/OWLv2/owlv2-prompts.jpg" style="width:100.0%" />
<figcaption>Prompt comparison for the OWLv2 model.</figcaption>
</figure>

### Tiling Evaluation: OWLv2

Applying a tiling strategy (Table
[5.11](#tab:tiling_owl){reference-type="ref"
reference="tab:tiling_owl"}) proves detrimental to the architecture. The
global F1-score drops from 0.106 to 0.049, and inference speed decreases
sharply to 0.11 FPS.

This degradation is caused by a structural conflict between our
macro-tiling grid and the model's internal vision system. OWLv2
inherently cuts images into tiny 16$\times$`<!-- -->`{=html}16 pixel
squares (patches) to look for objects. By forcing an artificial tiling
step on top of this, we create a repetitive "patch-over-patch" effect
that traps the model inside isolated windows. Without the broader
context of the surrounding tree or foliage, these small patches lose
their connection to the rest of the scene. The model essentially loses
the big picture, causing it to mistake random shadows or round
background textures for fruit. This triggers a flood of false positives,
leading to a collapse in Precision from 0.058 to 0.025.

  **Configuration**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**   **FPS**
  ------------------- --------------- ------------ -------- -------------- ----------------- ---------
  No tiling                     0.058        0.659    0.106          0.490             0.241     0.300
  Tiling                        0.025        0.872    0.049          0.618             0.319     0.110

  : Tiling evaluation on the validation set. Prompt P1. Model: OWLv2.
  {#tab:tiling_owl}

### NMS Threshold Sweep: OWLv2

With prompt P1 fixed and tiling disabled, the NMS threshold was
optimized. As shown in Table [5.12](#tab:nms_owl){reference-type="ref"
reference="tab:nms_owl"}, there is a clear inverse relationship between
the threshold and performance, with the optimal value achieved at the
most restrictive setting (0.01), yielding an F1-score of 0.213.

This behavior arises because OWLv2 tends to generate dense clusters of
predictions around patch tokens. In highly dense and occluded
environments such as this dataset, the model produces numerous redundant
bounding boxes per object. A strict NMS threshold (0.01) is therefore
required to aggressively suppress overlapping detections.

  **NMS**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**    
  --------- --------------- ------------ -------- -------------- ----------------- -- --
  0.01                0.135        0.548    0.213          0.428             0.215    
  0.1                 0.105        0.610    0.175          0.472             0.234    
  0.2                 0.084        0.630    0.145          0.481             0.238    
  0.3                 0.072        0.642    0.127          0.486             0.240    
  0.4                 0.064        0.652    0.114          0.489             0.240    
  0.5                 0.058        0.659    0.106          0.490             0.241    
  0.6                 0.055        0.664    0.100          0.491             0.242    

  : NMS threshold sweep on the validation set. Prompt P1, tiling
  disabled. Model: OWLv2. {#tab:nms_owl}

### Optimal Configuration Analysis: OWLv2

Table [5.13](#tab:conf_owl){reference-type="ref"
reference="tab:conf_owl"} presents the per-class performance using the
optimal configuration (Prompt P1, no tiling, NMS 0.01). The model shows
balanced performance across both categories; notably, for the first
time, the *Naranja* class slightly outperforms the *NaranjaVerde* class
in terms of mAP@0.50 (0.436 versus 0.421), while also demonstrating a
superior Precision of 0.186 compared to 0.085 for *NaranjaVerde*,
suggesting a better alignment between its visual features and the
representations learned during pretraining.

  **Class**          **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  ---------------- --------------- ------------ -------- -------------- -----------------
  All                        0.135        0.548    0.213          0.428             0.215
  *Naranja*                  0.186        0.549    0.277          0.436             0.216
  *NaranjaVerde*             0.085        0.548    0.148          0.421             0.214

  : Optimal configuration of OWLv2. {#tab:conf_owl}

Finally, to translate these raw detections into a practical deployment
setting, Figure [5.6](#fig:f1-ow){reference-type="ref"
reference="fig:f1-ow"} presents the F1-Confidence curve. The model
achieves its optimal confidence threshold at 0.226, achieving a Macro F1
of 0.522. Unlike other evaluated architectures, OWLv2 requires a
stricter confidence threshold to maximize performance. This behavior
confirms its tendency to generate an excessive number of low-confidence
proposals, a pattern already suggested by the stable Recall observed in
the prompt ablation stage.

<figure id="fig:f1-ow" data-latex-placement="H">
<img src="images/OWLv2/boxF1_curve.jpg" style="width:80.0%" />
<figcaption>F1-Confidence curve of the OWLv2 model.</figcaption>
</figure>

## YOLO-World

This section evaluates YOLO-World, an open-vocabulary architecture that
presents a clear technological contrast with the Transformer-based
models analyzed in previous sections. Built upon the convolutional
YOLOv8 architecture, this model prioritizes computational efficiency and
real-time inference. To provide a comprehensive analysis, four variants
are evaluated: Small, Medium, Large, and Extra-Large. For readability,
results are consolidated into unified comparative tables, while detailed
per-version breakdowns are provided in Appendix
[12](#ap_c){reference-type="ref" reference="ap_c"}.

### Prompt Ablation: YOLO-World

The results in Table [5.14](#tab:prompts_yworlds){reference-type="ref"
reference="tab:prompts_yworlds"} reveal a clear relationship between
network size and its ability to interpret textual prompts. The lighter
variants (Small, Medium, and Large) achieve their best performance using
the simplest descriptor (P1: \"orange\", \"green orange\"), suggesting
that their vision-language alignment modules lack sufficient depth to
process more complex descriptions without introducing noise. In
contrast, the Extra-Large variant demonstrates greater abstraction
capacity, benefiting from prompt P4 (\"spherical orange\", \"spherical
green orange\") by effectively leveraging morphological information.

Quantitatively, while the Small variant underperforms for the complexity
of this domain (F1 = 0.348), the increased parameter capacity of the
Extra-Large variant significantly improves performance, reaching an
F1-score of 0.451.

  **Version**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**   **Prompt**
  ------------- --------------- ------------ -------- -------------- ----------------- ------------
  Small                   0.692        0.248    0.348          0.202             0.119           P1
  Medium                  0.666        0.292    0.392          0.250             0.155           P1
  Large                   0.629        0.309    0.394          0.268             0.171           P1
  Extra-large             0.635        0.350    0.451          0.296             0.183           P4

  : Prompt ablation on the validation set. Model: YOLO-World.
  {#tab:prompts_yworlds}

Figure [5.7](#fig:prompt-yw){reference-type="ref"
reference="fig:prompt-yw"} highlights the performance progression: a
notable improvement from Small to Medium/Large (which then stabilizes),
followed by another measurable gain in the Extra-Large variant.

<figure id="fig:prompt-yw" data-latex-placement="H">
<img src="images/yolo-world/yoloworld-prompts.jpg"
style="width:100.0%" />
<figcaption>Prompt comparison for YOLO-World models.</figcaption>
</figure>

### Tiling Evaluation: YOLO-World

The tiling evaluation (Table
[5.15](#tab:tiling_yworlds){reference-type="ref"
reference="tab:tiling_yworlds"}) demonstrates that none of the
YOLO-World variants benefit from a patch-based processing strategy.
Therefore, the models maintain their native inference speeds (ranging
from 13.06 FPS for the Small variant to 8.30 FPS for the Extra-large
variant) while achieving a peak F1-score of 0.451. This result indicates
that YOLO-World's internal feature extraction is sufficiently robust,
rendering the tiling strategy redundant and computationally inefficient
for this specific use case.

  **Version**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**   **Tiling**   **FPS**
  ------------- --------------- ------------ -------- -------------- ----------------- ------------ ---------
  Small                   0.692        0.248    0.348          0.202             0.119           No    13.060
  Medium                  0.666        0.292    0.392          0.250             0.155           No    10.950
  Large                   0.629        0.309    0.394          0.268             0.171           No    11.240
  Extra-large             0.635        0.350    0.451          0.296             0.183           No     8.300

  : Tiling evaluation on the validation set. Model: YOLO-World.
  {#tab:tiling_yworlds}

### NMS Threshold Sweep: YOLO-World

The NMS threshold analysis (Table
[5.16](#tab:nms_yworlds){reference-type="ref"
reference="tab:nms_yworlds"}) reveals consistent behavior across all
variants, with optimal performance achieved at an IoU threshold of 0.4.

This relatively permissive threshold (compared to the extremely
restrictive values (0.01) required by Grounding DINO or OWLv2) reflects
the architectural strength of YOLO-World in bounding box regression. By
inheriting the robust loss formulation of YOLOv8, the model produces
well-localized predictions without generating excessive overlapping
boxes. Operating with a less restrictive NMS allows the model to
preserve detections of adjacent or partially occluded fruits more
effectively.

Overall, the Extra-Large variant emerges as the optimal configuration,
delivering the highest detection performance (F1 = 0.451) without
sacrificing inference speed, unlike the Large variant when tiling is
applied.

  **Version**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**   **NMS**
  ------------- --------------- ------------ -------- -------------- ----------------- ---------
  Small                   0.695        0.248    0.348          0.202             0.119     0.400
  Medium                  0.675        0.291    0.393          0.250             0.155     0.400
  Large                   0.634        0.307    0.395          0.266             0.170     0.400
  Extra-large             0.640        0.349    0.451          0.297             0.183     0.400

  : NMS threshold sweep on the validation set. Model: YOLO-World.
  {#tab:nms_yworlds}

### Optimal Configuration Analysis: YOLO-World

Table [5.17](#tab:conf_yw){reference-type="ref" reference="tab:conf_yw"}
presents the per-class performance under the optimal configuration
(Extra-Large variant, prompt P4, no tiling, NMS = 0.4). A notable
observation is that the model maintains nearly identical and robust
Precision across both classes (0.631 for *Naranja* and 0.648 for
*NaranjaVerde*). However, the *Naranja* class exhibits lower Recall
(0.321 versus 0.376), indicating that the slight reduction in global
performance is due to missed detections of mature fruit rather than
unreliable predictions.

  **CLass**          **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  ---------------- --------------- ------------ -------- -------------- -----------------
  All                        0.640        0.349    0.451          0.297             0.183
  *Naranja*                  0.631        0.321    0.426          0.249             0.155
  *NaranjaVerde*             0.648        0.376    0.476          0.344             0.211

  : Optimal configuration of YOLO-World. {#tab:conf_yw}

Finally, Figure [5.8](#fig:f1-yw){reference-type="ref"
reference="fig:f1-yw"} shows the F1-Confidence curve, where the optimal
confidence threshold is found at a very low value ($conf = 0.01$),
achieving a Macro F1 of 0.453. This behavior is consistent with the
zero-shot confidence dynamics previously discussed for Grounding DINO.

<figure id="fig:f1-yw" data-latex-placement="H">
<img src="images/yolo-world/boxF1_curve.jpg" style="width:80.0%" />
<figcaption>F1-Confidence curve of the YOLO-World model.</figcaption>
</figure>

## YOLOE

This section evaluates YOLOE, the most recent real-time zero-shot
detector introduced by Ultralytics. This open-vocabulary detection and
segmentation model enables dynamic object recognition without requiring
retraining. Its core design is based on the YOLO10 architecture,
granting high-speed inference capabilities, while being strongly
inspired by the vision-language alignment mechanisms of YOLO-World.

To accommodate different hardware requirements, YOLOE is deployed across
three architectural branches: YOLOE-v8 (leveraging the maturity of the
current industry standard), YOLOE-11 (optimized for efficiency and
lightweight computation), and YOLOE-26 (the most advanced variant,
designed to fully exploit the NMS-free paradigm introduced in recent
versions). The available configurations range from Small to Large for
the first two families, while the 26 branch spans from Nano to
Extra-Large. For readability, results are presented in unified
comparative tables, with full per-version details provided in Appendix
[13](#ap_d){reference-type="ref" reference="ap_d"}.

### Prompt Ablation: YOLOE

The results in Table [5.18](#tab:prompts_yoloes){reference-type="ref"
reference="tab:prompts_yoloes"} reveal distinct performance trends
across architectural families. The v8 and v11 branches exhibit similar
behavior across prompts. Within the 26 family, the Nano variant shows
limited representational capacity (F1 = 0.225), while scaling to the
Small version yields a significantly larger improvement compared to
other families.

Notably, contrary to the common trend where larger models achieve higher
accuracy, YOLOE reaches its peak performance at the Medium scale,
particularly YOLOE-11-Medium, which achieves the highest F1-score of
0.459. Beyond this point, increasing model size (Large or Extra-Large)
leads to slight performance degradation. This suggests that, in this
zero-shot agricultural setting, overly parameterized models may overfit
dataset noise or lose generalization capacity in vision-language
alignment.

  **Version**        **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**   **Prompt**
  ---------------- --------------- ------------ -------- -------------- ----------------- ------------
  8-Small                    0.445        0.329    0.355          0.256             0.146           P4
  8-Medium                   0.610        0.330    0.428          0.260             0.148           P4
  8-Large                    0.673        0.318    0.431          0.250             0.150           P4
  11-Small                   0.565        0.276    0.370          0.219             0.127           P3
  11-Medium                  0.673        0.348    0.459          0.300             0.177           P4
  11-Large                   0.596        0.324    0.420          0.271             0.165           P3
  26-Nano                    0.605        0.148    0.225          0.094             0.055           P4
  26-Small                   0.604        0.312    0.407          0.249             0.146           P2
  26-Medium                  0.683        0.324    0.427          0.272             0.164           P2
  26-Large                   0.548        0.352    0.407          0.260             0.160           P3
  26-Extra-large             0.454        0.391    0.393          0.274             0.169           P2

  : Prompt ablation on the validation set. Models: YOLOE.
  {#tab:prompts_yoloes}

Figure [5.9](#fig:prompt-ye){reference-type="ref"
reference="fig:prompt-ye"}, highlights these trends, with the most
pronounced differences observed at the Medium scale, where YOLOE-11
clearly stands out. Except for the v8 branch, which improves steadily
with scale, the remaining families exhibit performance degradation
beyond the Medium configuration.

<figure id="fig:prompt-ye" data-latex-placement="H">
<img src="images/yoloe/yoloe-prompts.jpg" style="width:100.0%" />
<figcaption>Prompt comparison for YOLOE models.</figcaption>
</figure>

### Tiling Evaluation: YOLOE

As shown in Table [5.19](#tab:tiling_yoloes){reference-type="ref"
reference="tab:tiling_yoloes"}, tiling proves ineffective across all
evaluated variants. None of the models benefit from patch-based
processing.

This indicates that YOLOE relies heavily on global scene context for
proper semantic grounding. Tiling disrupts spatial and contextual
relationships required for accurate vision-language alignment. Thus,
full-image inference is maintained, preserving the model's high native
inference speeds (ranging from approximately 8 to 14 FPS).

  **Version**        **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**   **Tiling**   **FPS**
  ---------------- --------------- ------------ -------- -------------- ----------------- ------------ ---------
  8-Small                    0.445        0.329    0.355          0.256             0.146           No     9.530
  8-Medium                   0.610        0.330    0.428          0.260             0.148           No     9.640
  8-Large                    0.673        0.318    0.431          0.250             0.150           No     8.720
  11-Small                   0.565        0.276    0.370          0.219             0.127           No    10.450
  11-Medium                  0.673        0.348    0.459          0.300             0.177           No     9.260
  11-Large                   0.596        0.324    0.420          0.271             0.165           No     8.590
  26-Nano                    0.605        0.148    0.225          0.094             0.055           No    14.180
  26-Small                   0.604        0.312    0.407          0.249             0.146           No    13.250
  26-Medium                  0.683        0.324    0.427          0.272             0.164           No    11.680
  26-Large                   0.548        0.352    0.407          0.260             0.160           No    10.990
  26-Extra-large             0.454        0.391    0.393          0.274             0.169           No     8.330

  : Tiling evaluation on the validation set. Model: YOLOE.
  {#tab:tiling_yoloes}

### NMS Threshold Sweep: YOLOE

Unlike YOLO-World, where all variants converged to a single optimal NMS
threshold (0.4), Table [5.20](#tab:nms_yoloes){reference-type="ref"
reference="tab:nms_yoloes"} shows that YOLOE exhibits strong sensitivity
to NMS tuning.

Each branch and variant requires a different optimal threshold, ranging
from highly restrictive values (0.2 for YOLOE-26-Nano or 11-Small) to
more permissive ones (0.4 for YOLOE-26-Medium, for example). This
variability reflects differences in detection heads and prediction
distributions across the v8, v11, and v26 families. Consequently,
optimal deployment requires fine-grained, model-specific tuning of
spatial post-processing.

Overall, YOLOE-11-Medium emerges as the best-performing configuration.
With its optimal setup (prompt P4, no tiling, NMS = 0.3), it achieves
the highest F1-score (0.460), and is therefore selected as the
representative model for test evaluation.

  **Version**        **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**   **NMS**
  ---------------- --------------- ------------ -------- -------------- ----------------- ---------
  8-Small                    0.452        0.327    0.356          0.256             0.145     0.400
  8-Medium                   0.617        0.328    0.428          0.257             0.148     0.400
  8-Large                    0.688        0.316    0.433          0.248             0.150     0.300
  11-Small                   0.601        0.270    0.372          0.218             0.127     0.200
  11-Medium                  0.685        0.346    0.460          0.300             0.177     0.300
  11-Large                   0.615        0.321    0.422          0.269             0.165     0.200
  26-Nano                    0.615        0.147    0.225          0.095             0.056     0.200
  26-Small                   0.612        0.310    0.408          0.249             0.146     0.400
  26-Medium                  0.705        0.319    0.428          0.270             0.163     0.200
  26-Large                   0.557        0.348    0.409          0.261             0.160     0.300
  26-Extra-large             0.460        0.388    0.394          0.273             0.169     0.400

  : NMS threshold sweep on the validation set. Models: YOLOE.
  {#tab:nms_yoloes}

### Optimal Configuration Analysis: YOLOE

Table [5.21](#tab:conf_ye){reference-type="ref" reference="tab:conf_ye"}
presents the per-class performance under the optimal configuration
(YOLOE-11-Medium, prompt P4, no tiling, NMS = 0.3). The results indicate
a clear preference for the *NaranjaVerde* class. This category achieves
both higher Recall (0.366 vs. 0.326) and higher Precision (0.722 vs.
0.647), indicating stronger and more discriminative feature extraction.
In contrast, performance on the *Naranja* class constitutes the main
limitation of the model.

  **Class**          **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  ---------------- --------------- ------------ -------- -------------- -----------------
  All                        0.685        0.346    0.460          0.300             0.177
  *Naranja*                  0.647        0.326    0.434          0.259             0.159
  *NaranjaVerde*             0.722        0.366    0.485          0.341             0.195

  : Optimal configuration of YOLOE. {#tab:conf_ye}

Finally, Figure [5.10](#fig:f1-ye){reference-type="ref"
reference="fig:f1-ye"} shows that the model's optimal performance is
achieved at an extremely low confidence threshold ($conf = 0.01$),
achieving a Macro F1 of 0.460, consistent with the zero-shot confidence
dynamics observed in previous architectures.

<figure id="fig:f1-ye" data-latex-placement="H">
<img src="images/yoloe/boxF1_curve.jpg" style="width:80.0%" />
<figcaption>F1-Confidence curve of the YOLOE model.</figcaption>
</figure>

## SAM 3

This section evaluates SAM 3, a model that introduces a paradigm shift
compared to the previously analyzed architectures. Unlike native
detectors such as YOLO-World or Grounding DINO, SAM 3 operates as a
prompt-based segmentation system. Its bounding boxes are not obtained
through direct coordinate regression, but are instead derived from
pixel-wise masks generated for each object. This distinction may
influence its overall performance in zero-shot tasks and is therefore
examined in detail.

### Prompt Ablation: SAM 3

The prompt analysis, summarized in Table
[5.22](#tab:prompts_SAM3){reference-type="ref"
reference="tab:prompts_SAM3"}, demonstrates that SAM 3 is highly
sensitive to the specificity of the input lexicon. While the model
exhibits relatively stable performance across several prompts, the
configuration using P4 (\"spherical orange\", \"spherical green
orange\") achieves the best balance, reaching an F1-score of 0.077. This
outcome is primarily driven by the superior Precision (0.050) attained
with P4, which suggests that the model is prone to false positives
caused by the morphological resemblance between the fruit and
surrounding foliage. Therefore, employing precise morphological
descriptors serves as an effective mechanism to improve discriminative
performance, validating P4 as the most robust choice for this
architecture.

  **Prompt**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  ------------ --------------- ------------ -------- -------------- -----------------
  P1                     0.045        0.157    0.070          0.071             0.016
  P2                     0.026        0.100    0.040          0.040             0.010
  P3                     0.049        0.160    0.075          0.074             0.017
  P4                     0.050        0.164    0.077          0.073             0.015
  P5                     0.046        0.161    0.070          0.080             0.019
  P6                     0.049        0.106    0.063          0.022             0.004

  : Prompt ablation on the validation set. Model: SAM 3.
  {#tab:prompts_SAM3}

Figure [5.11](#fig:prompt-SAM3){reference-type="ref"
reference="fig:prompt-SAM3"} illustrates these differences visually.
While simple fruit-based prompts underperform compared to those
including contextual and morphological descriptions, the model achieves
its peak performance with prompt P4 (F1-score of 0.077).

<figure id="fig:prompt-SAM3" data-latex-placement="H">
<img src="images/sam3/sam3-prompts.jpg" style="width:100.0%" />
<figcaption>Prompt comparison for the SAM 3 model.</figcaption>
</figure>

### Tiling Evaluation: SAM 3

For SAM 3, tiling (Table [5.23](#tab:tiling_SAM 3){reference-type="ref"
reference="tab:tiling_SAM 3"}) significantly alters the detection
dynamics, increasing Recall from 0.164 to 0.327 at the cost of a
substantial rise in false positives, which causes Precision to drop from
0.050 to 0.011. By isolating small image patches, the mask prediction
mechanism focuses on low-resolution local details, leading to the
segmentation of illuminated leaves or branch reflections due to their
morphological similarity to citrus fruits. Furthermore, this strategy
imposes a heavy computational penalty, reducing inference speed from
4.01 FPS to 0.29 FPS.

  **Configuration**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**   **FPS**
  ------------------- --------------- ------------ -------- -------------- ----------------- ---------
  **No tiling**                 0.050        0.164    0.077          0.073             0.015     4.010
  Tiling                        0.011        0.327    0.022          0.215             0.079     0.290

  : Tiling evaluation on the validation set. Prompt P4. Model: SAM 3.
  {#tab:tiling_SAM 3}

### NMS Threshold Sweep: SAM 3

The NMS evaluation (Table [5.24](#tab:nms_SAM 3){reference-type="ref"
reference="tab:nms_SAM 3"}) shows behavior consistent with
Transformer-based architectures such as Grounding DINO. The model
achieves its peak performance (F1 = 0.099) at the most restrictive
threshold (NMS = 0.01).

This indicates that, in dense and highly occluded scenarios, SAM 3
generates multiple overlapping segmentations for the same fruit
instance. Applying an extremely strict NMS effectively removes redundant
predictions, making this configuration optimal.

  **NMS**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95** 
  --------- --------------- ------------ -------- -------------- ----------------- --
  0.01                0.085        0.119    0.099          0.067             0.014 
  0.1                 0.069        0.121    0.088          0.068             0.014 
  0.2                 0.059        0.126    0.080          0.068             0.015 
  0.3                 0.055        0.138    0.079          0.070             0.015 
  0.4                 0.053        0.153    0.078          0.072             0.015 
  0.5                 0.050        0.164    0.077          0.073             0.015 
  0.6                 0.048        0.170    0.074          0.073             0.015 

  : NMS threshold sweep on the validation set. Prompt P4, no tiling.
  Model: SAM 3. {#tab:nms_SAM 3}

### Optimal Configuration Analysis: SAM 3

Table [5.25](#tab:conf_SAM 3){reference-type="ref"
reference="tab:conf_SAM 3"} presents the per-class performance under the
final optimal configuration (prompt P4, no tiling, NMS = 0.01). A
notable observation is the perfect balance in all metrics from all
classes.

  **Class**          **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  ---------------- --------------- ------------ -------- -------------- -----------------
  All                        0.085        0.119    0.099          0.067             0.014
  *Naranja*                  0.084        0.122    0.100          0.068             0.016
  *NaranjaVerde*             0.085        0.116    0.098          0.066             0.012

  : Optimal configuration of SAM 3. {#tab:conf_SAM 3}

Figure [5.12](#fig:f1-SAM 3){reference-type="ref"
reference="fig:f1-SAM 3"} shows the F1-Confidence curve, indicating that
the optimal confidence threshold is reached at a value of 0.246,
achieving a Macro F1 of 0.142. Despite being a segmentation-based model
rather than a bounding box regressor, SAM 3 exhibits the same
attenuation in confidence scores observed in other zero-shot
architectures. This indicates that low-confidence outputs are primarily
a consequence of the underlying vision-language alignment, rather than
the localization mechanism itself.

<figure id="fig:f1-SAM 3" data-latex-placement="H">
<img src="images/sam3/boxF1_curve.jpg" style="width:80.0%" />
<figcaption>F1-Confidence curve of the SAM 3 model.</figcaption>
</figure>

## Chapter Conclusions

The comprehensive analysis of open-vocabulary object detection (OVOD)
architectures on the validation set enables several key conclusions
regarding their behavior in agricultural environments under a zero-shot
paradigm. The evaluation reveals clear architectural and conceptual
divergences between Transformer-based models (Grounding DINO, OWLv2, SAM
3) and real-time convolutional structures (YOLO-World, YOLOE)

Table
[\[tab:metricas_modelos\]](#tab:metricas_modelos){reference-type="ref"
reference="tab:metricas_modelos"} summarizes the definitive optimal
configurations identified for each architectural family through the
systematic four-stage evaluation workflow, highlighting the performance
evolution from raw zero-shot baselines to optimized operating points:

Figure [5.13](#fig:comparacion-global-val){reference-type="ref"
reference="fig:comparacion-global-val"} provides a direct visual
comparison of the overall performance metrics, highlighting a critical
divergence between raw baseline behavior and optimized operational
points (Stage 4 F1-score). At the baseline level ($conf = 0.01$), the
real-time convolutional family (YOLO-Worldx and YOLOE-11m) achieves the
highest initial balance, demonstrating strong resistance to background
noise with baseline F1-scores of 0.451 and 0.460, respectively.
Conversely, OWLv2 initially stands out for generating an exceptionally
high candidate volume that maximizes Recall (0.548) at the extreme
expense of Precision (0.135). However, when introducing the optimized
F1-score evaluation, this dynamic shifts completely: while the
convolutional models remain virtually stagnant due to their rigid
internal calibration, OWLv2 leverages its dense candidate pool to
execute a massive performance leap, climbing from a baseline F1 of 0.213
to an overall peak optimized F1-score of 0.522. SAM 3, meanwhile,
exhibits the lowest overall performance across all stages due to the
compounding errors of executing zero-shot classification over pixel-wise
segmentation masks rather than native bounding box regressions.

<figure id="fig:comparacion-global-val" data-latex-placement="H">
<img src="images/global-comp-val.jpg" style="width:100.0%" />
<figcaption>Global comparison of the metrics.</figcaption>
</figure>

This evolution underscores that evaluating open-vocabulary models solely
on default baseline configurations can be deeply misleading for
real-world applications. While baseline F1-scores ranging from 0.10 to
0.46 may appear modest compared to fully supervised benchmarks, they do
not reflect the true operational capacity of the networks. Under a
strict zero-shot regime in highly complex agricultural environments, the
analytical optimization of operational thresholds unlocks the latent
potential of Vision-Language Transformers. The fact that OWLv2 can be
tuned to reach an outstanding F1-score of 0.522 (surpassing the highly
stable convolutional baselines) demonstrates its superior flexibility.

### Prompt Sensitivity

The prompt ablation phase demonstrates that semantic cross-modality
understanding is heavily dependent on the model's underlying backbone
and tokenization strategy, refuting the notion of a universal optimal
prompt for zero-shot tasks:

- **Transformer-Based Paradigms**: These models exhibit highly
  fragmented behavioral patterns. Grounding DINO Base leverages its
  deeper Swin-Transformer backbone to exploit complex environmental
  context, achieving its peak with prompt P5 (\"on a tree\") to resolve
  occlusions within the canopy. Conversely, OWLv2 suffers from
  representation dilution when text complexity increases, optimizing its
  visual-linguistic mapping under the most concise description (P1). SAM
  3 occupies a middle ground, requiring strict morphological constraints
  (P4, \"spherical\") to properly distinguish fruit boundaries from
  surrounding foliage.

- **Convolutional YOLO Family**: These architectures display a distinct
  phenomenon of representational saturation. Lighter variants align
  effectively only with primitive descriptions (P1), whereas
  higher-capacity scaling (such as YOLO-World Extra-Large and
  YOLOE-11-Medium) unlocks the abstraction capacity required to
  integrate morphological details (P4).

Quantitatively, the YOLO family reveals extreme sensitivity between
prompts (exhibiting a maximum variance of 0.234 F1 points), whereas
Transformer architectures like Grounding DINO Base maintain high
stability across changes in the lexicon with a delta of 0.069 F1 points
between distinct prompt levels.

### Inconsistency of the Tiling Strategy

One of the most operationally relevant findings of this study is that
under the specific parameters evaluated (1280 $\times$ 1280 px patches
with a 256 px overlap), grid-based tiling did not produce a consistent
improvement in the macro F1-score. Although initially hypothesized to
mitigate small-target omissions and instance density issues, the results
suggest that this outcome may be explained by two prominent technical
factors:

- **Context Alteration in ViT Backbones**: For Transformer-style
  architectures (Grounding DINO, OWLv2, SAM 3), fragmenting the image
  into localized windows appears to disrupt the global self-attention
  mechanism and challenge the constraints of learned positional
  embeddings. Deprived of the full macro-context of the orchard tree
  structure, these models exhibit a pronounced degradation in Precision,
  potentially driven by an over-generation of low-confidence false
  positives across leaves and illumination reflections.

- **Computational Constraints in CNN Detectors**: For the YOLO-World and
  YOLOE families, translation invariance preserves regional feature
  maps, keeping Precision relatively stable. However, the introduction
  of overlapping tiles did not yield statistically significant gains in
  detection metrics within this framework, while imposing a substantial
  computational overhead that reduces inference speeds below 1 FPS,
  thereby compromising the primary real-time operational advantage of
  these networks.

Consequently, a tiling strategy using these specific configuration
values is not recommended for practical deployment scenarios in
precision agriculture.

### NMS Dynamics

The NMS threshold optimization splits the evaluated architectures into
two clearly defined operational zones, as illustrated in Figure
[5.14](#fig:f1-nms-val){reference-type="ref"
reference="fig:f1-nms-val"}:

- **Aggressive Redundancy Filtering Zone ($IoU = 0.01$)**:
  Transformer-based systems and promptable segmentors (Grounding DINO,
  OWLv2, SAM 3) naturally tend to output heavy, overlapping clusters of
  candidate boxes or masks over identical target regions. Operating
  these models under zero-shot paradigms necessitates an
  ultra-restrictive NMS threshold of 0.01 to aggressively suppress
  spatial redundancies, which successfully doubles precision without
  incurring critical drops in recall. However, it must be recognized
  that such an aggressive threshold carries an operational downside: it
  is highly likely to eliminate valid detections of distinct fruit
  instances that are physically adjacent or tightly clustered in dense
  orchard branches, mistaking them for overlapping redundant boxes.

- **Standardized Regression Zone ($IoU = 0.30 - 0.40$)**: YOLO-World and
  YOLOE directly inherit the robust bounding box loss formulations and
  decoupled heads of the YOLOv8/v10 lineages. This structural
  inheritance enables highly localized coordinate regressions, allowing
  them to operate at standard, permissive NMS thresholds. This
  configuration provides a major operational advantage in high-density
  fields, as it successfully preserves valid detections of adjacent or
  partially occluded fruits.

<figure id="fig:f1-nms-val" data-latex-placement="H">
<img src="images/f1-nms.jpg" style="width:100.0%" />
<figcaption>Global F1-score vs. NMS threshold.</figcaption>
</figure>

### Confidence Thresholds

The analytical derivation of the F1-Confidence curves reveals a
fundamental constraint shared across all open-vocabulary systems, which
is the necessity of operating at highly permissive confidence thresholds
ranging from 0.010 in YOLOE to 0.246 in SAM 3. This uniform attenuation
is a direct consequence of the zero-shot paradigm. Because the
underlying vision-language encoders compute cosine similarities on
out-of-domain agricultural features where visual characteristics of
fruit and foliage frequently overlap, the absolute embedding match
scores remain numerically low. While the models accurately distribute
relative probabilities, implying correct localization, the absolute
confidence metrics are heavily suppressed.

A cross-comparison reveals a critical behavioral split between both
architectural lineages during threshold calibration:

- **Transformer Models (OWLv2, Grounding DINO):** Function as dense
  regional proposers. At a raw baseline ($conf = 0.01$), their metrics
  are heavily polluted by low-confidence background noise. Calibrating
  their thresholds acts as an aggressive semantic filter, unlocking
  massive F1-score leaps (OWLv2 jumps from 0.213 to 0.522; Grounding
  DINO rises from 0.249 to 0.325).

- **Convolutional Family (YOLO-World, YOLOE):** Exhibit high categorical
  certainty due to specialized coordinate regression heads. Their
  predictions are crisp and definitive from the start, making an
  operational confidence filter redundant. They show negligible
  baseline-to-optimized variations, with F1 deltas under 0.003.

- **Segmentation Framework (SAM 3):** Exhibits the lowest overall
  metrics due to compounding errors from executing zero-shot
  classification over pixel-wise masks instead of native bounding boxes.
  It shows a modest F1 improvement (from 0.099 to 0.142) but requires a
  much higher optimal threshold (0.246) to eliminate background errors.

In conclusion, this systematic ablation process has successfully
identified and isolated the optimal hyperparameter sets for each model
lineage. Considering both predictive accuracy (F1-score) and
computational feasibility (FPS), the top-performing variants from each
family have been selected as final candidates for the comprehensive
evaluation in Chapter [6](#comparativa_test){reference-type="ref"
reference="comparativa_test"}, where they will be tested against the
closed-vocabulary baseline under a simulated real-world deployment
scenario.

# Global Comparison on the Test Set {#comparativa_test}

This chapter presents the definitive evaluation of the analyzed
architectures on the test set, with the primary objective of evaluating
the models' generalization limits on a completely unseen, independent
split extracted from the same curated source. To ensure methodological
rigor, all open-vocabulary models (OVOD) were evaluated under the
optimal configurations determined during the validation phase (Chapter
[5](#cap:ovod){reference-type="ref" reference="cap:ovod"}) and, in order
to maintain absolute methodological consistency, all inference runs,
metric calculations, and processing throughput measurements (FPS) were
strictly executed under the uniform testing conditions defined in
Appendix [10](#execution_environment){reference-type="ref"
reference="execution_environment"}.

## Global Performance Analysis

Table [6.1](#tab:test_global){reference-type="ref"
reference="tab:test_global"} presents the final metrics for all models
against the supervised baseline (YOLO11s). As expected, the
closed-vocabulary detector establishes a highly optimized supervised
baseline reference that remains out of reach for open-vocabulary
architectures, achieving an F1-score of 0.758, confirming that strong
performance can be attained on this dataset when domain-specific
training is available.

Regarding the OVOD models, a clear performance stratification is
observed, dividing these architectures into three groups:

- **Efficiency and precision of YOLO-based architectures (YOLO-World and
  YOLOE):** Both models demonstrate an outstanding balance between
  predictive capacity and inference speed. YOLO-World registers a test
  F1-score of 0.456, closely followed by YOLOE at 0.447. Given that the
  numerical delta between these two detectors is minimal (under 0.010
  points) and lacks a multi-run variance analysis, it is not possible to
  assert that these differences are statistically significant,
  suggesting that both models exhibit practically equivalent performance
  under the evaluated scenario. Furthermore, the operational advantage
  of these convolutional models lies not only in their baseline
  F1-scores, but in their consistently high Precision (being the only
  candidates to substantially exceed 0.60) and, critically, in their
  computational efficiency. Operating at 8.10 FPS and 8.99 FPS,
  respectively, they represent a drastically superior throughput
  compared to their Transformer-based counterparts.

- **Divergent behavior of Vision Transformers (OWLv2 and Grounding
  DINO):** This group exhibits notable asymmetry. OWLv2 achieves the
  highest F1-score among all open-vocabulary models (0.519),
  substantially outperforming Grounding DINO (0.311). However, this
  detection capability is severely penalized in terms of inference speed
  due to the density of its attention windows, yielding rates of 0.34
  FPS and 1.79 FPS, respectively.

- **The collapse of SAM 3:** The foundational segmentation model fails
  at this specific high-density detection task, recording an F1-score of
  only 0.150. This confirms that its iterative prompt-based architecture
  is ill-suited for the extreme object density demands of precision
  agriculture, exhibiting a critically low Recall.

  **Model**          **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**   **FPS**
  ---------------- --------------- ------------ -------- -------------- ----------------- ---------
  YOLO11s                    0.813        0.710    0.758          0.685             0.401     4.440
  Grounding DINO             0.387        0.286    0.311          0.150             0.083     1.790
  OWLv2                      0.565        0.485    0.519          0.391             0.201     0.340
  YOLO-World                 0.668        0.346    0.456          0.286             0.175     8.100
  YOLOE                      0.662        0.338    0.447          0.277             0.166     8.990
  SAM 3                      0.292        0.103    0.150          0.065             0.017     4.190

  : Global results of all models on the test set. {#tab:test_global}

To complement the quantitative analysis, Figure
[6.1](#fig:pr_barras){reference-type="ref" reference="fig:pr_barras"}
provides a detailed visual comparison of each architecture's performance
in terms of Precision and Recall. The supervised model establishes a
clear margin over all others, leading both metrics with a Precision of
0.813 and a Recall of 0.710. At the opposite extreme, SAM 3's severe
performance degradation is evident, stagnating at a minimal Recall of
0.103.

Among the open-vocabulary models, a pronounced dispersion in Recall is
observed: while the YOLO family shows stable but moderate values (0.346
for YOLO-World and 0.338 for YOLOE), OWLv2 stands out as the
highest-recall model among open-vocabulary architectures (0.485), in
contrast to Grounding DINO, which falls to 0.286. Conversely, the YOLO
architectures achieve a qualitative leap in Precision, being the only
models to surpass the 0.60 threshold across both classes (0.668 for
YOLO-World and 0.662 for YOLOE), outperforming OWLv2 (0.565) and
Grounding DINO (0.387).

<figure id="fig:pr_barras" data-latex-placement="H">
<img src="images/pr_barras.jpg" style="width:100.0%" />
<figcaption>Global Precision and Recall of all models on the test
set.</figcaption>
</figure>

The qualitative results presented in Figure
[6.2](#fig:deployment_qualitative){reference-type="ref"
reference="fig:deployment_qualitative"} visually corroborate the
performance stratification observed in the quantitative analysis under a
completely unseen, independent split extracted from the same curated
source. The supervised baseline (YOLO11s) tracks the ground truth with
high fidelity, maintaining tight box regressions and minimal background
noise. Among the zero-shot architectures, YOLO-Worldx and YOLOE-11m
display highly distinct, clean, and well-localized bounding boxes
concentrated strictly on visible citrus fruit, visually demonstrating
their superior Precision (exceeding 0.66) and strong suppression of
background foliage. However, their conservative proposal mechanism
causes them to miss heavily shaded or deeply embedded internal fruits,
illustrating their lower bounds in sensitivity.

In contrast, OWLv2 (ViT) exhibits a significantly denser distribution of
bounding boxes across the tree, successfully identifying multiple
heavily occluded instances to achieve its peak open-vocabulary Recall of
0.485, though at the cost of occasional hallucinations on circular
foliage clusters and specular leaf highlights. This background confusion
is accompanied by substantial semantic confusion in Grounding DINO; the
model not only floods the canopy with loose, overlapping predictions on
background leaves but also exhibits high inter-class confusion,
frequently labeling ripe fruit regions under the *NaranjaVerde*
descriptor due to proximity-based cross-modal misalignment. Finally, the
qualitative breakdown of SAM 3 highlights a unique operational
bottleneck: while the framework successfully registers the semantic
presence and features of the oranges within the canopy, it completely
fails at instance isolation under a zero-shot text prompt. Instead of
delineating individual fruits within high-density clusters, the
segmentation-derived head merges the detections, drawing a single
massive bounding box that encapsulates almost the entire tree canopy
outline and restricts its operational Recall to a minimal 0.103.

<figure id="fig:deployment_qualitative" data-latex-placement="H">
<p><img src="images/gt-yolo.jpg" style="width:100.0%"
alt="image" /><br />
<img src="images/gd-owl.jpg" style="width:100.0%" alt="image" /><br />
<img src="images/ye-yw.jpg" style="width:100.0%" alt="image" /><br />
<img src="images/sam3.jpg" style="width:50.0%" alt="image" /></p>
<figcaption>Qualitative comparison of zero-shot open-vocabulary object
detection architectures on a representative field deployment scenario
featuring dense citrus clustering and canopy occlusions.</figcaption>
</figure>

To further investigate the underlying factors behind these global
results, the following sections present a per-class performance
breakdown. This analysis will identify specific error patterns through
the examination of individual confusion matrices, revealing how each
model responds to the physical challenges of the real agricultural
environment, characterized by high fruit density and constant occlusions
from tree foliage.

## Baseline Performance Analysis: YOLO11s

To establish the supervised reference in this agricultural domain for a
hypothetical deployment scenario, the behavior of YOLO11s is analyzed
first. This model was trained natively and in a fully supervised manner
on the training images of the dataset.

Table [6.2](#tab:test_yolo11){reference-type="ref"
reference="tab:test_yolo11"} presents the per-class inference metrics,
demonstrating robust performance with a global F1-score of 0.758. The
per-class breakdown reveals a persistent asymmetry that has been
observed throughout this work: the *NaranjaVerde* class consistently
achieves better performance (F1 = 0.795) than the mature fruit class (F1
= 0.721), indicating that the model successfully extracts highly
discriminative visual features for the immature fruit despite its shared
chromatic range with the surrounding foliage.

  **Class**          **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  ---------------- --------------- ------------ -------- -------------- -----------------
  All                        0.813        0.710    0.758          0.685             0.401
  *Naranja*                  0.774        0.675    0.721          0.641             0.377
  *NaranjaVerde*             0.852        0.745    0.795          0.728             0.426

  : Per-class results on the test set. Model: YOLO11s.
  {#tab:test_yolo11}

The confusion matrix (Figure [6.3](#fig:mc-yolo11){reference-type="ref"
reference="fig:mc-yolo11"}) provides clear empirical insights regarding
the nature of the model's predictions:

- **Near-zero inter-class confusion:** The model demonstrates a strong
  ability to distinguish ripeness states. Out of thousands of evaluated
  fruit instances, only 33 *Naranja* instances are misclassified as
  *NaranjaVerde*, and 93 in the reverse direction. The model can be
  considered to have internalized the visual concept of ripeness with
  near-perfect fidelity.

- **False positives:** Thanks to its domain-specific training, the model
  effectively controls hallucinations, confusing the background with
  *Naranja* in 565 cases and with *NaranjaVerde* in 431. These are
  highly contained figures for an environment with such complex and
  noisy textures.

- **False negatives (impact of occlusion):** The primary factor limiting
  Recall to 0.71 is the volume of false negatives. The model misses
  1,081 real *Naranja* instances and 818 *NaranjaVerde* instances,
  classifying them as background. These omissions are directly
  attributable to the geometric complexity of the dataset, where dense
  branching and foliage partially or almost entirely occlude the
  silhouette of numerous fruits.

<figure id="fig:mc-yolo11" data-latex-placement="H">
<img src="images/yolo/confusion_matrix2.jpg" style="width:80.0%" />
<figcaption>Confusion matrix of YOLO11s on the test set (absolute
instance counts).</figcaption>
</figure>

In conclusion, in this agricultural scenario, the true challenge of
computer vision lies not in distinguishing one type of fruit from
another, but in separating the concept of \"occluded fruit\" from the
concept of \"background leaves and branches.\"

## Performance Analysis: Grounding DINO

The first open-vocabulary model to be evaluated illustrates the gap
between the theoretical promise of foundational models and the reality
of a real-world scenario. As shown in Table
[6.3](#tab:test_gd){reference-type="ref" reference="tab:test_gd"},
Grounding DINO suffers a generalized performance collapse across all
metrics, achieving a global F1-score of only 0.311.

The per-class breakdown confirms the ripeness bias identified in the
baseline. However, in this architecture, the gap becomes critically
pronounced: while the model retains some capacity to localize immature
fruit (Recall = 0.425), it becomes nearly blind to the mature class
(Recall = 0.147). This demonstrates that zero-shot prompt alignment is
highly sensitive to occlusion conditions, with the visual contrast of
ripe fruit being drastically penalized.

  **Class**          **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  ---------------- --------------- ------------ -------- -------------- -----------------
  All                        0.387        0.286    0.311          0.150             0.083
  *Naranja*                  0.378        0.147    0.212          0.070             0.034
  *NaranjaVerde*             0.395        0.425    0.410          0.230             0.132

  : Per-class results on the test set. Model: Grounding DINO.
  {#tab:test_gd}

The confusion matrix (Figure [6.4](#fig:mc-gd){reference-type="ref"
reference="fig:mc-gd"}) reveals three critical failure modes in this
Vision Transformer's self-attention mechanism:

- **Inter-class confusion and increased semantic confusion:** The model
  exhibits severe difficulty in discriminating between fruit classes. It
  misclassifies 889 ripe oranges as unripe. Under high object density,
  the attention mechanism becomes saturated and tends to assign
  detections under a single semantic descriptor based on spatial
  proximity.

- **High false positive rate against the background:** The bottom row of
  the matrix reveals unstable behavior with respect to the environment.
  The detector generates 2,105 erroneous detections in regions
  containing only foliage, curved leaves, or illuminated branches (686
  classified as *Naranja* and 1,419 as *NaranjaVerde*). This structural
  inability to discriminate background texture explains the model's low
  global Precision of 38.7%.

- **Fruit omission due to occlusion (false negatives):** The rightmost
  column of the matrix reflects a massive loss of information. Operating
  in a zero-shot regime, the model requires clear visual exposure of the
  object's structure; when fruit is partially hidden by foliage, the
  visual-textual grounding is disrupted, causing 2,154 *Naranja* and
  1,863 *NaranjaVerde* to be discarded as background.

<figure id="fig:mc-gd" data-latex-placement="H">
<img src="images/groundingDino/confusion_matrix.jpg"
style="width:80.0%" />
<figcaption>Confusion matrix of Grounding DINO on the test set (absolute
instance counts).</figcaption>
</figure>

In summary, the test set evaluation confirms that Grounding DINO,
despite its sophisticated vision-language architecture, lacks the
geometric robustness required to operate reliably in high-density
agricultural scenarios.

## Performance Analysis: OWLv2

The results in Table [6.4](#tab:test_owlv2){reference-type="ref"
reference="tab:test_owlv2"} reveal a notable improvement over Grounding
DINO within the Transformer-based family, with OWLv2 achieving a global
F1-score of 0.519. Although still far from the supervised model's
ceiling, it demonstrates substantially superior generalization in this
environment.

The per-class analysis again validates the dominant trend in this
agricultural scenario, where immature fruit presents fewer detection
challenges thanks to its distinctive linguistic grounding. The
*NaranjaVerde* class achieves an F1-score of 0.536 and a strong
Precision of 0.627. Conversely, performance decreases slightly for the
mature fruit class (F1 = 0.502), reflecting the latent difficulties
associated with occlusion and illumination variability.

  **Class**          **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  ---------------- --------------- ------------ -------- -------------- -----------------
  All                        0.565        0.485    0.519          0.391             0.201
  *Naranja*                  0.503        0.501    0.502          0.382             0.192
  *NaranjaVerde*             0.627        0.468    0.536          0.399             0.210

  : Per-class results on the test set. Model: OWLv2. {#tab:test_owlv2}

The confusion matrix (Figure [6.5](#fig:mc-owlv2){reference-type="ref"
reference="fig:mc-owlv2"}) highlights three key behavioral
characteristics:

- **Robust inter-class semantic separation:** Unlike the previous
  architecture, OWLv2 demonstrates highly effective visual
  discrimination of ripeness states. Out of thousands of evaluated
  instances, only 37 *Naranja* are classified as unripe, and only 33
  unripe fruits are assigned to the ripe class. This minimal overlap
  confirms excellent visual-textual alignment for intrinsic ripeness
  characteristics.

- **Vulnerability to foliage (false positives):** The model's moderate
  global Precision is explained by the high false positive rate in the
  bottom row of the matrix. The system incorrectly labels 1,735
  background regions as *Naranja* and generates 953 additional false
  positives for the unripe class. This suggests that the ViT encoder may
  remain sensitive to circular plant geometries, dense canopy textures,
  and specular leaf reflections, which represent explanations for the
  generated false positives, although targeted optical experiments would
  be required to verify these causal links.

- **Recall penalty due to occlusion (false negatives):** The
  unstructured agricultural environment severely limits the model's
  exhaustive localization capacity. When fruits are partially covered by
  foliage, the network fails to find sufficient visual evidence to
  validate the text prompt, missing 1,744 *Naranja* and 1,856
  *NaranjaVerde* instances, which are erroneously discarded as
  background.

<figure id="fig:mc-owlv2" data-latex-placement="H">
<img src="images/OWLv2/confusion_matrix.jpg" style="width:80.0%" />
<figcaption>Confusion matrix of OWLv2 on the test set (absolute instance
counts).</figcaption>
</figure>

In summary, OWLv2 establishes itself as a semantically precise detector
in terms of ripeness discrimination, but shares the core weaknesses of
other foundational Transformers: difficulty isolating foliage noise from
background and high vulnerability to physical occlusion.

## Performance Analysis: YOLO-World

The evaluation of YOLO-World reveals great results. As shown in Table
[6.5](#tab:test_yw){reference-type="ref" reference="tab:test_yw"}, this
model leads the zero-shot real-time detector family, achieving a global
F1-score of 0.456.

Consistent with the asymmetric behavior inherent to the dataset,
YOLO-World also demonstrates superior performance on the immature fruit
class (F1 = 0.494 vs. 0.417). However, the true advantage of this
architecture over the Transformer-based models lies in its inter-class
consistency: it is the only model to surpass the 0.60 Precision
threshold homogeneously across both categories.

  **Class**          **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  ---------------- --------------- ------------ -------- -------------- -----------------
  All                        0.668        0.346    0.456          0.286             0.175
  *Naranja*                  0.634        0.311    0.417          0.226             0.141
  *NaranjaVerde*             0.703        0.381    0.494          0.346             0.209

  : Per-class results on the test set. Model: YOLO-Worldx.
  {#tab:test_yw}

The confusion matrix (Figure [6.6](#fig:mc-ywx){reference-type="ref"
reference="fig:mc-ywx"}) clearly illustrates the advantages of this
approach and the key differentiators from OWLv2 and Grounding DINO:

- **Precise discrimination of ripeness states:** The model grasps
  ripeness semantics with a level of accuracy that closely mirrors the
  supervised baseline. Of all evaluated instances, cross-class confusion
  is purely residual: only 32 *Naranja* are predicted as unripe, and the
  reverse error is limited to 107 cases, corroborating the robustness of
  its bimodal vision-language alignment path.

- **Effective suppression of background false positives:** The key to
  its high Precision lies in the bottom row of the matrix. Unlike the
  large-scale erroneous detections produced by Transformer-based models,
  YOLO-World successfully contains environmental noise, reducing
  foliage-related errors to 535 false positives for ripe fruit and 541
  for unripe. The model effectively delineates the spherical geometry of
  fruit against the complex tree textures.

- **Operational Recall ceiling under occlusion:** Despite its excellent
  discriminative capacity, the background prediction column reveals the
  inherent limitations of operating without supervised fine-tuning. The
  geometric density of the orchard causes the model to miss a
  significant volume of instances, overlooking 2,427 *Naranja* and 2,092
  *NaranjaVerde* physically hidden behind foliage.

<figure id="fig:mc-ywx" data-latex-placement="H">
<img src="images/yolo-world/confusion_matrix.jpg" style="width:80.0%" />
<figcaption>Confusion matrix of YOLO-World on the test set (absolute
instance counts).</figcaption>
</figure>

In conclusion, YOLO-World demonstrates that a spatially optimized
detection architecture can dramatically mitigate the false positive
problem in a zero-shot setting. The model has a precise understanding of
what an orange looks like and rarely generates hallucinations against
the background, although the dense agricultural occlusions continue to
prevent it from reaching the most concealed fruits within the canopy.

## Performance Analysis: YOLOE

The evaluation of YOLOE (in its optimal 11-Medium variant) confirms the
strong positioning of YOLO-based architectures in this deployment
scenario. With a global F1-score of 0.447, YOLOE achieves virtually
equivalent performance to YOLO-World (0.456), establishing itself as an
equally robust alternative with an outstanding global Precision of
0.662.

The per-class breakdown reaffirms the systematic advantage in detecting
immature fruit, where the *NaranjaVerde* class surpasses 71% Precision
(0.713). This behavior, consistent across all evaluated models, places
the mature fruit class at a comparatively lower performance level (F1 =
0.408), confirming that the chromatic and spatial complexity of ripe
fruit constitutes a challenge transversal to all evaluated encoders.

  **Class**          **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  ---------------- --------------- ------------ -------- -------------- -----------------
  All                        0.662        0.338    0.447          0.277             0.166
  *Naranja*                  0.612        0.307    0.408          0.220             0.135
  *NaranjaVerde*             0.713        0.369    0.486          0.335             0.196

  : Per-class results on the test set. Model: YOLOE-11m.
  {#tab:test_ye11m}

The confusion matrix (Figure [6.7](#fig:mc-ye){reference-type="ref"
reference="fig:mc-ye"}) shows a nearly identical pattern to YOLO-World,
confirming the shared spatial advantages and operational limitations
characteristic of this model family:

- **Full semantic alignment between categories:** The overlap between
  ripeness states is practically non-existent. The model misclassifies
  only 49 *Naranja* as unripe, and assigns 57 unripe fruits to the ripe
  class, confirming that the transfer of textual descriptions to the
  visual feature space is performed with high fidelity.

- **Effective filtering of structural background noise:** By relying on
  a convolutional architecture, the model proves far less prone to
  generating false detections on empty textures than Vision
  Transformers. False positive counts are well-contained, with 725
  errors in the ripe class and 570 in the unripe class, consolidating
  strong Precision in the test environment.

- **Fruit loss due to canopy density (false negatives):** The omission
  pattern due to the physical complexity of the orange tree recurs
  consistently. A total of 2,425 ripe fruits and 2,186 unripe fruits
  fail to exceed the detector's spatial confidence threshold, being
  discarded as background due to severe foreground occlusions.

<figure id="fig:mc-ye" data-latex-placement="H">
<img src="images/yoloe/confusion_matrix.jpg" style="width:80.0%" />
<figcaption>Confusion matrix of YOLOE on the test set (absolute instance
counts).</figcaption>
</figure>

In conclusion, YOLOE establishes itself as a prominent candidate in this
comparison, largely due to its ability to maintain high prediction
accuracy, effectively discriminate background noise, and operate at
competitive inference speeds under the tested workstation hardware (8.99
FPS). While this processing rate represents a promising indicator of
efficiency, it should not be categorized as definitive proof of
real-time edge computing viability, as the performance was benchmarked
on a high-end desktop GPU (RTX 5070) rather than a resource-constrained
embedded edge device

## Performance Analysis: SAM 3

The final model evaluated, SAM 3, introduces a radically different
paradigm based on interactive segmentation (Promptable Concept
Segmentation). The global results in Table
[6.7](#tab:test_SAM 3){reference-type="ref" reference="tab:test_SAM 3"}
yield an F1-score of 0.150, confirming what was already suggested during
validation: deploying this foundational model for a purely text-driven
zero-shot mass counting task exhibits severe operational limitations in
real-world scenarios.

  **Class**          **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  ---------------- --------------- ------------ -------- -------------- -----------------
  All                        0.292        0.103    0.150          0.065             0.017
  *Naranja*                  0.209        0.103    0.138          0.056             0.015
  *NaranjaVerde*             0.375        0.104    0.163          0.074             0.019

  : Per-class results on the test set. Model: SAM 3. {#tab:test_SAM 3}

The confusion matrix (Figure [6.8](#fig:mc-SAM 3){reference-type="ref"
reference="fig:mc-SAM 3"}) exposes the limitations of this promptable
architecture when deployed strictly under a text-driven zero-shot
configuration within high-density citrus datasets, where the absence of
precise spatial point or box prompts impairs its instance isolation
logic:

- **High inter-class classification consistency:** As a surprising
  counterpoint to its poor spatial performance, SAM 3 demonstrates
  near-perfect taxonomic precision in the few instances it successfully
  segments. The model incorrectly assigns only 3 *Naranja* to the
  *NaranjaVerde* class and 13 unripe fruits to the ripe class. This
  behavior confirms that the alignment between textual prompts and
  visual representations of its Presence Token is semantically highly
  accurate and does not suffer from chromatic ambiguity. These results
  suggest that omission associated with object density may play a larger
  role than chromatic confusion.

- **Uncontrolled background segmentation (false positives):** The bottom
  row of the matrix confirms the model's difficulty operating as an
  autonomous detector without bounding box prompts or visual support
  points. Relying exclusively on a text prompt in a zero-shot setting,
  the system generates 1,377 false positives in the ripe fruit class and
  611 in the unripe class, incorrectly treating any pronounced curvature
  or shadow in the foliage as a valid object.

- **Critical loss of real instances (false negatives):** The rightmost
  column reveals severe blindness to real fruit, constituting the
  model's primary bottleneck. The system fails to isolate individual
  masks when oranges are clustered in dense groups or semi-covered by
  branches, causing an absolute collapse in sensitivity: 3,199 *Naranja*
  and 3,170 *NaranjaVerde* are discarded as background, restricting
  global Recall to a critically low 0.103.

<figure id="fig:mc-SAM 3" data-latex-placement="H">
<img src="images/sam3/confusion_matrix.jpg" style="width:80.0%" />
<figcaption>Confusion matrix of SAM 3 on the test set (absolute instance
counts).</figcaption>
</figure>

In conclusion, the test set evaluation establishes that SAM 3, while a
state-of-the-art segmentation tool in controlled or interactive
scenarios, fails as an autonomous open-vocabulary detector in precision
agriculture. Its generative tendency to produce masks over any spherical
or shaded background texture renders it excessively vulnerable to the
noise characteristic of open-field imagery.

## Final Chapter Conclusions

The comprehensive evaluation on the test set has validated the behavior
of open-vocabulary object detection architectures under a simulated
real-world deployment scenario. The contrast with the supervised
baseline (YOLO11s), which serves as the supervised baseline with an
F1-score of 0.758, yields fundamental conclusions about the current
state of the zero-shot paradigm in precision agriculture:

- **Semantic alignment success (with exceptions):** One of the most
  significant achievements demonstrated by most OVOD models is their
  strong visual-linguistic understanding of ripeness discrimination. The
  confusion matrices of OWLv2, YOLO-World, YOLOE, and SAM 3 confirm that
  direct cross-class confusion is purely residual. Models based on
  direct grounding or bimodal alignment paths faithfully understand the
  concept of ripe versus unripe fruit. Grounding DINO, however, is a
  notable exception, exhibiting severe increased semantic confusion by
  misclassifying 889 *Naranja* as unripe due to the spatial density of
  the canopy.

- **The true bottleneck: occlusion and background:** The substantial
  performance gap between the supervised model and zero-shot approaches
  does not stem from fruit misclassification, but from the inability to
  discriminate the surrounding environment. Foundational Transformer
  architectures (Grounding DINO, OWLv2, and SAM 3) exhibited a
  pronounced susceptibility to false positives on this evaluation split,
  which limited their global Precision. Environmental challenges such as
  specular leaf reflections, severe canopy occlusions, and dense fruit
  clustering emerge as potential factors behind this behavior; however,
  these interpretations require further validation, as targeted
  experiments to definitively isolate and confirm these causal
  relationships were not conducted. Additionally, the geometric density
  of the orchard generates severe physical occlusions that cause
  critical Recall drops across all open-vocabulary candidates, as
  thousands of real instances are relegated to the background.

## Model Justification for Class Extension

Following the individual behavioral analysis of all architectures on the
test set, this section determines which models meet the conceptual and
operational requirements to lead the taxonomic extension phase. Since
the central objective of this work is to characterize the semantic
flexibility of models under a zero-shot paradigm, the selection
criterion extends beyond pure engineering or real-time speed
considerations to encompass the richness of each model's detection
behavior.

This balance is assessed visually in the scatter plot of Figure
[6.9](#fig:sc){reference-type="ref" reference="fig:sc"}, which
cross-references inference speed (FPS) against detection quality
(F1-score). To provide a clear descriptive framework rather than a
definitive or absolute selection rule, the statistical benchmark
averages are utilized strictly as exploratory reference points. The
vertical speed boundary is positioned at 4.64 FPS, while the horizontal
performance threshold is set at F1 = 0.440. It is essential to emphasize
that these dividing lines do not represent rigid or universal criteria
for operational viability; instead, they function as context-specific
baseline references designed to visually structure the relative
positioning of the evaluated cohort.

The distribution of candidates across the resulting quadrants in Figure
[6.9](#fig:sc){reference-type="ref" reference="fig:sc"} provides a
highly descriptive qualitative mapping that guides the selection of
three distinct model profiles for the extension phase:

- **Selection of the YOLO family (High Speed / High Performance):** Both
  YOLO-World Extra-Large (F1 = 0.456; 8.10 FPS) and YOLOE-11-Medium (F1
  = 0.447; 8.99 FPS) are firmly positioned in the upper-right quadrant,
  exceeding both averages. Their inclusion is mandatory on operational
  grounds: both demonstrated rigorous control over background false
  positives and excellent spatial localization. Evaluating their
  alignment modules against novel textual descriptors will provide
  insight into how a real-time-optimized detector responds to vocabulary
  expansion.

- **Inclusion of OWLv2 (Low Speed / High Performance):** Positioned in
  the upper-left quadrant, this pure Vision Transformer operates at a
  speed that is impractical for field robotics (0.34 FPS), yet achieves
  the highest absolute F1-score among open-vocabulary models (0.519) and
  leads in Recall (0.485). Since the core of this work is the study of
  visual-linguistic behavior rather than commercial deployment, its
  inclusion is essential. Its patch-based tokenization offers a
  theoretically rich contrast to the convolutional nature of YOLO,
  enabling an assessment of whether ViTs retain greater semantic
  resilience when confronted with entirely novel concepts.

- **Exclusion of Grounding DINO and SAM 3 (Low Speed / Low
  Performance):** Both models fall in the lower-left quadrant, failing
  to meet the minimum predictive robustness threshold. Grounding DINO
  (F1 = 0.311; 1.79 FPS) is hampered by severe increased semantic
  confusion generating inter-class confusion, while SAM 3 records the
  lowest performance in the benchmark (F1 = 0.150; 4.19 FPS), with a
  Recall that collapses to 0.103 due to its inability to isolate objects
  within dense clusters. Their inclusion would only introduce noise into
  the extension experiments.

<figure id="fig:sc" data-latex-placement="H">
<img src="images/f1-fps.jpg" style="width:85.0%" />
<figcaption>Global comparison of evaluated models based on inference
speed (FPS) and predictive performance (F1-score). Dashed lines indicate
the benchmark statistical averages (4.64 FPS and F1 =
0.440).</figcaption>
</figure>

In conclusion, the trio comprising **YOLO-Worldx, YOLOE-11m, and OWLv2**
will form the experimental core of the next chapter. This bimodal design
poses a high-value academic question: on one hand, it evaluates
CNN-based architectures as the efficient, real-time-ready pathway; on
the other, it retains OWLv2 (ViT) as the leading representative of
visual embedding transfer capacity. This positions the research in an
optimal methodological stance to probe the limits of zero-shot computer
vision without resorting to any form of supervised retraining.

# Generalization to Novel Classes {#ch:generalization}

This chapter presents an exploratory generalization study regarding the
zero-shot taxonomic scalability of open-vocabulary architectures by
introducing a citrus variety unseen in the task-specific orange dataset:
ripe and unripe lemons.

Rather than providing a definitive demonstration of cross-crop
performance, the primary goal of this analysis is to conduct an
exploratory assessment of whether open-vocabulary models can generalize
to new crops without retraining, and to evaluate if a unified
multi-class model is viable or if independent crop-specific deployments
are required. Crucially, because the evaluated architectures (OWLv2,
YOLO-Worldx, and YOLOE-11m) were preselected based on their superior
results during the prior orange dataset benchmarks, this testing
workflow introduces a certain selection bias that must be considered, as
it assumes that performance optimization on one crop variety inherently
transfers to another.

In strict alignment with the experimental design of all preceding
chapters, inference and evaluation procedures on this expanded dataset
were carried out using the unvaried infrastructure detailed in Appendix
[10](#execution_environment){reference-type="ref"
reference="execution_environment"}.

## Dataset Expansion and Morphological Challenges

As established in the literature review in Section
[2.4.3](#ausencia_datasets){reference-type="ref"
reference="ausencia_datasets"}, there is a severe shortage of public,
realistic datasets for open-field citrus detection. To evaluate
taxonomic extension, a new testing evaluation subset was compiled
consisting of 50 high-resolution images of lemon trees.

Due to the lack of pre-existing domain-specific repositories, this
custom evaluation collection was systematically aggregated from three
distinct visual channels: 27 images were gathered from Flickr, 13 images
were sourced from the Google Open Images v7 repository, and 10 images
were supplemented via personal field photographs. Regarding licensing
and attribution, the images drawn from Flickr and Open Images were
curated under their respective open-access and Creative Commons research
licenses, whereas the personal photographs are own-authored and remain
entirely free of external copyright restrictions.

To preserve absolute methodological and geometric consistency across
this thesis, the labeling process strictly adhered to the exact same
annotation criteria defined for the orange dataset in Chapter
[3](#dataset){reference-type="ref" reference="dataset"}. All annotations
were manually drawn using the identical interactive curation and
refinement tool detailed in Appendix
[11](#appendix:refinement_tool){reference-type="ref"
reference="appendix:refinement_tool"}. Bounding boxes were precisely
fitted to the morphological boundaries of the fruit, spanning the full
estimated perimeter under partial foliage occlusion, while filtering out
any background or fallen instances to ensure a contextually coherent
count. This dataset refinement process yielded a total of 3,333 fruit
instances, showcasing a localized distribution of 2,230 instances of
mature lemons (*Limon*) and 1,103 instances of unripe green lemons
(*LimonVerde*).

Furthermore, it is critical to state that the lemon images originate
from entirely different digital sources than the original orange
dataset. This acquisition divergence introduces a notable domain shift
(characterized by variations in sensor resolutions, lens focal lengths,
ambient color grading, and distinct cultural practices of the trees),
which represents an additional challenge for zero-shot text alignment
that may penalize the final metrics independently of fruit morphology.

This custom dataset introduces two fundamental engineering challenges:

- **Structural Imbalance**: The lemon subset contains roughly half the
  instances of the original orange dataset (3,569 *Naranja* and 3,552
  *NaranjaVerde* instances), mirroring real-world field data collection
  constraints.

- **Geometric and Chromatic Overlap**: Lemons introduce an
  elliptical/oval morphology that differs from the spherical nature of
  oranges. Furthermore, unripe green lemons display an extreme chromatic
  camouflage with the background foliage, creating a severe test for
  zero-shot text-to-visual embedding alignment.

## Global Evaluation

For this exploratory evaluation, the operational confidence and NMS
thresholds previously optimized on the orange validation split (reported
in Chapter [5](#cap:ovod){reference-type="ref" reference="cap:ovod"})
were directly transferred without any fine-tuning or re-adjustment on
the lemon images. This choice ensures a strict and independent
separation between the parameter selection domain and the novel testing
split, simulating a realistic zero-shot field deployment where no
validation samples of the new crop are available.

To thoroughly investigate deployment strategies, two distinct
experimental paths were executed:

- **Unified Evaluation**: A single model parsing four classes
  simultaneously (*Naranja*, *NaranjaVerde*, *Limon*, and *LimonVerde*).
  Global results are shown in Table
  [7.1](#tab:test_limones_naranjas_global){reference-type="ref"
  reference="tab:test_limones_naranjas_global"}.

- **Isolated Evaluation**: Evaluating the models exclusively on the
  lemon crop to assess performance when protected from cross-class
  semantic interference. Global results are shown in Table
  [7.2](#tab:test_limones_global){reference-type="ref"
  reference="tab:test_limones_global"}.

  **Model**       **Precision**   **Recall**   **F1-score**   **mAP@0.50**   **mAP@0.50:95**   **FPS**
  ------------- --------------- ------------ -------------- -------------- ----------------- ---------
  OWLv2                   0.441        0.369          0.396          0.256             0.132     0.210
  YOLO-Worldx             0.432        0.192          0.227          0.104             0.066     8.800
  YOLOE-11m               0.390        0.177          0.222          0.091             0.057     9.130

  : Global performance metrics for the unified multi-class inference
  dataset (oranges and lemons combined).
  {#tab:test_limones_naranjas_global}

  **Model**       **Precision**   **Recall**   **F1-score**   **mAP@0.50**   **mAP@0.50:95**   **FPS**
  ------------- --------------- ------------ -------------- -------------- ----------------- ---------
  OWLv2                   0.671        0.406          0.500          0.352             0.181     2.160
  YOLO-Worldx             0.569        0.245          0.268          0.126             0.081    10.240
  YOLOE-11m               0.599        0.302          0.387          0.224             0.142    11.860

  : Global performance metrics for the isolated lemon crop inference
  dataset. {#tab:test_limones_global}

Comparing Table
[7.1](#tab:test_limones_naranjas_global){reference-type="ref"
reference="tab:test_limones_naranjas_global"} and Table
[7.2](#tab:test_limones_global){reference-type="ref"
reference="tab:test_limones_global"} reveals a clear trend: expanding
the text-token space from two to four classes degrades all metrics
across every architecture. This drop in performance happens because the
different text labels compete with each other, confusing the model.

As illustrated in Figure [7.1](#fig:ch7-comp){reference-type="ref"
reference="fig:ch7-comp"}, OWLv2 maintains the highest raw metrics
across all evaluation models, which may be explained by its extensive
web-scale Vision Transformer pre-training. Conversely, the convolutional
families (YOLO-World and YOLOE) exhibit a higher sensitivity under the
unified evaluation space, experiencing noticeable Recall drops. This
behavior suggests that lightweight text-guided projection heads face
optimization constraints when processing complex, multi-class
agricultural features simultaneously. However, a key methodological
limitation must be acknowledged when comparing these deployment
strategies: transitioning from the unified framework to the isolated
crop scenario modifies not only the text prompts but also alters the
evaluation image subsets and the total number of active classes.
Therefore, the observed performance differential cannot be attributed
exclusively to semantic token competition among prompts, as it is
inherently compounded by the reduced categorical complexity and the
specific variance of the respective datasets.

Interestingly, the figure also uncovers a clear asymmetry during
isolated testing: the YOLO family recovers significantly better on the
orange dataset than on the lemon dataset. This variation may be
explained either by the data quality of the orange collection being
superior or by the fact that the hyperparameter tuning of the optimal
configurations was more heavily biased toward the specific
characteristics of the initial orange dataset in the case of the YOLO
models. In any case, since the OWLv2 model yields balanced results
across both isolated evaluations, the results suggest that the
convolutional YOLO family encounters greater constraints when adapting
zero-shot to the novel morphological features of the lemon dataset.

<figure id="fig:ch7-comp" data-latex-placement="H">
<img src="images/ch7-comp.jpg" style="width:80.0%" />
<figcaption>Comparison of F1-score across unified and crop-isolated
evaluation scenarios</figcaption>
</figure>

To compare how the selected open-vocabulary models adapt to both testing
strategies, visual examples are presented in
Figure [7.2](#fig:owl_comp){reference-type="ref"
reference="fig:owl_comp"} (OWLv2),
Figure [7.3](#fig:yw_comp){reference-type="ref" reference="fig:yw_comp"}
(YOLO-Worldx), and Figure [7.4](#fig:ye_comp){reference-type="ref"
reference="fig:ye_comp"} (YOLOE-11m). Looking at the isolated crop
results on the left side of each figure, the models show a solid
zero-shot performance because they are shielded from confusion between
different categories. Removing the orange labels prevents the model's
internal alignment layers from getting mixed up, allowing the
classification system to focus entirely on the lemon categories. As a
result, the output is dominated by accurate Blue (*Limon*) and Purple
(*LimonVerde*) bounding boxes that fit the actual fruits tightly.

Conversely, performance drops significantly and clear errors appear when
switching to the unified multi-class setup on the right side of the
figures. Because the text labels compete with each other and the green
fruits share very similar colors, the models struggle to tell them
apart, often applying orange labels to the new lemon instances. This
cross-class confusion is clearly visible when incorrect Red (*Naranja*)
and Green (*NaranjaVerde*) boxes appear around actual oval-shaped
lemons. Specifically, the Vision Transformer architecture of OWLv2
(Figure [7.2](#fig:owl_comp){reference-type="ref"
reference="fig:owl_comp"}) tends to mistake more background leaves for
fruit under these mixed conditions, while the convolutional engines of
YOLO-Worldx (Figure [7.3](#fig:yw_comp){reference-type="ref"
reference="fig:yw_comp"}) and YOLOE-11m
(Figure [7.4](#fig:ye_comp){reference-type="ref"
reference="fig:ye_comp"}) prove highly sensitive to this text clutter.
This behavior confirms that separating vocabularies by crop type is
essential to guarantee reliable zero-shot performance in multi-crop
agricultural environments.

<figure id="fig:owl_comp" data-latex-placement="H">

<figcaption>Qualitative comparison for OWLv2: crop-isolated (left) vs.
unified multi-class (right). Bounding boxes: Red (<em>Naranja</em>),
Green (<em>NaranjaVerde</em>), Blue (<em>Limon</em>), and Purple
(<em>LimonVerde</em>).</figcaption>
</figure>

<figure id="fig:yw_comp" data-latex-placement="H">

<figcaption>Qualitative comparison for YOLO-Worldx: crop-isolated (left)
vs. unified multi-class (right).</figcaption>
</figure>

<figure id="fig:ye_comp" data-latex-placement="H">

<figcaption>Qualitative comparison for YOLOE-11m: crop-isolated (left)
vs. unified multi-class (right).</figcaption>
</figure>

## Individual Model Performance and Error Trajectories

### OWLv2 Architectural Analysis

OWLv2 leverages a patch-based Vision Transformer backbone ($ViT-B/16$)
aligned with large-scale linguistic representations. This design allows
it to break images down into localized regional phrases, preserving high
semantic flexibility when mapping entirely new target concepts.

  **Class**          **Precision**   **Recall**   **F1-score**   **mAP@0.50**   **mAP@0.50:95**
  ---------------- --------------- ------------ -------------- -------------- -----------------
  All                        0.441        0.369          0.396          0.256             0.132
  *Naranja*                  0.483        0.493          0.488          0.374             0.189
  *NaranjaVerde*             0.512        0.285          0.366          0.244             0.131
  *Limon*                    0.533        0.453          0.490          0.325             0.165
  *LimonVerde*               0.235        0.244          0.239          0.082             0.043

  : Unified per-class performance breakdown for the OWLv2 architecture.
  {#tab:test_owl_unified}

The unified confusion matrix (Figure
[7.5](#fig:mc-ln-owl){reference-type="ref" reference="fig:mc-ln-owl"})
highlights four critical operational trends and failure modes:

- **True Positives**: The model shows solid zero-shot capability for
  mature fruits (1,759 *Naranja* and 1,009 *Limon*), but sensitivity
  collapses for *LimonVerde* (only 269 correct) due to its poor contrast
  against the canopy.

- **Cross-Class Bleeding**: Shape descriptions successfully separate
  mature fruits (under 80 confused instances), but color overrides
  boundaries between green classes, misclassifying 559 *NaranjaVerde*
  fruits as *LimonVerde*.

- **Background Omissions**: Canopy density remains the primary recall
  bottleneck, causing physical occlusions that miss 1,738 *Naranja*,
  1,788 *NaranjaVerde*, 1,105 *Limon*, and 659 *LimonVerde*.

- **Background Hallucinations**: Specular sun reflections and leaf
  clusters repeatedly fool the dense region proposal system, generating
  1,782 false positives for *Naranja* and 841 for *NaranjaVerde* on
  empty foliage.

<figure id="fig:mc-ln-owl" data-latex-placement="H">
<img src="images/limonesynaranjas/confusion_matrix3.jpg"
style="width:80.0%" />
<figcaption>Confusion matrix for the unified dataset. Model: OWLv2.
(Absolute instance counts).</figcaption>
</figure>

Table [7.4](#tab:test_limones_naranjas_owl){reference-type="ref"
reference="tab:test_limones_naranjas_owl"} presents the next results:
isolating the lemon vocabulary eliminates token competition, allowing
the global F1-score to rise to 0.500. The model achieves an F1-score of
0.552 for *Limon* and 0.448 for *LimonVerde*. This confirms that when
protected from cross-class dilution, the visual embedding transfer for
the *Limon* concept operates with high zero-shot accuracy.

  **Class**        **Precision**   **Recall**   **F1-score**   **mAP@0.50**   **mAP@0.50:95**
  -------------- --------------- ------------ -------------- -------------- -----------------
  All                      0.671        0.406          0.500          0.352             0.181
  *Limon*                  0.646        0.481          0.552          0.413             0.206
  *LimonVerde*             0.695        0.331          0.448          0.290             0.155

  : Isolated lemon per-class performance breakdown for the OWLv2
  architecture. {#tab:test_limones_naranjas_owl}

The isolated confusion matrix (Figure
[7.6](#fig:mc-l-owl2){reference-type="ref" reference="fig:mc-l-owl2"})
shows that the model tracks the targets accurately, correctly segmenting
1,073 ripe lemons and 365 unripe green lemons. However, background
clutter still leads to significant over-segmentation, with 1,130 ripe
lemons and 669 green lemons missed and relegated to the background. This
indicates that while isolation improves precision, foliage interference
remains a persistent challenge for ViT backbones.

<figure id="fig:mc-l-owl2" data-latex-placement="H">
<img src="images/limones/confusion_matrix3.jpg" style="width:80.0%" />
<figcaption>Confusion matrix for the isolated lemon dataset. Model:
OWLv2. (Absolute instance counts).</figcaption>
</figure>

### YOLO-Worldx Architectural Analysis

YOLO-Worldx utilizes a reparameterizable vision-language path based on a
convolutional engine, prioritizing spatial efficiency and high-speed
processing.

  **Class**          **Precision**   **Recall**   **F1-score**   **mAP@0.50**   **mAP@0.50:95**
  ---------------- --------------- ------------ -------------- -------------- -----------------
  All                        0.432        0.192          0.227          0.104             0.066
  *Naranja*                  0.574        0.291          0.386          0.190             0.122
  *NaranjaVerde*             0.493        0.201          0.286          0.156             0.098
  *Limon*                    0.570        0.060          0.109          0.046             0.029
  *LimonVerde*               0.090        0.215          0.127          0.025             0.015

  : Unified per-class performance breakdown for the YOLO-Worldx
  architecture. {#tab:test_yw_unified}

The unified confusion matrix (Figure
[7.7](#fig:mc-ln-yw){reference-type="ref" reference="fig:mc-ln-yw"})
reveals critical zero-shot constraints and a severe recall imbalance
across the expanded vocabulary:

- **True Positives**: Coordinate regressions are highly stable for
  oranges (1,038 *Naranja* and 714 *NaranjaVerde*), but localization
  sensitivity collapses for *Limon* (only 134 correct) when forced into
  a shared label space.

- **Cross-Class Bleeding**: Chromatic overlap severely impairs model
  discrimination, causing major bleeding between green fruits (781
  *NaranjaVerde* instances misclassified as *LimonVerde*) and notable
  shape confusion between mature classes (245 *Limon* instances
  predicted as *Naranja*).

- **Background Omissions**: Missing hidden fruit within the canopy
  remains the primary operational bottleneck, as strict convolutional
  matching rules overlook a massive volume of targets: 2,434 *Naranja*,
  2,021 *NaranjaVerde*, 1,364 *Limon*, and 661 *LimonVerde*.

- **Background Hallucinations**: While environmental noise is
  excellently contained for mature fruits, false positives spike
  drastically under the *LimonVerde* prompt (1,138 empty foliage regions
  falsely detected), showing that canopy textures heavily mimic the
  unripe lemon text embedding.

<figure id="fig:mc-ln-yw" data-latex-placement="H">
<img src="images/limonesynaranjas/confusion_matrix.jpg"
style="width:80.0%" />
<figcaption>Confusion matrix for the unified dataset. Model:
YOLO-Worldx. (Absolute instance counts).</figcaption>
</figure>

When evaluating the lemon crop independently, performance improves
significantly, raising global precision to 0.569. Most notably, ripe
lemon precision reaches an excellent 0.841. This demonstrates that
removing the orange prompts un-dilutes the vision-language projection
maps, allowing the convolutional backbone to detect targets with
exceptional geometric accuracy.

  **Class**        **Precision**   **Recall**   **F1-score**   **mAP@0.50**   **mAP@0.50:95**
  -------------- --------------- ------------ -------------- -------------- -----------------
  All                      0.569        0.245          0.268          0.126             0.081
  *Limon*                  0.841        0.117          0.205          0.108             0.071
  *LimonVerde*             0.297        0.373          0.331          0.144             0.090

  : Isolated lemon per-class performance breakdown for the YOLO-Worldx
  architecture. {#tab:test_yw_isolated}

The isolated confusion matrix (Figure
[7.8](#fig:mc-limnaryw2){reference-type="ref"
reference="fig:mc-limnaryw2"}) confirms that false positives are tightly
controlled compared to OWLv2. The model generates only 41 background
false positives for ripe lemons and 400 for green lemons. However, its
strict matching criteria still lead to high omission rates, with 1,398
lemons lost to the background. This underscores that while isolation
ensures clean, reliable detections, the architecture remains visually
conservative under zero-shot conditions.

<figure id="fig:mc-limnaryw2" data-latex-placement="H">
<img src="images/limones/confusion_matrix.jpg" style="width:80.0%" />
<figcaption>Confusion matrix for the isolated lemon dataset. Model:
YOLO-Worldx. (Absolute instance counts).</figcaption>
</figure>

### YOLOE Architectural Analysis

YOLOE-11m represents the efficiency frontier in this benchmark,
utilizing an advanced reparameterized text encoder designed to bypass
runtime NMS over-calculation.

  **Class**          **Precision**   **Recall**   **F1-score**   **mAP@0.50**   **mAP@0.50:95**
  ---------------- --------------- ------------ -------------- -------------- -----------------
  All                        0.390        0.177          0.222          0.091             0.057
  *Naranja*                  0.510        0.295          0.374          0.179             0.112
  *NaranjaVerde*             0.465        0.142          0.218          0.080             0.045
  *Limon*                    0.529        0.138          0.219          0.091             0.061
  *LimonVerde*               0.056        0.134          0.079          0.014             0.010

  : Unified per-class performance breakdown for the YOLOE-11m
  architecture. {#tab:test_yoloe_unified}

The multi-class confusion matrix for YOLOE-11m (Figure
[7.9](#fig:mc-limonnar){reference-type="ref"
reference="fig:mc-limonnar"}) highlights clear issues:

- **True Positives**: The architecture exhibits relatively stable
  localization for oranges (1,054 *Naranja* and 505 *NaranjaVerde*), but
  true sensitivity collapses for the new categories, dropping to just
  148 correct predictions for *LimonVerde*.

- **Cross-Class Bleeding**: Identical color spaces heavily override
  subtle shape variations, leading to massive semantic bleeding. The
  model misclassifies 761 *NaranjaVerde* instances as *LimonVerde*, 194
  *LimonVerde* instances as *NaranjaVerde*, and 308 *Limon* instances as
  *Naranja*.

- **Background Omissions**: Relegating hidden fruit to the background
  remains the dominant recall ceiling under complex canopy density,
  leaving 2,435 *Naranja*, 2,172 *NaranjaVerde*, 1,404 *Limon*, and 735
  *LimonVerde* completely undetected.

- **Background Hallucinations**: While foliage clutter is
  well-suppressed for the mature classes, false positives skyrocket
  under the *LimonVerde* prompt (1,654 background regions falsely
  segmented). This underscores that the lightweight text-guided heads
  struggle to distinguish intricate leaf patterns from the unripe lemon
  embedding.

<figure id="fig:mc-limonnar" data-latex-placement="H">
<img src="images/limonesynaranjas/confusion_matrix2.jpg"
style="width:80.0%" />
<figcaption>Confusion matrix for the unified dataset. Model: YOLOE-11m.
(Absolute instance counts).</figcaption>
</figure>

Isolating the lemon category resolves this semantic bleeding, allowing
the overall F1-score to jump to 0.387. *Limon* precision improves to
0.813, while green lemons achieve an F1-score of 0.343 with a balanced
precision of 0.384. This demonstrates that removing competing orange
tokens frees up the local feature maps, allowing the reparameterized
language heads to focus effectively on the target crop.

  **Class**        **Precision**   **Recall**   **F1-score**   **mAP@0.50**   **mAP@0.50:95**
  -------------- --------------- ------------ -------------- -------------- -----------------
  All                      0.599        0.302          0.387          0.224             0.142
  *Limon*                  0.813        0.293          0.431          0.273             0.173
  *LimonVerde*             0.384        0.310          0.343          0.176             0.111

  : Isolated lemon per-class performance breakdown for the YOLOE-11m
  architecture. {#tab:test_limones_yoloe_isolated}

The isolated confusion matrix (Figure
[7.10](#fig:mc-lim){reference-type="ref" reference="fig:mc-lim"})
illustrates the architectural efficiency of YOLOE-11m. The model
successfully detects 654 *Limon* and 342 *LimonVerde*, while keeping
background false positives remarkably low (118 for ripe and 405 for
green instances). Finally, 1,433 ripe lemons are still missing due to
canopy density.

<figure id="fig:mc-lim" data-latex-placement="H">
<img src="images/limones/confusion_matrix2.jpg" style="width:80.0%" />
<figcaption>Confusion matrix for the isolated lemon dataset. Model:
YOLOE-11m. (Absolute instance counts).</figcaption>
</figure>

## Strategic Agricultural Deployment Insights

The empirical findings from this taxonomic extension yield a decisive
conclusion for precision agriculture deployment: in the evaluated
scenarios, unified multi-class pipelines appeared less suitable than
crop-specific deployments. Forced multi-class token parsing triggers
severe cross-class confusion and causes a sharp drop in recall for newly
introduced crop categories.

As a result, the optimal engineering pathway requires decoupling
operations into crop-specific model instances:

- A dedicated instance initialized exclusively with the orange
  vocabulary (P4 and P1) for orange groves.

- An independent instance initialized with the isolated lemon vocabulary
  (P4: \"oval lemon\", \"oval green lemon\" and P1: \"lemon\", \"green
  lemon\") operating exclusively when navigating lemon fields.

Decoupling the inference pipeline allows architectures like YOLOE-11m to
increase their performance from an insufficient 0.222 F1 up to a
promising 0.387 F1, while running at an efficient 11.86 FPS. This
optimization indicates a highly encouraging trajectory for zero-shot
adaptation, although these values remain insufficient to guarantee fully
autonomous deployment in commercial agricultural operations without
further supervision.

# Conclusions and Future Work

The primary objective of this work was to conduct a robust and
comprehensive comparative evaluation of closed-vocabulary object
detection architectures against the emerging paradigms of
open-vocabulary object detection (OVOD) in a complex, real-world
precision agriculture environment.

By evaluating these models under a simulated field deployment scenario
(characterized by high foliage and fruit density, occlusions,
illumination variability, and chromatic mimicry), this research bridges
the gap between theoretical laboratory benchmarks and practical
real-world agricultural applications.

## Methodological Limitations

To provide a transparent framework for the empirical findings of this
study, it is necessary to formally outline the methodological
limitations and operational boundaries of the research. Far from
undermining the validity of the benchmark, these constraints define the
execution parameters required to maintain a feasible and rigorous scope
within the boundaries of this academic research framework:

- **Single Dataset Partitioning**: The supervised and open-vocabulary
  evaluations were restricted to a single, localized geographic data
  source and an individual data split partition. Due to time
  constraints, cross-validation techniques or multi-center orchard
  evaluations were omitted, which binds the baseline metrics to the
  regional imaging dynamics of the curated set.

- **Single-Run Deterministic Evaluation**: To accommodate the intensive
  computational requirements of hyperparameter tuning and model testing
  within the available timeline, the majority of the configurations were
  evaluated based on a single training and inference execution.
  Consequently, small numerical differentials between architectures must
  be interpreted as descriptive trends rather than definitive
  statistical indicators, as they lack confidence interval margins.

- **Sequential Parameter Selection Bias**: The optimization workflow for
  the open-vocabulary candidates followed a strictly sequential stage
  progression under a fixed baseline confidence threshold. While this
  strategy successfully isolated parameter trends without triggering an
  exponential growth of experimental combinations, it may fail to locate
  the global multi-variable mathematical optimum, potentially favoring
  architectures whose confidence output was naturally aligned with the
  fixed initial baseline.

- **Desktop-to-Edge Operational Translation**: The inference throughput
  and computational efficiency metrics (FPS) reported throughout this
  study were benchmarked on a high-performance desktop workstation
  architecture (NVIDIA RTX 5070). These speed values represent an
  upper-bound potential and cannot be directly extrapolated as evidence
  of real-time viability on resource-constrained embedded field robotics
  or edge computing units.

- **Interpretative Nature of Architectural Failures**: The structural
  explanations proposed to justify model errors (such as attributing
  false positives to leaf specular reflections or token representation
  dilution) are advanced as technical hypotheses derived from visual
  analysis, rather than causally proven physical relations, since
  isolated optical testing environments were beyond the scope of this
  project.

- **Exploratory Taxonomic Extension and Domain Shifts**: The scalability
  experiments conducted with lemons retain a strictly exploratory
  nature. The results are subject to a dual confounding factor: first,
  the unverified latent presence of the target classes within the
  massive web-scale pre-training data of the foundational backbones; and
  second, a pronounced domain shift, as the lemon images originated from
  distinct crowdsourced digital repositories, introducing variations in
  lighting, background styles, and camera sensors that independently
  affect zero-shot visual alignment.

- **Absence of a Dedicated Lemon Validation Split**: Due to the scarcity
  and limited scale of the assembled lemon evaluation subset, it was
  structurally unfeasible to isolate an independent validation partition
  to replicate the systematic hyperparameter search executed for the
  orange domain in Chapter [5](#cap:ovod){reference-type="ref"
  reference="cap:ovod"}. Consequently, the optimal operational
  parameters (prompts, tiling choices, and NMS thresholds) were directly
  transferred from the orange validation setup. This leaves open the
  methodological question of whether the models' optimal configurations
  would fluctuate or deviate when explicitly calibrated on the visual
  dynamics of the novel crop variety.

## Achievement of Research Objectives

The main empirical objectives were achieved:

- **Comprehensive Dataset Curation:** In the absence of well-annotated
  datasets capturing real agricultural environments, the original
  dataset obtained from Roboflow (comprising two classes, *Naranja* and
  *NaranjaVerde*) was subjected to a thorough re-annotation process.
  Using an interactive tool developed with OpenCV, the full curation
  pipeline was carried out: image removal, label deletion, and label
  addition. Following this exhaustive manual process, a contextually
  consistent ground truth of 546 high-resolution, high-quality images
  was established, producing a clean benchmark for zero-shot evaluation.

- **Establishment of a High-Quality Baseline:** With a curated dataset
  in place, model performance could be evaluated in isolation. To
  provide a reference for open-vocabulary models, a supervised YOLO11
  model was trained. The Small variant achieved the best results, with
  an F1-score of 0.756 and a mAP@0.50 of 0.769 on the validation set,
  demonstrating that accurate fruit detection and ripeness
  classification are highly achievable when domain-specific supervision
  is available. The remaining performance gap likely reflects a
  combination of dataset difficulty, architectural constraints, training
  choices, image resolution, split composition, and annotation
  uncertainty

- **OVOD Model Benchmarking:** Five representative open-vocabulary
  architectures were evaluated: Grounding DINO, OWLv2, YOLO-World,
  YOLOE, and SAM 3, under a strict zero-shot paradigm. Through a
  controlled ablation pipeline, the optimal prompts for each model were
  identified, the necessity of full-image context for reliable detection
  was established (contradicting the initial hypothesis that image
  tiling would improve detection of small and occluded fruit), and the
  architecture-specific NMS post-processing requirements were
  determined. Additionally, confidence thresholds were found to vary
  across models, consistently falling within a low range of 0.010 to
  0.230.

- **Novel Class Generalization Analysis:** Following the selection of
  the best-performing models, their generalization capacity was
  evaluated by introducing a new crop variety: lemons, both ripe and
  unripe. Through simple prompt modifications, the models'
  transferability was assessed. The analysis concluded that processing
  each crop category independently yields better detection performance,
  as introducing multiple classes simultaneously generates semantic
  noise and degrades overall accuracy.

## Empirical Findings and Model Stratification

Evaluating the models on the test set revealed a clear performance
stratification among the open-vocabulary architectures, exposing a
fundamental trade-off between architectural complexity, linguistic
representation, and computational throughput. To synthesize these
behavioral patterns, the evaluated models can be classified into three
distinct technical paradigms:

- **Transformer-Based Dense Object Detectors:** The representative
  models of this category are OWLv2 and Grounding DINO. These
  architectures are characterized by high Recall, yet are highly
  susceptible to severe visual hallucinations against the background,
  exacerbated by illumination reflections. Although OWLv2 achieves the
  strongest results among these architectures, both exhibit low
  inference throughput (0.34 FPS for OWLv2 and 1.79 FPS for Grounding
  DINO), making them inviable for real-time deployment. Nevertheless, as
  the focus of this work is on behavioral analysis rather than
  operational viability, these results remain relevant for
  characterizing model behavior in real agricultural environments.

- **Precise Convolutional Regressors:** The representative models of
  this category are YOLO-Worldx and YOLOE-11m. In contrast to
  Transformer-based models, these architectures achieve excellent
  Precision (consistently exceeding the 0.60 threshold), producing clean
  and well-localized bounding boxes. Moreover, following the behavioral
  patterns of the supervised YOLO baseline, these models demonstrate
  strong inter-class discrimination, with near-negligible cross-class
  confusion. They are further distinguished by their high inference
  throughput (approximately 8.10--8.99 FPS), making them the strongest
  candidates for real-world deployment. However, as noted, operational
  deployment is not the primary focus of this work, and OWLv2 still
  outperforms them in terms of absolute detection metrics.

- **Concept Segmenters:** Represented by SAM 3. This model exhibited a
  severe performance degradation under dense object clustering,
  recording an F1-score of only 0.150. Segmentation quality was severely
  degraded by foliage occlusions. While its inference speed is moderate
  (4.19 FPS), it is unsuitable both as a standalone detector and for
  real-world field deployment.

The global comparison allows the true bottlenecks of zero-shot models in
open-field scenarios to be identified. The core challenge does not lie
in semantic inter-class confusion (as most architectures effectively
learned to discriminate the linguistic variance between ripe and unripe
fruit) but rather in the inability to discriminate the background
environment. The complex textures of the foliage induced massive visual
hallucinations in pure Transformer models, severely degrading their
global Precision.

OWLv2 recorded the highest absolute F1-score among all OVOD models
(0.519), yet its computational latency is prohibitively high.
Consequently, YOLO-Worldx and YOLOE-11m emerge as the most well-balanced
architectures in terms of both performance and inference efficiency
(F1-scores between 0.447 and 0.456, at 8.10--8.99 FPS).

## Generalization to Novel Classes {#generalization-to-novel-classes}

The zero-shot extension to lemon detection demonstrated the semantic
flexibility inherent to open-vocabulary paradigms (a capability absent
in closed-vocabulary models) through the simple addition of a new prompt
per class. However, this process also exposed the limitations associated
with vocabulary expansion. Introducing a new morphologically challenging
variety increases semantic noise and degrades overall model performance.
Furthermore, the chromatic mimicry of unripe lemons with surrounding
foliage induced a generalized performance drop across all evaluated
models.

A comparative analysis of different inference strategies led to a key
conclusion: deploying independent, crop-specific models is superior to a
unified multi-class inference approach. When oranges and lemons were
processed simultaneously, the overlap of shared semantic concepts and
linguistic tokens saturated the feature maps, causing models to confuse
ripe lemons with ripe oranges and unripe lemons with unripe oranges.
Operating under crop-isolated prompts eliminated this noise,
significantly restoring detection accuracy, enabling YOLOE-11m to scale
from an F1-score of 0.222 to 0.387.

This crop-isolated deployment strategy is particularly well-suited for
environments where the target fruit variety is known in advance, and no
inter-variety mixing is expected. In such cases, accurate detection
simply requires associating the corresponding prompt with the target
crop.

## Future Research Directions

To advance the operational capabilities of open-vocabulary architectures
in dynamic agricultural environments, the following future research
directions are proposed:

- **Few-Shot Learning:** The present work evaluated all models
  exclusively under a zero-shot regime. However, open-vocabulary
  architectures from the YOLO family support the injection of a very
  limited number of domain-specific annotations (between 5 and 20
  images). Future work could investigate whether Few-Shot fine-tuning
  adapts the bimodal encoder weights to the local orchard background
  without incurring the high annotation costs associated with fully
  supervised training.

- **Knowledge Distillation:** A promising research direction involves
  training a lightweight, fast model to learn from the correct
  predictions of a larger, heavier model (such as OWLv2), with the goal
  of combining the best properties of both: inference speed and
  detection accuracy.

- **Exploration of Alternative Prompting Mechanisms:** Leveraging the
  native multimodal flexibility of YOLOE to transition from purely
  textual descriptors to visual prompts (SAVPE) or instruction-free
  internal vocabularies (prompt-free mode), assessing whether the use of
  reference fruit images as exemplars mitigates the linguistic ambiguity
  introduced by foliage density.

# Glossary

**Baseline**: A highly optimized reference model used as a quantitative
benchmark to evaluate and contrast the relative performance gains,
accuracy trade-offs, or structural variations of newly introduced
architectures within the same experimental setup.

**Chromatic Camouflage**: An agricultural computer vision challenge
where an object of interest, such as unripe green fruit, shares a nearly
identical color space and visual texture with the vegetative background
canopy, complicating feature extraction.

**Closed-Vocabulary Object Detection**: The traditional object detection
paradigm where a deep learning model is mathematically restricted to
recognizing and bounding a fixed, predefined set of target classes seen
during its supervised training phase.

**Confusion Matrix**: A tabular cross-reference visualization tool that
maps true target labels against model-predicted categories, explicitly
identifying distinct trajectory errors such as inter-class
misclassifications or background false positives.

**Contrastive Loss**: An optimization loss function used in multimodal
pre-training that minimizes the vector distance between true image-text
pairs in a shared projection space while actively maximizing the
distance between mismatched or negative pairs.

**Domain Shift**: A machine learning challenge where a model experiences
a performance drop because the statistical distribution, environmental
lighting, or sensor physics of the target deployment dataset deviates
from the source data used during training or optimization.

**Edge AI**: The engineering practice of running optimized machine
learning inference tasks locally on small, resource-constrained physical
embedded hardware or robotic units directly on-site, removing latency
and cloud-infrastructure dependencies.

**Embeddings**: Low-dimensional continuous vector representations
generated by deep neural networks to encapsulate the abstract semantic,
text-based, or visual properties of inputs, where geometric proximity
corresponds directly to conceptual similarity.

**F1-score**: A unified performance indicator computed as the harmonic
mean of precision and recall, providing a balanced measurement of a
model's joint counting and classification capabilities under a single
score.

**Grounding DINO**: A high-capacity open-vocabulary detector that
marries the DINO transformer architecture with grounded language
pre-training, executing deep cross-modal feature fusion through
bidirectional image-text attention layers from the earliest stages of
the network.

**Intersection over Union (IoU)**: A geometric metric that quantifies
the spatial alignment between two bounding boxes or segmentation
regions, calculated by dividing the area of their intersection by the
total combined area of their union.

**Mean Average Precision (mAP)**: The standard metric for object
detection evaluation that computes the average precision across a set of
classes, traditionally measured at a static IoU threshold of 0.50 or
averaged across a dynamic range from 0.50 to 0.95.

**Non-Maximum Suppression (NMS)**: A mandatory spatial filtering
post-processing algorithm that purges redundant, highly overlapping
candidate bounding boxes or masks predicting the same physical instance,
retaining only the single proposal with the highest confidence score.

**Occlusion**: A physical constraint in unstructured environments where
foreground obstacles, such as leaves, branches, or competing fruit
clusters, partially or entirely block an object's silhouette, disrupting
geometric boundaries and feature grounding.

**Open-Vocabulary Object Detection (OVOD)**: A computer vision paradigm
where a model can classify and localize arbitrary categories of objects
that were not explicitly annotated during its supervised training phase,
leveraging language-image semantic alignments to recognize novel
concepts at inference time.

**OWLv2**: An open-vocabulary object detection architecture developed by
Google DeepMind that utilizes a patch-based Vision Transformer backbone
trained via large-scale web self-training on billions of noisy
image-text pairs extracted from alternative image descriptions.

**Precision**: A predictive metric that measures the reliability of a
model's positive output by calculating the ratio of correctly identified
target objects over the total number of detections generated, penalizing
background false positives.

**Presence Token**: An original architectural module that decouples
object recognition from spatial localization by outputting an
independent image-wide classification probability to determine if a
concept exists in the frame before predicting coordinates.

**Prompt Ablation**: A systematic experimental process consisting of
evaluating a model against varying levels of text prompt complexity,
syntactic layout, or descriptive constraints to isolate and measure how
linguistic phrasing impacts vision-language embedding alignment.

**Recall**: A sensitivity metric that evaluates the exhaustive
localization capacity of a detector by calculating the ratio of
successfully found target instances over the actual number of ground
truth objects present in the dataset, penalizing omissions.

**RepVL-PAN**: An advanced, reparameterizable path aggregation network
that dynamically weaves language embedding tokens into structural visual
feature pyramids during training, allowing the textual inputs to be
compressed out prior to deployment.

**RT-DETR (Real-Time Detection Transformer)**: The first end-to-end,
transformer-based object detection architecture designed for real-time
inference, which completely bypasses the execution latency and
optimization bottlenecks of Non-Maximum Suppression (NMS) by employing a
query-based decoder coupled with an efficient hybrid encoder for
multi-scale feature interaction and an IoU-aware query selection
strategy.

**SAM 3 (Segment Anything Model 3)**: A unified foundational perception
framework designed for promptable concept segmentation and temporal
instance tracking, capable of isolating individual object boundaries
based on textual noun phrases or visual point/box prompts.

**Semantic Bleeding**: A failure mode in open-vocabulary inference where
highly overlapping color descriptions or morphologically similar prompts
cause the language-vision projection maps to blend, leading the model to
confuse related classes under an expanded label space.

**Tiling**: An image preprocessing technique that cuts a high-resolution
canvas into multiple lower-resolution, overlapping patches or
sub-windows to preserve fine-grained localized details and prevent tiny
or dense object clusters from being downscaled and omitted.

**Vision Transformer (ViT)**: A neural network architecture for computer
vision that dispenses with traditional localizing convolutional
operations, instead slicing input images into patch tokens and
processing them through global self-attention modules.

**Vision-Language Models (VLMs)**: A class of multimodal deep learning
systems that project visual feature maps and linguistic representations
into a unified, shared embedding space to model complex relationships
between pixels and words.

**YOLO (You Only Look Once)**: A prominent family of single-stage object
detection architectures that reframes the localization and
classification problem as a single regression task, predicting bounding
box coordinates and class probabilities simultaneously in a single
forward pass.

**YOLO-World**: A real-time open-vocabulary object detection network
that replaces standard classification heads with a Reparameterizable
Vision-Language Path, enabling user-defined text prompts to be encoded
directly into static convolutional weights prior to deployment.

**YOLOE**: A real-time open-vocabulary detection and segmentation
architecture built on an advanced reparameterized text engine that
unifies multiple prompt modalities, allowing dynamic inference via text
queries, reference image exemplars, or unprompted internal vocabularies.

# Execution Environment {#execution_environment}

All experiments were conducted within a single local environment. The
hardware and software configuration used is detailed below:

- **Operating System**: Windows 11. This system provides the native
  driver support required for the graphics card and ensures proper
  dependency management within the development environment.

- **Processor (CPU)**: AMD Ryzen 5 7600X, reaching up to 5.3 GHz. The
  high clock frequencies are critical during the training phase for
  efficiently managing data preprocessing and preventing bottlenecks in
  the image feed pipeline to the GPU.

- **GPU**: NVIDIA GeForce RTX 5070 with 12 GB of video memory (GDDR7).
  This component is the core of the training process, handling intensive
  matrix computations. The 12 GB VRAM capacity is the limiting factor in
  determining batch size, which motivated the decision to use the
  Ultralytics automatic batch size optimizer (set to -1 during training)
  to maximize memory utilization without incurring out-of-memory errors.

- **RAM**: 32 GB DDR5 at 6,000 MHz. The use of high-speed, low-latency
  memory allows large data volumes to be loaded into memory and data
  augmentation techniques to be applied without compromising overall
  system stability.

  - **Supervised Baseline (YOLO11)**: The training, hyperparameter
    optimization, and initial evaluation of the supervised model were
    executed using Jupyter Notebook. This facilitated interactive
    debugging, data augmentation validation, and rapid logging of loss
    curves through the native Ultralytics (version 8.4.46) API.

  - **Open-Vocabulary Framework (OVOD)**: The zero-shot evaluation
    pipeline for the open-vocabulary candidates was developed as a
    modular automated testing suite within Visual Studio. This
    environment executed independent scripting workflows for model
    orchestration: Hugging Face `transformers` library was utilized to
    deploy and process the Vision-Language granular tokenization of
    Grounding DINO Base and OWLv2, while dedicated scripts leveraged
    Ultralytics extensions to run YOLO-World, YOLOE, and SAM 3. All OVOD
    variants were bound to a standardized evaluation pipeline
    (`utils.py`) designed to compute agnostic IoU matching, aggregate
    mAP@0.50:95 metrics, and plot custom performance curves uniformly.

# Dataset Curation and Refinement Tool {#appendix:refinement_tool}

## General Description

To ensure maximum precision in the ground truth annotations and address
the defects identified in the original labels, an interactive visual
inspection algorithm was designed. This tool enables a thorough review
of each image through a dynamic navigation system, particularly
well-suited for regions with high fruit density.

## User Interface and Navigation System

The software renders each image in full screen and supports interaction
via mouse and keyboard (see Figure
[11.1](#fig:interfaz_tool){reference-type="ref"
reference="fig:interfaz_tool"}). Since unripe oranges exhibit strong
chromatic camouflage with surrounding leaves, the tool provides zoom and
panning functionality, facilitating the identification of fruit located
in the background or obscured by branches, and enabling accurate
annotation.

<figure id="fig:interfaz_tool" data-latex-placement="h">
<img src="images/python-script.jpg" style="width:90.0%" />
<figcaption>Interface of the refinement tool, showing the annotation
visualization system and the dynamic zoom assistance.</figcaption>
</figure>

## Algorithmic Foundations

### Dynamic Visual Magnification

The visualization module employs a mathematical transformation matrix to
magnify and pan the on-screen view without modifying the original image
pixels. This allows the user to explore complex regions at up to
15$\times$ magnification without altering the source file (see Figure
[11.2](#fig:zoom){reference-type="ref" reference="fig:zoom"}).

<figure id="fig:zoom" data-latex-placement="h">
<img src="images/zoom.jpg" style="width:90.0%" />
<figcaption>Example of dynamic visual magnification (zoom) in the
refinement tool.</figcaption>
</figure>

### Inverse Coordinate Mapping

When the user clicks or draws a selection box over a magnified region,
the system performs an inverse coordinate transformation. This process
maps the cursor's on-screen position back to the exact corresponding
coordinate in the original full-resolution image. This mechanism enables
fully precise addition or deletion of bounding box annotations,
regardless of the current zoom level.

### YOLO Label Recalculation

The standard YOLO annotation format stores bounding boxes using the
normalized center coordinates and dimensions (values in the range \[0,
1\]). When the user applies a crop operation, the algorithm
automatically recomputes the position and dimensions of all existing
labels to align with the new image boundaries, discarding any
annotations that fall outside the cropped region.

## Tool Operation Manual

  **Category**   **Control**    **Description**
  -------------- -------------- --------------------------------------------------------------------------------------
  *Navigation*   Mouse Wheel    Zooms in or out, centered on the cursor position.
  *Navigation*   Right Button   Pans the image across the screen.
  *Editing*      Left Button    Draws a rectangular selection box over a working area.
  *Action*       Key **A**      Adds a new annotation within the selected area (Ripe Orange or Unripe Orange class).
  *Action*       Key **E**      Deletes all annotations contained within the selected area.
  *Action*       Key **C**      Crops the image to retain only the selected area.
  *System*       Key **S**      Saves the final image and its updated annotations to disk.
  *System*       Key **D**      Discards all changes and advances to the next image.

  : Summary of controls for the dataset refinement tool.

## Algorithmic Structure of the Software

The internal logic of the interactive system is described below in
pseudocode, outlining the overall application behavior and event
handling:

``` {language="" caption="Pseudocode of the interactive dataset curation tool."}
Algorithm Dataset_Curation_and_Refinement
Begin
    For each Image in dataset do
        Load Original_Image and Label_List (YOLO format)
        Initialize State (Zoom_Level = 1.0, Offset = (0, 0))
        Initialize User_Selection = empty

        While user has not chosen Save or Discard do
            Apply Zoom and Offset to image and its annotations
            Render full-screen view and await user interaction

            // --- Mouse Event Handling ---
            If Mouse_Wheel then
                Update Zoom_Level centered on cursor position
            Else If Right_Button_Drag then
                Update Offset (pan view across the screen)
            Else If Left_Button_Drag then
                Update User_Selection coordinates (draw selection box)
            End If

            // --- Keyboard Event Handling ---
            If Key 'A' (Add) then
                Real_Area = Inverse_Mapping(User_Selection)
                Prompt user for class (Ripe Orange or Unripe Orange)
                Compute normalized center and dimensions of new box
                Append new box to Label_List
                User_Selection = empty

            Else If Key 'E' (Erase) then
                Real_Area = Inverse_Mapping(User_Selection)
                Remove from Label_List all boxes within Real_Area
                User_Selection = empty

            Else If Key 'C' (Crop) then
                Real_Area = Inverse_Mapping(User_Selection)
                Crop Original_Image to Real_Area
                Recompute normalized coordinates of surviving annotations
                Reset Zoom_Level = 1.0 and Offset = (0, 0)
                User_Selection = empty

            Else If Key 'R' (Reset) then
                Reload Original_Image and initial Label_List from disk
                Reset Zoom_Level and Offset

            Else If Key 'S' (Save) then
                Write current Original_Image and Label_List to disk
                Exit While loop (advance to next image)

            Else If Key 'D' (Discard) then
                Exit While loop without saving any changes
            End If
        End While
    End For
End
```

# YOLO-World: Validation Set Experiments {#ap_c}

This appendix presents the validation phase experiments conducted with
YOLO-World models across four size variants (Small, Medium, Large, and
Extra-Large). For each model, the same three-step ablation pipeline is
followed: selecting the optimal prompt, evaluating whether image tiling
improves detection, and tuning the NMS threshold to suppress duplicate
bounding boxes.

## YOLO-World Small

The lightest variant is evaluated first, designed for
resource-constrained devices where inference speed is the primary
requirement.

  **Prompt**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  ------------ --------------- ------------ -------- -------------- -----------------
  P1                     0.692        0.248    0.348          0.202             0.119
  P2                     0.477        0.276    0.279          0.211             0.123
  P3                     0.339        0.296    0.304          0.171             0.095
  P4                     0.499        0.184    0.192          0.117             0.069
  P5                     0.317        0.311    0.309          0.186             0.103
  P6                     0.480        0.181    0.215          0.139             0.079

  : Prompt ablation on the validation set. Model: YOLO-World S.
  {#tab:prompts_yws}

With P1 selected as the optimal prompt, the impact of image tiling
versus full-image processing is assessed. In direct inference mode, the
model operates at a competitive speed of 11--13 FPS.

  **Configuration**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**   **FPS**
  ------------------- --------------- ------------ -------- -------------- ----------------- ---------
  **No tiling**                 0.692        0.248    0.348          0.202             0.119    13.060
  Tiling                        0.497        0.284    0.360          0.195             0.109     2.300

  : Tiling evaluation on the validation set. Prompt P1. Model:
  YOLO-World S. {#tab:tiling_yws}

Retaining full-image processing for its speed advantage, the NMS
threshold is swept to assess its effect on suppressing duplicate
detections in high-density fruit regions.

  **NMS**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  --------- --------------- ------------ -------- -------------- -----------------
  0.2                 0.697        0.246    0.347          0.199             0.118
  0.3                 0.686        0.249    0.348          0.202             0.119
  0.4                 0.695        0.248    0.348          0.202             0.119
  0.5                 0.692        0.248    0.348          0.202             0.119
  0.6                 0.686        0.249    0.348          0.202             0.119
  0.7                 0.676        0.250    0.346          0.201             0.120

  : NMS threshold sweep on the validation set. Prompt P1, no tiling.
  Model: YOLO-World S. {#tab:nms_yws}

## YOLO-World Medium

The medium-sized variant is evaluated to determine whether its increased
capacity improves the detection of small or heavily occluded fruit
within the tree canopy.

  **Prompt**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  ------------ --------------- ------------ -------- -------------- -----------------
  P1                     0.666        0.292    0.392          0.250             0.155
  P2                     0.457        0.284    0.281          0.183             0.113
  P3                     0.366        0.324    0.334          0.215             0.132
  P4                     0.662        0.236    0.315          0.178             0.107
  P5                     0.255        0.313    0.273          0.168             0.098
  P6                     0.689        0.195    0.267          0.155             0.086

  : Prompt ablation on the validation set. Model: YOLO-World M.
  {#tab:prompts_ywm}

With P1 selected, tiling is compared against full-image processing.

  **Configuration**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**   **FPS**
  ------------------- --------------- ------------ -------- -------------- ----------------- ---------
  **No tiling**                 0.666        0.292    0.392          0.250             0.155    10.950
  Tiling                        0.502        0.353    0.403          0.242             0.137     1.600

  : Tiling evaluation on the validation set. Prompt P1. Model:
  YOLO-World M. {#tab:tiling_ywm}

The NMS threshold is tuned to remove redundant detections produced by
this model.

  **NMS**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  --------- --------------- ------------ -------- -------------- -----------------
  0.2                 0.683        0.287    0.392          0.247             0.153
  0.3                 0.680        0.289    0.393          0.247             0.154
  0.4                 0.675        0.291    0.393          0.250             0.155
  0.5                 0.666        0.292    0.392          0.250             0.155
  0.6                 0.655        0.293    0.390          0.249             0.155

  : NMS threshold sweep on the validation set. Prompt P1, no tiling.
  Model: YOLO-World M. {#tab:nms_ywm}

## YOLO-World Large

The large variant is evaluated to assess whether increased model
capacity improves sensitivity for detecting the most challenging fruit
instances within the orchard.

  **Prompt**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  ------------ --------------- ------------ -------- -------------- -----------------
  P1                     0.629        0.309    0.394          0.268             0.171
  P2                     0.462        0.325    0.354          0.236             0.148
  P3                     0.377        0.322    0.345          0.232             0.145
  P4                     0.619        0.287    0.370          0.227             0.146
  P5                     0.283        0.254    0.231          0.127             0.078
  P6                     0.738        0.270    0.365          0.233             0.145

  : Prompt ablation on the validation set. Model: YOLO-World L.
  {#tab:prompts_ywl}

Using prompt P1, the effect of tiling on detecting fruit occluded by
dense branching is examined.

  **Configuration**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**   **FPS**
  ------------------- --------------- ------------ -------- -------------- ----------------- ---------
  **No tiling**                 0.629        0.309    0.394          0.268             0.171    11.240
  Tiling                        0.470        0.415    0.429          0.282             0.160     1.130

  : Tiling evaluation on the validation set. Prompt P1. Model:
  YOLO-World L. {#tab:tiling_ywl}

The NMS threshold is fine-tuned for the final full-image processing
configuration.

  **NMS**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  --------- --------------- ------------ -------- -------------- -----------------
  0.2                 0.639        0.304    0.394          0.266             0.160
  0.3                 0.638        0.306    0.395          0.266             0.170
  0.4                 0.634        0.307    0.395          0.266             0.170
  0.5                 0.629        0.309    0.394          0.268             0.171
  0.6                 0.620        0.310    0.392          0.268             0.171

  : NMS threshold sweep on the validation set. Prompt P1, no tiling.
  Model: YOLO-World L. {#tab:nms_ywl}

## YOLO-World Extra-Large

The largest model in this family is evaluated to determine whether its
maximum representational capacity helps resolve shadow and
foliage-related detection failures in the orchard.

  **Prompt**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  ------------ --------------- ------------ -------- -------------- -----------------
  P1                     0.718        0.270    0.355          0.236             0.151
  P2                     0.470        0.364    0.398          0.292             0.183
  P3                     0.572        0.286    0.370          0.200             0.126
  P4                     0.635        0.350    0.451          0.296             0.183
  P5                     0.459        0.303    0.354          0.209             0.128
  P6                     0.763        0.239    0.326          0.212             0.135

  : Prompt ablation on the validation set. Model: YOLO-World X.
  {#tab:prompts_ywx}

With P4 selected, inference speed and detection accuracy are measured
with and without image tiling.

  **Configuration**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**   **FPS**
  ------------------- --------------- ------------ -------- -------------- ----------------- ---------
  **No tiling**                 0.635        0.350    0.451          0.296             0.183     8.300
  Tiling                        0.457        0.465    0.457          0.321             0.174     0.790

  : Tiling evaluation on the validation set. Prompt P4. Model:
  YOLO-World X. {#tab:tiling_ywx}

The NMS threshold is tuned to suppress duplicate bounding boxes from
this large-scale model.

  **NMS**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  --------- --------------- ------------ -------- -------------- -----------------
  0.3                 0.642        0.348    0.450          0.293             0.182
  0.4                 0.640        0.349    0.451          0.297             0.183
  0.5                 0.635        0.350    0.451          0.296             0.183
  0.6                 0.626        0.350    0.449          0.296             0.184

  : NMS threshold sweep on the validation set. Prompt P4, no tiling.
  Model: YOLO-World X. {#tab:nms_ywx}

# YOLOE: Validation Set Experiments {#ap_d}

This appendix presents the validation results for YOLOE models across
its three main architectural families (YOLOE-8, YOLOE-11, and YOLOE-26).
The experiments evaluate the influence of prompt selection, image
tiling, and NMS threshold tuning on detection performance.

## YOLOE-8

The first YOLOE branch is evaluated across its Small, Medium, and Large
size variants.

### YOLOE-8 Small

The smallest variant is assessed for its suitability in fast,
resource-constrained deployment scenarios.

  **Prompt**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  ------------ --------------- ------------ -------- -------------- -----------------
  P1                     0.448        0.287    0.339          0.219             0.128
  P2                     0.552        0.235    0.260          0.164             0.095
  P3                     0.509        0.297    0.343          0.243             0.144
  P4                     0.445        0.329    0.355          0.256             0.146
  P5                     0.438        0.318    0.348          0.253             0.147
  P6                     0.318        0.261    0.284          0.120             0.064

  : Prompt ablation on the validation set. Model: YOLOE-8 S.
  {#tab:prompts_yes}

Prompt P4 is selected for its best F1-score, and the impact of image
tiling against full-image processing is evaluated.

  **Configuration**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**   **FPS**
  ------------------- --------------- ------------ -------- -------------- ----------------- ---------
  **No tiling**                 0.445        0.329    0.355          0.256             0.146     9.530
  Tiling                        0.246        0.451    0.265          0.240             0.135     1.350

  : Tiling evaluation on the validation set. Prompt P4. Model: YOLOE-8
  S. {#tab:tiling_yes}

The NMS threshold is swept to assess its effect on duplicate bounding
box suppression.

  **NMS**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  --------- --------------- ------------ -------- -------------- -----------------
  0.3                 0.454        0.325    0.355          0.254             0.145
  0.4                 0.452        0.327    0.356          0.256             0.145
  0.5                 0.445        0.329    0.355          0.256             0.146
  0.6                 0.435        0.331    0.353          0.255             0.147

  : NMS threshold sweep on the validation set. Prompt P4, no tiling.
  Model: YOLOE-8 S. {#tab:nms_yes}

### YOLOE-8 Medium

The medium variant is evaluated for potential improvements in fruit
detection precision.

  **Prompt**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  ------------ --------------- ------------ -------- -------------- -----------------
  P1                     0.539        0.193    0.232          0.141             0.088
  P2                     0.536        0.227    0.283          0.138             0.082
  P3                     0.601        0.280    0.382          0.221             0.135
  P4                     0.610        0.330    0.428          0.260             0.148
  P5                     0.460        0.331    0.379          0.259             0.154
  P6                     0.301        0.113    0.161          0.041             0.024

  : Prompt ablation on the validation set. Model: YOLOE-8 M.
  {#tab:prompts_yem}

With prompt P4, tiled versus full-image performance is compared.

  **Configuration**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**   **FPS**
  ------------------- --------------- ------------ -------- -------------- ----------------- ---------
  **No tiling**                 0.610        0.330    0.428          0.260             0.148     9.640
  Tiling                        0.298        0.434    0.321          0.232             0.128     1.160

  : Tiling evaluation on the validation set. Prompt P4. Model: YOLOE-8
  M. {#tab:tiling_yem}

The NMS threshold is tuned to clean up overlapping detections.

  **NMS**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  --------- --------------- ------------ -------- -------------- -----------------
  0.1                 0.627        0.320    0.424          0.254             0.145
  0.2                 0.626        0.326    0.428          0.257             0.146
  0.3                 0.623        0.327    0.428          0.257             0.147
  0.4                 0.617        0.328    0.428          0.257             0.148
  0.5                 0.610        0.330    0.428          0.260             0.148
  0.6                 0.598        0.331    0.426          0.261             0.148

  : NMS threshold sweep on the validation set. Prompt P4, no tiling.
  Model: YOLOE-8 M. {#tab:nms_yem}

### YOLOE-8 Large

The large variant is evaluated to investigate whether increased scale
stabilizes detections in complex foliage regions.

  **Prompt**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  ------------ --------------- ------------ -------- -------------- -----------------
  P1                     0.594        0.286    0.369          0.234             0.141
  P2                     0.638        0.282    0.381          0.207             0.127
  P3                     0.659        0.312    0.421          0.258             0.156
  P4                     0.673        0.318    0.431          0.250             0.150
  P5                     0.562        0.329    0.411          0.255             0.156
  P6                     0.483        0.228    0.309          0.137             0.082

  : Prompt ablation on the validation set. Model: YOLOE-8 L.
  {#tab:prompts_yel}

Inference speed and accuracy are measured with and without image tiling.

  **Configuration**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**   **FPS**
  ------------------- --------------- ------------ -------- -------------- ----------------- ---------
  **No tiling**                 0.673        0.318    0.431          0.250             0.150     8.720
  Tiling                        0.333        0.440    0.353          0.261             0.148     0.920

  : Tiling evaluation on the validation set. Prompt P4. Model: YOLOE-8
  L. {#tab:tiling_yel}

The NMS threshold is tuned to balance detection coverage and
specificity.

  **NMS**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  --------- --------------- ------------ -------- -------------- -----------------
  0.2                 0.691        0.315    0.432          0.248             0.149
  0.3                 0.688        0.316    0.433          0.248             0.150
  0.4                 0.681        0.317    0.432          0.247             0.150
  0.5                 0.673        0.318    0.431          0.250             0.150
  0.6                 0.662        0.319    0.430          0.249             0.150

  : NMS threshold sweep on the validation set. Prompt P4, no tiling.
  Model: YOLOE-8 L. {#tab:nms_yel}

## YOLOE-11

The YOLOE-11 branch is evaluated next, featuring improved
vision-language alignment mechanisms relative to the YOLOE-8 family.

### YOLOE-11 Small

The small variant is assessed for its agility in orchard detection
tasks.

  **Prompt**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  ------------ --------------- ------------ -------- -------------- -----------------
  P1                     0.575        0.219    0.316          0.157             0.090
  P2                     0.621        0.251    0.354          0.187             0.106
  P3                     0.565        0.276    0.370          0.219             0.127
  P4                     0.565        0.262    0.354          0.193             0.111
  P5                     0.487        0.283    0.358          0.218             0.127
  P6                     0.357        0.205    0.257          0.087             0.047

  : Prompt ablation on the validation set. Model: YOLOE-11 S.
  {#tab:prompts_ye11s}

With P3 selected, the effect of image tiling on detection performance is
evaluated.

  **Configuration**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**   **FPS**
  ------------------- --------------- ------------ -------- -------------- ----------------- ---------
  **No tiling**                 0.565        0.276    0.370          0.219             0.127    10.450
  Tiling                        0.245        0.433    0.289          0.271             0.158     1.490

  : Tiling evaluation on the validation set. Prompt P3. Model: YOLOE-11
  S. {#tab:tiling_ye11s}

The NMS threshold is swept to refine bounding box predictions.

  **NMS**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  --------- --------------- ------------ -------- -------------- -----------------
  0.1                 0.608        0.267    0.371          0.215             0.125
  0.2                 0.601        0.270    0.372          0.218             0.127
  0.3                 0.594        0.271    0.372          0.218             0.127
  0.4                 0.582        0.273    0.371          0.220             0.127
  0.5                 0.565        0.276    0.370          0.219             0.127
  0.6                 0.549        0.277    0.368          0.218             0.127

  : NMS threshold sweep on the validation set. Prompt P3, no tiling.
  Model: YOLOE-11 S. {#tab:nms_ye11s}

### YOLOE-11 Medium

The medium variant is evaluated seeking to maximize the overall
detection balance in the orchard setting.

  **Prompt**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  ------------ --------------- ------------ -------- -------------- -----------------
  P1                     0.606        0.288    0.383          0.237             0.144
  P2                     0.598        0.262    0.339          0.196             0.118
  P3                     0.630        0.321    0.423          0.278             0.169
  P4                     0.673        0.348    0.459          0.300             0.177
  P5                     0.507        0.354    0.409          0.295             0.176
  P6                     0.441        0.207    0.280          0.127             0.076

  : Prompt ablation on the validation set. Model: YOLOE-11 M.
  {#tab:prompts_ye11m}

With prompt P4, tiled versus full-image performance is compared.

  **Configuration**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**   **FPS**
  ------------------- --------------- ------------ -------- -------------- ----------------- ---------
  **No tiling**                 0.673        0.348    0.459          0.300             0.177     9.260
  Tiling                        0.339        0.483    0.388          0.320             0.179     1.160

  : Tiling evaluation on the validation set. Prompt P4. Model: YOLOE-11
  M. {#tab:tiling_ye11m}

The NMS threshold is tuned to eliminate redundant bounding boxes.

  **NMS**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  --------- --------------- ------------ -------- -------------- -----------------
  0.2                 0.688        0.345    0.459          0.300             0.177
  0.3                 0.685        0.346    0.460          0.300             0.177
  0.4                 0.679        0.347    0.459          0.300             0.177
  0.5                 0.673        0.348    0.459          0.300             0.177
  0.6                 0.659        0.350    0.457          0.302             0.178

  : NMS threshold sweep on the validation set. Prompt P4, no tiling.
  Model: YOLOE-11 M. {#tab:nms_ye11m}

### YOLOE-11 Large

The large variant is assessed to determine whether increased capacity
addresses the most challenging camouflage scenarios in the tree canopy.

  **Prompt**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  ------------ --------------- ------------ -------- -------------- -----------------
  P1                     0.655        0.189    0.216          0.156             0.095
  P2                     0.607        0.292    0.389          0.220             0.127
  P3                     0.596        0.324    0.420          0.271             0.165
  P4                     0.701        0.289    0.394          0.238             0.145
  P5                     0.557        0.338    0.418          0.278             0.165
  P6                     0.510        0.193    0.276          0.118             0.070

  : Prompt ablation on the validation set. Model: YOLOE-11 L.
  {#tab:prompts_ye11l}

Inference speed is measured with and without image tiling.

  **Configuration**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**   **FPS**
  ------------------- --------------- ------------ -------- -------------- ----------------- ---------
  **No tiling**                 0.596        0.324    0.420          0.271             0.165     8.590
  Tiling                        0.250        0.530    0.312          0.328             0.183     0.910

  : Tiling evaluation on the validation set. Prompt P3. Model: YOLOE-11
  L. {#tab:tiling_ye11l}

The final NMS threshold is fine-tuned to refine prediction quality.

  **NMS**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  --------- --------------- ------------ -------- -------------- -----------------
  0.1                 0.617        0.317    0.418          0.268             0.163
  0.2                 0.615        0.321    0.422          0.269             0.165
  0.3                 0.610        0.322    0.421          0.269             0.165
  0.4                 0.605        0.323    0.421          0.269             0.165
  0.5                 0.596        0.324    0.420          0.271             0.165
  0.6                 0.584        0.325    0.418          0.270             0.166

  : NMS threshold sweep on the validation set. Prompt P3, no tiling.
  Model: YOLOE-11 L. {#tab:nms_ye11l}

## YOLOE-26

The most advanced and deepest branch of the YOLOE family is evaluated
across five size variants.

### YOLOE-26 Nano

The ultra-lightweight variant within this advanced family is assessed.

  **Prompt**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  ------------ --------------- ------------ -------- -------------- -----------------
  P1                     0.561        0.144    0.221          0.110             0.067
  P2                     0.674        0.113    0.187          0.090             0.058
  P3                     0.494        0.048    0.086          0.041             0.027
  P4                     0.605        0.148    0.225          0.094             0.055
  P5                     0.668        0.078    0.137          0.056             0.036
  P6                     0.454        0.108    0.169          0.059             0.036

  : Prompt ablation on the validation set. Model: YOLOE-26 N.
  {#tab:prompts_ye26n}

With prompt P4, the inference speed penalty of image tiling against
full-image processing is quantified.

  **Configuration**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**   **FPS**
  ------------------- --------------- ------------ -------- -------------- ----------------- ---------
  **No tiling**                 0.605        0.148    0.225          0.094             0.055    14.180
  Tiling                        0.262        0.267    0.180          0.103             0.059     2.280

  : Tiling evaluation on the validation set. Prompt P4. Model: YOLOE-26
  N. {#tab:tiling_ye26n}

The NMS threshold is swept to suppress duplicate detections.

  **NMS**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  --------- --------------- ------------ -------- -------------- -----------------
  0.1                 0.616        0.145    0.222          0.089             0.055
  0.2                 0.615        0.147    0.225          0.095             0.056
  0.3                 0.613        0.147    0.225          0.095             0.056
  0.4                 0.610        0.147    0.225          0.094             0.055
  0.5                 0.605        0.148    0.225          0.094             0.055
  0.6                 0.599        0.148    0.224          0.093             0.055

  : NMS threshold sweep on the validation set. Prompt P4, no tiling.
  Model: YOLOE-26 N. {#tab:nms_ye26n}

### YOLOE-26 Small

The small variant is evaluated seeking a strong balance between
detection accuracy and inference speed.

  **Prompt**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  ------------ --------------- ------------ -------- -------------- -----------------
  P1                     0.345        0.305    0.318          0.212             0.121
  P2                     0.604        0.312    0.407          0.249             0.146
  P3                     0.589        0.187    0.251          0.136             0.084
  P4                     0.329        0.259    0.158          0.109             0.057
  P5                     0.662        0.185    0.266          0.121             0.076
  P6                     0.260        0.366    0.283          0.149             0.079

  : Prompt ablation on the validation set. Model: YOLOE-26 S.
  {#tab:prompts_ye26s}

With prompt P2 selected, tiled versus full-image detection performance
is assessed.

  **Configuration**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**   **FPS**
  ------------------- --------------- ------------ -------- -------------- ----------------- ---------
  **No tiling**                 0.604        0.312    0.407          0.249             0.146    13.250
  Tiling                        0.306        0.437    0.341          0.225             0.127     1.990

  : Tiling evaluation on the validation set. Prompt P2. Model: YOLOE-26
  S. {#tab:tiling_ye26s}

The NMS threshold is tuned to suppress duplicate predictions.

  **NMS**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  --------- --------------- ------------ -------- -------------- -----------------
  0.3                 0.617        0.309    0.407          0.247             0.146
  0.4                 0.612        0.310    0.408          0.249             0.146
  0.5                 0.604        0.312    0.407          0.249             0.146
  0.6                 0.596        0.313    0.406          0.251             0.147

  : NMS threshold sweep on the validation set. Prompt P2, no tiling.
  Model: YOLOE-26 S. {#tab:nms_ye26s}

### YOLOE-26 Medium

The medium variant is evaluated to reduce false positives and improve
background discrimination.

  **Prompt**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  ------------ --------------- ------------ -------- -------------- -----------------
  P1                     0.392        0.300    0.335          0.214             0.126
  P2                     0.683        0.324    0.427          0.272             0.164
  P3                     0.720        0.315    0.423          0.271             0.167
  P4                     0.373        0.209    0.198          0.095             0.053
  P5                     0.763        0.293    0.421          0.250             0.154
  P6                     0.356        0.310    0.289          0.139             0.079

  : Prompt ablation on the validation set. Model: YOLOE-26 M.
  {#tab:prompts_ye26m}

With prompt P2, inference speed is measured with and without image
sub-windowing.

  **Configuration**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**   **FPS**
  ------------------- --------------- ------------ -------- -------------- ----------------- ---------
  **No tiling**                 0.683        0.324    0.427          0.272             0.164    11.680
  Tiling                        0.360        0.466    0.404          0.310             0.175     1.310

  : Tiling evaluation on the validation set. Prompt P2. Model: YOLOE-26
  M. {#tab:tiling_ye26m}

The NMS threshold is fine-tuned to suppress redundant predictions.

  **NMS**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  --------- --------------- ------------ -------- -------------- -----------------
  0.1                 0.709        0.316    0.425          0.266             0.161
  0.2                 0.705        0.319    0.428          0.270             0.163
  0.3                 0.700        0.320    0.428          0.270             0.163
  0.4                 0.691        0.321    0.427          0.272             0.163
  0.5                 0.683        0.324    0.427          0.272             0.164
  0.6                 0.673        0.326    0.426          0.271             0.164

  : NMS threshold sweep on the validation set. Prompt P2, no tiling.
  Model: YOLOE-26 M. {#tab:nms_ye26m}

### YOLOE-26 Large

The large variant is evaluated to achieve more stable bounding box
predictions.

  **Prompt**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  ------------ --------------- ------------ -------- -------------- -----------------
  P1                     0.362        0.297    0.276          0.214             0.131
  P2                     0.591        0.332    0.402          0.251             0.157
  P3                     0.548        0.352    0.407          0.260             0.160
  P4                     0.651        0.182    0.279          0.129             0.088
  P5                     0.726        0.191    0.295          0.138             0.090
  P6                     0.401        0.284    0.302          0.159             0.100

  : Prompt ablation on the validation set. Model: YOLOE-26 L.
  {#tab:prompts_ye26l}

With prompt P3, the inference speed penalty of image tiling is measured.

  **Configuration**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**   **FPS**
  ------------------- --------------- ------------ -------- -------------- ----------------- ---------
  **No tiling**                 0.548        0.352    0.407          0.260             0.160    10.990
  Tiling                        0.283        0.458    0.349          0.202             0.113     1.150

  : Tiling evaluation on the validation set. Prompt P3. Model: YOLOE-26
  L. {#tab:tiling_ye26l}

A precise NMS sweep is performed to suppress spatially redundant
predictions.

  **NMS**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  --------- --------------- ------------ -------- -------------- -----------------
  0.2                 0.560        0.346    0.408          0.259             0.160
  0.3                 0.557        0.348    0.409          0.261             0.160
  0.4                 0.554        0.350    0.408          0.261             0.160
  0.5                 0.548        0.352    0.407          0.260             0.160
  0.6                 0.541        0.353    0.406          0.261             0.160

  : NMS threshold sweep on the validation set. Prompt P3, no tiling.
  Model: YOLOE-26 L. {#tab:nms_ye26l}

### YOLOE-26 Extra-Large

The largest model in the entire YOLOE family is evaluated to assess
whether maximum representational capacity resolves detection failures in
the most complex canopy regions.

  **Prompt**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  ------------ --------------- ------------ -------- -------------- -----------------
  P1                     0.426        0.357    0.293          0.267             0.162
  P2                     0.454        0.391    0.393          0.274             0.169
  P3                     0.614        0.306    0.380          0.219             0.140
  P4                     0.717        0.219    0.326          0.170             0.112
  P5                     0.742        0.162    0.260          0.124             0.084
  P6                     0.429        0.265    0.327          0.145             0.090

  : Prompt ablation on the validation set. Model: YOLOE-26 X.
  {#tab:prompts_ye26x}

With prompt P2, the cost-benefit trade-off of image tiling versus
full-image processing is evaluated.

  **Configuration**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**   **FPS**
  ------------------- --------------- ------------ -------- -------------- ----------------- ---------
  **No tiling**                 0.454        0.391    0.393          0.274             0.169     8.330
  Tiling                        0.256        0.500    0.338          0.268             0.155     0.710

  : Tiling evaluation on the validation set. Prompt P2. Model: YOLOE-26
  X. {#tab:tiling_ye26x}

The NMS threshold is tuned to suppress redundant detections from this
large-scale model.

  **NMS**     **Precision**   **Recall**   **F1**   **mAP@0.50**   **mAP@0.50:95**
  --------- --------------- ------------ -------- -------------- -----------------
  0.1                 0.467        0.375    0.390          0.267             0.165
  0.2                 0.465        0.382    0.394          0.271             0.167
  0.3                 0.463        0.385    0.394          0.273             0.169
  0.4                 0.460        0.388    0.394          0.273             0.169
  0.5                 0.454        0.391    0.393          0.274             0.169
  0.6                 0.447        0.392    0.389          0.273             0.170

  : NMS threshold sweep on the validation set. Prompt P2, no tiling.
  Model: YOLOE-26 X. {#tab:nms_ye26x}

# Contribution to the Sustainable Development Goals {#contribution-to-the-sustainable-development-goals .unnumbered}

  ---------------------------------------------------- ---------- ------------ --------- --------------------
  **Sustainable Development Goals**                     **High**   **Medium**   **Low**   **Not applicable**
  SDG 1. **No Poverty**                                                                           X
  SDG 2. **Zero Hunger**                                                           X     
  SDG 3. **Good Health and Well-being**                                                           X
  SDG 4. **Quality Education**                                                                    X
  SDG 5. **Gender Equality**                                                                      X
  SDG 6. **Clean Water and Sanitation**                                                           X
  SDG 7. **Affordable and Clean Energy**                                                          X
  SDG 8. **Decent Work and Economic Growth**                                       X     
  SDG 9. **Industry, Innovation and Infrastructure**       X                             
  SDG 10. **Reduced Inequalities**                                                                X
  SDG 11. **Sustainable Cities and Communities**                                                  X
  SDG 12. **Responsible Consumption and Production**                   X                 
  SDG 13. **Climate Action**                                                                      X
  SDG 14. **Life Below Water**                                                                    X
  SDG 15. **Life on Land**                                                                        X
  SDG 16. **Peace, Justice and Strong Institutions**                                              X
  SDG 17. **Partnerships for the Goals**                                                          X
  ---------------------------------------------------- ---------- ------------ --------- --------------------

The present Final Degree Project is directly related to several
Sustainable Development Goals (SDGs), according to the levels of linkage
established in the previous table:

### High-Level Linkage {#high-level-linkage .unnumbered}

**SDG 9: Industry, innovation and infrastructure**: This goal lies at
the core of the research and has the strongest connection with the
project. The work develops a critical and empirical analysis of the
limitations of the most innovative artificial intelligence technologies
within the field of computer vision. Specifically, it evaluates and
compares the performance of closed-vocabulary traditional models
(YOLO11) against modern open-vocabulary architectures such as
YOLO-World, YOLOE, and Grounding DINO operating in a real field
environment. This comparison opens new avenues for technological
innovation and digital infrastructures for precision agriculture.

### Medium-Level Linkage {#medium-level-linkage .unnumbered}

**SDG 12: Responsible consumption and production**: This goal is
moderately related to the development of the project. The competitive
advantage of general-purpose open-vocabulary models (OVOD) lies in their
zero-shot generalization capability, which allows them to detect new
agricultural elements or crop varieties (such as an extension to lemons)
through simple text instructions (prompts). By removing the need for
continuous data collection cycles, massive manual labeling, and costly
network retraining on high-performance servers, a drastic reduction in
computational energy consumption is achieved. This promotes a much more
sustainable, responsible, and efficient use of technological resources
applied to the field.

### Low-Level Linkage {#low-level-linkage .unnumbered}

**SDG 2: Zero hunger**: This goal is linked at a low level because the
primary focus of the thesis belongs to the field of algorithm design and
AI software evaluation. However, it contributes indirectly by addressing
a real problem in precision agriculture using computer vision models
focused on automating fruit counting and phenological classification
(ripe and unripe oranges). These tools facilitate accurate real-time
harvest estimation, indirectly optimizing labor planning and the
efficient management of food resources in the field.

**SDG 8: Decent work and economic growth**: This goal has a low level of
linkage with the project. By automating repetitive and highly
error-prone tasks (such as dense manual fruit counting in complex
environments for estimating tree harvests), the use of these automated
detectors promotes the modernization of rural employment. This
transition transforms traditional work into a higher value-added
technical role focused on technological management, indirectly
increasing productivity and the economic sustainability of citrus farms.
