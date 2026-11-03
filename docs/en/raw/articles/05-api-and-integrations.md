# Connecting tools and applications to Rate Cloud

English · [Русский](../ru/articles/05-api-and-integrations.md)

Rate Cloud offers an OpenAI-compatible HTTP API and dedicated compatibility endpoints for supported coding clients. The official dashboard supplies application-specific setup instructions. Use those instructions for the installed client version and operating system.

## Published endpoints

| Purpose | Endpoint |
| --- | --- |
| OpenAI-compatible base URL | `https://llm.rate-cloud.com/v1` |
| Model catalog | `GET https://llm.rate-cloud.com/v1/models` |
| Chat completions | `POST https://llm.rate-cloud.com/v1/chat/completions` |
| Responses | `POST https://llm.rate-cloud.com/v1/responses` |
| Codex compatibility base URL | `https://llm.rate-cloud.com/codex/v1` |
| Claude Code compatibility base URL | `https://llm.rate-cloud.com/claude` |

Direct `/v1` requests authenticate with a bearer API key. Use an exact model ID from the [catalog](02-models.md), such as `glm-5.3`. Do not add the client-specific `ratecloud/` prefix to a direct HTTP model identifier.

## From registration to the first request

Register or sign in through [Rate Cloud](https://rate-cloud.com/). Complete the verification needed for trial access or purchase access to the model you need. In the dashboard's API-key settings, create a named key, choose its model access, permitted IP addresses, and expiry, then copy the displayed secret immediately.

A subscription provides the right to run a model; key permissions control whether a particular key may use that right. A key limited to selected models does not automatically gain access to a newly purchased model. A visible model catalog is not proof of active execution access.

For Codex or Claude Code, the public guide instructs users to enable the key's Codex / Claude Code compatibility option.

## A minimal HTTP request

Set `RATE_CLOUD_API_KEY` in your local environment using your preferred secret-handling mechanism, then run:

```sh
curl --fail-with-body https://llm.rate-cloud.com/v1/chat/completions \
  -H "Authorization: Bearer $RATE_CLOUD_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"model":"glm-5.3","messages":[{"role":"user","content":"Reply with a short greeting."}]}'
```

The variable above is a placeholder for your local secret. Never place a real key in a public repository, screenshot, support message, or committed client configuration. Use the model catalog endpoint to check identifiers, then make a small request with a model your account and key can access.

## Coding clients and other applications

The public connection guide covers OpenCode, Codex, Claude Code, OpenClaw, Continue, Hermes, and other compatible clients. The dashboard provides automatic commands and manual setup examples for supported operating systems.

Client configuration is version-specific. For example, the official guide distinguishes OpenCode v1 and v2 configuration formats. Prefer the current dashboard instructions over copying an old configuration block from a third-party article.

The client contributes the editor or terminal interface, local tools, MCP connections, project instructions, and conversation management. Available model features depend on both the selected model and the integration. A compatible endpoint does not imply every feature of every first-party API is available.

## Troubleshooting without exposing secrets

Check the base URL and exact model identifier, active subscription or trial, key model permissions, expiry, IP restrictions, and the compatibility option where required. If requests overlap, account for the shared slot pool. Keep the time and request identifier when contacting support, and remove authorization headers and private prompt content.

Source: [Rate Cloud API and connection documentation](https://rate-cloud.com/docs), retrieved November 3, 2026. [Back to overview](../README.md).
