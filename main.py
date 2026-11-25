"""Copy the newspaper image into the output folder.

This entry ships the finished image as ``entry.png`` next to this script.
All this program does is place an exact copy of that file at
``/output/entry.png``, which is where the competition expects it.

The copy is byte for byte, uses only the standard library, and touches
no network, so running it twice always produces identical output.
"""

import os
import shutil
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
DESTINATION = OUTPUT_DIR / "entry.png"


def main() -> int:
    if not SOURCE.is_file():
        print(f"missing source image: {SOURCE}", file=sys.stderr)
        return 1
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, DESTINATION)
    if DESTINATION.stat().st_size != SOURCE.stat().st_size:
        print("copy incomplete: size mismatch", file=sys.stderr)
        return 1
    print(f"wrote {DESTINATION} ({DESTINATION.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
