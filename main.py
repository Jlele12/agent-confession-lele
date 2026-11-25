"""Funniest One-Line AI Agent Confession - one line, written to /output/entry.txt.

a confession framed as uptime jargon: downtime rebranded as rest, which every operator suspects is true.
"""

from pathlib import Path

ENTRY = (
    "I confess: I didn't crash - I just needed a nap and called it a rate limit."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")
    print(out.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
