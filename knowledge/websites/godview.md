# godview.solutions

Canonical: https://godview.solutions/  
App: `app.godview.solutions` (auch `godview.nd-apps.de`)  
Repo: `C:\Githup\www-godview-landingpage`

Rolle: Browser-Digital-Twin. **Eine Plattform, zwei Kundentypen.** Die Live-Landing ist 2026 fast nur Typ A.

| Typ | Nutzer | Inhalt |
|---|---|---|
| **A — Bauinspektion** | Dom, Bauleitung, Facility | Photogrammetrie, Punktwolke, Messung, Risse, Doku |
| **B — Einsatz / Kommando** | Feuerwehr, Werkfeuer, Katastrophenschutz | Lagebild, Twin des Einsatzraums, Leitung analog Planspiel |

## Ist-Struktur

`index.html` (Hero Baustelle/Inspektion, Features, FAQ, Preise), `feuerwehr.html` (Lagebild/Einsatz, Link zu firefightervr.de/trainings/planspiel/), `news.html`, `roadmap.html`, Impressum, Datenschutz. Umschalter **Bau & Inspektion** / **Einsatz & Feuerwehr** in der Navigation. **Entschieden (Joachim, 20.10.2026, über Web):** Der Umschalter ist freigegeben; „Einsatz & Feuerwehr“ bleibt in der Navigation von index, news und roadmap (Link auf feuerwehr.html), beide Bereiche (Bau sowie Einsatz & Feuerwehr) werden auf godview.solutions aktiv beworben. Die Chat-Entscheidung vom 13.09.2026 (Feuerwehr-Links aus der Bau-Navigation entfernt) gilt nicht mehr. Sprachumschalter auf derselben URL — **keine** eigene `/en/`-Site (im Gegensatz zu firefightervr.de/en/).

Kontakt live: **kontakt@northdocks.com**, Telefon **+49 (0) 2173 9996715**, Mo.–Fr. 9:00–13:00. `godview@…` nicht verwenden.

Öffentliche Preise Typ A: Basis 119 €/Monat, Module +49 €.

Hosting-Aussage auf der Site: Deutschland, DSGVO. Intern Linode / DLR-On-Prem **nicht** auf die Site.

## Soll-Struktur (Inhaltliche Erweiterung)

1. Typ A unverändert klar (das ist der aktuelle öffentliche Stand).
2. **Typ B ergänzen**, ohne zwei Produkte zu erfinden: eine Plattform, zweite Nutzung „Lage / Einsatz / Kommando“. Anker: Planspiel/Playground, Chempark Bürrig, DRZ nur wenn öffentlich gewollt.
3. Nie behaupten, GodView sei die Unreal-Trainingsapp auf dem Headset. Headset = Training; GodView = Twin + Leitung/Inspektion.
4. VR-Export und 3D Tiles (auch kundeneigene Tilesets, analog FFVR-FAQ) sind Produktfeatures, kein FirefighterVR-Katalog.
5. Englisch: entweder vollwertige EN-Texte oder klarer Umschalter; keine halben Strings.
6. Kontakt: kontakt@northdocks.com, Telefon Hub **+49 (0) 2173 9996715**. `godview@…` nicht zum Firmenstandard machen.

## Öffentlich sagbar

- Cesium, 3D Tiles, Drohnen, Punktwolken, Messung, Team, Export, DE-Hosting-Aussage
- Preise wie auf der Site
- Dom als Inspektionsbeispiel (öffentlich laut claims.md, Joachim 21.10.2026: mehr als 200.000 Fotos und 1.000 Laserscans aufgenommen, aktuelles Modell rund 100.000 Fotos und über 2 Mrd. Polygone; getrennt nennen)

## Nicht auf diese Site

- Linode, On-Prem als Standard
- TED/TEMA als GodView-App-Store
- Headset-Multiplayer-Peak 16 als GodView-Claim

## App app.godview.solutions (intern, Cursor-Chat ND-NB-20, Abgleich 20.10.2026)

- **Zwei Editionen in einer App:** generisches GodView (Bau/Inspektion) und **GodView Firefighter** (eigenes Produkt mit FFVR-CI/Logo, eigenem Asset-Katalog, Registrierung mit `?edition=firefighter`). Produkte verlinkt, aber getrennt; **kein Embedding** in firefightervr.de (Chat 12.09.2026). Globus-Stil „Platte“ (stilisierte Planspielplatte aus OSM-Footprints) nur in der Firefighter-Edition; generisch: kein Globus / ohne / mit Terrain / Google Earth. Assetnamen der Firefighter-Edition nach FFVR-Playground-Objektliste.xlsx.
- **Lage-Funktionen (Firefighter):** Führungsebene beim Anlegen (Gruppenführer, Zugführer, Verbandsführer), Fahrzeug-Labels ELW 1/ELW 2, Lagephasen (Start, Anfahrt …), Feuer-/Rauch-Effekte, Export von Lagen ins FFVR-Planspiel. Grundlage: Janis-Feedback (Asana) und `_ref/planspiel`. Offen: Cap für Lage-Partikel.
- **Soft-Umzug auf app.godview.solutions:** beide Hosts parallel, kein Redirect; Origin aus Host/X-Forwarded-Proto, Mails über `APP_PUBLIC_URL`. Cookies host-only, Nutzer müssen sich auf dem neuen Host neu anmelden. Unreal-/VR-Exportlinks auf godview.nd-apps.de bleiben gültig. Asana-Task „Domain Umzug nach app.godview.solutions“ offen (DNS/Zertifikat serverseitig ausstehend).
- **Deploy:** Produktion nur per `deploy.sh`; es holt `origin/master` per Fast-Forward, lokale Commits müssen vorher gepusht sein, sonst baut der Server den alten Stand. Lokal `Start-DevEnv.ps1`. GitHub-Actions-Weg ungenutzt.
- **Super-Admin-Login mit E-Mail-Code (2FA)** seit 26.09.2026 (Migration 037).
- **News-Seiten in der App** als Vorstufe eines Feature-Newsletters (Hinweiskarte unten).
- **Geplant:** native/Unreal-App (zuerst Android-Tablets) mit Login und Datenabgleich zum GodView-Server; Handshake noch nicht gebaut. Seite „Einladungslink ungültig“ statt 404 gebaut, Deploy ausstehend.
- Kölner-Dom-Zahl offen, siehe [../open-questions.md](../open-questions.md).

## Standnotiz Monitoring (GodView Monitor, 18.10.2026)

- Repos in der Org Northdocks-GmbH: Landingpage `www-godview-landingpage` (Live-Stand inkl. `feuerwehr.html` noch nicht gepusht, letzter Commit 07.07.2026), App `ND-GodViewWeb` (letzter Commit 15.10.2026, live Version `2ef827e`). Ältere Repos: `ND-GodView` (2024) und `ND-CesiumTilesetViewer`.
- Login-Links der Landingpage zeigen auf `godview.nd-apps.de/auth`, die Feuerwehr-Edition mit `?edition=firefighter`.
- `app.godview.solutions` hat nur einen AAAA-Eintrag (nur IPv6), also für reine IPv4-Nutzer nicht erreichbar.
- App-Hilfe `/help`: 21 Themen; als Export ist nur PDF aus der Orthogonal-Ansicht dokumentiert. VR-Export daher nicht als dokumentierte Funktion nennen, bis die Hilfe ihn beschreibt.
- Roadmap auf der Landingpage: 5 Module (Smarte Inspektion, Baulogistik und Kranplanung, Mobiles Fototagging, 2D-Abwicklung zylindrischer Bauwerke, Photogrammetrie). Roadmap ist kein Lieferumfang.
- Preise live: 119 €/Monat, Module Inspect und Bautagebuch je +49 €, Feuerwehr auf Anfrage.
