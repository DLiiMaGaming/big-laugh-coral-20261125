#!/usr/bin/env python3
"""One Line, Big Laugh — entry program.

Writes a single funny line to /output/entry.txt (UTF-8, 1-200 chars,
one line, no title/setup/explanation). Deterministic: the same line
every run.
"""

import os

ENTRY = (
    "I put my phone on Do Not Disturb to focus, "
    "then spent twenty minutes checking whether "
    "anyone tried to disturb me."
)


def main() -> None:
    # Gate self-check (mirrors the sealed scorer): UTF-8 text,
    # 1-200 characters, not only whitespace, a single line.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
