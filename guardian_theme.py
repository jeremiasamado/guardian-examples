"""Shared terminal styling for Guardian research tools."""

from __future__ import annotations

import os
import sys
import time
from typing import TextIO

PURPLE = "\033[38;5;141m"
LIGHT_PURPLE = "\033[38;5;183m"
GREEN = "\033[38;5;120m"
YELLOW = "\033[38;5;221m"
DIM = "\033[2m"
RESET = "\033[0m"


def enabled(stream: TextIO | None = None) -> bool:
    stream = stream or sys.stdout
    return bool(stream.isatty() and os.environ.get("NO_COLOR") is None and os.environ.get("TERM") != "dumb")


def paint(value: object, colour: str, stream: TextIO | None = None) -> str:
    return f"{colour}{value}{RESET}" if enabled(stream) else str(value)


def banner(title: str, subtitle: str, stream: TextIO | None = None) -> None:
    stream = stream or sys.stderr
    print(paint(f"╭─ {title}", PURPLE, stream), file=stream)
    print(paint(f"╰─ {subtitle}", LIGHT_PURPLE, stream), file=stream)


def trace_sequence(stream: TextIO | None = None) -> None:
    """Show the BadBoy17 terminal signature when running interactively."""
    stream = stream or sys.stderr
    if not enabled(stream):
        return
    frames = (
        "[•    ] LINKING BADBOY17 NODE",
        "[ •   ] TRACE CHANNEL OPEN",
        "[  •  ] EVIDENCE PATH READY",
    )
    for frame in frames:
        print(paint(frame, LIGHT_PURPLE, stream), file=stream, flush=True)
        time.sleep(0.12)


def status(label: str, value: object, stream: TextIO | None = None) -> str:
    stream = stream or sys.stderr
    return f"{paint(label + ':', PURPLE, stream)} {paint(value, LIGHT_PURPLE, stream)}"
