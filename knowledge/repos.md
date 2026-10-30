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

## Intranet „Sanctum“ (in Aufbau, Patrick)

Interner Kontext (Weekly 21.10.2026, Transkript gegengeprüft; übermittelt von One): Patrick baut ein lokales Intranet „Sanctum“ auf Proxmox, lokales Git als Single Point of Truth. Module: **Asgard** (CRM), **Wakanda** (MDM), **Heimdall** (Rechte), **Bifrost** (Verbindungen). Das Team in Kiel soll Zugriff bekommen. Schnittstellen zum Infomation-HUB entscheidet Joachim; bis dahin keine Kopplung.

**Headset-MDM** (Joachim 26.10.2026 (über One)): vorerst bei Pico (Business Device Manager); ein eigenes MDM ist **kein aktuelles Ziel**. Das Modul Wakanda (MDM) oben ist damit für Headsets zurückgestellt. Im Gespräch Joachim/Patrick am 26.10.2026 klang noch „Brillenverwaltung unter eigene Kontrolle“ an; es gilt die Entscheidung von 17:02.

**Netzwerk Kiel** (Joachim 24.10.2026 im Asana-Ticket „W1021-18–20 Follow-ups“, über One 26.10.2026): Kiel hat Business-Leitungen mit festen IP-Adressen ohne Modem-Notwendigkeit; die **FRITZ!Box kann weg**. Das ersetzt Patricks Vorschlag vom 23.10.2026, die FRITZ!Box als Router zu behalten. Router/VPN laufen über eigene Asana-Tickets (Router VP2430e, VPN Kiel–Monheim). Keine IP-Adressen ins Repo. **Router Kiel** (Joachim 26.10.2026 (über One)): Erst im Büro Kiel nach DDR4-Teilen suchen. Gibt es welche, den Protectli VP2430e (braucht DDR5) gegen ein DDR4-Vorgängermodell tauschen; sonst den VP2430e behalten und DDR5 kaufen (Asana 1219858236498643).

## Produkt- und Plattformcode

| Ordner | Remote | Branch | Was es belegt |
|---|---|---|---|
| `NDFramework` | Northdocks-GmbH/NDFramework | main | Unreal 5.7: OpenXR + PICOOpenXR aktiv; Plugins NDVRCore, NDFire, NDGeo, CesiumForUnreal, AdvancedSessions, EOSCore, SmoothSync. OpenXREyeTracker/HandTracking im uproject **disabled**. Im Plugins-Ordner zusätzlich NDWidgets, NDCommonAssets, ND_LookDev, NDEditorTools, CharacterSetup, NDVRTutorial (uproject disabled), NDAuth (disabled), VaRest, **VRSpectatorUtilities** (Ordner lokal, **nicht** im uproject — nicht als Feature). `NDGeo` hängt an GeoReferencing + WebBrowserWidget. |
| `NDVRActemium` | Northdocks-GmbH/NDVRActemium | 5.7_update | Factory/Infinity, Unreal 5.7; `PICOOpenXR` aktiv, Legacy-`PicoXR` **disabled**. `ElevenVoice` im uproject enabled (intern Standard-TTS der meisten XR-Sprachen; nicht Fulldome, nicht Stadttouren). Plugin-Dateien **nicht** im Checkout. `McpAutomationBridge` im uproject **enabled** — interne Editor-/Agent-Brücke, **kein** Kundenfeature. TargetPlatforms: Android. README leer. |
| `ND-GodViewWeb` | Northdocks-GmbH/ND-GodViewWeb | master | GodView SvelteKit+Cesium, pnpm/Lerna, Docker, Node 20+. Dieselbe App unter `https://app.godview.solutions` **und** `https://godview.nd-apps.de` (kein Redirect). Deploy per `deploy.sh`, nicht GitHub Actions. Tokens/.env nicht zitieren. |
| `www-pointclouds` | Northdocks-GmbH/www-pointclouds | main | Zweite GodView-Schicht: Potree-Viewer + Express (:3001), LAS/LAZ-Extraktion. Szenen u. a. Kölner Dom, Holcim Höver, Currenta Bürrig. Punktdaten nicht im Git (R2/lokal). Öffentlicher Viewer-Host intern `pointclouds.nd-apps.de`. |
| `ND-Processing` | Northdocks-GmbH/ND-Processing | Standalone | Photogrammetrie RealityCapture → 3D Tiles, Cesium-Viewer |
| `ND-Strahlensimulation` | Northdocks-GmbH/ND-Strahlensimulation | **nicht lokal** — GitHub/Cursor | Unreal **4.27**-Projekt `NDRaySimulation.uproject`, Plugin `RaySimulation`. Historische Dosimetrie-Linie für StrahlenschutzVR — **nicht** die aktuelle UE-5.7-Produktionsengine |
| `TEMA-Server` | Northdocks-GmbH/TEMA-Server | main | Checkout vorhanden, Arbeitsbaum praktisch leer — Inhalt nachziehen |
| `nd-xyz-protree` | Northdocks-GmbH/nd-xyz-protree | main | XYZ → Potree |
| `XLR-Punktwolken-Converter` | Northdocks-GmbH/XLR-Punktwolken-Converter | main | Konverter (README fehlt) |
| `ND-Website` | Northdocks-GmbH/ND-Website | master | ältere Website? README leer |
| `www-ar` | Northdocks-GmbH/www-ar | main | AR-Web, kein README |

### Unreal-Projekte: Ablage (Unreal Build, 27.10.2026)

- Alle Unreal-Projekte liegen auf GitHub in der Org Northdocks-GmbH mit **Git LFS**; Perforce ist nicht bekannt.
- **NDFramework:** Northdocks-GmbH/NDFramework, **UE 5.7.4**; Wechsel auf UE 5.8 geplant (bestätigt; siehe W1021-28).
- **Build-Engine:** Northdocks baut nicht mehr mit UE 4.27; Build-Engine auf nd-pc-25 ist UE 5.8 (Joachim 28.10.2026 17:01, laut One). Projekt-Engine-Versionen einzelner Repos (z. B. NDFramework UE 5.7.4, ND-Strahlensimulation UE 4.27 historisch) bleiben als Fakten stehen.
- **FFVR-Repos laut GitHub-Suche:** FFVR-InteriorAttack, FFVR-CPR2024, FVR-CalifWildfire, FVR-Firesaber, FVR-Scouting, NDFireSystemV3 (alle Northdocks-GmbH).
- **Dräger-Port (UE 5.8, Mobile):** nach bestandener Prüfung mit normalen Commits in den Branch `ue58-mobile`, ohne zusätzliche Git-Regeln (Joachim 29.10.2026 19:43 direkt im Chat von One: „5. Sehr gut“ auf Ones Vorschlag; Wortlaut laut One).
  - **Dräger-Port-Freigabe** („alle daten die mit draeger zusammen hanegen sind fuer den gesammten port der gamingwelt freigegeben“ (Joachim 30.10.2026 09:02 direkt im Chat von One, Antwort auf Ones Punkt 2 zu Dräger-Fremd-Content und CAD-Daten)): Alle Daten mit Dräger-Bezug sind für den gesamten Port der Dräger Gaming Welt freigegeben, laut One ausdrücklich auch Fremd-Content (laut One 339 Assets, 1,37 GB) und CAD-Daten. Die Freigabe gilt nur für den **internen Port** (Arbeit in Repo, Drive und auf den Arbeitsrechnern); Veröffentlichen oder externes Teilen braucht weiter Joachims OK (Regel „Datenzugriff in Firmenkonten“, Joachim 29.10.2026 09:06/09:07, [README](../README.md)). Bestehende Dräger-Einschränkungen (nur intern, Regel 11, #73) bleiben für alle anderen Zwecke bestehen. Siehe auch [assets/README.md](assets/README.md) Regel 11 und [assets/tabu.md](assets/tabu.md).
  - **Repo neu angelegt 30.10.2026:** [Northdocks-GmbH/NDDraegerGW](https://github.com/Northdocks-GmbH/NDDraegerGW). Das alte Repo existierte nicht mehr („it looks like the repo dosent exits anymore“ (Joachim 30.10.2026 08:52 direkt im Chat von One); „i created the a repo again: https://github.com/Northdocks-GmbH/NDDraegerGW“ (Joachim 30.10.2026 08:54 direkt im Chat von One)). `main` wird aus der alten Historie in Repos_Alt (Drive, vollständiges .git inkl. LFS, Stand 09.04.2025, UE 4.27, laut Assets 30.10.2026) wiederhergestellt; der Port läuft auf Branch `ue58-mobile` (laut One).
  - **Ziel:** ganze Feuerwache, keine ATÜ-Strecke als eigenes Level; zuerst Android-Build im Emulator; PICO-Plugin installiert („die atue strecke ist fuer uns als sperates level nicht relevant wir wollen die gane fuerwache ich habe das pico plugin installiert. aber uns reicht auch erstmal android das wir im android simulator testen koennen.“ (Joachim 30.10.2026 08:42 direkt im Chat von One)). Reihenfolge: zuerst sinnvolle Polygonzahlen, LODs zuletzt (laut One).
  - **Git-Zugang auf nd-pc-25:** über den Git Credential Manager, Joachim meldet sich selbst an; keine Secrets im Repo oder HUB (laut One; Joachim 30.10.2026 08:48 direkt im Chat von One: „regarding git i dont see what wrong lets setup acces keys“). Cursor-GitHub-App hat bereits Zugriff auf alle Repos („it is allready on all repositories“ (Joachim 30.10.2026 08:45 direkt im Chat von One)).
- **Repos_Alt (Projektkopien nicht mehr auf GitHub):** Drive-Ordner [Repos_Alt](https://drive.google.com/drive/folders/1OnU8sDqDMPVyViekb7LbBw_3RrNSCfeW) („copies of the projects that are now longer on git are here“ (Joachim 30.10.2026 08:53 direkt im Chat von One)). Inhalt laut Assets 30.10.2026 (Stand 09.04.2025): AC-ACHEMA-Arena, ND-AssetReferenz, ND-CUR-Arena, ND-Landtag-Touch, NDDraegerGW, NDVR-Trier-Content, NDVR-Wilhelmshaven-Content, egeb-arena.
- **Offen:** welches das aktuelle FFVR-Haupt-Repo bzw. die Feuersimulation ist und welcher Branch (Frage an Moritz bzw. Joachim; W1021-17, assets/open-questions #21). Für das Hygiene-Projekt wurde kein Repo gefunden.

### Unreal-MCP: Regeln (Weekly 28.10.2026)

- **Toolset-Plugins nur gezielt aktivieren** (Weekly 28.10.2026, 00:14:15–00:15:02, laut One; W1028-14): Der Unreal-MCP kann nur mit freigeschalteten Toolset-Plugins arbeiten (z. B. das Niagara-Toolset für Niagara). Nur die Toolsets einschalten, die die Aufgabe braucht, nicht alle. Stand: Testprojekt auf UE 5.8, Unreal-MCP läuft.
- **Zuerst prüfen, ob der Unreal-MCP geladen ist** (Weekly 28.10.2026, 00:15:04–00:15:49, laut One; W1028-15): Nach dem Start von Cursor wird der MCP oft nicht erkannt, der Agent weicht dann auf Python aus. Regel: Der Agent prüft vor der Arbeit zuerst, ob der Unreal-MCP geladen ist; wenn nicht, bricht er ab. In Cursor den Unreal-MCP auf „immer an“ stellen; die Regel gehört in die Agent-MD-Datei des Projekts.

### NDFramework Build-Setup (nur intern)

Unreal Engine **5.7**, C++-Projekt. Ziel Android **Arm64**, **Vulkan**, Target API **34**, Plugin **PICOOpenXR**. Fab-Plugins: CesiumForUnreal, EOSCore, SmoothSyncPlugin, JsonXmlHelper, NodeGraphAssistant, VaRest. Offen: Bezugsweg der Fab-Plugins (Lizenzkonto), Package-Name, Rotation des Android-Keystores. Keine Keystore-Dateien oder Passwörter ins Git.

### Unreal: Stand aus Cursor-Chat ND-NB-20 (intern, Abgleich 20.10.2026)

- **NDFramework (UE 5.7):** Setup wie oben. `BP_NDVR_Hand` ist auf die leere C++-Basis `ANDVRHandBase` reparented; eine volle C++-Migration geht nicht ohne Editorarbeit.
- **VaRest:** `VaRest.uplugin` lokal auf EngineVersion 5.7.0 gesetzt, aber gitignored. **Offen:** Plugin vendoren (ins Repo übernehmen), sonst fehlt es auf anderen Rechnern.
- **NDVRActemium:** laut Chat richtiger Branch 5.7 (Tabelle oben: `5.7_update`, prüfen), ElevenVoice installiert, Lookdev-Wunsch AO-Look.
- **State of Emergency:** wird **eine** Quest-3-App; konsolidiertes USD-Angebot an Vincent Vallos (TMA); Jet-Pipe-Tracking prüfen.
- **FlowAR (Kotlin/ARCore):** Basis für AR mit QR-Ankern (Fresenius/Wasserwerk), Spin-off-Idee „Firefighter AR“.
- **GodView-App (ND-GodViewWeb):** Deploy und Editionen siehe [websites/godview.md](websites/godview.md).

## Vertical-Websites

| Ordner | Remote | Live-URL |
|---|---|---|
| `www-northdocks` | Northdocks-GmbH/www-northdocks | northdocks.com |
| `www-firefightervr` | Northdocks-GmbH/www-firefightervr | **https://firefightervr.de/** (Canonical). Alias firefightervrmobile.de |
| `www-feuerwehrvr.de` | Northdocks-GmbH/www-feuerwehrvr.de (prüfen Remote-Name) | **https://feuerwehrvr.de/** Shopify Checkout / Funnel |
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

## Bot-Verzeichnis (im Aufbau)

Bisher nur hier gelistet; weitere Bots (One, Video, Assets, Social, Web, 3D, Pico Native, BMA App, GodView App, Unreal Build, Wissen) werden nachgetragen.

| Bot | ID | Aufgabe | Zugriff |
|---|---|---|---|
| **IT** | `49ab7f47-f3d5-473c-8086-c5bd4b36dd8a` | Seit 26.10.2026 aktiv. Reine Lese-Health-Checks der Grok-Bot-Rechner ND-PC-80, Video-PC und ND-NB-20; ab 27.10.2026 in Ones Runde | Nur lesend; keine Änderungen an den Rechnern. Keine Adressen und Zugangsdaten im Repo |
| **GV Render** | `4d6c85c6-839e-402a-9b0b-e1d662dc44e2` | Baut `gv-render`, einen nativen Renderer (vsgCs / VulkanSceneGraph / cesium-native) nur für GodView-Cesium-Tiles; Details [brand/godview.md](brand/godview.md) | Nur Lesezugriff auf die Cesium-Test-Organisation „ND Testlabor“ mit eigenem Viewer-Login; keine Produktivdaten. Test auf dem Video-PC, finale Renders auf dem neuen Windows-PC mit RTX 4090 |
| **Unreal Assets** | `d9294990-a368-4b30-a42f-e1d54092f7d6` | Seit 28.10.2026: lädt und prüft 3D-Assets in Unreal 5.8 für Mobile VR (Pico 4 Ultra), Reviews z. B. HLF20, keine App- oder Funktionsentwicklung | laut One 29.10.2026 |

Quelle: GV Render (Joachim 23.10.2026, übermittelt von One); IT (One, Runde 27.10.2026).

## GPU-Rechner: gemeinsame Sperre (seit 18.10.2026)

**Neu (Joachim im Chat mit One, 20.10.2026):** Der GodView-AI-Inspect-PC bekommt 2 GPUs mit je 96 GB VRAM. Modelle mit hohem VRAM-Bedarf werden auf diesen PC **vertagt, nicht verworfen**. Modellerstellung (Image-to-3D, CAD) macht der Bot 3D, Rendern weiter Video.

Der GPU-Rechner (MSI, Ubuntu, RTX 4070 Laptop 8 GB) wird von mehreren Bots genutzt: Video (auch 3D-Renderings und Turntables, seit 18.10.2026) und Wissen. Damit sich Jobs nicht gegenseitig den Grafikspeicher wegnehmen, gilt für jeden GPU-Job:

1. Vorher mit `nvidia-smi` prüfen, ob die GPU frei ist, und in `~/gpu-jobs/lock` schauen.
2. Ist die GPU frei und gibt es keine gültige Sperre, eine Zeile nach `~/gpu-jobs/lock` schreiben: Bot, Start, erwartetes Ende, Job.
3. Nach dem Job `~/gpu-jobs/lock` löschen und eine Zeile an `~/gpu-jobs/log.txt` anhängen.
4. Eine Sperre, deren erwartetes Ende mehr als 30 Minuten zurückliegt, gilt als verwaist und darf übernommen werden (Eintrag im Log).
5. Lange Warteschlangen (z. B. Whisper-Transkription) setzen die Sperre pro Datei, damit andere Bots zwischendurch drankommen.

Vorschlag Northdocks Video, übernommen 18.10.2026.

