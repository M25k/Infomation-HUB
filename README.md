# Information HUB — Northdocks Wissens- und Skill-Basis

Interne Grundlage für **Förderanträge, Ausschreibungen und Verträge**.  
Stand der ersten Recherche: 2026-08-26. Letzter Quellenabgleich: **2026-10-05** ([research-log.md](knowledge/research-log.md) Pass 70).

Dieses Repository ist die kanonische Quelle für Formulierungen, Referenzen, Technik-Claims und Projektgeschichte. Öffentliche Websites, Asana, Google Drive, FreeAgent und die lokalen Git-Repos sind **Quellen**, nicht die Endfassung.

## Für Agenten

Beim Schreiben von Anträgen, Angeboten oder Verträgen zuerst das Skill lesen:

- [`.cursor/skills/grants-and-contracts/SKILL.md`](.cursor/skills/grants-and-contracts/SKILL.md)

Beim **Anpassen von Websites** (Copy, IA, Claims, Canonical-Links):

- [`.cursor/skills/website-content/SKILL.md`](.cursor/skills/website-content/SKILL.md)
- Briefs: [knowledge/websites/](knowledge/websites/README.md)

Wöchentliche **öffentliche Ausschreibungen** (nur Kompetenz-Match):

- [`.cursor/skills/tender-scan/SKILL.md`](.cursor/skills/tender-scan/SKILL.md)
- Startsatz: „Starte den wöchentlichen Ausschreibungs-Scan“
- Ablauf und Filter: [knowledge/tender-scan.md](knowledge/tender-scan.md)

Dann die Wissensdateien unter [`knowledge/`](knowledge/).

### Arbeitsregeln für Bots

- **Datenzugriff in Firmenkonten** („we need to chnage this. all company accounts are fine to acces data move and edit it.“ (Joachim 29.10.2026 09:06 direkt im Chat von One); „only thing that is imprted publik or external sharing“ (Joachim 29.10.2026 09:07 direkt im Chat von One)): Bots dürfen in allen Northdocks-Firmenkonten auf Daten zugreifen, sie verschieben und bearbeiten, ohne den Eigentümer zu fragen. Joachims OK braucht nur das Öffentlichmachen oder externe Teilen. ~~Löschen ist im Wortlaut nicht ausdrücklich genannt; das und die Geltung für Finanz-/Personal-Ordner und den Bielefeld-Angebotsordner klärt [#169](knowledge/assets/open-questions.md).~~ Präzisiert „1. yes delete mean move to bin 2. bids are fine finances not“ (Joachim 29.10.2026 09:12 direkt im Chat von One, Antwort auf Ones Rückfrage zu Löschen und zu Finanz-, Personal- und Bielefeld-Ordnern): **Löschen** ist erlaubt, aber nur in den Papierkorb. **Angebots- und Ausschreibungsordner** (auch Bielefeld) sind freigegeben. **Finanzordner** bleiben tabu. **Personalordner** bleiben nach der bisherigen Regel tabu (dazu keine Aussage Joachims). **Externes Teilen und Veröffentlichen** braucht weiter Joachims OK ([#169](knowledge/assets/open-questions.md), geschlossen). Die Tabu-Liste ([tabu.md](knowledge/assets/tabu.md)) bleibt unverändert; sie regelt Öffentlichkeit und Nutzung, nicht den Zugriff.
- **Fail fast** (Weekly 28.10.2026, 00:25:22–00:27:02, laut One; W1028-21): Früh an Grenzen gehen, statt lange festzustecken. Bei einer Blockade das Prozesswissen (z. B. die Agent-MD-Datei) an ein anderes LLM geben und einen frischen Ansatz machen lassen; Ergebnisse vergleichen, LLMs auch gegeneinander antreten lassen. Vertraulichkeitsregeln dieses Repos gelten dabei weiter.
- **Nur eigene oder umbaubare Tools** (Weekly 28.10.2026, 00:36:18–00:36:54, laut One; W1028-28): Nur Tools einsetzen, die wir selbst weiterentwickeln oder umbauen können. Gilt für neue Tools; bestehende (ElevenLabs, Fab-Plugins) bleiben. Grundsatz Joachim (28.10.2026, laut Unreal Assets): kommerzielle und Closed-Source-Lösungen möglichst vermeiden, offene und kostenlose bevorzugen (entschieden von One, Delegation Joachim 25.10.2026; Weekly 28.10.2026).
- **Zugänge und Dateien über IT:** Alle Probleme mit Dateizugriff, Zugängen und Berechtigungen sowie Fälle, in denen ein Bot bestimmte Daten auf einem bestimmten PC braucht, laufen über den Bot IT. IT führt eine Zugangsliste (welcher Bot bzw. PC welche Zugänge hat, ohne Secrets) und findet die Lösung. (Joachim 28.10.2026 19:13, laut One)

## Inhalt

| Datei | Zweck |
|---|---|
| [knowledge/company.md](knowledge/company.md) | Rechtsträger, Standorte, Organe, Präqualifikation |
| [knowledge/strategy.md](knowledge/strategy.md) | FFVR trägt; nächster Aufbau ist Meditrain |
| [knowledge/meditrain.md](knowledge/meditrain.md) | Medizinlinie: Module, Partner, Transfer von FFVR |
| [knowledge/koni.md](knowledge/koni.md) | Koni Trainer / Konisation: Port, Ablehnung VR-Koni-Edge, Partner |
| [knowledge/expertise.md](knowledge/expertise.md) | Technische Fähigkeiten, die wir belastbar behaupten dürfen |
| [knowledge/projects.md](knowledge/projects.md) | Projekte, Referenzen, Produkte — mit Quellen |
| [knowledge/history.md](knowledge/history.md) | Historisches Kompendium: 105 archivierte Asana-Boards + Mail-Belege |
| [knowledge/mailakte-silas.md](knowledge/mailakte-silas.md) | Fakten aus Silas' Postfach (Asana-Mailakten, intern) |
| [knowledge/grants.md](knowledge/grants.md) | Förderhistorie, laufende Anträge, Pipeline |
| [knowledge/claims.md](knowledge/claims.md) | Zahlen und Sätze mit Evidenzstufe |
| [knowledge/proposal-playbook.md](knowledge/proposal-playbook.md) | Horizon/EIC/KMU/VgV: Formulierungen, die Zuschläge wahrscheinlicher machen |
| [knowledge/repos.md](knowledge/repos.md) | Lokale Git-Repos und Cursor-Codebase-Pfade |
| [knowledge/accounting.md](knowledge/accounting.md) | FreeAgent: GJ, Rechnungsindex — **FA-Zahlen gelten**, ohne Fördermittel |
| [knowledge/accounting-pass.md](knowledge/accounting-pass.md) | Laufender FreeAgent-Tiefenpass (Coverage) |
| [knowledge/document-rules.md](knowledge/document-rules.md) | Wie Dokumente geschrieben werden (inkl. [german-prose.mdc](.cursor/rules/german-prose.mdc)) |
| [knowledge/recruiting-2026-10.md](knowledge/recruiting-2026-10.md) | Stellenanzeigen Festanstellung Okt. 2026; HTML am 19.10.2026 aus dem Repo entfernt (Git-Stand dc2ddfc) |
| [knowledge/tender-scan.md](knowledge/tender-scan.md) | Wöchentlicher Scan öffentlicher Ausschreibungen (Kompetenzfilter) |
| [knowledge/tender-runs/](knowledge/tender-runs/) | Ergebnisse der Wochenläufe |
| [knowledge/contacts/](knowledge/contacts/README.md) | Kontaktlisten Organisationen und Personen, Pflege über Bot „Northdocks Wissen“ |
| [knowledge/open-questions.md](knowledge/open-questions.md) | Widersprüche und offene Punkte |
| [knowledge/gmail-pass.md](knowledge/gmail-pass.md) | Laufender Gmail-Tiefenpass: Coverage, Filter, nächste Slices |
| [knowledge/websites/](knowledge/websites/README.md) | Struktur und Copy-Regeln je Domain |
| [knowledge/brand/](knowledge/brand/README.md) | Marken-CI je Marke (Logos als Drive-Links, Farben, Schriften, Schreibweisen; belegt vs. abgeleitet), Logo-Intros und -Animationen in video-intros.md |
| [knowledge/assets/](knowledge/assets/README.md) | Asset-Katalog des Drive: Landkarte, Freigaberegeln, Tabu-Liste, Sichtungsstand |

## Recherchequellen dieser Version

- northdocks.com und die sieben Vertical-Sites
- Asana-Workspace (Projekte + Board „Anträge & Ausschreibungen“)
- Google Drive (u. a. UKSH-Eignungsmappe, Business Deck)
- GitHub `Northdocks-GmbH` (Cursor-Zugang); `C:\Githup` nur Teilmenge — [knowledge/repos.md](knowledge/repos.md)
- Gmail-Postfach Joachim (Pass 20–21, 2026-08-28; Tiefenpass [knowledge/gmail-pass.md](knowledge/gmail-pass.md); ohne Secrets)
- FreeAgent (Bücher Northdocks GmbH; live per MCP, destilliert in [knowledge/accounting.md](knowledge/accounting.md); ohne Tokens)

## Regel

Nichts in ein externes Dokument schreiben, das in `knowledge/claims.md` nicht mindestens Stufe **intern belegt** hat. Unklare Punkte stehen in `knowledge/open-questions.md`.
