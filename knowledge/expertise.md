# Technische Expertise

Nur Fähigkeiten, die durch Produkt, Repo oder dokumentierte Referenz gedeckt sind. Keine Spekulation.

## Kernkompetenzen (antragstauglich)

### Spatial Computing / XR-Training

- Native VR-Anwendungen auf Standalone-Headsets (OpenXR), ohne lokale VR-PC-Farm im aktuellen FirefighterVR-/UKSH-Ansatz.
- Unreal Engine 5.7 als Produktionsengine (`NDFramework`, `NDVRActemium`).
- OpenXR, OpenXR Eye Tracker, OpenXR Hand Tracking, PICO OpenXR.
- Multiplayer / Sessions (Advanced Sessions, EOSCore im Framework; Planspiel-Peak intern 16 gleichzeitige Nutzer).
- Haptik: physische Objekte ins Tracking (Strahlrohr, Feuerlöscher-Adapter, CPR-Puppe, Industrieventile).
- Offline-Betrieb und lokales WLAN / lokaler Server.
- Desktop-3D-Ansicht zusätzlich zur Brille (UKSH-Angebot).
- Blicksteuerung und Eye-Tracking seit Stadttour Wilhelmshaven 2021/22; CSV-Export von Blick- und Interaktionslogs (ARiNeP).

### Digital Twin / Geospatial

- GodView: SvelteKit + Cesium, Google Earth 3D Tiles, Sentinel-2, Drohnen-Photogrammetrie, Punktwolken, GLB-Assets, Rollen/Orgs, PDF/JSON-Export, VR-Export.
- Hosting in Deutschland, DSGVO-Aussage auf godview.solutions.
- Photogrammetrie: Drohnenbefliegung, RealityCapture-Headless (`ND-Processing`), 3D Tiles, Potree (`nd-xyz-protree`, `www-pointclouds`).
- Volumenextraktion Punktwolke → LAS/LAZ.
- Extrem große Modelle: Kölner Dom mit **100.000+ Fotos und 1.000 Laserscans** (zitierfähig). Polygonzahl öffentlich 2 Mrd. — nicht unabhängig nachgezählt.

### Simulation

- Brandphysik / Löschangriff, Flashover, Waldbrand (FirefighterVR-Module).
- Physiologische Patientensimulation (Meditrain, Schockraum).
- Strahlenschutz mit Echtzeit-Dosimetrie (Radiation Protection VR, Evaluation UKK, ECR-Award laut Deck).
- Industrie-Verfahrensfolgen und Konsequenztraining (Actemium Infinity).
- Katastrophenlage 3D-Daten / Mapping (TEMA, Ahrtal).

### Software- und Systemlieferung

- All-in-one Hardwarekoffer, Pico Enterprise, Device Management.
- Web-Frontends der Vertikale (überwiegend SvelteKit/Vite).
- BMA-Trainer: Node/Express/Socket.IO, DIN 14675, Offline-Session (Produkt in Entwicklung, Live bmatraining.de laut Repo-README).
- Iterative Anpassung, Einweisung, Support DE/EN (UKSH-Angebot: Reaktion ≤ 4 h Werktags, 40 Personentage-Kontingent).

### Forschung / KI (belegt als Vorhaben, nicht als fertiges Allheilmittel)

- TEMA: semantische 3D-Karten, Extremdaten, XR-Interface für NDM (Horizon Europe, Partner).
- feir: KI-gestützte Generierung von VR-Führungsszenarien (BMBF-Verbund).
- Spot-KI: autonomer Roboterhund / Erfassung (KI-Transfer-Hub SH).
- GodView AI Inspect: experimenteller Riss-/Schadensfilter; SH-KI-Förderung in Einreichung.
- Pulse Engine / Sprachsteuerung für UKK als PFIF-Idee, nicht als ausgelieferte Standardfunktion.

## Stack-Überblick

| Schicht | Beleg |
|---|---|
| Unreal Engine 5.7, OpenXR, Pico | `NDFramework.uproject`, `NDVRActemium.uproject` |
| Cesium / SvelteKit / Postgres / MinIO / Docker | `ND-GodViewWeb` |
| RealityCapture, Node, Python, MinIO | `ND-Processing` |
| Potree / LAS | `nd-xyz-protree`, `www-pointclouds` |
| Vite/TS Marketing-Sites | `www-firefightervr` u. a. |
| Express/Socket.IO/Postgres | `www-bma-Trainer-App` |

## Was wir nicht als Standard behaupten

- Unity als Leit-Engine (nicht der lokale Hauptstack).
- IFC/BIM-Vollintegration in GodView (Roadmap, nicht fertig).
- Dass GodView die Headset-Trainingsanwendung sei.
- Dass jeder Auftrag den ganzen FirefighterVR-Katalog enthält.
