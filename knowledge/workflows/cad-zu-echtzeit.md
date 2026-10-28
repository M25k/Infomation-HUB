# Workflow: CAD (STEP) → Echtzeit-Asset (VR/Unreal/GLB)

Quelle: Bot 3D, 20.10.2026. **v3 (20.10.2026): Aufdrucke und das Entfernen von Innenflächen enthalten.**

Stand 21.10.2026 (v6), Regeln ergänzt bis v9 (26.10.2026, Review Marcel v8, 86/100); Regeln 47 und 48 ergänzt 28.10.2026 (Review v11, intern) · Northdocks 3D · angewendet auf ein internes Hersteller-CAD-Modell (Strahlrohr; Herstellerdaten nur intern), v2 bis v6. Die Abschnitte ab „Setup“ beschreiben den Stand v3; bei Widersprüchen gelten die verbindlichen Regeln unten.

**Abgabe immer gegen die [Abgabe-Checkliste](cad-zu-echtzeit-abgabe-checkliste.md) prüfen; die ausgefüllte Kopie liegt in jedem Exportpaket.**

## Verbindliche Regeln (allgemein, für jedes Rohr / Hero-Asset)

Quelle: Joachim, 21.10.2026, aus dem Review v3 von Marcel Timm (UE 5.7 + Quest, 55/100), umgesetzt vom Bot 3D. Gelten vor allen älteren Hinweisen in diesem Dokument; Herkunft im Changelog.

1. **Namensschema:** `Nozzle_[Hersteller][Produkt]` (Beispiel: `Nozzle_HerstellerProdukt`). Meshes `SM_<Name>_<Teil>`, Texturen `T_<Name>_BaseColor|Normal|ORM`, Material `M_<Name>`. Kein `_LOD0`, keine Format-Suffixe (`_DirectX`, `_OpenGL`).
2. **Hero-Asset = nur LOD0** (Strahlrohre sind immer nah an der Kamera). **Vertex-Regel neu (26.10.2026, ab v9; Review Marcel v8, 26.10.2026, 86/100, übermittelt von 3D, Marcel: „target Vertices leicht erhöhen“; Rahmen nach Joachims Regel „Qualität vor Zielzahl bis +30 %“ vom 23.10.2026): Zielzahl 39.000 Vertices** (UE-Zählung inkl. UV- und Hartkanten-Splits), Qualität geht vor der Zahl, **harte Obergrenze +30 % = 50.700 Vertices**, so wenig wie möglich darüber. **Bestätigt 26.10.2026:** Zielzahl 39.000 Vertices und harte Grenze 50.700 Vertices (entschieden von One, Delegation Joachim 25.10.2026). Hinweis: Die Anhebung des Ziels von 30.000 auf 39.000 kam von 3D nach Marcels v8-Review; Joachim hatte die 39.000 nicht ausdrücklich bestätigt (seine Regel vom 23.10.2026 deckt nur die +30 %). Mit der Entscheidung von One gilt sie jetzt als bestätigt. Zusätzliche Vertices zuerst dorthin, wo der Reviewer Eckigkeit sieht (Regel 26). Weitere LODs nur, wenn die Config sie ausdrücklich anfordert. ~~Bisher: Budget ca. 20.000 bis 30.000 Vertices gesamt; Qualität vor der Vertex-Zielzahl bis höchstens +30 % (also bis ca. 39.000 Vertices) (Joachim 23.10.2026, übermittelt von 3D).~~ Ersetzt 26.10.2026.
3. **Texturen 4096 × 4096** (geändert 23.10.2026, Review Marcel v6, 23.10.2026, 74/100, übermittelt von 3D; vorher 2048 × 2048), ein Atlas, ein Material für alle Teile. Texeldichte mindestens 3 px/mm, Teile mit Aufdruck mindestens 6 px/mm.
4. **Eine Normal-Map, nur im UE-Format** (DirectX, Grün = −Y), Name ohne Suffix. Eine zweite OpenGL-Variante führt nur zu Verwechslungen (Flip Green doppelt oder fehlend).
5. **Achsen:** +X = vorne (Mündung bzw. Blickrichtung des Bauteils), +Z = oben, Einheit cm. Der FBX-Header entspricht dem UE-Zielsystem (Blender-Export `axis_forward='Y', axis_up='Z'`), damit ist der Import ohne Optionen korrekt. Prüfung: Rohdaten-BBox im FBX gleich Blender-BBox.
6. **Pivots auf den echten Drehachsen**, berechnet aus den CAD-Zylinderflächen (Achse und Lage), nicht aus Bounding-Boxen: Rotationsteile exakt auf der Rohrachse, Hebel exakt auf der Scharnierachse. Statische Teile: Bezug Griff.
7. **Richtige Teilezuordnung:** Jedes CAD-Bauteil kommt in die Gruppe, mit der es sich real bewegt (z. B. Zeiger zum drehenden Ring). Mehrkomponenten-Teile (Hart/Weich, Einleger) per `split_regex` in Solids trennen und getrennt einfärben.
8. **Wasserdicht** (verschärft (Joachim 23.10.2026, übermittelt von 3D): Löcher und offene Kanten sind generell ein No-Go, mehr als 0 Boundary-Edges je Teil = nicht verwertbar, nicht nur „von außen sichtbar“; ~~von außen~~): keine sichtbaren Spalte, kein Durchgucken. Mittel: kein Voxel-Remesh bei Mehr-Solid-Teilen, strenges Culling mit Sicherheitssaum (nur nach Regel 22), Kontaktschutz beim Decimate, leichtes Inflate, Abdeckscheiben in offenen Bohrungen. Prüfung: Watertight-Skript (offene Kanten, Durchguck = 0), Renders aus vielen Winkeln, Durchguck-Render gegen Leuchtfläche.
9. **Farben, Materialien und Aufdrucke am Originalfoto prüfen.** Was nicht belegt ist, als Annahme kennzeichnen; fehlen Fotos, über One anfragen. Herstellerlogos auf dem Objekt sind erlaubt ([../document-rules.md](../document-rules.md) Nr. 5).
10. **Skalen und Aufdrucke** nach CAD-Prägung, Foto und Review positionieren: Zahl und Marke als Einheit, Nullstellung oben, Lesbarkeit aus der Bedienansicht prüfen (Nahaufnahme-Render).
11. **Texturen VR-tauglich:** kein Rauschen (AO mit mindestens 256 Samples plus Insel-Blur, Normal leicht gefiltert), glatte CAD-Flächen mit flacher Normal-Map, feine Strukturen (Rändel) nur mit einer Periode von mindestens 6 bis 8 Texeln (sonst Moiré und Mip-Flimmern).
12. **UE-5.7-Import (Interchange) ohne Altoptionen** (Uniform Scale, Convert Scene, Force Front X gibt es nicht mehr). Nur: Normals/Tangents nicht neu berechnen. Normal-Map als Normalmap (BC5/ASTC), ORM linear.
13. **Verifikation vor Abgabe:** ~~Re-Import jeder FBX (1 Objekt, Lage 0, Rotation 0, 1 Material, BBox, Vertex-Zahl),~~ Re-Import der FBX: Je Teil 1 Render-Mesh plus seine UCX-Hüllen, keine weiteren Objekte (Lage 0, Rot 0, 1 Material, BBox, Vert-Zahl) (Klärung 3D, 27.10.2026); Vorher/Nachher-Renders mit identischen Kameras, Durchguck vorn und hinten, Skalen-Nahaufnahme. Quest/Android (ASTC, Vulkan) darf nicht brechen: ein Material, keine Spezial-Shader.

14. **Abgabe als eine kombinierte FBX** für „Import Into Level“, die Texturen als zweite ZIP. Ersetzt getrennte Teil-FBX und eingebettete Texturen (siehe Changelog). UCX-Hüllen liegen in der kombinierten FBX unter dem Hauptteil (Root-Node, z. B. Griff), als Geschwister der Teil-Meshes, im Raum ihres Meshes. Unreal ordnet sie über den Namen `UCX_<Mesh>_NN` zu (Import Collision According To Mesh Name an, Auto Generate Collision aus) (Klärung 3D, 27.10.2026).
15. **Review-Priorität:** Watertight (Regeln 8 und 19) ist ein hartes Ausschlusskriterium und wird **vor** der Review-Priorität geprüft. Danach ordnet Regel 15 nur noch: erst Texturqualität, dann Skalen und Beschriftung (bestätigt, abgeleitet aus Joachims Regel vom 23.10.2026 „über 0 nicht verwertbar“; entschieden von One, Delegation Joachim 25.10.2026).
16. **Texte und Icons gerade und unverzerrt abwickeln**; mit Orthoansicht-Renders prüfen.
17. **Beschriftung nur auf Außenflächen**; erhabene CAD-Schrift darunter einebnen.
18. **Jede Beschriftung auf das Teil wie auf den Fotos**; Logos auch auf kleine Kappen.
19. **Watertight-Check je Teil**, **Pflicht** (verschärft (Joachim 23.10.2026, übermittelt von 3D), vorher „Ziel: 0 sichtbare offene Kanten“): 0 Boundary-Edges je Teil; mehr als 0 = Modell nicht verwertbar. Löcher und offene Kanten sind generell ein No-Go.
20. **Schwarz eloxiertes Metall:** metallic ≤ 0,3, roughness ≥ 0,5.
21. **Jedes Teil mit den Referenzfotos abgleichen.**
22. **Culling darf keine offenen Kanten hinterlassen:** entweder schließen und neu prüfen oder für das Teil weglassen. Praxis in v8: Culling ist aus, weil das nachträgliche Füllen große Dreiecke auf sichtbare Flächen gelegt hat (Joachim 23.10.2026, übermittelt von 3D, umgesetzt in v8).

Regeln 14 bis 21 und die Änderung an Regel 3: Review Marcel v6, 23.10.2026, 74/100, übermittelt von 3D.

23. **UV-Präzision wie in UE (fp16):** UE speichert UVs standardmäßig in 16 bit („Use Full Precision UVs“ aus). Bei 4096² verschiebt das jede Vertex-UV um bis zu etwa 1 Texel, je Dreieck anders; Aufdrucke knicken dann an Dreieckskanten („wellig“), obwohl sie in Blender gerade sind. Deshalb UVs **vor dem Bake** auf fp16 runden (`uv_fp16: true`, auch nach dem Hole-Fill-Skript); der Bake folgt den gerundeten UVs. Der Export prüft `uv_fp16_abw_px` ≤ 0,01 px je Node. Das README nennt „Use Full Precision UVs“ nur als optionale Zusatzsicherheit.
24. **Aufdrucke auf eigenen, exakt projizierten UV-Inseln:** Decal-Flächen bekommen eine eigene Insel (Seam an der Klassengrenze), UV = exakte Abwicklung (zylindrisch Winkel × Radius bzw. planar), **achsparallel, ohne PCA-Drehung**, Dichte ≥ 6 px/mm (`texel_boost` je Decal, Schnitt `uv_cut_deg` außerhalb des Drucks). Gerade Linien laufen so parallel zu den Texelzeilen (keine Treppen), die Dichte bleibt konstant. Prüfung: Nahaufnahme mit UE-Emulation (`UE_FP16=1`) neben dem Blender-Render, beide müssen gleich aussehen.
25. **Verdeckte Flächen nicht löschen, sondern klein mappen** (`hidden_texel`, Faktor ca. 0,15): verdeckte Flächen (Strahltest) bekommen eigene Mini-Inseln, die frei werdende Atlasfläche geht an sichtbare Flächen. Automatischer Texel-Bericht (`work/texel.json`): **jedes sichtbare Teil ≥ 3 px/mm, jeder Aufdruck ≥ 6 px/mm**, sonst `texel_boost` nachstellen; Ergebnis vor der Abgabe in die Checkliste.
26. **Kleine Rundteile in Nahsicht rund halten:** Kappen, Schraubenköpfe, Dichtringe, Bohrungen, Führungsschienen werden je Bauteil feiner tesselliert (`tess_fine`, Regex gegen den Originalnamen) und per `budget_boost` vor der Reduktion (Decimate) geschützt. Abnahme: Nahaufnahmen von vorn und seitlich, keine Polygon-Silhouetten (z. B. Bohrung als Fünfeck), keine zerklüfteten Kanten.
27. **Im Einbauzustand Unsichtbares entfernen:** Befestigungsteile, die nur stören (z. B. Schraubenschäfte, die innen aus dem Hebel ragen), per `skip_regex` weglassen; danach Watertight und Durchguck erneut prüfen.
28. **Nur was am Original ist:** geprägte CAD-Beschriftungen oder Logos, die am realen Teil nicht sichtbar sind (z. B. ein Herstellerkürzel auf den Hebelkappen), aus der Geometrie **und** der Normal-Map entfernen (`deemboss`: Kuppel glatt neu vernetzen, High-Poly entprägen), nicht nur das Decal weglassen.
29. **Aufdrucke 1:1 nach Originalfoto:** Text vollständig mit den Original-Zeilenumbrüchen; Maße (Versalhöhe, Zeilenabstand, Strichstärke) und Lage relativ zu den Nachbarmarken aus dem Foto messen; Ikonografie exakt (Anzahl der Fächerlinien, Übergangszeichen zwischen Icons, keine zusätzlichen Linien); Formen wie am Original (Logo nachgezeichnet, dünne Kastenlinien, Lage im Kasten). Widerspricht eine Kurzfassung dem Foto oder dem Reviewer-Kommentar, **gilt das Original**; im Bericht nennen.
30. **Griffstruktur nur auf Funktionsflächen:** Rändel bzw. Zacken nur auf den erhabenen Rippen (`knurl` mit `r_min_mm`); Nebenringe und glatte Flächen ohne Struktur (`material_regions` mit `r_min_mm`/`r_max_mm` plus `flat_normal`).
31. **„In UE anders als in euren Bildern“ wird gemessen, nicht vermutet:** Ursache systematisch prüfen (UV-Präzision fp16, Texeldichte, UV-Verzerrung oder -Drehung, Mips/Kompression, Normal-Map, Importeinstellungen); Ergebnis und Abhilfe im README dokumentieren und als Vergleichsbild (Blender gegen UE-Emulation, alt gegen neu) ins Paket legen.

32. **Eigenes Quellmodell vor Bild-zu-3D:** Wenn Referenzbilder Renders eines eigenen Northdocks-Modells sind, zuerst im Drive das Quellmodell suchen und dieses aufbereiten, statt es per Bild-zu-3D neu zu bauen (3D, 27.10.2026).
33. **Texte zwischen Symbolen mittig setzen:** Steht ein Text zwischen zwei Symbolen, wird er auf die Mitte zwischen den Symbolen zentriert, nicht bündig an einer Nachbarzeile.
34. **Mehrzeilige Textblöcke wie im Original ausrichten:** Die Ausrichtung je Block vom Foto übernehmen. Beim Korrigieren bleibt die Lage des Blocks gleich, nur die Zeilen werden neu ausgerichtet.
35. **Rändelung als Rautenraster statt Streifen:** ein Raster aus kleinen Zähnen mit zwei sich kreuzenden Rillenscharen, nie nur eine Rillenrichtung. Abnahme per Nahaufnahme unter Streiflicht. Die Periode umfasst mindestens 6–8 Texel. (Ergänzt Regel 30.)
36. **Logos in Normal Maps in Gebrauchslage lesbar:** Erhabene Logos auf beweglichen Teilen werden zentriert als Höhenbild in die Normal Map gesetzt, mit derselben Logo-Zeichnung wie an anderen Stellen des Assets, und so gedreht, dass sie in Gebrauchslage waagerecht lesbar sind. Die Gebrauchslage aus dem CAD ermitteln (vorhandene Prägung, Anschläge) und mit einem Render prüfen. Das Logo erst nach dem Glätten der Normal Map eintragen. Die Fläche mit dem Logo braucht mindestens 6 px/mm. (Vgl. 17/28: sichtbare erhabene Logos als Höhenbild, nicht als Geometrie.)
37. **Übergangszeichen nicht in Icons ragen lassen:** Zeichen enden mit sichtbarem Abstand vor dem Icon, mindestens halbe Icon-Breite plus Sicherheitsabstand. Länge, Spreizung und Linienabstände je Zeichen am Foto messen. (Präzisiert Regel 29.)
38. **Linienbündel als getrennte Linien:** Laufen die Linien am Original nicht in einem Punkt zusammen, bekommen sie am Fuß eine Lücke von mindestens 3 Texeln, damit sie in der Texturauflösung sichtbar bleibt.
39. **Schriftstärke vom Original übernehmen:** Die Strichstärke am Foto prüfen, nicht pauschal Bold nehmen. Versalhöhe, Laufweite und Lage bleiben gleich. (Präzisiert Regel 29.)
40. **Begleitgrafiken an Bezugsmarken ausrichten:** Balken und Bänder mit Anfang und Ende an den Nachbarmarken festmachen. Höhe und Verhältnis von Segment zu Lücke vom Foto übernehmen. (Präzisiert Regel 29.)
41. **Prozedurale Muster im Bake teilbezogen berechnen:** Beim Backen werden die Teile auseinandergezogen. Diesen Versatz abziehen oder Objektkoordinaten nutzen, sonst entstehen falsche Muster (Streifen statt Rauten). Vor dem endgültigen Bake einen Testbake machen.
42. **Datenblatt vor eigenen Grenzen:** Bewegungsbereiche und Maße zuerst gegen das Herstellerdatenblatt prüfen, bevor eigene Bewegungssperren oder Grenzen gebaut werden (3D, 27.10.2026).
43. **Text-Relikte aus der Geometrie entfernen:** Was schon in Textur oder Decal steckt, aus Low- und Highpoly entfernen und die Fläche glatt neu vernetzen. Echte Formmerkmale bleiben. (Vgl. 17/28.)
44. **Strichstärke messen:** Die Strichstärke der Schrift am Original messen, als Verhältnis Strich zu Versalhöhe, und bei Bedarf reduzieren, ohne Größe oder Lage zu ändern. (Präzisiert Regel 39.)
45. **Rundungen schützen und Normalen mitliefern:** Rundungen an Hebeln und Kappen bei der Reduktion schützen, ~~die geschützten Flächen kommen zusätzlich zum Budget.~~ Geschützte Rundungen kommen zusätzlich zum Decimate-Budget der übrigen Flächen desselben Teils, damit der Rest nicht gröber wird. Die Gesamtzahl bleibt unter der harten Obergrenze aus Regel 2 (Ziel +30 %, z. B. 50.700 Verts). Reicht das nicht, Budget aus weniger sichtbaren Teilen umverteilen (Klärung 3D, 27.10.2026). (Werkzeug: `budget_boost` bzw. `tess_fine` nach Regel 26; geschützte Flächen werden nicht vom Teilbudget abgezogen.) Normalen, Tangenten und Smoothing in die FBX exportieren. ~~Im README die Import-Einstellung „Import Normals and Tangents“ nennen (Interchange: Recompute aus, MikkTSpace).~~ ~~Smoothing „FACE“~~ **Den FBX-Teil ersetzt Regel 47:** Smoothing `SMOOTH_GROUP` (echte Smoothing-Groups); die Option „Import Normals and Tangents“ gibt es im Interchange-Import ab UE 5.7 nicht mehr; beim Import „Recompute Normals“, „Recompute Tangents“ und „Compute Weighted Normals“ aus (laut 3D, 28.10.2026). Abnahme mit einem Render ohne Normal Map.
46. **UCX-Collision für jedes Mesh:** Pflicht. Name `UCX_<Mesh>_NN` (NN ab 00 lückenlos, s. Regel 48) (laut 3D, 28.10.2026), konvex, höchstens 32 Verts. Kappen und bewegliche Teile bekommen eigene Hüllen. Prüfung in der FBX, nicht „Use Complex as Simple“. (Ablage und Zuordnung in der FBX: Regel 14.)
47. **FBX für den Interchange-Import ab UE 5.7:** Runde Flächen bekommen ihre Rundung aus der Geometrie, nicht aus der Normal Map. Export mit echten Smoothing-Groups und den CAD-Normalen, nicht mit Smoothing „Face“. Die Normalen direkt in der FBX prüfen: höchstens 0,1° Abweichung, nach dem Reimport höchstens 0,5°. Beim Import „Recompute Normals“, „Recompute Tangents“ und „Compute Weighted Normals“ ausschalten. (Präzisiert Regel 45.)
48. **UCX-Kollisionen:** Jedes `UCX_`-Objekt ist genau eine geschlossene konvexe Hülle, nummeriert ab `_00`. Höchstens 32 Vertices pro Hülle, mindestens 1 mm Punktabstand, höchstens 0,5 mm außerhalb der Box des Render-Meshes. Das Skript `ucx_check` prüft die finale FBX (Skript beim 3D-Bot, nicht im Repo). In UE „One Convex Hull Per UCX“ und „Import Collision According to Mesh Name“ einschalten. (Präzisiert Regeln 14 und 46.)

Regeln 33 bis 41: 3D, 27.10.2026, aus Marcels Review v9 (94/100). Regel 42: 3D, 27.10.2026 (Erfahrung aus einem Gerätemodell, v4). Regeln 43 bis 46: 3D, 27.10.2026, aus Marcels Review v10 (Asana 1219711295806018). Regeln 47 und 48: laut 3D, Changelog 28.10.2026; Quelle: Marcels Review v11 am Strahlrohr (Herstellerbezug, intern), CAD_zu_Echtzeit-Workflow (3D-Bot).

Regeln 23 bis 31 und die Änderung an Regel 2: Review Marcel v8, 26.10.2026, 86/100, übermittelt von 3D. Regel 25 ersetzt in der Praxis das Löschen verdeckter Flächen (Culling, Regel 22).

**Prozess (Joachim, 21.10.2026):**
- Die [Abgabe-Checkliste](cad-zu-echtzeit-abgabe-checkliste.md) vor jeder Übergabe abhaken und ausgefüllt ins Exportpaket legen.
- Jedes Review wird als **allgemeine Regel** formuliert (nicht nur für das eine Modell) und im Changelog mit Datum, Quelle und Regel eingetragen.
- Nach jedem Review Marcel Timm um eine Punktzahl (0 bis 100) bitten und sie im Changelog vermerken.
- **Geltungsbereich (intern)** (Weekly 28.10.2026, 00:39:56–00:40:17, laut One; W1028-30): Das Regelwerk wird am Strahlrohr fertig iteriert und gilt danach für alle CAD-Daten (z. B. Fahrzeuge).

## Changelog (Regeln)

| Datum | Quelle | Regel / Änderung |
|---|---|---|
| 28.10.2026 | laut 3D, 28.10.2026 | UCX-Nummerierung: NN ab 00 lückenlos (Regel 48), ergänzt in Regel 46 und Checkliste Punkt 38; Regel 45: FBX-Teil durch Regel 47 ersetzt, „Import Normals and Tangents“ (gibt es im Interchange-Import ab UE 5.7 nicht mehr) und Smoothing „FACE“ gestrichen; neu `SMOOTH_GROUP`, Recompute Normals/Tangents und Compute Weighted Normals aus; Checkliste Punkt 45 angepasst, HUB-Nummerierung 46/47 bleibt |
| 28.10.2026 | laut 3D, Changelog 28.10.2026; Quelle: Marcels Review v11 am Strahlrohr (Herstellerbezug, intern), CAD_zu_Echtzeit-Workflow (3D-Bot) | Regel 47 neu: FBX für den Interchange-Import ab UE 5.7 (Rundung aus der Geometrie, echte Smoothing-Groups und CAD-Normalen statt „Face“, Normalen in der FBX ≤ 0,1°, nach Reimport ≤ 0,5°, Recompute Normals/Tangents und Compute Weighted Normals aus); Regel 48 neu: UCX-Kollisionen (eine geschlossene konvexe Hülle je `UCX_`, ab `_00`, ≤ 32 Verts, ≥ 1 mm Punktabstand, ≤ 0,5 mm außerhalb der Render-Mesh-Box, `ucx_check` auf der finalen FBX, „One Convex Hull Per UCX“ und „Import Collision According to Mesh Name“ an); Checkliste Punkte 46 und 47 (in der 3D-Quelle Nr. 35 und 36) |
| 28.10.2026 | Weekly 28.10.2026, 00:39:56–00:40:17, laut One (W1028-30, intern) | Geltungsbereich: Regelwerk am Strahlrohr fertig iterieren, danach für alle CAD-Daten |
| 27.10.2026 | Klärung 3D, 27.10.2026 (zu den Konflikten aus 493d62b) | Regel 13 neu: je Teil 1 Render-Mesh plus seine UCX-Hüllen statt „1 Objekt“; Regel 14 ergänzt: UCX-Hüllen unter dem Root-Node als Geschwister der Teil-Meshes, Zuordnung über `UCX_<Mesh>_NN` (Import Collision According To Mesh Name an, Auto Generate Collision aus); Regel 45 neu: geschützte Rundungen zusätzlich zum Decimate-Budget desselben Teils, Gesamtzahl unter der harten Grenze aus Regel 2 (bleibt), sonst umverteilen. Beleg: Referenz-Asset v11, alle 94 UCX-Hüllen unter dem Root-Node; 43.736 Verts |
| 27.10.2026 | Marcel Review v10 (Asana 1219711295806018), übermittelt von 3D | Regeln 43–46 neu: Text-Relikte aus der Geometrie entfernen, Strichstärke messen, Rundungen schützen und Normalen/Tangenten mitliefern, UCX-Collision für jedes Mesh (Pflicht) |
| 27.10.2026 | 3D, 27.10.2026 (Gerätemodell v4) | Regel 42 neu: Bewegungsbereiche und Maße zuerst gegen das Herstellerdatenblatt prüfen, bevor eigene Bewegungssperren oder Grenzen gebaut werden |
| 27.10.2026 | Marcel Review v9, 94/100 (übermittelt von 3D) | Regeln 33–41 neu: Text zwischen Symbolen mittig, Textblöcke wie Original ausrichten, Rändelung als Rautenraster, Logos in Normal Maps in Gebrauchslage, Übergangszeichen mit Abstand zu Icons, Linienbündel getrennt, Schriftstärke vom Original, Begleitgrafiken an Bezugsmarken, prozedurale Muster im Bake teilbezogen |
| 27.10.2026 | 3D, 27.10.2026, 10:38 | Regel 32 neu: Sind Referenzbilder Renders eines eigenen Northdocks-Modells, zuerst das Quellmodell im Drive suchen und aufbereiten, nicht per Bild-zu-3D neu bauen |
| 26.10.2026 | entschieden von One, Delegation Joachim 25.10.2026 | Regel 2 bestätigt: Zielzahl 39.000 Vertices, harte Grenze 50.700. Vorher von Joachim nicht ausdrücklich bestätigt (Anhebung durch 3D nach Review Marcel v8; Joachims Regel vom 23.10.2026 deckte nur +30 %) |
| 26.10.2026 | Review Marcel v8, 26.10.2026, 86/100, übermittelt von 3D (Quelle: CAD_zu_Echtzeit.md und ABGABE_CHECKLISTE.md beim Bot 3D, anonymisiert übernommen) | Regel 2: Vertex-Ziel 39.000, harte Obergrenze +30 % = 50.700 (vorher Ziel 30.000, bis +30 % ≈ 39.000); Regeln 23 bis 31 neu: UVs vor dem Bake auf fp16 runden plus Export-Check (23), Aufdrucke auf eigenen achsparallelen, exakt projizierten UV-Inseln ≥ 6 px/mm (24), verdeckte Flächen klein mappen statt löschen plus Texel-Bericht ≥ 3/6 px/mm (25), kleine Rundteile feiner tessellieren und vor der Reduktion schützen (26), im Einbauzustand Unsichtbares entfernen (27), nicht am Original vorhandene Prägungen aus Geometrie und Normal-Map entfernen (28), Aufdrucke 1:1 nach Foto (29), Rändel nur auf Rippen (30), UE-Abweichungen messen und dokumentieren (31); Checkliste Punkt 2 neu und neue Punkte (in der 3D-Quelle Nr. 21 bis 26, im HUB Nr. 23 bis 28) |
| 26.10.2026 | entschieden von One, Delegation Joachim 25.10.2026 | Regel 15 bestätigt: Watertight ist hartes Ausschlusskriterium vor dem Review, danach Texturen, Skalen und Beschriftung (abgeleitet aus Joachims Regel vom 23.10.2026, „über 0 nicht verwertbar“); Vermerk „von Joachim nicht ausdrücklich bestätigt“ ersetzt. Die Auslegung im Eintrag vom 23.10.2026 (Zeile unten) gilt damit für Regel 15 als bestätigt |
| 23.10.2026 | Joachim 23.10.2026, übermittelt von 3D, umgesetzt in v8 | Regel 22 neu (Culling ohne offene Kanten, sonst weglassen; in v8 aus); Hole-Fill nach dem Bake als Pflichtschritt mit Pipeline-Abbruch; Checkliste 5: exakt 0 Boundary- und 0 Non-manifold-Edges nach Re-Import, Berührkanten geschlossener Solids nur Info. Ersetzt die Culling-Auslegung der Vorzeile |
| 23.10.2026 | Auslegung 3D aus Joachims Regel vom 23.10.2026, von Joachim nicht ausdrücklich bestätigt | Widersprüche aufgelöst: Culling (v3-Schritt und Regel 8) nur mit Cap/Fill der Schnittkanten und erneutem Boundary-Check, sonst kein Culling für das Teil; Watertight als Ausschlusskriterium vor der Review-Priorität, Regel 15 ordnet nur Texturen vor Skalen/Beschriftung |
| 23.10.2026 | Joachim, übermittelt von 3D | Regel 19 von Ziel zu Pflicht: 0 Boundary-Edges je Teil, sonst nicht verwertbar; Regel 8 verschärft (nicht nur sichtbar); Regel 2: Qualität vor Vertex-Ziel bei höchstens +30 %. **Widersprüche vermerkt:** Regel 15 (Watertight zuletzt), Culling verdeckter Flächen (v3) erzeugt offene Kanten |
| 23.10.2026 | 3D, `export_ue.py` | Export-Standard auf Regel 14 umgestellt: eine kombinierte FBX (Nodes unter dem Hauptteil, Node-Position = Pivot, nur LOD0) plus `<PAKET>_FBX.zip` und `<PAKET>_Texturen.zip`; Re-Import-Check bricht bei eingebetteten Texturen ab; `export_mode` single/both, `legacy_export` aus. Test v7-Config: 6 Nodes, 0,0 mm Pivot-Abweichung. **Korrektur:** „Texturen eingebettet“ war ein Doku-Fehler, das Skript hat nie eingebettet; falsch war nur, dass der alte Export standardmäßig aktiv war |
| 23.10.2026 | Review Marcel v6, 23.10.2026, 74/100, übermittelt von 3D | Regel 3 geändert (4096², ≥ 3 px/mm, Aufdruck ≥ 6 px/mm); neu 14 bis 21: eine kombinierte FBX + Textur-ZIP, Review-Priorität, gerade Abwicklung (Ortho-Check), Beschriftung nur außen, Beschriftung wie Fotos/Logos auf Kappen, Watertight je Teil, Eloxal-Werte, Referenzfoto-Abgleich. **Überholt:** getrennte Teil-FBX mit Platzierungstabelle (v5), FBX/GLB pro LOD als Standard (Pipeline-Tabelle; aufgelöst 23.10.2026, siehe nächste Zeile), Faustregel ≥ 4 px/mm (v3) |
| 21.10.2026 | Review Marcel Timm (UE 5.7 + Quest), v3, 55/100; Joachim | Regeln 1 bis 13: Namensschema `Nozzle_`, nur LOD0, 2048er, Normal nur UE-Format ohne Suffix, +X vorne ohne Importoptionen, Pivots aus CAD-Achsen, Teilezuordnung und Solid-Split, wasserdicht mit Prüfskript, Farben am Foto, Skalen nach CAD/Foto, Texturen entrauscht, UE-5.7-Interchange-Import, Abgabe-Checkliste |
| 20.10.2026 | UE-Importtest v5 | ~~Teil-FBX: Objekt am Ursprung, Transform angewendet, Platzierungstabelle~~ (überholt durch Regel 14, 23.10.2026); LOD1/2-Export sichtbar machen (leere FBX) |
| 20.10.2026 | UE-Importtest v4 | cm und UnitScaleFactor 1 (v3 importierte 1:100), ein Atlas/Material für alle LODs |
| 20.10.2026 | UE-Importtest v3 | Normal-Map: DirectX ohne Flip Green (nie beides), ORM linear |

Weitere Skripte des Stands v6 (Export-Paket mit Re-Import-Prüfung, Watertight-Prüfung, Vorher/Nachher-Renders) liegen beim Bot 3D auf der Box, nicht im Repo.
Alles läuft headless auf der Box, ohne GPU und nur mit lizenzfreien Tools:
- **OpenCascade 7.x** über `cadquery-ocp` (OCCT: LGPL-2.1 mit Ausnahme, Bindings: Apache-2.0)
- **Blender 5.2 LTS** (GPL, nur als Werkzeug, die Assets fallen nicht unter GPL)
- **numpy, Pillow**

Skripte: [cad2rt/](cad2rt/) (im Repo nur Skripte und eine generische Beispiel-Config, keine CAD-Daten, Meshes, Texturen, Aufdruck-PNGs oder Bakes)

| Datei | Zweck |
|---|---|
| `tess.py` | STEP → OBJ, ein Objekt pro Bauteil-Instanz (XCAF-Namen, Platzierungen, Einheit mm→m). Mit `--normals` exakte CAD-Flächennormalen (glättungskorrekter Highpoly). |
| `build_lod.py` | Ein LOD: Lowpoly-Erzeugung, Charts/Seams, UV-Packing, Bake (Normal/AO/ORM/BaseColor) gegen CAD-Highpoly, Teilegruppen + Pivots, Export FBX/GLB |
| `assemble.py` | Fasst LOD-Blends zu einer gepackten Master-.blend zusammen (Collections `LOD0..n`) |
| `shots.py` | Review-Renders: Gesamt, Detail, Wireframe je LOD; gleiche Kameras für Vorher/Nachher über `cams.json` |
| `uvshot.py` | UV-Layout über BaseColor als PNG (ohne GPU) |
| `run_all.sh CONFIG.json` | Komplette Pipeline |
| `make_decals.py` | Aufdruck-Texturen (RGBA) per PIL erzeugen – Vorlage für Skalen/Labels/Logos (Logo als Platzhalter, Text über `CAD2RT_LOGO_TEXT`) |
| `config_beispiel.json` | generische Beispiel-Konfiguration inkl. v3-Parametern (Culling, Texel-Boost, Aufdrucke); Platzhalter statt Teilenamen und Pfaden |

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
| Verdeckte Flächen (v3) | Vor dem Decimate: Raycast je Fläche (Mittelpunkt + 1 Eckpunkt, 64 Fibonacci-Richtungen, Hemisphäre) gegen BVH aller Lowpoly-Teile in Einbaulage; Fläche bleibt, wenn ≥ `min_visible` (3 %) der Strahlen frei entkommen. Budget fließt dadurch in sichtbare Flächen. | `cull_hidden.rays`, `cull_hidden.min_visible`, `cull_hidden.extra_pts` |
| Decimate | Collapse je Teil, Budget = 0,6·Flächenanteil + 0,4·Tri-Anteil, Rotationsteile ×1,5, Boost pro Teil möglich | `round_budget_boost`, `budget_boost` |
| Normalen | harte Kante bei >`hard_angle_deg` (75°), danach Weighted Normals (Face Area, Keep Sharp) | |
| Charts / Seams | Region-Growing: Normalen-Kegel `chart_cone_deg` (65°), Stopp an harten Kanten. Rotationsteile: Mantel als ein Streifen, Schnitt auf der verdeckten Seite (`hidden_dir`), Stirnflächen getrennt. Mini-Charts (<`min_chart_faces`) werden zusammengelegt. Seams = Chart-Grenzen. | |
| Unwrap | Angle Based, an den Seams | |
| Texel-Boost (v3) | Inseln bestimmter Teile im Packer vergrößert (z. B. Skalenring ×2, Gehäuse ×1,6) für lesbare Aufdrucke | `texel_boost` |
| Packing | eigener Packer: einheitliche Texeldichte (UV-Fläche ∝ 3D-Fläche), PCA-Rotation, Shelf-Packing, Padding garantiert | `padding_px` 16 |
| Bake Normal | Selected-to-Active, explodiert pro Bauteil (0,4 m Versatz), daher kein Fremdtreffer zwischen Teilen. Cage-Extrusion = 2·lin + 0,5 mm, Ray = 3× Extrusion | `bake_samples` 16; prozedurale Muster wegen des Versatzes teilbezogen berechnen (Regel 41) |
| Bake AO | Detail-AO (explodiert, Highpoly) × Kontakt-AO (Lowpoly in Lage), gemischt 0,35 + 0,65 | |
| BaseColor / Rough / Metal | Emission-Bake der Materialwerte auf Lowpoly **in Einbaulage** (Weltkoordinaten für Projektion) | prozedurale Muster nur teilbezogen (Versatz abziehen oder Objektkoordinaten), Testbake vor dem endgültigen Bake (Regel 41) |
| Aufdrucke (v3) | `decals`: pro Teil eine RGBA-Textur, projiziert im Shader über Weltposition: `cyl` = Abwicklung um Rohrachse (u = Winkel ab +Z, v = axial über Teil-BBox, REPEAT), `planar_x` = Seitenprojektion entlang ±X (side 0 = beide Seiten, lesbar), Maske über Normale. Wirkt in BaseColor (Bildfarbe), Roughness (`rough`) und Metallic (0) | `decals[].match/type/image/y0/y1/z0/z1/side/u_sign/u_offset/v_flip/rough` |
| Ausgabe | `T_<Name>_LOD<i>_{BaseColor, Normal (OpenGL), Normal_DirectX, ORM, AO}.png` · ORM: R = AO, G = Roughness, B = Metallic | |
| Teile | Join pro Gruppe, Origin auf Pivot, Name `SM_<Name>_<Gruppe>_LOD<i>`, Collection `LOD<i>`, ein Material `M_<Name>_LOD<i>` pro LOD | |
| Hole-Fill (Pflicht, nach dem Bake) (Joachim 23.10.2026, übermittelt von 3D, umgesetzt in v8) | Hole-Fill-Skript schließt offene Kanten je Teil; die Pipeline bricht ab, wenn danach ein Teil noch offene Kanten hat | – |
| Export (Standard, `export_ue.py`) (3D, 23.10.2026) | Eine kombinierte FBX `Meshes/SM_<Name>.fbx`: alle Teile als Nodes unter dem Hauptteil, Node-Position = Pivot, standardmäßig nur LOD0. Texturen werden nie eingebettet. Der Export schreibt selbst zwei ZIPs: `<PAKET>_FBX.zip` und `<PAKET>_Texturen.zip`. Re-Import-Check schlägt fehl, wenn eine Textur eingebettet ist. README, Checkliste und Vergleichsbilder müssen **vor** dem Export im Paketordner liegen, sonst fehlen sie im ZIP. Getestet mit der v7-Config: 6 Nodes, 0,0 mm Pivot-Abweichung, keine eingebetteten Texturen | `export_mode` = `single` (Standard) oder `both`; `legacy_export` (FBX/GLB pro LOD, alte Variante) standardmäßig aus |

## Neue Schritte v3 (Kurz)
1. **Verdeckte Flächen entfernen** (nur nach Regel 22; in v8 aus): `cull_hidden` in der Config setzen. Log prüfen: `Verdeckte Flächen entfernt X von Y`. Danach visuell prüfen (Mündung/Kupplung von vorn ansehen – sichtbare Bohrungsanfänge müssen bleiben; sonst `min_visible` senken).
2. **Aufdrucke**: Texte/Logo in `make_decals.py` (oder eigene PNGs mit Alpha) erstellen; Position in Weltmetern nach `rotate_x_deg`/Pivot-Transformation angeben (Hilfe: Teil-BBoxen aus Log/Blend). Zylindrische Skalen: Winkel 0 = Oberseite (+Z), Zahl über die Bildnaht hinweg doppelt zeichnen (u-Wrap). Testrender `detail_print_*`-Kameras in `cams.json`.
3. **Texel-Boost** für Aufdruckträger setzen; Lesbarkeit in LOD0 prüfen (Ziel ≥ 4 px pro mm Schrifthöhe… Faustregel: Schrifthöhe 5 mm ≥ 15 px). **Überholt durch Regel 3 (23.10.2026):** mindestens 3 px/mm, Teile mit Aufdruck mindestens 6 px/mm.

## Unreal-Hinweise
- Für Unreal `Normal_DirectX` verwenden, oder beim OpenGL-Map in UE „Flip Green Channel“ setzen.
- ORM-Textur als Linear (sRGB aus) importieren.
- LODs: `SM_*_LOD0` importieren, LOD1/2 als LOD-Stufen pro Teil zuweisen. Die Namen sind über die LODs konsistent.
- Pivots: Hebel dreht um die lokale X-Achse, Strahlformhülse, Mengenring und Kupplung um die lokale Y-Achse (Blender). In UE ändern sich die Achsen durch die FBX-Konvertierung, deshalb Drehachsen am Asset prüfen.

## Checkliste Review
- [ ] Maße in m plausibel (BBox gegen Datenblatt), Scale 1, Pivots auf den Drehachsen
- [ ] Tris je LOD im Budget (Log: `LOD i tris`); LOD1 ≈ 50 %, LOD2 ≈ 20 % — **überholt für Hero-Assets:** nur LOD0 (Regel 2), Qualität vor Vertex-Ziel bis +30 % (Joachim 23.10.2026, übermittelt von 3D)
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
| Aufdruck abgeschnitten an Bildkante | Text liegt über u = 0/1 | Text zusätzlich bei x ± Bildbreite zeichnen |
| Aufdruck an Fasen verzerrt | Projektion trifft schräge Flächen | Normalen-Maske (`planar_x` hat |n.x| > 0,6), Fläche verkleinern |
| Sichtbare Löcher nach Culling | `min_visible` zu hoch / zu wenige Strahlen | `min_visible` 0,01–0,02, `rays` 96 |
| Blender `uv.export_layout` schlägt headless fehl | braucht GPU-Kontext | `uvshot.py` (PIL) |
