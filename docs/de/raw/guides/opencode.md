# OpenCode mit Rate Cloud verbinden

[English](../../guides/opencode.md) · Deutsch · [Français](../../fr/guides/opencode.md) · [Русский](../../ru/guides/opencode.md)
Diese Anleitung konfiguriert OpenCode für die OpenAI-kompatible API von Rate Cloud. Sie behandelt das dokumentierte Format von OpenCode v1. Die aktuelle Verbindungsseite von Rate Cloud unterscheidet v1 und v2. Für v2 verwenden Sie das aktuelle v2-Beispiel im Dashboard und fügen kein v1-Format ein.

Offizielle Quellen: [Rate-Cloud-Verbindungsanleitung](https://rate-cloud.com/docs) und [OpenCode-Konfiguration](https://opencode.ai/docs/config/).

## Vor dem Start

1. Melden Sie sich bei Rate Cloud an und erstellen Sie unter **Einstellungen → API-Schlüssel** einen Schlüssel. Kopieren Sie ihn sofort, da das vollständige Geheimnis nur bei der Erstellung angezeigt wird.
2. Prüfen Sie, ob der Schlüssel das gewünschte Modell erlaubt und ein Testzugang oder Abonnement aktiv ist. Die Modellliste allein gewährt keinen Ausführungszugang.
3. OpenCode v1 verwendet bei Auswahl des konfigurierten Anbieters das Präfix `ratecloud/`. Dieses Präfix ist clientseitig. Die direkte HTTP-API verwendet die Modell-ID ohne Präfix.

| Modell | Direkte API-ID | Auswahl in OpenCode v1 |
| --- | --- | --- |
| GLM 5.3 | `glm-5.3` | `ratecloud/glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` | `ratecloud/glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` | `ratecloud/deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` | `ratecloud/deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` | `ratecloud/qwen-3.8-max` |

## Schlüssel in der Shell setzen

Die Beispiele lesen den Schlüssel ohne Anzeige. Wählen Sie Bash oder zsh, die Standardshell von macOS. Geben Sie das Geheimnis an der Eingabeaufforderung ein. Programme aus dieser Shell erben die Variable. Schließen Sie das Terminal oder entfernen Sie sie mit `unset`.

```sh
# Bash
read -r -s -p 'Rate Cloud API key: ' RATE_CLOUD_API_KEY
printf '\n'
export RATE_CLOUD_API_KEY
```

```sh
# zsh
read -r -s 'RATE_CLOUD_API_KEY?Rate Cloud API key: '
printf '\n'
export RATE_CLOUD_API_KEY
```

Fügen Sie den Schlüssel nicht in gemeinsam genutzte Konfigurationsdateien, Quellcode, Screenshots oder Supportnachrichten ein. Setzen Sie ihn unter Windows in der Umgebung, aus der OpenCode gestartet wird, und verwenden Sie Ihre übliche sichere lokale Methode zur Geheimnisverwaltung.

## OpenCode v1 konfigurieren

Öffnen Sie unter macOS/Linux `~/.config/opencode/opencode.json`. Bewahren Sie vorhandene Anbieter und Einstellungen. Fügen Sie den Eintrag `provider` in das vorhandene Objekt ein und setzen oder ergänzen Sie `model` auf oberster Ebene. Für eine neue Datei ist dies ein vollständiges Minimalbeispiel für GLM 5.3:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "ratecloud/glm-5.3",
  "provider": {
    "ratecloud": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Rate Cloud",
      "options": {
        "baseURL": "https://llm.rate-cloud.com/v1",
        "apiKey": "{env:RATE_CLOUD_API_KEY}"
      },
      "models": {
        "glm-5.3": { "name": "GLM 5.3" },
        "glm-5.3-flash": { "name": "GLM 5.3 Flash" },
        "deepseek-v4.1-flash": { "name": "DeepSeek V4.1 Flash" },
        "deepseek-v4-pro": { "name": "DeepSeek V4 Pro" },
        "qwen-3.8-max": { "name": "Qwen 3.8 Max" }
      }
    }
  }
}
```

OpenCode ersetzt `{env:RATE_CLOUD_API_KEY}` beim Laden durch die Umgebungsvariable. Ist sie nicht gesetzt, wird ein leerer Wert eingesetzt. Exportieren Sie den Schlüssel also vor dem Start. Die Konfiguration enthält nur den Variablenverweis, nicht das Geheimnis.

Unter Windows lautet der dokumentierte Benutzerpfad `%USERPROFILE%\.config\opencode\opencode.json`. OpenCode v1 und v2 haben unterschiedliche Anbieterstrukturen. Für v2 verwenden Sie das separate manuelle Beispiel aus dem Rate-Cloud-Dashboard.

## Modell wählen und Verbindung prüfen

Starten Sie OpenCode nach der Änderung neu, öffnen Sie die Modellauswahl (`/models` im TUI) und wählen Sie ein Rate-Cloud-Modell. Beginnen Sie mit einer kurzen Anfrage ohne vertrauliche Inhalte. Verwenden Sie die genaue v1-Auswahl aus der Tabelle.

## Fehlerbehebung

- **Rate Cloud fehlt in der Liste:** Prüfen Sie Speicherort, gültiges JSON sowie die Position von `provider.ratecloud` und `model` auf oberster Ebene.
- **Nicht autorisiert oder abgelehnt:** Exportieren Sie `RATE_CLOUD_API_KEY` in derselben Shell, aus der OpenCode gestartet wird. Prüfen Sie Ablaufdatum, IP-Beschränkungen, Modellrechte und aktiven Testzugang oder Tarif.
- **Schlüssel scheint leer:** Eine nicht gesetzte Variable wird zu einem leeren Wert. Setzen Sie sie vor dem Start und starten Sie den Client neu.
- **Modell abgelehnt:** Nutzen Sie die exakte kleingeschriebene ID samt Satzzeichen. Katalogsichtbarkeit allein beweist keinen Zugang.
- **OpenCode v2:** Verwenden Sie das `providers`-Format aus dem Dashboard, nicht dieses v1-Format mit `provider`.

Teilen Sie dem Support Clientversion, Betriebssystem, Modell-ID, Zeitpunkt und Fehlermeldung mit. Entfernen Sie API-Schlüssel, Autorisierungsheader und private Anfrageinhalte.
