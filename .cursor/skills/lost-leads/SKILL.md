---
name: lost-leads
description: Weekly Gmail scan for stalled Northdocks sales and inquiry threads, then match against current HUB capabilities. Builds a re-engagement list — not a fact mine and not an invoice history pass. Use when the user starts the weekly Lost-Lead-Scan, asks for lost leads, or says verlorene Leads / „Starte den wöchentlichen Lost-Lead-Scan“.
---

# Weekly lost-lead scan

Find **stille Verkaufs- und Anfrage-Threads**, die zu heutigen Northdocks-Fähigkeiten passen. Kein Dump der Mailbox, kein zweiter [gmail-pass](../../knowledge/gmail-pass.md).

## Start

1. Dieses File lesen, dann [knowledge/lost-leads.md](../../knowledge/lost-leads.md).
2. Danach [knowledge/strategy.md](../../knowledge/strategy.md), [knowledge/expertise.md](../../knowledge/expertise.md), [knowledge/meditrain.md](../../knowledge/meditrain.md), [knowledge/accounting.md](../../knowledge/accounting.md), [knowledge/gmail-pass.md](../../knowledge/gmail-pass.md), [knowledge/claims.md](../../knowledge/claims.md) und die Briefs unter [knowledge/websites/](../../knowledge/websites/README.md).
3. Dedup gegen die neueste Datei in `knowledge/lost-leads/` (falls vorhanden). Schon gelistete Threads nur neu führen, wenn sich Stall oder HUB-Match geändert hat.
4. Mailbox **`joachim@northdocks.com`** per Gmail-MCP (`search_threads`, danach `get_thread` mit **`PLAIN_TEXT`**). Drei Slices aus [knowledge/lost-leads.md](../../knowledge/lost-leads.md). Filter von gmail-pass.md immer mitlaufen. Drafts sind keine Fakten.
5. Jeden Kandidaten gegen [knowledge/accounting.md](../../knowledge/accounting.md) prüfen: schon fakturiert = kein Lost Lead. Partner-Threads (amatik) nur, wenn der **Endkunde** stillsteht.
6. Zwei Stapel bilden: **Quiet** (Gespräch tot) und **New ammo** (Thread älter als eine Fähigkeit, die laut strategy/meditrain/websites **jetzt** live ist). Nur behaupten, was in `knowledge/` steht, und nur in der Evidenzstufe aus [knowledge/claims.md](../../knowledge/claims.md).
7. Schreiben: `knowledge/lost-leads/YYYY-MM-DD.md`. Kompetenzfilter vor Vollständigkeit: höchstens **5–7** „Reopen now“.

Keine Asana-Tasks in diesem Scan (Asana-OAuth im Automations-Editor ohne `client_id` — wie in [tender-scan.md](../../knowledge/tender-scan.md)). Keine Kundenmail senden, keine Entwürfe anlegen.

## Output template

```markdown
# Lost-Lead-Scan YYYY-MM-DD

Mailbox: joachim@northdocks.com
Fenster: Slice A (Formulare, 14 Tage ohne ND-Antwort) / Slice B (gesendete Angebote ohne spätere Rechnung) / Slice C (externe Anfrage/Demo/Interesse, letzte menschliche Mail 45+ Tage)
Reopen now: N
Watch: N
Skip: N

## Reopen now (max. 5–7)

### {Organisation oder Absender-Domain}
- Letztes Datum:
- Stall: {Slice + warum still}
- HUB-Match: {Produkt/Modul laut knowledge/, mit Datei}
- Winkel: {ein Satz, nur belegte Fähigkeit}
- Stapel: Quiet | New ammo
- Thread: {Gmail-Thread-ID}

## Watch

- Organisation — letzte Date — eine Zeile warum warten — Thread-ID

## Skip

- … (eine Zeile Grund)
```

## Hard rules

- Der HUB ist kanonisch. Gmail ist eine Quelle.
- Lieber 5 echte Wiederaufnahmen als 40 Treffer.
- Kein Formspree-Spam-Dump. Weekly-Digest von Formspree ist kein Lead.
- Gewonnenes / fakturiertes (accounting.md) ist kein Lost Lead.
- Nie senden, nie Entwürfe. Nie Passwörter, Tokens, Kundentelefone, 2FA-Codes ins Git oder in die Laufdatei.
- Keine erfundenen Preise, Module oder Claims. New ammo nur, wenn die Datei in `knowledge/` die Fähigkeit **heute** trägt.
