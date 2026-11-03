# Connect Continue to Rate Cloud

Continue supports OpenAI-compatible models through its OpenAI provider and a custom `apiBase`. This guide uses Continue's current `config.yaml` format and stores the key in Continue's local secret-resolution file rather than in the YAML.

**Documentation checked:** November 3, 2026. This is a static docs-based configuration, not a live request from Continue or a Rate Cloud account. Continue's current docs prefer YAML; `config.json` is deprecated. The pages checked do not state a minimum Continue client version for this configuration. If your version does not accept a field, follow the current schema linked below.

Official references: [Rate Cloud connection guide](https://rate-cloud.com/docs), [Continue OpenAI-compatible model setup](https://docs.continue.dev/customize/model-providers/top-level/openai), [Continue YAML reference](https://docs.continue.dev/reference), [Continue secret FAQ](https://docs.continue.dev/faqs), and [Continue configuration locations](https://docs.continue.dev/guides/understanding-configs).

## Check access and model IDs

Create a Rate Cloud API key, allow the model you need, and make sure your account has an active trial or subscription for it. The key is displayed in full at creation time. Continue's model list does not grant access by itself.

Rate Cloud's OpenAI-compatible base URL is `https://llm.rate-cloud.com/v1`. Use the exact direct API IDs below. Continue displays the `name` you set in its picker; it does not require the `ratecloud/` prefix used by some other clients.

| Model | Direct API ID |
| --- | --- |
| GLM 5.3 | `glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` |

## Store the secret for the IDE extension

Continue's IDE extensions resolve `${{ secrets.NAME }}` from `.env` files. Its docs specify this lookup order: workspace `.env`, workspace `.continue/.env`, then global `~/.continue/.env`. The docs warn that IDE extensions do not inherit shell environment variables directly.

Create or update the global file `~/.continue/.env` (Windows: `%USERPROFILE%\.continue\.env`) with this local entry:

```dotenv
RATE_CLOUD_API_KEY=<your-key>
```

Keep this local file out of version control. Do not put a real key in `config.yaml` or share the `.env` file. For Continue CLI, the process environment can also resolve the secret, according to Continue's docs.

## Configure Continue's local YAML

Continue stores its local config at `~/.continue/config.yaml` on macOS/Linux and `%USERPROFILE%\.continue\config.yaml` on Windows. Use the config selector and gear icon in the Continue sidebar to open it. Preserve existing non-model sections. Add a model entry for each model you want to expose; this example includes all five:

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

`useResponsesApi: false` selects the documented Chat Completions path. The models are listed with chat, edit, and apply roles. This guide does not assign an Agent/tool-use capability because that depends on actual model/API tool-call support; enable that capability only after verifying it for the model you use.

Save the config. Continue's current configuration guide says it automatically reloads changes. Select a Rate Cloud entry from the model picker. No model request is necessary just to check the static config and picker entry.

## Troubleshooting

- **API key resolves as missing:** check the exact `RATE_CLOUD_API_KEY` spelling and that the key is in a supported `.env` location. For IDE extensions, do not rely only on an `export` in a terminal.
- **No Rate Cloud model appears:** confirm the YAML is at the local config path, `schema: v1` is present, and the saved file remains valid YAML. Use the Continue config selector to confirm you are editing the active config.
- **401 or access denied:** check that the secret is active and that Rate Cloud allows the selected model for both the key and account. A model name appearing in Continue does not prove access.
- **404 or wrong API route:** keep `apiBase` at `https://llm.rate-cloud.com/v1`; do not append `/chat/completions` to the base URL.
- **Agent tool calls fail:** `roles` and endpoint tool-call support are separate. Continue documents `tool_use` as required for Agent mode, but actual Rate Cloud compatibility has not been live-tested here. Do not declare it unless verified.
- **Config shape differs in your release:** Continue's reference is the owner for supported YAML fields. Prefer `config.yaml`; JSON configs are documented as deprecated.

Remove secrets and private prompt content from logs before sharing diagnostics. No installs or API requests were run while preparing this guide.

Russian version: [Подключение Continue к Rate Cloud](../ru/guides/continue.md). Back to [all English guides](README.md).
