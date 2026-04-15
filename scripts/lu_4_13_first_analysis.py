from __future__ import annotations

import csv
from pathlib import Path


RAW_FILE = Path("data/raw/sample_transactions.csv")
OUTPUT_FILE = Path("outputs/reports/lu_4_13_summary.txt")


def load_amounts(file_path: Path) -> list[float]:
    with file_path.open("r", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    return [float(row["amount"]) for row in rows]


def build_summary(amounts: list[float]) -> str:
    total_count = len(amounts)
    total_value = sum(amounts)
    average_value = total_value / total_count if total_count else 0.0
    high_value_count = len([amount for amount in amounts if amount > 5000])

    return (
        f"Transaction count: {total_count}\n"
        f"Total amount: {total_value:.2f}\n"
        f"Average amount: {average_value:.2f}\n"
        f"High-value transactions (>5000): {high_value_count}\n"
    )


def main() -> None:
    amounts = load_amounts(RAW_FILE)
    summary = build_summary(amounts)
    OUTPUT_FILE.write_text(summary, encoding="utf-8")
    print(summary)
    print(f"Saved summary to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
