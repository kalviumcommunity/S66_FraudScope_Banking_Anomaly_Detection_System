from __future__ import annotations


def compute_risk_score(amount: float, transaction_count_last_hour: int) -> float:
    amount_component = min(amount / 10000.0, 1.0)
    velocity_component = min(transaction_count_last_hour / 10.0, 1.0)
    return round((amount_component * 0.7) + (velocity_component * 0.3), 2)


def label_reason(score: float) -> str:
    if score >= 0.8:
        return "high amount and/or unusual velocity"
    if score >= 0.5:
        return "moderate anomaly signals"
    return "normal transaction pattern"


def score_transaction(amount: float, transaction_count_last_hour: int) -> dict[str, object]:
    score = compute_risk_score(amount, transaction_count_last_hour)
    return {
        "risk_score": score,
        "reason": label_reason(score),
    }


def print_function_demo() -> None:
    result = score_transaction(amount=8200.0, transaction_count_last_hour=6)
    print(result)


if __name__ == "__main__":
    print_function_demo()
