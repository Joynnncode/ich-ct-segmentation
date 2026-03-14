# Workflow Timeline

## Phase 1 — Problem Definition
The project began with the clinical and technical problem of automated intracranial haemorrhage segmentation on non-contrast CT images.

A key challenge identified early was poor segmentation performance on small haemorrhage lesions.

## Phase 2 — Dataset Familiarisation
The next step focused on understanding the dataset:
- image volumes and masks
- NCCT image appearance
- lesion distribution
- file structure and data organisation

This stage informed the design of preprocessing and model experimentation.

## Phase 3 — Baseline Modelling
A baseline 3D U-Net workflow was established for volumetric segmentation.

This provided a reference point for:
- segmentation quality
- overlap metrics
- comparison with later refinements

## Phase 4 — Identification of Bottlenecks
The baseline workflow highlighted several limitations:
- weaker performance on small lesions
- sensitivity to image variation
- resource constraints when handling volumetric data

These issues motivated workflow refinement.

## Phase 5 — Preprocessing Refinement
The project then introduced several preprocessing and workflow changes:
- intensity normalisation
- data augmentation
- resampling
- chunking / forced cropping style handling

These were intended to improve consistency and help the model focus on clinically relevant structures.

## Phase 6 — Improved Workflow Evaluation
Improved workflows were evaluated against the baseline using:
- Dice Similarity Coefficient
- Hausdorff Distance
- Intersection over Union

Both improved 3D and improved 2D workflows were compared.

## Phase 7 — Final Results
The final workflow improved mean Dice from 0.6047 to 0.6667 relative to the baseline 3D U-Net.

The results supported the conclusion that preprocessing and workflow refinement improved segmentation quality, particularly for small haemorrhage lesions.

## Phase 8 — Portfolio Translation
For portfolio purposes, the original dissertation work was reorganised into:
- a simplified README
- reproducible notebooks
- lightweight Python helper modules
- project notes and workflow documentation

This repository therefore presents the project in a format suitable for technical communication and job applications.
