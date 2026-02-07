#!/usr/bin/env python3
"""Download image URLs to a local directory.

Usage:
  python3 download_images.py --urls-file /tmp/img_urls.txt --out-dir attachments --prefix article-2026-02-07
"""

from __future__ import annotations

import argparse
import pathlib
import re
import urllib.parse
import urllib.request


def sanitize(name: str) -> str:
    name = re.sub(r"[^a-zA-Z0-9._-]+", "-", name).strip("-")
    return name or "img"


def infer_ext(url: str) -> str:
    path = urllib.parse.urlparse(url).path.lower()
    for ext in (".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".bmp", ".avif"):
        if path.endswith(ext):
            return ext
    return ".jpg"


def unique_path(base: pathlib.Path) -> pathlib.Path:
    if not base.exists():
        return base
    stem = base.stem
    suffix = base.suffix
    i = 2
    while True:
        p = base.with_name(f"{stem}-{i}{suffix}")
        if not p.exists():
            return p
        i += 1


def download(url: str, out_path: pathlib.Path, timeout: int = 20) -> bool:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; CodexImageFetcher/1.0)",
            "Accept": "image/*,*/*;q=0.8",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read()
        out_path.write_bytes(data)
        return True
    except Exception:
        return False


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--urls-file", required=True)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--prefix", default="article")
    args = ap.parse_args()

    urls_file = pathlib.Path(args.urls_file)
    out_dir = pathlib.Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    urls = [ln.strip() for ln in urls_file.read_text(encoding="utf-8").splitlines() if ln.strip()]
    seen = set()
    ok = 0
    fail = 0

    for idx, url in enumerate(urls, start=1):
        if url in seen:
            continue
        seen.add(url)

        ext = infer_ext(url)
        filename = sanitize(f"{args.prefix}-{idx}{ext}")
        out_path = unique_path(out_dir / filename)
        if download(url, out_path):
            print(f"OK\t{url}\t{out_path}")
            ok += 1
        else:
            print(f"FAIL\t{url}")
            fail += 1

    print(f"SUMMARY\tok={ok}\tfail={fail}\tout_dir={out_dir}")
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
