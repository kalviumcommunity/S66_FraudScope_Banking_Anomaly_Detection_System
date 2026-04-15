from __future__ import annotations


def risk_band(amount: float) -> str:
    if amount >= 10000:
        return "high"
    if amount >= 5000:
        return "medium"
    return "low"


def summarize_risk(amounts: list[float]) -> dict[str, int]:
    summary = {"low": 0, "medium": 0, "high": 0}
    for amount in amounts:
        summary[risk_band(amount)] += 1
    return summary


def print_conditional_demo() -> None:
    sample_amounts = [450.0, 2200.0, 7600.0, 15400.0]
    print("Sample amounts:", sample_amounts)
    print("Risk summary:", summarize_risk(sample_amounts))


if __name__ == "__main__":
    print_conditional_demo()
