# Asana-Ticket: Bid/No-Bid

Sobald eine Ausschreibung den Kompetenzfilter besteht, **sofort** ein Task anlegen. Das Ticket ist die Entscheidungsakte, kein Stub.

Projekt: `1200346071931886` (Anträge & Ausschreibungen)  
Spalte: **Sammlung** `1200346071931887`  
Name: `Ausschreibung: {Kurz-Titel}, Frist {YYYY-MM-DD}`  
Due date = Angebotsfrist. Assignee `me`, außer der User nennt jemand anderen. Patrick (`732711459534815`) als Follower, wenn er nicht Assignee ist.

Kein Task, wenn derselbe Vorgang schon im Board liegt — dann die bestehende Beschreibung auf dieses Raster **auffüllen**.

Keine Portal-Passwörter, keine AVPQ-Zugangscodes in die Notes.

## Pflichtblöcke

Jedes Feld ausfüllen. Unbekannt = `offen` (nicht weglassen). Bekanntmachung/XML/PDF lesen, bevor der Task gespeichert wird.

**Quellenrang für Eignung, Wertung, Fristen, Budget:**

1. Auftragsbekanntmachung (Portal-PDF / TED-XML / bund.de-HTML der Vergabestelle)
2. Leistungsbeschreibung, Preisblatt, Bewerbungsbedingungen
3. BKMS/TED-Rohfelder (Titel, CPV, Frist), wenn 1. noch fehlt

Nicht als Quelle: Bidfix, Tender Impulse, dtad, „KI-Kriterien-Analyse“, Such-Snippets. Die dürfen nur den **Fund** (URL) liefern. Kriterien daraus nicht ins Ticket, auch nicht als „zu prüfen“. Bis das amtliche PDF gelesen ist, bleibt das Feld `offen`.

```
ENTSCHEIDUNG
Teilnahme: offen
Empfehlung Scan: einreichen / nicht einreichen / nur mit Partner / klären
Begründung (max. 5 Sätze, Strategie + Machbarkeit + Formalia)
Was fehlt noch, um zu entscheiden:

ECKDATEN
Titel:
Vergabestelle:
Kontakt (Mail/Tel, wenn in der Bekanntmachung):
Verfahren (VgV / UVgO / VOL / VOF; offen / nicht offen):
Art (Dienst / Liefer / Bau):
CPV:
Veröffentlicht:
Angebotsfrist (Datum, Uhrzeit):
Fragenfrist / Bieterfragen bis:
Bindefrist:
TED-Nr. / bund.de / Unterlagen-URL:
Erfüllungsort:
Lose (welches Los, andere Lose ignorieren?):
Geschätzter Wert / Budgetdeckel:

GEGENSTAND
Was genau geliefert/entwickelt wird:
Hardware (Stückzahl, Typ) ja/nein:
Software: Katalog / Custom / beides:
Zielgruppe (Profi-Feuerwehr, Klinik, Schule, …):
Laufzeit und Meilensteine:
Offline / Local-Only / Hosting-DE verlangt?:
Sprache der Unterlagen und der Lieferung:

PASSUNG (Kompetenz + Strategie)
Cluster (XR / Meditrain / FFVR / Factory / GodView A / GodView B / Spearhead):
Koffer-Komplettpaket möglich? ja / teilweise / nein:
Was wir schon haben vs. neu bauen:
Produktanker (FirefighterVR, Meditrain, StrahlenschutzVR, GodView, …):
Strategie-Fit (Meditrain-Koffer und FFVR zuerst): hoch / mittel / niedrig

EIGNUNG / FORMALIA
AVPQ verlangt? (Zertifikatnummer intern bekannt, Code nicht ins Ticket)
Referenzen, die wir nennen dürfen:
Bietergemeinschaft / Unterauftrag / Eignungsleihe: erlaubt / verboten / offen
Nebenangebote: erlaubt / unzulässig / offen
Lieferort vs. Kiel:

RISIKEN
Kapazität bis zur Frist:
Preis/Budget (zu eng wie UniBw 300 k€?):
Custom-Falle (einmalig, kein Katalog):
Spezialhardware / Leasing / Eye-Tracking:
Sonstiges:

NÄCHSTER SCHRITT
Unterlagen gezogen: ja/nein
Wer entscheidet Teilnahme (Datum):
Wenn ja: Eignung vs. Zuschlag trennen, Claims nur aus claims.md
```

In Asana Task-**Beschreibung** (`html_notes`) mit denselben Überschriften (`h2`) und Listen. Links als `<a href="...">`.

**Kommentare** (`add_comment`): nur Klartext-Feld `text`, keine HTML-Tags. Sonst erscheint der Quelltext im Feed.
