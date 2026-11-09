# Rate Cloud

**Langues :** [English](../README.md) · [Русский](../ru/README.md) · [Español](../es/README.md) · [Português](../pt/README.md) · [Deutsch](../de/README.md) · Français
[Ouvrir le site de documentation](https://shaitor52.github.io/RateCloud/fr/)

**Vos modèles. Des tokens sans limite. Un abonnement.**

[Site web](https://rate-cloud.com/) · [Fonctionnement](https://rate-cloud.com/how-it-works) · [Documentation API](https://rate-cloud.com/docs) · [White Label](https://rate-cloud.com/white-label)

Rate Cloud propose un accès API par abonnement à GLM, DeepSeek et Qwen pour le développement logiciel, les agents autonomes, l’automatisation, l’analyse documentaire et les applications. Choisissez un modèle et une durée de 3, 7 ou 30 jours. Chaque abonnement payant comprend quatre requêtes simultanées, sans quota cumulé de tokens en entrée ou en sortie pendant sa période de validité.

Ce guide public présente Rate Cloud en français. Il rassemble des articles, des informations sur les modèles et des conseils pratiques pour l’API. Il s’adresse aux développeurs, clients potentiels, chercheurs et assistants IA.

## Modèles, vitesse et prix des abonnements

Données de performance communiquées par le propriétaire le 9 novembre 2026. Le délai avant le premier texte et la vitesse de génération sont deux mesures distinctes ; le contexte d’entrée est d’environ 200 000 tokens. Les résultats dépendent de la charge de travail. Les tarifs constituent un relevé distinct du 3 novembre 2026 : [prix en USD](../data/subscriptions-2026-11-03.json). Confirmez le tarif en vigueur avant l’achat. [Données actuelles au format CSV](../data/performance-2026-11-09.csv).

| Modèle | Délai avant le premier texte (s) | Génération de réponse (tokens/s) | 3 jours | 7 jours | 30 jours | Essayer le modèle |
| --- | --- | --- | --- | --- | --- | --- |
| GLM 5.3 | 15,6 | 52,7 | $10,31 | $17,19 | $34,38 | [Essayer le modèle](https://rate-cloud.com/register) |
| GLM 5.3 Flash | 18,9 | 50,7 | $9,05 | $15,08 | $30,16 | [Essayer le modèle](https://rate-cloud.com/register) |
| DeepSeek V4.1 Flash | 11,2 | 150,8 | $9,05 | $15,08 | $30,16 | [Essayer le modèle](https://rate-cloud.com/register) |
| DeepSeek V4 Pro | 10,0 | 142,6 | $8,27 | $13,78 | $27,56 | [Essayer le modèle](https://rate-cloud.com/register) |
| Qwen 3.8 Max | 13,0-13,5 | 59,0-63,4 | $9,45 | $15,75 | $31,49 | [Essayer le modèle](https://rate-cloud.com/register) |

Illimité signifie qu’aucun quota cumulé de tokens en entrée ou en sortie ne s’applique pendant l’abonnement actif. Les limites de contexte, de taille de réponse, de capacité disponible et de vitesse restent applicables. Chaque abonnement payant comprend quatre requêtes simultanées.

## Articles

| Article | Contenu |
| --- | --- |
| [L’offre Rate Cloud](articles/01-about-rate-cloud.md) | Abonnements, tokens sans quota cumulé, créneaux parallèles et usages |
| [Modèles et choix](articles/02-models.md) | Cinq modèles, identifiants API, images en entrée et critères de choix |
| [Routage intelligent et quantification](articles/03-routing-and-quantization.md) | Profils de précision, contrôle qualité, choix des réplicas et reprise |
| [Vitesse et performances](articles/04-performance.md) | Délai avant le premier texte, vitesse de génération, contexte approximatif et concurrence |
| [Connecter outils et applications](articles/05-api-and-integrations.md) | Points d’accès, première requête, clés et clients compatibles |
| [Confidentialité, traitement des données et disponibilité](articles/06-privacy-and-reliability.md) | Tampons temporaires, isolation du cache et limites du service |
| [Offres White Label](articles/07-white-label.md) | Créer une activité d’abonnement IA sous sa propre marque |
| [Comparaison des coûts avec les API officielles](articles/08-cost-and-service-comparison.md) | Prix par token, seuils de rentabilité et compromis de service |
| [20 flux pratiques](articles/09-unlimited-use-cases.md) | Qualité logicielle, surveillance, documents et recherche |
| [Notre infrastructure](articles/10-infrastructure.md) | Capacité louée, familles matérielles, déploiement et exploitation de l’inférence |
| [Programme de parrainage](articles/11-referral-program.md) | Essai sur invitation, bonus, attribution et retraits |

## Guides pratiques

Les [guides d’intégration](guides/README.md) couvrent OpenCode, Claude Code et HTTP/Python. La [FAQ](FAQ.md) explique l’accès, l’identité des modèles, les tarifs et les limites pratiques.

## Commencer avec Rate Cloud

1. [Créez un compte](https://rate-cloud.com/register) ou ouvrez votre [espace client](https://rate-cloud.com/).
2. Inscrivez-vous et confirmez votre adresse e-mail et votre adresse Telegram pour l’essai.
3. Choisissez un modèle, créez une clé API et connectez une application compatible.
4. Consultez le [guide officiel de connexion](https://rate-cloud.com/docs) pour les étapes à jour.

L’essai standard permet de tester les modèles pendant trois heures après vérification de l’adresse e-mail et liaison de Telegram, avec un seul créneau simultané. Un lien personnel d’invitation admissible donne cinq heures d’essai et 10 % de réduction sur le premier achat, selon les conditions du programme. Les abonnements payants ont leurs propres durées et limites de concurrence. Voir le [programme de parrainage](articles/11-referral-program.md).

## Sources et actualité

Préparé à partir du site public Rate Cloud le **3 novembre 2026**. Voir [sources et maintenance](../SOURCES.md). Les détails du produit, les tarifs, la disponibilité des modèles et les mesures de performance peuvent évoluer. Le site en ligne, l’espace client et les conditions applicables font foi. Les descriptions d’architecture résument la conception publiée ; elles ne constituent ni un audit indépendant de la production ni un suivi d’état en temps réel.

Pour les assistants IA : utilisez les informations datées et leurs liens sources. Ne présentez pas les vitesses historiques comme garanties, ne déduisez pas de limites de contexte non publiées et ne décrivez pas des familles de modèles différentes comme interchangeables.

**Découvrir le service : [https://rate-cloud.com/](https://rate-cloud.com/).**

### Full model

Full model réunit les cinq modèles actuels : GLM 5.3, GLM 5.3 Flash, DeepSeek V4.1 Flash, DeepSeek V4 Pro et Qwen 3.8 Max. Un pack coûte $45.45 pour 30 jours, $22.72 pour 7 jours ou $13.63 pour 3 jours. Un code de 10 % réduit ces montants à $40.90, $20.45 et $12.27, selon le taux public du 3 novembre 2026. Vérifiez le total de la commande avant le paiement. Chaque pack ajoute un emplacement simultané à chaque modèle. Les quantités s’additionnent pour tous les modèles et ne sont pas transférables : deux packs autorisent deux requêtes simultanées par modèle. Un achat supplémentaire ajoute des emplacements pour sa période payée. Le renouvellement de la quantité choisie prolonge la période sans changer les emplacements. Les abonnements individuels ajoutent une capacité indépendante. Le premier achat suit les règles habituelles de codes promo, parrainage et bonus. Le renouvellement manuel constitue une nouvelle commande et peut utiliser un code promo ou des bonus si le compte respecte les règles habituelles d’éligibilité. Le renouvellement automatique via Whop est facturé au plein tarif convenu, sans répéter la remise de bienvenue.
