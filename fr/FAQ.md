# Rate Cloud : questions fréquentes

[English](../FAQ.md) · [Deutsch](../de/FAQ.md) · [Русский](../ru/FAQ.md) · Français · [Présentation](README.md)

Les informations produit reflètent le site officiel au 3 novembre 2026. Avant tout achat, vérifiez les informations de l’espace client et les conditions en vigueur.

## Qu’est-ce que Rate Cloud ?

Rate Cloud fournit un accès API par abonnement à GLM, DeepSeek et Qwen pour le développement, les agents IA, l’automatisation et les applications. L’abonnement porte sur un modèle et une durée, plutôt que sur chaque million de tokens. Voir [la présentation du service](articles/01-about-rate-cloud.md).

## Existe-t-il une limite de tokens ?

Un abonnement actif n’impose pas de quota cumulé de tokens en entrée ou en sortie. Le contexte d’une opération, son délai et les contraintes techniques restent finis. Le volume traité dépend de la vitesse, de la longueur des entrées et sorties, des créneaux disponibles et de la disponibilité du service.

## Quatre créneaux signifient-ils seulement quatre requêtes ?

Non. Un abonnement payant permet quatre requêtes simultanées. Chaque opération terminée libère son créneau. Les différentes clés API d’un même compte partagent le pool du modèle concerné.

## Puis-je augmenter le parallélisme ?

L’offre publique permet de cumuler des abonnements. Deux abonnements au même modèle fournissent huit créneaux pour ce modèle. Les abonnements à des modèles différents ont chacun leur pool.

## Quels modèles puis-je utiliser ?

Le catalogue publié comprend GLM 5.3, GLM 5.3 Flash, DeepSeek V4.1 Flash, DeepSeek V4 Pro et Qwen 3.8 Max. Le [catalogue daté](articles/02-models.md) indique les IDs API exacts, les tarifs, le positionnement et la prise en charge des images.

## Flash est-il le même modèle que Pro ?

Non. Ce sont des entrées distinctes du catalogue. Les profils de précision sont des variantes d’exécution du modèle sélectionné ; ils n’autorisent pas à le remplacer discrètement par un autre. Voir [routage et quantification](articles/03-routing-and-quantization.md).

## Comment le routage intelligent choisit-il un profil de précision ?

La conception publiée vérifie les besoins de la tâche et les réplicas admissibles, privilégie la qualité pour les tâches difficiles ou incertaines et ne considère le coût qu’entre routes adaptées. Contexte, images, outils, format de sortie, mémoire disponible, files d’attente et état des réplicas influent sur l’admissibilité. La prise en charge dépend du modèle et du matériel.

## La quantification garantit-elle des réponses identiques ?

Non. La précision numérique peut modifier la qualité. L’architecture publique décrit des contrôles par rapport à la version source et des critères qualité propres aux tâches. Un profil économique n’est admissible que si sa qualité convient. La quantification est indépendante du réglage de l’effort de raisonnement.

## Quelles applications puis-je connecter ?

Le guide officiel couvre OpenCode, Codex, Claude Code, OpenClaw, Continue, Hermes et d’autres clients compatibles. Nos [guides pratiques](guides/README.md) présentent certains réglages. Les fonctions dépendent du client et du modèle ; connecter un client ne transforme pas le modèle choisi en modèle propriétaire de l’éditeur du client.

## Quelle URL de base utiliser ?

L’URL générale compatible OpenAI est `https://llm.rate-cloud.com/v1`. Des URL spécifiques existent pour certains clients. Consultez la [documentation officielle](https://rate-cloud.com/docs) et le guide correspondant sans mélanger les familles de points d’accès.

## Pourquoi un modèle répertorié refuse-t-il ma requête ?

La présence au catalogue ne prouve pas l’autorisation d’exécution. Vérifiez l’essai ou l’abonnement actif, les modèles permis par la clé, son expiration, les restrictions IP et les options de compatibilité du client. Vérifiez aussi les créneaux occupés et l’erreur reçue. Communiquez au support l’heure et l’identifiant de requête, sans clé ni contenu privé.

## Quelle est la vitesse de Rate Cloud ?

Le site publie un tableau historique de performances mesurant la latence complète et les débits effectifs, attente comprise. Votre tâche peut différer. Voir [performances et méthodologie](articles/04-performance.md) ; ces chiffres ne constituent ni un SLA garanti ni un benchmark contrôlé sur des consignes identiques.

## Les consignes servent-elles à entraîner les modèles ?

Le service indique ne pas utiliser les données des utilisateurs pour l’entraînement et ne pas créer d’historique permanent des textes des requêtes et réponses. Le traitement temporaire, le cache de calcul isolé, les métadonnées opérationnelles et les données de compte sont des catégories distinctes. Voir [confidentialité et fiabilité](articles/06-privacy-and-reliability.md) et la politique actuelle sur le site.

## Chaque modèle est-il disponible 24 h/24 et 7 j/7 ?

Non. Le site ne garantit pas la disponibilité permanente de chaque modèle. La règle de compensation publiée couvre une condition précise d’indisponibilité totale du système, pas chaque requête lente ni chaque erreur de modèle. Consultez les conditions applicables.

## Puis-je essayer avant de payer ?

L’essai publié donne accès aux modèles pendant les trois premières heures après inscription et vérification de l’adresse e-mail et de Telegram, avec un créneau simultané. Vérifiez son état dans l’espace client.

## Puis-je vendre des abonnements sous ma marque ?

Rate Cloud propose un service White Label avec identité visuelle, site et espace client, paiements et infrastructure technique. Voir l’[article White Label](articles/07-white-label.md) et l’[offre actuelle](https://rate-cloud.com/white-label).

Sources : [page d’accueil](https://rate-cloud.com/), [fonctionnement](https://rate-cloud.com/how-it-works) et [guide API](https://rate-cloud.com/docs).
