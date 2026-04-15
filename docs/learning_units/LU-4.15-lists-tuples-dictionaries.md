# Learning Unit 4.15: Working with Python Lists, Tuples, and Dictionaries

## Objective

Use Python collections to represent transactions, immutable identifiers, and account-level aggregates.

## Product-Oriented Implementation

1. Use lists to store batches of transaction records.
2. Use tuples for immutable record keys (transaction_id, account_id).
3. Use dictionaries for fast account-wise summaries required in fraud checks.

## Deliverables in this unit

- `src/fraudscope/data_structures.py`
- `notebooks/LU-4.15-data-structures.ipynb`
- LU implementation note and README update

## Why this matters for fraud detection

Most fraud rules begin with grouped transaction context. Lists, tuples, and dictionaries provide that context before moving to NumPy and Pandas scaling.
