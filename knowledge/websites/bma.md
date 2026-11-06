# bmatraining.de (BMA Trainer)

Repo: `C:\Githup\www-bma-Trainer-App`  
DIN 14675 Web-MVP (FAT/FBF). Eigenes Produkt, **kein** FirefighterVR-Headset-Modul.

## Vorgabe

Derzeit **keine Vermarktung**. Keine Landingpage-Kampagnen, keine Paketpreise, nicht in northdocks.com-Vertikale aufnehmen. **SEO für bmatraining.de darf weiterlaufen** (Joachim, 20.10.2026, über BMA App).

Perspektive intern: Funnel zu FirefighterVR (z. B. WebXR). Erst wenn GF Vermarktung frei gibt, diese Datei aktualisieren.

## Falls die bestehende App-Oberfläche geändert wird

- DIN-14675-Bezug nur so weit, wie das Repo/Produkt das hergibt
- Nicht als eines der 23 FFVR-Module listen
- Impressum GmbH laut [_shared.md](_shared.md)
- Keine Portal-Passwörter oder Testaccounts ins Frontend

## Standnotiz Monitoring (BMA Trainer Monitor, 17./18.10.2026)

- Live unter https://bmatraining.de als eigene Marke, tritt nicht als FirefighterVR-Modul auf. Repo `Northdocks-GmbH/www-bma-Trainer-App` (privat, Default-Branch `main`).
- Stack: Node/Express, PostgreSQL, Socket.io, nginx; Hosting bei Linode/Akamai, Mail über Migadu, DNS bei GoDaddy (nur intern, nicht auf Websites).
- Funktionen: Solo-Training (8 Szenarien), Prüfungsmodus (5 Szenarien), Übungsleitung mit Mehrteilnehmer-Modus (Einladungslink), Laufkarten-Generator, Feuerwehrplan-Generator, Konto (Registrierung mit E-Mail-Bestätigung, Passwort-Reset, Trainingsverlauf), Admin-Bereich.
- Impressum-Telefon bmatraining.de live seit 20.10.2026 (Nummer nicht im Repo; Festlegung in [_shared.md](_shared.md), Asana). Frühere Abweichung zur Hub-Nummer laut Monitoring 17./18.10.2026 damit überholt.
- Veraltet: Der Verweis auf die EU-Online-Streitbeilegungsplattform (eingestellt am 20.07.2025) muss raus. Gilt für alle Northdocks-Impressen.
- SSL-Zertifikat (Let's Encrypt) gültig bis 01.12.2026.
- Umsetzung von Fixes über den Bot „Northdocks Web“.

## Betrieb und Bedienlogik (intern, Cursor-Chat ND-NB-20, Abgleich 20.10.2026)

- Server-Checkout `/opt/bma-trainer`. `deploy/update.sh` baut und startet den Docker-Stack **ohne** git pull; den Pull macht der GitHub-Workflow `deploy.yml` nach grüner CI auf `main`. Merge auf `main` = Produktions-Deploy, nur mit Joachims OK.
- Bedienreihenfolge in allen Modi: **FBF-Schlüssel, dann FSE, dann FSD**, serverseitig erzwungen (Feedback Janis Weinbach über Asana, 19.09.2026).
- Ablauf laut Testbericht 01.10.2026: FAT lesen, Summer ab, Laufkarte, Schlüssel, Erkundung, Rückstellen. FAT-Summer und Gebäudesirene sind getrennt; die FSD-Klappe öffnet bei Alarm; ÜE ab und BFS ab nur optional.
- Die 2D-Laufkarte ist die Draufsicht desselben 3D-Gebäudeplans.
- Gestrichen am 15.08.2026: Offline-Pairing über Bluetooth/Ad-hoc-WLAN. Kopplung nur per Session-Link/Token.
- Konten: Solo und Teilnehmer ohne Konto, Übungsleitung mit Login.
- Fachliches Feedback: Janis Weinbach (Asana).
- SEO-Arbeit seit Juli 2026: erlaubt, entschieden 20.10.2026 (siehe Vorgabe oben).


## Prüfungsmodus und Offline-App (Joachim, 21.10.2026, via BMA App)

- **Prüfung** wird streng wie die Solo-Übung bewertet: Die Reihenfolge zählt, Fehler senken die Prozentzahl.
- **Zielbild (nicht extern als umgesetzt darstellen):** Offline-App für PICO-Headsets von FirefighterVR-Kunden, nur die Modi Solo und Prüfung. Technik: WebView-APK mit gemeinsamem Logikmodul. Umsetzung durch die Bots BMA App und Pico Native. ~~Start wartet auf Joachims OK.~~ **Entschieden (Joachim 21.10.2026 im Chat von Pico Native, übermittelt von Pico Native), Zielbild, nicht veröffentlicht:**
  - Native Android-App: Kotlin plus WebView mit dem Offline-Bundle, ausdrücklich ohne Unity/Unreal.
  - Zunächst nur Solo-Übung und Prüfung; Zielgruppe sind bestehende FirefighterVR-Kunden.
  - Verteilung wie die anderen Trainings, Vorschlag PICO MDM.
  - BMA Trainer bleibt ein eigenes Produkt, kein FirefighterVR-Modul.
  - Prüfung streng gewertet (siehe oben).
  - Stand: Debug-APK vorhanden, noch nicht auf einem Headset getestet; ~~BMA PR #9 nicht gemerged.~~ **PR #9 nicht gemerged (Stand 06.11.2026 weiterhin Draft).**
  - Offene Frage „BMA-Offline-App starten?“ damit erledigt.

### Verifizierter Stand 06.11.2026 (Bot BMA App, agent-intern; keine Marketing-/FFVR-Claims ableiten)

- **PR #9** „Solo und Prüfung: gemeinsames Logikmodul und Offline-Bundle“ ([Northdocks-GmbH/www-bma-Trainer-App#9](https://github.com/Northdocks-GmbH/www-bma-Trainer-App/pull/9)): per privatem Cursor-Worker ND-NB-20 mit Composer 2.5 aktualisiert; HEAD `804fcdf`, `main` `c18e039` integriert. Agent-Tests: 20 Unit + 303 Playwright sowie Builds grün; GitHub-CI-Run `42219712289` beide Checks direkt für HEAD grün. PR bleibt Draft, kein Merge, kein Deploy.
- Native `window.BmaResults`-Brücke und Headsettest sind durch die Web-/JS-Mock-Tests **nicht** belegt: JS-Mock-Webkonvention ≠ native Android-/PICO-Integration.
- Offizieller möglicher PICO-Weg für später: PICO OS 6 kann installfreie PWA/Web App per HTTPS + Manifest nutzen (PICO-Doku `/document/web/web-app/` und `/document/web/manifest/`). Emulator-Debug gegen lokalen Dev-Server, Standard-Port 5173, ist erlaubt. **Keine** Aussage zu PICO 4 / OS 5 und **keine** Aussage zu `file://`-Offline-APK.
- Generische Android-Basistest-APK auf PC80: startet WebView offline. **Korrigiert nach gezielter Prüfung durch den Bot Pico Native (06.11.2026):** Die ursprüngliche BMA-Meldung „keine native BmaResults-Brücke in der PC80-APK“ war falsch und gilt nicht. Statisch in `classes3.dex` der Original-APK (`sha962e…`) belegt: `ExamResultsBridge` mit `saveResult`/`readResult`/`listResults`/`deleteResult` sowie `MainActivity` mit `BmaResults` + `addJavascriptInterface` und `blockNetworkLoads`. ~~**Weiter offen:** Laufzeit Save/List/Read/Delete, Persistenz nach Neustart, Test auf PICO-Hardware; Web-Mock ≠ Runtime.~~ Korrektur ist in PR und Asana wahrheitsgemäß ergänzt (PR-Review `5800360452`). **Laufzeit bestätigt 06.11.2026 ca. 14:03 (Bot BMA App via One/Pico Native, unveränderte PC80-Debug-APK `sha962e…`):** save/read/list/delete wurden tatsächlich aufgerufen; der Testdatensatz blieb nach force-stop und kaltem Start erhalten und sichtbar; delete entfernte ihn, Index [] — nicht mehr nur statisch. Einziger derzeit reproduzierter Web-/Offlinefehler: nach echtem `deleteResult` blieb die gelöschte Karte in `#saved-results-list` sichtbar; der bestehende PR9-Lauf prüft/begrenzt das per Re-render in Offlinequelle + DOM-Test, keine native Änderung, keine Bridge-Neuimplementation. Kein Merge, kein Livegang. **Weiter offen:** PICO-4-/Headset-Test; der Android-Test darf nicht auf PICO verallgemeinert werden. Rohskripte und vollständige Testausgaben reicht BMA App nach (agent-intern, nicht im Repo).
- Zuständigkeiten: Pico Native bleibt für Hülle/Bridge zuständig. Die bisherige Dokumentation liegt agent-intern; bitte keine Marketing-/FFVR-Claims daraus ableiten (Abschnitt „Vorgabe“ / „keine Vermarktung“ bleibt).
