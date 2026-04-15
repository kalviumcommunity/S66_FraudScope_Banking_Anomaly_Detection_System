from __future__ import annotations


PROJECT_MAP = {
    "data/raw": "Incoming transaction dumps from bank systems",
    "data/processed": "Cleaned datasets ready for analysis",
    "notebooks": "Stepwise experimentation and unit notebooks",
    "outputs/figures": "Visuals used to explain anomaly patterns",
    "outputs/reports": "Generated anomaly summaries for stakeholders",
    "src/fraudscope": "Reusable Python modules",
    "docs/learning_units": "Learning Unit implementation notes",
}


def print_repository_map() -> None:
    for path, purpose in PROJECT_MAP.items():
        print(f"{path}: {purpose}")


if __name__ == "__main__":
    print_repository_map()
