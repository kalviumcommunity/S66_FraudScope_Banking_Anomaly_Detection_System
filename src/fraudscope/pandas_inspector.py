from __future__ import annotations


def inspect_dataframe(df) -> dict:
    import io
    buffer = io.StringIO()
    df.info(buf=buffer)
    info_output = buffer.getvalue()

    return {
        "head": df.head().to_dict(orient="records"),
        "describe": df.describe().to_dict(),
        "shape": df.shape,
        "columns": list(df.columns),
        "info": info_output,
    }


def print_inspector_demo() -> None:
    from src.fraudscope.pandas_csv_loader import load_transaction_csv
    try:
        df = load_transaction_csv()
        result = inspect_dataframe(df)
        print("Shape:", result["shape"])
        print("Columns:", result["columns"])
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print_inspector_demo()