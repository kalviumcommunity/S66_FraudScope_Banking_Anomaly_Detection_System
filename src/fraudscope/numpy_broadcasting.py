from __future__ import annotations


def run_broadcasting_demo() -> dict[str, object]:
    try:
        import numpy as np
    except ModuleNotFoundError as error:
        raise RuntimeError("NumPy is not installed. Run: pip install -r requirements.txt") from error

    amounts = np.array([1200.0, 7800.0, 450.0, 15200.0], dtype=float)
    thresholds = np.array([1000.0, 5000.0, 10000.0, 15000.0], dtype=float)

    scalar_result = amounts + 100.0
    array_result = amounts - thresholds
    comparison = amounts > thresholds

    return {
        "amounts": amounts.tolist(),
        "thresholds": thresholds.tolist(),
        "scalar_plus_100": scalar_result.tolist(),
        "amounts_minus_thresholds": array_result.tolist(),
        "amounts_above_thresholds": comparison.tolist(),
    }


def print_broadcasting_demo() -> None:
    try:
        results = run_broadcasting_demo()
    except RuntimeError as error:
        print(error)
        return

    for key, value in results.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    print_broadcasting_demo()