# Unsere Infrastruktur: Wir mieten Rechenkapazität, stellen Modelle bereit und betreiben Inferenz

[English](../../articles/10-infrastructure.md) · Deutsch · [Français](../../fr/articles/10-infrastructure.md) · [Русский](../../ru/articles/10-infrastructure.md)

**Rate Cloud mietet Rechenkapazität von Unternehmen, stellt Modellgewichte bereit und verwaltet die Modellausführung.** Unsere Aufgabe umfasst Infrastruktur und Inferenzablauf: kompatible Hardware und Laufzeitumgebungen auswählen, Modellprofile vorbereiten, Replikate in Betrieb nehmen, Anfragen routen und Wiederherstellung durchführen.

Kunden wählen ein Modell und verbinden ihre Werkzeuge über die API. Rate Cloud betreibt die Rechenebene hinter diesem Zugang. Die Hardware wird von Unternehmenseigentümern gemietet; Eigentum an der gemieteten Ausrüstung und der Betrieb der Modellumgebung sind unterschiedliche Verantwortungsbereiche.

## Was Rate Cloud verwaltet

| Bereich | Unsere Aufgaben |
| --- | --- |
| Rechenkapazität | Kapazitäten von Unternehmen mieten und eine stabile Reserve mit zusätzlich verfügbaren Ressourcen kombinieren |
| Modellbereitstellung | Kompatible Modellgewichte platzieren und die Inferenz-Engine für die ausgewählte Version vorbereiten |
| Präzisionsprofile | Geeignete Original-, gemischte oder quantisierte Profile desselben Modells validieren |
| Bereitschaft der Replikate | Gewichte laden, Ausführung aufwärmen, Bereitschaft prüfen und nur geeignete Replikate freigeben |
| Anfrage-Routing | Kontext, Bilder, Werkzeuge, Ausgabeformat, Speicher, Warteschlange und Replikatgesundheit berücksichtigen |
| Betrieb und Wiederherstellung | Ausführung überwachen, ungesunde Replikate außer Betrieb nehmen und soweit möglich innerhalb der ursprünglichen Frist wiederherstellen |

Darum umfasst die Dienstbeschreibung neben einem API-Endpunkt auch Gewichtsplatzierung, Inferenz-Laufzeitumgebungen, Präzision und den Lebenszyklus von Replikaten. Diese betrieblichen Aufgaben sind zentral für die veröffentlichte Architektur.

## Hardwarefamilien der veröffentlichten Architektur

Die Architektur nennt Huawei-Atlas-Systeme und Ascend-Beschleuniger. Das sind veröffentlichte Plattformbeschreibungen, kein Live-Inventar aller Maschinen und keine Zusage, dass jedes Modell auf jedem aufgeführten Gerät läuft.

| Plattform | Veröffentlichte Rolle |
| --- | --- |
| Atlas 800I A2 | Inferenz großer Modelle; acht NPUs mit je 64 GB |
| Atlas 800I A3 | Inferenz großer Modelle; acht physische NPUs mit je 128 GB, dargestellt als sechzehn logische Geräte |
| Atlas 900 A2 PoD und A3 SuperPoD | Verteilte Beschleunigergruppen für große Modelle |
| Atlas 500 und 500 A2 | Kleinere Dienstaufgaben |
| Atlas 800 mit Atlas 300I Duo | Separate Kompatibilitätsklasse, unabhängig bewertet |

Die physische und logische Beschreibung des A3 bezieht sich auf denselben Speicher und darf nicht addiert werden. Kompatibilität wird für jede Kombination aus Modell, Gewichtsformat, Engine und Hardware geprüft. Eng gekoppelte Berechnungen verwenden ein kompatibles lokales Netzwerk; ganze Anfragen zwischen Standorten zu verschieben ist ein separater Vorgang.

## Von Modellgewichten zu einer nutzbaren API

Ein Modellreplikat benötigt die richtige Version und eine kompatible Laufzeit, ausreichend Speicher, erlaubte Funktionen, abgeschlossene Aufwärmung und eine erfolgreiche Bereitschaftsprüfung. Freie Hardware allein bedeutet nicht, dass ein Modell verfügbar ist.

Der Router wählt ein geeignetes validiertes Profil des vom Nutzer angeforderten Modells. Bei schwierigem Code, Mathematik, Werkzeugen, strikten Schemata und unsicheren Aufgaben hat Qualität Vorrang. Flash und Pro bleiben verschiedene Modelle. Einzelheiten finden Sie unter [Routing und Quantisierung](03-routing-and-quantization.md).

Stabile Gruppen unterstützen Grundlast und Wiederherstellung. Zusätzliche unterbrechbare Ressourcen erweitern die verfügbare Kapazität. Eine Warnung vor Ressourcenentzug stoppt neue Zuweisungen an das betroffene Replikat. Vor Beginn der Ausgabe kann die Wiederherstellung innerhalb der ursprünglichen Frist auf einem kompatiblen Replikat erneut versuchen. Ein unterbrochener Stream muss sichtbar unvollständig bleiben.

## Warum dieses Betriebsmodell Abonnementzugang unterstützt

Der gemeinsame Betrieb von Rechenkapazität, Modellprofilen und Routing ermöglicht Rate Cloud, geeignete Ressourcen zu steuern. Kunden bezahlen für Modellzugang und Parallelität während eines Abonnementzeitraums ohne kumulatives Tokenkontingent. Die Verarbeitung bleibt durch Modellgeschwindigkeit, Kontext, Fristen, Slots und Verfügbarkeit begrenzt. Ein festes Monatsvolumen oder unterbrechungsfreier 24/7-Betrieb ist nicht garantiert.

Dieser Artikel beschreibt das öffentliche Betriebsmodell und die Aufgaben von Rate Cloud. Er behauptet weder, dass jede Anfrage über einen einzigen exklusiven Ausführungspfad läuft, noch bestätigt er den aktuellen Maschinenbestand. Maßgeblich bleiben die aktuelle offizielle Architektur und die Bedingungen.

## Dienst entdecken

[Rate-Cloud-Konto erstellen und testen](https://rate-cloud.com/register). Der reguläre dreistündige Testzugang setzt E-Mail-Bestätigung und Verknüpfung von Telegram voraus und umfasst einen gleichzeitigen Slot. Die Bedingungen für gültige Einladungen sind separat: [Empfehlungsvorteile](11-referral-program.md).

Sie haben bereits ein Konto? [Verbindungsanleitungen öffnen](https://rate-cloud.com/user/instructions). Möchten Sie einen eigenen Dienst unter Ihrer Marke aufbauen? [White Label ansehen](https://rate-cloud.com/white-label).

Quellen, geprüft am 3. November 2026: [Funktionsweise von Rate Cloud](https://rate-cloud.com/how-it-works), [Nutzungsbedingungen](https://rate-cloud.com/offer) und [Modellzugang](https://rate-cloud.com/). [Zur Dokumentation](../README.md).
