from __future__ import annotations

from pathlib import Path


def load_transaction_csv(file_path: str = "data/raw/sample_transactions.csv"):
    try:
        import pandas as pd
    except ModuleNotFoundError as error:
        raise RuntimeError("Pandas is not installed. Run: pip install -r requirements.txt") from error

    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"CSV file not found: {file_path}")

    return pd.read_csv(file_path)


def print_csv_demo() -> None:
    try:
        df = load_transaction_csv()
        print("Loaded DataFrame:")
        print(df)
    except (FileNotFoundError, RuntimeError) as error:
        print(error)


if __name__ == "__main__":
    print_csv_demo()