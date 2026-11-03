# Rate Cloud im Vergleich zu offiziellen APIs: feste Kosten bei intensiver Nutzung

[English](../../articles/08-cost-and-service-comparison.md) · Deutsch · [Français](../../fr/articles/08-cost-and-service-comparison.md) · [Русский](../../ru/articles/08-cost-and-service-comparison.md)

**Der Vorteil von Rate Cloud ist ein fester Abonnementpreis ohne kumulatives Tokenkontingent. Mit wachsender Nutzung bleibt der Modellpreis gleich.** Eine nutzungsabhängige API berechnet jeden abrechenbaren Token. Dadurch kann anhaltende Programmier-, Analyse- und Automatisierungsarbeit mit Rate Cloud erheblich günstiger sein, sofern Arbeitslast, Geschwindigkeit, Parallelität, Funktionen und Verfügbarkeit passen.

Bei geringer Nutzung ist Rate Cloud nicht automatisch günstiger. Offizielle Anbieter bieten nützliche Cache-, Batch-, Nebenzeit- und weitere Rabatte. Dieser Vergleich macht die Abwägungen sichtbar. Geprüft am 3. November 2026; keine Preiszusage für die Zukunft.

## Offizielle API-Preise und Rate-Cloud-Abonnements

USD-Preise gelten je einer Million Tokens. Die Eingabepreise sind **ohne Cache**. Rate-Cloud-Preise sind RUB je 30 Tage für ein Modellabonnement mit vier Slots. Währungen sind ausdrücklich getrennt.

| Offizielle API und Abrechnungsbedingung | Eingabe USD/M | Ausgabe USD/M | Rate-Cloud-Modell / RUB für 30 Tage |
| --- | ---: | ---: | --- |
| Z.ai GLM-5.3 | 1,40 | 4,40 | GLM 5.3 / 2 784 |
| Z.ai GLM-5.3-Flash | 0,15 | 0,50 | GLM 5.3 Flash / 2 442 |
| DeepSeek V4.1 Flash, Nebenzeit | 0,15 | 0,60 | DeepSeek V4.1 Flash / 2 442 |
| DeepSeek V4.1 Flash, Hauptzeit | 0,30 | 1,20 | DeepSeek V4.1 Flash / 2 442 |
| DeepSeek V4 Pro, Nebenzeit | 0,66 | 1,98 | DeepSeek V4 Pro / 2 232 |
| DeepSeek V4 Pro, Hauptzeit | 1,32 | 3,96 | DeepSeek V4 Pro / 2 232 |
| QwenCloud Qwen3.8-Max, Endpunkt Singapur | 2,00 | 6,00 | Qwen 3.8 Max / 2 550 |
| OpenAI GPT-6.1 Sol, Standard mit kurzem Kontext | 2,00 | 10,00 | Alternative mit anderem Modell; GPT wird hier nicht verkauft |

Quellen: [Z.ai-Preise](https://docs.z.ai/guides/overview/pricing), [DeepSeek-Preise und Zeitfenster](https://api-docs.deepseek.com/quick_start/pricing/), [QwenCloud-Modellpreise und Singapur-Endpunkt](https://www.qwencloud.com/models/qwen3.8-max), [GPT-6.1-Sol-Preise](https://developers.openai.com/api/docs/models/gpt-6.1-sol) und [Rate-Cloud-Katalog](https://rate-cloud.com/).

Der offizielle DeepSeek-Flash-API-Name für Version V4.1-Flash-1017 lautet `deepseek-flash`; Rate Cloud verwendet `deepseek-v4.1-flash`. Die DeepSeek-Hauptzeiten sind Montag bis Freitag 01:00-04:00 und 06:00-10:00 UTC, außer an chinesischen Feiertagen; alle anderen Zeiten sind Nebenzeiten. GLM- und DeepSeek-Zeilen vergleichen die jeweils genannten Releases. Qwen teilt die Produktfamilienbezeichnung, aber Hostingfunktionen und Ausführungsprofile können abweichen. GPT ist eine Alternative für ähnliche Arbeit, kein Vergleich identischer Gewichte, Fähigkeiten oder Ausgabequalität.

## Kosten bei wiederholter Nutzung

Annahme: 80 % der abrechenbaren Tokens sind Eingabe, 20 % Ausgabe; keine Cachetreffer, Werkzeuge, Batchverarbeitung, Steuern, Sonderrabatte oder Langkontextzuschläge. Schlussfolgerungstokens müssen gegebenenfalls zur abrechenbaren Ausgabe gezählt werden. Dies sind **rechnerische Arbeitsszenarien**, keine tatsächlichen Kundendaten oder Garantie, dass Rate Cloud dieses Volumen in 30 Tagen verarbeitet.

| Offizielle API | 10 Mio. Tokens | 100 Mio. | 500 Mio. | 1 Milliarde |
| --- | ---: | ---: | ---: | ---: |
| GLM-5.3 | $20 | $200 | $1 000 | $2 000 |
| GLM-5.3-Flash | $2,20 | $22 | $110 | $220 |
| DeepSeek Flash Nebenzeit / Hauptzeit | $2,40 / $4,80 | $24 / $48 | $120 / $240 | $240 / $480 |
| DeepSeek Pro Nebenzeit / Hauptzeit | $9,24 / $18,48 | $92,40 / $184,80 | $462 / $924 | $924 / $1 848 |
| Qwen3.8-Max | $28 | $280 | $1 400 | $2 800 |
| GPT-6.1 Sol Standard | $36 | $360 | $1 800 | $3 600 |

**Die aufgeführten Rate-Cloud-Preise für 30 Tage bleiben bei diesen Volumenszenarien zwischen RUB 2 232 und 2 784.** Das beschreibt die Preisstruktur, garantiert aber nicht die Verarbeitung einer Milliarde Tokens. Mehrere Modellabonnements, zusätzliche Slots, Client-Hosting, Websuche, CI-Rechenleistung und andere Werkzeuge Ihrer Anwendung können weitere Kosten verursachen.

## Break-even statt pauschaler Ersparnisbehauptung

Bei einer rein beispielhaften Wechselkursannahme von **RUB 100 je USD** kosten 500 Mio. uncached Tokens über die offizielle GLM-5.3-API RUB 100 000 gegenüber RUB 2 784 für ein Rate-Cloud-GLM-Abonnement, also etwa das 35,9-Fache der Modellzugangskosten. Über die günstige DeepSeek-Flash-API in Nebenzeiten ergibt dieselbe Rechnung RUB 12 000 gegenüber RUB 2 442, etwa das 4,9-Fache. Dieser Wechselkurs ist eine Annahme und kein aktueller Kurs; Ergebnisse ändern sich mit Wechselkurs und Arbeitslast.

Bei dieser Annahme liegt der Break-even ohne Cache bei etwa 13,92 Mio. Tokens für GLM-5.3, 111 Mio. für GLM Flash, 101,75 Mio. für DeepSeek Flash in Nebenzeiten, 24,16 Mio. für DeepSeek Pro in Nebenzeiten und 9,11 Mio. für Qwen. Unterhalb der jeweiligen Schwelle kann die offizielle Tokenabrechnung günstiger sein. Eine hohe Cachetrefferquote verschiebt die Schwellen nach oben.

Allgemeine Formel, Volumen in Millionen:

```text
weighted USD per million = input_fraction * input_price + output_fraction * output_price
break_even_millions = subscription_RUB / (RUB_per_USD * weighted_USD_per_million)
```

Ein Sensitivitätsbeispiel mit 100 % Cachetreffern auf Eingaben bei DeepSeek Flash außerhalb der Hauptzeit setzt $0,003 für Eingabe und $0,60 für Ausgabe an: 500 Mio. Tokens bei 80/20 kosten $61,20 statt $120. Beim angenommenen Wechselkurs sind dies RUB 6 120 gegenüber RUB 2 442. Reale Cachefähigkeit ist nicht garantiert; Cache-Schreibvorgänge und weitere Gebühren können zählen. Qwen, Z.ai und OpenAI bieten ebenfalls Cache-Rabatte. OpenAI bietet günstigere Batch-/Flex-Preise und berechnet für Langkontext-/Fast-Modi mehr. Vergleichen Sie den tatsächlich genutzten Tarif.

Szenarien offline mit den [datierten Preisdaten](../../data/pricing-2026-11-03.json) und dem [Rechner](../../tools/compare_costs.py) reproduzieren:

```sh
python3 tools/compare_costs.py --rub-per-usd 100 --million-tokens 500
python3 tools/compare_costs.py --rub-per-usd 100 --million-tokens 500 --cached-input-share 1
```

Führen Sie die Befehle im Repository-Stammverzeichnis aus. Es werden keine API-Anfragen gesendet. Geben Sie einen eigenen Wechselkurs an.

## Abwägungen bei Geschwindigkeit und Dienst

Wählen Sie Rate Cloud, wenn vorhersehbare Kosten bei intensiver Nutzung wichtiger sind als minimale Latenz pro Antwort. Ein direkter Anbieter oder ein Premium-Geschwindigkeitstarif kann besser passen, wenn eigene Tests kürzere Latenz zeigen oder gehostete Funktionen, deutlich höhere Parallelität oder vertragliche Bedingungen nötig sind. Vier Rate-Cloud-Slots entsprechen nicht den Parallelitätskontingenten offizieller APIs.

Dieses Repository enthält **keinen kontrollierten Geschwindigkeitsvergleich** mit identischen Prompts und Einstellungen für alle Dienste. Daher veröffentlichen wir keine erfundenen Tokens-pro-Sekunde-Werte für Wettbewerber und behaupten keine gemessene allgemeine Rangfolge. Die vollständige veröffentlichte Rate-Cloud-Momentaufnahme steht unter [Leistung](04-performance.md). Sie schließt Wartezeit ein und unterscheidet sich von reiner Token-Generierungsgeschwindigkeit. Der Vergleich berücksichtigt Latenz- und Kapazitätsabwägungen, ohne einen direkten Head-to-Head-Befund vorzutäuschen.

Offizielle Coding-Abonnements und kostenlose Chat-Apps sind andere Produkte als nutzungsabhängiger API-Zugang. Diese Tabelle vergleicht die genannten APIs, nicht alle Tarife der Anbieter. Prüfen Sie neben dem Preis auch Aufgabenqualität und Funktionen.

[Anwendungsfälle für feste Tokenkosten](09-unlimited-use-cases.md) · [Zur Übersicht](../README.md)
