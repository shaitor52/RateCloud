# Connecter OpenCode à Rate Cloud

[English](../../guides/opencode.md) · [Deutsch](../../de/guides/opencode.md) · Français · [Русский](../../ru/guides/opencode.md)
Ce guide configure OpenCode pour utiliser l’API Rate Cloud compatible avec OpenAI. Il présente le format documenté d’OpenCode v1. La page de connexion Rate Cloud distingue les formats v1 et v2 ; pour v2, utilisez l’exemple v2 actuel de l’espace client au lieu d’y coller une configuration v1.

Références officielles : [guide de connexion Rate Cloud](https://rate-cloud.com/docs) et [configuration OpenCode](https://opencode.ai/docs/config/).

## Avant de commencer

1. Connectez-vous à Rate Cloud et créez une clé dans **Paramètres → Clés API**. Copiez-la immédiatement : le secret complet n’est affiché qu’à la création.
2. Vérifiez que la clé autorise le modèle voulu et que l’essai ou l’abonnement correspondant est actif. La liste des modèles ne prouve pas le droit d’exécution.
3. OpenCode v1 utilise le préfixe `ratecloud/` pour sélectionner le fournisseur configuré. Ce préfixe est propre au client. L’API HTTP directe utilise l’ID sans préfixe.

| Modèle | ID API direct | Sélection OpenCode v1 |
| --- | --- | --- |
| GLM 5.3 | `glm-5.3` | `ratecloud/glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` | `ratecloud/glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` | `ratecloud/deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` | `ratecloud/deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` | `ratecloud/qwen-3.8-max` |

## Définir la clé dans le shell

Les exemples lisent la clé sans l’afficher. Choisissez Bash ou zsh, le shell par défaut de macOS. Saisissez le secret à l’invite. Les programmes lancés depuis ce shell héritent de la variable. Fermez le terminal ou supprimez-la avec `unset`.

```sh
# Bash
read -r -s -p 'Rate Cloud API key: ' RATE_CLOUD_API_KEY
printf '\n'
export RATE_CLOUD_API_KEY
```

```sh
# zsh
read -r -s 'RATE_CLOUD_API_KEY?Rate Cloud API key: '
printf '\n'
export RATE_CLOUD_API_KEY
```

Ne collez pas la clé dans un fichier partagé, un dépôt source, une capture d’écran ou un message au support. Sous Windows, définissez `RATE_CLOUD_API_KEY` dans l’environnement qui lance OpenCode avec votre méthode locale habituelle de gestion sécurisée des secrets.

## Configurer OpenCode v1

Ouvrez `~/.config/opencode/opencode.json` sur macOS/Linux. Conservez les autres fournisseurs et paramètres. Fusionnez l’entrée `provider` ci-dessous avec l’objet existant, puis définissez ou fusionnez `model` au niveau supérieur. Pour un nouveau fichier, voici un exemple minimal complet pour GLM 5.3 :

```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "ratecloud/glm-5.3",
  "provider": {
    "ratecloud": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Rate Cloud",
      "options": {
        "baseURL": "https://llm.rate-cloud.com/v1",
        "apiKey": "{env:RATE_CLOUD_API_KEY}"
      },
      "models": {
        "glm-5.3": { "name": "GLM 5.3" },
        "glm-5.3-flash": { "name": "GLM 5.3 Flash" },
        "deepseek-v4.1-flash": { "name": "DeepSeek V4.1 Flash" },
        "deepseek-v4-pro": { "name": "DeepSeek V4 Pro" },
        "qwen-3.8-max": { "name": "Qwen 3.8 Max" }
      }
    }
  }
}
```

Au chargement, OpenCode remplace `{env:RATE_CLOUD_API_KEY}` par la variable d’environnement. Si elle n’est pas définie, la valeur est vide. Exportez-la avant de lancer OpenCode. La configuration ne contient que la référence à la variable, pas le secret.

Sous Windows, le chemin utilisateur documenté est `%USERPROFILE%\.config\opencode\opencode.json`. OpenCode v1 et v2 utilisent des structures différentes. Pour v2, prenez l’exemple manuel correspondant dans l’espace client Rate Cloud.

## Choisir un modèle et vérifier la connexion

Redémarrez OpenCode après la modification, ouvrez le sélecteur (`/models` dans le TUI) et choisissez un modèle Rate Cloud. Commencez par une requête courte sans données confidentielles. Utilisez l’identifiant exact de la colonne OpenCode v1.

## Dépannage

- **Rate Cloud n’apparaît pas :** vérifiez le chemin du fichier, la validité du JSON et la position de `provider.ratecloud` et `model` au niveau supérieur.
- **Requête non autorisée ou refusée :** exportez `RATE_CLOUD_API_KEY` dans le shell qui lance OpenCode. Vérifiez expiration, restrictions IP, permissions du modèle et essai ou abonnement actif.
- **La clé semble vide :** une variable absente devient une valeur vide. Définissez-la avant le lancement et redémarrez le client.
- **Modèle refusé :** utilisez l’ID exact en minuscules, ponctuation comprise. La présence au catalogue ne prouve pas l’accès.
- **Vous utilisez OpenCode v2 :** employez son format `providers` disponible dans l’espace client, pas l’exemple v1 `provider`.

Pour le support, indiquez la version du client, le système, l’ID du modèle, l’heure et le message d’erreur, après suppression des clés API, en-têtes d’autorisation et contenus privés.
