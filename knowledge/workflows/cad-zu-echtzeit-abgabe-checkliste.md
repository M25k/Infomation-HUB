# Abgabe-Checkliste Echtzeit-Asset (Hero-Asset Strahlrohr), Northdocks 3D

Quelle: Bot 3D, 21.10.2026 (Joachim, aus dem Review v3 von Marcel Timm). Vor jeder Abgabe ausfüllen (☑ mit Nachweis oder Bild, ☐ offen mit Grund) und als `ABGABE_CHECKLISTE.md` ins Exportpaket legen. Regeln: [cad-zu-echtzeit.md](cad-zu-echtzeit.md), Abschnitt „Verbindliche Regeln“.

| # | Punkt | Prüfung / Nachweis |
|---|---|---|
| 1 | Namensschema `Nozzle_[Hersteller][Produkt]` (z. B. `Nozzle_HerstellerProdukt`), `SM_/T_/M_` | Dateiliste Paket |
| 2 | Hero-Asset nur LOD0; **Vertices ≤ Ziel +30 %: ab v9 Ziel 39.000 → höchstens 50.700** (UE-Zählung), Qualität vor Zahl (neu 26.10.2026, Review Marcel v8; ~~ca. 20.000 bis 30.000 Vertices, Qualität vor Ziel bis höchstens +30 % (Joachim 23.10.2026, übermittelt von 3D)~~); Texturen 4096² (geändert 23.10.2026, vorher 2048²), ≥ 3 px/mm, Aufdruck ≥ 6 px/mm, Texeldichte geloggt | Re-Import-Prüfung (Vertex-Zahl UE), Texturgröße |
| 3 | +X vorne, +Z oben, cm, ohne Importoptionen korrekt | Re-Import-Prüfung: Rohdaten-BBox ok, Header Z-up, Rotation 0 |
| 4 | Pivots auf Drehachsen (aus CAD-Zylinderachsen) | Platzierungstabelle plus Herleitung |
| 5 | Wasserdicht: nach dem Re-Import exakt 0 Boundary-Edges und 0 Non-manifold-Edges je Teil (sonst nicht verwertbar); Berührkanten zwischen anliegenden, jeweils geschlossenen Solids zählen nicht als Fehler, nur als Info protokolliert (Joachim 23.10.2026, übermittelt von 3D, umgesetzt in v8) | Ergebnis Watertight-Skript nach Re-Import, Info-Liste Berührkanten, Durchguck-Renders |
| 6 | Richtige Teilezuordnung (bewegte Teile in ihrer Gruppe) | Teileliste je Mesh |
| 7 | Farben, Materialien und Aufdrucke am Originalfoto geprüft (fehlende Fotos über One angefragt) | Fotoliste, Annahmen markiert |
| 8 | Skalen und Aufdrucke positioniert | Skalen-Nahaufnahme |
| 9 | UE-5.7-Import (Interchange) ohne Altoptionen | README im Paket |
| 10 | Eine Normal-Map, nur UE-Format, ohne Suffix | `T_<Name>_Normal.png` |
| 11 | ~~Re-Import der FBX geprüft (seit 23.10.2026 eine kombinierte FBX, Regel 14; 1 Material)~~ Re-Import der FBX: Je Teil 1 Render-Mesh plus seine UCX-Hüllen, keine weiteren Objekte (Lage 0, Rot 0, 1 Material, BBox, Vert-Zahl) (Regeln 13 und 14; Klärung 3D, 27.10.2026) | Re-Import-Prüfung |
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
| 23 | UVs fp16-fest (Regel 23): `uv_fp16_abw_px` ≤ 0,01 je Node; Nahaufnahme Blender gegen UE-Emulation (`UE_FP16=1`) gleich | Re-Import-Prüfung, Vergleichsbild |
| 24 | Texeldichte (Regeln 24 und 25): jedes sichtbare Teil ≥ 3 px/mm, jeder Aufdruck ≥ 6 px/mm, Decal-Inseln achsparallel | `texel.json` |
| 25 | Rundteile in Nahsicht rund (Regel 26): Kappen, Schrauben, Ringe, Bohrungen, Führungsschienen ohne Polygon-Silhouette | Nahaufnahmen vorn/seitlich |
| 26 | Nur was am Original ist (Regeln 27 und 28): keine unsichtbaren Befestigungsteile, keine nicht vorhandenen Prägungen oder Logos | Nahaufnahmen plus Foto |
| 27 | Aufdrucke 1:1 nach Foto (Regel 29): Text vollständig mit Umbrüchen, Ikonografie (Linienanzahl, Übergänge), Formen, Lage; Abweichungen zur Auftrags-Kurzfassung benannt | Foto/Render-Paare |
| 28 | Jeder Review-Punkt der Vorversion einzeln abgehakt (Tabelle Review-Punkt → Maßnahme → Nachweis) | `CHANGELOG_<ver>.md` |
| 29 | Textausrichtung (Regeln 33 und 34): Text zwischen zwei Symbolen mittig zwischen den Symbolen; mehrzeilige Blöcke je Block wie im Foto ausgerichtet, Lage des Blocks unverändert | Foto/Render-Paare |
| 30 | Rändelung als Rautenraster (Regel 35, ergänzt Regel 30): zwei sich kreuzende Rillenscharen, keine Streifen; Periode ≥ 6–8 Texel | Nahaufnahme unter Streiflicht |
| 31 | Logos in der Normal Map (Regel 36): zentriert als Höhenbild, gleiche Logo-Zeichnung wie am übrigen Asset, in Gebrauchslage waagerecht lesbar (Gebrauchslage aus CAD hergeleitet), nach dem Glätten eingetragen, Fläche ≥ 6 px/mm | Render in Gebrauchslage, Herleitung, `texel.json` |
| 32 | Übergangszeichen mit sichtbarem Abstand vor dem Icon (Regel 37): ≥ halbe Icon-Breite plus Sicherheitsabstand; Länge, Spreizung, Linienabstände je Zeichen am Foto gemessen | Nahaufnahme plus Foto, Messwerte |
| 33 | Linienbündel getrennt (Regel 38): wo die Linien am Original nicht zusammenlaufen, Lücke am Fuß ≥ 3 Texel | Nahaufnahme in Texturauflösung |
| 34 | Schriftstärke wie im Original (Regel 39): Strichstärke am Foto geprüft, kein pauschales Bold; Versalhöhe, Laufweite und Lage unverändert | Foto/Render-Paare |
| 35 | Begleitgrafiken (Regel 40): Balken und Bänder mit Anfang und Ende an den Nachbarmarken; Höhe und Segment-/Lückenverhältnis wie im Foto | Foto/Render-Paare |
| 36 | Prozedurale Muster im Bake teilbezogen (Regel 41): Explosionsversatz abgezogen oder Objektkoordinaten; Testbake vor dem endgültigen Bake | Testbake-Bild, Bake-Config |
| 37 | Bewegungsbereiche und Maße gegen das Herstellerdatenblatt geprüft, bevor eigene Sperren oder Grenzen gebaut wurden (Regel 42); Abweichungen begründet | Abgleichtabelle Datenblatt gegen Modell (Maß bzw. Grenze, Datenblattwert, Modellwert, Quelle) |
| 38 | Collision vorhanden und benannt (Regel 46; Ablage nach Regel 14): jedes Mesh hat mindestens eine Hülle `UCX_<Mesh>_NN` (NN ab 00 lückenlos, s. Regel 48) (laut 3D, 28.10.2026) | Dateiliste bzw. Node-Liste der FBX |
| 39 | Collision konvex (Regel 46; Ablage nach Regel 14): jede UCX-Hülle konvex | Ergebnis Konvexitätsprüfung je Hülle |
| 40 | Collision höchstens 32 Verts je Hülle (Regel 46; Ablage nach Regel 14) | Vert-Zahl je UCX-Hülle (Log oder Tabelle) |
| 41 | Eigene Hüllen für Kappen und bewegliche Teile (Regel 46; Ablage nach Regel 14) | Zuordnung Teil → Hülle, Render der Hüllen |
| 42 | Collision in der FBX geprüft, nicht über „Use Complex as Simple“ (Regel 46; Ablage nach Regel 14) | Re-Import-Prüfung mit angezeigter Simple Collision; Import-Optionen „Import Collision According To Mesh Name“ an, „Auto Generate Collision“ aus (Klärung 3D, 27.10.2026) |
| 43 | Text-Relikte entfernt (Regel 43): was in Textur oder Decal steckt, ist aus Low- und Highpoly entfernt und glatt neu vernetzt; echte Formmerkmale erhalten | Nahaufnahme bzw. Wireframe vorher/nachher |
| 44 | Strichstärke gemessen (Regel 44): Verhältnis Strich zu Versalhöhe am Original und am Modell, ggf. reduziert ohne Größe oder Lage zu ändern | Messwerte Original gegen Modell, Foto/Render-Paar |
| 45 | Rundungen geschützt, Normalen/Tangenten/Smoothing in der FBX, ~~README nennt „Import Normals and Tangents“ (Interchange: Recompute aus, MikkTSpace)~~ FBX-Teil ersetzt durch Regel 47 bzw. Punkt 46: `SMOOTH_GROUP`, Recompute Normals, Recompute Tangents und Compute Weighted Normals aus (laut 3D, 28.10.2026) (Regel 45); Gesamtzahl unter der Grenze aus Regel 2 (Klärung 3D, 27.10.2026) | Render ohne Normal Map, README, Vert-Zahl gesamt |
| 46 | FBX-Normalen (Regel 47): Rundungen aus der Geometrie, nicht aus der Normal Map; FBX mit echten Smoothing-Groups und CAD-Normalen (nicht Smoothing „Face“); Normalen in der FBX ≤ 0,1° Abweichung, nach Reimport ≤ 0,5°; Import mit „Recompute Normals“, „Recompute Tangents“ und „Compute Weighted Normals“ aus | Normalen-Prüfung aus der FBX und nach Reimport, Render ohne Normal Map, README (Import-Optionen) |
| 47 | UCX-Kollisionen (Regel 48): jedes `UCX_`-Objekt genau eine geschlossene konvexe Hülle, ab `_00` nummeriert; ≤ 32 Verts je Hülle, Punktabstand ≥ 1 mm, ≤ 0,5 mm außerhalb der Box des Render-Meshes; `ucx_check` auf der finalen FBX ohne Fehler; in UE „One Convex Hull Per UCX“ und „Import Collision According to Mesh Name“ an | Bericht `ucx_check` (finale FBX), Import-Optionen |

Punkte 15 bis 21 und Änderung Punkt 2/11: Review Marcel v6, 23.10.2026, 74/100, übermittelt von 3D. Prüfreihenfolge: zuerst Watertight als hartes Ausschlusskriterium (Punkte 5 und 19; bei mehr als 0 Boundary-Edges je Teil nicht verwertbar), danach Review-Priorität nach Regel 15: Texturqualität, dann Skalen und Beschriftung (Auslegung 3D aus Joachims Regel vom 23.10.2026, von Joachim nicht ausdrücklich bestätigt). Culling nur nach Regel 22 (in v8 aus); Hole-Fill nach dem Bake ist Pflicht (Joachim 23.10.2026, übermittelt von 3D, umgesetzt in v8). Nachtrag 26.10.2026: Die Prüfreihenfolge nach Regel 15 ist bestätigt (entschieden von One, Delegation Joachim 25.10.2026, siehe Changelog in [cad-zu-echtzeit.md](cad-zu-echtzeit.md)).

Punkte 23 bis 28 und Änderung Punkt 2: Review Marcel v8, 26.10.2026, 86/100, übermittelt von 3D. In der 3D-Quelldatei `ABGABE_CHECKLISTE.md` heißen diese Punkte 21 bis 26; im HUB sind 21 und 22 schon belegt (HUB hat zusätzlich Punkt 14 „Regel allgemein formulieren, Punktzahl erfragen“), deshalb hier 23 bis 28.

Punkte 29 bis 36: Regeln 33 bis 41, 3D, 27.10.2026, aus Marcels Review v9 (94/100). Punkt 37: Regel 42, 3D, 27.10.2026. Punkte 38 bis 45: Regeln 43 bis 46, 3D, 27.10.2026, aus Marcels Review v10 (Asana 1219711295806018) (Aufteilung sinngemäß nach der Vorlage von 3D: fünf Collision-Punkte, dazu je einer für 43, 44 und 45).

Punkte 46 und 47: Regeln 47 und 48, laut 3D, Changelog 28.10.2026; Quelle: Marcels Review v11 am Strahlrohr (Herstellerbezug, intern), CAD_zu_Echtzeit-Workflow (3D-Bot). In der 3D-Quelle heißen sie Punkte 35 und 36; im HUB sind 35 und 36 schon belegt (Regeln 40 und 41), deshalb hier 46 und 47.
