from __future__ import annotations

from pathlib import Path


STARTUP_STEPS = [
    "Open terminal in repository root",
    "Activate Python or Conda environment",
    "Run: jupyter notebook",
    "Open notebooks/ directory from home interface",
]

INTERFACE_SECTIONS = {
    "Files": "Browse notebooks and datasets",
    "Running": "See active notebooks and terminals",
    "Upload": "Add files such as CSV transaction dumps",
    "New": "Create new notebook or terminal",
}


def print_jupyter_guide() -> None:
    print("Jupyter startup steps")
    print("-" * 22)
    for index, step in enumerate(STARTUP_STEPS, start=1):
        print(f"{index}. {step}")

    print("\nHome interface sections")
    print("-" * 24)
    for section, purpose in INTERFACE_SECTIONS.items():
        print(f"{section}: {purpose}")

    notebooks_path = Path("notebooks")
    if notebooks_path.exists():
        print("\nNotebooks folder detected at:", notebooks_path.resolve())


if __name__ == "__main__":
    print_jupyter_guide()
