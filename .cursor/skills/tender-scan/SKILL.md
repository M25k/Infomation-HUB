---
name: tender-scan
description: Weekly public-tender scan for Northdocks. Finds VgV/TED/service.bund.de notices that match XR training, Meditrain, FirefighterVR, factory safety, GodView twins, or command/Lagebild — and skips generic IT, tourism apps, and hardware-only buys. Use when the user starts the weekly Ausschreibungslauf, asks for matching public tenders, or says Tender-Scan / Ausschreibungen finden.
---

# Weekly tender scan

Find **öffentliche Ausschreibungen** that fit Northdocks. Not a dump of every VR mention.

## Start

1. Read this file, then [match.md](match.md).
2. Read [knowledge/tender-scan.md](../../knowledge/tender-scan.md), [knowledge/strategy.md](../../knowledge/strategy.md), [knowledge/expertise.md](../../knowledge/expertise.md).
3. Dedup against Asana project `1200346071931886` (Anträge & Ausschreibungen) and the latest file in `knowledge/tender-runs/`.
4. Run the **public APIs** (no portal passwords):

```text
python .cursor/skills/tender-scan/scripts/scan.py --days 8 --out knowledge/tender-runs/YYYY-MM-DD.json
```

This loads TED (EU-Schwelle), oeffentlichevergabe.de / BKMS (Bund/Länder/Kommunen inkl. Unterschwelle) and the service.bund.de RSS. Notice text is fetched for BKMS review/maybe hits. Source map: [portals.json](portals.json).

No extra packages. Do not put portal passwords, AVPQ access codes, or mailbox secrets into Git or the run file.

5. **Browser-Lücken** nach dem Script: die Portale unter `layers.browser` in portals.json mit denselben Keyword-Sets aus [knowledge/tender-scan.md](../../knowledge/tender-scan.md) öffnen (evergabe-online, DTVP, VMP NRW/Bayern/SH). Login-Portale nur mit den Daten aus dem Drive-Sheet, Passwort nicht in den Chat oder ins Repo. TED/BKMS ersetzen diese VMPs nicht vollständig unter der Schwelle.
6. Open every `review` hit (and borderline `maybe` with Meditrain/FFVR/GodView/XR-Software after reading the notice). Re-score with match.md. Script scores are titles + loaded description, still not the Leistungsverzeichnis. After the script: run the bund.de keyword URLs in [knowledge/tender-scan.md](../../knowledge/tender-scan.md) — the RSS is capped at 500 and misses VMP-NRW notices that the keyword search finds (Bielefeld 09/2026).
7. **Sofort Asana**, sobald der Treffer nach dem Lesen ein Kompetenz-Match ist — nicht erst nach einer späteren Runde. Vollständiges Bid/No-Bid-Raster aus [asana-ticket.md](asana-ticket.md). Unbekannte Felder = `offen`. **Eignung und Wertung nur aus der amtlichen Bekanntmachung / dem LV**, nicht aus Bidfix, Tender Impulse oder anderer „KI-Kriterien-Analyse“. Aggregatoren dürfen die URL finden, keine K.O.-Listen.
8. Write `knowledge/tender-runs/YYYY-MM-DD.md` and include the Asana-URL for every new ticket.
9. Do not create tasks for Horizon/EIC/KMU-Skizzen in this scan. Do not create tasks for Hard-Skip (Fahrzeuge, Bau, Tourismus-App, …).

Project `1200346071931886`, section **Sammlung** `1200346071931887`. Name: `Ausschreibung: {Titel}, Frist {YYYY-MM-DD}`. Due date = Angebotsfrist. Assignee `me` unless the user names someone else; add Patrick as follower (`732711459534815`).

## Output template

```markdown
# Tender-Scan YYYY-MM-DD

Fenster: TED + BKMS (oeffentlichevergabe.de) + bund.de-RSS der letzten 8 Tage; Browser-VMPs laut portals.json.
Neu in Asana: N
Nur notiert: N
Übersprungen (unpassend): N

## Bid-Kandidaten (Asana, volles Entscheidungsraster)

- Titel — Vergabestelle — Frist — Asana-URL

## Beobachtet, kein Task

- …

## Bewusst verworfen

- … (eine Zeile Grund)
```

## Hard rules

**Ticket und Paket (Joachim 25.10.2026, übermittelt von One bzw. Förderung):**
- Eine Ausschreibung bekommt **ein** Asana-Ticket mit grobem Status. Unteraufgaben nur für Dinge, die andere Personen tun müssen.
- Details stehen als `.md` im Drive-Ordner der Ausschreibung (inkl. Checkliste; eine Checkliste wird nie als Asana-Unteraufgaben angelegt). Die Ticketbeschreibung ist sauber gegliedert; Referenz: [UKSH-Ticket](https://app.asana.com/1/8864272155433/project/1200346071931886/task/1217328350929037).
- Referenzvolumen und ähnliche Zahlen dürfen auf volle Tausend Euro gerundet werden (document-rules.md Nr. 15, (Joachim 25.10.2026, über One)).
- So schnell wie möglich bearbeiten. Joachim bekommt einen kompletten Vorschlag in **einem** Paket: Eignung/Referenzen, Umsetzungskonzept (falls gefordert) und Kalkulation.
- Theoretische Punkte wie Konflikte bei den Mitarbeiterressourcen fallen ganz weg.
- **Keine Bieterfragen**, weil sie Wettbewerber aufmerksam machen. Ist eine Ausschreibung uneindeutig, gilt die für Northdocks günstigere Auslegung.
- **Preise so ansetzen, dass wir gewinnen:** ein fester Tagessatz nach außen; die interne Kalkulation (Puffer, Wiederverwendung, Marge) bleibt intern.
- **Keine Preisreferenz aus Ausschreibungen, die Silas nach dem UKK-Projekt (ca. 08/2023) bearbeitet hat**; gerechnet wird auf den Betrag, den Joachim vorgibt (Joachim 26.10.2026 (über One); Stichtag bestätigt: „nach UKK-Projekt (ca. 02.08.2023, letzte Meilensteinrechnung 20230802-01)“ (entschieden von One, Delegation Joachim 25.10.2026)). **Präzisiert (Joachim 26.10.2026 17:53 (über One)):** Ausgeschlossen sind **nur** Ausschreibungen und Angebote, die **Silas** nach dem UKK-Ende (ca. 02.08.2023) bearbeitet hat. Joachims eigene Kalkulationen 2026 (Meißen `2026-01-12.8.1.01`, Bielefeld `702-2026-10`, UKFFM `20261039`) gelten **weiter als Preisreferenz**. Vorgänge ohne Silas-Beteiligung bleiben gültig. Begründung (Joachim 26.10.2026, 17:54, über One): Silas-Preise waren nicht wettbewerbsfähig, auch nicht als Untergrenze verwenden; Wortlaut in proposal-playbook §0.

**Inhaltsregel (Joachim 25.10.2026, 17:26, übermittelt von One):** Leasing war nur für eine bestimmte UKSH-Ausschreibung gedacht und gehört nicht in normale Northdocks-Inhalte (Angebote, Tickets, Dokumente), auch nicht als Abgrenzung. Allgemein keine Negativ-Abgrenzungen nach dem Muster „das ist nicht X“: Wir beschreiben nur, was wir anbieten.


- Kompetenzfilter vor Vollständigkeit. Lieber 2 volle Entscheidungs-Tickets als 40 Treffer.
- GodView ist nicht die Headset-App.
- FirefighterVR-Katalog nicht in jeden Auftrag kippen.
- Ein Kompetenz-Match ohne Asana-Ticket gilt als unerledigt.
- Eignung/Wertung/ISO/Umsatzschwellen nicht aus kommerziellen Tender-KIs. Bielefeld 09/2026: Bidfix erfand ISO 9001, 500 k€ Umsatz und drei Refs >100 k€ — stand in keiner Unterlage.
- Zugangsdaten bleiben im Drive-Sheet der Task [Ausschreibungen / Förderung](https://app.asana.com/1/8864272155433/project/1200346071931886/task/1210459272235392). Niemals hierher kopieren.
