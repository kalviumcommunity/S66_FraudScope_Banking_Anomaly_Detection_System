# FraudScope Banking Anomaly Detection System

FraudScope is a data science project focused on finding suspicious banking transactions early using a clean analytics pipeline, anomaly rules, and explainable visual outputs.

## Learning Unit Progression

This repository is executed through Learning Units (LU). Each LU adds a practical piece of the final product.

- LU 4.5 establishes local environment readiness and repository navigation.
- LU 4.6 adds automated verification for Python, Conda, and Jupyter tooling.
- LU 4.7 introduces Jupyter launch flow and home interface navigation.
- LU 4.8 differentiates code cells and markdown cells for clean notebook storytelling.
- LU 4.9 covers notebook kernel lifecycle controls for safe execution.
- LU 4.10 standardizes markdown headings, lists, and code blocks in notebooks.
- LU 4.11 formalizes project folder structure conventions for DS delivery.
- LU 4.12 organizes raw, processed, and output artifact boundaries.
- LU 4.13 adds the first runnable Python transaction analysis script.
- LU 4.14 introduces numeric and string data types for transaction fields.
- LU 4.15 applies lists, tuples, and dictionaries for transaction modeling.
- LU 4.16 introduces conditional logic for fraud screening decisions.
- LU 4.17 applies for/while loops for iterative transaction processing.
- LU 4.18 defines reusable Python functions for fraud analysis tasks.
- LU 4.19 formalizes function inputs and return values for scoring workflows.
- LU 4.20 applies PEP8 naming and meaningful comments for readability.
- LU 4.21 structures Python modules for readability and reuse.
- LU 4.22 introduces NumPy arrays created from Python lists.
- LU 4.23 explores array shape, dimensions, and index positions.
- LU 4.24 performs basic mathematical operations on NumPy arrays.
- LU 4.25 replaces Python loops with vectorized NumPy operations for efficiency.
- LU 4.26 demonstrates NumPy broadcasting with simple array examples.
- LU 4.27 creates Pandas Series from transaction amount lists and arrays.
- LU 4.28 creates Pandas DataFrames from dictionaries and transaction files.
- LU 4.29 loads CSV transaction data into Pandas DataFrames.
- LU 4.30 inspects DataFrames using head(), info(), and describe().
 - Later units build data pipelines, cleaning, EDA, anomaly logic, and insights reporting.

## Project Structure

- `data/raw/` source transaction files
- `data/processed/` cleaned and transformed datasets
- `notebooks/` Jupyter notebooks for exploration and model walkthroughs
- `outputs/figures/` plots and visual artifacts
- `outputs/reports/` anomaly reports and summaries
- `src/fraudscope/` reusable project code
- `docs/learning_units/` implementation notes for each Learning Unit

## LU 4.5 Outcome

- Project folders initialized for DS workflow.
- Repository interpretation guide added.
- Base Python package scaffold created for upcoming units.

## LU 4.6 Outcome

- Added environment verification module for Python, Conda, and Jupyter commands.
- Added a Jupyter notebook demonstrating setup checks and Python syntax basics.
- Added implementation note for LU 4.6 with product continuity focus.

## LU 4.7 Outcome

- Added notebook walkthrough for launching Jupyter and reading the home interface.
- Added helper script to print startup commands and interface sections.
- Added implementation note for LU 4.7 linked to product workflow readiness.

## LU 4.8 Outcome

- Added notebook examples showing code cells versus markdown cells.
- Added helper utility that prints recommended cell usage in DS notebooks.
- Added implementation note for LU 4.8 aligned to explainable fraud analysis.

## LU 4.9 Outcome

- Added kernel lifecycle helper for run, restart, and interrupt guidance.
- Added notebook with practical examples for managing long-running executions.
- Added implementation note for LU 4.9 linked to stable analysis operations.

## LU 4.10 Outcome

- Added markdown template helper for notebook documentation sections.
- Added notebook demonstrating headings, lists, and fenced code blocks.
- Added implementation note for LU 4.10 supporting consistent project communication.

## LU 4.11 Outcome

- Added folder structure blueprint and automated structure checker.
- Added notebook walkthrough for expected DS project directories.
- Added implementation note for LU 4.11 to keep repository scalable.

## LU 4.12 Outcome

- Added data stage policy helper to enforce raw/processed/output separation.
- Added notebook showing correct artifact placement for pipeline steps.
- Added implementation note for LU 4.12 focused on data lineage clarity.

## LU 4.13 Outcome

- Added sample raw transaction CSV for script-based analysis practice.
- Added first Python analysis script to compute basic transaction stats.
- Added implementation note for LU 4.13 linked to anomaly detection preparation.

## LU 4.14 Outcome

- Added type demonstration module for numeric and string transaction fields.
- Added notebook examples for type conversion and validation.
- Added implementation note for LU 4.14 to prepare for robust feature engineering.

## LU 4.15 Outcome

- Added data structure utility for transaction records using lists, tuples, and dictionaries.
- Added notebook examples that model records and account-level summaries.
- Added implementation note for LU 4.15 to support reusable fraud logic building blocks.

## LU 4.16 Outcome

- Added conditional screening helper for low/medium/high risk labeling.
- Added notebook examples applying if/elif/else rules on transaction amounts.
- Added implementation note for LU 4.16 to support explainable rule-based flags.

## LU 4.17 Outcome

- Added iterative processing helper using for and while loops.
- Added notebook examples for batch traversal and threshold counting.
- Added implementation note for LU 4.17 to support repeated anomaly checks.

## LU 4.18 Outcome

- Added reusable function set for transaction scoring and reason tagging.
- Added notebook examples showing function definition and invocation.
- Added implementation note for LU 4.18 to prepare modular fraud pipeline design.

## LU 4.19 Outcome

- Added typed function interfaces with input validation and structured returns.
- Added notebook examples passing transaction payloads and reading returned metrics.
- Added implementation note for LU 4.19 to strengthen reusable scoring contracts.

## LU 4.20 Outcome

- Added style-focused helper showcasing PEP8 variable naming patterns.
- Added notebook examples for readable naming and concise comment usage.
- Added implementation note for LU 4.20 to improve maintainability.

## LU 4.21 Outcome

- Added modular analysis pipeline helper separating load, score, and summarize steps.
- Added notebook demonstrating clean module composition for reuse.
- Added implementation note for LU 4.21 to support maintainable project growth.

## LU 4.22 Outcome

- Added NumPy conversion helper to create arrays from transaction amount lists.
- Added notebook demonstrating list-to-array conversion and dtype inspection.
- Added implementation note for LU 4.22 to prepare efficient numeric workflows.

## LU 4.23 Outcome

- Added NumPy helper to inspect array shape, dimensions, and key index access.
- Added notebook examples for 1D and 2D array indexing patterns.
- Added implementation note for LU 4.23 to prepare safe numerical slicing workflows.

## LU 4.24 Outcome

- Added NumPy math helper covering add, subtract, multiply, and divide operations.
- Added notebook showing element-wise math on transaction amount arrays.
- Added implementation note for LU 4.24 to support numerical feature transformations.

## LU 4.25 Outcome

- Added vectorization helper to replace loop-based scoring with array operations.
- Added notebook demonstrating fast element-wise threshold checking.
- Added implementation note for LU 4.25 to support efficient anomaly detection scaling.

## LU 4.26 Outcome

- Added broadcasting helper to perform cross-array operations without explicit loops.
- Added notebook demonstrating scalar-array and array-array broadcasting patterns.
- Added implementation note for LU 4.26 to enable efficient multi-array transformations.

## LU 4.27 Outcome

- Added Pandas helper to create Series from lists and arrays.
- Added notebook demonstrating Series creation and basic operations.
- Added implementation note for LU 4.27 to prepare for DataFrame-based workflows.
