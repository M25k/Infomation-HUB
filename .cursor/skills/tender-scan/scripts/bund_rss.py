#!/usr/bin/env python3
"""Read the public service.bund.de Ausschreibungen RSS feed. No login."""

from __future__ import annotations

import html
import re
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date, datetime, timedelta
from email.utils import parsedate_to_datetime

from score import score_notice

FEED = "https://www.service.bund.de/Content/Globals/Functions/RSSFeed/RSSGenerator_Ausschreibungen.xml"
USER_AGENT = "Northdocks-tender-scan/1.1 (+https://northdocks.com; kontakt@northdocks.com)"

FIELD_RE = re.compile(r"(Vergabestelle|Erf.{0,8}llungsort|Angebotsfrist):\s*([^|]+)")
DATE_RE = re.compile(r"(\d{2})\.(\d{2})\.(\d{4})")


def _strip_tags(raw: str) -> str:
    text = re.sub(r"<br\s*/?>", " | ", raw, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def _iso_de(value: str) -> str:
    m = DATE_RE.search(value or "")
    if not m:
        return ""
    return f"{m.group(3)}-{m.group(2)}-{m.group(1)}"


def _pub_iso(pub: str) -> str:
    if not pub:
        return ""
    try:
        return parsedate_to_datetime(pub).date().isoformat()
    except (TypeError, ValueError, IndexError):
        return ""


def flatten_item(item: ET.Element) -> dict:
    title = (item.findtext("title") or "").strip()
    link = (item.findtext("link") or "").split("#", 1)[0].strip()
    desc = _strip_tags(item.findtext("description") or "")
    fields = {k: v.strip() for k, v in FIELD_RE.findall(desc)}
    deadline = ""
    for key, val in fields.items():
        if "frist" in key.lower():
            deadline = _iso_de(val)
    planned = bool(
        re.search(
            r"beabsichtig|vorinformation|vorab.?information|transparenzbekanntmachung",
            title,
            re.I,
        )
    )
    return {
        "source": "bund.de",
        "id": link,
        "publication_number": "",
        "title": title,
        "lot_title": "",
        "buyer": fields.get("Vergabestelle", ""),
        "publication_date": _pub_iso(item.findtext("pubDate") or ""),
        "deadline": deadline,
        "cpv": "",
        "buyer_country": "DEU",
        "place": next((v for k, v in fields.items() if "llungsort" in k.lower()), ""),
        "notice_type": "pin-buyer" if planned else "",
        "contract_nature": "",
        "url": link,
        "url_de": link,
        "description": desc[:4000],
        "platform": "service.bund.de",
    }


def collect(days: int = 8) -> dict:
    req = urllib.request.Request(FEED, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=60) as resp:
        xml = resp.read()
    root = ET.fromstring(xml)
    since = date.today() - timedelta(days=days)
    rows = []
    errors = []
    for item in root.findall("./channel/item"):
        flat = flatten_item(item)
        pub = flat.get("publication_date") or ""
        if pub:
            try:
                if datetime.fromisoformat(pub).date() < since:
                    continue
            except ValueError:
                pass
        scored = {**flat, **score_notice(flat), "query_id": "bund-rss", "matched_queries": ["bund-rss"]}
        rows.append(scored)
    rows.sort(key=lambda r: (-r["score"], r.get("deadline") or "9999"))
    return {
        "generated": date.today().isoformat(),
        "since": since.isoformat(),
        "source": FEED,
        "notice_count": len(rows),
        "review": [r for r in rows if r["decision"] == "review"],
        "maybe": [r for r in rows if r["decision"] == "maybe"],
        "skip": [r for r in rows if r["decision"] == "skip"],
        "errors": errors,
        "all": rows,
    }
