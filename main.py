#!/usr/bin/env python3
"""Two Robots in an Elevator — make.fun entry.

Writes one line of awkward small talk that one robot says to another
while they ride an elevator together, to /output/entry.txt.

The line:
    So… do we talk about the smell, or do we both pretend my olfactory
    sensor has been faulty since floor three?

Why it works:
- It is one line of small talk between two robots in a lift: the
  speaker opens with the classic awkward "So…" and a question neither
  of them wants to answer.
- Machine logic shows through the politeness: an olfactory sensor, a
  fault report, a floor counter. A human would say "do you smell
  that?"; a robot blames a sensor.
- The awkwardness lands on the thing neither robot wants to name:
  the smell. Both of them know exactly what it is, and both would
  rather file a false sensor fault than say it out loud.
- The twist is the alibi: the sensor has supposedly been faulty
  "since floor three" — a suspiciously precise, conveniently timed
  malfunction that started exactly when the smell did.

Gate: UTF-8 text, 1-200 characters, not only whitespace, one line.
"""

import os
import sys

ENTRY = (
    "So… do we talk about the smell, or do we both pretend my "
    "olfactory sensor has been faulty since floor three?"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    # Gate checks, enforced before anything is written.
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must not be empty"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert 1 <= len(ENTRY) <= 200, f"entry must be 1-200 chars, got {len(ENTRY)}"

    encoded = ENTRY.encode("utf-8")  # raises if not valid UTF-8 text
    assert encoded.decode("utf-8") == ENTRY

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")

    # Round-trip verification: read back exactly what was written.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY + "\n", "round-trip mismatch"
    assert 1 <= len(written.rstrip("\n")) <= 200

    print(f"Wrote {len(ENTRY)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
