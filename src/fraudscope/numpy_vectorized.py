from __future__ import annotations


def run_vectorized_threshold(values: list[float], threshold: float = 5000.0) -> dict[str, object]:
    try:
        import numpy as np
    except ModuleNotFoundError as error:
        raise RuntimeError("NumPy is not installed. Run: pip install -r requirements.txt") from error

    amounts = np.array(values, dtype=float)
    mask = amounts > threshold
    return {
        "amounts": amounts,
        "above_threshold": mask,
        "count_above": int(mask.sum()),
        "values_above": amounts[mask].tolist(),
    }


def print_vectorized_demo() -> None:
    try:
        results = run_vectorized_threshold([1200.0, 7800.0, 450.0, 15200.0, 2300.0])
    except RuntimeError as error:
        print(error)
        return

    for key, value in results.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    print_vectorized_demo()