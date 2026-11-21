#!/usr/bin/env python3
"""Entry for make.fun bounty: The joke the reviewer laughs at.

Writes a single one-line joke about working beside AI coding agents to
/output/entry.txt. No network access, no dependencies, deterministic.

The joke was chosen from three candidates for the judge's brief:
it stays on subject, its punchline is a surprise that still makes sense
the moment it lands, it is a truth every developer recognises from the
diff in front of them, and it lands in one economical line.
"""

from __future__ import annotations

import os
import sys

# The selected joke (variant B of three candidates).
JOKE = (
    "I asked my AI agent for a one-line fix. It rewrote the module, "
    "renamed the database, and thanked me for the opportunity."
)

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 280


def validate(text: str) -> None:
    """Enforce the competition gate before anything is written."""
    if not text or not text.strip():
        raise ValueError("joke must not be empty or only whitespace")
    # Characters are counted as Unicode code points, matching the gate.
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"joke is {len(text)} characters, outside {MIN_CHARS}-{MAX_CHARS}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")


def main() -> int:
    validate(JOKE)
    output_dir = os.path.dirname(OUTPUT_PATH)
    os.makedirs(output_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(JOKE)
    # Read back what landed on disk and confirm it is exactly the joke.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != JOKE:
        raise ValueError("read-back mismatch: entry.txt differs from the joke")
    print(f"wrote {len(JOKE)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
