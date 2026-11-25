#!/usr/bin/env python3
"""The Best Meal You Ever Had — one sentence.

The entry is a single fixed sentence, written for make.fun
u-pangg7-the-best-meal-you-ever-had-a3ac0f85: one sentence of at
most 200 characters about the best meal I ever had. A warung at
2am off Jalan Sudirman, sate ayam still smoking off the grill,
peanut sauce dripping down my wrist. This program writes that
sentence to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
outside the grader's container):

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Python 3.13, standard library only. The sentence is fixed text:
the same bytes on every run, no network.
"""

import os
import sys
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINE = (
    "At 2am in a warung off Jalan Sudirman, the sate ayam came off "
    "the grill still smoking, peanut sauce dripping down my wrist, "
    "and I forgot every bad day I had ever had."
)


def abort(message):
    """Stop with the reason on stderr and a non-zero exit."""
    print(f"main.py: {message}", file=sys.stderr)
    return 1


def deliver():
    """Validate the sentence against the gate, then write it out."""
    if not 1 <= len(LINE) <= 200:
        return abort(f"sentence is {len(LINE)} characters, the gate allows 1-200")
    if not LINE.strip():
        return abort("sentence is only white space, the gate refuses it")
    target = Path(OUTPUT_DIR) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE, encoding="utf-8")
    print(f"wrote {target}: {len(LINE)} characters")
    return 0


if __name__ == "__main__":
    raise SystemExit(deliver())
