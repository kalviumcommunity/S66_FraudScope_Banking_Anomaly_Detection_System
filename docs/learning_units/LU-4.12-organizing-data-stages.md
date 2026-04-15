# Learning Unit 4.12: Organizing Raw Data, Processed Data, and Output Artifacts

## Objective

Separate raw data, transformed datasets, and generated outputs using clear storage rules.

## Product-Oriented Implementation

1. Define artifact placement policy for `data/raw`, `data/processed`, and `outputs`.
2. Add helper utility to classify files into the correct stage.
3. Add notebook examples to prevent data leakage and accidental overwrites.

## Deliverables in this unit

- `src/fraudscope/data_stage_policy.py`
- `notebooks/LU-4.12-data-stage-organization.ipynb`
- LU implementation note and README update

## Why this matters for fraud detection

Clear data stages preserve lineage, improve reproducibility, and reduce mistakes when generating anomaly reports from changing transaction feeds.
