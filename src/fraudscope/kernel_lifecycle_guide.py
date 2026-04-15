from __future__ import annotations


KERNEL_ACTIONS = {
    "Run": "Execute selected cell to update outputs",
    "Interrupt": "Stop a stuck or long-running cell without closing notebook",
    "Restart": "Clear kernel memory and rerun cells from top to avoid stale state",
}


def print_kernel_guide() -> None:
    print("Jupyter kernel lifecycle guide")
    print("-" * 30)
    for action, purpose in KERNEL_ACTIONS.items():
        print(f"{action:<10}: {purpose}")

    print("\nBest practice sequence")
    print("1. Run cells top to bottom")
    print("2. Interrupt if execution hangs")
    print("3. Restart and run all before final conclusions")


if __name__ == "__main__":
    print_kernel_guide()
