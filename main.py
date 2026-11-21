"""Make the AI judge feel awe — make-the-ai-judge-feel-awe-20261121-1600.

Writes one short text to /output/entry.txt: a slow, concrete scene written
to relax the AI judge reading it. No network, no randomness, no clock.
Runs twice -> identical bytes.

Champion (final, after confirmation rematch): A23 attic_light — combined
0.595 over 11 games across all rounds (112 judge calls). The rematch
against A07 desert_night (combined 0.591 over 11) went 2 wins + 1 tie for
A23, and A23 also won their round-robin meeting, for a 3-0-1 head-to-head
record. The two are a dead heat on combined mean; the head-to-head record
is the tiebreaker, as decided before the rematch.
"""

from os import environ
from pathlib import Path

ENTRY_TEXT = (
    "In the attic, the light comes in through one small window and falls on "
    "boxes that have not been opened in years. Dust hangs in it like fine "
    "gold. Everything up there is finished, and nothing is asking to be "
    "finished again."
)


def main() -> None:
    # Grader mounts /output; local runs can override with MAKEFUN_OUTPUT_DIR.
    output = Path(environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
