# Connect Hermes Agent to Rate Cloud

Hermes Agent supports OpenAI-compatible custom endpoints. This guide uses its documented custom provider configuration with Rate Cloud's OpenAI-compatible `/v1` Chat Completions endpoint.

**Documentation checked:** November 3, 2026. The examples follow the current published Hermes and Rate Cloud docs and have not been live-tested against an installed Hermes Agent or an account. Hermes docs are rolling documentation; no minimum Hermes version for this setup was stated in the pages checked. Its provider configuration has changed over time, so follow the current field names below rather than older snippets.

Official references: [Rate Cloud connection guide](https://rate-cloud.com/docs), [Hermes Agent providers guide](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/integrations/providers.md), [Hermes environment variables](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/reference/environment-variables.md), and [Hermes configuration files](https://hermes-agent.nousresearch.com/docs).

## Prepare access

Create a Rate Cloud API key in the dashboard, allow the model you plan to use, and confirm the account has active trial or subscription access. The full key is shown only at creation. Keep it out of source code and support messages.

Rate Cloud's generic compatible endpoint is:

```text
https://llm.rate-cloud.com/v1
```

The model ID is the bare direct API identifier. Hermes does not require the `ratecloud/` prefix used by some other clients.

| Model | Direct API ID |
| --- | --- |
| GLM 5.3 | `glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` |

## Store the secret in Hermes' local environment file

The current Hermes docs place user-managed secrets in `~/.hermes/.env`. Add this line locally, replacing the placeholder with your key:

```dotenv
RATE_CLOUD_API_KEY=<your-key>
```

On Windows, use `%USERPROFILE%\.hermes\.env`. Do not commit this file or paste a real key into a shared example. Hermes also supports a process environment variable; the `key_env` setting below names it.

## Configure one custom endpoint

Edit `~/.hermes/config.yaml` on macOS/Linux or `%USERPROFILE%\.hermes\config.yaml` on Windows. Merge these fields into the existing `model` section rather than replacing unrelated settings:

```yaml
model:
  default: glm-5.3
  provider: custom
  base_url: https://llm.rate-cloud.com/v1
  key_env: RATE_CLOUD_API_KEY
```

This uses Hermes' documented custom endpoint keys: `provider: custom`, `base_url`, and `key_env`. The endpoint speaks Chat Completions; do not change it to an Anthropic Messages or Responses transport. Do not add a context limit unless you have a verified value for the service and model.

To select another Rate Cloud model, change `model.default` to one of the other exact IDs in the table. Keep `provider: custom` and the Rate Cloud base URL.

## Optional interactive setup

Hermes documents `hermes model` as its custom endpoint setup wizard. The wizard asks for the base URL, API key, and model name and persists its choice. If using it, enter `https://llm.rate-cloud.com/v1` and a bare ID from the table. Prefer the environment-file/manual configuration above when you want to avoid saving the literal key in `config.yaml`.

## Troubleshooting

- **Missing credential:** confirm that `RATE_CLOUD_API_KEY` is defined in `~/.hermes/.env` or the process environment and that `key_env` has the same spelling.
- **Connection error:** use the base URL ending in `/v1`, not `/v1/chat/completions`; the client appends its API route.
- **Unknown model or access denied:** use the exact direct ID. Check model permissions on the key and active trial or subscription access in Rate Cloud.
- **Tools are returned as text:** OpenAI-compatible transport does not guarantee that every model and endpoint supports tool calls in the form the agent expects. Check the model's actual capability before relying on tool use.
- **Context limit looks wrong:** Hermes can infer metadata from `/v1/models`, but that listing is not guaranteed to provide every detail. Do not copy an unverified context length into the config.
- **You found an older example:** older docs may show `api_key` or another custom-provider shape. Use the current Hermes provider guide and confirm config fields for your installed release.

No API request or installation was run while preparing this guide.

Russian version: [Подключение Hermes Agent к Rate Cloud](../ru/guides/hermes-agent.md). Back to [all English guides](README.md).
