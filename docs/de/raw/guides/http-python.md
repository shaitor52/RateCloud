# HTTP- und Python-Zugriff

[English](../../guides/http-python.md) · Deutsch · [Français](../../fr/guides/http-python.md) · [Русский](../../ru/guides/http-python.md)
Rate Cloud bietet eine OpenAI-kompatible API für Clients mit frei konfigurierbarer Basis-URL sowie ein Python-Beispiel mit Standardbibliothek. Die Beispiele installieren keine Pakete und senden erst dann Anfragen, wenn Sie sie ausführen.

Offizielle Quelle: [Rate-Cloud-API- und Verbindungsdokumentation](https://rate-cloud.com/docs).

## Endpunkte

| Zweck | Methode und URL |
| --- | --- |
| OpenAI-kompatible Basis-URL | `https://llm.rate-cloud.com/v1` |
| Modelle auflisten | `GET https://llm.rate-cloud.com/v1/models` |
| Chat Completions | `POST https://llm.rate-cloud.com/v1/chat/completions` |
| Responses API | `POST https://llm.rate-cloud.com/v1/responses` |

Für `/v1`-Anfragen senden Sie `Authorization: Bearer <API key>`. Verwenden Sie eine exakte Modell-ID:

| Modell | Direkte API-ID |
| --- | --- |
| GLM 5.3 | `glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` |

Fügen Sie der direkten HTTP-Modell-ID kein Anbieterpräfix wie `ratecloud/` hinzu. Die Formen `ratecloud/` und `ocx-claude-ratecloud--` gelten für bestimmte Clientintegrationen.

## Umgebungsvariable setzen

Nutzen Sie unter macOS oder Linux den Abschnitt für Ihre Shell. Beide Varianten lesen das Geheimnis ohne Anzeige ein. Entfernen Sie die Variable mit `unset` oder schließen Sie das Terminal.

```sh
# Bash
read -r -s -p 'Rate Cloud API key: ' RATE_CLOUD_API_KEY
printf '\n'
export RATE_CLOUD_API_KEY
```

```sh
# zsh (macOS-Standardshell)
read -r -s 'RATE_CLOUD_API_KEY?Rate Cloud API key: '
printf '\n'
export RATE_CLOUD_API_KEY
```

Unter Windows PowerShell setzen Sie `$env:RATE_CLOUD_API_KEY` in der Sitzung, die den Client startet. Speichern Sie keinen echten Schlüssel im Quellcode, in einer eingecheckten `.env`-Datei oder einem öffentlichen Issue.

## Optionale Verbindungskontrolle mit curl

Dies sendet eine einfache Anfrage an den Modellkatalog. Sie prüft, ob der Endpunkt antwortet und der Schlüssel akzeptiert wird, beweist aber nicht, dass ein bestimmtes Modell abonniert oder für den Schlüssel freigegeben ist.

```sh
curl --fail-with-body 'https://llm.rate-cloud.com/v1/models' \
  -H "Authorization: Bearer $RATE_CLOUD_API_KEY"
```

## Python 3 mit Standardbibliothek

Speichern Sie den folgenden Code in einer lokalen `.py`-Datei. Er nutzt nur die Python-Standardbibliothek (`urllib.request`), liest das Geheimnis aus der Umgebung und sendet beim Ausführen eine kleine Chat-Completions-Anfrage. Ändern Sie `MODEL` bei Bedarf in eine andere direkte API-ID.

```python
import json
import os
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

BASE_URL = "https://llm.rate-cloud.com/v1"
MODEL = "glm-5.3"
API_KEY = os.environ.get("RATE_CLOUD_API_KEY")

if not API_KEY:
    sys.exit("Set RATE_CLOUD_API_KEY in the environment before running this script.")

payload = {
    "model": MODEL,
    "messages": [
        {"role": "user", "content": "Reply with a short greeting."}
    ],
}
request = Request(
    f"{BASE_URL}/chat/completions",
    data=json.dumps(payload).encode("utf-8"),
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    },
    method="POST",
)

try:
    with urlopen(request, timeout=60) as response:
        result = json.load(response)
    print(result["choices"][0]["message"]["content"])
except HTTPError as error:
    # Avoid printing request headers or the API key in diagnostics.
    print(f"HTTP error: {error.code} {error.reason}", file=sys.stderr)
    sys.exit(1)
except URLError as error:
    print(f"Connection error: {error.reason}", file=sys.stderr)
    sys.exit(1)
except (KeyError, IndexError, json.JSONDecodeError) as error:
    print(f"Unexpected response format: {error}", file=sys.stderr)
    sys.exit(1)
```

Führen Sie das Skript in der Shell aus, in der `RATE_CLOUD_API_KEY` gesetzt ist. Schreiben Sie die vollständige Antwort nicht in gemeinsam genutzte Protokolle, wenn Eingaben oder Ausgaben private Daten enthalten können.

## Fehlerbehebung

- **401 oder Authentifizierungsfehler:** Prüfen Sie die Umgebungsvariable im Prozess, Gültigkeit des Schlüssels und den Header `Bearer`.
- **403 oder Zugriff verweigert:** Prüfen Sie Testzugang oder Abonnement für das Modell, Schlüsselrechte, IP-Beschränkungen und erforderliche Client-Kompatibilität.
- **404 oder Modell unbekannt:** Prüfen Sie Pfad und Schreibweise. Für diese allgemeinen Beispiele ist `/v1` richtig, nicht der Codex- oder Claude-Code-Endpunkt.
- **Modell im Katalog, aber Generierung abgelehnt:** Der Katalog beweist keine Konto- oder Schlüsselberechtigung. Prüfen Sie Abonnement und Schlüsselzugriff im Dashboard.
- **Zeitüberschreitung oder unvollständige Ausgabe:** Prüfen Sie den Anfragezustand vor einem Wiederholungsversuch. Eine Zeitüberschreitung beweist nicht, dass der Vorgang abgeschlossen ist. Wiederholen Sie Anfragen mit Nebenwirkungen nicht blind.

Nennen Sie dem Support Zeitpunkt, Modell-ID, Endpunkt, HTTP-Status und Anfragekennung, falls vorhanden. Entfernen Sie API-Schlüssel, Autorisierungsheader sowie private Anfrage- und Antwortinhalte.
