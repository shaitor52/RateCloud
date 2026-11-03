# Acesso HTTP e Python genérico

A Rate Cloud oferece uma API compatível com OpenAI para clientes que permitem URL base personalizada e um exemplo de chamadas diretas com a biblioteca padrão do Python. Estes exemplos não instalam pacotes nem enviam solicitações até que você decida executá-los.

Fonte oficial: [documentação de API e conexão da Rate Cloud](https://rate-cloud.com/docs).

## Endpoints

| Finalidade | Método e URL |
| --- | --- |
| URL base compatível com OpenAI | `https://llm.rate-cloud.com/v1` |
| Listar modelos | `GET https://llm.rate-cloud.com/v1/models` |
| Chat completions | `POST https://llm.rate-cloud.com/v1/chat/completions` |
| API Responses | `POST https://llm.rate-cloud.com/v1/responses` |

Para solicitações `/v1`, envie `Authorization: Bearer <API key>`. Use um ID de modelo exatamente como na tabela:

| Modelo | ID da API direta |
| --- | --- |
| GLM 5.3 | `glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` |

Não acrescente prefixo de provedor, como `ratecloud/`, ao ID HTTP direto. As formas `ratecloud/` e `ocx-claude-ratecloud--` são usadas em integrações específicas de clientes.

## Defina uma variável de ambiente

No macOS ou Linux, use o bloco do seu shell. Ambos leem o segredo sem exibi-lo. A variável é removida quando você executa `unset` ou fecha o terminal.

```sh
# Bash
read -r -s -p 'Rate Cloud API key: ' RATE_CLOUD_API_KEY
printf '\n'
export RATE_CLOUD_API_KEY
```

```sh
# zsh (o shell padrão do macOS)
read -r -s 'RATE_CLOUD_API_KEY?Rate Cloud API key: '
printf '\n'
export RATE_CLOUD_API_KEY
```

No Windows PowerShell, defina `$env:RATE_CLOUD_API_KEY` na sessão que executará o cliente. Não coloque uma chave real no código-fonte, em arquivo `.env` versionado ou em issue pública.

## Verificação opcional de conexão com curl

Isto envia uma solicitação simples ao catálogo de modelos. Confirma que o endpoint responde e aceita a chave, mas não prova que há assinatura ou permissão da chave para um modelo específico.

```sh
curl --fail-with-body 'https://llm.rate-cloud.com/v1/models' \
  -H "Authorization: Bearer $RATE_CLOUD_API_KEY"
```

## Exemplo Python 3 com biblioteca padrão

Salve este código em um arquivo `.py` local. Ele usa apenas a biblioteca padrão do Python (`urllib.request`), lê o segredo do ambiente e envia uma solicitação pequena de chat completions ao ser executado. Se quiser, altere `MODEL` para outro ID exato da API direta.

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

Execute-o no shell em que `RATE_CLOUD_API_KEY` está definida. Não imprima a resposta completa em logs compartilhados se prompts ou saídas puderem conter dados privados.

## Solução de problemas

- **401 ou erro de autenticação:** confirme que a variável está no ambiente do processo, que a chave está ativa e não expirou e que o cabeçalho `Authorization` usa `Bearer` seguido da chave.
- **403 ou acesso negado:** verifique acesso de teste ou assinatura ao modelo, permissões da chave, restrições de IP e qualquer opção de compatibilidade exigida por endpoint dedicado.
- **404 ou modelo não encontrado:** confira o caminho do endpoint e a grafia exata do modelo. Use `/v1` nestes exemplos, não os endpoints de compatibilidade do Codex ou Claude Code.
- **O catálogo lista o modelo, mas a geração é negada:** o catálogo não prova permissões da conta ou da chave. Confirme no painel a assinatura do modelo e o acesso da chave.
- **Tempo limite ou saída incompleta:** confira o estado da resposta antes de tentar de novo. Um tempo limite não comprova que a operação terminou; evite repetir às cegas solicitações que causem efeitos colaterais no seu aplicativo.

Ao pedir suporte, informe horário, ID do modelo, caminho do endpoint, status HTTP e identificador da solicitação, se disponível. Remova chaves de API, cabeçalhos de autorização e conteúdo privado das solicitações e respostas.
