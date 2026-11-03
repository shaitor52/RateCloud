# Connect Claude Code to Rate Cloud

Claude Code uses Rate Cloud's dedicated compatibility endpoint and client-specific model names. This is API access to GLM, DeepSeek, or Qwen through Rate Cloud; it does not turn those models into Anthropic models.

Official references: [Rate Cloud connection guide](https://rate-cloud.com/docs) and [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code/overview).

## Create and prepare an API key

In the Rate Cloud dashboard, create a key, copy its full secret at creation time, and enable **Codex / Claude Code compatibility**. Give the key permission for the model you plan to use, and make sure the account has an active trial or subscription for it. The model list alone does not confirm execution access.

## Model names for Claude Code

Claude Code uses the `ocx-claude-ratecloud--` prefix followed by the exact model ID. This differs from the direct HTTP API, which uses the bare ID.

| Model | Direct API ID | Claude Code `ANTHROPIC_MODEL` |
| --- | --- | --- |
| GLM 5.3 | `glm-5.3` | `ocx-claude-ratecloud--glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` | `ocx-claude-ratecloud--glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` | `ocx-claude-ratecloud--deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` | `ocx-claude-ratecloud--deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` | `ocx-claude-ratecloud--qwen-3.8-max` |

## Launch from macOS or Linux

In a Bash or zsh terminal, first read the key without echoing it. Then set the three variables and launch Claude Code from the same terminal. The value remains in this shell's environment until you close the shell or unset it.

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

Continue in that same terminal:

```sh
export ANTHROPIC_BASE_URL='https://llm.rate-cloud.com/claude'
export ANTHROPIC_AUTH_TOKEN="$RATE_CLOUD_API_KEY"
export ANTHROPIC_MODEL='ocx-claude-ratecloud--glm-5.3'
claude
```

Replace the model value with another exact Claude Code model name from the table if needed. When finished, close the terminal or run `unset RATE_CLOUD_API_KEY ANTHROPIC_AUTH_TOKEN ANTHROPIC_BASE_URL ANTHROPIC_MODEL`.

## Launch from Windows PowerShell

Set the variables in the PowerShell window from which you launch Claude Code. `Read-Host` displays typed input; use an approved local secret manager if you need hidden input.

```powershell
$env:RATE_CLOUD_API_KEY = Read-Host 'Rate Cloud API key'
$env:ANTHROPIC_BASE_URL = 'https://llm.rate-cloud.com/claude'
$env:ANTHROPIC_AUTH_TOKEN = $env:RATE_CLOUD_API_KEY
$env:ANTHROPIC_MODEL = 'ocx-claude-ratecloud--glm-5.3'
claude
```

After closing Claude Code, remove the values from the current PowerShell session:

```powershell
Remove-Item Env:RATE_CLOUD_API_KEY, Env:ANTHROPIC_BASE_URL, Env:ANTHROPIC_AUTH_TOKEN, Env:ANTHROPIC_MODEL
```

## Troubleshooting

- **Authentication or compatibility error:** check that the key's **Codex / Claude Code compatibility** option is enabled. This compatibility setting is required for this endpoint.
- **Unknown model:** use the full `ocx-claude-ratecloud--` name, with the exact suffix shown above. Do not use the bare HTTP ID in `ANTHROPIC_MODEL`.
- **Model access denied:** check active trial or subscription access, key model permissions, expiry, and any IP allowlist in the dashboard.
- **It works in a terminal but not in an app launcher:** environment variables set in a terminal are inherited by programs launched from that terminal. Start Claude Code from the configured shell or use the dashboard's current setup guide for persistent client settings.
- **Connection fails:** verify the base URL is exactly `https://llm.rate-cloud.com/claude`; this is the Claude Code compatibility URL, not the generic `/v1` endpoint.

For support, provide the client version, OS, model name, time, and error text. Remove API secrets, authorization headers, and private prompt content first.
