# Datenschutz, Datenverarbeitung und Verfügbarkeit

[English](../../articles/06-privacy-and-reliability.md) · Deutsch · [Français](../../fr/articles/06-privacy-and-reliability.md) · [Русский](../../ru/articles/06-privacy-and-reliability.md)

Die öffentliche Architektur von Rate Cloud unterscheidet Anfrageinhalte, temporären Verarbeitungszustand, Betriebsmetadaten sowie Konto- und Zahlungsdaten. Diese Kategorien erfüllen verschiedene Zwecke und haben unterschiedliche Aufbewahrungsregeln. Dieser Artikel fasst die veröffentlichte Richtlinie und das Design zusammen, ist aber kein unabhängiges Sicherheits-Audit.

## Anfrageinhalte und temporäre Puffer

Der Dienst erklärt, keine dauerhafte Historie von Anfrage- und Antworttexten zu erstellen und Nutzerdaten nicht zum Modelltraining zu verwenden. Inhalte werden vorübergehend im Arbeitsspeicher verarbeitet. Für verwaltete Anwendungspuffer gilt laut Dokumentation: Löschung binnen 5 Sekunden nach erfolgreicher Übermittlung beziehungsweise binnen 30 Sekunden nach endgültigem Fehler, Abbruch oder Verbindungsabbruch.

Der isolierte Rechen-KV-Cache hat eigene Fristen: höchstens 5 Minuten ohne Wiederverwendung und höchstens 15 Minuten absolutes Alter. Danach wird ein Block nicht mehr für neue Treffer verwendet; eine bereits darauf zugreifende Operation kann innerhalb ihrer Frist enden. Nach Freigabe der letzten Referenz wird der Speicher bereinigt.

Der dokumentierte Cache wird weder auf dauerhaften Datenträger geschrieben noch in Snapshots aufgenommen. Zur Kompatibilität gehören Konto, Modell, Gewichtsrevision, Quantisierung, Tokenizer, Gesprächsvorlage und Systemanweisungen. Der Index ist HMAC-geschützt; Nutzer können keinen Cachebereich eines anderen Kontos auswählen. Eine Projektregel kann einen Modus ohne anfrageübergreifenden Cache festlegen.

Der Verlauf auf dem Client ist davon getrennt. Editor, Agent, Bot oder Anwendung können eigene Gespräche und Dateien gemäß ihren Einstellungen speichern.

## Betriebsmetadaten

Die öffentliche Architektur nennt Metadaten wie Kennungen, Modell und Profil, Zeitstempel, Dauer, Nutzungswerte, Slotstatus und Fehlercodes. Detaillierte Datensätze werden nach 30 Tagen gelöscht. Sie enthalten keine Prompts, Antworten, Werkzeugargumente, Dateien oder Autorisierungstokens. Konto-, Zahlungs- und freiwillig übermittelte Supportdaten haben eigene Zwecke und Fristen.

„Keine dauerhafte Prompt-Historie“ bedeutet nicht „keine Konto- oder Betriebsdaten“. Maßgeblich sind die aktuelle Datenschutzerklärung und die geltenden Bedingungen.

## Transport und Infrastrukturgrenzen

Die Architektur beschreibt TLS für externe Verbindungen, Identitätsprüfungen und mTLS zwischen Diensten sowie bedarfsgerechte Zugriffsrechte. Schlüssel, Konten, Projekte und Cachebereiche werden getrennt. API-Geheimnisse und Anfragekörper sollen gemäß den dokumentierten Regeln nicht in Protokolle oder Sicherungen gelangen.

Geschützter Transport und hardwaregeschützte Berechnung sind unterschiedliche Garantien. Die Website verspricht keine vertrauliche Ausführung auf jedem Beschleuniger. Ein Knoten ohne vertrauenswürdige Verwaltung wird ausgeschlossen, seine Berechtigungen werden widerrufen; vor einer Rückkehr sind Prüfung und Bereinigung erforderlich.

## Verfügbarkeit und unterbrochene Arbeit

Eine durchgehende Verfügbarkeit jedes Modells rund um die Uhr ist nicht garantiert. Vor Beginn der Ausgabe kann die Wiederherstellung innerhalb der ursprünglichen Frist auf einem kompatiblen Replikat erneut versuchen. Das kann die Latenz erhöhen. Nach Beginn eines Streams muss eine Unterbrechung als unvollständiger Vorgang sichtbar bleiben.

Die veröffentlichte Ausgleichsregel gilt für einen vollständigen, ununterbrochenen Systemausfall von mehr als vier Stunden mit HTTP 503. Sie verlängert ein Drei-Tage-Abonnement um 12 Stunden, ein Sieben-Tage-Abonnement um einen Tag und ein 30-Tage-Abonnement um drei Tage. Einzelne Modellfehler, langsame Antworten, Parallelitätsgrenzen und andere Fehlercodes fallen nicht unter diese spezielle Regel. Maßgeblich bleiben die geltenden Bedingungen und zwingende Nutzerrechte.

Melden Sie bei einem Vorfall Zeitpunkt und Vorgangskennungen. Senden Sie keine API-Geheimnisse oder vertraulichen Anfrageinhalte.

Quelle: [Rate Cloud: Datenverarbeitung, Sicherheit und Verfügbarkeit](https://rate-cloud.com/how-it-works). Die aktuellen Bedingungen und Datenschutzregeln finden Sie auf der [offiziellen Website](https://rate-cloud.com/). Stand: 3. November 2026. [Zur Übersicht](../README.md).
