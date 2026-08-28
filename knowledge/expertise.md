# Technische Expertise

Nur Fähigkeiten, die durch Produkt, Repo oder dokumentierte Referenz gedeckt sind. Keine Spekulation.

## Kernkompetenzen (antragstauglich)

### Spatial Computing / XR-Training

- Native VR-Anwendungen auf Standalone-Headsets (OpenXR), ohne lokale VR-PC-Farm im aktuellen FirefighterVR-/UKSH-Ansatz.
- Unreal Engine 5.7 als Produktionsengine (`NDFramework`, `NDVRActemium`).
- OpenXR und PICO OpenXR aktiv in `NDFramework.uproject`. Plugins `OpenXREyeTracker` und `OpenXRHandTracking` liegen im Projekt, sind dort aktuell **disabled**. Blicksteuerung/Eye-Tracking daher über Storywalx (Wilhelmshaven 2021/22) und ARiNeP belegen, nicht über diese beiden Häkchen.
- Eigene Plugins u. a. `NDVRCore`, `NDFire`, `NDGeo`; `NDAuth` liegt im Framework, ist in `NDFramework.uproject` derzeit **disabled**. Plus CesiumForUnreal, Advanced Sessions, EOSCore, SmoothSync, PICOOpenXR, OpenXR. `GoogleARCore`/`ARUtilities` sind im uproject aktiv — nicht als ausgeliefertes AR-Produkt behaupten. TargetPlatforms: Android und Windows. Weitere Plugin-Ordner (NDWidgets, NDCommonAssets, ND_LookDev, NDEditorTools, CharacterSetup) existieren lokal, sind aber nicht automatisch Produktionsfeatures. `NDGeo` nutzt Unreal GeoReferencing + WebBrowserWidget.
- Multiplayer / Sessions (Advanced Sessions, EOSCore; Planspiel-Peak intern 16 gleichzeitige Nutzer).
- Haptik: physische Objekte ins Tracking (Strahlrohr, Feuerlöscher-Adapter, CPR-Puppe, Industrieventile).
- Offline-Betrieb und lokales WLAN / lokaler Server.
- Desktop-3D-Ansicht zusätzlich zur Brille (UKSH-Angebot).
- 3D Tiles in VR: öffentliche FFVR-FAQ — GodView und das Planspiel-Modul können eigene 3D-Tilesets laden.

### Digital Twin / Geospatial

- GodView: SvelteKit + Cesium (`ND-GodViewWeb`, Docker/Postgres/MinIO). Zusätzlich Potree-Punktwolkenviewer (`www-pointclouds`, Express, LAS/LAZ-Export) für Szenen Dom / Holcim Höver / Bürrig. Beide sind Browser-Twins, keine Headset-Trainingsapp. Google Earth 3D Tiles, Sentinel-2, Drohnen-Photogrammetrie, GLB, Rollen/Orgs, PDF/JSON, VR-Export.
- Hosting in Deutschland, DSGVO-Aussage auf godview.solutions. Intern (DLR-Gespräch 2026): Betrieb derzeit bei Linode; DLR will On-Premise — für Anträge nicht als Linode nennen, On-Prem nicht als Standard behaupten.
- Photogrammetrie: Drohnenbefliegung, RealityCapture-Headless über `ND-Processing` (Express Port 3000 → Python `process.py` → RealityCapture.exe → Cesium-3D-Tiles; lokal oder MinIO; Export u. a. GLB und Orthophoto). Hardcoded-User nicht zitieren.
- Volumenextraktion Punktwolke → LAS/LAZ.
- Extrem große Modelle: Kölner Dom mit **100.000+ Fotos und 1.000 Laserscans** (zitierfähig). Polygonzahl öffentlich 2 Mrd. — nicht unabhängig nachgezählt.

### Simulation

- Brandphysik / Löschangriff, Flashover, Waldbrand (FirefighterVR-Module).
- Physiologische Patientensimulation (Meditrain, Schockraum).
- Strahlenschutz mit Echtzeit-Dosimetrie (Radiation Protection VR, Evaluation UKK, ECR-Award laut Deck). Öffentliches Repo `ND-Strahlensimulation` = Unreal **4.27** (`NDRaySimulation`, Plugin `RaySimulation`) — Kompetenzbeleg für Dosimetrie, nicht der aktuelle 5.7-Produktionsstand.
- Industrie-Verfahrensfolgen und Konsequenztraining (Actemium Infinity).
- Sprachausgabe intern über **ElevenVoice** (TTS) in den meisten XR-Produkten. Ausnahmen: diverse Fulldome-Shows und VR-Stadttouren (Storywalx). `NDVRActemium.uproject` hat das Plugin enabled; Dateien fehlen im Git-Checkout — Nutzung trotzdem intern Standard. Nicht als öffentliches Website-Feature.
- Katastrophenlage 3D-Daten / Mapping (TEMA, Ahrtal). Tecnosylva-Waldbrand-Sims intern als GeoTIFF (Arrival Time) + KMZ-Isochronen an die TEMA-Plattform; KPI Immersion erst in den 2026-Trials statistisch belegen, nicht als abgeschlossene Validierung zitieren.

### Software- und Systemlieferung

- All-in-one Hardwarekoffer, Pico Enterprise, Device Management.
- Web-Frontends der Vertikale (überwiegend SvelteKit/Vite).
- BMA-Trainer: eigenes Produkt (`www-bma-Trainer-App`), DIN 14675 FAT/FBF. Perspektivisch Funnel für FirefighterVR (z. B. WebXR). **Derzeit keine Vermarktung** — nicht als laufendes Vertriebsprodukt oder FFVR-Headset-Modul behaupten.
- FlowAR intern (Stand 13.07.2026): Android-Prototyp mit Mapbox-Karte, Custom-OpenGL-AR, GLB-Objekte, Tap-to-Place. iOS-Build und WebXR-auf-Pico intern offen — nicht als ausgeliefertes Multi-OS-Produkt.
- Iterative Anpassung, Einweisung, Support DE/EN (UKSH-Angebot: Reaktion ≤ 4 h Werktags, 40 Personentage-Kontingent).

### Forschung / KI (belegt als Vorhaben, nicht als fertiges Allheilmittel)

- TEMA: semantische 3D-Karten, Extremdaten, XR-Interface für NDM (Horizon Europe, Partner).
- feir: KI-gestützte Generierung von VR-Führungsszenarien (BMBF-Verbund).
- Spot-KI: autonomer Roboterhund / Erfassung (KI-Transfer-Hub SH).
- GodView AI Inspect: experimenteller Riss-/Schadensfilter; SH-KI-Förderung in Einreichung.
- Pulse Engine / Sprachsteuerung UKK: intern 40 k€ zugesagt, Rechnungstellung ab 01.01.2027, Arbeit über das UKK-Projekt (Asana „UKK KI / Voice“). Nicht als ausgelieferte Standardfunktion aller Meditrain-Koffer behaupten. Historie: Evaluierung **06.12.2021** (Joachim an Datta); Unity-Integration vorhanden, Port nach **Unreal/C++**. Engine-Änderungen wären OSS-Rückfluss, die VR-App nicht. **Zuschlag UKK 28.12.2021**. Drei Szenarien von Beginn: Schockraum, Instabiler Patient/Station, Fahrstuhl.

## Stack-Überblick

| Schicht | Beleg |
|---|---|
| Unreal Engine 5.7, OpenXR, Pico, NDFire/NDGeo/NDVRCore, CesiumForUnreal | `NDFramework.uproject` (EyeTracker/HandTracking-Plugins dort disabled) |
| Factory/Infinity, PICOOpenXR (nicht Legacy-PicoXR), ElevenVoice (TTS intern) | `NDVRActemium.uproject`; Plugin-Dateien nicht im Checkout |
| Cesium / SvelteKit / Postgres / MinIO / Docker; App-Hosts `app.godview.solutions` = `godview.nd-apps.de` | `ND-GodViewWeb` (deploy.sh, kein GitHub-Actions-Deploy) |
| Potree / Express / LAS-LAZ-Export | `www-pointclouds` |
| RealityCapture, Node, Python, MinIO | `ND-Processing` |
| Unreal 4.27 Dosimetrie-Plugin (historisch) | GitHub `ND-Strahlensimulation` / `NDRaySimulation.uproject` |
| Vite/TS Marketing-Sites | `www-firefightervr` u. a. |
| Express/Socket.IO/Postgres | `www-bma-Trainer-App` |

## Was wir nicht als Standard behaupten

- Unity als Leit-Engine (nicht der lokale Hauptstack).
- IFC/BIM-Vollintegration in GodView (Roadmap, nicht fertig).
- Dass GodView die Headset-Trainingsanwendung sei.
- Dass jeder Auftrag den ganzen FirefighterVR-Katalog enthält.
- `McpAutomationBridge` (in `NDVRActemium.uproject` enabled) als Liefergegenstand oder öffentliche API.
