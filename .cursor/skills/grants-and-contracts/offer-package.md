# Angebots-Paket (Standard ab UKFFM 02.11.2026)

**Basis für alle zukünftigen Ausschreibungen.** Vorbilder: Uni Bielefeld `702-2026-10` (Inhalts- und Dateischnitt) und UKFFM `20261039` / `20261040` (Drive-Ordnerstruktur, Abgabe vs. Intern). Entscheidung Joachim 02.11.2026.

Google Docs im Drive gelten vor HTML-Erstentwürfen. Nutzer redigiert im Doc; das Doc nicht zurück in HTML schreiben. Nichts aus dem Angebotsordner ins Git.

## Drive-Ordner je Verfahren

Unter `001 Teilnahme / {Aktenzeichen oder Kurzname}` immer diese Struktur anlegen (Namen fest):

| Ordner | Zweck | Ins Portal |
|---|---|---|
| **`00-Unterlagen`** | Amtliche Vergabeunterlagen, Bekanntmachung, Bieterinfos (Read-only-Ablage) | nein |
| **`01-Arbeit-Entwuerfe`** | Alte Versionen, Entwürfe, überholte Ausfüllhilfen. Nicht einreichen. | nein |
| **`03-Abgabe`** | **Nur** einreichungsfertige Docs. Positiv formuliert, ohne interne Erklärblöcke, ohne Versions-Meta. | **ja** (Inhalt) |
| **`99-Intern`** | Portal-Ausfüllhilfe (Feldwerte, Kriterienkatalog-Kreuze, EVB-Hilfe), interne Notizen fürs Cockpit | **nein** |
| **`Nachweise-auf-Verlangen`** | AVPQ, Handelsregister, Policen, Qualifikationsnachweise. Bereitgehalten, nur hochladen wenn verlangt oder ausdrücklich mit einzureichen. | nur auf Verlangen / wenn gefordert |
| **`01-Angebot`** (oder gleichwertig neben den Nummern) | Preiskalkulation (Sheets), Preisblatt-Arbeitsfassung, Entscheidungen_und_Annahmen.md | nein (Preisblatt-Portal separat ausfüllen) |

Asana-Ticket verlinkt mindestens: Akte-Root, `03-Abgabe`, `99-Intern`, `Nachweise-auf-Verlangen`. Ticketbeschreibung: grober Status, Frist, Preis, Offen-Liste. Details und Checklisten als `.md` im Drive, nicht als Asana-Unteraufgaben-Wälder.

Nach Einreichung: Abgabebeleg und Portal-Zusammenfassung in die Akte; eine Zeile in [grants.md](../../../knowledge/grants.md).

## Inhalt von `03-Abgabe`

Eine Datei → ein Google Doc → eine Portal-Anlage. Nichts hinten anhängen. Nur was der Call verlangt; fehlende Call-Positionen weglassen, nicht erfinden.

| Datei | Ins Portal | Inhalt |
|---|---|---|
| **Inhaltliches Angebot** | ja | Briefkopf aus [northdocks-briefkopf.html](../../templates/northdocks-briefkopf.html), Anschreiben, Preis, Zahlungsplan falls nötig, Liste der Anlagen, Unterschrift |
| **Umsetzungskonzept / Lösungsbeschreibung** | ja | Nur die gewerteten Call-Abschnitte. Seitenlimit der Unterlagen einhalten (Bielefeld: 6 DIN-A4; Deckblatt/Inhaltsverzeichnis zählen nicht) |
| **Referenzen** | ja | Nur die verlangten Slots. Kontakte und Telefon aus der KB ([people.md](../../../knowledge/contacts/people.md), [claims.md](../../../knowledge/claims.md)), sofern freigegeben. Volumen auf volle Tausend Euro rundbar ([document-rules.md](../../../knowledge/document-rules.md) Nr. 15) |
| **Projektteam / Schlüsselpersonen** | ja, wenn verlangt | Eigenes Doc oder Abschnitt nach Call; Rollen **dieses** Auftrags |
| **EVB-IT / Drittkomponenten / Lizenzen / Quellcode** | ja, wenn verlangt | **Lizenzregel NDFramework (Joachim 25.10.2026):** vorbestehende Komponente offenlegen; Rechte nur am neu Entwickelten; keine eigenen AGB; Framework nicht Open Source. **Offen:** Quellcode-Hinterlegung des Frameworks (#142). **Sprachausgabe (entschieden von One; Delegation Joachim 25.10.2026):** nur „Sprachausgabe“, ohne Anbieter; keine vertragliche Zusicherung zu ElevenLabs (#141) |
| **Datenschutz / Informationssicherheit** | ja, wenn verlangt | |
| **Beispiel-Export** (JSON/CSV o. Ä.) | ja, wenn verlangt | Maschinenlesbares Beispiel zum Logging/Export-Konzept |
| **Ausfüllhilfe** | **nein** | Liegt in `99-Intern`, nicht in `03-Abgabe` |

## Textregeln für Abgabe-Docs

- Leserbezug: [reader-facing-prose.mdc](../../rules/reader-facing-prose.mdc). Keine Abgrenzungs-Sätze („nicht der Fokus …“), kein Revisions-Meta („gegenüber Entwurf v2 …“).
- Typografie DE: [german-prose.mdc](../../rules/german-prose.mdc).
- Bekannte HUB-/Website-Kontakte und Firmentelefone einsetzen; keine Platzhalter, wenn die KB den Wert hat.
- Interne Begründung, Annahmen-IDs, Freigabepunkte F1–Fn nur in `01-Angebot` / `99-Intern`, nie in `03-Abgabe`.

## Konzept: was rausbleibt

Startet mit der ersten Call-Überschrift. **Kein** Vorspann.

Im gewerteten Konzept **nicht**:

- Briefkopf, HRB, USt-IdNr., Telefon, Kiel-Adresse, „Umfang: n Seiten“
- Personentage, Tagessatz, Gesamtsumme (Preis nur im Inhaltsangebot / Preisblatt)
- „Keine Unteraufträge / keine BG / keine Eignungsleihe“ (steht im Anschreiben)
- Schlusskatalog „Nicht Leistungsbestandteil: …“ — Grenze nur wenn das amtliche Formular ein Out-of-scope-Feld verlangt, sonst weglassen ([document-rules.md](../../../knowledge/document-rules.md) Nr. 13)
- Internkasten, Förder-Vorgeschichte, Vorbefassungs-Warnungen, Programmnamen der AG-Förderung (z. B. Freiraum)

Wenn der Lehr-/Forschungsrahmen die Leistung erklärt: ein Satz, dass Northdocks die Software umsetzt und die **Hochschule Zuwendungsempfängerin bleibt** — ohne Förderliniennamen.

Hardware, Architektur, Drittkomponenten-Kurz und Risiken bleiben im Konzept, soweit der Call sie wertet.

## Anschreiben / Inhaltsangebot

Vollständiger Brief (Firma, AG-Adresse, Ort Datum). Custom vs. Katalog. Zielhardware. EVB/Bindefrist. Preis inkl. USt. und Skonto. Zahlungsplan, wenn das Preisblatt keine Phasen hat. Was eingereicht wird. Unterschrift GF.

Nur beschreiben, was angeboten wird. Keine Negativ-Abgrenzungen ([document-rules.md](../../../knowledge/document-rules.md) Nr. 13; Joachim 25.10.2026).

Nicht ins Anschreiben: Förderprogrammnamen der AG, Internkalkulation, Portal-Feldlisten.

## Personaltabelle im Konzept

Zuschlag = Rollen **dieses** Auftrags, nicht 1:1 Eignung Teil 2 ([team.md](../../../knowledge/team.md)).

**Vorbild Bielefeld 15.09.2026 (Nutzer-Doc):**

| Rolle | Person |
|---|---|
| Projektleitung | Patrick D. Reschke |
| Technische Projektleitung | Joachim Perschbacher |
| Senior VR-Entwicklung | Finn Marquardt |
| Unreal-Entwicklung | Marcel Timm |
| 3D / QA | Renke Niehaus |
| UX / QA | Seiko Foubert |
| Didaktik | Julia Barenthien |

Stephan zu Münster steht in diesem Raster **nicht** in der Konzepttabelle (weiter Eignung 3D/QA, Meißen; bei UKFFM zusätzlich benannt). Renke in Angeboten als **3D-Integration**, Medienpädagogik nur bei Bedarf. julia.barenthien: Konzeptzeile ja, wenn der Nutzer sie setzt oder das Bielefeld-Vorbild gilt; **nie** Eignung Teil 2, kein ND-Arbeitsverhältnis (GF 28.08.2026). Vor der nächsten Abgabe kurz nachfragen, wenn unsicher.

Nutzer ändert Namen im Doc → Doc gilt, nicht zurückkorrigieren.

PT und Tagessatz nur in der **Ausfüllhilfe** / Kalkulation. Regel (Joachim 25.10.2026): Pro Ausschreibung **ein fester Tagessatz nach außen**; Puffer, Wiederverwendung und Marge bleiben intern.

**Keine Preisreferenz aus der Silas-Zeit:** Details [proposal-playbook.md](../../../knowledge/proposal-playbook.md) §0, [grants.md](../../../knowledge/grants.md). Joachims Kalkulationen 2026 (Meißen, Bielefeld, UKFFM) bleiben gültige Preisreferenz.

Belegtes Beispiel intern (UKFFM, Stand Variante B 02.11.2026): Tagessatz **900 €/PT**, Skonto ÷ 0,97, Escrow einmalig 3.600 €, Pflege 1.200 €/Monat. Triage `20261039`: 130.405 € netto. Schockraum `20261040`: 156.384 € netto.

## Portalformulare

Gelbe Felder der Originalformulare sind die Abgabe. `99-Intern` listet Werte, ersetzt die PDFs nicht. Bietercockpit/Upload macht Joachim; Agent bereitet Werte und Links vor.
