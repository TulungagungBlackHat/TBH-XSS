# TBH-XSS

<p align="center">
  <a href="https://github.com/TulungagungBlackHat/TBH-XSS/actions/workflows/ci.yml"><img src="https://github.com/TulungagungBlackHat/TBH-XSS/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <img src="https://img.shields.io/badge/license-MIT-red.svg" alt="License">
  <img src="https://img.shields.io/badge/python-3.8%2B-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/payload-safe-green.svg" alt="Safe payloads">
</p>

Reflected XSS detector. Injects a harmless marker payload and checks whether it comes back unencoded in the response — a strong reflection signal you can confirm manually.

Part of the [Tulungagung Black Hat](https://github.com/TulungagungBlackHat) toolset.

## What It Checks

- Reflection of a unique marker string in the response body
- HTTP status alongside the reflection (helps distinguish 200-reflected from error pages)
- JSON output for pipeline use

The payload is a benign canary string — nothing is executed, nothing is stored. This is a **signal finder**, not an exploit framework: a reflection needs manual confirmation and, in real programs, a working proof of concept.

## Install

```bash
git clone https://github.com/TulungagungBlackHat/TBH-XSS
cd TBH-XSS
pip install -r requirements.txt
```

## Usage

```
usage: xss.py [-h] -u URL [--json JSON]

options:
  -u, --url URL     Target URL with a query parameter
  --json JSON       Save result as JSON
```

```bash
python3 xss.py -u "https://example.com/search?q=test" --json result.json
```

## Sample Output

```
[*] Testing https://example.com/search?q=test dengan payload: <marker>
[!] Reflected! https://example.com/search?q=test -> 200 - Potensi XSS, cek manual!
[✓] JSON: result.json
```

## Authorized Use Only

Only against scopes you own or are authorized to test. Reflection ≠ automatic XSS — respect program rules on payload delivery. See [SECURITY.md](SECURITY.md).

## Related Tools

- [TBH-AllScan](https://github.com/TulungagungBlackHat/TBH-AllScan) — XSS plus 9 other modules in one scan
- [TBH-OpenRedirect](https://github.com/TulungagungBlackHat/TBH-OpenRedirect) / [TBH-CORS](https://github.com/TulungagungBlackHat/TBH-CORS) — sibling detectors

## License

[MIT](LICENSE) — Tulungagung Black Hat, East Java, Indonesia. Always Smile :)
