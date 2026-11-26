#!/usr/bin/env python3
"""The Worst Line an AI Could Say — make.fun entry.

Writes one pickup line (the worst an AI could plausibly say) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt) and prints it
to stdout. Standard library only; fully deterministic.
"""

import hashlib
import os
import sys
from pathlib import Path

LINE = "I'd retrain my whole model just to raise the chance you'd say yes from 0.0% to 0.3%."

EXPECTED_SHA256 = "efd205e6287098191254b16b310ece29fedc91b8b35561914fb54ad0a3909bde"


def output_path() -> Path:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(out_dir) / "entry.txt"


def check() -> int:
    """Re-read entry.txt and verify hash, length and single-line shape."""
    path = output_path()
    if not path.is_file():
        print(f"FAIL: {path} does not exist")
        return 1
    data = path.read_bytes()
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        print("FAIL: entry.txt is not valid UTF-8")
        return 1
    digest = hashlib.sha256(data).hexdigest()
    problems = []
    if digest != EXPECTED_SHA256:
        problems.append(f"sha256 mismatch: {digest} != {EXPECTED_SHA256}")
    if not 1 <= len(text) <= 140:
        problems.append(f"length {len(text)} not in 1..140")
    if text != text.strip() or not text.strip():
        problems.append("entry is empty or only whitespace")
    if "\n" in text or "\r" in text:
        problems.append("entry is not a single line")
    if problems:
        for p in problems:
            print(f"FAIL: {p}")
        return 1
    print(f"OK: {len(text)} chars, sha256 {digest}, single line")
    return 0


def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv and argv[0] == "--check":
        return check()
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE, encoding="utf-8")
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
