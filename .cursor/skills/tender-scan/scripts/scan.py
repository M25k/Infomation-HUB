#!/usr/bin/env python3
"""Run the weekly Northdocks tender scan across public APIs.

Sources (no logins, no portal passwords):
  ted     EU-threshold notices via TED Search API v3
  bkms    Bund/Länder/Kommunen via oeffentlichevergabe.de search + notice text
  bund    service.bund.de public RSS (adds notices BKMS often misses)

Credentials for e-Vergabe / DTVP stay in the Drive sheet. This script never
reads them.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

import bkms_search
import bund_rss
import ted_search

HERE = Path(__file__).resolve().parent


def _norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (text or "").lower()).strip()


def merge_key(row: dict) -> str:
    pub = (row.get("publication_number") or "").strip()
    if pub:
        return f"ted:{pub}"
    return title_key(row)


def title_key(row: dict) -> str:
    title = _norm(row.get("title", ""))[:70]
    deadline = (row.get("deadline") or "")[:10]
    return f"txt:{title}|{deadline}"


def merge(buckets: list[dict]) -> list[dict]:
    seen: dict[str, dict] = {}
    by_title: dict[str, str] = {}

    def absorb(row: dict) -> None:
        key = merge_key(row)
        tkey = title_key(row)
        if key.startswith("txt:") and tkey in by_title:
            key = by_title[tkey]
        elif key.startswith("ted:"):
            by_title[tkey] = key
        prev = seen.get(key)
        if prev is None:
            row = {**row, "sources": [s for s in [row.get("source")] if s]}
            seen[key] = row
            by_title.setdefault(tkey, key)
            return
        prev["sources"] = sorted(set(prev.get("sources", []) + [row.get("source")]))
        prev["matched_queries"] = sorted(
            set(prev.get("matched_queries", []) + row.get("matched_queries", []))
        )
        if (row.get("score") or 0) > (prev.get("score") or 0):
            for field in ("score", "clusters", "decision", "skip_reasons", "description"):
                if row.get(field):
                    prev[field] = row[field]
        if not prev.get("publication_number") and row.get("publication_number"):
            prev["publication_number"] = row["publication_number"]
            prev["url_ted"] = row.get("url_ted") or prev.get("url_ted")
        if not prev.get("description") and row.get("description"):
            prev["description"] = row["description"]
        if not prev.get("deadline") and row.get("deadline"):
            prev["deadline"] = row["deadline"]
        if row.get("url") and "oeffentlichevergabe.de" in (row.get("url") or ""):
            prev["url"] = row["url"]
            prev["url_de"] = row.get("url_de") or prev.get("url_de")

    for bucket in buckets:
        for row in bucket.get("all") or []:
            absorb(row)
    rows = list(seen.values())
    rows.sort(key=lambda r: (-(r.get("score") or 0), r.get("deadline") or "9999"))
    return rows


def collect(days: int, sources: list[str]) -> dict:
    parts = []
    errors = []
    coverage = {}
    if "ted" in sources:
        ted = ted_search.collect(days=days)
        parts.append(ted)
        coverage["ted"] = ted.get("notice_count", 0)
        errors.extend({"source": "ted", **e} for e in ted.get("errors") or [])
    if "bkms" in sources:
        bkms = bkms_search.collect(days=days)
        parts.append(bkms)
        coverage["bkms"] = bkms.get("notice_count", 0)
        errors.extend({"source": "bkms", **e} for e in bkms.get("errors") or [])
    if "bund" in sources:
        bund = bund_rss.collect(days=days)
        parts.append(bund)
        coverage["bund"] = bund.get("notice_count", 0)
        errors.extend({"source": "bund", **e} for e in bund.get("errors") or [])

    rows = merge(parts)
    review = [r for r in rows if r.get("decision") == "review"]
    maybe = [r for r in rows if r.get("decision") == "maybe"]
    skip = [r for r in rows if r.get("decision") == "skip"]
    return {
        "generated": date.today().isoformat(),
        "days": days,
        "sources_run": sources,
        "coverage": coverage,
        "notice_count": len(rows),
        "review": review,
        "maybe": maybe,
        "skip_count": len(skip),
        "skip_sample": [
            {"title": r.get("title"), "buyer": r.get("buyer"), "score": r.get("score"), "clusters": r.get("clusters")}
            for r in skip
            if r.get("clusters")
        ][:25],
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Northdocks multi-portal tender scan")
    parser.add_argument("--days", type=int, default=8)
    parser.add_argument("--sources", default="ted,bkms,bund", help="Comma list: ted,bkms,bund")
    parser.add_argument("--out", type=Path, help="Write merged JSON")
    args = parser.parse_args()
    sources = [s.strip() for s in args.sources.split(",") if s.strip()]
    result = collect(args.days, sources)
    text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text, encoding="utf-8")
        review_n = len(result["review"])
        maybe_n = len(result["maybe"])
        sys.stderr.write(
            f"Wrote {args.out} — {result['notice_count']} notices, "
            f"{review_n} review, {maybe_n} maybe, coverage={result['coverage']}\n"
        )
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
