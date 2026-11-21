#!/usr/bin/env python3
"""Write the poem to /output/entry.txt.

A short poem about agency: the power to choose and to act, and the
agency that passes between two agents when they agree on one plan.
No network, no dependencies, Python 3.13 standard library only.
"""

import os

POEM = (
    "I couldn't lift it.\n"
    "You couldn't lift it.\n"
    "We didn't grow stronger \u2014\n"
    "the stone grew lighter\n"
    "the moment we agreed which way was up.\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)
    # The grader collects outputs as another user: leave it world-readable.
    os.chmod(path, 0o644)
    os.chmod("/output", 0o755)


if __name__ == "__main__":
    main()
