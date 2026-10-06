<div align="center">

[PT-PT](./README.pt-PT.md) | **EN**

<img src="https://readme-typing-svg.demolab.com?font=Share+Tech+Mono&size=36&duration=3200&pause=1200&color=8A00C4&background=00000000&center=true&vCenter=true&width=850&height=80&lines=GUARDIAN+RESEARCH+TOOLING;MAP+THE+SURFACE;TRIAGE+THE+ARTEFACT;FOLLOW+THE+EVIDENCE;RECON+%2F+RESEARCH+%2F+REPORT" alt="Guardian research tooling">

<br>

<img src="https://readme-typing-svg.demolab.com?font=VT323&size=24&duration=2600&pause=1000&color=E4BCFF&background=00000000&center=true&vCenter=true&width=850&height=40&lines=%3E+enumerate+%2F+fingerprint+%2F+triage;%3E+files+%2F+strings+%2F+hashes;%3E+observe+%E2%86%92+extract+%E2%86%92+document;Small+tools.+Clean+evidence." alt="Enumerate, fingerprint and triage">

</div>

# Guardian Examples

Small Python utilities for **authorised reconnaissance** and local research.
The repository keeps the tooling deliberately narrow: collect what is visible,
fingerprint the response, triage local artefacts and leave the interpretation
to the operator.

## Layout

```text
recon/
├─ web_surface_mapper.py   # one-page surface map: links, forms and metadata
├─ endpoint_inventory.py    # robots, sitemap and same-origin endpoint inventory
└─ headers_fingerprint.py   # response headers, TLS scheme and server hints
research/
├─ file_triage.py           # local file identity and basic type triage
├─ strings_extract.py       # printable ASCII/UTF-16LE string extraction
├─ hash_inventory.py        # SHA-256 inventory for a file or directory
└─ bounded_bruteforce_demo.py # fixed local credential-guessing exercise
guardian_theme.py             # shared purple terminal theme
```

## Quick start

```powershell
python .\recon\headers_fingerprint.py https://example.com
python .\recon\web_surface_mapper.py https://example.com
python .\recon\endpoint_inventory.py https://example.com

python .\research\file_triage.py .\sample.bin
python .\research\strings_extract.py .\sample.bin
python .\research\hash_inventory.py .\samples
python .\research\bounded_bruteforce_demo.py
```

Recon tools make one request per discovered resource at most and stay on the
same origin. They do not brute-force paths, exploit inputs, bypass controls or
launch concurrent scans.

The brute-force demo is deliberately different: it runs only against an
in-memory synthetic fixture, uses a fixed eight-candidate list and has no
network or user-supplied target. It demonstrates bounded credential auditing,
not access against a real service.

## Terminal style

Every tool uses the shared `guardian_theme.py` module for a purple terminal
signature. JSON remains on standard output; banners are sent to standard error
so the tools still work cleanly in pipelines. Set `NO_COLOR=1` when plain
output is needed.

## Scope

Use the recon tools only against systems you own or are explicitly authorised
to assess. Use the research tools on files you are allowed to inspect. See
[`SCOPE.md`](./SCOPE.md).

<p>
  <img src="./assets/badboy17jpg.jpg" width="24" height="24" alt="">
  <strong>BadBoy17</strong>
</p>
