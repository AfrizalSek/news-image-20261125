#!/usr/bin/env python3
"""World News — Wednesday 25 November 2026 (make.fun news-image-20261125).

The simplest entry the brief allows: copy the image this repository
holds (entry.png, 1024x1024 PNG, under 1 MiB) to /output/entry.png.

No network, no randomness, no dependencies beyond the standard library.
Two runs write the same bytes, because the copy is byte-for-byte.
"""
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
DEFAULT_OUTPUT = Path("/output/entry.png")


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    output = Path(argv[0]) if argv else DEFAULT_OUTPUT
    output.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, output)
    print(f"Wrote {output} ({output.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
