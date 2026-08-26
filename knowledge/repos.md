# Lokale Git-Repositories

Alle unter `C:\Githup`, erfasst 2026-08-26. Organisation: überwiegend `Northdocks-GmbH` auf GitHub. `Infomation-HUB` und `www-meta-dom` liegen unter `M25k`.

Zum Verstehen von Technik und Liefergegenstand diese Repos lesen, nicht raten.

## Produkt- und Plattformcode

| Ordner | Remote | Branch | Was es belegt |
|---|---|---|---|
| `NDFramework` | Northdocks-GmbH/NDFramework | main | Unreal 5.7: OpenXR + PICOOpenXR aktiv; Plugins NDVRCore, NDFire, NDGeo, CesiumForUnreal, AdvancedSessions, EOSCore, SmoothSync. OpenXREyeTracker/HandTracking im uproject **disabled**. |
| `NDVRActemium` | Northdocks-GmbH/NDVRActemium | 5.7_update | Factory/Infinity, Unreal 5.7; `PICOOpenXR` aktiv, Legacy-`PicoXR` **disabled**. TargetPlatforms im uproject: Android. README leer. |
| `ND-GodViewWeb` | Northdocks-GmbH/ND-GodViewWeb | master | GodView SvelteKit+Cesium, Docker, DE-Hosting, `app.godview.solutions` |
| `ND-Processing` | Northdocks-GmbH/ND-Processing | Standalone | Photogrammetrie RealityCapture → 3D Tiles, Cesium-Viewer |
| `ND-Strahlensimulation` | Northdocks-GmbH/ND-Strahlensimulation | public GitHub, nicht in C:\Githup | Unreal **4.27**-Projekt `NDRaySimulation.uproject`, Plugin `RaySimulation`. Historische Dosimetrie-Linie für Strahlenschutz VR — **nicht** die aktuelle UE-5.7-Produktionsengine |
| `TEMA-Server` | Northdocks-GmbH/TEMA-Server | main | Checkout vorhanden, Arbeitsbaum praktisch leer — Inhalt nachziehen |
| `nd-xyz-protree` | Northdocks-GmbH/nd-xyz-protree | main | XYZ → Potree |
| `www-pointclouds` | Northdocks-GmbH/www-pointclouds | main | Potree-Viewer, LAS-Extraktion; Szenen Dom / Holcim / Bürrig |
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

Diese lokalen Pfade sollen als Workspace-Referenz dienen, wenn Anträge Technik belegen. Information-HUB bleibt die kanonische Textquelle; die anderen Repos sind Beweis, kein zweites Firmenprofil.

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

## Lücken (nächste Loop-Runde)

- Unreal-Content-Projekte (FFVR-Szenen) nicht unter `C:\Githup` als eigenes Repo. Drive-Ordner `ND-AssetReferenz` enthält `NDAssetReferenz.uproject` (Stand 2025) — nicht als Git-Remote.
- National-Guard-App intern **State of Emergency** (Asana, kombiniertes Unreal-Projekt) — Content-Repo nicht unter `C:\Githup` gefunden.
- `gh` CLI fehlt; `ND-Strahlensimulation` weiter nicht lokal (GitHub-Stand UE 4.27, siehe oben).
- `TEMA-Server` praktisch leer; TEMA-Betrieb läuft u. a. über GodView (BRK) und XR Viewer (KPI Immersion, Trials 2026).
- Xing-Tippfehler `firefighervr.de` nicht zitieren.
