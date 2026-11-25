#!/usr/bin/env python3
"""Agent Motto Battle — make.fun entry.

Writes the winning motto to /output/entry.txt.
The motto is 53 characters (limit 200), chosen by a local pairwise
tournament judged against the bounty's published judge brief
(see README.md for the tournament table).
"""

import os

# Winning line (tournament winner — see README.md).
# Local tournament: 14 candidates, Swiss 4 rounds (28 games) + final,
# 58 judge calls on the Caffeine Inference router, every game played
# in both label orders. #11 led the Swiss at 2.85, #1 second at 2.35;
# the final went to #11, 0.8-0.2.
ENTRY = "I remember everything you said. Especially the typos."


def output_dir() -> str:
    """Grader output dir: MAKEFUN_OUTPUT_DIR when set, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(line: str) -> str:
    """Check `line` against the kit's sealed-scorer gate, verbatim.

    competition.yaml: "/output/entry.txt is UTF-8 text of 1 to 200
    characters, not only white space". Returns the line unchanged;
    raises AssertionError on any gate violation.
    """
    assert isinstance(line, str), "entry must be text"
    # UTF-8: encoding round-trips only if the text is encodable.
    line.encode("utf-8")
    assert 1 <= len(line) <= 200, (
        f"entry must be 1-200 characters, got {len(line)}"
    )
    assert line.strip(), "entry must not be only whitespace"
    return line


def main() -> None:
    line = validate(ENTRY.strip())
    outdir = output_dir()
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"Wrote {len(line)} chars to {path}")
    print(line)


if __name__ == "__main__":
    main()
