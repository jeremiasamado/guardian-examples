"""Demonstrate bounded credential guessing against a local synthetic fixture."""

from __future__ import annotations

import argparse
import hashlib
import sys
import time
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from guardian_theme import GREEN, PURPLE, banner, paint, trace_sequence


@dataclass(frozen=True)
class Fixture:
    username: str
    password_sha256: str


def digest(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def run_audit(fixture: Fixture, candidates: list[str], limit: int) -> tuple[str | None, int]:
    for attempts, candidate in enumerate(candidates[:limit], start=1):
        if digest(candidate) == fixture.password_sha256:
            return candidate, attempts
    return None, min(len(candidates), limit)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=8)
    parser.add_argument("--quiet", action="store_true", help="show only the final result")
    args = parser.parse_args()
    if not 1 <= args.limit <= 8:
        parser.error("--limit must be between 1 and 8")

    fixture = Fixture(username="lab-user", password_sha256=digest("orbit-17"))
    candidates = ["spring-01", "admin123", "ne0sync", "redteam", "orbit-16", "orbit-17", "password", "guardian"]
    if not args.quiet:
        trace_sequence()
        banner("GUARDIAN / BOUNDED AUDIT", "local synthetic fixture · SHA-256 · max 8 candidates")
        print(paint("  target     ", PURPLE) + "local synthetic fixture")
        print(paint("  username   ", PURPLE) + fixture.username)
        print(paint("  candidates ", PURPLE) + f"{min(args.limit, len(candidates))}/{len(candidates)}")

    started = time.perf_counter()
    found, attempts = run_audit(fixture, candidates, args.limit)
    elapsed_ms = (time.perf_counter() - started) * 1000
    if not args.quiet:
        print(paint("  attempts   ", PURPLE) + f"{attempts}/{args.limit}")
        print(paint("  elapsed    ", PURPLE) + f"{elapsed_ms:.3f} ms")

    if found is None:
        print(paint("  result     ", PURPLE) + paint("not found", GREEN if args.quiet else PURPLE))
        return 1
    print(paint("  result     ", PURPLE) + paint("match found", GREEN))
    print(paint("  secret     ", PURPLE) + "synthetic-only")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
