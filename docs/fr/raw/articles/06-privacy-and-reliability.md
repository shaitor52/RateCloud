# Confidentialité, traitement des données et disponibilité

[English](../../articles/06-privacy-and-reliability.md) · [Deutsch](../../de/articles/06-privacy-and-reliability.md) · Français · [Русский](../../ru/articles/06-privacy-and-reliability.md)

L’architecture publique de Rate Cloud distingue le contenu des requêtes, l’état temporaire de calcul, les métadonnées opérationnelles et les données de compte ou de paiement. Ces catégories ont des finalités et des durées de conservation différentes. Cet article résume la politique et la conception publiées ; il ne constitue pas un audit de sécurité indépendant.

## Contenu des requêtes et tampons temporaires

Le service indique ne pas créer d’historique permanent des textes de requête et de réponse et ne pas utiliser les données des utilisateurs pour entraîner les modèles. Le contenu est traité temporairement en mémoire. La règle publiée pour les tampons applicatifs gérés prévoit leur suppression sous 5 secondes après transmission réussie, ou sous 30 secondes après erreur définitive, annulation ou rupture de connexion.

Le cache KV de calcul isolé a ses propres délais : au plus 5 minutes sans réutilisation et 15 minutes d’âge absolu. Au terme, un bloc n’est plus utilisé pour de nouveaux accès ; une opération qui l’utilise déjà peut se terminer dans son délai. La mémoire est effacée après libération de la dernière référence.

Selon la documentation, ce cache n’est pas écrit sur disque et n’est pas inclus dans les instantanés. La compatibilité tient compte du compte, du modèle, de la révision des poids, de la quantification, du tokenizer, du modèle de conversation et des instructions système. L’index est protégé par HMAC et un utilisateur ne peut pas sélectionner le cache d’un autre compte. Une politique de projet peut désactiver le cache entre requêtes.

L’historique local du client est distinct. Un éditeur, un agent, un bot ou une application peut conserver ses propres conversations et fichiers selon ses paramètres.

## Métadonnées opérationnelles

L’architecture publique mentionne des métadonnées telles que les identifiants, le modèle et le profil, les horodatages, la durée, l’usage, l’état des créneaux et les codes d’erreur. Les enregistrements détaillés sont supprimés après 30 jours. Ils excluent les consignes, réponses, arguments d’outils, fichiers et jetons d’autorisation. Les données de compte, de paiement et les renseignements volontairement transmis au support ont des finalités et durées distinctes.

« Pas d’historique permanent des consignes » ne signifie pas « aucune donnée de compte ou d’exploitation ». Consultez la politique de confidentialité et les conditions en vigueur.

## Transport et limites de l’infrastructure

L’architecture décrit TLS pour le transport externe, des contrôles d’identité et mTLS entre services, ainsi que des droits d’accès selon les besoins du service. Les clés, comptes, projets et espaces de cache sont séparés. Selon les règles publiées, les secrets API et corps des requêtes ne doivent pas figurer dans les journaux ou sauvegardes.

Le transport protégé et le calcul protégé par matériel sont deux garanties différentes. Le site ne promet pas un calcul confidentiel sur chaque accélérateur. Un nœud dont la gestion de confiance est perdue est exclu et ses autorisations révoquées ; son retour nécessite vérification et nettoyage.

## Disponibilité et opérations interrompues

La disponibilité permanente de chaque modèle, 24 h/24 et 7 j/7, n’est pas garantie. Avant le début de la réponse, une reprise peut réessayer sur un réplica compatible dans le délai initial. Cela peut accroître la latence. Une fois le flux commencé, une interruption doit rester visible comme opération incomplète.

La règle de compensation publiée s’applique à une indisponibilité complète et continue du système durant plus de quatre heures avec des réponses HTTP 503. Elle prolonge de 12 heures un abonnement de 3 jours, d’un jour un abonnement de 7 jours et de 3 jours un abonnement de 30 jours. Les erreurs d’un modèle particulier, les réponses lentes, les limites de concurrence et les autres codes d’erreur ne relèvent pas de cette règle spécifique. Les conditions applicables et les droits impératifs des utilisateurs restent déterminants.

Pour signaler un incident, indiquez l’heure et les identifiants des opérations. N’envoyez ni secrets API ni contenu confidentiel des requêtes.

Source : [traitement des données, sécurité et disponibilité de Rate Cloud](https://rate-cloud.com/how-it-works). Consultez les conditions et la politique de confidentialité actuelles sur le [site officiel](https://rate-cloud.com/). État au 3 novembre 2026. [Retour à la présentation](../README.md).
