# Angebots-Paket (Standard ab Bielefeld 15.09.2026)

Vorbild: Uni Bielefeld `702-2026-10`. Google Docs im Drive-Ordner `01-Angebot` gelten vor den HTML-Erstentwürfen. Nutzer redigiert im Doc; das Doc nicht zurück in HTML schreiben.

## Dateien trennen

Eine HTML-Datei → ein Google Doc → eine Portal-Anlage. Nichts hinten anhängen.

| Datei | Ins Portal | Inhalt |
|---|---|---|
| **Inhaltliches Angebot** | ja | Briefkopf aus [northdocks-briefkopf.html](../../templates/northdocks-briefkopf.html), Anschreiben, Preis, Zahlungsplan, Liste der Anlagen, Unterschrift |
| **Projektkonzept / Lösungsbeschreibung** | ja | Nur die gewerteten Call-Abschnitte. Seitenlimit der Unterlagen (Bielefeld: 6 DIN-A4; Deckblatt/Inhaltsverzeichnis zählen nicht) |
| **Referenzen** | ja | Nur die verlangten Slots. Volumen dürfen auf volle Tausend Euro gerundet werden ([document-rules.md](../../../knowledge/document-rules.md) Nr. 15) |
| **Drittkomponenten / Lizenzen / Quellcode** | ja, wenn verlangt | **Lizenzregel NDFramework (Joachim 25.10.2026, laut UKFFM-Ticket; gleich im Meißen-Ticket):** Das NDFramework wird als vorbestehende Komponente offengelegt. Der Auftraggeber bekommt Rechte nur am neu Entwickelten; es gelten keine eigenen AGB; das Framework ist nicht Open Source. **Offen:** Eine Quellcode-Hinterlegung des Frameworks ist nicht belegt (#142). **Sprachausgabe (entschieden von One; Delegation durch Joachim 25.10.2026):** In Angeboten nur „Sprachausgabe“ nennen, ohne Anbieter; keine vertragliche Zusicherung zu ElevenLabs. Der Tarif wird erst im Auftragsfall geprüft (#141). |
| **Datenschutz / Informationssicherheit** | ja, wenn verlangt | |
| **Ausfüllhilfe** | **nein** | Eigenes Doc, Titel intern: PT-Kalkulation, Portal-Felder (324, 521, 533, EVB), Screenshot-Links |

## Konzept: was rausbleibt

Startet mit der ersten Call-Überschrift. **Kein** Vorspann.

Im gewerteten Konzept **nicht**:

- Briefkopf, HRB, USt-IdNr., Telefon, Kiel-Adresse, „Umfang: n Seiten“
- Personentage, Tagessatz, Gesamtsumme (Preis nur im Inhaltsangebot / Preisblatt)
- „Keine Unteraufträge / keine BG / keine Eignungsleihe“ (steht im Anschreiben)
- Schlusskatalog „Nicht Leistungsbestandteil: …“ — Grenze **einmal** im Anschreiben, nicht als Anhang am Konzept
- Internkasten, Förder-Vorgeschichte, Vorbefassungs-Warnungen, Programmnamen der AG-Förderung (z. B. Freiraum)

Wenn der Lehr-/Forschungsrahmen die Leistung erklärt: ein Satz, dass Northdocks die Software umsetzt und die **Hochschule Zuwendungsempfängerin bleibt** — ohne Förderliniennamen.

Hardware, Architektur, Drittkomponenten-Kurz und Risiken bleiben im Konzept, soweit der Call sie wertet.

## Anschreiben / Inhaltsangebot

Vollständiger Brief (Firma, AG-Adresse, Ort Datum). Custom vs. Katalog. Zielhardware. EVB/Bindefrist. Preis inkl. USt. und Skonto. Zahlungsplan, wenn das Preisblatt keine Phasen hat. Was eingereicht wird. Was nicht einschlägig ist (531/534). Unterschrift GF.

~~Leistungsgrenzen, die den Preis erklären, gehören **hierher**: Hardwarekauf nicht Preisblattposition; keine gesonderte Pflege nach Abnahme (gesetzliche Mängelhaftung bleibt).~~ **Überholt** durch die Inhaltsregel (Joachim 25.10.2026, 17:26, übermittelt von One): keine Negativ-Abgrenzungen, nur beschreiben, was angeboten wird ([document-rules.md](../../../knowledge/document-rules.md) Nr. 13).

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

Stephan zu Münster steht in diesem Raster **nicht** in der Konzepttabelle (weiter Eignung 3D/QA, Meißen). julia.barenthien: Konzeptzeile ja, wenn der Nutzer sie setzt oder das Bielefeld-Vorbild gilt; **nie** Eignung Teil 2, kein ND-Arbeitsverhältnis (GF 28.08.2026). Vor der nächsten Abgabe kurz nachfragen, wenn unsicher.

Nutzer ändert Namen im Doc → Doc gilt, nicht zurückkorrigieren.

PT und Tagessatz nur in der **Ausfüllhilfe**. Regel (Joachim 25.10.2026; Förderung 25.10.2026): Pro Ausschreibung wird **ein fester Tagessatz nach außen** auf Gewinnen kalkuliert; Puffer, Wiederverwendung und Marge bleiben intern. Keine allgemeine Beispielzahl.

**Keine Preisreferenz aus der Silas-Zeit (Joachim 26.10.2026 (über One)):** Ausschreibungen und Angebote, die Silas nach dem UKK-Projekt bearbeitet hat (Stichtag bestätigt: „nach UKK-Projekt (ca. 02.08.2023, letzte Meilensteinrechnung 20230802-01)“ (entschieden von One, Delegation Joachim 25.10.2026)), sind keine Preis- oder Kalkulationsreferenz. **Präzisiert (Joachim 26.10.2026 17:53 (über One)):** Ausgeschlossen sind **nur** Ausschreibungen und Angebote, die **Silas** nach dem UKK-Ende (ca. 02.08.2023) bearbeitet hat. Joachims eigene Kalkulationen 2026 (Meißen `2026-01-12.8.1.01`, Bielefeld `702-2026-10`, UKFFM `20261039`) gelten **weiter als Preisreferenz**. Vorgänge ohne Silas-Beteiligung bleiben gültig. Begründung (Joachim 26.10.2026, 17:54, über One): Silas-Preise waren nicht wettbewerbsfähig, auch nicht als Untergrenze verwenden; Wortlaut in proposal-playbook §0. Sonst wird auf den von Joachim vorgegebenen Betrag gerechnet. Regel und Liste: [proposal-playbook.md](../../../knowledge/proposal-playbook.md) §0, [grants.md](../../../knowledge/grants.md).

Belegtes Beispiel, **nur intern** (~~Vermerk 26.10.2026: fällt formal unter die Regel oben, nicht als Preisreferenz für andere Ausschreibungen verwenden~~ zurückgenommen: als Joachims eigene Kalkulation gilt UKFFM weiter als Preisreferenz, Joachim 26.10.2026 17:53 (über One)): Frankfurt 20261039, intern 900 €/PT plus 10 % Puffer (V2); Variante V3 mit 1.000 €/PT nach außen und 128 PT. Quelle: Sheet `1iDF_r_Rr1IDakNUBJgfFoZe1VRm4nolSDrSuOahG9FQ`. Frankfurt-Preis bis zur zweiten UKFFM-Ausschreibung nicht final.

## Portalformulare

Gelbe Felder der Originalformulare sind die Abgabe. Die Ausfüllhilfe listet Werte, ersetzt die PDFs nicht.
