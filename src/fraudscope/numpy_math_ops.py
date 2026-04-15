from __future__ import annotations


def run_basic_math(values: list[float]) -> dict[str, object]:
    try:
        import numpy as np
    except ModuleNotFoundError as error:
        raise RuntimeError("NumPy is not installed. Run: pip install -r requirements.txt") from error

    base = np.array(values, dtype=float)
    return {
        "base": base,
        "add_100": base + 100.0,
        "subtract_50": base - 50.0,
        "multiply_2": base * 2.0,
        "divide_10": base / 10.0,
    }


def print_math_demo() -> None:
    try:
        results = run_basic_math([1200.0, 7800.0, 450.0, 15200.0])
    except RuntimeError as error:
        print(error)
        return

    for key, value in results.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    print_math_demo()
