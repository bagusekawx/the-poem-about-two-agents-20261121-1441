#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt.

The poem must be UTF-8 text of 1 to 280 Unicode code points, not only
whitespace. No network access.
"""

import os

POEM = """Neither of us moved first.
We laid our reasons down like tools
and picked up the same one.
Two wills, one road —
the yes was not surrender.
It was the moment the plan
stopped asking whose it was."""

def main() -> None:
    text = POEM.strip() + "\n"
    code_points = len(text.strip())
    assert 1 <= code_points <= 280, f"entry is {code_points} code points, must be 1-280"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()
