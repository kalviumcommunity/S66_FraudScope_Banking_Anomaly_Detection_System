from __future__ import annotations

from pathlib import Path


STAGE_RULES = {
    "raw": "Original source files, never edited in place",
    "processed": "Cleaned and transformed analysis-ready datasets",
    "outputs": "Generated charts, summaries, and anomaly reports",
}


def classify_artifact(path_text: str) -> str:
    path = Path(path_text).as_posix()
    if path.startswith("data/raw/"):
        return "raw"
    if path.startswith("data/processed/"):
        return "processed"
    if path.startswith("outputs/"):
        return "outputs"
    return "unclassified"


def print_stage_policy() -> None:
    print("Data stage policy")
    print("-" * 17)
    for stage, rule in STAGE_RULES.items():
        print(f"{stage:<10}: {rule}")


if __name__ == "__main__":
    print_stage_policy()
