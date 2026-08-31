# Wöchentlicher Ausschreibungs-Scan

Stand: 2026-08-31.

Ziel: öffentliche **Vergaben** finden, die zu FirefighterVR, Meditrain, Next Factory, GodView oder der Twin-/Photogrammetrie-Linie passen. Kein allgemeines VR-Monitoring, keine Fördercalls (die stehen in [grants.md](grants.md)).

**Betrieb:** lokal in diesem Chat, manuell. Keine Cloud-Automation (Asana-OAuth im Automations-Editor bricht ohne `client_id`). Start: **„Starte den wöchentlichen Ausschreibungs-Scan“** — das Skill [tender-scan](../.cursor/skills/tender-scan/SKILL.md) läuft dann durch. Letzter Lauf: `knowledge/tender-runs/2026-08-31.md`.

## Was wir suchen (Kompetenzfilter)

Nur Lose mit Software, Simulation oder 3D-Erfassung in einem dieser Felder:

1. **Meditrain** — Klinik, Rettung, Strahlenschutz, CPR, Schockraum, Pflegelehre (Strategie-Priorität)
2. **FirefighterVR** — Feuerwehrschule, Werkfeuer, Brandschutz-Ausbildung, Koffer/Offline
3. **GodView A** — Bauinspektion, Photogrammetrie, Punktwolke, Denkmal/Bestand
4. **GodView B** — Lagebild, Einsatzleitung, Planspiel/COP
5. **Next Factory** — Anlagensicherheit, Chemiepark, Verfahrensfolgen
6. **Spearhead** — The Marketing Arm (TMA/Omnicom) als Auftraggeber für National-Guard-Trainings, oder Kosovo-Playground; nicht Polizei-IT, nicht Site-Zahlen

CPV, die oft passen (nie allein entscheidend):

| CPV | Bedeutung | Hinweis |
|---|---|---|
| 48190000 | Educational software | UKSH Flashlight lag hier |
| 80500000 / 80521000 | Training services | nur mit Simulation/XR |
| 72262000 | Software development | nur mit Cluster-Wörtern |
| 71354100 | Digital mapping | Twin/Photogrammetrie |
| 79961200 | Aerial photography | Drohnen + 3D, nicht reiner Bildflug |

## Was wir nicht wollen

Gelernt aus Asana „Nicht eingereicht“: IGA-Erlebnis-App, ARbenteuer, Stadtführungs-AR, Museum/Planetarium, Website-IT, reine Headset-Lieferung, Polizei-Vergabe ohne Training („unpassend“), Wärme-/H2-Zwillinge ohne 3D/XR.

TED-Zuschlags- und Änderungsbekanntmachungen (`can-*`) sind fürs Bieten unbrauchbar — das Script filtert sie.

## Quellen

Vollständige Portal-Karte: [.cursor/skills/tender-scan/portals.json](../.cursor/skills/tender-scan/portals.json).

| Quelle | Was sie abdeckt | Wie |
|---|---|---|
| TED Search API | EU-Schwelle, DE/AT/DK/NL/BE/LU | Teil von `scripts/scan.py` |
| oeffentlichevergabe.de (BKMS) | Bund/Länder/Kommunen, oft unter Schwelle; Volltext + Bekanntmachungstext | Teil von `scripts/scan.py` |
| service.bund.de RSS | Zweiter Aggregator; ergänzt BKMS | Teil von `scripts/scan.py` |
| evergabe-online, DTVP, VMP NRW/Bayern/SH | Unterschwelle, kein öffentliches API | Browser nach dem Script, Keywords unten |
| Drive-Sheet | Portal-Liste + Logins | Task [Ausschreibungen / Förderung](https://app.asana.com/1/8864272155433/project/1200346071931886/task/1210459272235392). **Keine Passwörter ins Repo.** Login ok: subreport, Deutsche eVergabe, evergabe-online, RIB/iTWO, **DTVP** (bestätigt 31.08.2026). Lücken: siehe `portals.json` `login_gaps`. |

Ein Lauf:

```text
python .cursor/skills/tender-scan/scripts/scan.py --days 8 --out knowledge/tender-runs/YYYY-MM-DD.json
```

Es gibt **kein** einziges deutsches Portal, das alle UVgO-Lose trägt. TED ist für die EU-Schwelle vollständig. BKMS + bund.de decken den Großteil der veröffentlichten nationalen Bekanntmachungen ab. Die VMPs in portals.json `browser` bleiben Pflicht, sobald der Script-Lauf review/maybe geliefert hat oder SH/NRW/Bayern strategisch relevant sind.

Mailbox `ausschreibungen@northdocks.com` ist der Bieter-Account. Passwort nicht versionieren.

## Suchwörter für bund.de (einzeln, nicht als ODER-Brei)

Direkte Such-URLs (öffentlich, ohne Login):

- [Virtual Reality](https://www.service.bund.de/Content/DE/Ausschreibungen/Suche/Formular.html?nn=4641482&type=0&searchResult=true&templateQueryString=Virtual%20Reality)
- [VR-Training](https://www.service.bund.de/Content/DE/Ausschreibungen/Suche/Formular.html?nn=4641482&type=0&searchResult=true&templateQueryString=VR-Training)
- [virtuelle Realität](https://www.service.bund.de/Content/DE/Ausschreibungen/Suche/Formular.html?nn=4641482&type=0&searchResult=true&templateQueryString=virtuelle%20Realit%C3%A4t)
- [Trainingssimulation](https://www.service.bund.de/Content/DE/Ausschreibungen/Suche/Formular.html?nn=4641482&type=0&searchResult=true&templateQueryString=Trainingssimulation)
- [digitaler Zwilling](https://www.service.bund.de/Content/DE/Ausschreibungen/Suche/Formular.html?nn=4641482&type=0&searchResult=true&templateQueryString=digitaler%20Zwilling)
- [Photogrammetrie](https://www.service.bund.de/Content/DE/Ausschreibungen/Suche/Formular.html?nn=4641482&type=0&searchResult=true&templateQueryString=Photogrammetrie)
- [Schockraum](https://www.service.bund.de/Content/DE/Ausschreibungen/Suche/Formular.html?nn=4641482&type=0&searchResult=true&templateQueryString=Schockraum)
- [Strahlenschutz](https://www.service.bund.de/Content/DE/Ausschreibungen/Suche/Formular.html?nn=4641482&type=0&searchResult=true&templateQueryString=Strahlenschutz)

Weitere Einzelwörter: `OpenXR`, `Einsatztraining`, `Planspiel`, `Patientensimulation`, `Punktwolke`, `Lagebild`, `Bestandsdokumentation`.

Nicht: `Website`, `App` allein, `SAP`, `Headset` allein. UKSH stand unter „VR-Trainingsumgebung“, nicht unter englisch „Virtual Reality“ — deshalb mehrere Suchen, nicht eine.

## Ablage

- Rohdaten TED: `knowledge/tender-runs/YYYY-MM-DD.json`
- Entscheidung: `knowledge/tender-runs/YYYY-MM-DD.md`
- Treffer nach Kompetenzfilter: **sofort** Asana-Board [Anträge & Ausschreibungen](https://app.asana.com/1/8864272155433/project/1200346071931886), Spalte **Sammlung**, mit dem vollen Bid/No-Bid-Raster ([asana-ticket.md](../.cursor/skills/tender-scan/asana-ticket.md)). Ohne dieses Ticket gilt der Fund als nicht abgelegt.

Eine **konkrete** Ausschreibung schreiben (nicht nur finden): Chat **„Wir machen die Ausschreibung …“**. Unterlagen und Entwürfe liegen in Drive [001 Teilnahme](https://drive.google.com/drive/folders/1uHMr8flT_jj4tRFy4mxbcuk2dbTwegKU), nicht in `tender-runs/`. Ablauf: Skill [grants-and-contracts](../.cursor/skills/grants-and-contracts/SKILL.md).

Bestehende Prüfungstask (Patrick): [Ausschreibung / Förderung Prüfung](https://app.asana.com/1/8864272155433/task/1217550927850615).
