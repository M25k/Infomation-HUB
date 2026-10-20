# Workflow: CAD (STEP) → Echtzeit-Asset (VR/Unreal/GLB)

Quelle: Bot 3D, 20.10.2026. **Update folgt:** Aufdrucke und Entfernen von Innenflächen.

Stand 20.10.2026 · Northdocks 3D · erstmals angewendet auf ein internes Hersteller-CAD-Modell (Strahlrohr; Herstellerdaten nur intern).
Alles läuft headless auf der Box, ohne GPU und nur mit lizenzfreien Tools:
- **OpenCascade 7.x** über `cadquery-ocp` (OCCT: LGPL-2.1 mit Ausnahme, Bindings: Apache-2.0)
- **Blender 5.2 LTS** (GPL, nur als Werkzeug, die Assets fallen nicht unter GPL)
- **numpy, Pillow**

Skripte: [cad2rt/](cad2rt/) (im Repo nur Skripte und eine generische Beispiel-Config, keine CAD-Daten, Meshes, Texturen oder Bakes)

| Datei | Zweck |
|---|---|
| `tess.py` | STEP → OBJ, ein Objekt pro Bauteil-Instanz (XCAF-Namen, Platzierungen, Einheit mm→m). Mit `--normals` exakte CAD-Flächennormalen (glättungskorrekter Highpoly). |
| `build_lod.py` | Ein LOD: Lowpoly-Erzeugung, Charts/Seams, UV-Packing, Bake (Normal/AO/ORM/BaseColor) gegen CAD-Highpoly, Teilegruppen + Pivots, Export FBX/GLB |
| `assemble.py` | Fasst LOD-Blends zu einer gepackten Master-.blend zusammen (Collections `LOD0..n`) |
| `shots.py` | Review-Renders: Gesamt, Detail, Wireframe je LOD; gleiche Kameras für Vorher/Nachher über `cams.json` |
| `uvshot.py` | UV-Layout über BaseColor als PNG (ohne GPU) |
| `run_all.sh CONFIG.json` | Komplette Pipeline |
| `config_beispiel.json` | generische Beispiel-Konfiguration (Platzhalter statt Teilenamen und Pfaden) |

## Setup (einmalig)
```bash
python3 -m venv <VENV> && <VENV>/bin/pip install cadquery-ocp numpy pillow
export CAD2RT_PY=<VENV>/bin/python
```

## Neues Modell: Schritte
1. **STEP sichten**: `tess.py IN.step /tmp/probe --lin 0.6 --ang 1.0` gibt Teilenamen und Tris aus. Mit einem Blender-Import Bauteil-BBoxen prüfen (Achse, Lage).
2. **Config anlegen** (Kopie der Beispiel-Config):
   - `skip_regex`: unsichtbare Innenteile (Kugeln, Federn, O-Ringe, Gewindestifte, Ventilteile)
   - `materials`: PBR-Grundwerte, Zuordnung per Namens-Teilstring. Der Eintrag ohne `match` ist der Default.
   - `groups`: Funktionsgruppen in Reihenfolge, der erste Treffer gewinnt; die letzte Gruppe mit `[""]` fängt den Rest. Pivot-Regeln:
     - `origin`: Ursprung = BBox-Mitte von `origin_part`
     - `barrel_axis`: auf der Rotationsachse (CAD-Z durch 0,0), mittig in der Gruppe
     - `axis_between:TEIL`: Mittelpunkt zwischen den Teilen, z. B. Lagerkappen einer Hebelachse
   - `lods`: Tessellier-Parameter (`lin` mm, `ang` rad), Tri-Budget, Texturgröße, optional `drop` (Kleinteile aus `lod_drop` weglassen)
   - `rotate_x_deg`, `hidden_dir`: Ausrichtung und verdeckte Seite für den Mantelschnitt bei Rotationsteilen
3. `./run_all.sh config.json` ausführen (Laufzeit auf der Box für ~30 Teile: ca. 10 min).
4. **Review** (Checkliste unten), Parameter nachstellen, einzelne LODs neu bauen:
   `blender -b --python build_lod.py -- config.json 0`

## Was die Pipeline intern macht (Parameter mit Default)
| Schritt | Methode | Parameter |
|---|---|---|
| Highpoly | OCCT-Tessellat, fein, mit exakten Normalen, nicht verschweißt | `high.lin` 0.02 mm, `high.ang` 0.12 rad |
| Lowpoly-Basis | eigenes, grobes OCCT-Tessellat je LOD: Rundungen bekommen eine feste Segmentzahl (ang 0.35 ≈ 18, 0.6 ≈ 11, 1.0 ≈ 6 Segmente/Kreis) | `lods[i].lin/ang` |
| Bereinigung | Verschweißen (2 µm), Planar-Dissolve 0,5° | – |
| Nicht-manifold CAD | Teile mit >0,5 % Kanten an >2 Flächen bekommen Voxel-Remesh | `voxel_mm` (Default max(0,35; 1,5·lin)) |
| Decimate | Collapse je Teil, Budget = 0,6·Flächenanteil + 0,4·Tri-Anteil, Rotationsteile ×1,5, Boost pro Teil möglich | `round_budget_boost`, `budget_boost` |
| Normalen | harte Kante bei >`hard_angle_deg` (75°), danach Weighted Normals (Face Area, Keep Sharp) | |
| Charts / Seams | Region-Growing: Normalen-Kegel `chart_cone_deg` (65°), Stopp an harten Kanten. Rotationsteile: Mantel als ein Streifen, Schnitt auf der verdeckten Seite (`hidden_dir`), Stirnflächen getrennt. Mini-Charts (<`min_chart_faces`) werden zusammengelegt. Seams = Chart-Grenzen. | |
| Unwrap | Angle Based, an den Seams | |
| Packing | eigener Packer: einheitliche Texeldichte (UV-Fläche ∝ 3D-Fläche), PCA-Rotation, Shelf-Packing, Padding garantiert | `padding_px` 16 |
| Bake Normal | Selected-to-Active, explodiert pro Bauteil (0,4 m Versatz), daher kein Fremdtreffer zwischen Teilen. Cage-Extrusion = 2·lin + 0,5 mm, Ray = 3× Extrusion | `bake_samples` 16 |
| Bake AO | Detail-AO (explodiert, Highpoly) × Kontakt-AO (Lowpoly in Lage), gemischt 0,35 + 0,65 | |
| BaseColor / Rough / Metal | Emission-Bake der Materialwerte | |
| Ausgabe | `T_<Name>_LOD<i>_{BaseColor, Normal (OpenGL), Normal_DirectX, ORM, AO}.png` · ORM: R = AO, G = Roughness, B = Metallic | |
| Teile | Join pro Gruppe, Origin auf Pivot, Name `SM_<Name>_<Gruppe>_LOD<i>`, Collection `LOD<i>`, ein Material `M_<Name>_LOD<i>` pro LOD | |
| Export | FBX pro LOD (Meter, −Z forward / Y up, Tangenten, Texturen eingebettet), GLB pro LOD | |

## Unreal-Hinweise
- Für Unreal `Normal_DirectX` verwenden, oder beim OpenGL-Map in UE „Flip Green Channel“ setzen.
- ORM-Textur als Linear (sRGB aus) importieren.
- LODs: `SM_*_LOD0` importieren, LOD1/2 als LOD-Stufen pro Teil zuweisen. Die Namen sind über die LODs konsistent.
- Pivots: Hebel dreht um die lokale X-Achse, Strahlformhülse, Mengenring und Kupplung um die lokale Y-Achse (Blender). In UE ändern sich die Achsen durch die FBX-Konvertierung, deshalb Drehachsen am Asset prüfen.

## Checkliste Review
- [ ] Maße in m plausibel (BBox gegen Datenblatt), Scale 1, Pivots auf den Drehachsen
- [ ] Tris je LOD im Budget (Log: `LOD i tris`); LOD1 ≈ 50 %, LOD2 ≈ 20 %
- [ ] Log: `UV gepackt … Texeldichte px/m`; Richtwert VR-Handobjekt LOD0 ≥ 1500 px/m
- [ ] Keine WARNUNG zu UV-Pack oder Padding
- [ ] Nahaufnahmen (Rohr, Kupplung, Hebel): keine Flecken, keine Wellen auf Zylindern, keine Naht-Kanten, kein Z-Fighting
- [ ] Wireframe: gleichmäßige Facettierung der Rundteile, keine Dreiecksfächer, die die Silhouette zerstören
- [ ] UV-Bild: Inseln ohne Überlappung, Padding sichtbar, keine stark verzerrten Inseln
- [ ] GLB im Viewer und FBX in UE geprüft (Normal-Map-Konvention!)
- [ ] Vertraulichkeit: Herstellerdaten nur intern ablegen, nichts veröffentlichen

## Typische Fehler und Lösungen
| Symptom | Ursache | Lösung |
|---|---|---|
| Decimate stoppt weit über dem Ziel | Teil nicht-manifold (CAD-Überlappungen) oder zu viele geschützte UV-Grenzen | Voxel-Fallback (automatisch); erst decimieren, dann UVs erzeugen |
| Alle Bakes schwarz bzw. flache Normal-Map | UV-Packer skaliert Inseln auf Fläche ~0 (Blender `pack_islands` mit sehr vielen Inseln und Margin) | eigener Packer `pack_uniform` (bereits drin); UV-Fläche prüfen |
| Texeldichte winzig | zu viele Inseln: Padding frisst die Fläche | `hard_angle_deg` hoch, `chart_cone_deg` hoch, `min_chart_faces` hoch, Kleinteile in LOD2 weglassen (`drop`) |
| BaseColor von Metallen schwarz | Diffuse-Bake liefert bei Metallic = 1 null | Emission-Bake (bereits drin) |
| Flecken auf Normal-Map | Strahlen treffen Nachbarteile | Explodiert baken (bereits drin), Extrusion/Ray an `lin` koppeln |
| Zackige Kanten im Bake | 1 Sample, kein AA | `bake_samples` ≥ 16 |
| Zackenmuster / Flimmern an aufliegenden Teilen | Z-Fighting koplanarer Bauteile (z. B. Skalenring auf Hülse) | `offset_mm` für das untere Teil (z. B. −0,15 mm) |
| Zerknitterte Fläche nach Decimate | Budget für ein Teil zu klein | `budget_boost` für das Teil |
| Blender `uv.export_layout` schlägt headless fehl | braucht GPU-Kontext | `uvshot.py` (PIL) |
