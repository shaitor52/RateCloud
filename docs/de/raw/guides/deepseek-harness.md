# DeepSeek Harness mit Rate Cloud verbinden

[English](../../guides/deepseek-harness.md) · Deutsch · [Français](../../fr/guides/deepseek-harness.md) · [Русский](../../ru/guides/deepseek-harness.md)
DeepSeek Harness verfügt über ein Formular „Custom model API“ für OpenAI-kompatible Gateways. Rate Cloud dokumentiert einen OpenAI-kompatiblen Chat-Completions-Endpunkt. Die folgende Einrichtung nutzt dieses Protokoll und manuelle Modell-IDs.

**Dokumentation geprüft:** 3. November 2026. DeepSeek Harness bezeichnet sich als Entwickler-Vorschau mit möglichen inkompatiblen Änderungen. Diese Anleitung folgt der veröffentlichten Web-UI- und Rate-Cloud-Dokumentation; sie ist eine statische Zuordnung und wurde nicht live getestet. Installation und API-Aufruf wurden nicht ausgeführt.

Offizielle Quellen: [Rate-Cloud-Verbindungsanleitung](https://rate-cloud.com/docs), [DeepSeek-Harness-Repository und Vorschauhinweis](https://github.com/deepseek-ai/deepseek-harness), [Harness-Modellkonfiguration](https://deepseek-harness.github.io/deepseek-harness/en/guide/providers), [Harness-Schnellstart](https://deepseek-harness.github.io/deepseek-harness/en/guide/quickstart) und [Plugin-Konfigurationskatalog](https://deepseek-harness.github.io/deepseek-harness/en/reference/config-catalog).

## Kompatibilitätsumfang

Rate Cloud dokumentiert folgende Endpunkte und direkte Modell-IDs:

| Zweck | Wert |
| --- | --- |
| Basis-URL | `https://llm.rate-cloud.com/v1` |
| Chat-Completions-Pfad | `POST /v1/chat/completions` |
| GLM 5.3 | `glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` |

Harness dokumentiert eigene Anbieter mit frei angegebener Basis-URL, Protokoll, Zugangsdaten und Modellliste. Wählen Sie **OpenAI Chat Completions**. Wählen Sie für dieses Beispiel weder Responses noch Anthropic Messages. Die veröffentlichten Dokumente belegen keinen integrierten Rate-Cloud-Anbieter und keinen live getesteten Betrieb.

## Konto und Schlüsselrechte vorbereiten

Erstellen Sie im Rate-Cloud-Dashboard einen API-Schlüssel, erlauben Sie das gewünschte Modell und prüfen Sie aktiven Testzugang oder aktives Abonnement. Der vollständige Schlüssel wird bei Erstellung einmalig angezeigt. Ein sichtbarer Katalogeintrag beweist nicht, dass der Schlüssel das Modell aufrufen darf.

## Eigene Model API in der Web-UI hinzufügen

Dies ist eine reine UI-Konfiguration. Sie installiert nichts und sendet keine Modellanfrage.

1. Starten Sie die Harness-Web-UI anhand der Schritte in der offiziellen README. Diese Anleitung wiederholt keine Installationsbefehle.
2. Öffnen Sie **Settings → Models** und wählen Sie **Add model provider**.
3. Wechseln Sie zum Formular **Custom model API**.
4. Legen Sie eine kleingeschriebene Anbieter-ID fest, zum Beispiel `ratecloud`. Laut Harness bleibt diese ID dauerhaft bestehen, weil Sitzungen, Standardwerte, Anfragen und Zugangsdatenreferenzen sie verwenden.
5. Setzen Sie den Anzeigenamen auf `Rate Cloud` und die Basis-URL auf `https://llm.rate-cloud.com/v1`.
6. Wählen Sie als API-Protokoll **OpenAI Chat Completions**.
7. Geben Sie den Rate-Cloud-Schlüssel in das Zugangsdatenfeld ein. Harness dokumentiert, dass gespeicherte Schlüssel in der UI nur geschrieben, nicht zurückgelesen werden können. Die Zugangsdaten liegen in `$DSH_HOME/.credentials.yaml`; Einstellungen speichern eine Referenz. Legen Sie den Schlüssel nicht in ein Repository oder öffentliches Issue.
8. Fügen Sie manuell ein Modell mit einer exakten ID aus der Tabelle hinzu und geben Sie ihm einen lesbaren Anzeigenamen. Lassen Sie Kontextfenster, maximale Ausgabe, Bildeingabe und Schlussfolgerungsoptionen leer, sofern kein geprüfter Wert oder keine geprüfte Fähigkeit vorliegt.
9. Speichern Sie den Anbieter und wählen Sie das konfigurierte Modell im Modellmenü als Standard für neue Sitzungen.

Sie können dem Anbieter weitere Modelle mit ihren exakten IDs ohne Präfix hinzufügen. Fügen Sie im Feld für die eigene API kein Clientpräfix wie `ratecloud/` hinzu.

## Optionale Modellerkennung

Harness kann anhand von Anbieter-URL, Protokoll und Zugangsdaten eine Modellliste abrufen. Dadurch wird eine authentifizierte HTTP-Anfrage an den Endpunkt gesendet. Diese Erkennung ist optional und funktioniert nicht garantiert mit jedem Listenformat. Für eine Einrichtung ohne Anfrage fügen Sie die Modell-IDs wie oben manuell ein. Bei Erstellung dieser Anleitung wurde keine Erkennungsanfrage gesendet.

## Fehlerbehebung

- **`MISSING_CREDENTIAL`:** Prüfen Sie, ob ein Schlüssel für den Anbieter gespeichert oder die konfigurierte Zugangsdatenreferenz verfügbar ist.
- **`UNKNOWN_MODEL`:** Fügen Sie die Modell-ID dem eigenen Anbieter hinzu und wählen Sie diesen Eintrag. Exakte Kleinschreibung und Satzzeichen beachten.
- **HTTP 401:** Schlüssel, Ablaufdatum und Modellberechtigung bei Rate Cloud prüfen. Die Modellliste in der UI ist keine Zugangsprüfung.
- **HTTP 404 oder falsche Route:** Basis-URL `https://llm.rate-cloud.com/v1` und OpenAI Chat Completions wählen. `/chat/completions` nicht an die Basis-URL anhängen.
- **Modellerkennung liefert nichts:** Das Listenformat wird eventuell nicht erkannt. Modell manuell eintragen; ein fehlgeschlagener Erkennungsaufruf beweist nicht, dass Generierung unmöglich ist.
- **Werkzeuge, Bilder oder Schlussfolgerungen schlagen fehl:** Eine deklarierte Funktion erzeugt oder testet keine API-Unterstützung. Aktivieren Sie nur Funktionen, die für das Modell dokumentiert und praktisch bestätigt sind.
- **Konfigurationspfade unterscheiden sich:** Harness ist eine Entwicklervorschau und kann sich schnell ändern. Verwenden Sie die aktuelle Modellkonfigurationsseite und den erzeugten Plugin-Konfigurationskatalog für Ihre Version.

Es wurde keine Live-Anfrage durchgeführt; Authentifizierung und Funktionsverhalten in Harness sind daher nicht bestätigt.

Version auf Russisch: [DeepSeek Harness mit Rate Cloud verbinden](../../ru/guides/deepseek-harness.md). Zurück zu [allen deutschen Anleitungen](README.md).
