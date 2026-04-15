from __future__ import annotations


def create_amount_series(values: list[float], labels: list[str] = None):
    try:
        import pandas as pd
    except ModuleNotFoundError as error:
        raise RuntimeError("Pandas is not installed. Run: pip install -r requirements.txt") from error

    if labels is None:
        labels = [f"T{i+1:04d}" for i in range(len(values))]
    return pd.Series(data=values, index=labels, name="transaction_amount")


def describe_series(series) -> dict:
    return {
        "length": len(series),
        "dtype": str(series.dtype),
        "mean": float(series.mean()),
        "sum": float(series.sum()),
    }


def print_series_demo() -> None:
    try:
        amounts = create_amount_series([1200.0, 7800.0, 450.0, 15200.0])
        print("Series:\n", amounts)
        print("\nStats:", describe_series(amounts))
    except RuntimeError as error:
        print(error)


if __name__ == "__main__":
    print_series_demo()