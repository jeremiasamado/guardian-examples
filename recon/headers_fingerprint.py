"""Capture response headers and basic transport metadata."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from guardian_theme import banner


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url")
    args = parser.parse_args()
    url = args.url if "://" in args.url else f"https://{args.url}"
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        parser.error("URL must use http:// or https://")
    banner("GUARDIAN / HEADERS", f"authorised target · {parsed.netloc}")
    request = Request(url, method="HEAD", headers={"User-Agent": "guardian-examples/1.0"})
    with urlopen(request, timeout=15) as response:
        headers = {key.lower(): value for key, value in response.headers.items()}
        result = {"url": response.geturl(), "status": response.status, "scheme": urlparse(response.geturl()).scheme, "server": headers.get("server"), "headers": headers}
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
