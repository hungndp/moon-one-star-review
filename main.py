#!/usr/bin/env python3
"""The Moon Gets One Star — make.fun entry.

Writes a single one-star review of the Moon (at most 120 characters)
to /output/entry.txt (or $ENTRY_OUTPUT) and prints it.

The review: a deadpan stalker complaint. The Moon appears to follow you
home every night — parallax, but try telling the reviewer that.
"""

import os
import sys

# The setup: the star rating, the subject named outright, the incident.
SETUP = "★☆☆☆☆ The Moon follows me home every night, watches me sleep,"

# The punch: the twist lands on the last word.
PUNCH = "never once introduced itself."


def build_line():
    """Assemble the review from its two halves."""
    return SETUP + " " + PUNCH


def write_entry(line, path):
    """Write the review deterministically, no trailing newline."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(line)


def main():
    line = build_line()
    if not (1 <= len(line) <= 120):
        print(f"refusing: review is {len(line)} chars, must be 1-120", file=sys.stderr)
        return 1
    if not line.strip():
        print("refusing: review is blank", file=sys.stderr)
        return 1
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    write_entry(line, out)
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
