# Modelle und Auswahl

[English](../../articles/02-models.md) · Deutsch · [Français](../../fr/articles/02-models.md) · [Русский](../../ru/articles/02-models.md)

Der veröffentlichte Katalog von Rate Cloud enthält fünf Modelle. Für jedes gibt es ein eigenes Abonnement und eine genaue Kennung für direkte HTTP-Anfragen. Wählen Sie nach Ihrer Aufgabe und testen Sie typische Eingaben.

**Full model ist ein kommerzielles Paket aus diesen fünf nativen API-Modellen, kein sechstes Modell und keine zusätzliche API-ID.** Jedes Paket fügt jedem der unten aufgeführten Modelle einen parallelen Slot hinzu. Die Paketanzahl gilt gleichmäßig für alle fünf Modelle; Slots lassen sich nicht umverteilen. Zwei Pakete bieten daher zwei parallele Slots je Modell. Details und Preise finden Sie unter [Full model](01-about-rate-cloud.md).

## Veröffentlichter Katalog

| Modell | Direkte API-ID | Schwerpunkt | Bildeingabe | Preis für 30 Tage, veröffentlicht |
| --- | --- | --- | --- | ---: |
| GLM 5.3 | `glm-5.3` | Anspruchsvolle Entwicklung und autonome Agenten | Nein | $34,38 |
| GLM 5.3 Flash | `glm-5.3-flash` | Häufige Anfragen, tägliche Entwicklung, Automatisierung, Unteragenten | Ja | $30,16 |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` | Programmieragenten und parallele Programmieraufgaben | Ja | $30,16 |
| DeepSeek V4 Pro | `deepseek-v4-pro` | Mehrstufiges Schlussfolgern, Architektur und Code-Review | Nein | $27,56 |
| Qwen 3.8 Max | `qwen-3.8-max` | Große Repositories, Dokumente, Recherche und langer Kontext | Nein | $31,49 |

Die USD-Anzeige auf der Website wurde am 3. November 2026 geprüft. Preise und Funktionen können sich ändern; die USD-Anzeige ist vor dem Checkout nicht als Festpreis garantiert. Prüfen Sie die aktuellen Kaufbedingungen im Dashboard. Jedes aufgeführte kostenpflichtige Abonnement umfasst vier gleichzeitige Anfragen ohne kumulatives Tokenkontingent während der Laufzeit. Bildeingabe bedeutet, dass das Modell Bilder annimmt, nicht dass es Bilder erzeugt.

## Modell und Arbeitsablauf abstimmen

GLM 5.3 ist für längere Arbeit an komplexen Softwareprojekten, Repository-Analysen, Werkzeugnutzung und Unteragenten positioniert. GLM 5.3 Flash zielt auf häufige Alltagsaufgaben und Automatisierung mit vielen Aufrufen.

DeepSeek V4.1 Flash ist für Codegenerierung und -änderung, Programmieragenten und viele parallele Programmieraufgaben vorgesehen. DeepSeek V4 Pro betont Schlussfolgerungen und vertiefte Analyse, etwa Architekturentscheidungen und Reviews, bei denen Qualität wichtiger ist als minimale Verzögerung.

Qwen 3.8 Max ist für umfangreiches Material wie Repositories und Dokumente positioniert. Die Aussage zu langem Kontext ist keine numerische Spezifikation der Kontextgröße. Prüfen Sie Dokumentation und tatsächliche Anfragegrenzen, bevor Sie große Eingaben planen.

Dies sind beschriebene Einsatzbereiche, keine allgemeine Rangliste oder Garantie, dass ein Modell bei jeder Aufgabe gewinnt. Bewerten Sie Korrektheit, Befolgung von Anweisungen, Werkzeugaufrufe, Bildbedarf, Antwortzeit und manuellen Korrekturaufwand.

## Modellidentität und Ausführungsprofil

Ein Modell kann mehrere freigegebene Präzisionsprofile haben. Das Routing wählt ein geeignetes Profil des angeforderten Modells. Ein kompaktes Profil ersetzt nicht stillschweigend das Modell durch einen anderen Katalogeintrag. Flash und Pro sind unterschiedliche Modelle.

Verwenden Sie für die direkte API exakt die IDs aus der Tabelle. Client-spezifische Namen können ein Anbieterpräfix enthalten, das nicht zur direkten HTTP-ID gehört. Ein Modell in der Clientliste beweist nicht, dass Konto oder Schlüssel zur Ausführung berechtigt sind.

Quellen: [Modellkatalog und Preise](https://rate-cloud.com/), [API-Modell-IDs](https://rate-cloud.com/docs) und [Modellprofile](https://rate-cloud.com/how-it-works). [Zur Übersicht](../README.md).
