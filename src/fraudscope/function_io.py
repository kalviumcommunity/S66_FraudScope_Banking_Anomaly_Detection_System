from __future__ import annotations


def score_from_payload(payload: dict[str, object]) -> dict[str, object]:
    amount = float(payload.get("amount", 0.0))
    hourly_count = int(payload.get("transaction_count_last_hour", 0))

    amount_score = min(amount / 10000.0, 1.0)
    velocity_score = min(hourly_count / 10.0, 1.0)
    risk_score = round((amount_score * 0.7) + (velocity_score * 0.3), 2)

    return {
        "account_id": str(payload.get("account_id", "unknown")),
        "risk_score": risk_score,
        "is_flagged": risk_score >= 0.75,
    }


def print_function_io_demo() -> None:
    payload = {
        "account_id": "A02",
        "amount": 9100,
        "transaction_count_last_hour": 7,
    }
    print(score_from_payload(payload))


if __name__ == "__main__":
    print_function_io_demo()
