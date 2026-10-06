"""Map links, forms and metadata from one authorised web page."""

from __future__ import annotations

import argparse
import json
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urldefrag, urljoin, urlparse
from urllib.request import Request, urlopen

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from guardian_theme import banner, trace_sequence


class SurfaceParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: set[str] = set()
        self.forms: list[dict[str, object]] = []
        self.meta: dict[str, str] = {}
        self._form: dict[str, object] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "a" and values.get("href"):
            self.links.add(values["href"] or "")
        elif tag == "form":
            self._form = {"action": values.get("action", ""), "method": values.get("method", "get").upper(), "inputs": []}
        elif tag == "input" and self._form is not None:
            inputs = self._form["inputs"]
            assert isinstance(inputs, list)
            inputs.append({"name": values.get("name", ""), "type": values.get("type", "text")})
        elif tag == "meta" and values.get("name") and values.get("content"):
            self.meta[values["name"] or ""] = values["content"] or ""

    def handle_endtag(self, tag: str) -> None:
        if tag == "form" and self._form is not None:
            self.forms.append(self._form)
            self._form = None


def fetch(url: str) -> tuple[str, bytes]:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError("URL must use http:// or https://")
    request = Request(url, headers={"User-Agent": "guardian-examples/1.0"})
    with urlopen(request, timeout=15) as response:
        return response.geturl(), response.read(2_000_000)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url")
    args = parser.parse_args()
    trace_sequence()
    banner("GUARDIAN / SURFACE MAP", f"authorised target · {urlparse(args.url).netloc or args.url}")
    final_url, body = fetch(args.url)
    origin = urlparse(final_url).netloc
    parser_impl = SurfaceParser()
    parser_impl.feed(body.decode("utf-8", errors="replace"))
    links = set()
    for link in parser_impl.links:
        absolute, _ = urldefrag(urljoin(final_url, link))
        if urlparse(absolute).netloc == origin:
            links.add(absolute)
    print(json.dumps({"url": final_url, "same_origin_links": sorted(links), "forms": parser_impl.forms, "metadata": parser_impl.meta}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
