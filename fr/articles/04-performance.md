# Comprendre la vitesse et les performances

[English](../../articles/04-performance.md) · [Deutsch](../../de/articles/04-performance.md) · Français · [Русский](../../ru/articles/04-performance.md)

La question utile est le délai nécessaire pour obtenir un résultat exploitable pour votre tâche. Un débit élevé pendant la génération ne décrit pas toute l’expérience : l’attente, le traitement de l’entrée, la longueur de la réponse et les reprises comptent aussi.

## Instantané des performances publiées

Les valeurs suivantes figuraient sur la page d’accueil Rate Cloud le 3 novembre 2026. Cette date est celle de la consultation, pas une période de mesure établie indépendamment.

| Modèle | Réponse complète typique, secondes | Tokens/s effectifs typiques, attente comprise | Tokens/s effectifs des réponses rapides, attente comprise |
| --- | ---: | ---: | ---: |
| GLM 5.3 | 21,48 | 14,05 | 58,47 |
| GLM 5.3 Flash | 23,32 | 14,58 | 61,92 |
| DeepSeek V4 Pro | 15,67 | 25,83 | 127,84 |
| DeepSeek V4.1 Flash | 14,99 | 19,22 | 78,38 |
| Qwen 3.8 Max | 21,37 | 13,13 | 80,68 |

Ce sont des observations de service publiées, pas des délais garantis, des benchmarks matériels fixes ou une comparaison contrôlée sur des requêtes identiques. La page d’accueil ne fournit avec ce tableau ni taille de cohorte ni intervalle complet de mesure ; ces chiffres ne prouvent donc ni disponibilité durable ni SLA.

## Sens des colonnes

Le temps de réponse complet va de l’envoi de la requête à la réception du résultat terminé. Il inclut l’attente, le traitement de l’entrée et la production de la réponse.

Selon le site, « typique » désigne la médiane : la moitié des résultats est plus rapide, l’autre moitié plus lente. Les débits effectifs incluent toute la requête et son attente. Il ne faut pas les renommer vitesse de décodage pure ou délai avant le premier token.

La colonne des réponses rapides décrit les dix requêtes les plus rapides sur cent. Elle montre la partie rapide de la distribution observée, sans garantir ce débit pour une nouvelle requête. Ne multipliez pas des mesures de latence et de débit résumées séparément pour en déduire une longueur moyenne de sortie.

## Pourquoi votre tâche peut être plus longue

Un document volumineux demande davantage de traitement en entrée qu’une question courte. Une réponse détaillée prend plus de temps à générer. Les agents avec outils peuvent effectuer plusieurs appels. La charge actuelle, l’admissibilité du profil, la disponibilité du réplica et une reprise influent aussi sur la durée.

Un modèle présenté comme rapide ou adapté aux appels fréquents peut afficher une durée médiane observée supérieure à celle d’un autre modèle si les requêtes étudiées diffèrent. Le tableau ne sépare pas la vitesse du modèle de la complexité des consignes, de la longueur des réponses ou du comportement des utilisateurs.

## Concurrence et débit total

Quatre créneaux payants permettent d’exécuter plusieurs opérations indépendantes en parallèle. Ils ne rendent pas une requête quatre fois plus rapide. Le parallélisme aide si le travail peut être réparti ; une chaîne séquentielle de raisonnement ou d’outils attend toujours ses dépendances.

Pour une évaluation concrète, mesurez votre propre délai jusqu’au résultat utile, l’exactitude, les requêtes incomplètes, les erreurs et le besoin de relance. Notez le modèle, la taille des entrées et sorties, la concurrence et la période observée.

Source : [tableau et explications des performances publiés par Rate Cloud](https://rate-cloud.com/). Voir aussi la [documentation de connexion](https://rate-cloud.com/docs). [Retour à la présentation](../README.md).

## Résultats publics disponibles et données téléchargeables

Le tableau ci-dessus contient les 15 valeurs numériques publiées dans le tableau des performances de la page d’accueil pour les cinq modèles au moment de la consultation. Un [instantané CSV](../../data/performance-2026-11-03.csv) conserve les IDs modèles, unités, date de consultation et URL source. Aucun nouveau benchmark n’a été réalisé pour créer ce fichier.

| Élément de preuve | Disponible dans cet instantané ? |
| --- | --- |
| Durée typique de réponse complète, cinq modèles | Oui, tableau et CSV |
| Débit typique effectif, attente comprise, cinq modèles | Oui, tableau et CSV |
| Débit effectif du décile le plus rapide, cinq modèles | Oui, tableau et CSV |
| Durées brutes par requête, taille de l’échantillon et période d’observation | Non fournis avec le tableau public |
| Délai avant le premier token, vitesse de décodage pure, percentiles de latence | Non fournis dans le tableau public |
| Comparaison contrôlée à charge identique avec les fournisseurs officiels | Indisponible dans ce dépôt |

La page d’accueil renvoie à la méthodologie `/docs#statistics` ; lors de la consultation, la documentation de connexion actuelle ne présentait pas de section statistique détaillée correspondante. Nous signalons cette lacune au lieu d’inventer d’autres résultats. Pour l’arbitrage tarifaire, voir la [comparaison des API officielles](08-cost-and-service-comparison.md).
