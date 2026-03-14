# ich-ct-segmentation
Medical image segmentation project for intracranial haemorrhage analysis on CT.
# Automated Intracranial Haemorrhage Segmentation on Non-Contrast CT Images

## Overview
This repository presents a portfolio version of my undergraduate dissertation project on automated intracranial haemorrhage (ICH) segmentation from non-contrast CT images.

The project explored a deep learning-based workflow for lesion segmentation, using a baseline 3D U-Net and improved workflow refinements designed to address small-lesion segmentation challenges. The original work focused on medical image preprocessing, segmentation evaluation and quantitative comparison of workflow performance.

## Project Background
Intracranial haemorrhage is a clinically important emergency finding on CT imaging. Automated segmentation can support quantitative analysis and potentially improve workflow efficiency in image interpretation and downstream assessment.

A major difficulty in ICH segmentation is the accurate delineation of small lesions, especially when labelled data are limited and image boundaries are unclear. This project investigated whether preprocessing and workflow refinement could improve segmentation quality compared with a baseline model.

## Objectives
- Build a baseline segmentation workflow for ICH on non-contrast CT
- Improve performance on small haemorrhage lesions
- Compare baseline and refined workflows using quantitative metrics
- Present a reproducible and well-documented portfolio version of the project

## Methods
### Imaging task
- Modality: Non-contrast CT
- Task: Intracranial haemorrhage segmentation

### Workflow components
- Baseline model: 3D U-Net
- Improved workflow: preprocessing and segmentation refinement
- Evaluation metrics: Dice Similarity Coefficient, Hausdorff Distance, Intersection over Union

### Preprocessing strategy
- Intensity normalisation
- Data augmentation
- Resampling
- Forced cropping / patch handling

## Key Results
The original dissertation compared a baseline 3D U-Net with improved segmentation workflows.

| Model | DSC | HD | IoU |
|------|------|------|------|
| Baseline 3D U-Net | 0.6047 | 49.9967 | 0.5052 |
| 3D Improved U-Net | 0.6667 | 41.6946 | 0.5686 |
| 2D Improved U-Net | 0.6804 | 29.3923 | 0.5865 |

These results indicated that workflow refinement improved segmentation quality, particularly for small lesions.

## Repository Structure
- `notebooks/01_preprocessing_demo.ipynb` – demonstration of image preprocessing logic
- `notebooks/02_metrics_evaluation_demo.ipynb` – explanation of Dice, IoU and HD evaluation
- `notebooks/03_results_visualisation.ipynb` – visual summary of project outputs
- `src/` – helper scripts for preprocessing, metrics and visualisation
- `results/` – sample metrics tables
- `images/` – workflow diagrams and representative figures
- `docs/` – supplementary notes

## Skills Demonstrated
- Medical image preprocessing
- Deep learning workflow interpretation
- Quantitative image analysis
- Model evaluation using segmentation metrics
- Reproducible project documentation
- Python-based analytical workflow design

## Limitations
The original clinical imaging dataset is not included in this repository due to privacy and access restrictions. This repository is designed to present the project structure, methods, evaluation approach and representative outputs rather than reproduce the full training pipeline.

## Future Improvements
- Add a lightweight public demo using synthetic or open sample data
- Expand lesion-size-specific error analysis
- Add a more complete PyTorch training skeleton
- Explore explainability and robustness analysis

## Disclaimer
This repository is intended for educational and portfolio purposes only. It is not a validated clinical tool.
