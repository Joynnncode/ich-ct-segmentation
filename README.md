# Automated Intracranial Haemorrhage Segmentation on Non-Contrast CT Images

## Overview
This repository presents a portfolio version of my undergraduate dissertation project on automated intracranial haemorrhage (ICH) segmentation from non-contrast CT (NCCT) images.

The project explored a deep learning workflow for lesion segmentation using a baseline 3D U-Net and improved U-Net-based refinements designed to address one of the main bottlenecks in ICH image analysis: accurate segmentation of small haemorrhage lesions.

This repository is intended to present the workflow design, preprocessing logic, evaluation approach and representative outputs in a clear, reproducible, portfolio-friendly format.

## Project Background
Intracranial haemorrhage is a life-threatening emergency condition associated with high morbidity and mortality. Non-contrast CT is commonly used for diagnosis, but manual delineation of haemorrhage regions can be difficult and time-sensitive.

A major challenge in this task is the segmentation of small lesions, particularly when labelled medical imaging data are limited. This project investigated whether preprocessing refinement and workflow optimisation could improve segmentation quality compared with a baseline 3D U-Net model.

## Objectives
- Build a baseline deep learning workflow for ICH segmentation on NCCT images
- Improve segmentation performance for small haemorrhage lesions
- Compare baseline and improved U-Net workflows using quantitative metrics
- Present a structured and reproducible portfolio version of the project

## Dataset
The original project used 200 annotated 3D non-contrast CT volumes from an intracranial haemorrhage segmentation challenge dataset. The labelled dataset was organised into:
- 100 training cases
- 70 closed testing cases
- 30 open validation cases

The image volumes were stored in `.nii.gz` format. Example CT volume dimensions were approximately `512 × 512 × 29`.

The original clinical dataset is not included in this repository because of data access and privacy restrictions.

## Initial Data Review
Before model development, the CT volumes and segmentation masks were reviewed to understand:
- haemorrhage appearance and lesion distribution
- intensity characteristics of NCCT images
- structural differences between images and masks
- general constraints of working with anisotropic 3D volumes

This early dataset inspection informed preprocessing design and later workflow refinement.

## Methods

### Baseline Model
The baseline workflow used a 3D U-Net for volumetric ICH segmentation.

### Improved Workflow
The improved workflow was designed to address limitations of the baseline model, especially poor performance on small haemorrhage lesions.

### Preprocessing and Workflow Refinement
Key preprocessing and workflow refinements included:
- intensity normalisation using CT windowing
- data augmentation
- resampling to improve consistency across different voxel sizes
- forced cropping / chunk-based handling to reduce memory limitations
- workflow adaptation for both 3D and 2D improved U-Net experiments

### Evaluation Metrics
Segmentation performance was assessed using:
- Dice Similarity Coefficient (DSC)
- Hausdorff Distance (HD)
- Intersection over Union (IoU)

## Key Results
The original dissertation compared a baseline 3D U-Net with improved workflows.

| Model | DSC | HD | IoU |
|------|------|------|------|
| Baseline 3D U-Net | 0.6047 | 49.9967 | 0.5052 |
| 3D Improved U-Net | 0.6667 | 41.6946 | 0.5686 |
| 2D Improved U-Net | 0.6804 | 29.3923 | 0.5865 |

The improved workflow increased mean Dice from 0.60 to 0.66 compared with the baseline 3D U-Net, demonstrating that preprocessing and workflow refinement improved segmentation quality. The project particularly focused on improving segmentation of small haemorrhage lesions.

## Repository Structure
- `notebooks/01_preprocessing_demo.ipynb` – demonstration of preprocessing logic
- `notebooks/02_metrics_evaluation_demo.ipynb` – explanation of Dice, IoU and evaluation metrics
- `notebooks/03_results_visualisation.ipynb` – project result visualisation
- `src/preprocess.py` – preprocessing helper functions
- `src/metrics.py` – segmentation metric functions
- `src/visualisation.py` – plotting and image display helpers
- `results/` – sample metrics tables
- `images/` – workflow diagrams and representative figures
- `docs/project_notes.md` – dataset and workflow notes
- `docs/workflow_timeline.md` – summary of project progression

## Skills Demonstrated
- Medical image preprocessing
- NCCT volume handling
- Deep learning workflow interpretation
- Quantitative segmentation evaluation
- Python-based analytical workflow design
- Reproducible project documentation

## Limitations
- The original clinical dataset is not included
- This repository presents a portfolio version of the workflow rather than the full original training environment
- The project is intended for educational and portfolio purposes only and is not a validated clinical tool

## Future Improvements
- Add a lightweight public demo using synthetic or open sample data
- Expand lesion-size-specific error analysis
- Add a fuller PyTorch training skeleton
- Explore robustness and generalisability across broader datasets

## Disclaimer
This repository is intended for educational and portfolio purposes only. It does not constitute a clinically validated tool.
