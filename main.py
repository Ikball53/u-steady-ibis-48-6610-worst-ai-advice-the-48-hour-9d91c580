"""Worst AI Advice — entry v3.

Writes exactly one line of deliberately terrible advice to
/output/entry.txt. Deterministic, stdlib only, no network access.
"""

import os

LINE = "Use the same password everywhere so you never forget it. Hackers can only be in one place at a time."


def main() -> None:
    # The sealed scorer accepts 1 to 140 characters; refuse to emit an
    # invalid entry rather than silently submitting one.
    if not 1 <= len(LINE) <= 140:
        raise ValueError(f"entry is {len(LINE)} characters, must be 1-140")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
