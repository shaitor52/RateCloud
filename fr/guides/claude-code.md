# Connecter Claude Code à Rate Cloud

[English](../../guides/claude-code.md) · [Deutsch](../../de/guides/claude-code.md) · Français · [Русский](../../ru/guides/claude-code.md)
Claude Code utilise le point d’accès de compatibilité dédié de Rate Cloud et des noms de modèles propres au client. Il s’agit d’un accès API à GLM, DeepSeek ou Qwen via Rate Cloud, pas de modèles Anthropic.

Références officielles : [guide de connexion Rate Cloud](https://rate-cloud.com/docs) et [documentation Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview).

## Créer et préparer une clé API

Dans l’espace client Rate Cloud, créez une clé, copiez son secret complet au moment de la création et activez **Compatibilité Codex / Claude Code**. Autorisez le modèle voulu et vérifiez qu’un essai ou abonnement correspondant est actif. La liste des modèles ne confirme pas le droit d’exécution.

## Noms de modèles pour Claude Code

Claude Code utilise le préfixe `ocx-claude-ratecloud--` suivi de l’ID exact du modèle. L’API HTTP directe utilise l’ID seul.

| Modèle | ID API direct | Valeur Claude Code `ANTHROPIC_MODEL` |
| --- | --- | --- |
| GLM 5.3 | `glm-5.3` | `ocx-claude-ratecloud--glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` | `ocx-claude-ratecloud--glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` | `ocx-claude-ratecloud--deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` | `ocx-claude-ratecloud--deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` | `ocx-claude-ratecloud--qwen-3.8-max` |

## Lancer sous macOS ou Linux

Dans Bash ou zsh, lisez d’abord la clé sans l’afficher, puis définissez les trois variables et lancez Claude Code dans le même terminal. Elles restent dans l’environnement de ce shell jusqu’à sa fermeture ou leur suppression.

```sh
# Bash
read -r -s -p 'Rate Cloud API key: ' RATE_CLOUD_API_KEY
printf '\n'
```

```sh
# zsh
read -r -s 'RATE_CLOUD_API_KEY?Rate Cloud API key: '
printf '\n'
```

Dans ce même terminal :

```sh
export ANTHROPIC_BASE_URL='https://llm.rate-cloud.com/claude'
export ANTHROPIC_AUTH_TOKEN="$RATE_CLOUD_API_KEY"
export ANTHROPIC_MODEL='ocx-claude-ratecloud--glm-5.3'
claude
```

Remplacez si nécessaire la valeur du modèle par un autre nom complet du tableau. Après usage, fermez le terminal ou exécutez `unset RATE_CLOUD_API_KEY ANTHROPIC_AUTH_TOKEN ANTHROPIC_BASE_URL ANTHROPIC_MODEL`.

## Lancer avec Windows PowerShell

Définissez les variables dans la fenêtre PowerShell qui lance Claude Code. `Read-Host` affiche les caractères saisis. Pour une saisie masquée, utilisez votre gestionnaire local de secrets approuvé.

```powershell
$env:RATE_CLOUD_API_KEY = Read-Host 'Rate Cloud API key'
$env:ANTHROPIC_BASE_URL = 'https://llm.rate-cloud.com/claude'
$env:ANTHROPIC_AUTH_TOKEN = $env:RATE_CLOUD_API_KEY
$env:ANTHROPIC_MODEL = 'ocx-claude-ratecloud--glm-5.3'
claude
```

Après avoir quitté Claude Code, supprimez les variables de la session PowerShell :

```powershell
Remove-Item Env:RATE_CLOUD_API_KEY, Env:ANTHROPIC_BASE_URL, Env:ANTHROPIC_AUTH_TOKEN, Env:ANTHROPIC_MODEL
```

## Dépannage

- **Erreur d’authentification ou de compatibilité :** activez l’option **Compatibilité Codex / Claude Code** de la clé.
- **Modèle inconnu :** utilisez le nom complet commençant par `ocx-claude-ratecloud--`, pas l’ID HTTP seul.
- **Accès refusé :** vérifiez l’essai ou l’abonnement, les modèles permis par la clé, son expiration et les restrictions IP dans l’espace client.
- **Fonctionne dans le terminal mais pas via le lanceur d’application :** les programmes lancés depuis un terminal héritent de ses variables. Lancez Claude Code depuis le shell configuré ou suivez le guide actuel de l’espace client pour une configuration persistante.
- **Échec de connexion :** l’URL doit être exactement `https://llm.rate-cloud.com/claude`, et non le point d’accès général `/v1`.

Pour le support, indiquez la version du client, le système, le modèle, l’heure et le texte de l’erreur. Supprimez les secrets API, en-têtes d’autorisation et contenus privés.
