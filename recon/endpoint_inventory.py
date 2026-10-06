"""Inventory robots.txt, sitemap.xml and same-origin references."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from guardian_theme import banner, trace_sequence


def read(url: str) -> str:
    request = Request(url, headers={"User-Agent": "guardian-examples/1.0"})
    with urlopen(request, timeout=15) as response:
        return response.read(1_000_000).decode("utf-8", errors="replace")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url")
    args = parser.parse_args()
    parsed = urlparse(args.url if "://" in args.url else f"https://{args.url}")
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        parser.error("URL must use http:// or https://")
    base = f"{parsed.scheme}://{parsed.netloc}"
    trace_sequence()
    banner("GUARDIAN / ENDPOINT MAP", f"authorised target · {parsed.netloc}")
    robots_url = urljoin(base, "/robots.txt")
    sitemap_url = urljoin(base, "/sitemap.xml")
    robots = read(robots_url)
    sitemap = read(sitemap_url)
    paths = [line.split(":", 1)[1].strip() for line in robots.splitlines() if line.lower().startswith("sitemap:")]
    urls = sorted({line.strip() for line in sitemap.splitlines() if "<loc>" in line for line in [line.replace("<loc>", "").replace("</loc>", "")]})
    print(json.dumps({"origin": base, "robots_url": robots_url, "sitemaps": sorted(set(paths + [sitemap_url])), "sitemap_urls": urls}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
