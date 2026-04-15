from __future__ import annotations

from pathlib import Path


REQUIRED_DIRECTORIES = [
    "data/raw",
    "data/processed",
    "notebooks",
    "outputs/figures",
    "outputs/reports",
    "src/fraudscope",
    "docs/learning_units",
]


def check_structure() -> list[tuple[str, bool]]:
    results: list[tuple[str, bool]] = []
    for directory in REQUIRED_DIRECTORIES:
        exists = Path(directory).exists()
        results.append((directory, exists))
    return results


def print_structure_report() -> None:
    print("FraudScope folder structure report")
    print("-" * 33)
    for directory, exists in check_structure():
        status = "OK" if exists else "MISSING"
        print(f"{directory:<24} {status}")


if __name__ == "__main__":
    print_structure_report()
