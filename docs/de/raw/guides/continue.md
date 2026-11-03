# Continue mit Rate Cloud verbinden

[English](../../guides/continue.md) · Deutsch · [Français](../../fr/guides/continue.md) · [Русский](../../ru/guides/continue.md)
Continue unterstützt OpenAI-kompatible Modelle über seinen OpenAI-Anbieter und eine eigene `apiBase`. Diese Anleitung verwendet das aktuelle `config.yaml`-Format und speichert den Schlüssel in Continues lokaler Geheimnisdatei, nicht in YAML.

**Dokumentation geprüft:** 3. November 2026. Dies ist eine statische Konfiguration anhand der Dokumentation, keine Live-Anfrage aus Continue oder einem Rate-Cloud-Konto. Continue empfiehlt aktuell YAML; `config.json` ist veraltet. Die geprüften Seiten nennen keine Mindestversion. Wenn Ihre Version ein Feld nicht akzeptiert, folgen Sie dem verlinkten aktuellen Schema.

Offizielle Quellen: [Rate-Cloud-Verbindungsanleitung](https://rate-cloud.com/docs), [OpenAI-kompatible Modelle in Continue](https://docs.continue.dev/customize/model-providers/top-level/openai), [Continue-YAML-Referenz](https://docs.continue.dev/reference), [Continue-FAQ zu Geheimnissen](https://docs.continue.dev/faqs) und [Continue-Konfigurationspfade](https://docs.continue.dev/guides/understanding-configs).

## Zugriff und Modell-IDs prüfen

Erstellen Sie einen Rate-Cloud-API-Schlüssel, erlauben Sie das benötigte Modell und prüfen Sie aktiven Testzugang oder aktives Abonnement. Der vollständige Schlüssel wird nur bei Erstellung angezeigt. Die Modellliste von Continue gewährt keinen Zugriff.

Die OpenAI-kompatible Basis-URL von Rate Cloud lautet `https://llm.rate-cloud.com/v1`. Nutzen Sie die exakten direkten API-IDs unten. Continue zeigt im Auswahlmenü den von Ihnen gesetzten `name`; das Präfix `ratecloud/`, das andere Clients verwenden, ist nicht nötig.

| Modell | Direkte API-ID |
| --- | --- |
| GLM 5.3 | `glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` |

## Geheimnis für die IDE-Erweiterung speichern

Continues IDE-Erweiterungen lösen `${{ secrets.NAME }}` aus `.env`-Dateien auf. Laut Dokumentation gilt diese Suchreihenfolge: Workspace `.env`, Workspace `.continue/.env`, dann global `~/.continue/.env`. IDE-Erweiterungen übernehmen Shell-Umgebungsvariablen nicht direkt.

Erstellen oder aktualisieren Sie die globale Datei `~/.continue/.env` (Windows: `%USERPROFILE%\.continue\.env`) mit folgendem lokalem Eintrag:

```dotenv
RATE_CLOUD_API_KEY=<your-key>
```

Halten Sie die Datei aus der Versionsverwaltung heraus. Speichern Sie keinen echten Schlüssel in `config.yaml` und teilen Sie die `.env`-Datei nicht. Für Continue CLI kann laut Dokumentation auch die Prozessumgebung das Geheimnis auflösen.

## Lokale YAML für Continue konfigurieren

Continues lokale Konfiguration liegt unter macOS/Linux in `~/.continue/config.yaml`, unter Windows in `%USERPROFILE%\.continue\config.yaml`. Öffnen Sie sie mit dem Konfigurationswähler und dem Zahnradsymbol in der Continue-Seitenleiste. Bewahren Sie andere Abschnitte auf. Fügen Sie je gewünschtem Modell einen Eintrag hinzu; dieses Beispiel enthält alle fünf:

```yaml
name: Rate Cloud
version: 1.0.0
schema: v1
models:
  - name: Rate Cloud - GLM 5.3
    provider: openai
    model: glm-5.3
    apiBase: https://llm.rate-cloud.com/v1
    apiKey: ${{ secrets.RATE_CLOUD_API_KEY }}
    useResponsesApi: false
    roles: [chat, edit, apply]
  - name: Rate Cloud - GLM 5.3 Flash
    provider: openai
    model: glm-5.3-flash
    apiBase: https://llm.rate-cloud.com/v1
    apiKey: ${{ secrets.RATE_CLOUD_API_KEY }}
    useResponsesApi: false
    roles: [chat, edit, apply]
  - name: Rate Cloud - DeepSeek V4.1 Flash
    provider: openai
    model: deepseek-v4.1-flash
    apiBase: https://llm.rate-cloud.com/v1
    apiKey: ${{ secrets.RATE_CLOUD_API_KEY }}
    useResponsesApi: false
    roles: [chat, edit, apply]
  - name: Rate Cloud - DeepSeek V4 Pro
    provider: openai
    model: deepseek-v4-pro
    apiBase: https://llm.rate-cloud.com/v1
    apiKey: ${{ secrets.RATE_CLOUD_API_KEY }}
    useResponsesApi: false
    roles: [chat, edit, apply]
  - name: Rate Cloud - Qwen 3.8 Max
    provider: openai
    model: qwen-3.8-max
    apiBase: https://llm.rate-cloud.com/v1
    apiKey: ${{ secrets.RATE_CLOUD_API_KEY }}
    useResponsesApi: false
    roles: [chat, edit, apply]
```

`useResponsesApi: false` wählt den dokumentierten Chat-Completions-Pfad. Die Modelle sind mit Chat-, Editier- und Apply-Rollen aufgeführt. Diese Anleitung aktiviert keine Agenten-/Werkzeugnutzung, da sie von der tatsächlichen Werkzeugaufruf-Unterstützung des Modells und der API abhängt. Aktivieren Sie diese Funktion erst nach Prüfung.

Speichern Sie die Konfiguration. Laut aktueller Continue-Anleitung werden Änderungen automatisch neu geladen. Wählen Sie im Modellmenü einen Rate-Cloud-Eintrag. Eine Modellanfrage ist nicht nötig, um statische Konfiguration und Auswahl zu prüfen.

## Fehlerbehebung

- **API-Schlüssel wird nicht aufgelöst:** Prüfen Sie Schreibweise `RATE_CLOUD_API_KEY` und Speicherort der `.env`-Datei. Bei IDE-Erweiterungen nicht allein auf `export` im Terminal vertrauen.
- **Kein Rate-Cloud-Modell sichtbar:** Prüfen Sie YAML-Pfad, `schema: v1` und gültige YAML-Syntax. Stellen Sie mit Continues Konfigurationsauswahl sicher, dass Sie die aktive Datei bearbeiten.
- **401 oder Zugriff verweigert:** Prüfen Sie aktiven Schlüssel und die Modellberechtigung für Schlüssel und Konto. Ein Modellname in Continue beweist keinen Zugriff.
- **404 oder falscher API-Pfad:** `apiBase` bleibt `https://llm.rate-cloud.com/v1`; `/chat/completions` nicht anhängen.
- **Agenten-Werkzeugaufrufe schlagen fehl:** `roles` und Unterstützung von Werkzeugaufrufen sind getrennt. Continue verlangt `tool_use` für den Agent-Modus; die tatsächliche Rate-Cloud-Kompatibilität wurde hier nicht live getestet. Nicht ohne Prüfung deklarieren.
- **Konfiguration in Ihrer Version anders:** Die Continue-Referenz ist maßgeblich für unterstützte YAML-Felder. YAML bevorzugen; JSON-Konfigurationen sind veraltet.

Entfernen Sie Geheimnisse und private Eingaben aus Protokollen, bevor Sie Diagnosen teilen. Bei Erstellung wurden keine Installationen oder API-Anfragen ausgeführt.

Version auf Russisch: [Continue mit Rate Cloud verbinden](../../ru/guides/continue.md). Zurück zu [allen deutschen Anleitungen](README.md).
