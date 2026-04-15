from __future__ import annotations


def evaluate_transaction_risk(transaction_amount: float, hourly_transaction_count: int) -> dict[str, object]:
    normalized_amount = min(transaction_amount / 10000.0, 1.0)
    normalized_velocity = min(hourly_transaction_count / 10.0, 1.0)
    risk_score = round((normalized_amount * 0.7) + (normalized_velocity * 0.3), 2)

    # This threshold is used as a simple explainable baseline flag.
    is_high_risk = risk_score >= 0.75

    return {
        "risk_score": risk_score,
        "is_high_risk": is_high_risk,
    }


def print_pep8_demo() -> None:
    result = evaluate_transaction_risk(transaction_amount=6400.0, hourly_transaction_count=5)
    print(result)


if __name__ == "__main__":
    print_pep8_demo()
