from __future__ import annotations


def count_high_value_for_loop(amounts: list[float], threshold: float = 5000.0) -> int:
    count = 0
    for amount in amounts:
        if amount > threshold:
            count += 1
    return count


def count_until_limit_while_loop(amounts: list[float], threshold: float = 5000.0, limit: int = 2) -> int:
    index = 0
    count = 0
    while index < len(amounts) and count < limit:
        if amounts[index] > threshold:
            count += 1
        index += 1
    return count


def print_loop_demo() -> None:
    sample_amounts = [1200.0, 7800.0, 450.0, 15200.0, 2300.0]
    print("For loop count:", count_high_value_for_loop(sample_amounts))
    print("While loop count (limit=2):", count_until_limit_while_loop(sample_amounts))


if __name__ == "__main__":
    print_loop_demo()
