"""Create a deterministic SHA-256 inventory for a file or directory."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    if not args.path.exists():
        parser.error("path does not exist")
    files = [args.path] if args.path.is_file() else sorted(path for path in args.path.rglob("*") if path.is_file())
    print(json.dumps([{"path": str(path), "size": path.stat().st_size, "sha256": digest(path)} for path in files], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
