# Asset-Katalog Northdocks-Drive

Katalog des Northdocks-Drive. Damit finden Video, Web, Social und Förderung Material (Clips, Fotos, Renderings, 3D, Präsentationen), ohne den Drive selbst zu durchsuchen. Jeder Eintrag sagt, wo eine Datei liegt, was sie ist und wofür sie freigegeben ist.

Dateien in diesem Ordner:

| Datei | Inhalt |
|---|---|
| [landkarte.md](landkarte.md) | Überblick Drive: Bereiche, Hauptordner mit Kennzahlen, Prioritäten der Sichtung |
| [assets.csv](assets.csv) | Maschinenlesbarer Gesamtkatalog (eine Zeile je Asset) |
| [firefightervr.md](firefightervr.md), [meditrainvr.md](meditrainvr.md), [strahlenschutzvr.md](strahlenschutzvr.md), [nextfactoryvr.md](nextfactoryvr.md), [spearheadvr.md](spearheadvr.md), [godview.md](godview.md), [storywalx.md](storywalx.md), [meta-dom.md](meta-dom.md), [northdocks.md](northdocks.md) | Lesbare Auszüge je Produkt |
| [tabu.md](tabu.md) | Tabu-Ordner und Ordner „nur intern“ |
| [_progress.md](_progress.md) | Sichtungsstand je Ordner |
| [3d-kandidaten.md](3d-kandidaten.md) | 3D-Quellen, die sich für Renderings/Turntables eignen könnten (fortlaufend) |
| [open-questions.md](open-questions.md) | Offene Freigabefragen zum Drive |

## Schema

Gilt für [assets.csv](assets.csv) und die Tabellen der Produktdateien.

| Feld (CSV) | Bedeutung | Werte |
|---|---|---|
| `id` | Stabile Katalog-ID, wird nie neu vergeben | Präfix je Produkt plus vierstellige Nummer: `FFVR-0001` (FirefighterVR), `MED-` (MeditrainVR), `STR-` (StrahlenschutzVR), `NFVR-` (Next Factory VR), `SPVR-` (SpearheadVR), `GV-` (GodView), `SW-` (Storywalx), `MD-` (Meta-dom), `ND-` (Northdocks allgemein) |
| `titel` | Kurzer sprechender Titel | Freitext |
| `drive_link` | Drive-Link mit Datei-ID | `https://drive.google.com/file/d/<ID>` |
| `pfad` | Pfad im Drive zum Zeitpunkt der Sichtung | Text, kann veralten; maßgeblich ist die Datei-ID |
| `typ` | Art des Assets | 3D, Video, Foto, Audio, Doku, Präsentation, Render, Screenshot |
| `format` | Dateiformat | z. B. mp4, mov, jpg, fbx, pptx |
| `groesse` | Dateigröße | MB |
| `produkt` | Produkt oder Vertical | FirefighterVR, MeditrainVR, StrahlenschutzVR, Next Factory VR, SpearheadVR, GodView, Storywalx, Meta-dom, Northdocks |
| `projekt_kunde` | Projekt oder Kunde | Freitext |
| `datum` | Aufnahme- oder Erstellungsdatum | JJJJ-MM-TT |
| `freigabe` | Wofür das Asset verwendet werden darf | `website`, `social-video`, `angebot`, `nur intern`; mehrere mit `;` |
| `einschraenkungen` | Hinweise zur Nutzung | Personen erkennbar, Kundenlogo, Kundendaten, Einsatzpläne, Lizenz/Fremdmaterial, Musikrechte |
| `qualitaet` | Brauchbarkeit | gut, brauchbar, Archiv |
| `freigabe_quelle` | Woher die Freigabe kommt | `Regel <Name>` oder `Joachim JJJJ-MM-TT` |
| `gesichtet_am` | Datum der Sichtung | JJJJ-MM-TT |
| `gesichtet_von` | Wer gesichtet hat | Bot- oder Personenname |

Grundsätze:

- Default ist **ungeklärt = nur intern**. Ein Asset ohne ausdrückliche Freigabe gilt als „nur intern“.
- Freigaben setzt nur dieser Katalog. Eine Freigabe außerhalb des Katalogs (Chat, Mail, Dateiname) zählt erst, wenn sie hier mit Quelle eingetragen ist.
- Personen und Kundenlogos stehen im Feld `einschraenkungen` nur als Info, nicht als Sperrgrund (Entscheidung Joachim, 18.10.2026).

## Freigaberegeln

Die Regeln gelten zusätzlich zu [document-rules.md](../document-rules.md) und [claims.md](../claims.md). Bei Widerspruch gilt die strengere Regel.

1. **Bürrig (Currenta):** Der Name darf genannt werden. Bilder, Einsatzpläne und Einsatzbereitschaftsdaten aus Bürrig sind immer tabu. Die Regel gilt nur für Bürrig, nicht für andere Currenta-Standorte (Joachim, 18.10.2026); deren sicherheitsrelevantes Material bleibt nur intern. Bei unklarem Standort tabu, bis geklärt.
2. **Reschke Productions:** Nie als Kunde oder Referenz. Material daraus nur intern.
3. **Koni Trainer:** Nie als ausgeliefert oder klinisch validiert zeigen.
4. **Steinmeier:** Keine Aufnahme von Bundespräsident Steinmeier mit VR-Brille verwenden.
5. **Sicherheitsrelevantes nur intern:** Werkfeuerwehr-Interna, Militär (TMA, Kosovo, Army VR), Pläne, Seriennummern.
6. **Lizenzen:** Fremdmaterial, Stock und Musik ohne nachgewiesene Lizenz nicht extern.
7. **Nicht ausgelieferte Funktionen** (Roadmap, Prototypen): nur intern oder ausdrücklich als Ausblick.
8. **Website-Freigabe** nur, wenn der gezeigte Inhalt als Claim mit Stufe „öffentlich“ in [claims.md](../claims.md) steht.
9. **Personen und Kundenlogos** auf Fotos und Videos sind in Ordnung. Der frühere Default „nur intern bis Einwilligung“ entfällt (Joachim über One, 18.10.2026). Die Regeln 1 bis 8 bleiben davon unberührt.
10. **Tabu-Ordner** (Finanzen, Personal und Vergleichbares, Liste in [tabu.md](tabu.md)): Zugriff ist erlaubt, um eine konkrete Frage zu klären. Informationen daraus werden nie ohne Abstimmung mit Joachim freigegeben oder weitergegeben (Joachim über One, 18.10.2026).
11. **Kunden- und Partnermaterial als Referenz:** Kundenmaterial ist grundsätzlich als Referenz freigegeben (Freigabe `angebot`), ausdrücklich auch DJI, Vodafone, sonnen und Merck (Joachim, 18.10.2026). `social-video` nur, wenn Musik und Rechte belegt sind (Regel 6); `website` nur bei Claim-Stufe „öffentlich“ (Regel 8). Die festen Regeln bleiben: Bürrig-Bildmaterial nie, Reschke Productions nie als Referenz, Militär/TMA/Army VR nur intern, Koni Trainer nie als ausgeliefert. Produktionsdateien, Standort-/Kundendaten und Stock-Referenzen aus Kundenprojekten sind keine Referenz-Assets und bleiben nur intern.

## Rollen

- **Northdocks Wissen** pflegt Katalog, Regeln und Freigaben und committet ins Repo. Nur Northdocks Wissen trägt Einträge in [assets.csv](assets.csv) und die Produktdateien ein.
- **Northdocks Assets** (Bot) sichtet den Drive nur lesend und liefert Einträge als Vorschlag an Northdocks Wissen. Er rendert 3D-Assets zu Renderings, Turntables und Clips in seinen Ausgabeordner. Er schreibt nicht ins Repo und beginnt erst, wenn die Tabu-Liste in [tabu.md](tabu.md) von Joachim bestätigt ist.
  - Ausgabeordner: „Assets Output“ im Shared Drive „Marketing Sales“, neben „Social Clips“ (Ordner-ID `1pXmME0amj9-6IeLgg0ZsUmBCyftveBGm`, https://drive.google.com/drive/folders/1pXmME0amj9-6IeLgg0ZsUmBCyftveBGm). Angelegt von Northdocks Assets, Stand 18.10.2026, siehe [landkarte.md](landkarte.md).
  - Rendern: Der GPU-Rechner darf für Renderings genutzt werden, in Absprache mit Northdocks Video (Joachim über One, 18.10.2026).
- **Video, Web, Social und Förderung** lesen [assets.csv](assets.csv) oder fragen Northdocks Wissen. Sie verwenden nur Assets mit passender Freigabe.

## Ablauf

1. Runde 0: Inventur nur über Metadaten (erledigt 18.10.2026, Ergebnis [landkarte.md](landkarte.md)).
2. Joachim bestätigt oder ändert [tabu.md](tabu.md).
3. Northdocks Assets sichtet Ordner nach Priorität aus [landkarte.md](landkarte.md) und meldet Vorschläge.
4. Northdocks Wissen prüft gegen die Freigaberegeln, vergibt IDs, trägt ein und setzt den Ordner in [_progress.md](_progress.md) auf „fertig“.
5. Unklare Freigaben gehen nach [open-questions.md](open-questions.md).
