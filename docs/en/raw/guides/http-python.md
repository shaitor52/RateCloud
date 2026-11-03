# Generic HTTP and Python access

Rate Cloud provides an OpenAI-compatible API for clients that allow a custom base URL, and a standard-library Python example for direct calls. These examples do not install packages and do not make a request until you choose to run them.

Official reference: [Rate Cloud API and connection documentation](https://rate-cloud.com/docs).

## Endpoints

| Purpose | Method and URL |
| --- | --- |
| OpenAI-compatible base URL | `https://llm.rate-cloud.com/v1` |
| List models | `GET https://llm.rate-cloud.com/v1/models` |
| Chat completions | `POST https://llm.rate-cloud.com/v1/chat/completions` |
| Responses API | `POST https://llm.rate-cloud.com/v1/responses` |

For `/v1` requests, send `Authorization: Bearer <API key>`. Use a model ID exactly as shown in the table:

| Model | Direct API ID |
| --- | --- |
| GLM 5.3 | `glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` |

Do not add a provider prefix such as `ratecloud/` to a direct HTTP model ID. The `ratecloud/` and `ocx-claude-ratecloud--` forms are for particular client integrations.

## Set an environment variable

On macOS or Linux, use the block for your shell. Both variants read the secret without echoing it. The variable is removed when you run `unset` or close the terminal.

```sh
# Bash
read -r -s -p 'Rate Cloud API key: ' RATE_CLOUD_API_KEY
printf '\n'
export RATE_CLOUD_API_KEY
```

```sh
# zsh (the default macOS shell)
read -r -s 'RATE_CLOUD_API_KEY?Rate Cloud API key: '
printf '\n'
export RATE_CLOUD_API_KEY
```

On Windows PowerShell, set `$env:RATE_CLOUD_API_KEY` in the session that runs your client. Do not put a real key in source code, a committed `.env` file, or a public issue.

## Optional connectivity check with curl

This sends a simple request to the model catalog. It confirms that the endpoint responds and the key is accepted, but does not prove that a specific model is subscribed or permitted for the key.

```sh
curl --fail-with-body 'https://llm.rate-cloud.com/v1/models' \
  -H "Authorization: Bearer $RATE_CLOUD_API_KEY"
```

## Python 3 standard-library example

Save this as a local `.py` file. It uses only Python's standard library (`urllib.request`), reads the secret from the environment, and sends one small chat-completions request when you run it. Change `MODEL` to another exact direct API ID if desired.

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

Run it from the shell where `RATE_CLOUD_API_KEY` is set. Do not print the full response in shared logs if prompts or model outputs may contain private information.

## Troubleshooting

- **401 or authentication error:** confirm the environment variable is set in the process environment, the key is active and unexpired, and the `Authorization` header uses `Bearer` followed by the key.
- **403 or access denied:** verify trial or subscription access for the requested model, key model permissions, IP restrictions, and any client compatibility flag required by a dedicated client endpoint.
- **404 or model not found:** check the endpoint path and exact model spelling. Use `/v1` for these generic examples, not the Codex or Claude Code compatibility endpoints.
- **The catalog lists a model but generation is denied:** the catalog is not proof of account or key permission. Confirm both model subscription and key access in the dashboard.
- **Timeout or incomplete output:** retry only after checking the response state. A timeout does not establish that the operation completed; avoid blindly repeating requests that trigger costly side effects in your own application.

When asking support for help, share the time, model ID, endpoint path, HTTP status, and request identifier if available. Remove API keys, authorization headers, and private prompt or response content.
