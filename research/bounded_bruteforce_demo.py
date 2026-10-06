"""Demonstrate bounded credential guessing against a local synthetic fixture."""

from __future__ import annotations

import argparse
import hashlib
from dataclasses import dataclass


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
    args = parser.parse_args()
    if not 1 <= args.limit <= 8:
        parser.error("--limit must be between 1 and 8")

    fixture = Fixture(username="lab-user", password_sha256=digest("orbit-17"))
    candidates = ["spring-01", "admin123", "ne0sync", "redteam", "orbit-16", "orbit-17", "password", "guardian"]
    found, attempts = run_audit(fixture, candidates, args.limit)

    print("target: local synthetic fixture")
    print(f"username: {fixture.username}")
    print(f"attempts: {attempts}/{args.limit}")
    if found is None:
        print("result: not found")
        return 1
    print("result: match found")
    print("password: synthetic-only")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
