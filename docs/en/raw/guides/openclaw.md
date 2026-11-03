# Connect OpenClaw to Rate Cloud

OpenClaw can register a custom provider with an OpenAI-compatible base URL. This guide uses its documented `openai-completions` transport and Rate Cloud's OpenAI-compatible Chat Completions API.

**Documentation checked:** November 3, 2026. This is a static configuration example based on the published docs. It has not been live-tested against an OpenClaw installation or Rate Cloud account. OpenClaw docs are rolling docs and do not specify a minimum supported app version here; use the current config format for your installed version.

Official references: [Rate Cloud connection guide](https://rate-cloud.com/docs), [Rate Cloud's OpenClaw example](https://rate-cloud.com/docs), [OpenClaw custom providers](https://docs.openclaw.ai/concepts/model-providers/custom-providers), [OpenClaw provider examples](https://docs.openclaw.ai/gateway/config-tools/provider-examples), [OpenClaw environment variables](https://docs.openclaw.ai/help/environment), and [OpenClaw secret references](https://docs.openclaw.ai/reference/secretref-credential-surface).

## Requirements and access

Create a Rate Cloud API key in the dashboard. Allow the model you want to use, confirm a trial or active subscription for it, and copy the full secret at creation time. A model catalog listing does not itself grant execution access.

Rate Cloud documents this endpoint for OpenAI-compatible requests:

```text
https://llm.rate-cloud.com/v1
```

Select the `openai-completions` adapter. Do not add `/chat/completions` to the base URL. Rate Cloud's direct model IDs are:

| Model | Direct API ID | OpenClaw model reference |
| --- | --- | --- |
| GLM 5.3 | `glm-5.3` | `ratecloud/glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` | `ratecloud/glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` | `ratecloud/deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` | `ratecloud/deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` | `ratecloud/qwen-3.8-max` |

The OpenClaw model reference includes the provider ID; the request sent upstream uses the bare model ID.

## Supply the key without putting it in the config

OpenClaw supports `${VARIABLE_NAME}` substitution in provider `apiKey` values. The current OpenClaw docs recommend the global `~/.openclaw/.env` file for provider keys, which is also read when a Gateway runs as a service. Add this local entry (Windows: `%USERPROFILE%\.openclaw\.env`):

```dotenv
RATE_CLOUD_API_KEY=<your-key>
```

Keep this file local and restrict access to it. OpenClaw's dotenv loader does not expand references inside `.env` values, so put the actual key on the right side of the assignment. Do not put the literal key in a shared `openclaw.json`, source repository, or public issue. Restart the Gateway if its current process has not loaded the new environment value.

## Add the custom provider

Open the existing `~/.openclaw/openclaw.json` on macOS/Linux or `%USERPROFILE%\.openclaw\openclaw.json` on Windows. Back it up, then merge the `models` and `agents` fields below with the existing configuration. Do not replace unrelated settings. The object is JSON5 in OpenClaw, so this no-comment sample is also valid JSON.

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

This example uses the fields in the current OpenClaw custom provider docs and the Rate Cloud example: `baseUrl`, `apiKey`, `api`, `models`, and `agents.defaults.model.primary`. It does not assert context length, image support, tool compatibility, or reasoning behavior. Leave those unspecified unless you have verified them for the endpoint and model.

## Select and troubleshoot

Restart the Gateway after saving the config, then choose the configured Rate Cloud model. For a static check, confirm that the primary model reference exactly matches a provider/model ID in the config. Do not use a live model-list or generation command unless you intend to make an authenticated API request.

- **Provider/model is unknown:** check that `models.providers.ratecloud.models[]` has the exact bare ID and that the selected reference is `ratecloud/<same-id>`.
- **Unauthorized:** confirm the Gateway process can read `RATE_CLOUD_API_KEY`, that the key is active, and that its IP restrictions allow the Gateway host.
- **Access denied:** check key model permissions and trial/subscription access for that specific model.
- **Tool calls or images fail:** the generic protocol does not guarantee every feature. Do not add `reasoning`, `input`, `contextWindow`, or compatibility overrides unless the actual endpoint/model supports them.
- **Using older OpenClaw configuration:** the docs may evolve. Check the current custom provider reference rather than copying a legacy `models.json` schema into `openclaw.json`.

Remove credentials and private prompts before sharing diagnostics. The examples here document configuration only; no API call was run.

Russian version: [Подключение OpenClaw к Rate Cloud](../ru/guides/openclaw.md). Back to [all English guides](README.md).
