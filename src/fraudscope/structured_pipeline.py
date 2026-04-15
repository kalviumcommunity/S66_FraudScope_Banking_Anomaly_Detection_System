from __future__ import annotations


def load_sample_transactions() -> list[dict[str, float]]:
    return [
        {"amount": 1200.0, "hourly_count": 2.0},
        {"amount": 7800.0, "hourly_count": 6.0},
        {"amount": 15200.0, "hourly_count": 9.0},
    ]


def compute_score(amount: float, hourly_count: float) -> float:
    amount_component = min(amount / 10000.0, 1.0)
    velocity_component = min(hourly_count / 10.0, 1.0)
    return round((amount_component * 0.7) + (velocity_component * 0.3), 2)


def score_transactions(records: list[dict[str, float]]) -> list[dict[str, float]]:
    scored_records: list[dict[str, float]] = []
    for record in records:
        score = compute_score(record["amount"], record["hourly_count"])
        scored_records.append({**record, "risk_score": score})
    return scored_records


def summarize_scores(records: list[dict[str, float]]) -> dict[str, float]:
    scores = [record["risk_score"] for record in records]
    return {
        "count": float(len(scores)),
        "average_score": round(sum(scores) / len(scores), 2) if scores else 0.0,
        "max_score": max(scores) if scores else 0.0,
    }


def run_pipeline() -> dict[str, float]:
    records = load_sample_transactions()
    scored = score_transactions(records)
    return summarize_scores(scored)


if __name__ == "__main__":
    print(run_pipeline())
