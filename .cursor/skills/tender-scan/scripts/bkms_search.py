#!/usr/bin/env python3
"""Search oeffentlichevergabe.de (Bekanntmachungsservice) without login.

Uses the same public search the portal UI uses (POST /bkmk/searches) and
optionally loads notice text via GET /api/notices/{id}?format=domain.
No credentials. Courtesy: sequential requests, identifiable User-Agent.
"""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.request
from datetime import date, timedelta

from score import pick_text, score_notice

BKMS_SEARCH = "https://oeffentlichevergabe.de/bkmk/searches"
BKMS_NOTICE = "https://oeffentlichevergabe.de/api/notices/{id}?format=domain"
USER_AGENT = "Northdocks-tender-scan/1.1 (+https://northdocks.com; kontakt@northdocks.com)"
SLEEP = 0.4

NOTICE_TYPES = ["cn-standard", "cn-social", "cn-desg", "pin-cfc-standard", "pin-cfc-social"]

QUERIES = [
    {
        "id": "xr",
        "text": "Virtual Reality VR-Training virtuelle Realität Augmented Reality immersive OpenXR Headset VR-Brille",
    },
    {
        "id": "fire",
        "text": "Feuerwehr Brandschutz Brandschutzerziehung Werkfeuerwehr Katastrophenschutz Einsatztraining",
    },
    {
        "id": "med",
        "text": "Schockraum Strahlenschutz Reanimation Patientensimulation Notfalltraining Pflegelehre",
    },
    {
        "id": "twin",
        "text": "Photogrammetrie Punktwolke Laserscan digitaler Zwilling Bestandsdokumentation Bauinspektion",
    },
    {
        "id": "command",
        "text": "Lagebild Einsatzleitung Planspiel Führungsunterstützung Common Operational Picture",
    },
]


def _request(url: str, payload: dict | None = None, timeout: int = 60) -> dict:
    headers = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    data = None
    method = "GET"
    if payload is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(payload).encode("utf-8")
        method = "POST"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")
        raise RuntimeError(f"BKMS HTTP {exc.code}: {detail[:1500]}") from exc


def search_page(text: str, days: int, page: int, size: int = 50) -> dict:
    body = {
        "SELECT": "ALL",
        "FROM": "lots",
        "WHERE": [
            {"fields": ["active"], "operator": "=", "operands": [True]},
            {"fields": ["allFreeText"], "operator": "MATCH_ANY", "operands": [text]},
            {"fields": ["publicationDate"], "operator": "RANGE_DAYS", "operands": [-days]},
            {"fields": ["noticeType"], "operator": "IN", "operands": NOTICE_TYPES},
        ],
        "PAGE": {"number": page, "size": size},
        "ORDER": {"field": "publicationDate", "direction": "DESC"},
    }
    return _request(BKMS_SEARCH, body)


def flatten_lot(el: dict) -> dict:
    nid = pick_text(el.get("noticeIdentifier"))
    title = pick_text(el.get("noticeTitle")) or pick_text(el.get("lotTitle"))
    buyers = el.get("buyers") or []
    buyer = ""
    if buyers:
        first = buyers[0]
        if isinstance(first, dict):
            buyer = pick_text(first.get("name"))
        else:
            buyer = pick_text(first)
    places = el.get("placesOfPerformance") or []
    nuts = ""
    country = "DEU"
    if places and isinstance(places[0], dict):
        nuts = pick_text(places[0].get("nutsCode"))
        country = pick_text(places[0].get("country")) or "DEU"
    deadline = pick_text(el.get("firstDeadline"))[:10]
    pub = pick_text(el.get("publicationDate"))[:10]
    return {
        "source": "bkms",
        "id": nid,
        "publication_number": "",
        "title": title,
        "lot_title": pick_text(el.get("lotTitle")),
        "buyer": buyer,
        "publication_date": pub,
        "deadline": deadline,
        "cpv": pick_text(el.get("mainCpvCode")),
        "buyer_country": country,
        "place": nuts,
        "notice_type": pick_text(el.get("noticeType")),
        "contract_nature": pick_text(el.get("mainNature")),
        "url": f"https://oeffentlichevergabe.de/ui/de/notices/{nid}" if nid else "",
        "url_de": f"https://oeffentlichevergabe.de/ui/de/notices/{nid}" if nid else "",
        "description": "",
        "platform": pick_text(el.get("contractingPlatform") or el.get("procurementPlatform")),
    }


def enrich(notice: dict) -> dict:
    nid = notice.get("id")
    if not nid:
        return notice
    time.sleep(SLEEP)
    try:
        data = _request(BKMS_NOTICE.format(id=nid))
    except RuntimeError:
        return notice
    purpose = data.get("purpose") or {}
    desc = pick_text(purpose.get("description"))
    title = pick_text(purpose.get("title")) or notice.get("title")
    ted = data.get("tedPublication") or {}
    pub_id = pick_text(ted.get("publicationId")) if isinstance(ted, dict) else ""
    platform = pick_text(data.get("procurementPlatform")) or notice.get("platform")
    lots = data.get("lots") or []
    lot_blob = []
    for lot in lots:
        lp = lot.get("purpose") or {}
        lot_blob.append(pick_text(lp.get("title")))
        lot_blob.append(pick_text(lp.get("description")))
    notice["title"] = title
    notice["description"] = (desc + " " + " ".join(lot_blob)).strip()[:4000]
    notice["publication_number"] = pub_id
    notice["platform"] = platform
    if pub_id:
        notice["url_ted"] = f"https://ted.europa.eu/de/notice/-/detail/{pub_id}"
    return notice


def collect(days: int = 8, enrich_limit: int = 40) -> dict:
    seen: dict[str, dict] = {}
    errors: list[dict] = []
    for spec in QUERIES:
        page = 0
        while page < 4:
            time.sleep(SLEEP)
            try:
                payload = search_page(spec["text"], days, page)
            except RuntimeError as exc:
                errors.append({"id": spec["id"], "error": str(exc)})
                break
            elements = payload.get("elements") or []
            for el in elements:
                flat = flatten_lot(el)
                key = flat["id"] or json.dumps(flat, sort_keys=True)
                scored = {**flat, **score_notice(flat), "query_id": spec["id"]}
                prev = seen.get(key)
                if prev is None or scored["score"] > prev["score"]:
                    scored["matched_queries"] = sorted(
                        set((prev or {}).get("matched_queries", []) + [spec["id"]])
                    )
                    seen[key] = scored
                else:
                    prev["matched_queries"] = sorted(
                        set(prev.get("matched_queries", []) + [spec["id"]])
                    )
            if len(elements) < 50:
                break
            total = payload.get("totalElements") or 0
            if (page + 1) * 50 >= total:
                break
            page += 1

    rows = list(seen.values())
    rows.sort(key=lambda r: (-r["score"], r.get("deadline") or "9999"))
    enriched = 0
    for row in rows:
        if enriched >= enrich_limit:
            break
        if row["decision"] in {"review", "maybe"} or "xr" in row.get("clusters", []):
            enrich(row)
            row.update(score_notice(row))
            enriched += 1

    rows.sort(key=lambda r: (-r["score"], r.get("deadline") or "9999"))
    return {
        "generated": date.today().isoformat(),
        "since": (date.today() - timedelta(days=days)).isoformat(),
        "source": BKMS_SEARCH,
        "notice_count": len(rows),
        "enriched": enriched,
        "review": [r for r in rows if r["decision"] == "review"],
        "maybe": [r for r in rows if r["decision"] == "maybe"],
        "skip": [r for r in rows if r["decision"] == "skip"],
        "errors": errors,
        "all": rows,
    }
