# Rate Cloud face aux API officielles : coût fixe pour un usage soutenu

[English](../../articles/08-cost-and-service-comparison.md) · [Deutsch](../../de/articles/08-cost-and-service-comparison.md) · Français · [Русский](../../ru/articles/08-cost-and-service-comparison.md)

**L’avantage de Rate Cloud est un prix d’abonnement fixe, sans quota cumulé de tokens. Le prix du modèle reste le même lorsque l’usage augmente.** Une API à la consommation facture chaque token facturable. Rate Cloud peut donc réduire sensiblement le coût d’un travail soutenu de programmation, d’analyse ou d’automatisation, à condition que le flux convienne à sa vitesse, sa concurrence, ses fonctions et sa disponibilité.

Rate Cloud n’est pas automatiquement moins cher en cas d’usage faible. Les fournisseurs officiels proposent des réductions utiles pour le cache, le traitement par lots, les heures creuses et d’autres conditions. Cette comparaison explicite ces compromis. Vérifiée le 3 novembre 2026 ; elle ne prédit pas les tarifs futurs.

## Tarifs des API officielles et abonnements Rate Cloud

Les prix USD sont par million de tokens. Les prix d’entrée du tableau sont **sans cache**. L’affichage en USD du site Rate Cloud a été vérifié le 3 novembre 2026. Il indique le prix sur 30 jours d’un abonnement à un modèle avec quatre créneaux. Cet affichage ne garantit pas un prix fixe en USD avant paiement.

| API officielle et condition de facturation | Entrée USD/M | Sortie USD/M | Modèle Rate Cloud / affichage USD pour 30 jours |
| --- | ---: | ---: | --- |
| Z.ai GLM-5.3 | 1,40 | 4,40 | GLM 5.3 / $34,38 |
| Z.ai GLM-5.3-Flash | 0,15 | 0,50 | GLM 5.3 Flash / $30,16 |
| DeepSeek V4.1 Flash, heures creuses | 0,15 | 0,60 | DeepSeek V4.1 Flash / $30,16 |
| DeepSeek V4.1 Flash, heures de pointe | 0,30 | 1,20 | DeepSeek V4.1 Flash / $30,16 |
| DeepSeek V4 Pro, heures creuses | 0,66 | 1,98 | DeepSeek V4 Pro / $27,56 |
| DeepSeek V4 Pro, heures de pointe | 1,32 | 3,96 | DeepSeek V4 Pro / $27,56 |
| QwenCloud Qwen3.8-Max, point d’accès Singapour | 2,00 | 6,00 | Qwen 3.8 Max / $31,49 |
| OpenAI GPT-6.1 Sol, Standard à contexte court | 2,00 | 10,00 | Alternative d’un autre modèle ; GPT n’est pas vendu ici |

Sources : [tarifs Z.ai](https://docs.z.ai/guides/overview/pricing), [tarifs et plages horaires DeepSeek](https://api-docs.deepseek.com/quick_start/pricing/), [tarifs QwenCloud et point d’accès Singapour](https://www.qwencloud.com/models/qwen3.8-max), [tarifs GPT-6.1 Sol](https://developers.openai.com/api/docs/models/gpt-6.1-sol) et [catalogue Rate Cloud](https://rate-cloud.com/).

Le nom officiel de l’API DeepSeek Flash est `deepseek-flash` pour la version V4.1-Flash-1017 ; Rate Cloud utilise `deepseek-v4.1-flash`. Les heures de pointe DeepSeek sont de 01:00 à 04:00 et de 06:00 à 10:00 UTC, du lundi au vendredi hors jours fériés chinois ; les autres heures sont creuses. Les lignes GLM et DeepSeek comparent les versions nommées correspondantes. Qwen partage une étiquette de famille de produit, mais les fonctions d’hébergement et profils d’exécution peuvent différer. GPT est une solution de rechange pour un travail similaire, pas une comparaison de poids, de capacités ou de qualité identiques.

## Coût d’un usage répété

Hypothèse : 80 % des tokens facturés en entrée et 20 % en sortie, sans cache, outils, batch, taxes, réductions spéciales ni supplément de long contexte. Le cas échéant, incluez les tokens de raisonnement dans la sortie facturable. Ce sont des **scénarios de calcul**, pas des données d’utilisation réelle ni une promesse que Rate Cloud peut traiter ce volume en 30 jours.

| API officielle | 10 M tokens | 100 M | 500 M | 1 milliard |
| --- | ---: | ---: | ---: | ---: |
| GLM-5.3 | $20 | $200 | $1 000 | $2 000 |
| GLM-5.3-Flash | $2,20 | $22 | $110 | $220 |
| DeepSeek Flash creuses / pointe | $2,40 / $4,80 | $24 / $48 | $120 / $240 | $240 / $480 |
| DeepSeek Pro creuses / pointe | $9,24 / $18,48 | $92,40 / $184,80 | $462 / $924 | $924 / $1 848 |
| Qwen3.8-Max | $28 | $280 | $1 400 | $2 800 |
| GPT-6.1 Sol Standard | $36 | $360 | $1 800 | $3 600 |

**Les prix Rate Cloud affichés lors de la consultation se situaient entre 27,56 $ et 34,38 $ pour 30 jours dans ces scénarios de volume.** Cet instantané de l’affichage en USD ne garantit pas un prix fixe avant paiement ni le traitement d’un milliard de tokens. Plusieurs abonnements, des créneaux supplémentaires, l’hébergement du client, la recherche web, le calcul CI et les autres outils de votre application peuvent entraîner des frais.

## Calculer le seuil de rentabilité plutôt que promettre des économies universelles

Selon l’affichage monétaire du site au 3 novembre 2026, 500 M de tokens sans cache coûtaient 1 000 $ sur l’API officielle GLM-5.3, contre 34,38 $ pour l’abonnement Rate Cloud affiché, soit environ 29,1 fois le coût d’accès au modèle. Pour l’API DeepSeek Flash la moins chère en heures creuses, le même calcul donne 120 $ contre 30,16 $, soit environ 4,0 fois. Il s’agit d’un instantané de l’affichage en USD, pas d’un prix fixe garanti avant paiement ; le coût réel dépend du tarif de facturation et de la charge.

Aux prix affichés en USD, le seuil de rentabilité sans cache est d’environ 17,19 M de tokens pour GLM-5.3, 137,09 M pour GLM Flash, 125,67 M pour DeepSeek Flash en heures creuses, 29,83 M pour DeepSeek Pro en heures creuses et 11,25 M pour Qwen. En dessous du seuil concerné, la facture API à l’usage peut être plus basse. Un taux élevé de cache en entrée repousse ces seuils.

Formule générale, volume exprimé en millions :

```text
weighted USD per million = input_fraction * input_price + output_fraction * output_price
break_even_millions = subscription_USD / weighted_USD_per_million
```

Exemple de sensibilité avec toutes les entrées servies depuis le cache pour DeepSeek Flash en heures creuses : 0,003 $ en entrée et 0,60 $ en sortie. À 500 M de tokens au ratio 80/20, le coût est de 61,20 $, et non 120 $. Cela représente environ 2,0 fois le prix Rate Cloud affiché de 30,16 $. L’éligibilité réelle au cache n’est pas garantie et les écritures cache ou autres frais peuvent compter. Qwen, Z.ai et OpenAI proposent aussi des réductions cache. OpenAI offre des tarifs Batch/Flex plus bas et facture davantage les modes long contexte/Fast. Comparez le tarif réellement applicable.

Reproduisez ces scénarios hors ligne avec les [données tarifaires datées](../../data/pricing-2026-11-03.json) et le [calculateur](../../tools/compare_costs.py) :

```sh
python3 tools/compare_costs.py --million-tokens 500
python3 tools/compare_costs.py --million-tokens 500 --cached-input-share 1
```

À lancer depuis la racine du dépôt. Aucune requête API n’est envoyée. La sortie utilise des prix en USD.

## Compromis de vitesse et de service

Choisissez Rate Cloud si le coût prévisible pour un travail soutenu compte plus que la latence minimale de chaque réponse. Un fournisseur direct ou un niveau premium rapide peut mieux convenir si vos propres essais montrent une latence plus courte, ou si vous avez besoin de fonctions hébergées, d’une concurrence bien supérieure ou de conditions contractuelles. Les quatre créneaux Rate Cloud ne sont pas équivalents aux capacités de concurrence des API officielles.

Ce dépôt ne contient **aucun benchmark contrôlé de vitesse** avec consignes et réglages identiques pour tous ces services. Nous ne publions donc pas de débit concurrentiel inventé en tokens/s et ne prétendons pas disposer d’un classement universel mesuré. L’instantané publié de Rate Cloud figure dans [performances](04-performance.md). Il inclut l’attente et diffère de la vitesse pure de génération. Cette comparaison reconnaît les compromis de latence et de capacité sans les présenter comme un résultat comparatif direct établi.

Les abonnements de programmation officiels et les applications de chat gratuites sont des produits différents de l’accès API à la consommation. Ce tableau compare les API citées, pas tous les forfaits des fournisseurs. Évaluez aussi la qualité et les fonctions.

[Cas d’usage où un coût fixe aide](09-unlimited-use-cases.md) · [Retour à la présentation](../README.md)
