from __future__ import annotations


def build_transaction_batch() -> list[dict[str, object]]:
    return [
        {"transaction_id": "T1001", "account_id": "A01", "amount": 1200.0},
        {"transaction_id": "T1002", "account_id": "A02", "amount": 7800.0},
        {"transaction_id": "T1003", "account_id": "A01", "amount": 450.0},
    ]


def build_record_keys(records: list[dict[str, object]]) -> list[tuple[str, str]]:
    keys: list[tuple[str, str]] = []
    for record in records:
        keys.append((str(record["transaction_id"]), str(record["account_id"])))
    return keys


def account_totals(records: list[dict[str, object]]) -> dict[str, float]:
    totals: dict[str, float] = {}
    for record in records:
        account_id = str(record["account_id"])
        amount = float(record["amount"])
        totals[account_id] = totals.get(account_id, 0.0) + amount
    return totals


def print_data_structure_demo() -> None:
    records = build_transaction_batch()
    keys = build_record_keys(records)
    totals = account_totals(records)

    print("List size:", len(records))
    print("Tuple keys:", keys)
    print("Dictionary totals:", totals)


if __name__ == "__main__":
    print_data_structure_demo()
