from __future__ import annotations


def create_amount_array(values: list[float]):
    try:
        import numpy as np
    except ModuleNotFoundError as error:
        raise RuntimeError("NumPy is not installed. Run: pip install -r requirements.txt") from error

    return np.array(values, dtype=float)


def print_numpy_demo() -> None:
    values = [1200.0, 7800.0, 450.0, 15200.0]
    try:
        amount_array = create_amount_array(values)
    except RuntimeError as error:
        print(error)
        return

    print("Array:", amount_array)
    print("Shape:", amount_array.shape)
    print("Dtype:", amount_array.dtype)


if __name__ == "__main__":
    print_numpy_demo()
