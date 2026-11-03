# Tools und Anwendungen mit Rate Cloud verbinden

[English](../../articles/05-api-and-integrations.md) · Deutsch · [Français](../../fr/articles/05-api-and-integrations.md) · [Русский](../../ru/articles/05-api-and-integrations.md)

Rate Cloud bietet eine OpenAI-kompatible HTTP-API und spezielle Kompatibilitätsendpunkte für unterstützte Programmierclients. Das Dashboard enthält anwendungsspezifische Einrichtungsschritte. Verwenden Sie die Hinweise für die installierte Clientversion und das Betriebssystem.

## Veröffentlichte Endpunkte

| Zweck | Endpunkt |
| --- | --- |
| OpenAI-kompatible Basis-URL | `https://llm.rate-cloud.com/v1` |
| Modellkatalog | `GET https://llm.rate-cloud.com/v1/models` |
| Chat Completions | `POST https://llm.rate-cloud.com/v1/chat/completions` |
| Responses | `POST https://llm.rate-cloud.com/v1/responses` |
| Codex-Kompatibilitätsbasis | `https://llm.rate-cloud.com/codex/v1` |
| Claude-Code-Kompatibilitätsbasis | `https://llm.rate-cloud.com/claude` |

Direkte `/v1`-Anfragen verwenden einen Bearer-API-Schlüssel. Verwenden Sie eine exakte Modell-ID aus dem [Katalog](02-models.md), zum Beispiel `glm-5.3`. Das clientspezifische Präfix `ratecloud/` gehört nicht in eine direkte HTTP-Modellkennung.

## Von der Registrierung zur ersten Anfrage

Registrieren Sie sich oder melden Sie sich bei [Rate Cloud](https://rate-cloud.com/) an. Erfüllen Sie die erforderlichen Prüfungen für den Testzugang oder erwerben Sie den Zugang zum benötigten Modell. Erstellen Sie in den API-Schlüsseleinstellungen einen benannten Schlüssel, wählen Sie Modellzugriff, erlaubte IP-Adressen und Ablaufdatum und kopieren Sie das angezeigte Geheimnis sofort.

Ein Abonnement berechtigt zur Nutzung eines Modells; Schlüsselberechtigungen legen fest, ob ein bestimmter Schlüssel diesen Zugang verwenden darf. Ein auf ausgewählte Modelle beschränkter Schlüssel erhält nicht automatisch Zugriff auf ein neu gekauftes Modell. Der sichtbare Katalog beweist keinen aktiven Ausführungszugang.

Für Codex oder Claude Code verlangt die öffentliche Anleitung, die Kompatibilitätsoption „Codex / Claude Code“ für den Schlüssel zu aktivieren.

## Minimale HTTP-Anfrage

Setzen Sie `RATE_CLOUD_API_KEY` lokal mit Ihrer bevorzugten Methode zur Geheimnisverwaltung und führen Sie dann Folgendes aus:

```sh
curl --fail-with-body https://llm.rate-cloud.com/v1/chat/completions \
  -H "Authorization: Bearer $RATE_CLOUD_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"model":"glm-5.3","messages":[{"role":"user","content":"Reply with a short greeting."}]}'
```

Die Variable steht für Ihr lokales Geheimnis. Speichern Sie nie einen echten Schlüssel in einem öffentlichen Repository, Screenshot, Supporttext oder eingecheckter Clientkonfiguration. Prüfen Sie Kennungen im Modellkatalog und senden Sie eine kleine Anfrage für ein Modell, das Konto und Schlüssel verwenden dürfen.

## Programmierclients und andere Anwendungen

Die öffentliche Anleitung behandelt OpenCode, Codex, Claude Code, OpenClaw, Continue, Hermes und weitere kompatible Clients. Das Dashboard stellt automatische Befehle und manuelle Beispiele für unterstützte Systeme bereit.

Die Konfiguration hängt von der Clientversion ab. Die offizielle Anleitung unterscheidet beispielsweise OpenCode v1 und v2. Bevorzugen Sie die aktuellen Dashboard-Anweisungen gegenüber veralteten Konfigurationsblöcken aus Drittquellen.

Der Client liefert Oberfläche, lokale Werkzeuge, MCP-Verbindungen, Projektanweisungen und Gesprächsverwaltung. Verfügbare Modellfunktionen hängen sowohl vom ausgewählten Modell als auch von der Integration ab. Ein kompatibler Endpunkt bedeutet nicht, dass jede Funktion jeder herstellereigenen API verfügbar ist.

## Fehlerbehebung ohne Geheimnisse preiszugeben

Prüfen Sie Basis-URL und genaue Modellkennung, aktives Abonnement oder Testzugang, Modellrechte des Schlüssels, Ablaufdatum, IP-Beschränkungen und erforderliche Kompatibilitätsoptionen. Berücksichtigen Sie den gemeinsamen Slot-Pool. Teilen Sie dem Support Zeitpunkt und Anfragekennung mit, aber entfernen Sie Autorisierungsheader und private Eingaben.

Quelle: [Rate-Cloud-API- und Verbindungsdokumentation](https://rate-cloud.com/docs), abgerufen am 3. November 2026. [Zur Übersicht](../README.md).
