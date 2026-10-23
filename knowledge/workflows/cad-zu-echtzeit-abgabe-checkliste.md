# Abgabe-Checkliste Echtzeit-Asset (Hero-Asset Strahlrohr), Northdocks 3D

Quelle: Bot 3D, 21.10.2026 (Joachim, aus dem Review v3 von Marcel Timm). Vor jeder Abgabe ausfüllen (☑ mit Nachweis oder Bild, ☐ offen mit Grund) und als `ABGABE_CHECKLISTE.md` ins Exportpaket legen. Regeln: [cad-zu-echtzeit.md](cad-zu-echtzeit.md), Abschnitt „Verbindliche Regeln“.

| # | Punkt | Prüfung / Nachweis |
|---|---|---|
| 1 | Namensschema `Nozzle_[Hersteller][Produkt]` (z. B. `Nozzle_HerstellerProdukt`), `SM_/T_/M_` | Dateiliste Paket |
| 2 | Hero-Asset nur LOD0, ca. 20.000 bis 30.000 Vertices (Qualität vor Ziel bis höchstens +30 %, (Joachim 23.10.2026, übermittelt von 3D)), Texturen 4096² (geändert 23.10.2026, vorher 2048²), ≥ 3 px/mm, Aufdruck ≥ 6 px/mm | Re-Import-Prüfung (Vertex-Zahl UE), Texturgröße |
| 3 | +X vorne, +Z oben, cm, ohne Importoptionen korrekt | Re-Import-Prüfung: Rohdaten-BBox ok, Header Z-up, Rotation 0 |
| 4 | Pivots auf Drehachsen (aus CAD-Zylinderachsen) | Platzierungstabelle plus Herleitung |
| 5 | Wasserdicht: nach dem Re-Import exakt 0 Boundary-Edges und 0 Non-manifold-Edges je Teil (sonst nicht verwertbar); Berührkanten zwischen anliegenden, jeweils geschlossenen Solids zählen nicht als Fehler, nur als Info protokolliert (Joachim 23.10.2026, übermittelt von 3D, umgesetzt in v8) | Ergebnis Watertight-Skript nach Re-Import, Info-Liste Berührkanten, Durchguck-Renders |
| 6 | Richtige Teilezuordnung (bewegte Teile in ihrer Gruppe) | Teileliste je Mesh |
| 7 | Farben, Materialien und Aufdrucke am Originalfoto geprüft (fehlende Fotos über One angefragt) | Fotoliste, Annahmen markiert |
| 8 | Skalen und Aufdrucke positioniert | Skalen-Nahaufnahme |
| 9 | UE-5.7-Import (Interchange) ohne Altoptionen | README im Paket |
| 10 | Eine Normal-Map, nur UE-Format, ohne Suffix | `T_<Name>_Normal.png` |
| 11 | Re-Import der FBX geprüft (seit 23.10.2026 eine kombinierte FBX, Regel 14; 1 Material) | Re-Import-Prüfung |
| 12 | Quest/Android ASTC/Vulkan nicht gebrochen (1 Material, Standard-Shader) | Materialaufbau |
| 13 | Vertraulichkeit: Herstellerdaten nur intern, keine Freigabe nach außen | Drive-Freigabe geprüft |
| 14 | Nach dem Review: Regel allgemein formuliert, Changelog ergänzt, Punktzahl bei Marcel Timm erfragt | Changelog in [cad-zu-echtzeit.md](cad-zu-echtzeit.md) |
| 15 | Eine kombinierte FBX für Import Into Level, Texturen als zweite ZIP (Regel 14) | Dateiliste Paket, Import-Into-Level-Test |
| 16 | Texte und Icons gerade und unverzerrt abgewickelt (Regel 16) | Orthoansicht-Renders |
| 17 | Beschriftung nur auf Außenflächen, erhabene CAD-Schrift darunter eingeebnet (Regel 17) | Nahaufnahme-Renders |
| 18 | Jede Beschriftung wie auf den Fotos, Logos auch auf kleinen Kappen (Regel 18) | Foto/Render-Gegenüberstellung |
| 19 | Watertight je Teil: **Pflicht** 0 Boundary-Edges, Löcher/offene Kanten = No-Go (Regel 19, verschärft (Joachim 23.10.2026, übermittelt von 3D)) | Ergebnis Watertight-Skript je Teil |
| 20 | Schwarz eloxiertes Metall metallic ≤ 0,3, roughness ≥ 0,5; jedes Teil mit Referenzfotos abgeglichen (Regeln 20, 21) | Materialwerte, Fotoliste |
| 21 | Vorher/Nachher-Vergleich (gleiche Kameras) | Renders vorher/nachher |
| 22 | README, Checkliste und Vergleichsbilder liegen **vor** dem Export im Paketordner (sonst fehlen sie im ZIP); Paket = `<PAKET>_FBX.zip` + `<PAKET>_Texturen.zip`, keine eingebetteten Texturen (3D, 23.10.2026) | Inhalt beider ZIPs, Re-Import-Check |

Punkte 15 bis 21 und Änderung Punkt 2/11: Review Marcel v6, 23.10.2026, 74/100, übermittelt von 3D. Prüfreihenfolge: zuerst Watertight als hartes Ausschlusskriterium (Punkte 5 und 19; bei mehr als 0 Boundary-Edges je Teil nicht verwertbar), danach Review-Priorität nach Regel 15: Texturqualität, dann Skalen und Beschriftung (Auslegung 3D aus Joachims Regel vom 23.10.2026, von Joachim nicht ausdrücklich bestätigt). Culling nur nach Regel 22 (in v8 aus); Hole-Fill nach dem Bake ist Pflicht (Joachim 23.10.2026, übermittelt von 3D, umgesetzt in v8).
