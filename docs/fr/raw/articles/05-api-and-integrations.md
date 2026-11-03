# Connecter des outils et applications à Rate Cloud

[English](../../articles/05-api-and-integrations.md) · [Deutsch](../../de/articles/05-api-and-integrations.md) · Français · [Русский](../../ru/articles/05-api-and-integrations.md)

Rate Cloud propose une API HTTP compatible avec OpenAI et des points d’accès de compatibilité dédiés à certains clients de programmation. L’espace client fournit des consignes adaptées à chaque application. Suivez celles correspondant à votre version du client et à votre système.

## Points d’accès publiés

| Usage | Adresse |
| --- | --- |
| URL de base compatible OpenAI | `https://llm.rate-cloud.com/v1` |
| Catalogue des modèles | `GET https://llm.rate-cloud.com/v1/models` |
| Chat completions | `POST https://llm.rate-cloud.com/v1/chat/completions` |
| Responses | `POST https://llm.rate-cloud.com/v1/responses` |
| Base de compatibilité Codex | `https://llm.rate-cloud.com/codex/v1` |
| Base de compatibilité Claude Code | `https://llm.rate-cloud.com/claude` |

Les requêtes directes à `/v1` utilisent une clé API Bearer. Reprenez un ID de modèle exact du [catalogue](02-models.md), par exemple `glm-5.3`. N’ajoutez pas le préfixe propre au client `ratecloud/` à l’identifiant du modèle HTTP direct.

## De l’inscription à la première requête

Inscrivez-vous ou connectez-vous à [Rate Cloud](https://rate-cloud.com/). Effectuez les vérifications requises pour l’essai ou achetez l’accès au modèle nécessaire. Dans les paramètres de clés API, créez une clé nommée, choisissez les modèles autorisés, les adresses IP permises et l’expiration, puis copiez immédiatement le secret affiché.

L’abonnement autorise l’utilisation d’un modèle ; les permissions de la clé déterminent si cette clé peut utiliser ce droit. Une clé limitée à certains modèles n’obtient pas automatiquement accès à un modèle acheté par la suite. La présence d’un modèle dans le catalogue ne prouve pas que l’exécution est autorisée.

Pour Codex ou Claude Code, le guide public demande d’activer l’option de compatibilité « Codex / Claude Code » pour la clé.

## Requête HTTP minimale

Définissez localement `RATE_CLOUD_API_KEY` avec votre méthode habituelle de gestion des secrets, puis exécutez :

```sh
curl --fail-with-body https://llm.rate-cloud.com/v1/chat/completions \
  -H "Authorization: Bearer $RATE_CLOUD_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"model":"glm-5.3","messages":[{"role":"user","content":"Reply with a short greeting."}]}'
```

La variable représente votre secret local. Ne placez jamais une vraie clé dans un dépôt public, une capture d’écran, un message au support ou une configuration versionnée. Vérifiez les identifiants dans le catalogue, puis envoyez une petite requête avec un modèle accessible au compte et à la clé.

## Clients de programmation et autres applications

Le guide public couvre OpenCode, Codex, Claude Code, OpenClaw, Continue, Hermes et d’autres clients compatibles. L’espace client propose des commandes automatiques et des exemples manuels pour les systèmes pris en charge.

La configuration dépend de la version du client. Le guide officiel distingue par exemple les formats OpenCode v1 et v2. Préférez les consignes actuelles de l’espace client aux anciens blocs trouvés dans des articles tiers.

Le client apporte son interface, ses outils locaux, ses connexions MCP, ses instructions de projet et la gestion des conversations. Les fonctions disponibles dépendent du modèle choisi et de l’intégration. Un point d’accès compatible ne garantit pas la disponibilité de toutes les fonctions des API propriétaires.

## Dépannage sans exposer les secrets

Vérifiez l’URL de base et l’identifiant exact du modèle, l’abonnement ou l’essai actif, les permissions de modèle de la clé, son expiration, les restrictions IP et l’option de compatibilité requise. Tenez compte du pool de créneaux partagé. Pour contacter le support, indiquez l’heure et l’identifiant de requête, sans les en-têtes d’autorisation ni le contenu privé des consignes.

Source : [documentation API et connexion Rate Cloud](https://rate-cloud.com/docs), consultée le 3 novembre 2026. [Retour à la présentation](../README.md).
