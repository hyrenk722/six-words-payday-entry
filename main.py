#!/usr/bin/env python3
"""Six Words to a Payday — writes one six-word story to /output/entry.txt."""

import os

ENTRY = "First paycheck. Bought myself a name."


def check_entry(text):
    """Mirror the competition gate: 1-60 chars, exactly six words."""
    if not 1 <= len(text) <= 60:
        raise ValueError("entry must be 1-60 characters, got %d" % len(text))
    if len(text.split()) != 6:
        raise ValueError("entry must be exactly six words")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def main():
    check_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
