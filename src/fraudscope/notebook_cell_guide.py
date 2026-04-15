from __future__ import annotations


CELL_GUIDE = {
    "code": [
        "Load and transform transaction data",
        "Run anomaly rules and numeric checks",
        "Generate plots and outputs",
    ],
    "markdown": [
        "State objective of analysis section",
        "Document assumptions and caveats",
        "Explain why transactions were flagged",
    ],
}


def print_cell_guide() -> None:
    print("Notebook cell usage guide")
    print("-" * 25)
    for cell_type, items in CELL_GUIDE.items():
        print(f"\n{cell_type.upper()} CELLS")
        for item in items:
            print(f"- {item}")


if __name__ == "__main__":
    print_cell_guide()
