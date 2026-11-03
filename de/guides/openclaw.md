# OpenClaw mit Rate Cloud verbinden

[English](../../guides/openclaw.md) · Deutsch · [Français](../../fr/guides/openclaw.md) · [Русский](../../ru/guides/openclaw.md)
OpenClaw kann einen eigenen Anbieter mit OpenAI-kompatibler Basis-URL registrieren. Diese Anleitung verwendet den dokumentierten Transport `openai-completions` und die OpenAI-kompatible Chat-Completions-API von Rate Cloud.

**Dokumentation geprüft:** 3. November 2026. Dies ist ein statisches Konfigurationsbeispiel nach den veröffentlichten Dokumentationen. Es wurde nicht live mit einer OpenClaw-Installation oder einem Rate-Cloud-Konto getestet. Die OpenClaw-Dokumentation wird fortlaufend aktualisiert und nennt hier keine Mindestversion. Verwenden Sie für Ihre installierte Version das aktuelle Konfigurationsformat.

Offizielle Quellen: [Rate-Cloud-Verbindungsanleitung](https://rate-cloud.com/docs), [Rate-Cloud-Beispiel für OpenClaw](https://rate-cloud.com/docs), [eigene OpenClaw-Anbieter](https://docs.openclaw.ai/concepts/model-providers/custom-providers), [OpenClaw-Anbieterbeispiele](https://docs.openclaw.ai/gateway/config-tools/provider-examples), [OpenClaw-Umgebungsvariablen](https://docs.openclaw.ai/help/environment) und [OpenClaw-Geheimnisreferenzen](https://docs.openclaw.ai/reference/secretref-credential-surface).

## Voraussetzungen und Zugang

Erstellen Sie im Dashboard einen Rate-Cloud-API-Schlüssel. Erlauben Sie das gewünschte Modell, prüfen Sie den Testzugang oder das aktive Abonnement und kopieren Sie das vollständige Geheimnis bei der Erstellung. Ein Modell im Katalog gewährt noch keinen Ausführungszugang.

Rate Cloud dokumentiert diesen Endpunkt für OpenAI-kompatible Anfragen:

```text
https://llm.rate-cloud.com/v1
```

Wählen Sie den Adapter `openai-completions`. Fügen Sie `/chat/completions` nicht an die Basis-URL an. Direkte Modell-IDs von Rate Cloud:

| Modell | Direkte API-ID | OpenClaw-Modellreferenz |
| --- | --- | --- |
| GLM 5.3 | `glm-5.3` | `ratecloud/glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` | `ratecloud/glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` | `ratecloud/deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` | `ratecloud/deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` | `ratecloud/qwen-3.8-max` |

Die OpenClaw-Referenz enthält die Anbieter-ID; an den Upstream wird die Modell-ID ohne Präfix gesendet.

## Schlüssel verwenden, ohne ihn in der Konfiguration abzulegen

OpenClaw unterstützt `${VARIABLE_NAME}` in Anbieterwerten für `apiKey`. Die aktuelle OpenClaw-Dokumentation empfiehlt die globale Datei `~/.openclaw/.env` für Anbieterschlüssel. Sie wird auch gelesen, wenn ein Gateway als Dienst läuft. Fügen Sie dort lokal diese Zeile hinzu (Windows: `%USERPROFILE%\.openclaw\.env`):

```dotenv
RATE_CLOUD_API_KEY=<your-key>
```

Bewahren Sie die Datei lokal auf und beschränken Sie den Zugriff. Der dotenv-Lader von OpenClaw expandiert Referenzen innerhalb von `.env`-Werten nicht; rechts vom Gleichheitszeichen steht daher der tatsächliche Schlüssel. Tragen Sie den Schlüssel weder in eine gemeinsam genutzte `openclaw.json` noch in ein Repository oder öffentliches Issue ein. Starten Sie das Gateway neu, falls der laufende Prozess den neuen Wert noch nicht geladen hat.

## Eigenen Anbieter ergänzen

Öffnen Sie unter macOS/Linux `~/.openclaw/openclaw.json`, unter Windows `%USERPROFILE%\.openclaw\openclaw.json`. Sichern Sie die Datei und führen Sie die Felder `models` und `agents` mit der bestehenden Konfiguration zusammen. Ersetzen Sie keine unabhängigen Einstellungen. OpenClaw verwendet JSON5; dieses Beispiel ohne Kommentare ist auch gültiges JSON.

```json
{
  "models": {
    "mode": "merge",
    "providers": {
      "ratecloud": {
        "baseUrl": "https://llm.rate-cloud.com/v1",
        "apiKey": "${RATE_CLOUD_API_KEY}",
        "api": "openai-completions",
        "models": [
          { "id": "glm-5.3", "name": "GLM 5.3" },
          { "id": "glm-5.3-flash", "name": "GLM 5.3 Flash" },
          { "id": "deepseek-v4.1-flash", "name": "DeepSeek V4.1 Flash" },
          { "id": "deepseek-v4-pro", "name": "DeepSeek V4 Pro" },
          { "id": "qwen-3.8-max", "name": "Qwen 3.8 Max" }
        ]
      }
    }
  },
  "agents": {
    "defaults": {
      "model": {
        "primary": "ratecloud/glm-5.3"
      }
    }
  }
}
```

Das Beispiel nutzt die Felder der aktuellen OpenClaw-Dokumentation für eigene Anbieter und des Rate-Cloud-Beispiels: `baseUrl`, `apiKey`, `api`, `models` und `agents.defaults.model.primary`. Es legt weder Kontextgröße, Bildunterstützung, Werkzeugkompatibilität noch Schlussfolgerungsverhalten fest. Lassen Sie diese Angaben aus, sofern sie für Endpunkt und Modell nicht verifiziert sind.

## Auswahl und Fehlerbehebung

Starten Sie das Gateway nach dem Speichern neu und wählen Sie das konfigurierte Rate-Cloud-Modell. Für eine statische Prüfung muss die primäre Modellreferenz genau einer Anbieter-/Modell-ID in der Datei entsprechen. Ein Modelllisten- oder Generierungsbefehl würde eine authentifizierte API-Anfrage senden und soll nur bewusst ausgeführt werden.

- **Anbieter/Modell unbekannt:** Prüfen Sie `models.providers.ratecloud.models[]` auf die genaue ID ohne Präfix und die Auswahl `ratecloud/<dieselbe-ID>`.
- **Nicht autorisiert:** Stellen Sie sicher, dass der Gateway-Prozess `RATE_CLOUD_API_KEY` lesen kann, der Schlüssel aktiv ist und die IP-Regeln den Gateway-Host zulassen.
- **Zugriff verweigert:** Prüfen Sie Schlüsselrechte und Testzugang/Abonnement für das konkrete Modell.
- **Werkzeugaufrufe oder Bilder schlagen fehl:** Das generische Protokoll garantiert nicht jede Funktion. Ergänzen Sie `reasoning`, `input`, `contextWindow` oder Kompatibilitätsüberschreibungen nur, wenn der tatsächliche Endpunkt und das Modell dies unterstützen.
- **Ältere OpenClaw-Konfiguration:** Dokumentation kann sich ändern. Prüfen Sie den aktuellen Verweis für eigene Anbieter, statt ein altes `models.json`-Schema in `openclaw.json` zu kopieren.

Entfernen Sie Zugangsdaten und private Eingaben, bevor Sie Diagnosen weitergeben. Diese Anleitung beschreibt nur die Konfiguration; es wurde kein API-Aufruf ausgeführt.

Version auf Russisch: [OpenClaw mit Rate Cloud verbinden](../../ru/guides/openclaw.md). Zurück zu [allen deutschen Anleitungen](README.md).
