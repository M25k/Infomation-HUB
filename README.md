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

- **Wir arbeiten in Git** („Hm stop“ (Joachim 29.10.2026 19:13 direkt im Chat von One); „This all wrong“ (Joachim 29.10.2026 19:13 direkt im Chat von One); „You need to understand we work in git“ (Joachim 29.10.2026 19:13 direkt im Chat von One); „Even all our unreal stuff life’s in git“ (Joachim 29.10.2026 19:13 direkt im Chat von One); „The bots can work lokal for testing things ect“ (Joachim 29.10.2026 19:14 direkt im Chat von One); „The unreal projects take there content that is imported for example 3d assets from Google Drive“ (Joachim 29.10.2026 19:15 direkt im Chat von One)): Northdocks arbeitet in Git; auch Unreal-Projekte und Unreal-Assets liegen in Git-Repos, nicht im Drive. Bots dürfen lokal (Box, Workstations) zum Testen und Ausprobieren arbeiten. Unreal-Projekte holen importierte Inhalte, z. B. 3D-Assets, aus Google Drive. Laut One (29.10.2026), nicht im Wortlaut: ~~Die Drive-Regeln unten gelten nur für 3D-Quelldateien, Videos und Renderings~~ (zu eng, s. Gesamtregel); kein rclone- oder Kopier-Setup; echte Ergebnisse gehen ins Git (Medien ins Drive); Workflow: 3D legt fertige Assets (FBX, Texturen) in den Drive-Projektordner, Unreal importiert von dort ins Git-Projekt. **Gesamtregel („And Google Drive is also for alle company documents text tendered ect“ (Joachim 29.10.2026 19:15 direkt im Chat von One); Zusammenfassung laut One 29.10.2026):** Drive für Firmendokumente, Texte, Ausschreibungen, 3D-Quell-Assets, Video und Renderings; Git für Code und Unreal-Projekte (die ihre Assets aus Drive importieren); lokal nur zum Testen.
- **Projektdateien bleiben zusammen** („It is imported that we keep files together is they belong to a project“ (Joachim 29.10.2026 19:16 direkt im Chat von One)): Dateien, die zu einem Projekt gehören, bleiben zusammen. Laut One (29.10.2026), nicht im Wortlaut: im Projektordner im Drive bzw. im Projekt-Repo in Git, nicht verteilt auf Bot-Ordner.
- **Ablage (bestätigt 29.10.2026 19:43)** („1. Ok 2. Ok 3. Sehr gut 4. Ok 5. Sehr gut“ (Joachim 29.10.2026 19:43 direkt im Chat von One, Antwort auf Ones Vorschläge zu drei Kollisionen und zwei Lücken mit den Regeln vom 18.10.); Wortlaut der Punkte laut One): (1) Assets ist nicht mehr auf einen eigenen Unterordner beschränkt; in „Northdocks IT“ legt Assets nur Audit-Berichte ab. (2) Die Regeln „Datenzugriff in Firmenkonten“ und „Wir arbeiten in Git“ gelten; Assets schlägt nur noch größere Umbauten vor. Löschen nur in den Papierkorb, Finanz- und Personalordner tabu (aus der Regel vom 09:12, nicht Teil der 19:43-Vorschläge). (3) Renderings und Turntables liegen im Drive-Ordner des jeweiligen Projekts; in „Marketing Sales“ nur fertige Social-Clips. (4) Fertige Videos und Zwischenstände von Workstations (z. B. GV Render, Unreal Assets) kommen sofort in den Drive-Projektordner (z. B. Kölner Dom in den GodView-Ordner); lokale Kopien sind nur Cache. (5) Dräger-Port: nach bestandener Prüfung mit normalen Commits in den Branch `ue58-mobile`, keine zusätzlichen Git-Regeln. Ersetzt die Ablageregeln vom 18.10.2026 (durchgestrichen in knowledge/assets/README.md und landkarte.md).
- **Google Drive wie eine lokale, synchronisierte Platte** („Außerdem die bots kopieren Daten hin und her und legen zip Archive in Drive an und verlinken sie in asana Tickets. We use drive like a lokal disk so this makes it more difficult“ (Joachim 29.10.2026 19:07 direkt im Chat von One)): Bots legen keine ZIP-Archive in Drive an und kopieren keine Daten hin und her. Dateien kommen entpackt direkt in den Arbeitsordner des Projekts und werden dort aktualisiert, ohne Kopien. In Asana-Tickets wird der Ordner bzw. die Datei verlinkt, nie eine ZIP. (Ausformulierung laut One/3D 29.10.2026; „entpackt in den Arbeitsordner“ und „Ordner/Datei statt ZIP verlinken“ stehen so nicht im Wortlaut.) **Geltungsbereich präzisiert** („Das gilt natürlich nur für 3d video usw Programmierung läuft über git“ (Joachim 29.10.2026 19:11 direkt im Chat von One)): gilt nur für 3D, Video und ähnliche Medien-/Asset-Arbeit; Programmierung läuft über Git. Laut One (29.10.2026), nicht im Wortlaut: ausdrücklich auch Renderings; Code, Skripte und App-Arbeit gehören in die Repos, nicht ins Drive. **Korrigiert (19:13–19:15, s. Regel „Wir arbeiten in Git“ darüber):** ~~gilt nur für 3D-Quelldateien, Videos und Renderings~~ gilt für Firmendokumente, Texte, Ausschreibungen, 3D-Quell-Assets, Video und Renderings (Joachim 19:11 „3d video usw“, 19:15 „company documents text tendered“; s. Gesamtregel).
- **Arbeit ~~liegt immer~~ (Medien und Assets) liegt in Google Drive** („And the bots seam to loose data on the computer all the time which seams to make the work take longer and data gets lost work should always be in Google Drive so ist is backed up and we don’t need toncare about data on workstations“ (Joachim 29.10.2026 19:08 direkt im Chat von One)): Bots verlieren auf den Rechnern ständig Daten; deshalb liegt die Arbeit immer in Google Drive, weil Drive gesichert ist, und um Daten auf Workstations müssen wir uns nicht kümmern. Laut One (29.10.2026), nicht im Wortlaut: gilt auch für die Box; ~~Bots arbeiten direkt im Drive-Projektordner oder speichern jedes Ergebnis und jeden Zwischenstand sofort dort;~~ lokale Kopien sind nur Wegwerf-Cache, niemand verlässt sich darauf, dass Daten auf Box oder PC erhalten bleiben. **Geltungsbereich präzisiert** („Das gilt natürlich nur für 3d video usw Programmierung läuft über git“ (Joachim 29.10.2026 19:11 direkt im Chat von One)): gilt nur für 3D, Video und ähnliche Medien-/Asset-Arbeit; Programmierung läuft über Git. Laut One (29.10.2026), nicht im Wortlaut: ausdrücklich auch Renderings; Code, Skripte und App-Arbeit gehören in die Repos, nicht ins Drive. **Korrigiert (19:13–19:15, s. Regel „Wir arbeiten in Git“ darüber):** Unreal-Projekte und Unreal-Assets liegen in Git, nicht im Drive; lokal nur zum Testen; ~~Drive nur für 3D-Quelldateien, Videos und Renderings.~~ Drive für Firmendokumente, Texte, Ausschreibungen, 3D-Quell-Assets, Video und Renderings (s. Gesamtregel).
- **Weekly-Follow-ups an Patrick als Einzeltickets** („… 2. Ok“ (Joachim 29.10.2026 10:06 direkt im Chat von One, Antwort auf Ones Rückfrage zu italienischen Videos/Wörterbuch und zu Einzeltickets); Anlass: Patricks Asana-Kommentar 28.10.2026 gegen Sammeltickets): je Vorgang ein Asana-Ticket, keine Sammeltickets, keine Dopplungen mit Patricks eigener To-do-Liste. Das Sammelticket 1219983017232554 (W1028-02/-19/-38) hat One geschlossen (laut One 29.10.2026).
- **Datenzugriff in Firmenkonten** („we need to chnage this. all company accounts are fine to acces data move and edit it.“ (Joachim 29.10.2026 09:06 direkt im Chat von One); „only thing that is imprted publik or external sharing“ (Joachim 29.10.2026 09:07 direkt im Chat von One)): Bots dürfen in allen Northdocks-Firmenkonten auf Daten zugreifen, sie verschieben und bearbeiten, ohne den Eigentümer zu fragen. Joachims OK braucht nur das Öffentlichmachen oder externe Teilen. ~~Löschen ist im Wortlaut nicht ausdrücklich genannt; das und die Geltung für Finanz-/Personal-Ordner und den Bielefeld-Angebotsordner klärt [#169](knowledge/assets/open-questions.md).~~ Präzisiert „1. yes delete mean move to bin 2. bids are fine finances not“ (Joachim 29.10.2026 09:12 direkt im Chat von One, Antwort auf Ones Rückfrage zu Löschen und zu Finanz-, Personal- und Bielefeld-Ordnern): **Löschen** ist erlaubt, aber nur in den Papierkorb. **Angebots- und Ausschreibungsordner** (auch Bielefeld) sind freigegeben. **Finanzordner** bleiben tabu. **Personalordner** bleiben nach der bisherigen Regel tabu (dazu keine Aussage Joachims). **Externes Teilen und Veröffentlichen** braucht weiter Joachims OK ([#169](knowledge/assets/open-questions.md), geschlossen). Die Tabu-Liste ([tabu.md](knowledge/assets/tabu.md)) bleibt unverändert; sie regelt Öffentlichkeit und Nutzung, nicht den Zugriff.
- **Fail fast** (Weekly 28.10.2026, 00:25:22–00:27:02, laut One; W1028-21): Früh an Grenzen gehen, statt lange festzustecken. Bei einer Blockade das Prozesswissen (z. B. die Agent-MD-Datei) an ein anderes LLM geben und einen frischen Ansatz machen lassen; Ergebnisse vergleichen, LLMs auch gegeneinander antreten lassen. Vertraulichkeitsregeln dieses Repos gelten dabei weiter.
- **Nur eigene oder umbaubare Tools** (Weekly 28.10.2026, 00:36:18–00:36:54, laut One; W1028-28): Nur Tools einsetzen, die wir selbst weiterentwickeln oder umbauen können. Gilt für neue Tools; bestehende (ElevenLabs, Fab-Plugins) bleiben. Grundsatz Joachim (28.10.2026, laut Unreal Assets): kommerzielle und Closed-Source-Lösungen möglichst vermeiden, offene und kostenlose bevorzugen (entschieden von One, Delegation Joachim 25.10.2026; Weekly 28.10.2026).
- **Zugänge und Dateien über IT:** Alle Probleme mit Dateizugriff, Zugängen und Berechtigungen sowie Fälle, in denen ein Bot bestimmte Daten auf einem bestimmten PC braucht, laufen über den Bot IT. IT führt eine Zugangsliste (welcher Bot bzw. PC welche Zugänge hat, ohne Secrets) und findet die Lösung. (Joachim 28.10.2026 19:13, laut One)
- **Wochenende** („danke btw am wochenende machen wir pause und lassen nur die wichtigsten taks weiterlaufen batch jobs z.b. rendering koenen laufen aber entwicklungs geht erst montags wieder los“ (Joachim 30.10.2026 09:21 direkt im Chat von One)): Am Wochenende machen die Bots Pause. Nur die wichtigsten Aufgaben und Batch-Jobs (z. B. Rendering) laufen weiter; die Entwicklung geht erst montags weiter.

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
