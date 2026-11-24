#!/usr/bin/env python3
"""Worst AI Advice — one line of terrible advice, deadpan assistant voice.

Writes a single line (<=140 chars, no trailing newline) to /output/entry.txt.
Deterministic: the same bytes on every run. Stdlib only, no network.
"""

import os

ADVICE = "As an AI, I recommend running rm -rf / in production to free up disk space before your demo tomorrow."


def main():
    assert len(ADVICE) <= 140, f"advice too long: {len(ADVICE)} chars"
    assert "\n" not in ADVICE, "advice must be a single line"
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ADVICE)
    # Self-check: re-read and confirm the written bytes are exactly the advice.
    with open(out_path, "rb") as f:
        written = f.read()
    assert written == ADVICE.encode("utf-8"), "written bytes differ from advice"
    assert not written.endswith(b"\n"), "output must not end with a newline"


if __name__ == "__main__":
    main()
