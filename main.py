#!/usr/bin/env python3
"""Write one short text for make.fun bounty u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610."""

import os
import sys
from pathlib import Path

TEXT = "My watch congratulated me on a twelve-hour stand goal I hit standing at the fridge."


def main() -> None:
    assert 1 <= len(TEXT) <= 280, "text must be between 1 and 280 characters"

    out_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    )
    out_dir.mkdir(parents=True, exist_ok=True)

    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))

    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
