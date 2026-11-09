# Rate Cloud: häufig gestellte Fragen

[English](../FAQ.md) · Deutsch · [Русский](../ru/FAQ.md) · [Français](../fr/FAQ.md) · [Übersicht](README.md)

Die Produktangaben entsprechen der offiziellen Website vom 3. November 2026. Prüfen Sie vor dem Kauf das aktuelle Dashboard und die Bedingungen.

## Was ist Rate Cloud?

Rate Cloud bietet API-Zugang zu GLM, DeepSeek und Qwen im Abonnement für Entwicklung, KI-Agenten, Automatisierung und Anwendungen. Sie wählen Modell und Laufzeit, statt pro Million Tokens abzurechnen. Siehe [Überblick](articles/01-about-rate-cloud.md).

## Gibt es ein Tokenlimit?

Während eines aktiven Abonnements gibt es kein kumulatives Kontingent für Ein- oder Ausgabetokens. Kontext einer einzelnen Operation, Frist und technische Einschränkungen bleiben begrenzt. Das verarbeitete Volumen hängt von Geschwindigkeit, Länge der Eingabe und Antwort, freien Slots und Verfügbarkeit ab.

## Bedeutet vier Slots nur vier Anfragen?

Nein. Ein kostenpflichtiges Abonnement erlaubt vier gleichzeitig laufende Anfragen. Abgeschlossene Anfragen geben ihre Slots frei. Mehrere API-Schlüssel desselben Kontos nutzen den gemeinsamen Slot-Pool des jeweiligen Modells.

## Kann ich die Parallelität erhöhen?

Laut öffentlichem Angebot lassen sich Abonnements kombinieren. Zwei Abonnements desselben Modells ergeben acht Slots für dieses Modell. Verschiedene Modellabonnements haben eigene Pools.

## Welche Modelle gibt es?

Der veröffentlichte Katalog umfasst GLM 5.3, GLM 5.3 Flash, DeepSeek V4.1 Flash, DeepSeek V4 Pro und Qwen 3.8 Max. Der [datierte Katalog](articles/02-models.md) enthält genaue API-IDs, Preise, Einsatzbereiche und Bildunterstützung.

## Ist Flash dasselbe Modell wie Pro?

Nein. Es sind unterschiedliche Katalogeinträge. Präzisionsprofile sind Ausführungsvarianten des ausgewählten Modells und erlauben keinen stillen Austausch durch ein anderes Modell. Siehe [Routing und Quantisierung](articles/03-routing-and-quantization.md).

## Wie wählt das intelligente Routing ein Präzisionsprofil?

Das veröffentlichte Design prüft Aufgabenanforderungen und geeignete Replikate, priorisiert Qualität bei schwierigen oder unsicheren Aufgaben und berücksichtigt Kosten nur unter geeigneten Routen. Kontext, Bilder, Werkzeuge, Ausgabeformat, verfügbarer Speicher, Warteschlangen und Replikatgesundheit beeinflussen die Eignung. Die Profilunterstützung hängt von Modell und Hardware ab.

## Garantiert Quantisierung identische Antworten?

Nein. Zahlenpräzision kann die Ausgabequalität beeinflussen. Die öffentliche Architektur beschreibt Prüfungen gegen die Quellversion und aufgabenspezifische Qualitätskriterien. Ein wirtschaftliches Profil ist nur dort zulässig, wo die Qualität ausreicht. Quantisierung ist unabhängig von Einstellungen zum Schlussfolgerungsaufwand.

## Welche Anwendungen kann ich verbinden?

Die offizielle Anleitung behandelt OpenCode, Codex, Claude Code, OpenClaw, Continue, Hermes und weitere kompatible Clients. Unsere [praktischen Anleitungen](guides/README.md) behandeln ausgewählte Setups. Client und Modell bestimmen die verfügbaren Funktionen. Ein verbundener Client macht das Modell nicht zu einem hauseigenen Modell des Client-Anbieters.

## Welche Basis-URL soll ich verwenden?

Die allgemeine OpenAI-kompatible Basis-URL lautet `https://llm.rate-cloud.com/v1`. Für bestimmte Clients gibt es eigene Kompatibilitätsadressen. Nutzen Sie die [offizielle Dokumentation](https://rate-cloud.com/docs) und die passende Anleitung, ohne Endpunktfamilien zu vermischen.

## Warum lehnt ein aufgelistetes Modell meine Anfrage ab?

Ein Katalogeintrag bestätigt keinen Ausführungszugang. Prüfen Sie Testzugang oder aktives Abonnement, Modellrechte des Schlüssels, Ablaufdatum, IP-Beschränkungen und Client-Kompatibilität. Prüfen Sie außerdem belegte Slots und Fehlermeldung. Teilen Sie dem Support Zeitpunkt und Anfragekennung mit, aber weder Schlüssel noch private Inhalte.

## Wie schnell ist Rate Cloud?

Die aktuelle Tabelle zeigt getrennt die vom Eigentümer am 9. November 2026 gemeldete Zeit bis zum ersten Text und die Antwortgenerierung sowie den ungefähren Kontext. Siehe [Leistung und Methodik](articles/04-performance.md). Dies sind weder Garantien noch kontrollierte Vergleiche identischer Prompts.

## Werden Prompts zum Training verwendet?

Der Dienst erklärt, Nutzerdaten nicht zum Training zu verwenden und keine dauerhafte Textgeschichte aus Prompts und Antworten anzulegen. Temporäre Verarbeitung, isolierter Rechen-Cache, Betriebsmetadaten und Kontodaten sind getrennte Kategorien. Siehe [Datenschutz und Zuverlässigkeit](articles/06-privacy-and-reliability.md) sowie die aktuelle Datenschutzerklärung auf der Website.

## Ist jedes Modell rund um die Uhr verfügbar?

Nein. Die Website garantiert nicht die dauernde Verfügbarkeit jedes Modells. Die veröffentlichte Ausgleichsregel gilt für einen bestimmten vollständigen Systemausfall, nicht für jede langsame Anfrage oder jeden einzelnen Modellfehler. Maßgeblich sind die geltenden Bedingungen.

## Kann ich vor dem Kauf testen?

Der veröffentlichte Testzugang bietet nach Registrierung sowie E-Mail- und Telegram-Bestätigung die ersten drei Stunden mit einem gleichzeitigen Slot. Prüfen Sie den Status im Dashboard.

## Welche Infrastruktur betreibt Rate Cloud?

Rate Cloud mietet Rechenkapazität von Unternehmen, stellt Modellgewichte bereit, validiert Ausführungsprofile und verwaltet Inferenzreplikate sowie Anfrage-Routing. Die veröffentlichten Beschreibungen von Huawei-Atlas- und Ascend-Hardware nennen Plattformrollen, kein Live-Inventar und keine Garantie, dass jedes Modell auf jedem Gerät läuft. Siehe [Infrastrukturüberblick](articles/10-infrastructure.md).

## Wie funktionieren Empfehlungslinks?

Ein neues Konto, das über einen gültigen persönlichen Einladungslink erstellt wird, kann fünf statt der regulären drei Teststunden und 10 % Rabatt auf den ersten Abonnementkauf erhalten. E-Mail-Bestätigung, Telegram-Verknüpfung, Testberechtigung und geltende IP-Beschränkungen bleiben erforderlich; der Rabatt ist nicht mit Aktionscodes kombinierbar. Eine gewöhnliche Registrierung lässt sich nicht nachträglich zuordnen. Werbende können aus berechtigten Zahlungen über drei Stufen 10 %, 3 % und 1 % erhalten. Boni werden nach 14 Tagen verfügbar; die Zuordnung über einen Link kann bis zu 180 Tage bestehen. Siehe [Empfehlungsprogramm](articles/11-referral-program.md) und [Registrierung](https://rate-cloud.com/register).

## Kann ich Abonnements unter eigener Marke verkaufen?

Rate Cloud bietet White-Label-Leistungen mit Branding, Website und Dashboard, Zahlungen und technischer Infrastruktur. Siehe den [White-Label-Artikel](articles/07-white-label.md) und das [aktuelle Angebot](https://rate-cloud.com/white-label).

Quellen: [Startseite](https://rate-cloud.com/), [Funktionsweise](https://rate-cloud.com/how-it-works) und [API-Anleitung](https://rate-cloud.com/docs).

## Full model

Full model umfasst die fünf aktuellen Modelle: GLM 5.3, GLM 5.3 Flash, DeepSeek V4.1 Flash, DeepSeek V4 Pro und Qwen 3.8 Max. Ein Paket kostet $45.45 für 30 Tage, $22.72 für 7 Tage oder $13.63 für 3 Tage. Ein 10%-Code senkt die Beträge auf $40.90, $20.45 und $12.27, anhand des öffentlichen Wechselkursstands vom 3. November 2026. Prüfen Sie den Bestellbetrag vor der Zahlung. Jedes Paket fügt jedem Modell einen parallelen Slot hinzu. Paketmengen stapeln sich gleichmäßig über alle Modelle und können nicht umverteilt werden: Zwei Pakete erlauben zwei gleichzeitige Anfragen je Modell. Ein zusätzlicher Kauf fügt Slots für die bezahlte Laufzeit hinzu. Die Verlängerung der gewählten Paketmenge verlängert die Laufzeit ohne Änderung der Slotzahl. Einzelabos bieten unabhängige Kapazität. Für den ersten Kauf gelten die üblichen Regeln für Gutscheine, Empfehlungen und Boni. Eine manuelle Verlängerung ist eine neue Bestellung und kann einen Gutscheincode oder Boni verwenden, wenn das Konto die üblichen Voraussetzungen erfüllt. Die automatische Verlängerung über Whop wird zum vollen vereinbarten Preis berechnet, ohne den Einführungsrabatt erneut anzuwenden.
