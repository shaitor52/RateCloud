# Geschwindigkeit und Leistung verstehen

[English](../../articles/04-performance.md) · Deutsch · [Français](../../fr/articles/04-performance.md) · [Русский](../../ru/articles/04-performance.md)

Die relevante Leistungsfrage lautet: Wie lange dauert es, bis Ihre Aufgabe ein brauchbares Ergebnis liefert? Eine hohe Tokenrate während der Generierung beschreibt das Gesamterlebnis nicht. Wartezeit, Eingabeverarbeitung, Antwortlänge und Wiederherstellung zählen ebenfalls.

## Aktuelle Leistungsdaten

Die Werte wurden vom Eigentümer am 9. November 2026 gemeldet. Zeit bis zum ersten Text und Antwortgenerierung sind getrennte Kennzahlen. Der Eingabekontext beträgt ungefähr 200.000 Tokens; Ergebnisse hängen von der Arbeitslast ab.

| Modell | Zeit bis zum ersten Text (s) | Antwortgenerierung (Tokens/s) |
| --- | ---: | ---: |
| GLM 5.3 | 15,6 | 52,7 |
| GLM 5.3 Flash | 18,9 | 50,7 |
| DeepSeek V4.1 Flash | 11,2 | 150,8 |
| DeepSeek V4 Pro | 10,0 | 142,6 |
| Qwen 3.8 Max | 13,0-13,5 | 59,0-63,4 |

[Aktuelle Leistungsdaten als CSV](../../data/performance-2026-11-09.csv). Die Qwen-Bereiche umfassen zwei Durchläufe.

Der [CSV-Snapshot vom 3. November](../../data/performance-2026-11-03.csv) bleibt als historische Datei erhalten.

## Warum Ihre Aufgabe länger dauern kann

Ein langes Dokument benötigt mehr Eingabeverarbeitung als eine kurze Frage. Eine ausführliche Antwort braucht länger als eine knappe. Werkzeugbasierte Agenten können mehrere Aufrufe benötigen. Aktuelle Auslastung, Profilverfügbarkeit, Bereitschaft des Replikats und Wiederherstellung beeinflussen ebenfalls die Dauer.

## Parallelität und Gesamtdurchsatz

Vier kostenpflichtige Slots ermöglichen unabhängige Vorgänge gleichzeitig. Sie machen eine einzelne Anfrage nicht viermal schneller. Parallelität hilft, wenn sich Arbeit teilen lässt; eine sequenzielle Schlussfolgerungs- oder Werkzeugkette wartet weiterhin auf ihre Abhängigkeiten.

Messen Sie für einen praktischen Vergleich Ihre eigene Zeit bis zu einem brauchbaren Ergebnis, Korrektheit, unvollständige Anfragen, Fehler und Wiederholungsbedarf. Notieren Sie Modell, Eingabe- und Ausgabegröße, Parallelität und Beobachtungszeitraum.

Quelle: [veröffentlichte Leistungstabelle von Rate Cloud](https://rate-cloud.com/). Siehe auch [API-Dokumentation](https://rate-cloud.com/docs). [Zur Übersicht](../README.md).
