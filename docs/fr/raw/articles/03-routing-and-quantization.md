# Routage intelligent et quantification

[English](../../articles/03-routing-and-quantization.md) · [Deutsch](../../de/articles/03-routing-and-quantization.md) · Français · [Русский](../../ru/articles/03-routing-and-quantization.md)

L’architecture publique de Rate Cloud décrit une combinaison de capacité de calcul stable, de ressources d’entreprise supplémentaires disponibles, de profils de précision validés et d’un routage adapté aux requêtes. L’objectif est d’utiliser efficacement les ressources tout en préservant l’identité et les exigences fonctionnelles du modèle choisi.

Cet article présente l’architecture publiée. Il ne constitue ni un audit indépendant de chaque déploiement en production ni une garantie que toutes les combinaisons matérielles et de précision sont toujours disponibles.

## Capacité de calcul et réplicas de modèles

Le service indique louer de la capacité disponible auprès de grappes d’entreprise en complément d’une réserve stable. Rate Cloud gère le placement des poids, les moteurs d’inférence, les profils de précision et la distribution des requêtes.

L’architecture cite des systèmes Huawei Atlas et des accélérateurs Ascend, notamment Atlas 800I A2 et A3 pour les grands modèles, ainsi que Atlas 900 A2 PoD et A3 SuperPoD pour les groupes distribués. La compatibilité matérielle est évaluée pour chaque modèle. Déplacer une requête entre sites ne revient pas à répartir arbitrairement entre sites les calculs étroitement couplés d’un modèle : ceux d’un réplica utilisent un réseau local compatible.

Un réplica utilisable nécessite davantage que de la mémoire disponible : poids compatibles, moteur pris en charge, fonctions API requises, modèle chargé et préchauffé, puis contrôle de disponibilité réussi.

## Effets de la quantification

Les paramètres du modèle et les calculs intermédiaires peuvent employer différents formats numériques. Des formats plus compacts réduisent les besoins mémoire et peuvent améliorer l’efficacité, mais aussi influencer la qualité. Les précisions plus faibles doivent donc être évaluées par rapport à la version source et aux tâches concernées.

La conception publiée utilise des profils qualité, équilibré et économique d’un même modèle. Un profil qualité peut employer le format source validé, W8A8 ou une autre configuration approuvée. Un profil équilibré peut combiner des composants de précisions différentes, par exemple 4 et 8 bits. Une moyenne effective proche de 6 bits ne signifie pas qu’il existe une implémentation INT6 universelle. Les profils économiques peuvent utiliser des configurations W4A16, W4A8 ou MXFP4 validées, si le modèle et le matériel les prennent en charge.

La disponibilité d’un format dépend de la version du modèle, du matériel, du moteur et des vérifications qualité ; le format n’est pas proposé indistinctement pour tous les modèles. Augmenter la précision nominale de poids déjà quantifiés ne restaure pas l’information précédemment perdue.

## Contrôles qualité avant le routage

Les profils sont comparés à la version source exacte sur des tâches publiques, synthétiques et conçues spécialement : code, mathématiques, contexte long, outils et JSON strict. Le processus publié tient compte de la qualité, de la mémoire, de la vitesse et du comportement de l’API. Les conversations des utilisateurs ne servent ni à l’entraînement ni au calibrage.

Un profil compact n’est admissible que pour les tâches qu’il peut traiter convenablement. Le code difficile, les mathématiques, l’usage d’outils, les schémas stricts et les requêtes incertaines donnent la priorité à la qualité. Une consigne courte peut être difficile. `reasoning_effort` est un réglage distinct, pas un effet de la quantification.

## Choix du routeur

Le routeur considère les besoins de contexte, les images, les outils, le format de sortie, la complexité, la mémoire disponible, la file d’attente, l’état des réplicas et la durée de ressources restante. Il détermine d’abord les routes adaptées ; le coût n’intervient qu’entre ces options.

Le modèle sélectionné reste fixe. La révision des poids et les fonctions autorisées le sont aussi pour l’opération. Un serveur incompatible est écarté avant l’affectation. Si aucune capacité adaptée n’est disponible, le système peut attendre dans son budget interne ou renvoyer une erreur explicite d’indisponibilité temporaire, sans substituer silencieusement un autre modèle.

## Cycle d’une requête

1. Établir la connexion protégée et vérifier la clé API, l’abonnement et la disponibilité d’un créneau.
2. Déterminer les besoins et choisir un profil admissible du modèle demandé.
3. Affecter un réplica prêt et compatible, puis lancer l’exécution.
4. Transmettre la réponse, libérer le créneau et effacer le contenu temporaire selon les règles de traitement.

Une opération logique possède un `request_id` ; chaque tentative de calcul possède un `attempt_id`. Avant le début de la réponse, une reprise peut essayer un réplica compatible dans le délai global initial. Elle peut augmenter la latence.

Une fois le flux commencé, le début d’une génération ne doit pas être assemblé à la suite d’une nouvelle génération. Le client doit traiter un flux interrompu comme incomplet.

## Ressources stables et interruptibles

Les groupes stables assurent la charge de base et la reprise. Des groupes interruptibles supplémentaires augmentent la capacité. Un réplica averti d’un retrait de ressources cesse d’accepter de nouvelles opérations. La perte d’un accélérateur critique rend indisponible le réplica qui en dépend. Des groupes de panne indépendants limitent l’impact d’un incident, sans garantir une disponibilité permanente de chaque modèle.

Source : [fonctionnement de Rate Cloud](https://rate-cloud.com/how-it-works), consulté le 3 novembre 2026. [Retour à la présentation](../README.md).
