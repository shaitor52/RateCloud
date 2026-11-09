# Comprendre la vitesse et les performances

[English](../../articles/04-performance.md) · [Deutsch](../../de/articles/04-performance.md) · Français · [Русский](../../ru/articles/04-performance.md)

La question utile est le délai nécessaire pour obtenir un résultat exploitable pour votre tâche. Un débit élevé pendant la génération ne décrit pas toute l’expérience : l’attente, le traitement de l’entrée, la longueur de la réponse et les reprises comptent aussi.

## Données de performance actuelles

Les valeurs ont été communiquées par le propriétaire le 9 novembre 2026. Le délai avant le premier texte et la vitesse de génération sont deux mesures distinctes. Le contexte d’entrée est d’environ 200 000 tokens ; les résultats dépendent de la charge de travail.

| Modèle | Délai avant le premier texte (s) | Génération de réponse (tokens/s) |
| --- | ---: | ---: |
| GLM 5.3 | 15,6 | 52,7 |
| GLM 5.3 Flash | 18,9 | 50,7 |
| DeepSeek V4.1 Flash | 11,2 | 150,8 |
| DeepSeek V4 Pro | 10,0 | 142,6 |
| Qwen 3.8 Max | 13,0-13,5 | 59,0-63,4 |

[Données de performance actuelles au format CSV](../../data/performance-2026-11-09.csv). Les plages de Qwen couvrent deux essais.

Le [CSV du 3 novembre](../../data/performance-2026-11-03.csv) est conservé comme donnée historique.

## Pourquoi votre tâche peut être plus longue

Un document volumineux demande davantage de traitement en entrée qu’une question courte. Une réponse détaillée prend plus de temps à générer. Les agents avec outils peuvent effectuer plusieurs appels. La charge actuelle, l’admissibilité du profil, la disponibilité du réplica et une reprise influent aussi sur la durée.

## Concurrence et débit total

Quatre créneaux payants permettent d’exécuter plusieurs opérations indépendantes en parallèle. Ils ne rendent pas une requête quatre fois plus rapide. Le parallélisme aide si le travail peut être réparti ; une chaîne séquentielle de raisonnement ou d’outils attend toujours ses dépendances.

Pour une évaluation concrète, mesurez votre propre délai jusqu’au résultat utile, l’exactitude, les requêtes incomplètes, les erreurs et le besoin de relance. Notez le modèle, la taille des entrées et sorties, la concurrence et la période observée.

Source : [tableau et explications des performances publiés par Rate Cloud](https://rate-cloud.com/). Voir aussi la [documentation de connexion](https://rate-cloud.com/docs). [Retour à la présentation](../README.md).
