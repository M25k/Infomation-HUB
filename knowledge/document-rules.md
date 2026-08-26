# Regeln für Anträge, Angebote und Verträge

## Sprache und Ton

- Deutsch für deutsche/EU-Vergaben, Englisch nur wenn die Unterlagen englisch sind.
- Sachlich, nachvollziehbar, keine Marketing-Superative ohne Beleg.
- Markennamen nicht übersetzen: FirefighterVR, MeditrainVR, Next Factory VR, SpearheadVR, Storywalx, Meta-dom, GodView.

## Was immer gleich bleibt

| Feld | Wert |
|---|---|
| Firma | Northdocks GmbH |
| Sitz | Niederstraße 18, 40789 Monheim am Rhein |
| Register | HRB 76844, Amtsgericht Düsseldorf |
| USt-IdNr. | DE298519758 |
| Geschäftsführer | Joachim Perschbacher, Patrick D. Reschke |
| Standardkontakt | +49 (0) 2173 9996713, kontakt@northdocks.com |

Kiel (Schauenburgerstraße 116, 24118 Kiel) ist **Umsetzungsstandort**, nicht der Rechtssitz. Nur nennen, wenn der Auftrag dort erbracht wird.

Vertical-Mails (`info@handaufsherz-vr.de`, `info@northdocks.de`, `godview@…`) sind **kein** Firmenstandard. Immer **kontakt@northdocks.com**.

## Was nie vermischt werden darf

1. **Produkt vs. Auftrag.** FirefighterVR bleibt eigenständiges Produkt. Ein Auftrag auf Los 2 / Flashlight / Custom gibt keinen Zugang zum gesamten Trainingskatalog, außer das ist ausdrücklich Leistungsbestandteil.
2. **Marke vs. GmbH.** MeditrainVR, SpearheadVR usw. sind Marken. Vertragspartnerin ist immer die GmbH.
3. **Forschung vs. Produkt.** TEMA, feir, Spot-KI, FlowAR sind Forschungs-/Förderprojekte. Sie belegen Kompetenz, sind aber nicht automatisch Liefergegenstand.
4. **GodView vs. Headset.** GodView = Browser-Twin mit zwei Kundentypen (Bauinspektion vs. Einsatz/Playground). Headset-Training = Unreal/OpenXR. Nie als dieselbe Anwendung beschreiben.

## Evidenzstufen (in Texten verwenden)

| Stufe | Darf in |
|---|---|
| **öffentlich** | Website, Impressum, Presseseite — Struktur und Verbote je Domain in [websites/](websites/README.md) |
| **intern belegt** | Angebot, Eignung, Antrag (nicht ungeprüft auf die Website) |
| **widersprüchlich** | Nur mit Klärung oder der konservativen Variante |
| **offen** | Nicht verwenden |

Konservativ heißt: die schwächere, leichter nachzuweisende Aussage.

## Referenzen

Eine Referenz braucht mindestens: Auftraggeber, Gegenstand, Zeitraum. Volumen und Ansprechperson nur, wenn in `projects.md` als referenzierbar markiert und für das Verfahren nötig.

Vor Namensnennung externer Personen: Freigabe einholen, wenn `projects.md` das verlangt (Beispiel Henkel).

## Technik in Leistungsbeschreibungen

- Engine: Unreal Engine 5.7 in den lokalen Framework-Repos, OpenXR, Pico OpenXR.
- GodView: SvelteKit, Cesium, Hosting in Deutschland.
- Photogrammetrie: RealityCapture-Pipeline (`ND-Processing`), Potree/3D Tiles, Drohnenbefliegung. Dom: 100.000+ Fotos und 1.000 Laserscans.
- Keine Engine erfinden (kein Unity als Standard-Stack, außer ein konkretes Altprojekt das belegt).

## Verbote

- Keine AVPQ-Zugangscodes, Passwörter, Mailbox-Zugänge.
- Keine Unteraufträge/Eignungsleihe erfinden.
- Keine Bietergemeinschaft unterstellen.
- Keine „100 %“-Sätze aus Landingpages (z. B. Meditrain-Statistiken, die im HTML als 0 gerendert wurden), solange sie nicht in `claims.md` stehen.
