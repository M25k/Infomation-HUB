# Wöchentlicher Lost-Lead-Scan

Stand: 2026-08-31.

Ziel: in Gmail **stille Verkaufs- und Anfrage-Threads** finden und gegen die **heutigen** Fähigkeiten in diesem HUB halten. Ergebnis ist eine Wiederaufnahmeliste, kein zweiter Tiefenpass für Rechnungen oder Historie (das bleibt [gmail-pass.md](gmail-pass.md)).

**Betrieb:** lokal in diesem Chat bzw. im Agent, manuell, wöchentlich. Kein Auto-Versand, keine Cloud-Automation. Start: **„Starte den wöchentlichen Lost-Lead-Scan“** — das Skill [lost-leads](../.cursor/skills/lost-leads/SKILL.md) läuft dann durch. Letzter Lauf: [`knowledge/lost-leads/2026-08-31.md`](lost-leads/2026-08-31.md).

Mailbox: `joachim@northdocks.com`. Kein Passwort, Token oder 2FA-Code versionieren.

## Was wir suchen (Kompetenzfilter)

Nur Threads, bei denen Northdocks **heute** etwas Passendes liefern kann. Anker (nichts erfinden, nur diese Dateien):

| Linie | Was live / belastbar ist | Quelle |
|---|---|---|
| **FirefighterVR** | Funktionierendes Katalogprodukt: Koffer, Kauf/Miete, 23 Module | [strategy.md](strategy.md), [websites/firefightervr.md](websites/firefightervr.md) |
| **Meditrain** | Nächste Linie, Ziel Produktisierung als Koffer wie FFVR; kein Startup-Pitch 2024 | [strategy.md](strategy.md), [meditrain.md](meditrain.md) |
| **StrahlenschutzVR** | Schon Kauf/Miete (öffentlich: Miete ab 499 €/Woche, Kauf ab 3.499 €) | [meditrain.md](meditrain.md), [websites/strahlenschutzvr.md](websites/strahlenschutzvr.md), [claims.md](claims.md) |
| **Schockraum / Station / CPR** | Module existieren (Klinikprojekte bzw. CPR auch im FFVR-Paket) | [meditrain.md](meditrain.md) |
| **Hand aufs Herz** | Schul-CPR, Launch/Warteliste 2026; nicht das Klinik-Kofferprodukt | [websites/handaufsherz.md](websites/handaufsherz.md) |

Preise und Module nur in der Stufe aus [claims.md](claims.md) bzw. den öffentlichen Site-Briefs. Keine erfundenen Pakete.

## Was wir nicht wollen

Gelernt aus [gmail-pass.md](gmail-pass.md) und [accounting.md](accounting.md):

- `from:asana.com`, Vergabe-Newsletter, Promotions
- WordPress-Spam (`[Radiation Protection VR] Bitte moderiere`)
- Linode-Alerts (außer Team-Hinweis — der ist intern, kein Lead)
- Booking-/Apple-/Google-Promo
- Formspree-Wochen-Digest (kein Lead)
- 2FA-Codes
- Lieferanten-Inbound: Retouren, Scanner-Miete, ArborXR-Billing
- rein interne Threads (nur `@northdocks.com`)
- schon fakturiert — Abgleich [accounting.md](accounting.md)
- explizites Nein / verlorene Vergaben, die schon liegen (Mail 2024: Wunsiedel `24-L-0077-LRA`, Eichstätt `LRA-2024-MZ-1`)
- Partner-Threads **amatik**, solange nur der Partner spricht und der Endkunde nicht stillsteht

## Drei Slices

### A — Website-Formulare

Formspree / Betreff **„Neue Anfrage“** / **„New form submission“** von FirefighterVR, StrahlenschutzVR, Brandschutz-/Feuerlöscher-Landings, northdocks.com.

Stall: Formular da, **keine menschliche Northdocks-Antwort nach 14 Tagen**. Autoreply, Formspree-Bestätigung und Drafts zählen nicht als Antwort.

Startsuche (Gmail-Syntax, immer mit den Ausschlüssen oben):

```text
(from:formspree.io OR subject:"Neue Anfrage" OR subject:"New form submission") -from:asana.com -category:promotions -subject:digest
```

Kein Formspree-Spam-Dump. Ohne erkennbaren Produktbezug (FFVR, Strahlenschutz, Brandschutz/Löscher, GmbH-Kontakt) → Skip.

### B — Gesendete Angebote

Ausgang: Betreff **Angebot**, Dateinamen wie `202XXXXX-01` (PDF/Anhang). Stall: **keine spätere Rechnung** zu diesem Vorgang in [accounting.md](accounting.md).

```text
in:sent subject:Angebot has:attachment -from:asana.com
```

Angebotsnummer gegen den Rechnungsindex in accounting.md halten. Paid/Open-Rechnung zum selben Los = kein Lost Lead. Rejected-Estimates und schon notierte Absagen nicht neu aufwärmen.

### C — Externe Anfrage / Demo / Interesse

Threads mit externer Partei, deren **letzte menschliche Nachricht 45+ Tage** alt ist (Kunde oder Northdocks — Gespräch steht).

```text
(subject:Anfrage OR subject:Demo OR subject:Interesse) older_than:45d -from:asana.com -category:promotions
```

Nur echte Gesprächsfäden. Keine Newsletter, keine Portal-Benachrichtigungen.

`get_thread` immer mit `PLAIN_TEXT`. Drafts sind keine Fakten.

## Zwei Stapel

1. **Quiet** — das Gespräch ist tot. Wiederaufnahme ohne neue Produktlage (Erinnern, Status, gleicher Gegenstand).
2. **New ammo** — der Thread ist **älter** als eine Fähigkeit, die **jetzt** live ist. Beispiele nur aus dem HUB, nichts erfinden: FirefighterVR als laufendes Katalogprodukt; Meditrain als nächste Koffer-Linie; StrahlenschutzVR mit Kauf/Miete; Schockraum/Station/CPR vorhanden; Hand aufs Herz für Schulen. Winkel nur, wenn strategy/meditrain/websites die Fähigkeit tragen, und nur in der Evidenzstufe aus claims.md.

## Ablage

- Entscheidung: `knowledge/lost-leads/YYYY-MM-DD.md`
- Ordner: [lost-leads/](lost-leads/)

In der Laufdatei: Organisation (keine Privatadresse), letztes Datum, Stall-Grund, HUB-Match, Wiederaufnahme-Winkel, Gmail-Thread-ID. **Keine Kundentelefone**, keine Passwörter, keine Tokens.

**Keine Asana-Tasks** in diesem Scan (Asana-OAuth im Automations-Editor bricht ohne `client_id` — [tender-scan.md](tender-scan.md)). **Keine Kundenmail** senden oder entwerfen.

Kompetenzfilter vor Vollständigkeit: höchstens 5–7 „Reopen now“, dann Watch, dann Skip mit einer Zeile Grund.
