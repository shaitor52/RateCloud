# Connect DeepSeek Harness to Rate Cloud

DeepSeek Harness has a documented **Custom model API** form for OpenAI-compatible gateways. Rate Cloud documents an OpenAI-compatible Chat Completions endpoint. The setup below uses that protocol and manual model IDs.

**Documentation checked:** November 3, 2026. DeepSeek Harness identifies itself as a developer preview with breaking changes. This guide follows its published Web UI docs and Rate Cloud docs; it is a static compatibility mapping, not a live-tested integration. No installation or API request was run.

Official references: [Rate Cloud connection guide](https://rate-cloud.com/docs), [DeepSeek Harness repository and preview notice](https://github.com/deepseek-ai/deepseek-harness), [DeepSeek Harness model configuration](https://deepseek-harness.github.io/deepseek-harness/en/guide/providers), [DeepSeek Harness quickstart](https://deepseek-harness.github.io/deepseek-harness/en/guide/quickstart), and [plugin configuration catalog](https://deepseek-harness.github.io/deepseek-harness/en/reference/config-catalog).

## Compatibility boundary

Rate Cloud documents these endpoints and direct model IDs:

| Purpose | Value |
| --- | --- |
| Base URL | `https://llm.rate-cloud.com/v1` |
| Chat Completions route | `POST /v1/chat/completions` |
| GLM 5.3 | `glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` |

Harness documents custom providers with a user-supplied base URL, protocol, credential, and model list. For this endpoint select **OpenAI Chat Completions**. Do not select Responses or Anthropic Messages for this example. The published docs do not establish a Harness built-in Rate Cloud provider or live-tested compatibility.

## Prepare account and key permissions

In the Rate Cloud dashboard, create an API key, allow the model you will use, and confirm that the account has active trial or subscription access to that model. The full key is shown once when created. A visible catalog entry does not prove the key can call the model.

## Add a custom model API in the Web UI

This is a UI-only configuration walkthrough. It does not run an installer or send a model request.

1. Start the Harness Web UI using the steps in its official README. This guide does not reproduce install commands.
2. Open **Settings → Models**, then choose **Add model provider**.
3. Switch the form to **Custom model API**.
4. Set a lowercase provider ID such as `ratecloud`. Harness documents this ID as permanent because sessions, defaults, requests, and credential references use it.
5. Set the display name to `Rate Cloud` and the Base URL to `https://llm.rate-cloud.com/v1`.
6. Choose **OpenAI Chat Completions** as the API protocol.
7. Enter the Rate Cloud key in the form's credential field. Harness documents that saved keys are write-only in the UI; the credential is stored under `$DSH_HOME/.credentials.yaml` and settings keep a credential reference. Do not put the key in a repository or public issue.
8. Add a model manually using one of the exact IDs in the table. Give it a readable display name. Leave context-window, maximum-output, image-input, and reasoning options unset unless you have a verified value or capability for that model.
9. Save the provider, then select the configured model in the model picker to make it the default for new sessions.

You can add more models to the same provider using their exact bare IDs. Do not add a client prefix such as `ratecloud/` to the model ID entered in this custom API form.

## Optional model discovery

Harness can fetch a model list using the provider's URL, protocol, and credential. That action sends an authenticated HTTP request to the endpoint. Discovery is optional and not guaranteed to work with every listing format. For a no-request setup, add the model IDs manually as above. No discovery request was made while preparing this guide.

## Troubleshooting

- **`MISSING_CREDENTIAL`:** confirm that a key was saved for the provider or that its configured credential reference is available.
- **`UNKNOWN_MODEL`:** add the model ID to the custom provider, then select that configured entry. Use the exact lowercase ID and punctuation.
- **HTTP 401:** verify the key, expiry, and model permission in Rate Cloud. The model-list UI is not an access check.
- **HTTP 404 or route mismatch:** use `https://llm.rate-cloud.com/v1` as Base URL and select OpenAI Chat Completions. Do not include `/chat/completions` in the Base URL.
- **A fetch-models action returns no entries:** the endpoint's listing format may not be one Harness discovery recognizes. Add a model ID manually; do not treat a failed discovery call as proof that inference is unavailable.
- **Tool calls, images, or reasoning fail:** declaring these capabilities in Harness does not test or create API support. Configure only capabilities documented for the selected model and confirmed by actual compatibility work.
- **Configuration paths differ:** Harness is in developer preview and may change quickly. Use its current model configuration page and generated plugin config catalog for the installed version.

No live request was made, so endpoint authentication and feature behavior remain unverified in Harness itself.

Russian version: [Подключение DeepSeek Harness к Rate Cloud](../ru/guides/deepseek-harness.md). Back to [all English guides](README.md).
