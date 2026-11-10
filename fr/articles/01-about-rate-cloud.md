# L’offre Rate Cloud

[English](../../articles/01-about-rate-cloud.md) · [Deutsch](../../de/articles/01-about-rate-cloud.md) · Français · [Русский](../../ru/articles/01-about-rate-cloud.md)

Rate Cloud repose sur un modèle d’achat simple : payer l’accès à un modèle d’IA choisi pendant une durée déterminée, puis utiliser son API sans quota cumulé de tokens. C’est utile lorsqu’une application multiplie les appels au modèle et que la facturation au token devient difficile à prévoir.

Un agent de programmation autonome peut lire un dépôt, planifier une modification, éditer des fichiers, utiliser des outils, examiner les erreurs et recommencer. Chaque cycle peut ajouter une requête ainsi que des tokens en entrée et en sortie. Pendant la période active, le prix de l’abonnement n’augmente pas avec le nombre de tokens consommés.

## Tokens sans quota cumulé, capacité de traitement finie

L’absence de quota cumulé signifie que Rate Cloud ne fixe pas de plafond journalier, hebdomadaire ou mensuel sur le total de tokens en entrée et en sortie pendant la période payée. Cela ne signifie pas qu’une requête peut contenir un contexte infini ou durer sans fin. La capacité de contexte, les délais, les traitements simultanés, les limites de protection, le matériel et la disponibilité restent finis.

Le volume mensuel réel dépend du modèle, de la longueur des entrées et des réponses, de la vitesse et du parallélisme disponible. Les exemples portant sur des centaines de millions ou des milliards de tokens illustrent le principe tarifaire, sans garantir un volume mensuel traité.

## Quatre créneaux simultanés par abonnement payant

Chaque abonnement payant fournit quatre requêtes simultanées pour son modèle. Un créneau correspond à une requête en cours de traitement. Il est libéré à la fin de l’opération. Ce n’est pas une limite de quatre requêtes par jour ou par mois.

Une limite de fréquence s’applique aussi à l’ensemble du compte : 20 nouvelles requêtes LLM dans toute fenêtre glissante de 60 secondes. Elle est partagée entre tous les modèles, clés API, abonnements, forfaits Full model et les deux origines du service. Les abonnements ou forfaits Full model supplémentaires augmentent les créneaux simultanés décrits ci-dessous, mais ne relèvent pas cette limite de fréquence. Une réponse 429 due à la limite de fréquence signifie que le compte a atteint son quota de requêtes dans la fenêtre glissante. Une réponse 429 due aux créneaux signifie que tous les créneaux simultanés applicables sont occupés. Ce sont deux limites distinctes.

Un développeur peut répartir les créneaux entre un agent principal et trois sous-agents, quatre sessions de travail ou des automatisations indépendantes. Les clés API d’un même compte partagent le pool de créneaux du modèle concerné. Créer d’autres clés n’ajoute pas de capacité.

Les abonnements peuvent se cumuler. Deux abonnements au même modèle fournissent huit créneaux pour ce modèle. Des abonnements à des modèles différents disposent de pools distincts, par exemple quatre créneaux GLM et quatre DeepSeek. Pour utiliser chaque pool, les requêtes doivent viser le modèle correspondant.

## Durées et démarrage

Le site propose des abonnements de 3, 7 et 30 jours. Après l’inscription et les vérifications requises de l’adresse e-mail et de Telegram, les nouveaux utilisateurs peuvent tester les modèles pendant les trois premières heures, avec un créneau simultané. L’essai et les abonnements payants ont des limites différentes.

Commencez par une tâche représentative : un dépôt que vous utilisez, un document courant ou un vrai scénario d’automatisation. Évaluez la réponse, le comportement des outils et le délai total jusqu’à un résultat exploitable avant de choisir un modèle et une durée.

## À quels usages le service convient-il ?

Rate Cloud peut servir de couche modèle pour des agents de programmation, assistants internes, bots, chaînes d’extraction de données, traitements de documents et produits personnalisés. Un client compatible fournit son interface, ses outils, ses consignes de projet et son historique. Les fonctions dépendantes du modèle varient selon le modèle et l’intégration.

Le service vend un accès API. Connecter une application familière ne transforme pas le modèle GLM, DeepSeek ou Qwen choisi en modèle propriétaire de l’éditeur de cette application.

Sources : [site Rate Cloud](https://rate-cloud.com/) et [fonctionnement](https://rate-cloud.com/how-it-works). État au 3 novembre 2026. [Retour à la présentation](../README.md).

## Full model

Full model réunit les cinq modèles actuels : GLM 5.3, GLM 5.3 Flash, DeepSeek V4.1 Flash, DeepSeek V4 Pro et Qwen 3.8 Max.

Un pack coûte $45.45 pour 30 jours, $22.72 pour 7 jours ou $13.63 pour 3 jours. Un code de 10 % réduit ces montants à $40.90, $20.45 et $12.27, selon le taux public du 3 novembre 2026. Vérifiez le total de la commande avant le paiement.

Chaque pack ajoute un emplacement simultané à chaque modèle. Les quantités s’additionnent pour tous les modèles et ne sont pas transférables : deux packs autorisent deux requêtes simultanées par modèle. Un achat supplémentaire ajoute des emplacements pour sa période payée. Le renouvellement de la quantité choisie prolonge la période sans changer les emplacements. Les abonnements individuels ajoutent une capacité indépendante. Le premier achat suit les règles habituelles de codes promo, parrainage et bonus. Le renouvellement manuel constitue une nouvelle commande et peut utiliser un code promo ou des bonus si le compte respecte les règles habituelles d’éligibilité. Le renouvellement automatique via Whop est facturé au plein tarif convenu, sans répéter la remise de bienvenue.
