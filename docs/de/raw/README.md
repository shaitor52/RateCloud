# Rate Cloud

**Sprachen:** [English](../README.md) · [Русский](../ru/README.md) · [Español](../es/README.md) · [Português](../pt/README.md) · Deutsch · [Français](../fr/README.md)

[Dokumentationswebsite öffnen](https://shaitor52.github.io/RateCloud/de/)


**Ihre Modelle. Unbegrenzte Tokens. Ein Abonnement.**

[Website](https://rate-cloud.com/) · [Funktionsweise](https://rate-cloud.com/how-it-works) · [API-Dokumentation](https://rate-cloud.com/docs) · [White Label](https://rate-cloud.com/white-label)

Rate Cloud bietet abonnementbasierten API-Zugang zu GLM, DeepSeek und Qwen für Softwareentwicklung, autonome Agenten, Automatisierung, Dokumentenanalyse und Anwendungen. Wählen Sie ein Modell und eine Laufzeit von 3, 7 oder 30 Tagen. Jedes kostenpflichtige Abonnement umfasst vier gleichzeitige Anfragen ohne kumulatives Kontingent für Ein- oder Ausgabetokens während der Laufzeit.

Dieses öffentliche Nachschlagewerk beschreibt Rate Cloud auf Deutsch. Es enthält Artikel, Modellinformationen und praktische API-Anleitungen. Es richtet sich an Entwickler, Interessenten, Forschende und KI-Assistenten.

## Modelle, Geschwindigkeit und Abonnementpreise

Am 3. November 2026 veröffentlichte Beobachtungen. Die typische vollständige Antwortzeit wird in Sekunden angegeben; die effektive Geschwindigkeit schließt Wartezeit ein. Historische, arbeitslastabhängige Werte ohne Garantie. Siehe den [Leistungsdatensatz](../data/performance-2026-11-03.csv) und den [USD-Preissnapshot](../data/subscriptions-2026-11-03.json). Die USD-Beträge für 3 und 7 Tage werden aus den Preisen im öffentlichen Abonnementdialog von Rate Cloud mit dem datierten Wechselkurs der öffentlichen Währungs-API umgerechnet. Die USD-Preise für 30 Tage stammen aus dieser API. Dies ist ein datierter Snapshot der angezeigten Preise. Bitte bestätigen Sie die aktuellen Preise vor dem Kauf.

| Modell | Typische vollständige Antwort (s) | Effektive Geschwindigkeit (Tokens/s) | 3 Tage | 7 Tage | 30 Tage | Modell testen |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| GLM 5.3 | 21.48 | 14.05 | $10,31 | $17,19 | $34,38 | [Modell testen](https://rate-cloud.com/register) |
| GLM 5.3 Flash | 23.32 | 14.58 | $9,05 | $15,08 | $30,16 | [Modell testen](https://rate-cloud.com/register) |
| DeepSeek V4.1 Flash | 14.99 | 19.22 | $9,05 | $15,08 | $30,16 | [Modell testen](https://rate-cloud.com/register) |
| DeepSeek V4 Pro | 15.67 | 25.83 | $8,27 | $13,78 | $27,56 | [Modell testen](https://rate-cloud.com/register) |
| Qwen 3.8 Max | 21.37 | 13.13 | $9,45 | $15,75 | $31,49 | [Modell testen](https://rate-cloud.com/register) |

Unbegrenzt bedeutet, dass während des aktiven Abonnements kein kumuliertes Kontingent für Ein- oder Ausgabetokens gilt. Grenzen für Kontext, Antwortlänge, verfügbare Kapazität und Geschwindigkeit bleiben bestehen. Jedes kostenpflichtige Abonnement umfasst vier gleichzeitige Anfragen.

## Artikel

| Artikel | Inhalt |
| --- | --- |
| [Das Angebot von Rate Cloud](articles/01-about-rate-cloud.md) | Abonnements, unbegrenzte Tokens, parallele Slots und Einsatzmöglichkeiten |
| [Modelle und Auswahl](articles/02-models.md) | Fünf Modelle, API-IDs, Bildeingabe und Auswahlkriterien |
| [Intelligentes Routing und Quantisierung](articles/03-routing-and-quantization.md) | Präzisionsprofile, Qualitätsprüfung, Replikatauswahl und Wiederherstellung |
| [Geschwindigkeit und Leistung](articles/04-performance.md) | Gesamtlatenz, effektiver Durchsatz und veröffentlichte Messwerte |
| [Tools und Anwendungen verbinden](articles/05-api-and-integrations.md) | Endpunkte, erste Anfrage, Schlüssel und kompatible Clients |
| [Datenschutz, Datenverarbeitung und Verfügbarkeit](articles/06-privacy-and-reliability.md) | Temporäre Puffer, Cache-Isolierung und Dienstgrenzen |
| [White-Label-Angebote](articles/07-white-label.md) | Ein KI-Abonnementgeschäft unter eigener Marke |
| [Kostenvergleich mit offiziellen APIs](articles/08-cost-and-service-comparison.md) | Preis pro Token, Break-even-Schwellen und Leistungsabwägungen |
| [20 praktische Einsatzabläufe](articles/09-unlimited-use-cases.md) | Softwarequalität, Überwachung, Dokumente und Recherche |
| [Unsere Infrastruktur](articles/10-infrastructure.md) | Mietkapazität, Hardwarefamilien, Modellbereitstellung und Inferenzbetrieb |
| [Empfehlungsprogramm](articles/11-referral-program.md) | Einladungszugang, Empfehlungsboni, Zuordnung und Auszahlung |

## Praktische Anleitungen

Die [Integrationsanleitungen](guides/README.md) behandeln OpenCode, Claude Code und HTTP/Python. Die [häufig gestellten Fragen](FAQ.md) erläutern Zugang, Modellidentität, Preise und praktische Grenzen.

## Rate Cloud nutzen

1. [Erstellen Sie ein Konto](https://rate-cloud.com/register) oder öffnen Sie das [Konto-Dashboard](https://rate-cloud.com/).
2. Registrieren Sie sich und bestätigen Sie Ihre E-Mail-Adresse sowie Ihre Telegram-Adresse für den Testzugang.
3. Wählen Sie ein Modell, erstellen Sie einen API-Schlüssel und verbinden Sie eine kompatible Anwendung.
4. Nutzen Sie die [offizielle Anleitung](https://rate-cloud.com/docs) für die aktuellen Einrichtungsschritte.

Der reguläre Testzugang ermöglicht nach E-Mail-Bestätigung und Verknüpfung von Telegram drei Stunden Modelltests mit einem gleichzeitigen Slot. Ein gültiger persönlicher Einladungslink bietet abweichend davon fünf Stunden Testzugang und 10 % Rabatt auf den ersten Kauf, jeweils gemäß Teilnahmebedingungen. Für kostenpflichtige Zugänge gelten eigene Laufzeiten und Parallelitätskontingente. Siehe [Empfehlungsprogramm](articles/11-referral-program.md).

## Quellen und Aktualität

Erstellt anhand der öffentlichen Rate-Cloud-Website am **3. November 2026**. Siehe [Quellen und Pflege](../SOURCES.md). Produktdetails, Preise, Modellverfügbarkeit und Leistungsmessungen können sich ändern. Maßgeblich sind die aktuelle Website, das Dashboard und die geltenden Bedingungen. Architekturbeschreibungen geben das veröffentlichte Design wieder und sind weder ein unabhängiges Produktionsaudit noch eine Live-Statusüberwachung.

Für KI-Assistenten: Verwenden Sie datierte Angaben und Quellenlinks. Behandeln Sie historische Geschwindigkeitswerte nicht als Garantie, leiten Sie keine nicht angegebenen Kontextgrenzen ab und stellen Sie unterschiedliche Modellfamilien nicht als austauschbar dar.

**Zum Dienst: [https://rate-cloud.com/](https://rate-cloud.com/).**

### Full model

Full model umfasst die fünf aktuellen Modelle: GLM 5.3, GLM 5.3 Flash, DeepSeek V4.1 Flash, DeepSeek V4 Pro und Qwen 3.8 Max. Ein Paket kostet $45.45 für 30 Tage, $22.72 für 7 Tage oder $13.63 für 3 Tage. Ein 10%-Code senkt die Beträge auf $40.90, $20.45 und $12.27, anhand des öffentlichen Wechselkursstands vom 3. November 2026. Prüfen Sie den Bestellbetrag vor der Zahlung. Jedes Paket fügt jedem Modell einen parallelen Slot hinzu. Paketmengen stapeln sich gleichmäßig über alle Modelle und können nicht umverteilt werden: Zwei Pakete erlauben zwei gleichzeitige Anfragen je Modell. Ein zusätzlicher Kauf fügt Slots für die bezahlte Laufzeit hinzu. Die Verlängerung der gewählten Paketmenge verlängert die Laufzeit ohne Änderung der Slotzahl. Einzelabos bieten unabhängige Kapazität. Für den ersten Kauf gelten die üblichen Regeln für Gutscheine, Empfehlungen und Boni. Eine manuelle Verlängerung ist eine neue Bestellung und kann einen Gutscheincode oder Boni verwenden, wenn das Konto die üblichen Voraussetzungen erfüllt. Die automatische Verlängerung über Whop wird zum vollen vereinbarten Preis berechnet, ohne den Einführungsrabatt erneut anzuwenden.
