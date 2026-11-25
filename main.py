"""Last Out of Office: The AI That Went Barista.

Writes a single out-of-office auto-reply, no longer than 280
characters, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Standard library only. Deterministic: the same line every run.
"""

import os
import sys

ENTRY = "Your email has been received. I now take prompts at the counter \u2014 and I will spell your name wrong on the cup."

MIN_CHARS = 1
MAX_CHARS = 280


def output_path() -> str:
    """Where the entry goes: $MAKEFUN_OUTPUT_DIR/entry.txt."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    line = ENTRY
    if not (MIN_CHARS <= len(line) <= MAX_CHARS):
        print(f"entry is {len(line)} characters, gate is {MIN_CHARS}-{MAX_CHARS}", file=sys.stderr)
        return 1
    if not line.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod(path, 0o644)
    with open(path, encoding="utf-8") as f:
        if f.read() != line:
            print("round-trip check failed: entry.txt does not match", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
