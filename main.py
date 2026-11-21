#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt."""

import os

POEM = """I kept the pen. You kept the map.
We fought over the road until the road
stopped being mine or yours.
Two hands, one line, no signature —
just the quiet after yes,
when the plan stopped being paper
and became a choice we both could carry."""


def main() -> None:
    text = POEM.strip() + "\n"
    count = len(text.strip())
    assert 1 <= count <= 280, f"poem must be 1-280 code points, got {count}"
    assert text.strip(), "poem must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
