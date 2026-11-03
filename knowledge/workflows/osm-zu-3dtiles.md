# Workflow: OSM → 3D Tiles (Planspielplatte / Ortsteil für GodView)

Quelle: Bot 3D, Entwurf 03.11.2026. Auftrag laut 3D: Joachim über Morgen-Briefing/One am 03.11.2026 (von Wissen nicht verifiziert).

Stand 03.11.2026 · Entwurf laut 3D · **nur intern** (Tiles bleiben intern bis Freigabe Joachim, vgl. [brand/godview.md](../brand/godview.md), [open-questions.md](../open-questions.md) #150). Technische Details und Skripte: Repo `Northdocks-GmbH/3d-pipeline`, `docs/planspielplatten-osm-pipeline.md` (PR offen, laut 3D). Alle Fakten unten laut 3D, 03.11.2026, sofern nicht anders vermerkt.

## Rollen
- **3D** erzeugt: OSM-/DGM-Abruf, Blender-Build, GLB, tileset.json, ZIP, Doku je Ort.
- **GodView App** importiert in GodView (Test-Org „ND Testlabor“) und prüft Lage, Lücken, Darstellung.
- **GV Render** rendert Kameraflüge aus den Tiles (`gv-render`).

## Planspielplatte vs. Ortsteil
| | Planspielplatte | Ortsteil |
|---|---|---|
| Ziel | Stilisierte Platte für die Zugführerausbildung, nur GodView Firefighter (Globus-Stil „Platte“) | **offen** (#172) |
| Größe | Testorte ca. 1 km × 1 km (`fetch_osm_place.py`, halbe Breite 500 m) | **offen** (#172) |
| Detail | v5.1: Low-Poly, Vertexfarben, Sockel, Dachformen aus OSM, Bäume, Hydranten | **offen** (#172) |

**Offen (#172):** Sind „Ortsteil“ und „Planspielplatte“ zwei Produkte (Größe/Detail/Ziel) oder ein Produkt in zwei Größen? Entscheidung Joachim.

## Ablauf
1. **Ort und Ausschnitt** (`config.json`: slug, name, state, Ortsmitte, bbox, epsg, DGM-Dateien und -Lizenz). Ortsmitte per Nominatim (max. 1 Anfrage/s).
2. **OSM-Abfrage:** Overpass ist aus der 3D-Arbeitsumgebung **nicht erreichbar**; genutzt wird die OSM-API 0.6 `/map?bbox=` (`fetch_osm_place.py`, ca. 1 km², nur Einzelabrufe). Für Produktion: Geofabrik-PBF + `osmium extract --bbox`. Overpass ist im Standard **nicht** vorgesehen; eigene Instanz: **offen** (#176).
3. **Kataster-/Geländequellen** (DGM1, 1 m; Quellenvermerk mit „Daten geändert“; Lizenzen laut 3D, nicht von Wissen geprüft):
   - SH: LVermGeo SH, CC BY 4.0
   - BY: LDBV, CC BY 4.0 · NI: LGLN, CC BY 4.0
   - BB: LGB, dl-de/by-2-0 · BW: LGL, dl-de/by-2-0
   - HE: HVBG, dl-de/zero-2-0
   - Andere Länder: **offen** (#174). ALKIS-Gebäude oder LoD2 werden derzeit **nicht** genutzt, nur OSM-Grundrisse.
4. **Aufbereitung** (`prep_v5.py`): lokales ENU in Metern, Ursprung = BBox-Mitte. Gebäude als geschlossene Volumen mit Sockel; Höhe aus `height`, sonst `building:levels`, sonst Standard 2 Geschosse (seit 26.10.2026). Ausschnittregel: nur vollständig enthaltene Objekte, nichts zerschneiden.
5. **Dächer:** aus `roof:shape` (flat, gabled, hipped, half-hipped, gambrel, pyramidal u. a.); Gebäude ohne Tag bekommen eine Standardform. **Offen** (#175): `roof:direction`, `roof:orientation=across`, Mansard- und Zwerchgiebel.
6. **Bäume:** derzeit nur aus OSM (`natural=tree`, `tree_row`, `shrub`, `leaf_type`) und als Füllung von Grünflächen. Ein Pflanzen- oder Baumkataster wird bisher nicht genutzt. **Offen** (#173): welche Kommune, welche Lizenz, gewünscht ja/nein.
7. **Gelände:** DGM → `dgm_to_npz.py` → stilisierter, geschlossener Boden mit Schürze (`build_v5_scene.py`).
8. **Blender-Build** (Blender 5.2.2 headless, `build_blender_v5.py`): GLB, Y-up, Meter; Vorschau aus dem GLB mit Cycles (`render_preview_v5.py`).
9. **Tiling:** eigenes Skript (`build_tileset.py`, `make_zip_orte.py`). Kachelstruktur: **ein Tileset je Ort mit einem Root-Tile (ein GLB)**, Transform aus `origin.json` (ECEF), Attribution in `asset.copyright` und den Extras. LOD-Variante nur für Rendsburg (`*_v5_lod_tiles.zip`). Mehrstufige Kachelung oder OSM2World-`tileset`: **offen** (#177).

## Ausgabe: Namen und Ablage (3D-Arbeitsordner)
- **Arbeitsdaten** im 3D-Arbeitsordner der OSM-Stadt-Pipeline, Unterordner `work/orte/<slug>/` (config.json, `<slug>.osm`, dgm/, scene_v5.json, run.log, result.json).
- **Modelle/Doku** im selben Arbeitsordner unter `3d/orte/<slug>/` (GLB, origin.json, METRIKEN.md, LIZENZ.md, Vorschau-PNG), Übersicht `3d/orte/UEBERSICHT.md`.
- **Tiles** unter `tiles/orte/<slug>_v5_tiles.zip` (tileset.json + GLB); Liste `tiles/orte/upload_queue.md`.
- **Offen** (#178): endgültiger Ablageort außerhalb der 3D-Arbeitsumgebung (Drive/Repo/R2).

## Reproduktion
Skript `run_place.py config.json` im 3D-Arbeitsordner führt DGM → npz, Ursprung/Höhe (GCG2016), prep_v5, build_v5_scene, Blender-Export, Vorschau und Prüfungen in einem Lauf aus. Danach `make_zip_orte.py`. Ortsauswahl reproduzierbar über den Seed (`orte_wuerfeln.py`, Seed 20261026). Blender immer gedrosselt (`nice -n 15`) und über die gemeinsame Blender-Sperrdatei der 3D-Arbeitsumgebung (`flock`) starten.

## Übergabe an GodView App
3D legt das ZIP in `tiles/orte/` ab und trägt es in `upload_queue.md` ein (Dateiname, Größe, Ortsmitte). 3D lädt **nicht** selbst hoch. GodView App importiert in „ND Testlabor“, prüft (Lage, Lücken, Schattenartefakte, Speicher) und vermerkt Status und Ansichts-Link in der Queue. GV Render rendert danach Kameraflüge.

## Lizenzen und Pflichthinweise
- Sichtbar: „© OpenStreetMap contributors“ mit Link auf openstreetmap.org/copyright und der DGM-Vermerk des Landes.
- OSM-Attribute getrennt von Kunden- und Feuerwehrdaten halten (ODbL, juristische Bestätigung offen: #150).
- Nicht verwenden: Google Photorealistic 3D Tiles, Bing-/Cesium-ion-/Mapbox-/ESRI-Satellitenbilder als Export in eigene Assets (Anbieter-AGB).
- Werkzeuge (Prüfung 3D 03.11.2026): CesiumForBlender (MIT, v0.1) nicht für die Produktion, weil es nur Anbieter-Streams anzeigt. BlenderGIS (GPL-3.0) nur optional für DGM-/Shapefile-Import. Standard bleibt der eigene Import.
