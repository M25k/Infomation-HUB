# Regeln für Anträge, Angebote und Verträge

## Sprache und Ton

- Deutsch für deutsche/EU-Vergaben, Englisch nur wenn die Unterlagen englisch sind.
- Sachlich, nachvollziehbar, keine Marketing-Superative ohne Beleg.
- Markennamen nicht übersetzen: FirefighterVR, MeditrainVR, Next Factory VR, SpearheadVR, Storywalx, Meta-dom, GodView. Schreibweise **FirefighterVR** zusammen, nie „Firefighter VR“ (Joachim, 19.10.2026); historische Dokumenttitel bleiben, wie sie sind.
- **Typografie (verbindlich):** Nach Doppelpunkt **Großschreibung** des folgenden Worts (Ausnahme Eigennamen, URLs, Code). **Keine Gedankenstriche** (`—`, `–` als Einschub); stattdessen Komma, Punkt, Klammer oder neuer Satz. Details: [.cursor/rules/german-prose.mdc](../.cursor/rules/german-prose.mdc).

## Was immer gleich bleibt

| Feld | Wert |
|---|---|
| Firma | Northdocks GmbH |
| Sitz | Niederstraße 18, 40789 Monheim am Rhein |
| Register | HRB 76844, Amtsgericht Düsseldorf |
| USt-IdNr. | DE298519758 |
| Geschäftsführer | Joachim Perschbacher, Patrick D. Reschke |
| Standardkontakt | +49 (0) 2173 9996715, kontakt@northdocks.com |

Produktnummern: FirefighterVR **9996713**, MeditrainVR/StrahlenschutzVR **9996714**. Erreichbarkeit Mo.–Fr. 9:00–13:00. Nicht 6713 als GmbH-Standard.

Kiel (Schauenburgerstraße 116, 24118 Kiel) ist **Umsetzungsstandort**, nicht der Rechtssitz. Nur nennen, wenn der Auftrag dort erbracht wird.

Vertical-Mails (`info@handaufsherz-vr.de`, `info@northdocks.de`, `godview@…`) sind **kein** Firmenstandard. Immer **kontakt@northdocks.com**.

## Was nie vermischt werden darf

1. **Produkt vs. Auftrag.** FirefighterVR bleibt eigenständiges Produkt. Ein Auftrag auf Los 2 / Flashlight / Custom gibt keinen Zugang zum gesamten Trainingskatalog, außer das ist ausdrücklich Leistungsbestandteil.
2. **Marke vs. GmbH.** MeditrainVR, SpearheadVR usw. sind Marken. Vertragspartnerin ist immer die GmbH.
3. **Forschung vs. Produkt.** TEMA, feir, Spot-KI, FlowAR sind Forschungs-/Förderprojekte. Sie belegen Kompetenz, sind aber nicht automatisch Liefergegenstand.
4. **GodView vs. Headset.** GodView = Browser-Twin mit zwei Kundentypen (Bauinspektion vs. Einsatz/Playground). Headset-Training = Unreal/OpenXR. Nie als dieselbe Anwendung beschreiben.
5. **Logo im Bild vs. Logo im Video.** Herstellerlogos auf Gegenständen, in 3D-Szenen und 3D-Assets sowie auf Fotos sind immer in Ordnung (z. B. Minimax am Feuerlöscher im Spiel, Gloria, Rosenbauer/Empl auf Fahrzeugen oder Geräten im Bild). Fremde Logos, die als Einblendung, Overlay, Bauchbinde oder Endcard in ein Video eingebaut werden, brauchen eine Freigabe. Northdocks-eigene Logos sind immer in Ordnung (Joachim, 20.10.2026, 10:01 Athen: „logos on objects, 3D assets and in photos are always fine, but logos that are integrated into the video except from ours need permission“).
6. **VR-Training vs. Erstausbildung mit realer Flamme.** VR-Feuerlöscher-Training ergänzt die Brandschutz-Erstausbildung, ersetzt sie nicht. DGUV Information 205-023 verlangt, dass jede Person in der Erstausbildung selbst eine reale Flamme löscht (z. B. gasbetriebener Löschtrainer). Positionierung: „ergänzend, kein Ersatz“, wie bei Brandschutzhelfern ([claims.md](claims.md); Cursor-Chat ND-NB-20).

## Evidenzstufen (in Texten verwenden)

| Stufe | Darf in |
|---|---|
| **öffentlich** | Website, Impressum, Presseseite — Struktur und Verbote je Domain in [websites/](websites/README.md) |
| **intern belegt** | Angebot, Eignung, Antrag (nicht ungeprüft auf die Website) |
| **widersprüchlich** | Nur mit Klärung oder der konservativen Variante |
| **offen** | Nicht verwenden |

Konservativ heißt: die schwächere, leichter nachzuweisende Aussage.

## Referenzen

Eine Referenz braucht mindestens: Auftraggeber, Gegenstand, Zeitraum. Volumen und Ansprechperson nur, wenn in `projects.md` als referenzierbar markiert und für das Verfahren nötig. Namen und Lose aus der Vergangenheit: [history.md](history.md) — Task-Zahlen sind keine Volumina.

**Großkunden** (Currenta, Merck, …): FA-**Gesamtsumme** der Kundenbeziehung ist erlaubt. Oft getrennte Workstreams und Ansprechpartner — nicht so formulieren, als sei alles ein Auftrag. Ein Los nur mit seiner eigenen Zahl.

Vor Namensnennung externer Personen: Freigabe einholen, wenn `projects.md` das verlangt (Beispiel Henkel).

## Technik in Leistungsbeschreibungen

- Engine: Unreal Engine 5.7 in den Framework-Repos (lokal oder GitHub/Cursor), OpenXR, Pico OpenXR.
- GodView: SvelteKit, Cesium, Hosting in Deutschland.
- Photogrammetrie: RealityCapture-Pipeline (`ND-Processing`), Potree/3D Tiles, Drohnenbefliegung. Dom: 100.000+ Fotos und 1.000 Laserscans.
- Keine Engine erfinden (kein Unity als Standard-Stack, außer ein konkretes Altprojekt das belegt).

## Bücher

Live in **FreeAgent**. Verkaufszahlen aus FA **sind richtig** und zählen. Mail/Deck/alte KB weichen → FA. **Nur Fördermittel** stehen nicht in FA ([grants.md](grants.md)) — nicht auf den Umsatz legen. Git nur destilliert in [accounting.md](accounting.md).

## Briefkopf

Default für von uns erzeugte HTML-Docs: [.cursor/templates/northdocks-briefkopf.html](../.cursor/templates/northdocks-briefkopf.html) (Wortmarke quer, Haarlinien, vierspaltiger Footer, Telefon **6715**). Ablauf in [.cursor/rules/google-docs-html.mdc](../.cursor/rules/google-docs-html.mdc). Gewertetes Konzept und Portal-Formulare **ohne** Briefkopf.

## Angebots-Paket

Öffentliche Vergabe: Inhaltsangebot (Brief + Preis), Konzept (nur Wertung), Referenzen und Pflicht-Erklärungen getrennt. **Ausfüllhilfe und PT-Kalkulation nie ins Portal.** Konzept ohne Firmenkopf und ohne Summe. Schnitt: [.cursor/skills/grants-and-contracts/offer-package.md](../.cursor/skills/grants-and-contracts/offer-package.md).

## Leserbezogener Text (Abgrenzung und Revision)

Einreichungs- und empfängerbezogene Texte beschreiben **Leistung und Beitrag**, nicht wiederholt, was **nicht** gemeint ist. Interne Trennungen (Produkt vs. Auftrag, Forschung vs. Produkt) gelten beim Schreiben als Prüfregeln, nicht als Negationssätze im Dokument.

- **Keine Abgrenzungs-Floskeln:** Keine Sätze, die Partner, WPs, Tools oder Produktlinien nur nennen, um sie auszuschließen („only where they interface …“, „focus is X, not the commercial Y“). Scope nur dort, wo das Template es verlangt, und dort kompakt.
- **Kein Versions-Meta:** Keine Hinweise auf frühere Entwürfe, Änderungen gegenüber Vorgängerversionen oder Redaktionsgründe, es sei denn, der Empfänger ist ausdrücklich im internen Review (vom Nutzer so benannt).

Details und Agent-Checkliste: [.cursor/rules/reader-facing-prose.mdc](../.cursor/rules/reader-facing-prose.mdc).

## Verbote

- Keine AVPQ-Zugangscodes, Passwörter, Mailbox-Zugänge, FreeAgent-Tokens.
- Keine Unteraufträge/Eignungsleihe erfinden.
- Keine Bietergemeinschaft unterstellen.
- Keine „100 %“-Sätze aus Landingpages (z. B. Meditrain-Statistiken, die im HTML als 0 gerendert wurden), solange sie nicht in `claims.md` stehen.
- **Reschke Productions GmbH:** interne Verrechnung, keine Kundenreferenz, nicht in Eignung.
- **KPI „Immersion“ (TEMA):** Nie als „validiert“ bezeichnen. Es gibt keine abgeschlossene Studie (Joachim, 16.10.2026).
- **Bürrig (Currenta):** Namentlich nennen ist erlaubt. Nie Bildmaterial, Einsatzpläne, Einsatzbereitschaftsdaten o. Ä. teilen (Joachim, 16.10.2026).
- **Support- und Update-Preise FirefighterVR:** Immer wie auf der FirefighterVR-Website angegeben, aktuell **699 € netto je Headset und Jahr** ab dem 13. Monat, gültig ab 01.10.2026 (Quelle [websites/firefightervr.md](websites/firefightervr.md), Zeile 24). Alte Preise 500 € bzw. 499 € netto sind ungültig und nur in Sonderfällen zu nennen (Joachim, 16.10.2026). Preishistorie in firefightervr.md gilt als historisch, ungültig.
