# Learning Unit 4.9: Running, Restarting, and Interrupting Jupyter Kernels

## Objective

Understand kernel lifecycle operations and use them safely during transaction analysis workflows.

## Product-Oriented Implementation

1. Document when to run cells, restart kernel, and interrupt execution.
2. Provide a practical notebook that demonstrates execution management patterns.
3. Reduce notebook instability during heavy anomaly exploration.

## Deliverables in this unit

- `src/fraudscope/kernel_lifecycle_guide.py`
- `notebooks/LU-4.9-kernel-controls.ipynb`
- LU implementation note and README update

## Why this matters for fraud detection

Anomaly experiments can involve long calculations. Proper kernel control prevents stale state, blocked sessions, and incorrect conclusions.
