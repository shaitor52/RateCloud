# Connecter Continue à Rate Cloud

[English](../../guides/continue.md) · [Deutsch](../../de/guides/continue.md) · Français · [Русский](../../ru/guides/continue.md)
Continue prend en charge les modèles compatibles OpenAI via son fournisseur OpenAI et un `apiBase` personnalisé. Ce guide utilise le format actuel `config.yaml` et conserve la clé dans le fichier local de résolution des secrets de Continue, pas dans le YAML.

**Documentation vérifiée :** 3 novembre 2026. Il s’agit d’une configuration statique fondée sur la documentation, sans requête en direct depuis Continue ou un compte Rate Cloud. Continue recommande actuellement YAML ; `config.json` est obsolète. Les pages consultées n’indiquent pas de version minimale. Si votre version refuse un champ, suivez le schéma actuel indiqué ci-dessous.

Références officielles : [guide de connexion Rate Cloud](https://rate-cloud.com/docs), [modèle compatible OpenAI dans Continue](https://docs.continue.dev/customize/model-providers/top-level/openai), [référence YAML Continue](https://docs.continue.dev/reference), [FAQ Continue sur les secrets](https://docs.continue.dev/faqs) et [emplacements de configuration Continue](https://docs.continue.dev/guides/understanding-configs).

## Vérifier l’accès et les IDs de modèles

Créez une clé API Rate Cloud, autorisez le modèle voulu et vérifiez qu’un essai ou abonnement est actif. La clé complète n’est affichée qu’à sa création. La liste des modèles de Continue ne donne pas à elle seule le droit d’accès.

L’URL de base compatible OpenAI de Rate Cloud est `https://llm.rate-cloud.com/v1`. Utilisez les IDs directs exacts ci-dessous. Continue affiche le `name` défini dans son sélecteur ; le préfixe `ratecloud/` utilisé par certains clients n’est pas nécessaire.

| Modèle | ID API direct |
| --- | --- |
| GLM 5.3 | `glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` |

## Stocker le secret pour l’extension IDE

Les extensions IDE Continue résolvent `${{ secrets.NAME }}` à partir de fichiers `.env`. La documentation précise cet ordre : `.env` du workspace, `.continue/.env` du workspace, puis `~/.continue/.env` global. Les extensions IDE n’héritent pas directement des variables d’environnement du shell.

Créez ou modifiez le fichier global `~/.continue/.env` (Windows : `%USERPROFILE%\.continue\.env`) avec cette entrée locale :

```dotenv
RATE_CLOUD_API_KEY=<your-key>
```

Gardez ce fichier hors du contrôle de version. Ne mettez pas de vraie clé dans `config.yaml` et ne partagez pas le fichier `.env`. Pour Continue CLI, l’environnement du processus peut aussi résoudre le secret selon la documentation.

## Configurer le YAML local Continue

Le fichier local Continue se trouve dans `~/.continue/config.yaml` sous macOS/Linux et `%USERPROFILE%\.continue\config.yaml` sous Windows. Utilisez le sélecteur de configuration et l’icône d’engrenage dans la barre latérale. Conservez les sections non liées aux modèles. Ajoutez une entrée pour chaque modèle souhaité ; cet exemple comprend les cinq :

```yaml
name: Rate Cloud
version: 1.0.0
schema: v1
models:
  - name: Rate Cloud - GLM 5.3
    provider: openai
    model: glm-5.3
    apiBase: https://llm.rate-cloud.com/v1
    apiKey: ${{ secrets.RATE_CLOUD_API_KEY }}
    useResponsesApi: false
    roles: [chat, edit, apply]
  - name: Rate Cloud - GLM 5.3 Flash
    provider: openai
    model: glm-5.3-flash
    apiBase: https://llm.rate-cloud.com/v1
    apiKey: ${{ secrets.RATE_CLOUD_API_KEY }}
    useResponsesApi: false
    roles: [chat, edit, apply]
  - name: Rate Cloud - DeepSeek V4.1 Flash
    provider: openai
    model: deepseek-v4.1-flash
    apiBase: https://llm.rate-cloud.com/v1
    apiKey: ${{ secrets.RATE_CLOUD_API_KEY }}
    useResponsesApi: false
    roles: [chat, edit, apply]
  - name: Rate Cloud - DeepSeek V4 Pro
    provider: openai
    model: deepseek-v4-pro
    apiBase: https://llm.rate-cloud.com/v1
    apiKey: ${{ secrets.RATE_CLOUD_API_KEY }}
    useResponsesApi: false
    roles: [chat, edit, apply]
  - name: Rate Cloud - Qwen 3.8 Max
    provider: openai
    model: qwen-3.8-max
    apiBase: https://llm.rate-cloud.com/v1
    apiKey: ${{ secrets.RATE_CLOUD_API_KEY }}
    useResponsesApi: false
    roles: [chat, edit, apply]
```

`useResponsesApi: false` sélectionne le chemin Chat Completions documenté. Les modèles sont déclarés avec les rôles chat, edit et apply. Ce guide n’active pas la capacité Agent/outils, qui dépend du support réel des appels d’outils par le modèle et l’API ; ne l’activez qu’après vérification.

Enregistrez la configuration. Le guide Continue actuel indique que les changements sont rechargés automatiquement. Sélectionnez une entrée Rate Cloud dans le sélecteur. Aucune requête modèle n’est nécessaire pour vérifier la configuration statique et l’entrée du menu.

## Dépannage

- **Clé API introuvable :** vérifiez l’orthographe `RATE_CLOUD_API_KEY` et que le fichier se trouve à un emplacement `.env` pris en charge. Pour l’extension IDE, ne comptez pas uniquement sur un `export` dans le terminal.
- **Aucun modèle Rate Cloud n’apparaît :** vérifiez le chemin YAML, la présence de `schema: v1` et la syntaxe YAML. Utilisez le sélecteur Continue pour vérifier que vous modifiez la configuration active.
- **401 ou accès refusé :** vérifiez que le secret est actif et que Rate Cloud autorise le modèle pour le compte et la clé. Son nom dans Continue ne prouve pas l’accès.
- **404 ou route API incorrecte :** gardez `apiBase` à `https://llm.rate-cloud.com/v1`, sans ajouter `/chat/completions`.
- **Échec des appels d’outils Agent :** les rôles et le support des appels d’outils sont distincts. Continue indique que `tool_use` est nécessaire au mode Agent, mais la compatibilité Rate Cloud réelle n’a pas été testée en direct ici. Ne la déclarez pas sans vérification.
- **Format différent dans votre version :** la référence Continue fait autorité pour les champs YAML pris en charge. Préférez `config.yaml` ; les configurations JSON sont indiquées comme obsolètes.

Retirez secrets et contenu privé des consignes avant de partager des journaux. Aucune installation ni requête API n’a été effectuée pour préparer ce guide.

Version russe : [Connecter Continue à Rate Cloud](../../ru/guides/continue.md). Retour aux [guides français](README.md).
