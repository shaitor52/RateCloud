# Hermes Agent mit Rate Cloud verbinden

[English](../../guides/hermes-agent.md) · Deutsch · [Français](../../fr/guides/hermes-agent.md) · [Русский](../../ru/guides/hermes-agent.md)
Hermes Agent unterstützt eigene OpenAI-kompatible Endpunkte. Diese Anleitung nutzt die dokumentierte Konfiguration eines eigenen Anbieters mit der Chat-Completions-API `/v1` von Rate Cloud.

**Dokumentation geprüft:** 3. November 2026. Die Beispiele folgen den aktuellen veröffentlichten Hermes- und Rate-Cloud-Dokumentationen und wurden nicht live mit einer Installation oder einem Konto getestet. Hermes-Dokumentation wird fortlaufend aktualisiert; die geprüften Seiten nannten keine Mindestversion. Die Anbieterkonfiguration hat sich geändert. Verwenden Sie die aktuellen Feldnamen, nicht ältere Beispiele.

Offizielle Quellen: [Rate-Cloud-Verbindungsanleitung](https://rate-cloud.com/docs), [Hermes-Anbieteranleitung](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/integrations/providers.md), [Hermes-Umgebungsvariablen](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/reference/environment-variables.md) und [Hermes-Konfigurationsdateien](https://hermes-agent.nousresearch.com/docs).

## Zugang vorbereiten

Erstellen Sie im Rate-Cloud-Dashboard einen API-Schlüssel, erlauben Sie das gewünschte Modell und prüfen Sie, dass Testzugang oder Abonnement aktiv sind. Der vollständige Schlüssel wird nur bei Erstellung angezeigt. Halten Sie ihn aus Quellcode und Supportnachrichten heraus.

Der allgemeine kompatible Endpunkt von Rate Cloud lautet:

```text
https://llm.rate-cloud.com/v1
```

Verwenden Sie die direkte API-Modell-ID. Hermes benötigt nicht das Präfix `ratecloud/`, das einige andere Clients nutzen.

| Modell | Direkte API-ID |
| --- | --- |
| GLM 5.3 | `glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` |

## Geheimnis in der lokalen Hermes-Umgebungsdatei ablegen

Die aktuelle Hermes-Dokumentation nennt `~/.hermes/.env` für benutzerverwaltete Geheimnisse. Fügen Sie lokal diese Zeile hinzu und ersetzen Sie den Platzhalter:

```dotenv
RATE_CLOUD_API_KEY=<your-key>
```

Unter Windows: `%USERPROFILE%\.hermes\.env`. Checken Sie diese Datei nicht ein und geben Sie keinen echten Schlüssel in Beispielen weiter. Hermes kann auch eine Prozess-Umgebungsvariable lesen; die Einstellung `key_env` unten verweist auf sie.

## Eigenen Endpunkt konfigurieren

Bearbeiten Sie unter macOS/Linux `~/.hermes/config.yaml` oder unter Windows `%USERPROFILE%\.hermes\config.yaml`. Führen Sie diese Felder mit dem bestehenden Abschnitt `model` zusammen, statt andere Einstellungen zu ersetzen:

```yaml
model:
  default: glm-5.3
  provider: custom
  base_url: https://llm.rate-cloud.com/v1
  key_env: RATE_CLOUD_API_KEY
```

Dies verwendet die dokumentierten Hermes-Felder für einen eigenen Endpunkt: `provider: custom`, `base_url` und `key_env`. Der Endpunkt spricht Chat Completions. Stellen Sie ihn nicht auf Anthropic Messages oder Responses um. Ergänzen Sie keine Kontextgrenze ohne verifizierten Dienst- und Modellwert.

Für ein anderes Rate-Cloud-Modell ändern Sie `model.default` in eine exakte andere ID aus der Tabelle. Behalten Sie `provider: custom` und die Rate-Cloud-Basis-URL.

## Optionale interaktive Einrichtung

Hermes dokumentiert `hermes model` als Assistenten für eigene Endpunkte. Er fragt Basis-URL, API-Schlüssel und Modellnamen ab und speichert die Auswahl. Geben Sie `https://llm.rate-cloud.com/v1` und eine bloße Modell-ID aus der Tabelle ein. Wenn der wörtliche Schlüssel nicht in `config.yaml` gespeichert werden soll, bevorzugen Sie die obige Konfiguration mit Umgebungsdatei.

## Fehlerbehebung

- **Zugangsdaten fehlen:** Prüfen Sie `RATE_CLOUD_API_KEY` in `~/.hermes/.env` oder der Prozessumgebung sowie die identische Schreibweise in `key_env`.
- **Verbindungsfehler:** Basis-URL mit `/v1` verwenden, nicht `/v1/chat/completions`; der Client ergänzt den API-Pfad.
- **Modell unbekannt oder Zugriff verweigert:** Exakte direkte ID verwenden und Modellrechte des Schlüssels sowie aktiven Testzugang oder Tarif prüfen.
- **Werkzeugaufrufe erscheinen als Text:** OpenAI-kompatibler Transport garantiert nicht, dass jedes Modell und jeder Endpunkt Werkzeugaufrufe in der erwarteten Form unterstützt. Prüfen Sie die reale Modellfähigkeit.
- **Kontextlimit wirkt falsch:** Hermes kann Metadaten aus `/v1/models` ableiten, aber die Liste enthält nicht garantiert alle Angaben. Übernehmen Sie keine ungeprüfte Kontextgröße in die Konfiguration.
- **Älteres Beispiel gefunden:** Alte Dokumentation zeigt möglicherweise `api_key` oder eine andere Struktur. Verwenden Sie die aktuelle Hermes-Anbieteranleitung und prüfen Sie die Felder für Ihre Version.

Bei der Erstellung dieser Anleitung wurden weder API-Aufrufe noch Installationen ausgeführt.

Version auf Russisch: [Hermes Agent mit Rate Cloud verbinden](../../ru/guides/hermes-agent.md). Zurück zu [allen deutschen Anleitungen](README.md).
