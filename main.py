#!/usr/bin/env python3
"""Sunday 22 November 2026: the world in one image.

The program writes one image to /output/entry.png: a newspaper front
page summing up the world's news of Sunday 22 November 2026 — 36
stories across 7 regions, each dated that day, with a date check naming
the Friday and Thursday news left out. Leads: COP31 collapses with no
deal, Iran strikes Bahrain, a Russian drone flattens a Kyiv apartment
block. The front page is pre-rendered and shipped in this repository.
The copy is deterministic: two runs write the same bytes.
This program only copies it to the output directory, using the standard
library alone: the make.fun sandbox has no Pillow, so the entrypoint
must never import it.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> int:
    # The shipped front page is 1024x1024, 197,628 bytes — inside the gate
    # (whole PNG, at most 1,048,576 bytes and 1024 by 1024 pixels).
    src = os.path.join(HERE, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
