#!/usr/bin/env python3
"""Refresh the live sections of README.md from bayar.dev.

Rewrites the text between marker comments:
  <!-- BENCH:START --> ... <!-- BENCH:END -->  measured numbers from /api/benchmarks
  <!-- LOG:START -->   ... <!-- LOG:END -->    latest posts from /log/rss.xml
Stdlib only. Leaves a section untouched if its source can't be fetched.
"""
import json
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from pathlib import Path

README = Path(__file__).resolve().parent.parent / "README.md"
BENCH_URL = "https://bayar.dev/api/benchmarks"
RSS_URL = "https://bayar.dev/log/rss.xml"
WORKLOAD = "chat-short"
MAX_POSTS = 3


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "namchinbayar-readme-refresh"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def badge(label, value, color):
    q = lambda s: urllib.parse.quote(str(s).replace("-", "--").replace("_", "__"), safe="")
    return (f'<img alt="{label}: {value}" src="https://img.shields.io/badge/'
            f'{q(label)}-{q(value)}-{color}?style=flat-square&labelColor=0d1117">')


def bench_section():
    data = json.loads(fetch(BENCH_URL))
    model = data["productionModel"]
    row = next(s for s in data["summary"] if s["model"] == model and s["workload"] == WORKLOAD)
    w = str(data.get("window", "7d"))
    window = f"{w[:-1]} days" if w.endswith("d") else w
    label = next((m["label"] for m in data["models"] if m["id"] == model), model)
    badges = "\n  ".join([
        badge("TTFT p50", f'{round(row["ttftP50"])} ms', "7ee7ff"),
        badge("output p50", f'{round(row["tokensPerSecP50"])} tok/s', "a78bfa"),
        badge("success", f'{row["successRate"] * 100:.1f}%'.replace(".0%", "%"), "3fb950"),
        badge("samples", f'{row["samples"]:,}', "8b949e"),
    ])
    return (f'<p>\n  <a href="https://bayar.dev/benchmarks">\n  {badges}\n  </a>\n</p>\n\n'
            f'<sub>{label}, short chat, last {window}, '
            f'probed every 15 minutes. Method and raw data at '
            f'<a href="https://bayar.dev/benchmarks">bayar.dev/benchmarks</a>.</sub>')


def log_section():
    root = ET.fromstring(fetch(RSS_URL))
    lines = []
    for item in root.findall("./channel/item")[:MAX_POSTS]:
        title = item.findtext("title", "").strip()
        link = item.findtext("link", "").strip()
        date = item.findtext("pubDate", "").strip()
        when = parsedate_to_datetime(date).strftime("%b %-d, %Y") if date else ""
        lines.append(f"- [{title}]({link})" + (f" · <sub>{when}</sub>" if when else ""))
    lines.append("- [All entries →](https://bayar.dev/log)")
    return "\n".join(lines)


def replace(text, name, body):
    pat = re.compile(rf"(<!-- {name}:START -->\n).*?(<!-- {name}:END -->)", re.S)
    if not pat.search(text):
        raise SystemExit(f"marker {name} missing from README")
    return pat.sub(lambda m: m.group(1) + body + "\n" + m.group(2), text)


def main():
    text = README.read_text()
    new = text
    for name, build in (("BENCH", bench_section), ("LOG", log_section)):
        try:
            new = replace(new, name, build())
        except SystemExit:
            raise
        except Exception as e:  # keep the last good content on any fetch/parse error
            print(f"skip {name}: {e}", file=sys.stderr)
    if new != text:
        README.write_text(new)
        print("README updated")
    else:
        print("no changes")


if __name__ == "__main__":
    main()
