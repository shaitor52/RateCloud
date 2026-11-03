# Connect OpenCode to Rate Cloud

This guide configures OpenCode to use Rate Cloud's OpenAI-compatible API. It covers the documented OpenCode v1 configuration format. Rate Cloud's live connection page distinguishes v1 and v2 formats; for v2, use the current v2 example in the dashboard rather than pasting a v1 configuration into it.

Official references: [Rate Cloud connection guide](https://rate-cloud.com/docs) and [OpenCode configuration](https://opencode.ai/docs/config/).

## Before you start

1. Sign in to Rate Cloud and create an API key in **Settings → API keys**. Copy it when created because the full secret is shown only once.
2. Ensure the key allows the model you intend to use and that you have an active trial or subscription for that model. The model list can show models without granting execution access.
3. OpenCode's v1 provider configuration uses the `ratecloud/` prefix when selecting the configured provider. This prefix is for the client. The model ID sent through the direct HTTP API does not include it.

The exact direct API IDs are:

| Model | Direct API ID | OpenCode v1 selection |
| --- | --- | --- |
| GLM 5.3 | `glm-5.3` | `ratecloud/glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` | `ratecloud/glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` | `ratecloud/deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` | `ratecloud/deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` | `ratecloud/qwen-3.8-max` |

## Set the key in your shell

The examples below read the key without echoing it. Use the block for your shell: Bash, or zsh (the default macOS shell). Enter the secret at the prompt. The variable is available to programs launched from that shell; close the terminal when finished or remove it with `unset`.

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

Do not paste the key into a shared config file, source repository, screenshot, or support message. On Windows, set `RATE_CLOUD_API_KEY` in the environment used to launch OpenCode, using your usual secure local secret-handling method.

## Configure OpenCode v1

Open the existing OpenCode configuration at `~/.config/opencode/opencode.json` on macOS/Linux. Preserve other providers and settings. Merge the `provider` entry below into your existing object, then set or merge the top-level `model` value. If the file is new, this complete minimal example selects GLM 5.3:

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

OpenCode substitutes `{env:RATE_CLOUD_API_KEY}` from the environment when it loads the config. An unset variable becomes an empty string, so export the key before launching OpenCode. The config stores only the variable reference, not the secret.

On Windows, the documented user config location is `%USERPROFILE%\.config\opencode\opencode.json`. OpenCode v1 and v2 use different provider structures. For OpenCode v2, follow the v2-specific manual example in the Rate Cloud dashboard; do not convert this v1 sample by guesswork.

## Select a model and check the connection

Restart OpenCode after changing its config, open the model picker (`/models` in the TUI), and select a `Rate Cloud` model. Start with a short non-sensitive request. Use the matching ID from the OpenCode v1 selection column above.

## Troubleshooting

- **Rate Cloud is missing from the model list:** confirm the config was saved in the location for your OS and that the JSON is valid. Check that `provider.ratecloud` and the selected `model` are merged at the correct top level.
- **The request is unauthorized or denied:** make sure `RATE_CLOUD_API_KEY` was exported in the same shell that launched OpenCode. Check key expiry, IP restrictions, model permissions, and trial or subscription access in the dashboard.
- **The key appears blank:** OpenCode replaces an unset environment variable with an empty value. Set it before launching the client, then restart OpenCode.
- **A request is rejected for the model:** use the exact lowercase ID, including punctuation, and ensure the key and account can run that model. A visible catalog entry alone is not proof of access.
- **You use OpenCode v2:** use its own `providers` format from the dashboard. Do not insert this v1 `provider` example into a v2 file.

When contacting support, share the client version, operating system, model ID, time, and error text after removing API keys, authorization headers, and private prompt content.
