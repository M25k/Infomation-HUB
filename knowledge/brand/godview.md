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

- **Endkarte:** GodView-Reels enden nur mit der GodView-Wortmarke, ohne Northdocks-Logo. (Joachim 22.10.2026, 12:30 UTC+3, übermittelt von Video) Im Voiceover darf „von Northdocks“ gesprochen bleiben; im Bild nur die GodView-Wortmarke. (Joachim 22.10.2026, 12:47 UTC+3, übermittelt von Video) Konkretisierung von [document-rules.md](../document-rules.md) Nr. 9 (eine CI pro Reel).
- **Freigabe:** Alle GodView-Videos sind freigegeben, auch für northdocks.com/reels/: GV-0014 (Reel 17 v4) und GV-0015 (Dom-Reel v3, Reel 16) (Joachim 22.10.2026, übermittelt von One).
- **Notiz Kameraflüge:** ~~Ab Montag (26.10.2026) klärt der Bot GodView App das Rendern der Cesium-Tiles (Dom und andere Modelle) für neue Kameraflüge (Joachim 22.10.2026, übermittelt von One).~~ **Überholt:** Das Rendern der Cesium-Tiles für Kameraflüge übernimmt der Bot GV Render mit `gv-render` (siehe Abschnitt Renderer) (Joachim 23.10.2026, übermittelt von One). GodView App bleibt Admin der Test-Organisation.

## Renderer gv-render (Bot GV Render)

(Joachim 23.10.2026, übermittelt von One)
- Nativer Renderer `gv-render` (vsgCs / VulkanSceneGraph / cesium-native), nur für GodView-Cesium-Tiles. Kein Unreal, vorerst kein Gelände.
- Ausgabe: 4K / 30 fps, H.265, zusätzlich PNG.
- Kamerapfad aus der Web-POI-Tour; Feinschliff in der App.
- Tests auf dem Video-PC; finale Renders auf dem neuen Windows-PC mit RTX 4090.
- Daten: nur Lesezugriff auf die Test-Organisation „ND Testlabor“ (eigener Viewer-Login), keine Produktivdaten; GodView App ist dort Admin. Inhalt der Test-Org: eine Punktwolke (Actemium), ein Mesh und das Dom-Tileset.

## Offen

- GodView.jpg ist die Pico-MDM-App-Kachel (geklärt über Fundort). Ein Markenlogo fehlt weiterhin.
- Offizielle Wortmarke als Vektor fehlt.
