# Git-Repositories

**Kanonisch ist GitHub**, nicht die Festplatte. Org: [Northdocks-GmbH](https://github.com/Northdocks-GmbH) (fast alles privat). `Infomation-HUB` und `www-meta-dom` unter `M25k`. Cursor hat den GitHub-Zugang — Repos, die hier fehlen, dort öffnen oder klonen, nicht als „existiert nicht“ behandeln.

`C:\Githup` ist nur eine **Teilmenge** (22 Ordner, Stand 30.08.2026). Viele Org-Repos sind nicht ausgecheckt. Öffentlich ohne Login sichtbar u. a. `ND-Strahlensimulation`; der Rest braucht den Cursor-/GitHub-Login.

Zum Verstehen von Technik und Liefergegenstand: zuerst lokal, sonst **GitHub über Cursor**. Nicht raten.

## Zugriff

| Wo | Wann |
|---|---|
| `C:\Githup\{Name}` | wenn der Ordner da ist |
| `https://github.com/Northdocks-GmbH/{Name}` | immer die volle Kopie; in Cursor als GitHub-Projekt / Clone |
| Drive `ND-AssetReferenz` | FFVR-Szenen, kein Git-Remote |

Nicht lokal, aber auf GitHub / in Asana-Repo-Karten (nicht „Lücke weil nicht auf der Platte“):

| Remote | Hinweis |
|---|---|
| `Northdocks-GmbH/ND-Strahlensimulation` | öffentlich, UE 4.27 `NDRaySimulation` — historisch, nicht 5.7-Produktion |
| `Northdocks-GmbH/TUHH-SensorViz` | Asana Repo-Info; CSV-Importer |
| `Northdocks-GmbH/TUHH-SensorVizCN` | China-Folge, Format wie TUHH |
| State of Emergency / FFVR-Content | Remote in Asana; nicht unter `C:\Githup` |

## Produkt- und Plattformcode

| Ordner | Remote | Branch | Was es belegt |
|---|---|---|---|
| `NDFramework` | Northdocks-GmbH/NDFramework | main | Unreal 5.7: OpenXR + PICOOpenXR aktiv; Plugins NDVRCore, NDFire, NDGeo, CesiumForUnreal, AdvancedSessions, EOSCore, SmoothSync. OpenXREyeTracker/HandTracking im uproject **disabled**. Im Plugins-Ordner zusätzlich NDWidgets, NDCommonAssets, ND_LookDev, NDEditorTools, CharacterSetup, NDVRTutorial (uproject disabled), NDAuth (disabled), VaRest, **VRSpectatorUtilities** (Ordner lokal, **nicht** im uproject — nicht als Feature). `NDGeo` hängt an GeoReferencing + WebBrowserWidget. |
| `NDVRActemium` | Northdocks-GmbH/NDVRActemium | 5.7_update | Factory/Infinity, Unreal 5.7; `PICOOpenXR` aktiv, Legacy-`PicoXR` **disabled**. `ElevenVoice` im uproject enabled (intern Standard-TTS der meisten XR-Sprachen; nicht Fulldome, nicht Stadttouren). Plugin-Dateien **nicht** im Checkout. `McpAutomationBridge` im uproject **enabled** — interne Editor-/Agent-Brücke, **kein** Kundenfeature. TargetPlatforms: Android. README leer. |
| `ND-GodViewWeb` | Northdocks-GmbH/ND-GodViewWeb | master | GodView SvelteKit+Cesium, pnpm/Lerna, Docker, Node 20+. Dieselbe App unter `https://app.godview.solutions` **und** `https://godview.nd-apps.de` (kein Redirect). Deploy per `deploy.sh`, nicht GitHub Actions. Tokens/.env nicht zitieren. |
| `www-pointclouds` | Northdocks-GmbH/www-pointclouds | main | Zweite GodView-Schicht: Potree-Viewer + Express (:3001), LAS/LAZ-Extraktion. Szenen u. a. Kölner Dom, Holcim Höver, Currenta Bürrig. Punktdaten nicht im Git (R2/lokal). Öffentlicher Viewer-Host intern `pointclouds.nd-apps.de`. |
| `ND-Processing` | Northdocks-GmbH/ND-Processing | Standalone | Photogrammetrie RealityCapture → 3D Tiles, Cesium-Viewer |
| `ND-Strahlensimulation` | Northdocks-GmbH/ND-Strahlensimulation | **nicht lokal** — GitHub/Cursor | Unreal **4.27**-Projekt `NDRaySimulation.uproject`, Plugin `RaySimulation`. Historische Dosimetrie-Linie für Strahlenschutz VR — **nicht** die aktuelle UE-5.7-Produktionsengine |
| `TEMA-Server` | Northdocks-GmbH/TEMA-Server | main | Checkout vorhanden, Arbeitsbaum praktisch leer — Inhalt nachziehen |
| `nd-xyz-protree` | Northdocks-GmbH/nd-xyz-protree | main | XYZ → Potree |
| `XLR-Punktwolken-Converter` | Northdocks-GmbH/XLR-Punktwolken-Converter | main | Konverter (README fehlt) |
| `ND-Website` | Northdocks-GmbH/ND-Website | master | ältere Website? README leer |
| `www-ar` | Northdocks-GmbH/www-ar | main | AR-Web, kein README |

## Vertical-Websites

| Ordner | Remote | Live-URL |
|---|---|---|
| `www-northdocks` | Northdocks-GmbH/www-northdocks | northdocks.com |
| `www-firefightervr` | Northdocks-GmbH/www-firefightervr | **https://firefightervr.de/** (Canonical). Alias firefightervrmobile.de |
| `WWW-meditrain-vr` | Northdocks-GmbH/WWW-meditrain-vr | meditrainvr.com |
| `WWW-next-factory-vr` | Northdocks-GmbH/WWW-next-factory-vr | nextfactoryvr.com |
| `WWW-spearhead-vr` | Northdocks-GmbH/WWW-spearhead-vr | spearheadvr.de |
| `www-storywalx` | Northdocks-GmbH/www-storywalx | storywalx.com |
| `www-meta-dom` | M25k/www-meta-dom | meta-dom.de |
| `www-godview-landingpage` | Northdocks-GmbH/www-godview-landingpage | godview.solutions |
| `www-strahlenschutzvr` | Northdocks-GmbH/www-strahlenschutzvr | Strahlenschutz-Landing |
| `www-handaufsherz` | Northdocks-GmbH/www-handaufsherz | **https://handaufsherz-vr.de/** Schul-CPR (Launch/Warteliste). Vertical-Mail `info@handaufsherz-vr.de` — Firmenstandard bleibt kontakt@northdocks.com |
| `www-bma-Trainer-App` | Northdocks-GmbH/www-bma-Trainer-App | bmatraining.de |

## Cursor-Codebases (Referenz)

Information-HUB bleibt die Textquelle. Technik belegen: lokaler Ordner **oder** dasselbe Repo über GitHub in Cursor. Die Liste unten ist die lokale Teilmenge, kein Inventar der Org.

| Pfad | Nutzen für Anträge |
|---|---|
| `C:\Githup\Infomation-HUB` | Claims, Playbook, Skill |
| `C:\Githup\NDFramework` | Unreal 5.7, OpenXR, Pico, Multiplayer |
| `C:\Githup\NDVRActemium` | Factory/Infinity |
| `C:\Githup\ND-GodViewWeb` | GodView-Plattform, Hosting |
| `C:\Githup\ND-Processing` | Photogrammetrie RealityCapture |
| `C:\Githup\www-pointclouds` | Potree, Dom/Holcim/Bürrig |
| `C:\Githup\www-firefightervr` | Öffentlicher Katalog, Canonical-Site |
| `C:\Githup\www-bma-Trainer-App` | BMA DIN-14675 MVP |

## Wie Repos in Anträgen nutzen

- Engine- und Plugin-Listen aus `.uproject`, nicht aus Marketingtext.
- GodView-Hosting und Domains aus `ND-GodViewWeb/README.md`.
- Photogrammetrie-Workflow aus `ND-Processing/.agent/SKILL_nd_processing.md`.
- BMA-DIN-Claim nur, wenn das Repo/Produkt gemeint ist, nicht als FirefighterVR-Standardmodul.

## Lücken (nicht: „fehlt lokal“)

- FFVR-Szenen: Drive `ND-AssetReferenz` (`NDAssetReferenz.uproject`, Stand 2025) — kein Git-Remote.
- **State of Emergency**: Asana-Repo-Karte; über GitHub/Cursor suchen, nicht nur `C:\Githup`.
- `TEMA-Server` Checkout lokal fast leer — Remote auf GitHub nachziehen.
- `gh` CLI fehlt auf diesem Rechner; Org-Liste über Cursor-GitHub oder die Website. Private Repos sieht die öffentliche API nicht.
- Xing-Tippfehler `firefighervr.de` nicht zitieren.
