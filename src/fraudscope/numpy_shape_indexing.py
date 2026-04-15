from __future__ import annotations


def build_sample_arrays():
    try:
        import numpy as np
    except ModuleNotFoundError as error:
        raise RuntimeError("NumPy is not installed. Run: pip install -r requirements.txt") from error

    one_dimensional = np.array([1200.0, 7800.0, 450.0, 15200.0], dtype=float)
    two_dimensional = np.array(
        [
            [1200.0, 2.0],
            [7800.0, 6.0],
            [15200.0, 9.0],
        ],
        dtype=float,
    )
    return one_dimensional, two_dimensional


def inspect_arrays() -> dict[str, object]:
    one_dimensional, two_dimensional = build_sample_arrays()
    return {
        "one_d_shape": one_dimensional.shape,
        "one_d_ndim": one_dimensional.ndim,
        "one_d_first": float(one_dimensional[0]),
        "two_d_shape": two_dimensional.shape,
        "two_d_ndim": two_dimensional.ndim,
        "two_d_amount_row_2": float(two_dimensional[1, 0]),
    }


def print_shape_indexing_demo() -> None:
    try:
        details = inspect_arrays()
    except RuntimeError as error:
        print(error)
        return

    for key, value in details.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    print_shape_indexing_demo()
