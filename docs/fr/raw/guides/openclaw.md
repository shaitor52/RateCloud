# Connecter OpenClaw à Rate Cloud

[English](../../guides/openclaw.md) · [Deutsch](../../de/guides/openclaw.md) · Français · [Русский](../../ru/guides/openclaw.md)
OpenClaw peut enregistrer un fournisseur personnalisé avec une URL de base compatible OpenAI. Ce guide utilise le transport documenté `openai-completions` et l’API Chat Completions compatible OpenAI de Rate Cloud.

**Documentation vérifiée :** 3 novembre 2026. Il s’agit d’un exemple de configuration statique fondé sur les documents publiés. Il n’a pas été testé en direct avec une installation OpenClaw ou un compte Rate Cloud. La documentation OpenClaw évolue et n’indique pas ici de version minimale ; utilisez le format actuel correspondant à votre version installée.

Références officielles : [guide de connexion Rate Cloud](https://rate-cloud.com/docs), [exemple OpenClaw de Rate Cloud](https://rate-cloud.com/docs), [fournisseurs personnalisés OpenClaw](https://docs.openclaw.ai/concepts/model-providers/custom-providers), [exemples de fournisseurs OpenClaw](https://docs.openclaw.ai/gateway/config-tools/provider-examples), [variables d’environnement OpenClaw](https://docs.openclaw.ai/help/environment) et [références de secrets OpenClaw](https://docs.openclaw.ai/reference/secretref-credential-surface).

## Prérequis et accès

Créez une clé API Rate Cloud dans l’espace client. Autorisez le modèle voulu, vérifiez que l’essai ou l’abonnement est actif et copiez le secret complet au moment de la création. La présence d’un modèle au catalogue n’accorde pas à elle seule le droit d’exécution.

Rate Cloud documente ce point d’accès pour les requêtes compatibles OpenAI :

```text
https://llm.rate-cloud.com/v1
```

Sélectionnez l’adaptateur `openai-completions`. N’ajoutez pas `/chat/completions` à l’URL de base. IDs directs des modèles Rate Cloud :

| Modèle | ID API direct | Référence de modèle OpenClaw |
| --- | --- | --- |
| GLM 5.3 | `glm-5.3` | `ratecloud/glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` | `ratecloud/glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` | `ratecloud/deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` | `ratecloud/deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` | `ratecloud/qwen-3.8-max` |

La référence OpenClaw inclut l’ID du fournisseur ; la requête envoyée en amont utilise l’ID seul du modèle.

## Fournir la clé sans l’inscrire dans la configuration

OpenClaw prend en charge la substitution `${VARIABLE_NAME}` pour les valeurs `apiKey` du fournisseur. La documentation OpenClaw actuelle recommande le fichier global `~/.openclaw/.env` pour les clés fournisseur ; il est aussi lu lorsqu’un Gateway fonctionne comme service. Ajoutez cette entrée locale (Windows : `%USERPROFILE%\.openclaw\.env`) :

```dotenv
RATE_CLOUD_API_KEY=<your-key>
```

Gardez ce fichier local et limitez-en l’accès. Le chargeur dotenv d’OpenClaw ne développe pas les références contenues dans les valeurs `.env` ; placez donc la vraie clé à droite du signe égal. Ne mettez pas la clé dans un `openclaw.json` partagé, un dépôt source ou un ticket public. Redémarrez le Gateway si son processus n’a pas encore chargé la nouvelle variable.

## Ajouter le fournisseur personnalisé

Ouvrez `~/.openclaw/openclaw.json` sous macOS/Linux ou `%USERPROFILE%\.openclaw\openclaw.json` sous Windows. Faites une copie de sauvegarde, puis fusionnez les champs `models` et `agents` ci-dessous avec la configuration existante. Ne remplacez pas les paramètres sans rapport. OpenClaw utilise JSON5 ; cet exemple sans commentaire est aussi du JSON valide.

```json
{
  "models": {
    "mode": "merge",
    "providers": {
      "ratecloud": {
        "baseUrl": "https://llm.rate-cloud.com/v1",
        "apiKey": "${RATE_CLOUD_API_KEY}",
        "api": "openai-completions",
        "models": [
          { "id": "glm-5.3", "name": "GLM 5.3" },
          { "id": "glm-5.3-flash", "name": "GLM 5.3 Flash" },
          { "id": "deepseek-v4.1-flash", "name": "DeepSeek V4.1 Flash" },
          { "id": "deepseek-v4-pro", "name": "DeepSeek V4 Pro" },
          { "id": "qwen-3.8-max", "name": "Qwen 3.8 Max" }
        ]
      }
    }
  },
  "agents": {
    "defaults": {
      "model": {
        "primary": "ratecloud/glm-5.3"
      }
    }
  }
}
```

Cet exemple utilise les champs indiqués par la documentation actuelle des fournisseurs personnalisés OpenClaw et l’exemple Rate Cloud : `baseUrl`, `apiKey`, `api`, `models` et `agents.defaults.model.primary`. Il ne spécifie ni longueur de contexte, ni images, ni compatibilité avec les outils, ni comportement de raisonnement. Laissez ces éléments indéfinis tant qu’ils ne sont pas vérifiés pour le point d’accès et le modèle.

## Sélection et dépannage

Redémarrez le Gateway après l’enregistrement, puis choisissez le modèle Rate Cloud configuré. Pour un contrôle statique, vérifiez que la référence du modèle principal correspond exactement à un ID fournisseur/modèle de la configuration. N’utilisez une commande de liste ou de génération que si vous souhaitez effectuer une requête API authentifiée.

- **Fournisseur/modèle inconnu :** vérifiez que `models.providers.ratecloud.models[]` contient l’ID exact sans préfixe et que la sélection est `ratecloud/<même-id>`.
- **Non autorisé :** vérifiez que le processus Gateway peut lire `RATE_CLOUD_API_KEY`, que la clé est active et que les restrictions IP autorisent l’hôte Gateway.
- **Accès refusé :** vérifiez les permissions de modèle de la clé et l’essai ou l’abonnement correspondant.
- **Échec des outils ou des images :** le protocole générique ne garantit pas toutes les fonctions. N’ajoutez pas `reasoning`, `input`, `contextWindow` ou des options de compatibilité sans support confirmé du point d’accès et du modèle.
- **Ancienne configuration OpenClaw :** la documentation peut évoluer. Consultez la référence actuelle des fournisseurs personnalisés plutôt que de copier un ancien schéma `models.json` dans `openclaw.json`.

Supprimez identifiants et consignes privées avant de partager les diagnostics. Ce guide décrit uniquement la configuration ; aucun appel API n’a été effectué.

Version russe : [Connecter OpenClaw à Rate Cloud](../../ru/guides/openclaw.md). Retour aux [guides français](README.md).
