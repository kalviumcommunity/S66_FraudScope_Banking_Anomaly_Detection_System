from __future__ import annotations


def build_markdown_template() -> str:
    return """# FraudScope Analysis Section

## Objective
- Describe the analysis goal

## Checks Performed
1. Data quality validation
2. Suspicious amount threshold review
3. Account activity pattern check

## Command Reference
```python
high_risk = transactions[transactions[\"risk_score\"] > 0.8]
```
"""


def print_markdown_template() -> None:
    print(build_markdown_template())


if __name__ == "__main__":
    print_markdown_template()
