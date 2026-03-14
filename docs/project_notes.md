# Project Notes

## Project Summary
This project focused on automated intracranial haemorrhage (ICH) segmentation from non-contrast CT images using deep learning.

The main aim was to improve segmentation performance for haemorrhage lesions, especially small lesions that were difficult to segment accurately with a baseline model.

## Dataset Summary
- 200 annotated 3D NCCT volumes
- File format: `.nii.gz`
- Split:
  - 100 training cases
  - 70 closed testing cases
  - 30 open validation cases
- Example image size: approximately `512 × 512 × 29`

## Core Workflow
1. Review image and mask structure
2. Build a baseline 3D U-Net workflow
3. Identify limitations in small-lesion segmentation
4. Apply preprocessing refinements
5. Evaluate improved workflows using quantitative segmentation metrics

## Preprocessing Logic
The project used several preprocessing strategies to improve segmentation quality:
- intensity normalisation
- data augmentation
- resampling
- chunk-based / forced cropping style handling for memory efficiency

These steps were designed to improve consistency across images and help the model better handle variation in lesion shape and size.

## Evaluation Metrics
The original experiments used:
- Dice Similarity Coefficient (DSC)
- Hausdorff Distance (HD)
- Intersection over Union (IoU)

These metrics were used to compare the baseline and improved workflows.

## Main Technical Challenge
The most important challenge was accurate segmentation of small haemorrhage lesions.

Small lesions were difficult because:
- they occupied fewer pixels/voxels
- boundaries could be unclear
- labelled data were limited
- anisotropic volume structure complicated 3D analysis

## Final Outcome
Compared with the baseline 3D U-Net, the improved workflow increased mean Dice from 0.6047 to 0.6667.

This suggested that preprocessing and workflow refinement improved segmentation quality and could support more robust quantitative image analysis.

## Skills Demonstrated
- Medical image analysis
- CT preprocessing
- Deep learning segmentation workflow design
- Quantitative evaluation of model performance
- Technical communication and project documentation
