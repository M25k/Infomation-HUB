#!/usr/bin/env python3
"""Search TED for public notices that could match Northdocks competencies.

Does not log in to national portals. Does not store credentials.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from datetime import date, timedelta
from pathlib import Path

from score import pick_text, score_notice

TED_URL = "https://api.ted.europa.eu/v3/notices/search"
USER_AGENT = "Northdocks-tender-scan/1.1 (+https://northdocks.com; kontakt@northdocks.com)"

FIELDS = [
    "publication-number",
    "notice-title",
    "buyer-name",
    "publication-date",
    "deadline-date-lot",
    "classification-cpv",
    "buyer-country",
    "place-of-performance",
    "notice-type",
    "contract-nature",
    "links",
]

HERE = Path(__file__).resolve().parent
QUERIES_PATH = HERE.parent / "queries.json"


def load_queries() -> list[dict]:
    data = json.loads(QUERIES_PATH.read_text(encoding="utf-8"))
    return data["queries"]


def ted_search(query: str, limit: int, scope: str, next_token: str | None = None) -> dict:
    body = {
        "query": query,
        "fields": FIELDS,
        "limit": min(limit, 100),
        "scope": scope,
        "paginationMode": "ITERATION",
    }
    if next_token:
        body["iterationNextToken"] = next_token
    req = urllib.request.Request(
        TED_URL,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": USER_AGENT,
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")
        raise RuntimeError(f"TED HTTP {exc.code}: {detail[:2000]}") from exc


def html_url(notice: dict, pub: str) -> str:
    links = notice.get("links") or {}
    html = links.get("html") or {}
    for lang in ("DEU", "ENG"):
        if lang in html:
            return html[lang]
    if pub:
        return f"https://ted.europa.eu/de/notice/-/detail/{pub}"
    return ""


def flatten_notice(notice: dict) -> dict:
    pub = pick_text(notice.get("publication-number"))
    title = pick_text(notice.get("notice-title"))
    desc = (
        pick_text(notice.get("description-lot"))
        + " "
        + pick_text(notice.get("description-proc"))
    ).strip()
    return {
        "source": "ted",
        "id": pub,
        "publication_number": pub,
        "title": title,
        "lot_title": pick_text(notice.get("lot-title")),
        "buyer": pick_text(notice.get("buyer-name")),
        "publication_date": pick_text(notice.get("publication-date"))[:10],
        "deadline": pick_text(notice.get("deadline-date-lot"))[:10],
        "cpv": pick_text(notice.get("classification-cpv")),
        "buyer_country": pick_text(notice.get("buyer-country")),
        "place": pick_text(notice.get("place-of-performance")),
        "notice_type": pick_text(notice.get("notice-type")),
        "contract_nature": pick_text(notice.get("contract-nature")),
        "url": html_url(notice, pub),
        "url_de": f"https://ted.europa.eu/de/notice/-/detail/{pub}" if pub else "",
        "description": desc[:4000],
        "platform": "TED",
    }


def extract_notices(payload) -> list:
    notices = []
    if isinstance(payload, list):
        return payload
    if not isinstance(payload, dict):
        return notices
    notices = payload.get("notices") or payload.get("results") or []
    if not notices:
        for key in ("data", "items", "content"):
            if isinstance(payload.get(key), list):
                notices = payload[key]
                break
    return notices or []


def ingest(seen: dict, notices: list, query_id: str) -> None:
    for notice in notices:
        flat = flatten_notice(notice)
        key = flat["publication_number"] or json.dumps(flat, sort_keys=True)
        scored = {**flat, **score_notice(flat), "query_id": query_id}
        prev = seen.get(key)
        if prev is None or scored["score"] > prev["score"]:
            scored["matched_queries"] = sorted(
                set((prev or {}).get("matched_queries", []) + [query_id])
            )
            seen[key] = scored
        else:
            prev["matched_queries"] = sorted(set(prev.get("matched_queries", []) + [query_id]))


def collect(days: int = 8, limit: int = 100, scope: str = "ACTIVE", query_id: str | None = None) -> dict:
    since = (date.today() - timedelta(days=days)).strftime("%Y%m%d")
    queries = load_queries()
    if query_id:
        queries = [q for q in queries if q["id"] == query_id]
        if not queries:
            raise SystemExit(f"Unknown query id: {query_id}")

    seen: dict[str, dict] = {}
    errors: list[dict] = []
    for spec in queries:
        q = spec["query"].replace("{SINCE}", since)
        token = None
        pages = 0
        while pages < 5:
            if pages == 0:
                time.sleep(1.0)
            else:
                time.sleep(0.5)
            try:
                payload = ted_search(q, limit, scope, token)
            except RuntimeError as exc:
                err = str(exc)
                if "429" in err and pages == 0:
                    time.sleep(8.0)
                    try:
                        payload = ted_search(q, limit, scope, token)
                    except RuntimeError as exc2:
                        errors.append({"id": spec["id"], "error": str(exc2)})
                        break
                else:
                    errors.append({"id": spec["id"], "error": err})
                    break
            ingest(seen, extract_notices(payload), spec["id"])
            token = payload.get("iterationNextToken") or payload.get("nextToken")
            pages += 1
            if not token or payload.get("timedOut"):
                break

    rows = sorted(seen.values(), key=lambda r: (-r["score"], r.get("deadline") or "9999"))
    return {
        "generated": date.today().isoformat(),
        "since": since,
        "source": TED_URL,
        "query_count": len(queries),
        "notice_count": len(rows),
        "review": [r for r in rows if r["decision"] == "review"],
        "maybe": [r for r in rows if r["decision"] == "maybe"],
        "skip": [r for r in rows if r["decision"] == "skip"],
        "errors": errors,
        "all": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="TED competence search for Northdocks")
    parser.add_argument("--days", type=int, default=8, help="Publication lookback in days")
    parser.add_argument("--limit", type=int, default=100)
    parser.add_argument("--scope", default="ACTIVE", choices=["ACTIVE", "ALL"])
    parser.add_argument("--out", type=Path, help="Write JSON here instead of stdout")
    parser.add_argument("--query-id", help="Run only one named query from queries.json")
    args = parser.parse_args()

    result = collect(days=args.days, limit=args.limit, scope=args.scope, query_id=args.query_id)
    text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
