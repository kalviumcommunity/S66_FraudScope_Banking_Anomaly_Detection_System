from __future__ import annotations


def create_transaction_dataframe():
    try:
        import pandas as pd
    except ModuleNotFoundError as error:
        raise RuntimeError("Pandas is not installed. Run: pip install -r requirements.txt") from error

    data = {
        "transaction_id": ["T1001", "T1002", "T1003", "T1004"],
        "account_id": ["A01", "A02", "A01", "A03"],
        "amount": [1200.0, 7800.0, 450.0, 15200.0],
        "channel": ["ATM", "Online", "POS", "Online"],
    }
    return pd.DataFrame(data)


def get_column_info(df) -> dict:
    return {
        "columns": list(df.columns),
        "shape": df.shape,
        "dtypes": df.dtypes.to_dict(),
    }


def print_dataframe_demo() -> None:
    try:
        df = create_transaction_dataframe()
        print("DataFrame:\n", df)
        print("\nInfo:", get_column_info(df))
    except RuntimeError as error:
        print(error)


if __name__ == "__main__":
    print_dataframe_demo()