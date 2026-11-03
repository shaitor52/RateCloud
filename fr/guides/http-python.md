# Accès HTTP et Python

[English](../../guides/http-python.md) · [Deutsch](../../de/guides/http-python.md) · Français · [Русский](../../ru/guides/http-python.md)
Rate Cloud fournit une API compatible avec OpenAI pour les clients acceptant une URL de base personnalisée, ainsi qu’un exemple Python fondé sur la bibliothèque standard. Ces exemples n’installent aucun paquet et n’envoient de requête que si vous les exécutez.

Référence officielle : [documentation API et connexion Rate Cloud](https://rate-cloud.com/docs).

## Points d’accès

| Usage | Méthode et URL |
| --- | --- |
| URL de base compatible OpenAI | `https://llm.rate-cloud.com/v1` |
| Liste des modèles | `GET https://llm.rate-cloud.com/v1/models` |
| Chat completions | `POST https://llm.rate-cloud.com/v1/chat/completions` |
| API Responses | `POST https://llm.rate-cloud.com/v1/responses` |

Pour les requêtes `/v1`, envoyez `Authorization: Bearer <API key>`. Utilisez exactement l’ID du modèle indiqué :

| Modèle | ID API direct |
| --- | --- |
| GLM 5.3 | `glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` |

N’ajoutez pas de préfixe fournisseur comme `ratecloud/` à l’ID HTTP direct. Les formes `ratecloud/` et `ocx-claude-ratecloud--` sont propres à certaines intégrations client.

## Définir une variable d’environnement

Sur macOS ou Linux, choisissez le bloc correspondant à votre shell. Dans les deux cas, la clé est lue sans être affichée. La variable disparaît avec `unset` ou à la fermeture du terminal.

```sh
# Bash
read -r -s -p 'Rate Cloud API key: ' RATE_CLOUD_API_KEY
printf '\n'
export RATE_CLOUD_API_KEY
```

```sh
# zsh (shell par défaut de macOS)
read -r -s 'RATE_CLOUD_API_KEY?Rate Cloud API key: '
printf '\n'
export RATE_CLOUD_API_KEY
```

Dans Windows PowerShell, définissez `$env:RATE_CLOUD_API_KEY` dans la session qui exécute le client. Ne placez pas une vraie clé dans le code source, un fichier `.env` versionné ou une demande publique.

## Vérification facultative avec curl

Cette commande envoie une requête simple au catalogue. Elle vérifie que le point d’accès répond et accepte la clé, mais ne prouve pas qu’un modèle précis est souscrit ou autorisé pour cette clé.

```sh
curl --fail-with-body 'https://llm.rate-cloud.com/v1/models' \
  -H "Authorization: Bearer $RATE_CLOUD_API_KEY"
```

## Exemple Python 3 avec la bibliothèque standard

Enregistrez ce code dans un fichier `.py` local. Il n’utilise que la bibliothèque standard (`urllib.request`), lit le secret depuis l’environnement et envoie une petite requête Chat Completions lorsque vous le lancez. Vous pouvez remplacer `MODEL` par un autre ID API direct exact.

```python
import json
import os
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

BASE_URL = "https://llm.rate-cloud.com/v1"
MODEL = "glm-5.3"
API_KEY = os.environ.get("RATE_CLOUD_API_KEY")

if not API_KEY:
    sys.exit("Set RATE_CLOUD_API_KEY in the environment before running this script.")

payload = {
    "model": MODEL,
    "messages": [
        {"role": "user", "content": "Reply with a short greeting."}
    ],
}
request = Request(
    f"{BASE_URL}/chat/completions",
    data=json.dumps(payload).encode("utf-8"),
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    },
    method="POST",
)

try:
    with urlopen(request, timeout=60) as response:
        result = json.load(response)
    print(result["choices"][0]["message"]["content"])
except HTTPError as error:
    # Avoid printing request headers or the API key in diagnostics.
    print(f"HTTP error: {error.code} {error.reason}", file=sys.stderr)
    sys.exit(1)
except URLError as error:
    print(f"Connection error: {error.reason}", file=sys.stderr)
    sys.exit(1)
except (KeyError, IndexError, json.JSONDecodeError) as error:
    print(f"Unexpected response format: {error}", file=sys.stderr)
    sys.exit(1)
```

Lancez le script depuis le shell où `RATE_CLOUD_API_KEY` est défini. N’écrivez pas la réponse complète dans des journaux partagés si les requêtes ou réponses peuvent contenir des données privées.

## Dépannage

- **401 ou erreur d’authentification :** vérifiez que la variable est transmise au processus, que la clé est active et que l’en-tête comporte `Bearer`.
- **403 ou accès refusé :** vérifiez l’essai ou l’abonnement au modèle, les permissions de la clé, les restrictions IP et la compatibilité requise par le client.
- **404 ou modèle introuvable :** vérifiez le chemin et l’orthographe exacte. Ces exemples utilisent `/v1`, pas les points d’accès Codex ou Claude Code.
- **Modèle listé mais génération refusée :** le catalogue ne prouve pas l’autorisation du compte ou de la clé. Vérifiez l’abonnement et l’accès de la clé dans l’espace client.
- **Délai dépassé ou réponse incomplète :** vérifiez l’état de la requête avant de réessayer. Un délai dépassé ne prouve pas que l’opération est terminée. Ne relancez pas aveuglément des requêtes déclenchant des effets secondaires dans votre application.

Pour le support, indiquez l’heure, l’ID du modèle, le point d’accès, le statut HTTP et l’identifiant de requête s’il existe. Supprimez les clés API, en-têtes d’autorisation et contenus privés des requêtes et réponses.
