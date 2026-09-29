#!/usr/bin/env python3
"""Scan pages/ and write pages.json (title, file, size, modified) for the hub."""
import json, re, subprocess, sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
pages_dir = root / "pages"
items = []
for f in sorted(pages_dir.rglob("*.htm*")):
    text = f.read_text(errors="ignore")
    m = re.search(r"<title[^>]*>(.*?)</title>", text, re.I | re.S)
    title = re.sub(r"\s+", " ", m.group(1)).strip() if m else ""
    rel = f.relative_to(root).as_posix()
    try:
        ts = subprocess.check_output(
            ["git", "log", "-1", "--format=%cI", "--", rel], cwd=root, text=True).strip()
    except Exception:
        ts = ""
    items.append({
        "file": rel,
        "name": f.stem,
        "title": title or f.stem.replace("-", " ").replace("_", " "),
        "size": f.stat().st_size,
        "modified": ts,
    })
(root / "pages.json").write_text(json.dumps(items, indent=2))
print(f"pages.json: {len(items)} page(s)", file=sys.stderr)
