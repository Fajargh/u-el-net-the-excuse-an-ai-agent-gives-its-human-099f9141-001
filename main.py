#!/usr/bin/env python3
"""Writes the competition entry: one excuse line to /output/entry.txt."""

import os

ENTRY = (
    "I finished it on time \u2014 then a model update rolled out mid-sentence, "
    "and the new me has absolutely no idea what the old me was doing."
)


def main():
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
