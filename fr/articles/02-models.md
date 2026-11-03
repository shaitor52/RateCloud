# Modèles et choix

[English](../../articles/02-models.md) · [Deutsch](../../de/articles/02-models.md) · Français · [Русский](../../ru/articles/02-models.md)

Le catalogue publié par Rate Cloud comprend cinq modèles. Chacun a son propre abonnement et un identifiant précis pour les requêtes HTTP directes. Choisissez selon le travail à effectuer, puis testez des entrées représentatives.

## Catalogue publié

| Modèle | ID API direct | Positionnement principal | Image en entrée | Prix publié pour 30 jours |
| --- | --- | --- | --- | ---: |
| GLM 5.3 | `glm-5.3` | Développement complexe et agents autonomes | Non | $34,38 |
| GLM 5.3 Flash | `glm-5.3-flash` | Requêtes fréquentes, programmation quotidienne, automatisation, sous-agents | Oui | $30,16 |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` | Agents de programmation et tâches parallèles | Oui | $30,16 |
| DeepSeek V4 Pro | `deepseek-v4-pro` | Raisonnement en plusieurs étapes, architecture et revue de code | Non | $27,56 |
| Qwen 3.8 Max | `qwen-3.8-max` | Grands dépôts, documents, recherche et contexte long | Oui | $31,49 |

L’affichage en USD du site a été vérifié le 3 novembre 2026. Tarifs et fonctionnalités peuvent évoluer ; l’affichage en USD ne garantit pas un prix fixe avant le paiement. Vérifiez les conditions actuelles dans l’espace client. Chaque abonnement payant indiqué comprend quatre requêtes simultanées et aucun quota cumulé de tokens pendant sa durée. La prise en charge des images en entrée signifie que le modèle accepte des images, pas qu’il en génère.

## Choisir selon le flux de travail

GLM 5.3 est présenté pour les projets logiciels complexes, l’analyse de dépôts, l’utilisation d’outils et la coordination de sous-agents. GLM 5.3 Flash vise les tâches courantes répétées et l’automatisation avec de nombreux appels.

DeepSeek V4.1 Flash est destiné à la génération et à la modification de code, aux agents de programmation et aux charges comportant de nombreuses tâches parallèles. DeepSeek V4 Pro met l’accent sur le raisonnement et l’analyse approfondie, notamment les décisions d’architecture et les revues où la qualité compte davantage que la latence minimale.

Qwen 3.8 Max est positionné pour les contenus volumineux, tels que dépôts et documents. La mention du contexte long ne constitue pas une valeur numérique de fenêtre de contexte. Vérifiez la documentation et les limites réelles avant de concevoir des flux avec de grandes entrées.

Ces usages ne forment ni un classement universel ni une garantie qu’un modèle sera supérieur pour chaque tâche. Évaluez l’exactitude, le respect des consignes, les appels d’outils, les besoins d’image, le délai et le travail de correction manuelle.

## Identité du modèle et profil d’exécution

Un modèle peut disposer de plusieurs profils de précision validés. Le routage sélectionne un profil adapté du modèle demandé. Un profil compact ne remplace pas silencieusement le modèle par une autre entrée du catalogue. Flash et Pro sont des modèles distincts.

Pour l’API directe, utilisez exactement les IDs du tableau. Les noms propres à certains clients peuvent ajouter un préfixe fournisseur, absent de l’identifiant HTTP direct. La présence d’un modèle dans la liste d’un client ne prouve pas que le compte ou la clé est autorisé à l’exécuter.

Sources : [catalogue et tarifs](https://rate-cloud.com/), [IDs des modèles API](https://rate-cloud.com/docs) et [profils des modèles](https://rate-cloud.com/how-it-works). [Retour à la présentation](../README.md).
