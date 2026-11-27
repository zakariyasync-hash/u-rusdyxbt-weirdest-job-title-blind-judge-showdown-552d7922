#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown (v1).

Writes one deterministic job title to /output/entry.txt and validates
the competition gate: UTF-8 text of 1 to 60 characters, not only
whitespace.
"""

import os
import sys

ENTRY = "Lead Apologizer to Disappointed Office Plants"
OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 60


def validate(text: str) -> None:
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")  # must be valid UTF-8


def self_check() -> None:
    """Edge-case checks for the gate validator itself (not the entry)."""
    for bad in ("", " " * 5, "x" * (MAX_CHARS + 1)):
        try:
            validate(bad)
        except ValueError:
            continue
        raise AssertionError(f"validator accepted invalid input: {bad!r}")
    validate("x" * MAX_CHARS)  # boundary: exactly 60 chars is valid


def main() -> int:
    self_check()
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    # Round-trip: read the file back and require it byte-identical.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    if raw != ENTRY.encode("utf-8"):
        raise ValueError("round-trip mismatch: file differs from ENTRY")
    validate(raw.decode("utf-8"))
    print(f"wrote {len(ENTRY)} characters to {OUTPUT_PATH} (round-trip OK)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
