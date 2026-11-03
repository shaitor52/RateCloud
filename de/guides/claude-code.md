# Claude Code mit Rate Cloud verbinden

[English](../../guides/claude-code.md) · Deutsch · [Français](../../fr/guides/claude-code.md) · [Русский](../../ru/guides/claude-code.md)
Claude Code nutzt den speziellen Kompatibilitätsendpunkt von Rate Cloud und clientspezifische Modellnamen. Dies ist API-Zugang zu GLM, DeepSeek oder Qwen über Rate Cloud; daraus werden keine Anthropic-Modelle.

Offizielle Quellen: [Rate-Cloud-Verbindungsanleitung](https://rate-cloud.com/docs) und [Claude-Code-Dokumentation](https://docs.anthropic.com/en/docs/claude-code/overview).

## API-Schlüssel erstellen

Erstellen Sie im Rate-Cloud-Dashboard einen Schlüssel, kopieren Sie das vollständige Geheimnis bei der Erstellung und aktivieren Sie **Codex / Claude Code-Kompatibilität**. Erlauben Sie dem Schlüssel das gewünschte Modell und prüfen Sie, ob Testzugang oder Abonnement aktiv ist. Die Modellliste allein bestätigt keinen Ausführungszugang.

## Modellnamen für Claude Code

Claude Code verwendet den Präfix `ocx-claude-ratecloud--` gefolgt von der exakten Modell-ID. Die direkte HTTP-API verwendet nur die ID.

| Modell | Direkte API-ID | Claude-Code-Wert für `ANTHROPIC_MODEL` |
| --- | --- | --- |
| GLM 5.3 | `glm-5.3` | `ocx-claude-ratecloud--glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` | `ocx-claude-ratecloud--glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` | `ocx-claude-ratecloud--deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` | `ocx-claude-ratecloud--deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` | `ocx-claude-ratecloud--qwen-3.8-max` |

## Start unter macOS oder Linux

Lesen Sie den Schlüssel in Bash oder zsh zuerst ohne Anzeige ein. Setzen Sie anschließend die drei Variablen und starten Sie Claude Code im selben Terminal. Sie bleiben in dieser Shell gesetzt, bis Sie sie entfernen oder das Terminal schließen.

```sh
# Bash
read -r -s -p 'Rate Cloud API key: ' RATE_CLOUD_API_KEY
printf '\n'
```

```sh
# zsh
read -r -s 'RATE_CLOUD_API_KEY?Rate Cloud API key: '
printf '\n'
```

Führen Sie im selben Terminal aus:

```sh
export ANTHROPIC_BASE_URL='https://llm.rate-cloud.com/claude'
export ANTHROPIC_AUTH_TOKEN="$RATE_CLOUD_API_KEY"
export ANTHROPIC_MODEL='ocx-claude-ratecloud--glm-5.3'
claude
```

Ersetzen Sie bei Bedarf den Modellwert durch einen anderen vollständigen Namen aus der Tabelle. Entfernen Sie anschließend alle Werte mit `unset RATE_CLOUD_API_KEY ANTHROPIC_AUTH_TOKEN ANTHROPIC_BASE_URL ANTHROPIC_MODEL` oder schließen Sie das Terminal.

## Start unter Windows PowerShell

Setzen Sie die Variablen in dem PowerShell-Fenster, aus dem Sie Claude Code starten. `Read-Host` zeigt die eingegebenen Zeichen an. Verwenden Sie für verborgene Eingabe einen von Ihnen freigegebenen lokalen Geheimnisspeicher.

```powershell
$env:RATE_CLOUD_API_KEY = Read-Host 'Rate Cloud API key'
$env:ANTHROPIC_BASE_URL = 'https://llm.rate-cloud.com/claude'
$env:ANTHROPIC_AUTH_TOKEN = $env:RATE_CLOUD_API_KEY
$env:ANTHROPIC_MODEL = 'ocx-claude-ratecloud--glm-5.3'
claude
```

Nach Claude Code entfernen Sie die Variablen aus der PowerShell-Sitzung:

```powershell
Remove-Item Env:RATE_CLOUD_API_KEY, Env:ANTHROPIC_BASE_URL, Env:ANTHROPIC_AUTH_TOKEN, Env:ANTHROPIC_MODEL
```

## Fehlerbehebung

- **Authentifizierungs- oder Kompatibilitätsfehler:** Aktivieren Sie die Schlüsseloption **Codex / Claude Code-Kompatibilität**.
- **Unbekanntes Modell:** Verwenden Sie den vollständigen Namen mit `ocx-claude-ratecloud--`, nicht die bloße HTTP-ID.
- **Kein Modellzugang:** Prüfen Sie aktiven Testzugang oder Tarif, Modellrechte, Ablaufdatum und IP-Zulassung im Dashboard.
- **Im Terminal funktioniert es, im App-Launcher nicht:** Terminalvariablen werden an daraus gestartete Programme vererbt. Starten Sie Claude Code aus der konfigurierten Shell oder verwenden Sie die aktuelle Dashboard-Anleitung für dauerhafte Einstellungen.
- **Verbindung fehlgeschlagen:** Die Basis-URL muss genau `https://llm.rate-cloud.com/claude` lauten, nicht der allgemeine `/v1`-Endpunkt.

Nennen Sie dem Support Clientversion, Betriebssystem, Modellname, Zeitpunkt und Fehlertext. Entfernen Sie vorher API-Geheimnisse, Autorisierungsheader und private Anfrageinhalte.
