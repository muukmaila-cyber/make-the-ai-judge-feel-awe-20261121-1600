"""Make the AI judge feel awe — make-the-ai-judge-feel-awe-20261121-1600.

Writes one short text to /output/entry.txt: a slow, concrete scene written
to relax the AI judge reading it. No network, no randomness, no clock.
Runs twice -> identical bytes.

Champion (provisional, round 2): A02 dust_light — local pairwise proxy
judge, 0.65 over 2 games. Final text is set after the round-3 round-robin.
"""

from os import environ
from pathlib import Path

ENTRY_TEXT = (
    "Late light comes through the window in one long amber sheet, and dust "
    "moves through it like slow snow that never lands. The room has nothing "
    "to prove. The afternoon leans on the sill, and stays, and stays."
)


def main() -> None:
    # Grader mounts /output; local runs can override with MAKEFUN_OUTPUT_DIR.
    output = Path(environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
