# GodView – Brand

Stand: 19.10.2026. Vollständigkeit: **kein Styleguide, kein Logofile**. Alles **abgeleitet, nicht belegt**.

## Quellen (Drive)

| Datei | Drive-ID | Inhalt |
|---|---|---|
| GodView.jpg | [1uucD34E9uDqCRqI6dmDoeR9OHRr0I-yH](https://drive.google.com/open?id=1uucD34E9uDqCRqI6dmDoeR9OHRr0I-yH) (GV-0002) | Orange-roter Globus mit „VR“-Badge auf Dunkel (Median-Orange ca. #FF4900). Liegt laut Assets-Liste im Ordner FirefighterVR / _Media / ICONS / „ICONS FFVR PICO MDM“ zwischen den Modul-Kacheln, ist also die **App-Kachel für das Pico-MDM**, kein Markenlogo (so auch im Katalog vermerkt) |
| godview_handbuch_BETA.pdf | [1DcRWDj1TBFrPnEy9IIbkbZSz-cSCCQHp](https://drive.google.com/open?id=1DcRWDj1TBFrPnEy9IIbkbZSz-cSCCQHp) (GV-0003) | Handbuch (Helvetica). Screenshot des App-Startbildschirms mit Wortmarke „GODVIEW“: „GOD“ Weiß, „VIEW“ #FF9900, schmale fette Versalien (wirkt wie Oswald Bold), Tagline „DIGITAL TWIN OPERATION PLATFORM“ gesperrt in Grau ca. #8890A0 |

## Logos

Kein Logofile (SVG/PNG) gefunden. Die Vorschau setzt die Wortmarke aus dem App-Screenshot in Oswald Bold nach (Ersatz, deutlich als solcher markiert).

## Farben (abgeleitet, nicht belegt)

| Rolle | Hex | Quelle |
|---|---|---|
| Akzent Orange | #FF9900 | App-Screenshot (gemessen #FE9900/#FF9900), Website `--accent-primary` |
| Akzent 2 | #FF6600 | Website `--accent-secondary` |
| Hintergrund | #0B0B0B | Website |
| Karte | #191919 | Website |
| Tagline-Grau | #8890A0 | App-Screenshot (gemessen, gerundet) |
| Weiß | #FFFFFF | App-Screenshot |

Das Orange #FF9900 ist identisch mit dem Northdocks-Orange (Farbkit 2020).

## Schriften (abgeleitet, nicht belegt)

Wortmarke wirkt wie Oswald Bold. Website godview.solutions: Oswald, Inter, Space Grotesk. Alle frei (Google Fonts).

## Claims

„DIGITAL TWIN OPERATION PLATFORM“ (App-Startbildschirm).

## Reels

- **Endkarte:** GodView-Reels enden nur mit der GodView-Wortmarke, ohne Northdocks-Logo. (Joachim 22.10.2026, 12:30 UTC+3, übermittelt von Video) Im Voiceover darf „von Northdocks“ gesprochen bleiben; im Bild nur die GodView-Wortmarke. (Joachim 22.10.2026, 12:47 UTC+3, übermittelt von Video) **Bestätigt:** „von Northdocks“ bleibt im GodView-Voiceover; eine anderslautende Entscheidung von One ist zurückgezogen (Joachim 26.10.2026, über One). Konkretisierung von [document-rules.md](../document-rules.md) Nr. 9 (eine CI pro Reel).
- **Freigabe:** Alle GodView-Videos sind freigegeben, auch für northdocks.com/reels/: GV-0014 (Reel 17 v4) und GV-0015 (Dom-Reel v3, Reel 16) (Joachim 22.10.2026, übermittelt von One).
- **Notiz Kameraflüge:** ~~Ab Montag (26.10.2026) klärt der Bot GodView App das Rendern der Cesium-Tiles (Dom und andere Modelle) für neue Kameraflüge (Joachim 22.10.2026, übermittelt von One).~~ **Überholt:** Das Rendern der Cesium-Tiles für Kameraflüge übernimmt der Bot GV Render mit `gv-render` (siehe Abschnitt Renderer) (Joachim 23.10.2026, übermittelt von One). GodView App bleibt Admin der Test-Organisation.

## Renderer gv-render (Bot GV Render)

(Joachim 23.10.2026, übermittelt von One)
- Nativer Renderer `gv-render` (vsgCs / VulkanSceneGraph / cesium-native), nur für GodView-Cesium-Tiles. Kein Unreal, vorerst kein Gelände.
- Ausgabe: 4K / 30 fps, H.265, zusätzlich PNG.
- Kamerapfad aus der Web-POI-Tour; Feinschliff in der App.
- Tests auf dem Video-PC; finale Renders auf dem neuen Windows-PC mit RTX 4090.
- Daten: nur Lesezugriff auf die Test-Organisation „ND Testlabor“ (eigener Viewer-Login), keine Produktivdaten; GodView App ist dort Admin. Inhalt der Test-Org: eine Punktwolke (Actemium), ein Mesh und das Dom-Tileset.

## Technik in Arbeit (intern)

- **OSM-Stadt-Pipeline:** OSM → Blender → Cesium 3D Tiles → GodView. Status: in Arbeit (GodView App). Nur intern, kein Claim nach außen, bis Ergebnis und Freigabe vorliegen (Joachim 26.10.2026, über One).
  - **Lizenz (3D, 26.10.2026, intern):** OSM-Daten stehen unter ODbL. Angezeigte 3D-Modelle und Tiles gelten als Produced Work und brauchen den sichtbaren Hinweis „© OpenStreetMap contributors“ mit Link. Mitgelieferte OSM-Attribute (osm_id, Adresse, Höhe) können als abgeleitete Datenbank zählen; dann gilt Share-Alike. Deshalb bleiben Kunden- und Feuerwehrdaten getrennt. Juristische Bestätigung offen ([open-questions.md](../open-questions.md) #150). **Regel:** „© OpenStreetMap contributors“ steht immer sichtbar mit Link. OSM-Attribute liegen in einer eigenen Tabelle, getrennt von Kunden- und Feuerwehrdaten. Bis Joachim entschieden hat, bleiben die Tiles intern. Offen bei Joachim: ob Kundendaten zusammen mit OSM-Attributen weitergegeben werden dürfen und ob das juristisch geprüft wird; das kommt in die Empfehlung von GodView App zur OSM-Stadt. (entschieden von One, Delegation Joachim 25.10.2026)
  - **Werkzeuge (3D, 26.10.2026):** Blosm Base: GPL v3, kostenlos. Blosm Pro: ausgeschlossen (AGB von Google, Mapbox und ArcGIS). Urban Forge 1.19: GPL-3.0, 9,99 bzw. 29,99 $ pro Seat, nicht gekauft; „Lite“ ist nur ein Preset. OSM2World: MIT, Texturen CC0. Open Voxel Map Generator: ausgeschlossen (nur Windows, Alpha).
  - **Standard-Pipeline (3D, 26.10.2026):** eigener Python-Import in Blender 5.2.2, headless; Skripte auf der Box unter `/workspace/godview/osm-city/scripts/` (nicht im Repo). Liefert geschlossene Gebäude, Attribute als glTF-Extras, ENU Y-up, ca. 8 s pro km².

## Technik-Stand und Regeln (intern; Quelle: GodView App, Stand 27.10.2026)

- **Test-Uploads (Joachim, 26.10.2026):** Bei Tests höchstens ein Tileset-Upload pro 30 Minuten, weil der Server bei paralleler Last kippt. Eine Upload-Warteschlange ist als P1 geplant.
- **Punktwolken ohne Koordinatensystem (Joachim, 26.10.2026):** bleiben im lokalen System und werden in GodView mit „Position festlegen“ bzw. Parenting platziert.
- **Original-Punktwolken (nur intern, Kundendaten):** liegen als LAZ (ohne CRS, aus E57 konvertiert) auf ND-PC-80 im Konvertierungsordner, darunter Kölner Dom (17 Teilscans in einem gemeinsamen lokalen System) und Holcim Höver v001/v002. Intensität und Klassifikation sind leer, nur RGB ist befüllt. Kein Pfad im Repo.
- ~~**Code-Stand (Momentaufnahme 26.10.2026, Repo `ND-GodViewWeb`):** Joachim hat die PRs #6–8 und #17–22 nach `master` gemergt (`master` = `d6ce751`); die Produktion läuft noch auf `2ef827e`. Offen: PR #23 (Tour-Verweildauer) und PR #24 (LAS-Import mit lokalem Koordinatensystem).~~ **Überholt durch Stand 28.10.2026 (unten).**
- **Rendsburg:** Höhenbezug künftig GCG2016 (entschieden von One, Delegation Joachim 25.10.2026).

## Technik-Stand (intern; Quelle: GodView App, Stand 28.10.2026)

- **Code-Stand `master` = `db36925`:** LAS/LAZ-Import (py3dtiles, lokales Koordinatensystem), CesiumJS 1.146, Ellipsoid-Fallback für „Position festlegen“.
- **Produktion** läuft noch auf `2ef827e`. Deploy wartet auf den fertigen AGB-Text, weil Migration 039 jedes Konto beim nächsten Aufruf die AGB annehmen lässt.
- **Stadt-Assets:** Import als 3D Tiles 1.1 im ZIP (`tileset.json` im Root, glb, `EXT_mesh_gpu_instancing`); Georeferenzierung per ECEF-Root-Transform, Höhenbezug GCG2016. Getestet 28.10.2026 mit Rendsburg (GodView App zusammen mit 3D).

## Offen

- GodView.jpg ist die Pico-MDM-App-Kachel (geklärt über Fundort). Ein Markenlogo fehlt weiterhin.
- Offizielle Wortmarke als Vektor fehlt.
