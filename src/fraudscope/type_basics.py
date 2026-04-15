from __future__ import annotations


def parse_transaction(amount_text: str, channel_text: str) -> dict[str, object]:
    amount_value = float(amount_text)
    channel_value = str(channel_text).strip()
    is_high_value = amount_value > 5000.0

    return {
        "amount": amount_value,
        "channel": channel_value,
        "is_high_value": is_high_value,
    }


def print_type_demo() -> None:
    record = parse_transaction("7800.50", " Online ")
    print("Parsed record:", record)
    print("Type of amount:", type(record["amount"]).__name__)
    print("Type of channel:", type(record["channel"]).__name__)
    print("Type of is_high_value:", type(record["is_high_value"]).__name__)


if __name__ == "__main__":
    print_type_demo()
