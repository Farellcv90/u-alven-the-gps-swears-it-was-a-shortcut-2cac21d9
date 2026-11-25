#!/usr/bin/env python3
"""Write the GPS's one-line excuse to /output/entry.txt.

Entry for make.fun's "The GPS Swears It Was a Shortcut" bounty.
Standard library only; no network, no secrets.
"""

from pathlib import Path

ENTRY = (
    "The map swore that llama farm was a four-lane highway, "
    "and frankly the llamas waved us through like they believed it too."
)

OUTPUT_PATH = Path("/output/entry.txt")


def validate_entry(text: str) -> None:
    """Check the entry meets the gate: 1-200 chars, one line, not blank."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def main() -> None:
    validate_entry(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
