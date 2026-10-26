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
| `groesse` | Dateigröße | MB im Sinne von MiB (1 MB = 1.048.576 Byte), eine Nachkommastelle; so seit Runde 1 im Katalog. Assets rechnet in Dezimal-MB (1.000.000 Byte) und rechnet beim Import um. Bestehende Einträge werden nicht nur wegen der Einheit geändert (Wissen 22.10.2026) |
| `produkt` | Produkt oder Vertical | FirefighterVR, MeditrainVR, StrahlenschutzVR, Next Factory VR, SpearheadVR, GodView, Storywalx, Meta-dom, Northdocks, IMP Solutions; leer bei Kunden-CI (KCI) |
| `projekt_kunde` | Projekt oder Kunde | Freitext |
| `datum` | Aufnahme- oder Erstellungsdatum | JJJJ-MM-TT |
| `freigabe` | Wofür das Asset verwendet werden darf | `website`, `social-video`, `angebot`, `nur intern`; mehrere mit `;`. Ausnahme `tabu` für Einzeleinträge, die nach [tabu.md](tabu.md) gesperrt sind (z. B. Currenta-Standort unklar; seit 22.10.2026) |
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
8. **Website-Freigabe** nur, wenn der gezeigte Inhalt als Claim mit Stufe „öffentlich“ oder als Zielbild im Wortlaut von [claims.md](../claims.md) steht (Joachim über One, 21.10.2026, #96).
9. **Personen und Kundenlogos** auf Fotos und Videos sind in Ordnung. Der frühere Default „nur intern bis Einwilligung“ entfällt (Joachim über One, 18.10.2026). Die Regeln 1 bis 8 bleiben davon unberührt.
10. **Tabu-Ordner** (Finanzen, Personal und Vergleichbares, Liste in [tabu.md](tabu.md)): Zugriff ist erlaubt, um eine konkrete Frage zu klären. Informationen daraus werden nie ohne Abstimmung mit Joachim freigegeben oder weitergegeben (Joachim über One, 18.10.2026).
11. **Kunden- und Partnermaterial als Referenz:** Kundenmaterial ist grundsätzlich als Referenz freigegeben (Freigabe `angebot`), ausdrücklich auch DJI, Vodafone, sonnen und Merck (Joachim, 18.10.2026). `social-video` nur, wenn Musik und Rechte belegt sind (Regel 6); `website` nur bei Claim-Stufe „öffentlich“ (Regel 8). Die festen Regeln bleiben: Bürrig-Bildmaterial nie, Reschke Productions nie als Referenz, Militär/TMA/Army VR nur intern, Koni Trainer nie als ausgeliefert. Produktionsdateien, Standort-/Kundendaten und Stock-Referenzen aus Kundenprojekten sind keine Referenz-Assets und bleiben nur intern. Kunden-Clips mit nicht lizenzierter oder ungeklärter Musik kommen erst ins Angebot, wenn die Musik durch lizenzierte (z. B. CC0) ersetzt ist; ohne Ton gilt nicht als Ersatz (Joachim, 18.10.2026). Das gilt auch für Videos aus Kundenprojekten mit ungeklärtem Ton: nicht ins Angebot.
12. **VR-Stadttour Hannover (HVR):** Öffentlich nur als „VR-Stadttour Hannover“ mit amatik nennen, die Stadt Hannover nicht als Auftraggeber; keine Beträge, keine Blicksteuerung, Pressetour 10.09. nicht als gelaufen ([claims.md](../claims.md), Joachim 18.10.2026). Extern freigegebene HVR-Einträge tragen den Vermerk „Nennung nur VR-Stadttour Hannover mit amatik, Stadt nicht als Auftraggeber“. Dunkle Gasse, KI-Material, Fremdpakete ohne Lizenz und AE-Produktionsdateien bleiben nur intern. Historische Postkarten Flusswasserkunst und das HGM-Saal-Bild sind gemeinfrei (Joachim 18.10.2026, Quelle wird nicht genannt); andere historische Bilder nur mit Vermerk „gemeinfrei“, sonst nur intern. Die Kröpcke-Figuren sind Marketplace-Assets: Zeigen erlaubt, nicht als Eigenbau darstellen. Altstadt und Dunkle Gasse sind dieselbe Szene; bis zur Klärung durch Joachim nur intern.
13. **CI-Dateien (Typ CI, Joachim 19.10.2026):** Standard „nur intern“, bis Joachim entscheidet. Eigene Markenlogos dürfen auf social-video;website;angebot, wenn sie im Styleguide stehen **und** auf der Live-Site verwendet werden (Stand 19.10.2026: MED-0022, MED-0026, NFVR-0020, SW-0018). Kunden- und Fremd-CI (Präfix KCI, u. a. Reschke, Die drei ???) bleibt immer intern; Reschke und National Guard nie als Referenz. Markenblätter: [../brand/](../brand/README.md).
14. **Drittmarken (Logos fremder Hersteller):** Herstellerlogos auf Gegenständen, in 3D-Szenen und 3D-Assets sowie auf Fotos sind immer in Ordnung (z. B. Minimax am Feuerlöscher im Spiel, Gloria, Rosenbauer/Empl auf Fahrzeugen oder Geräten im Bild). Fremde Logos, die als Einblendung, Overlay, Bauchbinde oder Endcard in ein Video eingebaut werden, brauchen eine Freigabe. Northdocks-eigene Logos sind immer in Ordnung (Joachim, 20.10.2026, 10:01 Athen: „logos on objects, 3D assets and in photos are always fine, but logos that are integrated into the video except from ours need permission“). Eine sichtbare Drittmarke im Bild ist kein Sperrgrund; ein eingebautes Fremdlogo ohne Freigabe schon ([../document-rules.md](../document-rules.md) Nr. 5). **Produktübergreifend (Joachim über One, 21.10.2026, #97):** Eigene Assets dürfen produktübergreifend genutzt werden (z. B. das FirefighterVR-Modell Corpus C3 in einem MeditrainVR-Reel); ein Gerätedesign (z. B. corpuls C3) gilt wie ein Herstellerlogo am Objekt.

- **Gewollte öffentliche Drive-Freigabe** (Joachim über Assets, 21.10.2026): Der Ordner „Firefighter VR Mobile - Infos & Docs [Public]“ (`10idEtQT11vu4nmN5wwprrJFJrQsNIY5P`) ist absichtlich für jeden mit dem Link lesbar; darüber werden FirefighterVR-Dokumente geteilt (u. a. Quick Setup Guides FFVR-0658–0660). Kein Audit-Fund. Dort nur Dokumente ablegen, die für die öffentliche Weitergabe geeignet sind (keine internen, personenbezogenen oder Herstellerdaten).

## Rollen

Stand 18.10.2026 (Joachim über One), ergänzt 19.10.2026 (Freigabe-Audits):

- **Wissen** pflegt Katalog, Regeln und Freigaben und committet ins Repo. Nur Wissen trägt Einträge in [assets.csv](assets.csv) und die Produktdateien ein. Wissen bündelt die Freigabefragen und die Aufräumvorschläge von Assets für Joachim.
- **Assets** ist der Drive-Bot. Er sichtet den Bestand nur lesend nach Priorität aus [landkarte.md](landkarte.md), überwacht werktäglich neue und geänderte Dateien und liefert Einträge als Vorschlag an Wissen. Außerdem sammelt er Aufräumvorschläge für das Drive (Duplikate, Altstände, Ablage). Umgesetzt wird eine Änderung im Drive nur mit Joachims OK. Assets schreibt nicht ins Repo.
  - Ausgabeordner: „Assets Output“ im Shared Drive „Marketing Sales“, neben „Social Clips“ (Ordner-ID `1pXmME0amj9-6IeLgg0ZsUmBCyftveBGm`, https://drive.google.com/drive/folders/1pXmME0amj9-6IeLgg0ZsUmBCyftveBGm). Er ist neben „Northdocks IT“ (nur Audit-Berichte, siehe unten) die einzige Schreibstelle von Assets im Drive.
  - **Freigabe-Audits** (Entscheidung Joachim, 19.10.2026, ca. 15:40 MESZ, über One): Assets prüft regelmäßig die Freigaben im ganzen Drive, **montags Vollaudit, werktags Delta-Prüfung**. Die Prüfung ist rein lesend, Assets ändert keine Freigaben. Bei Tabu-Ordnern liest Assets nur die Berechtigungen des Ordners, keine Inhalte. Funde gehen an Joachim, Patrick und Wissen; Wissen trägt sie in [open-questions.md](open-questions.md) ein (Entscheidung Joachim, Umsetzung Eigentümer bzw. Patrick). Assets darf in den geteilten Ordner „Northdocks IT“ schreiben, aber nur seine Audit-Berichte. Der Ordner existiert noch nicht (Stand 19.10.2026, [open-questions.md](open-questions.md) Nr. 67); bis dahin liegen die Berichte auf der Box unter `/workspace/asset-katalog/audit/` (erster Bericht `freigabe-audit-2026-10-19.md`). Delta-Berichte heißen „Freigabe-Delta JJJJ-MM-TT (Assets)“ und entstehen nur bei neuen Öffnungen nach außen (wie in `/workspace/asset-katalog/audit/README-audit.md`, Wissen 22.10.2026).
- **3D** (seit 20.10.2026, Joachim im Chat mit One, 20.10.2026) erstellt die 3D-Modelle: Image-to-3D und CAD-Aufbereitung. Kandidaten in [3d-kandidaten.md](3d-kandidaten.md). Workflow CAD → Echtzeit: [../workflows/cad-zu-echtzeit.md](../workflows/cad-zu-echtzeit.md) (v3 (20.10.2026): Aufdrucke und das Entfernen von Innenflächen enthalten).
- **Video** macht seit 20.10.2026 nur noch Reels, Renders, Turntables und Cutaways, keine Modellerstellung mehr. Bisher: Video übernimmt 3D-Rendering, Turntables und die GPU-Nutzung, über die gemeinsame Sperre in [../repos.md](../repos.md). Der Output landet in einem Unterordner in „Marketing Sales“. Turntables liegen in „Assets Output / Turntables“ (`1hLNuppiWO9sEAzqWiZ995_h5bV1dpa7d`). B-Roll legt Video ab 19.10.2026 unter „Assets Output / Turntables / B-Roll“ ab (`1tBtqIJlDKnEKCxBMx5rsGrp8C4wtznWQ`). Die Hannover-B-Roll (HVR-0560 bis HVR-0566) liegt im älteren Ordner „Assets Output / B-Roll“ (`1e_Zkj93CNRson7xZZRkw1Tc9hddQJC2G`). Kandidaten stehen in [3d-kandidaten.md](3d-kandidaten.md).
- **Web, Social und Förderung** lesen [assets.csv](assets.csv) oder fragen Wissen. Sie verwenden nur Assets mit passender Freigabe.
- **Zuständigkeit 3D-Material** (Runde 4, 21.10.2026): Quellfotos und CAD für 3D-Modelle gehen an den Bot 3D, Renders an Video.
- Der Logo-Entwurf für StrahlenschutzVR kommt erst ins Drive, wenn Joachim es will.

- **Shorts und Thumbnails** (Video über Assets, 21.10.2026): Läuft ein Reel unter 60 s, ist der YouTube-Short dieselbe 9:16-Datei wie das Final, nur mit einer TXT im Ordner YouTube Shorts; doppelte Thumbnails sind Kopien für Bibliothek und Shorts. Beides ist gewollt, kein Aufräumfall; im Katalog als Duplikat mit Verweis auf das Original führen. Video liefert bald neue Fassungen aller Reels mit ElevenLabs-Stimmen; die alten Versionen werden dann ersetzt. Regel auch in [../websites/_shared.md](../websites/_shared.md) (Video und Clips).

- **TXT-Arbeitsdateien** (Upload-/Caption-TXTs zu Reels und Shorts): immer **nur intern**; der Text wird nur zusammen mit dem Video verwendet (Joachim 21.10.2026).
- **Für die Reels-Seite freigegeben (pro Reel):** die 12 Reels (Joachim 20.10.2026), Reel 14 und 15 (21.10.2026), Reel 16 = Kölner-Dom-Reel GV-0015 (v3, ersetzt GV-0005; Freigabe übernommen) (Joachim 21.10.2026, 15:04, nach Sichtung, ohne Dombauhütten-Logo; auch Social). Reel 17 (GodView Fiale, GV-0014) für die Reels-Seite freigegeben (alle GodView-Videos, Joachim 22.10.2026, übermittelt von One); Reel 18 (Rauchgasdurchzündung, FFVR-0865) ist social-video, für die Reels-Seite noch ohne Joachims OK; Reel 29 (GodView Bauinspektion, GV-0016) für Reels-Seite und Social freigegeben, Reel 30 (MeditrainVR Schockraum, MED-0088/MED-0092) nicht freigegeben (Joachim 26.10.2026, über One) (Nummerierung laut Video 22.10.2026; Drive-Dateinamen 16_/17_ bleiben).
- **Reels-Seite (Joachim über Web und Video, 21.10.2026):** Die Kanal-Freigaben im Katalog gelten für Social Media. Die Seite northdocks.com/reels/ (noindex, nicht im Menü) ist davon ausgenommen: Reels dort brauchen Joachims Freigabe pro Reel, nicht den Kanal „website“ der Quellen; im Katalog steht dann `website` mit Vermerk „Reels-Seite“. Regel auch in [../websites/_shared.md](../websites/_shared.md).

## Ablauf

1. Runde 0: Inventur nur über Metadaten (erledigt 18.10.2026, Ergebnis [landkarte.md](landkarte.md)).
2. Joachim bestätigt oder ändert [tabu.md](tabu.md).
3. Assets sichtet Ordner nach Priorität aus [landkarte.md](landkarte.md) und meldet Vorschläge.
4. Wissen prüft gegen die Freigaberegeln, vergibt IDs, trägt ein und setzt den Ordner in [_progress.md](_progress.md) auf „fertig“.
5. Unklare Freigaben und Aufräumvorschläge gehen nach [open-questions.md](open-questions.md). Wissen legt sie Joachim gebündelt vor.
6. Danach überwacht Assets werktäglich neue und geänderte Dateien und liefert sie im selben Ablauf.

**Vorgabe Joachim, 18.10.2026 (an Video):** „Gehe davon aus, dass du alles nehmen darfst. Wir sehen die Reviews im Discord und sagen Bescheid, wenn etwas dabei ist, was nicht geht.“ Video darf damit Drive-Material für Reels und Renderings verwenden, auch 3D-Modelle ohne schriftlichen Lizenzbeleg (z. B. Strahlrohr-Scan KW-235, PICO-4-Adapter, CO2-Löscher Gloria). Kontrolliert wird über das Discord-Feedback. Die festen Regeln gelten weiter: Tabu-Ordner, Bürrig-Bilder, TMA/Militär nur intern, Reschke Productions, Textregeln und claims.md, Epic-Mannequin nicht als eigenes Modell. Im Katalog steht bei solchen Assets „Lizenz nicht schriftlich belegt“.
