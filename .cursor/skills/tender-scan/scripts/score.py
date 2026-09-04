"""Shared first-pass scoring for TED, BKMS and bund.de hits.

The weekly skill still re-reads the notice. This is only the machine filter.
"""

from __future__ import annotations

import re

POSITIVE = {
    "xr": (
        r"\bvr\b",
        r"virtual[ -]?reality",
        r"virtuelle[rn]?[ -]?realit",
        r"augmented reality",
        r"extended reality",
        r"\bxr\b",
        r"immersiv",
        r"headset",
        r"openxr",
        r"simulationstrain",
        r"trainingssimulation",
        r"vr-train",
        r"vr train",
        r"vr-brille",
        r"vr brille",
        r"lernmodul",
    ),
    "meditrain": (
        r"medizin",
        r"klinik",
        r"krankenhaus",
        r"uniklinik",
        r"rettung",
        r"notfall",
        r"schockraum",
        r"strahlenschutz",
        r"reanimation",
        r"cpr\b",
        r"pflege",
        r"patientensim",
        r"sanit[äa]ter",
        r"rettungsdienst",
    ),
    "firefighter": (
        r"feuerwehr",
        r"brandschutz",
        r"brandschutzerziehung",
        r"werkfeuer",
        r"katastrophenschutz",
        r"thw\b",
        r"bos\b",
        r"flashover",
        r"l.schangriff",
        r"einsatztrain",
    ),
    "factory": (
        r"arbeitssicherheit",
        r"chempark",
        r"chemiepark",
        r"fabrik",
        r"industrieanlage",
        r"verfahrenstechnik",
        r"anlagensicherheit",
        r"psa\b",
    ),
    "twin": (
        r"digital(?:er)? twin",
        r"digitaler zwilling",
        r"photogrammetr",
        r"punktwolke",
        r"laserscan",
        r"3d[- ]?(?:modell|mesh|tiles|erfassung)",
        r"drohne",
        r"bestandsdokumentation",
        r"bauinspektion",
        r"denkmal",
        r"orthofoto",
        r"cesium",
    ),
    "command": (
        r"lagebild",
        r"f.hrungsunterst.tzung",
        r"einsatzleitung",
        r"kommandozentrale",
        r"common operational picture",
        r"\bcop\b",
        r"planspiel",
        r"playground",
    ),
}

HARD_SKIP = (
    r"erlebnis-?app",
    r"gartenausstellung",
    r"stadtführung",
    r"stadtfuehrung",
    r"museumsp.dagog",
    r"tourist",
    r"website[- ]relaunch",
    r"\bsap\b",
    r"microsoft 365",
    r"office 365",
    r"content[- ]management",
    r"sozialplattform",
    r"schulbuch",
    r"feuerwehrfahrzeug",
    r"gefahrgutzug",
    r"hausfeuerwehr",
    r"rettungss[aä]t",
    r"hydraulisch.{0,20}rettung",
    r"spreizer",
    r"sanit.reinrichtung",
    r"neubau .{0,40}ausbildungszentrum",
)

WANTED_TYPES = {
    "cn-standard",
    "cn-social",
    "cn-desg",
    "pin-cfc-standard",
    "pin-cfc-social",
    "pin-buyer",
    "",  # bund.de RSS has no TED notice-type
}

NEAR_COUNTRIES = {"DEU", "DE", "DNK", "AUT", "NLD", "BEL", "LUX"}


def pick_text(value) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        return " ".join(pick_text(v) for v in value)
    if isinstance(value, dict):
        if "value" in value and "languageId" in value:
            return str(value.get("value") or "")
        for lang in ("deu", "de", "DEU", "eng", "en", "ENG"):
            if lang in value:
                return pick_text(value[lang])
        return " ".join(pick_text(v) for v in value.values())
    return str(value)


def score_notice(notice: dict) -> dict:
    blob = " ".join(
        [
            notice.get("title", ""),
            notice.get("buyer", ""),
            notice.get("cpv", ""),
            notice.get("notice_type", ""),
            notice.get("description", ""),
            notice.get("lot_title", ""),
        ]
    ).lower()
    notice_type = (notice.get("notice_type") or "").strip()
    reasons_skip = [pat for pat in HARD_SKIP if re.search(pat, blob, re.I)]
    if notice_type and notice_type not in WANTED_TYPES:
        reasons_skip.append(f"notice-type:{notice_type}")
    clusters = []
    for name, pats in POSITIVE.items():
        if any(re.search(pat, blob, re.I) for pat in pats):
            clusters.append(name)
    points = 0
    if "xr" in clusters:
        points += 40
    for extra in ("meditrain", "firefighter", "factory", "twin", "command"):
        if extra in clusters:
            points += 20
    country = (notice.get("buyer_country") or "").upper()
    if country in NEAR_COUNTRIES or notice.get("source") in {"bkms", "bund.de"}:
        points += 10
    if reasons_skip:
        points = min(points, 25)
        decision = "skip"
    elif points >= 70:
        decision = "review"
    elif points >= 40:
        decision = "maybe"
    else:
        decision = "skip"
    return {
        "score": min(points, 100),
        "clusters": clusters,
        "decision": decision,
        "skip_reasons": reasons_skip,
    }
