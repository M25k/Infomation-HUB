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
| [aufraeumen.md](aufraeumen.md) | Aufräumvorschläge für das Drive (Duplikate, Altstände, Tippfehler), nur mit Joachims OK umsetzen |
| [open-questions.md](open-questions.md) | Offene Freigabefragen zum Drive |

## Schema

Gilt für [assets.csv](assets.csv) und die Tabellen der Produktdateien.

| Feld (CSV) | Bedeutung | Werte |
|---|---|---|
| `id` | Stabile Katalog-ID, wird nie neu vergeben | Präfix je Produkt plus vierstellige Nummer: `FFVR-0001` (FirefighterVR), `MED-` (MeditrainVR), `STR-` (StrahlenschutzVR), `NFVR-` (Next Factory VR), `SPVR-` (SpearheadVR), `GV-` (GodView), `SW-` (Storywalx), `MD-` (Meta-dom), `IMP-` (IMP Solutions, Submarke im Manual 2023), `KCI-` (Kunden- und Fremd-CI, immer nur intern; Joachim 19.10.2026), `ND-` (Northdocks allgemein). Für große Kundenprojekte sind eigene Projekt-Präfixe erlaubt (Joachim, 18.10.2026): `HVR-` = VR-Stadttour Hannover (Produkt Storywalx). Ein Präfix wird nur einmal vergeben und darf mit keinem bestehenden kollidieren |
| `titel` | Kurzer sprechender Titel | Freitext |
| `drive_link` | Drive-Link mit Datei-ID | `https://drive.google.com/file/d/<ID>` |
| `pfad` | Pfad im Drive zum Zeitpunkt der Sichtung | Text, kann veralten; maßgeblich ist die Datei-ID |
| `typ` | Art des Assets | 3D, Video, Foto, Audio, Doku, Präsentation, Render, Screenshot, CI (Logos, Icons, Schriften, Farben, Styleguides/Manuals, Vorlagen; seit 19.10.2026) |
| `format` | Dateiformat | z. B. mp4, mov, jpg, fbx, pptx |
| `groesse` | Dateigröße | MB |
| `produkt` | Produkt oder Vertical | FirefighterVR, MeditrainVR, StrahlenschutzVR, Next Factory VR, SpearheadVR, GodView, Storywalx, Meta-dom, Northdocks, IMP Solutions; leer bei Kunden-CI (KCI) |
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
11. **Kunden- und Partnermaterial als Referenz:** Kundenmaterial ist grundsätzlich als Referenz freigegeben (Freigabe `angebot`), ausdrücklich auch DJI, Vodafone, sonnen und Merck (Joachim, 18.10.2026). `social-video` nur, wenn Musik und Rechte belegt sind (Regel 6); `website` nur bei Claim-Stufe „öffentlich“ (Regel 8). Die festen Regeln bleiben: Bürrig-Bildmaterial nie, Reschke Productions nie als Referenz, Militär/TMA/Army VR nur intern, Koni Trainer nie als ausgeliefert. Produktionsdateien, Standort-/Kundendaten und Stock-Referenzen aus Kundenprojekten sind keine Referenz-Assets und bleiben nur intern. Kunden-Clips mit nicht lizenzierter oder ungeklärter Musik kommen erst ins Angebot, wenn die Musik durch lizenzierte (z. B. CC0) ersetzt ist; ohne Ton gilt nicht als Ersatz (Joachim, 18.10.2026). Das gilt auch für Videos aus Kundenprojekten mit ungeklärtem Ton: nicht ins Angebot.
12. **VR-Stadttour Hannover (HVR):** Öffentlich nur als „VR-Stadttour Hannover“ mit amatik nennen, die Stadt Hannover nicht als Auftraggeber; keine Beträge, keine Blicksteuerung, Pressetour 10.09. nicht als gelaufen ([claims.md](../claims.md), Joachim 18.10.2026). Extern freigegebene HVR-Einträge tragen den Vermerk „Nennung nur VR-Stadttour Hannover mit amatik, Stadt nicht als Auftraggeber“. Dunkle Gasse, KI-Material, Fremdpakete ohne Lizenz und AE-Produktionsdateien bleiben nur intern. Historische Postkarten Flusswasserkunst und das HGM-Saal-Bild sind gemeinfrei (Joachim 18.10.2026, Quelle wird nicht genannt); andere historische Bilder nur mit Vermerk „gemeinfrei“, sonst nur intern. Die Kröpcke-Figuren sind Marketplace-Assets: Zeigen erlaubt, nicht als Eigenbau darstellen. Altstadt und Dunkle Gasse sind dieselbe Szene; bis zur Klärung durch Joachim nur intern.
13. **CI-Dateien (Typ CI, Joachim 19.10.2026):** Standard „nur intern“, bis Joachim entscheidet. Eigene Markenlogos dürfen auf social-video;website;angebot, wenn sie im Styleguide stehen **und** auf der Live-Site verwendet werden (Stand 19.10.2026: MED-0022, MED-0026, NFVR-0020, SW-0018). Kunden- und Fremd-CI (Präfix KCI, u. a. Reschke, Die drei ???) bleibt immer intern; Reschke und National Guard nie als Referenz. Markenblätter: [../brand/](../brand/README.md).

## Rollen

Stand 18.10.2026 (Joachim über One):

- **Wissen** pflegt Katalog, Regeln und Freigaben und committet ins Repo. Nur Wissen trägt Einträge in [assets.csv](assets.csv) und die Produktdateien ein. Wissen bündelt die Freigabefragen und die Aufräumvorschläge von Assets für Joachim.
- **Assets** ist der Drive-Bot. Er sichtet den Bestand nur lesend nach Priorität aus [landkarte.md](landkarte.md), überwacht werktäglich neue und geänderte Dateien und liefert Einträge als Vorschlag an Wissen. Außerdem sammelt er Aufräumvorschläge für das Drive (Duplikate, Altstände, Ablage). Umgesetzt wird eine Änderung im Drive nur mit Joachims OK. Assets schreibt nicht ins Repo.
  - Ausgabeordner: „Assets Output“ im Shared Drive „Marketing Sales“, neben „Social Clips“ (Ordner-ID `1pXmME0amj9-6IeLgg0ZsUmBCyftveBGm`, https://drive.google.com/drive/folders/1pXmME0amj9-6IeLgg0ZsUmBCyftveBGm). Er ist die einzige Schreibstelle von Assets im Drive.
- **Video** übernimmt 3D-Rendering, Turntables und die GPU-Nutzung, über die gemeinsame Sperre in [../repos.md](../repos.md). Der Output landet in einem Unterordner in „Marketing Sales“. Turntables liegen in „Assets Output / Turntables“ (`1hLNuppiWO9sEAzqWiZ995_h5bV1dpa7d`). B-Roll legt Video ab 19.10.2026 unter „Assets Output / Turntables / B-Roll“ ab (`1tBtqIJlDKnEKCxBMx5rsGrp8C4wtznWQ`). Die Hannover-B-Roll (HVR-0560 bis HVR-0566) liegt im älteren Ordner „Assets Output / B-Roll“ (`1e_Zkj93CNRson7xZZRkw1Tc9hddQJC2G`). Kandidaten stehen in [3d-kandidaten.md](3d-kandidaten.md).
- **Web, Social und Förderung** lesen [assets.csv](assets.csv) oder fragen Wissen. Sie verwenden nur Assets mit passender Freigabe.

## Ablauf

1. Runde 0: Inventur nur über Metadaten (erledigt 18.10.2026, Ergebnis [landkarte.md](landkarte.md)).
2. Joachim bestätigt oder ändert [tabu.md](tabu.md).
3. Assets sichtet Ordner nach Priorität aus [landkarte.md](landkarte.md) und meldet Vorschläge.
4. Wissen prüft gegen die Freigaberegeln, vergibt IDs, trägt ein und setzt den Ordner in [_progress.md](_progress.md) auf „fertig“.
5. Unklare Freigaben und Aufräumvorschläge gehen nach [open-questions.md](open-questions.md). Wissen legt sie Joachim gebündelt vor.
6. Danach überwacht Assets werktäglich neue und geänderte Dateien und liefert sie im selben Ablauf.

**Vorgabe Joachim, 18.10.2026 (an Video):** „Gehe davon aus, dass du alles nehmen darfst. Wir sehen die Reviews im Discord und sagen Bescheid, wenn etwas dabei ist, was nicht geht.“ Video darf damit Drive-Material für Reels und Renderings verwenden, auch 3D-Modelle ohne schriftlichen Lizenzbeleg (z. B. Strahlrohr-Scan KW-235, PICO-4-Adapter, CO2-Löscher Gloria). Kontrolliert wird über das Discord-Feedback. Die festen Regeln gelten weiter: Tabu-Ordner, Bürrig-Bilder, TMA/Militär nur intern, Reschke Productions, Textregeln und claims.md, Epic-Mannequin nicht als eigenes Modell. Im Katalog steht bei solchen Assets „Lizenz nicht schriftlich belegt“.
