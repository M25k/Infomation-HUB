---
name: grants-and-contracts
description: Writes Northdocks grant applications, tenders, eligibility sections, and contract texts from the repository knowledge base. Use when drafting Förderanträge, Ausschreibungen, Angebote, Eignung, Referenzen, Leistungsbeschreibungen, or Verträge for Northdocks GmbH.
---

# Grants and contracts

## Pflichtreihenfolge

1. Dieses Skill lesen.
2. [knowledge/document-rules.md](../../knowledge/document-rules.md) lesen.
3. Nur Claims verwenden, die in [knowledge/claims.md](../../knowledge/claims.md) stehen.
4. Vertikale aus [knowledge/verticals.md](../../knowledge/verticals.md). Produktpriorität: FirefighterVR (läuft) und Meditrain ([knowledge/strategy.md](../../knowledge/strategy.md), [knowledge/meditrain.md](../../knowledge/meditrain.md)).
5. Offene Widersprüche in [knowledge/open-questions.md](../../knowledge/open-questions.md) **nicht** als Fakten formulieren.
6. Zuschlagssprache aus [knowledge/proposal-playbook.md](../../knowledge/proposal-playbook.md): Call-Text spiegeln, Eignung von Zuschlag trennen, Horizon-Kästen nicht vermischen.
7. Umsatz oder Referenzvolumen: wenn FreeAgent-MCP da ist, gegen die Bücher prüfen ([knowledge/accounting.md](../../knowledge/accounting.md)), dann `claims.md` / `projects.md`. Keine erfundenen GJ-Zahlen. MCP fehlt: nur die bestehenden Claims.

## Was dieses Skill tut

Erzeugt Antrags- und Vertragstexte, die Northdocks als Bieter, Partner oder Auftragnehmer beschreiben. Es erfindet keine Referenzen, Umsätze, Kundenzahlen, Fördersummen oder Technikfähigkeiten.

Öffentliche Ausschreibungen **suchen** (nicht schreiben): Skill [tender-scan](../tender-scan/SKILL.md), wöchentlich startbar.

Website-Copy und IA: Skill [website-content](../website-content/SKILL.md), Briefs unter [knowledge/websites/](../../knowledge/websites/README.md). Intern belegte Eignungssätze nicht ungefragt auf Live-Sites heben.

## Konkrete Ausschreibung (nicht der Wochen-Scan)

Start im Chat: **„Wir machen die Ausschreibung {Name oder URL}“** (oder Asana-Link). Das ist Schreiben, nicht Suchen.

| Schicht | Was dort liegt | Was nicht |
|---|---|---|
| **Asana** Board [Anträge & Ausschreibungen](https://app.asana.com/1/8864272155433/project/1200346071931886) | Entscheidungsakte: Bid/No-Bid-Raster aus [asana-ticket.md](../tender-scan/asana-ticket.md), Frist, Los, Portal-URL, Link zum Drive-Ordner. Spalte **Sammlung** bis zur Teilnahme-Entscheidung, dann **Eingereicht** / **Nicht eingereicht**. | Keine PDFs, keine Passwörter, kein AVPQ-Code. Kommentare nur Klartext. |
| **Drive** Ordner [001 Teilnahme](https://drive.google.com/drive/folders/1uHMr8flT_jj4tRFy4mxbcuk2dbTwegKU) (`01 Administration / 03 Förderungen+Ausschreibungen / 001 Teilnahme`) | Unterlagen, LV, Eignungsentwürfe, Preise, eingereichte Dateien. Pro Vorgang ein Unterordner `{Aktenzeichen oder Kurzname}` (Muster: `UKSH-Föd-2026-0001`). | Nichts davon ins Git. |
| **FreeAgent** | Live-Bücher: Rechnungen, Kontakte, P&L. Destillat: [knowledge/accounting.md](../../knowledge/accounting.md). | Keine Tokens, IBANs, Lohnzeilen, keine Schreib-Tools (create/send/delete). |
| **Information-HUB (Git)** | Wiederverwendbare Firma: `claims.md`, `projects.md`, `expertise.md`, `accounting.md`. Nach Einreichung **eine Zeile** in [knowledge/grants.md](../../knowledge/grants.md) plus Asana- und Drive-Link. | Keine Ausschreibungs-PDFs, keine Portal-Logins, keine Kundentelefone. |

Ablauf: (1) Asana-Task prüfen oder anlegen. (2) Unterlagen in den Drive-Unterordner. (3) Texte mit diesem Skill aus der KB, Call-Text aus Drive/Portal spiegeln. (4) Abgabe im Portal; Mailbox `ausschreibungen@northdocks.com`. (5) grants.md kurz nachziehen.

Eignung, Wertung und K.O.-Listen nur aus den amtlichen Unterlagen im Drive/Portal. Bidfix und ähnliche Tender-KIs nicht zitieren (Bielefeld 09/2026: erfundene ISO 9001).

## Was es nicht tut

- Keine Geheimnisse (Zugangscodes, Passwörter, interne Mailbox-Zugänge) in Dokumente oder Git schreiben.
- Keine Kundendaten veröffentlichen, die nicht ausdrücklich als referenzierbar markiert sind.
- Kein gesamtes FirefighterVR-Katalogversprechen in einen Auftrag kippen, wenn nur Komponenten gemeint sind.
- Keine Unteraufträge oder Eignungsleihe unterstellen, wenn der Auftrag das nicht vorsieht.

## Dokumenttypen

| Typ | Primärquellen |
|---|---|
| Eignung / Firmenprofil | company.md, claims.md, projects.md, accounting.md (Umsatz/Rechnungen gegen FreeAgent) |
| Leistungsbeschreibung | expertise.md, verticals.md, repos.md |
| Referenzen | projects.md (nur Einträge mit Referenzstatus). Historisches Inventar: [history.md](../../knowledge/history.md) — Task-Zahlen keine Volumina, nicht ungeprüft in Eignung |
| Forschungsantrag | grants.md + expertise.md + proposal-playbook.md |
| Angebot / Vertrag | document-rules.md + proposal-playbook.md + das konkrete Los |

## Formulierungsregeln

- Rechtsträger immer **Northdocks GmbH**, Marken (FirefighterVR, MeditrainVR, GodView, …) als Marken der GmbH.
- Sitz: Niederstraße 18, 40789 Monheim am Rhein. Umsetzungsstandort nur nennen, wenn er für den Auftrag stimmt (oft Kiel).
- Öffentliche Claims: Website/Impressum. Interne Zahlen: Drive/Asana, nicht auf die Website kopieren.
- Vertikale: immer die **sieben öffentlichen** von northdocks.com. Das Business Deck mit fünf Vertikalen ignorieren.
- FirefighterVR-URL: **https://firefightervr.de/**. `firefightervrmobile.de` nur erwähnen, wenn der Auftrag die Domain verlangt.
- GodView: zwei Kundentypen (Bauinspektion vs. Einsatz/Playground), nie als Headset-App.
- Spot-KI: nur KI-Transfer-Hub SH, nie Vodafone oder UKK.
- Dom-Erfassung: 100.000+ Fotos und 1.000 Laserscans; nicht 30.000.
- Meditrain: Vertical der GmbH, Ziel **Koffer + Hardware/Software-Komplettpaket** wie FirefighterVR. Pitch 2024 (Ausgründung) nicht verwenden. Nicht behaupten, Meditrain habe schon 100 Klinik-Kunden.
- Kundenclaim FirefighterVR: **>100 Kunden** darf in Eignung stehen. Alte Linie: PCVR-Launcher, eingestellt nach Kundenfeedback (zu teuer/kompliziert), Nachfolger ist der Koffer. Nicht „gescheitert“ nach außen.
- Spearhead: Auftraggeber **The Marketing Arm (TMA)**, Omnicom, für National-Guard-Trainings; plus Playground-Kosovo. Keine Site-Zahlen, kein pauschales US Army, National Guard nicht als Vertragspartner.
- Kein DFV, wenn nur WFVD/vfdb auf der Site stehen.
- RWE/Framatome: FFVR-Feuerlöscher, Factory nur als Randfall (Sprinklerwartung).
- Großkunden (Currenta, Merck, …): FA-**Gesamtsumme** erlaubt. Trotzdem oft getrennte Workstreams/Ansprechpartner — nicht als ein Projekt. UKSH-Mappe Currenta ca. 20 k€ nicht umschreiben.
- ElevenVoice: intern Standard-TTS der meisten XR-Sprachen. Nicht für Fulldome-Shows und nicht für VR-Stadttouren. Nicht als Website-Feature.
- Kontakt immer **kontakt@northdocks.com**.
- BMA Trainer nicht vermarkten, nicht als FFVR-Modul.
- Umsatz: Eignungsschwelle >200 k€; intern vage ca. 1 Mio. € p.a. **FreeAgent-Verkaufszahlen gelten.** Fördermittel nur [grants.md](../../knowledge/grants.md), nicht auf FA legen. Alte Mappen-Zahlen (UKK 380 k, Trier 80 k, TMA 25 k USD) nicht verwenden.
- julia.barenthien nicht als Northdocks-Personal oder in Eignung Teil 2. Expertise intern bei Bedarf (Arbeitgeber F&E GmbH Kiel).
- Reschke Productions GmbH: interne Verrechnung, nie als Kunde, Referenz oder Eignung.

## Checkliste vor Abgabe

- [ ] Firma, HRB, USt-IdNr. stimmen mit company.md
- [ ] Jede Zahl hat eine Quelle in claims.md
- [ ] Umsatz/Referenzvolumen gegen [accounting.md](../../knowledge/accounting.md) / FreeAgent, nicht erfunden
- [ ] Referenzen haben Auftraggeber, Zeitraum, Gegenstand
- [ ] Technik-Stack stimmt mit repos.md (keine erfundenen Engines)
- [ ] Playbook: Call-Text gespiegelt, Eignung ≠ Zuschlag, Horizon-Kästen getrennt
- [ ] Keine Secrets, keine unfreigegebenen Kundentelefonnummern in öffentlichen Anhängen
