# Notre infrastructure : location de capacité, déploiement des modèles et exploitation de l’inférence

[English](../../articles/10-infrastructure.md) · [Deutsch](../../de/articles/10-infrastructure.md) · Français · [Русский](../../ru/articles/10-infrastructure.md)

**Rate Cloud loue de la capacité informatique d’entreprise, déploie les poids des modèles et gère leur exécution.** Notre rôle couvre l’infrastructure et le flux d’inférence : choix du matériel et des moteurs compatibles, préparation des profils, mise en service des réplicas, routage des requêtes et reprise.

Les clients choisissent un modèle et connectent leurs outils par l’API. Rate Cloud exploite la couche de calcul qui fournit cet accès. Le matériel est loué auprès de propriétaires d’entreprise ; la propriété de l’équipement loué et l’exploitation de l’environnement qui exécute les modèles relèvent de responsabilités distinctes.

## Ce que Rate Cloud gère

| Domaine | Notre travail |
| --- | --- |
| Capacité de calcul | Louer de la capacité d’entreprise et combiner une réserve stable à des ressources supplémentaires disponibles |
| Déploiement des modèles | Placer les poids compatibles et préparer le moteur d’inférence pour la version choisie |
| Profils de précision | Valider les profils originaux, mixtes ou quantifiés admissibles du même modèle |
| Disponibilité des réplicas | Charger les poids, préchauffer l’exécution, contrôler l’état et n’admettre que les réplicas adaptés |
| Routage des requêtes | Tenir compte du contexte, des images, outils, format de sortie, mémoire, file d’attente et état des réplicas |
| Exploitation et reprise | Surveiller l’exécution, retirer les réplicas défaillants et reprendre, si possible, dans le délai initial |

C’est pourquoi la description du service couvre le placement des poids, les moteurs d’inférence, la précision et le cycle de vie des réplicas, en plus d’un point d’accès API. Ces responsabilités opérationnelles sont au cœur de l’architecture publiée.

## Familles matérielles de l’architecture publiée

L’architecture cite les systèmes Huawei Atlas et les accélérateurs Ascend. Ce sont des descriptions publiques de plateformes, pas un inventaire en temps réel de chaque machine ni la promesse que chaque modèle fonctionne sur chaque équipement listé.

| Plateforme | Rôle publié |
| --- | --- |
| Atlas 800I A2 | Inférence de grands modèles ; huit NPU de 64 Go chacun |
| Atlas 800I A3 | Inférence de grands modèles ; huit NPU physiques de 128 Go chacun, présentés comme seize dispositifs logiques |
| Atlas 900 A2 PoD et A3 SuperPoD | Groupes distribués d’accélérateurs pour les grands modèles |
| Atlas 500 et 500 A2 | Tâches de service plus modestes |
| Atlas 800 avec Atlas 300I Duo | Classe de compatibilité distincte, évaluée séparément |

Les représentations physique et logique de l’A3 désignent la même mémoire et ne doivent pas être additionnées. La compatibilité est vérifiée pour chaque association de modèle, format de poids, moteur et matériel. Les calculs étroitement couplés utilisent un réseau local compatible ; déplacer des requêtes entières entre sites est une opération distincte.

## Des poids du modèle à une API exploitable

Un réplica doit disposer de la bonne version, d’un moteur compatible, de mémoire suffisante, des fonctions autorisées, d’un préchauffage terminé et d’un contrôle de disponibilité réussi. Du matériel libre ne signifie pas à lui seul qu’un modèle est disponible.

Le routeur choisit un profil validé adapté du modèle demandé. La qualité est prioritaire pour le code difficile, les mathématiques, les outils, les schémas stricts et les tâches incertaines. Flash et Pro restent des modèles différents. Voir [routage et quantification](03-routing-and-quantization.md) pour le processus de sélection.

Les groupes stables soutiennent la charge de base et la reprise. Des ressources supplémentaires interruptibles augmentent la capacité disponible. Un avis de retrait de ressources arrête les nouvelles affectations au réplica concerné. Avant le début de la réponse, une reprise peut réessayer sur un réplica compatible dans le délai initial. Un flux interrompu doit rester visiblement incomplet.

## Pourquoi ce modèle d’exploitation permet l’accès par abonnement

En gérant ensemble capacité de calcul, profils de modèles et routage, Rate Cloud peut diriger les ressources adaptées. Les clients paient l’accès au modèle et la concurrence pendant une période d’abonnement, sans quota cumulé de tokens. Le traitement reste limité par la vitesse du modèle, le contexte, les délais, les créneaux et la disponibilité. Cela ne garantit ni volume mensuel fixe ni service continu 24 h/24 et 7 j/7.

Cet article décrit le modèle d’exploitation public et les responsabilités de Rate Cloud. Il n’affirme pas que chaque requête suit une voie d’exécution exclusive unique et ne certifie pas l’inventaire actuel des machines. L’architecture officielle et les conditions actuelles restent la référence.

## Découvrir le service

[Créer un compte Rate Cloud et essayer](https://rate-cloud.com/register). L’essai standard de trois heures nécessite la vérification de l’adresse e-mail et la liaison Telegram ; il comprend un créneau simultané. Les conditions d’une invitation valide sont distinctes : [avantages du parrainage](11-referral-program.md).

Vous avez déjà un compte ? [Ouvrir les consignes de connexion](https://rate-cloud.com/user/instructions). Vous souhaitez créer votre propre service sous votre marque ? [Découvrir White Label](https://rate-cloud.com/white-label).

Sources consultées le 3 novembre 2026 : [fonctionnement de Rate Cloud](https://rate-cloud.com/how-it-works), [conditions du service](https://rate-cloud.com/offer) et [accès aux modèles](https://rate-cloud.com/). [Retour à la documentation](../README.md).
