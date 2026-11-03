# Connecter Hermes Agent à Rate Cloud

[English](../../guides/hermes-agent.md) · [Deutsch](../../de/guides/hermes-agent.md) · Français · [Русский](../../ru/guides/hermes-agent.md)
Hermes Agent prend en charge les points d’accès personnalisés compatibles OpenAI. Ce guide utilise sa configuration documentée de fournisseur personnalisé avec le point d’accès Chat Completions `/v1` de Rate Cloud.

**Documentation vérifiée :** 3 novembre 2026. Les exemples suivent les documentations publiées de Hermes et Rate Cloud, sans test en direct sur une installation Hermes ou un compte. La documentation Hermes évolue ; les pages consultées n’indiquaient pas de version minimale. Sa configuration fournisseur a changé : utilisez les champs actuels ci-dessous plutôt que d’anciens exemples.

Références officielles : [guide de connexion Rate Cloud](https://rate-cloud.com/docs), [guide des fournisseurs Hermes](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/integrations/providers.md), [variables d’environnement Hermes](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/reference/environment-variables.md) et [fichiers de configuration Hermes](https://hermes-agent.nousresearch.com/docs).

## Préparer l’accès

Créez une clé API dans l’espace client Rate Cloud, autorisez le modèle voulu et vérifiez que l’essai ou l’abonnement correspondant est actif. La clé complète n’est affichée qu’à sa création. Ne la mettez ni dans le code source ni dans un message au support.

Le point d’accès générique compatible Rate Cloud est :

```text
https://llm.rate-cloud.com/v1
```

Utilisez l’identifiant API direct du modèle. Hermes ne nécessite pas le préfixe `ratecloud/` employé par certains autres clients.

| Modèle | ID API direct |
| --- | --- |
| GLM 5.3 | `glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` |

## Stocker le secret dans le fichier d’environnement local Hermes

La documentation Hermes actuelle indique `~/.hermes/.env` pour les secrets gérés par l’utilisateur. Ajoutez localement la ligne suivante en remplaçant le placeholder par votre clé :

```dotenv
RATE_CLOUD_API_KEY=<your-key>
```

Sous Windows, utilisez `%USERPROFILE%\.hermes\.env`. Ne versionnez pas ce fichier et ne partagez pas une vraie clé dans un exemple. Hermes sait aussi lire une variable d’environnement du processus ; le réglage `key_env` ci-dessous la désigne.

## Configurer un point d’accès personnalisé

Modifiez `~/.hermes/config.yaml` sur macOS/Linux ou `%USERPROFILE%\.hermes\config.yaml` sous Windows. Fusionnez ces champs dans la section `model` existante au lieu de remplacer d’autres paramètres :

```yaml
model:
  default: glm-5.3
  provider: custom
  base_url: https://llm.rate-cloud.com/v1
  key_env: RATE_CLOUD_API_KEY
```

Ce sont les champs documentés par Hermes pour un point d’accès personnalisé : `provider: custom`, `base_url` et `key_env`. Le point d’accès parle Chat Completions ; ne le configurez pas en transport Anthropic Messages ou Responses. N’ajoutez pas de limite de contexte sans valeur vérifiée pour le service et le modèle.

Pour choisir un autre modèle Rate Cloud, remplacez `model.default` par l’un des IDs exacts du tableau. Gardez `provider: custom` et l’URL Rate Cloud.

## Configuration interactive facultative

Hermes documente `hermes model` comme assistant de configuration d’un point d’accès personnalisé. Il demande l’URL de base, la clé et le modèle, puis enregistre le choix. Saisissez `https://llm.rate-cloud.com/v1` et un ID sans préfixe du tableau. Si vous ne voulez pas enregistrer la clé littérale dans `config.yaml`, privilégiez la configuration manuelle ci-dessus.

## Dépannage

- **Identifiant absent :** vérifiez que `RATE_CLOUD_API_KEY` figure dans `~/.hermes/.env` ou l’environnement du processus et que `key_env` l’orthographie pareil.
- **Erreur de connexion :** utilisez l’URL se terminant par `/v1`, pas `/v1/chat/completions` ; le client ajoute le chemin API.
- **Modèle inconnu ou accès refusé :** utilisez l’ID direct exact et vérifiez les permissions de la clé, l’essai ou l’abonnement actif.
- **Les appels d’outils apparaissent comme du texte :** le transport compatible OpenAI ne garantit pas que chaque modèle et point d’accès accepte les appels d’outils sous la forme attendue. Vérifiez la capacité réelle.
- **Limite de contexte incorrecte :** Hermes peut déduire des métadonnées de `/v1/models`, mais cette liste ne garantit pas tous les détails. Ne copiez pas une valeur de contexte non vérifiée dans la configuration.
- **Ancien exemple :** d’anciennes pages peuvent montrer `api_key` ou une autre structure. Consultez le guide fournisseur Hermes actuel et vérifiez les champs pris en charge par votre version.

Aucune requête API et aucune installation n’ont été effectuées pour préparer ce guide.

Version russe : [Connecter Hermes Agent à Rate Cloud](../../ru/guides/hermes-agent.md). Retour aux [guides français](README.md).
