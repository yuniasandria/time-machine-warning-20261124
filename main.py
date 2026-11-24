#!/usr/bin/env python3
"""Funniest Time Machine Warning Label entry.

Writes a single one-line warning label (<=120 characters) to
/output/entry.txt. Pure standard library; no third-party imports.
"""

import os

LABEL = (
    "WARNING: Never wave at your own grandfather. "
    "If he waves back, you were never born, "
    "and neither was this warning."
)


def main() -> None:
    label = LABEL.strip()
    if not 1 <= len(label) <= 120:
        raise SystemExit(f"label is {len(label)} chars, must be 1-120")
    if "\n" in label or "\r" in label:
        raise SystemExit("label must be a single line")
    label.encode("utf-8")  # must be valid UTF-8 text

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(label)


if __name__ == "__main__":
    main()
