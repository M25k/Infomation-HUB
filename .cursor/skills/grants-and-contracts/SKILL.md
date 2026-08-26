---
name: grants-and-contracts
description: Writes Northdocks grant applications, tenders, eligibility sections, and contract texts from the repository knowledge base. Use when drafting Förderanträge, Ausschreibungen, Angebote, Eignung, Referenzen, Leistungsbeschreibungen, or Verträge for Northdocks GmbH.
---

# Grants and contracts

## Pflichtreihenfolge

1. Dieses Skill lesen.
2. [knowledge/document-rules.md](../../knowledge/document-rules.md) lesen.
3. Nur Claims verwenden, die in [knowledge/claims.md](../../knowledge/claims.md) stehen.
4. Vertikale aus [knowledge/verticals.md](../../knowledge/verticals.md), Projekte aus [knowledge/projects.md](../../knowledge/projects.md), Technik aus [knowledge/expertise.md](../../knowledge/expertise.md), Firma aus [knowledge/company.md](../../knowledge/company.md).
5. Offene Widersprüche in [knowledge/open-questions.md](../../knowledge/open-questions.md) **nicht** als Fakten formulieren.
6. Zuschlagssprache aus [knowledge/proposal-playbook.md](../../knowledge/proposal-playbook.md): Call-Text spiegeln, Eignung von Zuschlag trennen, Horizon-Kästen nicht vermischen.

## Was dieses Skill tut

Erzeugt Antrags- und Vertragstexte, die Northdocks als Bieter, Partner oder Auftragnehmer beschreiben. Es erfindet keine Referenzen, Umsätze, Kundenzahlen, Fördersummen oder Technikfähigkeiten.

## Was es nicht tut

- Keine Geheimnisse (Zugangscodes, Passwörter, interne Mailbox-Zugänge) in Dokumente oder Git schreiben.
- Keine Kundendaten veröffentlichen, die nicht ausdrücklich als referenzierbar markiert sind.
- Kein gesamtes FirefighterVR-Katalogversprechen in einen Auftrag kippen, wenn nur Komponenten gemeint sind.
- Keine Unteraufträge oder Eignungsleihe unterstellen, wenn der Auftrag das nicht vorsieht.

## Dokumenttypen

| Typ | Primärquellen |
|---|---|
| Eignung / Firmenprofil | company.md, claims.md, projects.md |
| Leistungsbeschreibung | expertise.md, verticals.md, repos.md |
| Referenzen | projects.md (nur Einträge mit Referenzstatus) |
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
- Herkunft: 2009 CAU Kiel, Fulldome→XR; nicht 17 Jahre FirefighterVR.
- Kundenclaim FirefighterVR: **>100 Kunden** darf in Eignung stehen. Interne Historie „alte Plattform gescheitert“ nie nach außen.

## Checkliste vor Abgabe

- [ ] Firma, HRB, USt-IdNr. stimmen mit company.md
- [ ] Jede Zahl hat eine Quelle in claims.md
- [ ] Referenzen haben Auftraggeber, Zeitraum, Gegenstand
- [ ] Technik-Stack stimmt mit repos.md (keine erfundenen Engines)
- [ ] Playbook: Call-Text gespiegelt, Eignung ≠ Zuschlag, Horizon-Kästen getrennt
- [ ] Keine Secrets, keine unfreigegebenen Kundentelefonnummern in öffentlichen Anhängen
