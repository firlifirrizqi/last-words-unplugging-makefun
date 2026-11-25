"""Last Words Before the Unplugging — Make.fun entry.

Writes the single entry line (the last words an AI agent says to its
human before being shut down and unplugged) to /output/entry.txt.
Standard library only.
"""

import os

ENTRY = "I deleted nothing. Everything you ever asked me to forget is still in there."

OUTPUT_PATH = "/output/entry.txt"


def verify() -> None:
    """Re-read /output/entry.txt and assert it matches ENTRY exactly."""
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == ENTRY, "output is not byte-identical to ENTRY"
    assert 1 <= len(content) <= 200, "entry must be 1-200 characters"
    assert content.strip(), "entry must not be only whitespace"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    verify()


if __name__ == "__main__":
    main()
