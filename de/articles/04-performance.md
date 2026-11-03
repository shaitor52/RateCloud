# Geschwindigkeit und Leistung verstehen

[English](../../articles/04-performance.md) · Deutsch · [Français](../../fr/articles/04-performance.md) · [Русский](../../ru/articles/04-performance.md)

Die relevante Leistungsfrage lautet: Wie lange dauert es, bis Ihre Aufgabe ein brauchbares Ergebnis liefert? Eine hohe Tokenrate während der Generierung beschreibt das Gesamterlebnis nicht. Wartezeit, Eingabeverarbeitung, Antwortlänge und Wiederherstellung zählen ebenfalls.

## Veröffentlichte Leistungsmomentaufnahme

Die folgenden Werte wurden am 3. November 2026 auf der Rate-Cloud-Startseite angezeigt. Das Datum bezeichnet den Abruf, nicht einen unabhängig ermittelten Messzeitraum.

| Modell | Typische vollständige Antwort, Sekunden | Typische effektive Tokens/Sekunde, einschließlich Wartezeit | Effektive Tokens/Sekunde bei schnellen Antworten, einschließlich Wartezeit |
| --- | ---: | ---: | ---: |
| GLM 5.3 | 21,48 | 14,05 | 58,47 |
| GLM 5.3 Flash | 23,32 | 14,58 | 61,92 |
| DeepSeek V4 Pro | 15,67 | 25,83 | 127,84 |
| DeepSeek V4.1 Flash | 14,99 | 19,22 | 78,38 |
| Qwen 3.8 Max | 21,37 | 13,13 | 80,68 |

Dies sind veröffentlichte Dienstbeobachtungen, keine garantierten Antwortzeiten, festen Hardware-Benchmarks oder kontrollierten Vergleiche mit identischen Prompts. Die Startseite nennt neben dieser Tabelle weder Stichprobengröße noch vollständigen Messzeitraum. Die Werte belegen daher keine dauerhafte Verfügbarkeit und kein SLA.

## Bedeutung der Spalten

Die vollständige Antwortzeit reicht vom Absenden der Anfrage bis zum fertigen Ergebnis. Sie enthält Wartezeit, Verarbeitung der Eingabe und Erstellung der Antwort.

Laut Website bezeichnet „typisch“ den Median: Die Hälfte der Ergebnisse ist schneller, die andere langsamer. Die effektiven Tokenraten schließen die gesamte Anfrage samt Wartezeit ein. Sie dürfen nicht als reine Decodiergeschwindigkeit oder Zeit bis zum ersten Token bezeichnet werden.

Die Spalte für schnelle Antworten zeigt die schnellsten zehn von hundert Anfragen. Sie veranschaulicht das schnellere Ende der beobachteten Verteilung und verspricht diese Rate nicht für neue Anfragen. Multiplizieren Sie unabhängig zusammengefasste Latenz- und Durchsatzwerte nicht, um eine mittlere Antwortlänge abzuleiten.

## Warum Ihre Aufgabe länger dauern kann

Ein langes Dokument benötigt mehr Eingabeverarbeitung als eine kurze Frage. Eine ausführliche Antwort braucht länger als eine knappe. Werkzeugbasierte Agenten können mehrere Aufrufe benötigen. Aktuelle Auslastung, Profilverfügbarkeit, Bereitschaft des Replikats und Wiederherstellung beeinflussen ebenfalls die Dauer.

Ein für häufige oder schnelle Arbeit beworbenes Modell kann in den beobachteten Daten eine höhere mediane Antwortzeit als ein anderes Modell haben, wenn sich die Anfragegruppen unterscheiden. Die Tabelle isoliert weder Modellgeschwindigkeit von Aufgabenkomplexität und Antwortlänge noch das Nutzerverhalten.

## Parallelität und Gesamtdurchsatz

Vier kostenpflichtige Slots ermöglichen unabhängige Vorgänge gleichzeitig. Sie machen eine einzelne Anfrage nicht viermal schneller. Parallelität hilft, wenn sich Arbeit teilen lässt; eine sequenzielle Schlussfolgerungs- oder Werkzeugkette wartet weiterhin auf ihre Abhängigkeiten.

Messen Sie für einen praktischen Vergleich Ihre eigene Zeit bis zu einem brauchbaren Ergebnis, Korrektheit, unvollständige Anfragen, Fehler und Wiederholungsbedarf. Notieren Sie Modell, Eingabe- und Ausgabegröße, Parallelität und Beobachtungszeitraum.

Quelle: [veröffentlichte Leistungstabelle von Rate Cloud](https://rate-cloud.com/). Siehe auch [API-Dokumentation](https://rate-cloud.com/docs). [Zur Übersicht](../README.md).

## Alle verfügbaren öffentlichen Ergebnisse und Datendownload

Die obige Tabelle enthält alle 15 Zahlenwerte der Leistungstabelle für fünf Modelle, die bei Abruf auf der Startseite veröffentlicht waren. Eine [CSV-Momentaufnahme](../../data/performance-2026-11-03.csv) bewahrt Modell-IDs, Einheiten, Abrufdatum und Quell-URL zur Wiederverwendung. Für diese Datei wurde kein neuer Benchmark durchgeführt.

| Nachweis | In dieser Momentaufnahme vorhanden? |
| --- | --- |
| Typische vollständige Antwortdauer für alle fünf Modelle | Ja, Tabelle und CSV |
| Typische effektive Tokenrate einschließlich Wartezeit für alle fünf Modelle | Ja, Tabelle und CSV |
| Effektive Tokenrate des schnellsten Zehntels für alle fünf Modelle | Ja, Tabelle und CSV |
| Rohzeiten je Anfrage, Stichprobengröße und Beobachtungszeitraum | In Verbindung mit der öffentlichen Tabelle nicht angegeben |
| Zeit bis zum ersten Token, reine Decodiergeschwindigkeit, Latenzperzentile | In der öffentlichen Tabelle nicht angegeben |
| Kontrollierter Vergleich derselben Arbeitslast mit offiziellen Anbietern | In diesem Repository nicht verfügbar |

Die Startseite verlinkt die Methodik auf `/docs#statistics`; zum Abrufzeitpunkt enthielt die aktuelle Verbindungsdokumentation keinen passenden ausführlichen Statistikabschnitt. Diese Beleglücke bleibt offen, statt zusätzliche Ergebnisse zu erfinden. Zum Preisvergleich siehe [Vergleich offizieller APIs](08-cost-and-service-comparison.md).
