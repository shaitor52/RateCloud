# Connecter DeepSeek Harness à Rate Cloud

[English](../../guides/deepseek-harness.md) · [Deutsch](../../de/guides/deepseek-harness.md) · Français · [Русский](../../ru/guides/deepseek-harness.md)
DeepSeek Harness propose un formulaire **Custom model API** pour les passerelles compatibles OpenAI. Rate Cloud documente un point d’accès Chat Completions compatible OpenAI. La configuration ci-dessous utilise ce protocole et des IDs de modèles saisis manuellement.

**Documentation vérifiée :** 3 novembre 2026. DeepSeek Harness se présente comme une préversion développeur susceptible de changements incompatibles. Ce guide suit les pages publiques de son interface Web et la documentation Rate Cloud ; il s’agit d’une correspondance statique non testée en direct. Aucune installation ni requête API n’a été exécutée.

Références officielles : [guide de connexion Rate Cloud](https://rate-cloud.com/docs), [dépôt DeepSeek Harness et avis de préversion](https://github.com/deepseek-ai/deepseek-harness), [configuration des modèles Harness](https://deepseek-harness.github.io/deepseek-harness/en/guide/providers), [démarrage rapide Harness](https://deepseek-harness.github.io/deepseek-harness/en/guide/quickstart) et [catalogue de configuration des extensions](https://deepseek-harness.github.io/deepseek-harness/en/reference/config-catalog).

## Périmètre de compatibilité

Rate Cloud documente ces points d’accès et identifiants directs :

| Usage | Valeur |
| --- | --- |
| URL de base | `https://llm.rate-cloud.com/v1` |
| Route Chat Completions | `POST /v1/chat/completions` |
| GLM 5.3 | `glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` |

Harness documente les fournisseurs personnalisés avec URL de base, protocole, identifiant secret et liste de modèles. Sélectionnez **OpenAI Chat Completions**. Pour cet exemple, ne choisissez ni Responses ni Anthropic Messages. La documentation publiée n’établit pas l’existence d’un fournisseur Rate Cloud intégré ni une compatibilité testée en direct.

## Préparer le compte et les droits de la clé

Dans l’espace client Rate Cloud, créez une clé API, autorisez le modèle choisi et vérifiez que l’essai ou l’abonnement correspondant est actif. La clé complète n’est affichée qu’une fois, à la création. Un modèle visible au catalogue ne prouve pas que la clé peut l’appeler.

## Ajouter une API de modèle personnalisée dans l’interface Web

Cette procédure configure uniquement l’interface. Elle ne lance pas d’installateur ni de requête de modèle.

1. Démarrez l’interface Web Harness en suivant le README officiel. Ce guide ne reprend pas les commandes d’installation.
2. Ouvrez **Settings → Models**, puis **Add model provider**.
3. Choisissez le formulaire **Custom model API**.
4. Définissez un ID fournisseur en minuscules, par exemple `ratecloud`. Harness indique que cet ID est permanent, car les sessions, valeurs par défaut, requêtes et références d’identifiants l’utilisent.
5. Définissez le nom affiché sur `Rate Cloud` et l’URL de base sur `https://llm.rate-cloud.com/v1`.
6. Choisissez **OpenAI Chat Completions** comme protocole API.
7. Entrez la clé Rate Cloud dans le champ d’identifiants. Harness précise que les clés enregistrées sont inscriptibles mais non lisibles depuis l’interface ; elles sont stockées dans `$DSH_HOME/.credentials.yaml` et les réglages conservent une référence. Ne mettez pas la clé dans un dépôt ou une demande publique.
8. Ajoutez manuellement un modèle avec un ID exact du tableau et un nom lisible. Laissez vides la fenêtre de contexte, la sortie maximale, l’entrée image et les options de raisonnement, sauf valeur ou capacité vérifiée.
9. Enregistrez le fournisseur puis choisissez le modèle dans le sélecteur pour en faire le défaut des nouvelles sessions.

Vous pouvez ajouter d’autres modèles au même fournisseur avec leurs IDs directs exacts. N’ajoutez pas de préfixe client comme `ratecloud/` dans le champ d’ID du modèle.

## Découverte facultative des modèles

Harness peut récupérer une liste de modèles avec l’URL, le protocole et les identifiants du fournisseur. Cela envoie une requête HTTP authentifiée au point d’accès. Cette découverte est facultative et son fonctionnement n’est pas garanti pour tous les formats de liste. Pour éviter tout appel, saisissez les IDs manuellement comme ci-dessus. Aucune requête de découverte n’a été envoyée pour préparer ce guide.

## Dépannage

- **`MISSING_CREDENTIAL` :** vérifiez qu’une clé a été enregistrée pour le fournisseur ou que sa référence est disponible.
- **`UNKNOWN_MODEL` :** ajoutez l’ID au fournisseur personnalisé, puis sélectionnez cette entrée configurée. Respectez casse et ponctuation exactes.
- **HTTP 401 :** vérifiez clé, expiration et autorisation du modèle dans Rate Cloud. La liste de modèles n’est pas un contrôle d’accès.
- **HTTP 404 ou route incorrecte :** utilisez `https://llm.rate-cloud.com/v1` et OpenAI Chat Completions. N’ajoutez pas `/chat/completions` à l’URL de base.
- **Aucun résultat de découverte :** le format de liste n’est peut-être pas reconnu. Ajoutez le modèle manuellement ; un échec de découverte ne prouve pas que l’inférence est indisponible.
- **Échec des outils, images ou du raisonnement :** déclarer une capacité dans Harness ne crée ni ne teste le support API. Ne configurez que des capacités documentées et confirmées pour le modèle choisi.
- **Chemins différents dans votre version :** Harness étant une préversion, il peut évoluer rapidement. Consultez la page de configuration actuelle et le catalogue généré pour votre version.

Aucune requête en direct n’a été faite ; l’authentification et les fonctionnalités dans Harness ne sont donc pas vérifiées.

Version russe : [Connecter DeepSeek Harness à Rate Cloud](../../ru/guides/deepseek-harness.md). Retour aux [guides français](README.md).
