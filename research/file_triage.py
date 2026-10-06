"""Produce basic local file identity and type triage."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from guardian_theme import banner


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    if not args.path.is_file():
        parser.error("path must point to a file")
    banner("GUARDIAN / FILE TRIAGE", f"local artefact · {args.path.name}")
    data = args.path.read_bytes()
    print(json.dumps({"path": str(args.path), "size": len(data), "sha256": hashlib.sha256(data).hexdigest(), "magic": data[:16].hex(), "extension": args.path.suffix.lower()}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
