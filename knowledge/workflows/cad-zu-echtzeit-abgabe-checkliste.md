# Abgabe-Checkliste Echtzeit-Asset (Hero-Asset Strahlrohr), Northdocks 3D

Quelle: Bot 3D, 21.10.2026 (Joachim, aus dem Review v3 von Marcel Timm). Vor jeder Abgabe ausfüllen (☑ mit Nachweis oder Bild, ☐ offen mit Grund) und als `ABGABE_CHECKLISTE.md` ins Exportpaket legen. Regeln: [cad-zu-echtzeit.md](cad-zu-echtzeit.md), Abschnitt „Verbindliche Regeln“.

| # | Punkt | Prüfung / Nachweis |
|---|---|---|
| 1 | Namensschema `Nozzle_[Hersteller][Produkt]` (z. B. `Nozzle_HerstellerProdukt`), `SM_/T_/M_` | Dateiliste Paket |
| 2 | Hero-Asset nur LOD0, ca. 20.000 bis 30.000 Vertices, Texturen 2048² | Re-Import-Prüfung (Vertex-Zahl UE), Texturgröße |
| 3 | +X vorne, +Z oben, cm, ohne Importoptionen korrekt | Re-Import-Prüfung: Rohdaten-BBox ok, Header Z-up, Rotation 0 |
| 4 | Pivots auf Drehachsen (aus CAD-Zylinderachsen) | Platzierungstabelle plus Herleitung |
| 5 | Wasserdicht: kein Durchgucken, keine sichtbaren Spalte | Ergebnis Watertight-Skript, Durchguck-Renders, Nahaufnahmen |
| 6 | Richtige Teilezuordnung (bewegte Teile in ihrer Gruppe) | Teileliste je Mesh |
| 7 | Farben, Materialien und Aufdrucke am Originalfoto geprüft (fehlende Fotos über One angefragt) | Fotoliste, Annahmen markiert |
| 8 | Skalen und Aufdrucke positioniert | Skalen-Nahaufnahme |
| 9 | UE-5.7-Import (Interchange) ohne Altoptionen | README im Paket |
| 10 | Eine Normal-Map, nur UE-Format, ohne Suffix | `T_<Name>_Normal.png` |
| 11 | Re-Import jeder FBX geprüft (1 Objekt, 1 Material) | Re-Import-Prüfung |
| 12 | Quest/Android ASTC/Vulkan nicht gebrochen (1 Material, Standard-Shader) | Materialaufbau |
| 13 | Vertraulichkeit: Herstellerdaten nur intern, keine Freigabe nach außen | Drive-Freigabe geprüft |
| 14 | Nach dem Review: Regel allgemein formuliert, Changelog ergänzt, Punktzahl bei Marcel Timm erfragt | Changelog in [cad-zu-echtzeit.md](cad-zu-echtzeit.md) |
