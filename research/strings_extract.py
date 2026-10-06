"""Extract printable ASCII and UTF-16LE strings from a local file."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--min-length", type=int, default=5)
    args = parser.parse_args()
    if not args.path.is_file():
        parser.error("path must point to a file")
    data = args.path.read_bytes()
    ascii_strings = re.findall(rb"[\x20-\x7e]{%d,}" % args.min_length, data)
    wide_strings = re.findall(rb"(?:[\x20-\x7e]\x00){%d,}" % args.min_length, data)
    for value in sorted({item.decode("ascii", errors="replace") for item in ascii_strings}):
        print(value)
    for value in sorted({item.decode("utf-16le", errors="replace") for item in wide_strings}):
        print(value)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
