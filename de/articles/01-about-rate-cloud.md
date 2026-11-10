# Das Angebot von Rate Cloud

[English](../../articles/01-about-rate-cloud.md) · Deutsch · [Français](../../fr/articles/01-about-rate-cloud.md) · [Русский](../../ru/articles/01-about-rate-cloud.md)

Rate Cloud basiert auf einem einfachen Kaufmodell: Sie bezahlen für den Zugang zu einem ausgewählten KI-Modell während eines festgelegten Zeitraums und nutzen dessen API ohne kumulatives Tokenkontingent. Das ist besonders nützlich, wenn eine Anwendung viele Modellaufrufe ausführt und nutzungsabhängige Tokenkosten schwer planbar sind.

Ein autonomer Programmieragent kann ein Repository lesen, Änderungen planen, Dateien bearbeiten, Werkzeuge aufrufen, Fehler prüfen und den Ablauf wiederholen. Jeder Zyklus kann weitere Anfragen und zusätzliche Ein- und Ausgabetokens verursachen. Der Abonnementpreis steigt während der Laufzeit nicht mit der verbrauchten Tokenzahl.

## Unbegrenzte Tokens, begrenzte Verarbeitungskapazität

Unbegrenzte Tokens bedeutet, dass Rate Cloud während eines bezahlten Zeitraums kein tägliches, wöchentliches oder monatliches Gesamtlimit für Ein- und Ausgabetokens festlegt. Eine einzelne Anfrage kann dennoch keinen unbegrenzten Kontext enthalten und nicht unbegrenzt laufen. Kontextkapazität, Fristen, gleichzeitige Verarbeitung, Schutzgrenzen, Hardwarekapazität und Verfügbarkeit bleiben begrenzt.

Das tatsächliche monatliche Volumen hängt vom Modell, der Länge von Eingabe und Antwort, der Geschwindigkeit und der verfügbaren Parallelität ab. Beispiele mit Hunderten Millionen oder Milliarden Tokens erläutern das Preisprinzip, sie versprechen kein monatliches Verarbeitungsvolumen.

## Vier gleichzeitige Slots je kostenpflichtigem Abonnement

Jedes kostenpflichtige Abonnement stellt vier gleichzeitige Anfragen für sein Modell bereit. Ein Slot steht für eine gerade verarbeitete Anfrage. Nach deren Abschluss wird er wieder frei. Es handelt sich nicht um ein Limit von vier Anfragen pro Tag oder Monat.

Zusätzlich gilt ein kontoweites Ratenlimit: 20 neue LLM-Anfragen in jedem gleitenden 60-Sekunden-Zeitraum. Es gilt gemeinsam für alle Modelle, API-Schlüssel, Abonnements, Full-model-Pakete und beide Service-Origins. Weitere Abonnements oder Full-model-Pakete erhöhen die unten beschriebenen gleichzeitigen Slots, aber nicht dieses Ratenlimit. Eine 429-Antwort wegen des Ratenlimits bedeutet, dass das Konto sein Anfragekontingent im gleitenden Zeitfenster erreicht hat. Eine 429-Antwort wegen des Slotlimits bedeutet, dass alle zutreffenden gleichzeitigen Slots belegt sind. Das sind getrennte Limits.

Ein Entwickler kann die Slots für einen Hauptagenten und drei Unteragenten, vier getrennte Arbeitssitzungen oder unabhängige Automatisierungen verwenden. API-Schlüssel desselben Kontos teilen sich den Slot-Pool des betreffenden Modells. Zusätzliche Schlüssel schaffen keine zusätzliche Kapazität.

Abonnements lassen sich kombinieren. Zwei Abonnements desselben Modells ergeben acht Slots für dieses Modell. Abonnements für unterschiedliche Modelle haben getrennte Pools, zum Beispiel vier GLM- und vier DeepSeek-Slots. Die Anfragen müssen an das jeweilige Modell gesendet werden.

## Laufzeiten und Einstieg

Die Website bietet Abonnements für 3, 7 und 30 Tage. Neue Nutzer können die Modelle während der ersten drei Stunden nach Registrierung und erforderlicher E-Mail- und Telegram-Bestätigung mit einem gleichzeitigen Slot testen. Testzugang und kostenpflichtige Abonnements haben unterschiedliche Kontingente.

Beginnen Sie mit einer repräsentativen Aufgabe: einem Repository, einem typischen Dokument oder einem echten Automatisierungsablauf. Prüfen Sie die Antwort, das Verhalten der Werkzeuge und die gesamte Zeit bis zu einem brauchbaren Ergebnis, bevor Sie Modell und Laufzeit auswählen.

## Geeignete Einsatzbereiche

Rate Cloud kann als Modellebene für Programmieragenten, interne Assistenten, Bots, Datenextraktion, Dokumentenabläufe und eigene Produkte dienen. Ein kompatibler Client stellt seine Oberfläche, Werkzeuge, Projektanweisungen und den Verlauf bereit. Welche modellabhängigen Funktionen verfügbar sind, hängt vom Modell und der Integration ab.

Der Dienst verkauft API-Zugang. Eine vertraute Anwendung zu verbinden macht das gewählte GLM-, DeepSeek- oder Qwen-Modell nicht zu einem eigenen Modell des Anwendungsanbieters.

Quellen: [Rate-Cloud-Startseite](https://rate-cloud.com/) und [Funktionsweise](https://rate-cloud.com/how-it-works). Stand: 3. November 2026. [Zur Übersicht](../README.md).

## Full model

Full model umfasst die fünf aktuellen Modelle: GLM 5.3, GLM 5.3 Flash, DeepSeek V4.1 Flash, DeepSeek V4 Pro und Qwen 3.8 Max.

Ein Paket kostet $45.45 für 30 Tage, $22.72 für 7 Tage oder $13.63 für 3 Tage. Ein 10%-Code senkt die Beträge auf $40.90, $20.45 und $12.27, anhand des öffentlichen Wechselkursstands vom 3. November 2026. Prüfen Sie den Bestellbetrag vor der Zahlung.

Jedes Paket fügt jedem Modell einen parallelen Slot hinzu. Paketmengen stapeln sich gleichmäßig über alle Modelle und können nicht umverteilt werden: Zwei Pakete erlauben zwei gleichzeitige Anfragen je Modell. Ein zusätzlicher Kauf fügt Slots für die bezahlte Laufzeit hinzu. Die Verlängerung der gewählten Paketmenge verlängert die Laufzeit ohne Änderung der Slotzahl. Einzelabos bieten unabhängige Kapazität. Für den ersten Kauf gelten die üblichen Regeln für Gutscheine, Empfehlungen und Boni. Eine manuelle Verlängerung ist eine neue Bestellung und kann einen Gutscheincode oder Boni verwenden, wenn das Konto die üblichen Voraussetzungen erfüllt. Die automatische Verlängerung über Whop wird zum vollen vereinbarten Preis berechnet, ohne den Einführungsrabatt erneut anzuwenden.
