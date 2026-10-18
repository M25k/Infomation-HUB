# bmatraining.de (BMA Trainer)

Repo: `C:\Githup\www-bma-Trainer-App`  
DIN 14675 Web-MVP (FAT/FBF). Eigenes Produkt, **kein** FirefighterVR-Headset-Modul.

## Vorgabe

Derzeit **keine Vermarktung**. Keine Landingpage-Kampagnen, keine Paketpreise, kein SEO-Ausbau, nicht in northdocks.com-Vertikale aufnehmen.

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
- Abweichung Impressum: Live steht eine Telefonnummer mit Endung 9996713, Stammdaten-Soll ist +49 (0) 2173 9996715 ([open-questions.md](../open-questions.md)).
- Veraltet: Der Verweis auf die EU-Online-Streitbeilegungsplattform (eingestellt am 20.07.2025) muss raus. Gilt für alle Northdocks-Impressen.
- SSL-Zertifikat (Let's Encrypt) gültig bis 01.12.2026.
- Umsetzung von Fixes über den Bot „Northdocks Web“.
