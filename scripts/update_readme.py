#!/usr/bin/env python3
"""
Scan `src/` Python solution files for complexity comments and update README.md

Supported comment forms (placed near the top of the solution file):

# Time: O(n)
# Space: O(1)

# Complexity: Time=O(n), Space=O(1)

Runs as: `python3 scripts/update_readme.py` and writes the table between
`<!-- COMPLEXITY_TABLE_START -->` and `<!-- COMPLEXITY_TABLE_END -->` in README.md
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
README = ROOT / "README.md"


def extract_complexity(path: Path):
    time = None
    space = None
    try:
        head = path.read_text(encoding="utf-8").splitlines()[:40]
    except Exception:
        return None, None

    for line in head:
        # direct Time / Space lines
        mt = re.search(r'Time\s*[:=]\s*([^,;\n]+)', line, re.I)
        ms = re.search(r'Space\s*[:=]\s*([^,;\n]+)', line, re.I)
        if mt:
            time = mt.group(1).strip()
        if ms:
            space = ms.group(1).strip()

        # Complexity: Time=...
        # Space=...
        mc = re.search(r'Complexity\s*[:=]\s*(.*)$', line, re.I)
        if mc:
            s = mc.group(1)
            mt2 = re.search(r'Time\s*[:=]?\s*([^,;\n]+)', s, re.I)
            ms2 = re.search(r'Space\s*[:=]?\s*([^,;\n]+)', s, re.I)
            if mt2:
                time = mt2.group(1).strip()
            if ms2:
                space = ms2.group(1).strip()
            # fallback: if values look like O(...)
            if not (time or space):
                parts = [p.strip() for p in s.split(',')]
                for p in parts:
                    if 'O(' in p:
                        if not time:
                            time = p
                        elif not space:
                            space = p
    return time or "?", space or "?"


def filename_to_title(fname: str):
    # try to parse `123.name-here.py` to get a readable title
    m = re.match(r'(\d+)\.(.+)\.py$', fname)
    if m:
        num = m.group(1)
        raw = m.group(2)
        title = raw.replace('-', ' ').replace('_', ' ').strip()
        title = ' '.join(w.capitalize() for w in title.split())
        return f"{num} — {title}"
    return fname


def build_rows():
    rows = []
    if not SRC.exists():
        return rows
    files = sorted([p for p in SRC.iterdir() if p.suffix == '.py'])
    for p in files:
        fname = p.name
        time, space = extract_complexity(p)
        title = filename_to_title(fname)
        link = f"src/{fname}"
        rows.append(f"| [{fname}]({link}) | {title} | {time} | {space} |")
    return rows


def update_readme():
    if not README.exists():
        print("README.md not found", file=sys.stderr)
        return 2
    text = README.read_text(encoding="utf-8")
    start = '<!-- COMPLEXITY_TABLE_START -->'
    end = '<!-- COMPLEXITY_TABLE_END -->'
    if start not in text or end not in text:
        print("Markers not found in README.md", file=sys.stderr)
        return 3

    rows = build_rows()
    body = "\n".join(rows) + "\n" if rows else ""

    new = re.sub(rf"{re.escape(start)}.*?{re.escape(end)}",
                 f"{start}\n{body}{end}", text, flags=re.S)
    README.write_text(new, encoding="utf-8")
    print(f"Wrote {len(rows)} rows to README.md")
    return 0


if __name__ == '__main__':
    sys.exit(update_readme())
