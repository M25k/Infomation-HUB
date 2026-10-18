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

`index.html` (Hero Baustelle/Inspektion, Features, FAQ, Preise), `feuerwehr.html` (Lagebild/Einsatz, Link zu firefightervr.de/trainings/planspiel/), `news.html`, `roadmap.html`, Impressum, Datenschutz. Umschalter **Bau & Inspektion** / **Einsatz & Feuerwehr** in der Navigation. Sprachumschalter auf derselben URL — **keine** eigene `/en/`-Site (im Gegensatz zu firefightervr.de/en/).

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
- Dom als Inspektionsbeispiel (100k Fotos + 1000 Scans nur wenn GF das hier öffentlich will; sonst auf meta-dom.de belassen)

## Nicht auf diese Site

- Linode, On-Prem als Standard
- TED/TEMA als GodView-App-Store
- Headset-Multiplayer-Peak 16 als GodView-Claim

## Standnotiz Monitoring (GodView Monitor, 18.10.2026)

- Repos in der Org Northdocks-GmbH: Landingpage `www-godview-landingpage` (Live-Stand inkl. `feuerwehr.html` noch nicht gepusht, letzter Commit 07.07.2026), App `ND-GodViewWeb` (letzter Commit 15.10.2026, live Version `2ef827e`). Ältere Repos: `ND-GodView` (2024) und `ND-CesiumTilesetViewer`.
- Login-Links der Landingpage zeigen auf `godview.nd-apps.de/auth`, die Feuerwehr-Edition mit `?edition=firefighter`.
- `app.godview.solutions` hat nur einen AAAA-Eintrag (nur IPv6), also für reine IPv4-Nutzer nicht erreichbar.
- App-Hilfe `/help`: 21 Themen; als Export ist nur PDF aus der Orthogonal-Ansicht dokumentiert. VR-Export daher nicht als dokumentierte Funktion nennen, bis die Hilfe ihn beschreibt.
- Roadmap auf der Landingpage: 5 Module (Smarte Inspektion, Baulogistik und Kranplanung, Mobiles Fototagging, 2D-Abwicklung zylindrischer Bauwerke, Photogrammetrie). Roadmap ist kein Lieferumfang.
- Preise live: 119 €/Monat, Module Inspect und Bautagebuch je +49 €, Feuerwehr auf Anfrage.
