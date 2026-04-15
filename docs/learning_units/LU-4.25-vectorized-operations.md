# Learning Unit 4.25: Applying Vectorized Operations Instead of Python Loops

## Objective

Replace explicit Python loops with vectorized NumPy operations for faster and more efficient anomaly calculations.

## Product-Oriented Implementation

1. Implement element-wise threshold checks using array broadcasting instead of loops.
2. Demonstrate performance advantage of vectorization over iteration.
3. Add notebook examples using transaction amount arrays.

## Deliverables in this unit

- `src/fraudscope/numpy_vectorized.py`
- `notebooks/LU-4.25-vectorized-operations.ipynb`
- LU implementation note and README update

## Why this matters for fraud detection

Vectorized operations are significantly faster for large transaction volumes, which is essential for real-time anomaly scoring.