from __future__ import annotations

import platform
import shutil
import subprocess
from dataclasses import dataclass


@dataclass
class ToolCheck:
    name: str
    command: list[str]
    available: bool
    details: str


def run_command(command: list[str]) -> tuple[bool, str]:
    executable = command[0]
    if shutil.which(executable) is None:
        return False, f"{executable} not found in PATH"

    try:
        result = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as error:
        stderr = error.stderr.strip() or "command failed"
        return False, stderr

    output = result.stdout.strip() or result.stderr.strip() or "no version output"
    return True, output


def verify_environment() -> list[ToolCheck]:
    checks: list[ToolCheck] = []
    commands: dict[str, list[list[str]]] = {
        "python": [["python", "--version"], ["py", "--version"]],
        "conda": [["conda", "--version"]],
        "jupyter": [["jupyter", "--version"]],
    }

    for name, command_options in commands.items():
        selected_command = command_options[0]
        available = False
        details = "not checked"

        for command in command_options:
            selected_command = command
            available, details = run_command(command)
            if available:
                break

        checks.append(
            ToolCheck(
                name=name,
                command=selected_command,
                available=available,
                details=details,
            )
        )

    return checks


def print_report() -> None:
    print(f"OS: {platform.system()} {platform.release()}")
    print("Environment verification report")
    print("-" * 34)
    for check in verify_environment():
        status = "OK" if check.available else "MISSING"
        print(f"{check.name:<8} [{status}] {check.details}")


if __name__ == "__main__":
    print_report()
