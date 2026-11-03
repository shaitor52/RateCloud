# Conectar o OpenClaw à Rate Cloud

O OpenClaw permite registrar um provedor personalizado com URL base compatível com OpenAI. Este guia usa o transporte documentado `openai-completions` e a API Chat Completions da Rate Cloud compatível com OpenAI.

**Documentação consultada:** 3 de novembro de 2026. Este é um exemplo estático baseado na documentação publicada. Não foi testado ao vivo em uma instalação do OpenClaw ou conta da Rate Cloud. A documentação do OpenClaw é contínua e não especifica aqui uma versão mínima; use o formato atual da configuração da sua versão instalada.

Referências oficiais: [guia de conexão da Rate Cloud](https://rate-cloud.com/docs), [exemplo de OpenClaw da Rate Cloud](https://rate-cloud.com/docs), [provedores personalizados do OpenClaw](https://docs.openclaw.ai/concepts/model-providers/custom-providers), [exemplos de provedores do OpenClaw](https://docs.openclaw.ai/gateway/config-tools/provider-examples) e [referências de segredo do OpenClaw](https://docs.openclaw.ai/reference/secretref-credential-surface).

## Requisitos e acesso

Crie uma chave de API da Rate Cloud no painel. Permita o modelo que deseja usar, confirme que há teste ou assinatura ativa para ele e copie o segredo completo no momento da criação. A presença no catálogo não concede, por si só, acesso à execução.

A Rate Cloud documenta este endpoint para solicitações compatíveis com OpenAI:

```text
https://llm.rate-cloud.com/v1
```

Selecione o adaptador `openai-completions`. Não acrescente `/chat/completions` à URL base. Os IDs diretos de modelo da Rate Cloud são:

| Modelo | ID da API direta | Referência do modelo no OpenClaw |
| --- | --- | --- |
| GLM 5.3 | `glm-5.3` | `ratecloud/glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` | `ratecloud/glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` | `ratecloud/deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` | `ratecloud/deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` | `ratecloud/qwen-3.8-max` |

A referência de modelo do OpenClaw inclui o ID do provedor; a solicitação enviada ao serviço usa o ID de modelo sem o prefixo.

## Forneça a chave sem colocá-la na configuração

O OpenClaw aceita substituição `${VARIABLE_NAME}` em valores `apiKey` do provedor. Defina `RATE_CLOUD_API_KEY` no ambiente do processo Gateway do OpenClaw. O prompt do shell ajuda a não registrar o segredo no histórico:

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

Então inicie ou reinicie o Gateway a partir desse ambiente. Para um gerenciador de serviços ou Windows, configure a variável pelo mecanismo local seguro de segredos desse ambiente. Não coloque a chave literal em um `openclaw.json` compartilhado, repositório de código ou issue pública.

## Adicione o provedor personalizado

Abra o `~/.openclaw/openclaw.json` existente no macOS/Linux ou `%USERPROFILE%\.openclaw\openclaw.json` no Windows. Faça uma cópia de segurança e mescle os campos `models` e `agents` abaixo na configuração existente. Não substitua configurações não relacionadas. O OpenClaw usa JSON5, portanto este exemplo sem comentários também é JSON válido.

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

Este exemplo usa os campos da documentação atual de provedor personalizado do OpenClaw e o exemplo da Rate Cloud: `baseUrl`, `apiKey`, `api`, `models` e `agents.defaults.model.primary`. Ele não afirma limite de contexto, suporte a imagens, compatibilidade de ferramentas nem comportamento de raciocínio. Deixe esses itens sem especificação, a menos que os tenha verificado para o endpoint e o modelo.

## Seleção e solução de problemas

Reinicie o Gateway após salvar a configuração e escolha o modelo Rate Cloud configurado. Para uma verificação estática, confirme que a referência do modelo principal corresponde exatamente a um ID de provedor/modelo na configuração. Não use comandos de listagem ou geração ao vivo, a menos que pretenda fazer uma solicitação autenticada à API.

- **Provedor/modelo desconhecido:** confira se `models.providers.ratecloud.models[]` contém o ID exato sem prefixo e se a referência selecionada é `ratecloud/<mesmo-id>`.
- **Não autorizado:** confirme que o processo Gateway consegue ler `RATE_CLOUD_API_KEY`, que a chave está ativa e que suas restrições de IP permitem o host do Gateway.
- **Acesso negado:** verifique permissões de modelo da chave e acesso de teste/assinatura para aquele modelo.
- **Falha de ferramentas ou imagens:** o protocolo genérico não garante todos os recursos. Não adicione `reasoning`, `input`, `contextWindow` ou substituições de compatibilidade sem que o endpoint/modelo realmente os suporte.
- **Configuração antiga do OpenClaw:** a documentação pode mudar. Consulte a referência atual de provedores personalizados em vez de copiar um esquema legado `models.json` para `openclaw.json`.

Remova credenciais e prompts privados antes de compartilhar diagnósticos. Os exemplos documentam apenas a configuração; nenhuma chamada à API foi executada.

Versão em russo: [Conectar o OpenClaw à Rate Cloud](../../ru/guides/openclaw.md). Voltar para [todos os guias em português](README.md).

[Referência](https://docs.openclaw.ai/help/environment)
