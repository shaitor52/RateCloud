# Intelligentes Routing und Quantisierung

[English](../../articles/03-routing-and-quantization.md) · Deutsch · [Français](../../fr/articles/03-routing-and-quantization.md) · [Русский](../../ru/articles/03-routing-and-quantization.md)

Die öffentliche Architektur von Rate Cloud beschreibt eine Kombination aus stabiler Rechenkapazität, zusätzlich verfügbarer Unternehmenskapazität, freigegebenen Präzisionsprofilen und anfrageabhängigem Routing. Ziel ist eine effiziente Ressourcennutzung, wobei Identität und funktionale Anforderungen des ausgewählten Modells erhalten bleiben.

Dieser Artikel erläutert die veröffentlichte Architektur. Er ist weder eine unabhängige Prüfung jeder Produktionsbereitstellung noch ein Versprechen, dass jede Hardware- und Präzisionskombination jederzeit verfügbar ist.

## Rechenkapazität und Modellreplikate

Der Dienst beschreibt die Anmietung freier Kapazität von Unternehmensknoten neben einer stabilen Reserve. Rate Cloud verwaltet die Platzierung von Modellgewichten, Inferenz-Engines, Präzisionsprofile und Anfrageverteilung.

Die Architektur nennt Huawei-Atlas-Systeme und Ascend-Beschleuniger, darunter Atlas 800I A2 und A3 für große Modelle sowie Atlas 900 A2 PoD und A3 SuperPoD für verteilte Gruppen. Die Hardwarekompatibilität wird je Modell geprüft. Eine Anfrage zwischen Standorten zu verschieben ist etwas anderes, als eng gekoppelte Modellberechnungen beliebig über Standorte aufzuteilen: eng gekoppelte Berechnungen eines Replikats nutzen ein kompatibles lokales Netzwerk.

Ein nutzbares Replikat benötigt mehr als freien Speicher. Es braucht kompatible Gewichte, Laufzeitunterstützung, erforderliche API-Funktionen, geladene Modelle, Aufwärmung und eine erfolgreiche Bereitschaftsprüfung.

## Was Quantisierung verändert

Modellparameter und Zwischenberechnungen können unterschiedliche Zahlenformate verwenden. Kompaktere Formate benötigen weniger Speicher und können die Ausführung beschleunigen, aber auch die Ausgabequalität beeinflussen. Niedrigere Präzision muss daher für die jeweilige Quellversion und Aufgabenarten geprüft werden.

Das veröffentlichte Design verwendet Qualitäts-, ausgewogene und wirtschaftliche Profile desselben Modells. Ein Qualitätsprofil kann das validierte Originalformat, W8A8 oder eine andere freigegebene Konfiguration nutzen. Ein ausgewogenes Profil kann Komponenten mit unterschiedlicher Präzision kombinieren, etwa 4 und 8 Bit. Ein effektiver Mittelwert nahe 6 Bit bedeutet keine universelle INT6-Implementierung. Wirtschaftliche Profile können validierte W4A16-, W4A8- oder MXFP4-Konfigurationen nutzen, sofern Modell und Hardware sie unterstützen.

Verfügbarkeit eines Formats hängt von Modellversion, Hardware, Laufzeit und Qualitätsprüfung ab. Es gilt nicht pauschal für alle Modelle. Eine höhere nominelle Präzision bereits quantisierter Gewichte stellt zuvor verlorene Information nicht wieder her.

## Qualitätsprüfungen vor dem Routing

Profile werden anhand der exakten Quellmodellversion mit öffentlichen, synthetischen und speziell erstellten Aufgaben zu Code, Mathematik, langem Kontext, Werkzeugen und strengem JSON geprüft. Der veröffentlichte Prozess berücksichtigt Ausgabequalität, Speicherbedarf, Geschwindigkeit und API-Verhalten. Nutzergespräche werden nicht für Training oder Kalibrierung verwendet.

Ein kompaktes Profil ist nur für Aufgaben geeignet, die es ausreichend bewältigt. Anspruchsvoller Code, Mathematik, Werkzeugabläufe, strikte Schemata und unsichere Aufgaben erhalten Qualitätspriorität. Auch eine kurze Eingabe kann schwierig sein. `reasoning_effort` ist eine separate Einstellung und kein Effekt der Quantisierung.

## Wie der Router auswählt

Der Router berücksichtigt Kontextanforderungen, Bildeingaben, Werkzeuge, Ausgabeformat, Aufgabenkomplexität, verfügbaren Speicher, Warteschlange, Replikatgesundheit und verbleibende Ressourcenzeit. Zuerst werden geeignete Routen bestimmt; Kosten werden nur unter geeigneten Optionen berücksichtigt.

Das ausgewählte Modell bleibt fest. Auch Gewichtsrevision und erlaubte Funktionen werden für den Vorgang festgelegt. Ein inkompatibler Server wird vor der Zuweisung ausgeschlossen. Ist keine geeignete Kapazität verfügbar, kann das System innerhalb seines internen Budgets warten oder einen expliziten Fehler wegen vorübergehender Nichtverfügbarkeit zurückgeben, statt stillschweigend ein anderes Modell einzusetzen.

## Ablauf einer Anfrage

1. Geschützte Verbindung herstellen und API-Schlüssel, Abonnement und freien Slot prüfen.
2. Anforderungen bestimmen und ein geeignetes Profil des angeforderten Modells wählen.
3. Ein bereites, kompatibles Replikat zuweisen und die Ausführung starten.
4. Antwort liefern, Slot freigeben und temporäre Inhalte gemäß den Datenregeln löschen.

Ein logischer Vorgang hat eine `request_id`; einzelne Rechenversuche haben eine `attempt_id`. Vor Beginn der Ausgabe kann innerhalb der ursprünglichen Gesamtdauer auf einem kompatiblen Replikat erneut versucht werden. Eine Wiederherstellung kann die Latenz erhöhen.

Nach Beginn eines Streams darf der Anfang einer Generation nicht mit der Fortsetzung einer neuen Generation verbunden werden. Ein abgebrochener Stream ist unvollständig und muss vom Client so behandelt werden.

## Stabile und unterbrechbare Ressourcen

Stabile Gruppen tragen die Grundlast und Wiederherstellung. Zusätzliche unterbrechbare Gruppen erweitern die Kapazität. Ein Replikat, das eine Warnung vor Ressourcenentzug erhält, nimmt keine neuen Vorgänge an. Der Verlust eines kritischen Beschleunigers macht das davon abhängige Replikat unbrauchbar. Unabhängige Fehlergruppen verringern die Folgen einzelner Ausfälle, garantieren aber keine dauernde Verfügbarkeit jedes Modells.

Quelle: [Rate Cloud: Funktionsweise](https://rate-cloud.com/how-it-works), abgerufen am 3. November 2026. [Zur Übersicht](../README.md).
