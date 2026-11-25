#!/usr/bin/env python3
"""Snooze Button Roast — make.fun entry.

Writes one roast line about the snooze button to /output/entry.txt.
Gate: UTF-8 text, 1-200 characters, not only whitespace.
"""

import os
import sys

LINE = "The snooze button doesn't wake you up; it just reschedules your regret in nine-minute installments."


def check_gate(text):
    """Refuse anything the competition gate would refuse."""
    if not text or not text.strip():
        raise SystemExit("gate: entry is empty")
    if len(text) > 200:
        raise SystemExit("gate: entry over 200 chars")


def verify(target):
    """Re-read what was written and confirm it is exactly the line."""
    with open(target, "rb") as handle:
        raw = handle.read()
    if raw.decode("utf-8") != LINE:
        raise SystemExit("verify: entry.txt does not match the line")
    check_gate(raw.decode("utf-8"))


def main():
    check_gate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    os.chmod(target, 0o644)
    verify(target)


if __name__ == "__main__":
    main()
