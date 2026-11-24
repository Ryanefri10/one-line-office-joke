# One-Line Office Joke: 24-Hour Sprint — u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162
# (Python 3, standard library only.)
# Writes one funny one-line office joke to /output/entry.txt.
# Deterministic: one constant, no network, no randomness, no clock.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
# Concept (final): my keycard opens every door in the building except
# the one where they decide my salary. The joke is the fit: access is
# total everywhere it doesn't matter and denied exactly where it does.
# Deadpan, tight, and a fresh angle — "keycard" appears in none of the
# 757 titles already in the field, while "meeting" appears in 127.

import os
from pathlib import Path

LINE = "My keycard opens every door in the building except the one where they decide my salary."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    # Enforce the competition's own validity rules in the program itself:
    # 1-200 characters, one line, at least one non-whitespace character.
    if not 1 <= len(LINE) <= 200 or not any(not c.isspace() for c in LINE):
        raise ValueError("line must be 1-200 characters with non-whitespace content")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be a single line")
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
