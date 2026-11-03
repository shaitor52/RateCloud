# Conectar o OpenCode à Rate Cloud

Este guia configura o OpenCode para usar a API compatível com OpenAI da Rate Cloud. Ele cobre o formato documentado de configuração do OpenCode v1. A página atual de conexão da Rate Cloud distingue os formatos v1 e v2; para v2, use o exemplo v2 atual no painel, sem colar nele uma configuração v1.

Fontes oficiais: [guia de conexão da Rate Cloud](https://rate-cloud.com/docs) e [configuração do OpenCode](https://opencode.ai/docs/config/).

## Antes de começar

1. Entre na Rate Cloud e crie uma chave de API em **Settings → API keys**. Copie-a ao criar, pois o segredo completo é exibido apenas uma vez.
2. Confirme que a chave permite o modelo desejado e que a conta tem um teste ativo ou assinatura para esse modelo. A lista pode mostrar modelos sem conceder permissão para executá-los.
3. A configuração de provedor do OpenCode v1 usa o prefixo `ratecloud/` ao selecionar o provedor configurado. Esse prefixo é do cliente. O ID enviado pela API HTTP direta não o inclui.

Os IDs exatos da API direta são:

| Modelo | ID da API direta | Seleção no OpenCode v1 |
| --- | --- | --- |
| GLM 5.3 | `glm-5.3` | `ratecloud/glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` | `ratecloud/glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` | `ratecloud/deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` | `ratecloud/deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` | `ratecloud/qwen-3.8-max` |

## Defina a chave no shell

Os exemplos abaixo leem a chave sem exibi-la. Use o bloco do seu shell: Bash ou zsh, o shell padrão do macOS. Digite o segredo no prompt. A variável fica disponível para programas iniciados por esse shell; ao terminar, feche o terminal ou remova-a com `unset`.

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

Não cole a chave em arquivo de configuração compartilhado, repositório, captura de tela ou mensagem de suporte. No Windows, defina `RATE_CLOUD_API_KEY` no ambiente usado para iniciar o OpenCode, com seu método local seguro habitual de gerenciamento de segredos.

## Configure o OpenCode v1

Abra a configuração existente do OpenCode em `~/.config/opencode/opencode.json` no macOS/Linux. Preserve outros provedores e configurações. Mescle a entrada `provider` abaixo no objeto existente e depois defina ou mescle o campo `model` de nível superior. Se o arquivo for novo, este exemplo mínimo completo seleciona GLM 5.3:

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

Ao carregar a configuração, o OpenCode substitui `{env:RATE_CLOUD_API_KEY}` pelo valor do ambiente. Se a variável não estiver definida, será substituída por uma string vazia; portanto, exporte-a antes de iniciar o OpenCode. A configuração guarda apenas a referência à variável, não o segredo.

No Windows, o caminho de configuração de usuário documentado é `%USERPROFILE%\.config\opencode\opencode.json`. OpenCode v1 e v2 usam estruturas de provedor diferentes. Para v2, siga o exemplo manual específico de v2 no painel da Rate Cloud; não adapte este exemplo v1 por tentativa.

## Escolha um modelo e verifique a conexão

Reinicie o OpenCode após alterar a configuração, abra o seletor de modelos (`/models` na TUI) e escolha um modelo `Rate Cloud`. Comece com uma solicitação curta e sem conteúdo sensível. Use o ID correspondente na coluna de seleção do OpenCode v1.

## Solução de problemas

- **Rate Cloud não aparece na lista:** confirme que a configuração foi salva no local do seu sistema e que o JSON é válido. Verifique se `provider.ratecloud` e o `model` selecionado estão no nível superior correto.
- **Solicitação não autorizada ou negada:** confira se `RATE_CLOUD_API_KEY` foi exportada no mesmo shell que iniciou o OpenCode. Verifique expiração, restrições de IP, permissões do modelo e acesso de teste ou assinatura no painel.
- **A chave parece vazia:** o OpenCode substitui uma variável de ambiente não definida por valor vazio. Defina-a antes de iniciar o cliente e reinicie-o.
- **Solicitação rejeitada para o modelo:** use o ID exato em minúsculas, incluindo a pontuação, e confirme que a conta e a chave podem executar o modelo. A presença no catálogo não prova acesso.
- **Você usa OpenCode v2:** use o formato `providers` próprio dele no painel. Não insira este exemplo v1 com o campo `provider` em um arquivo v2.

Ao contatar o suporte, informe versão do cliente, sistema operacional, ID do modelo, horário e texto do erro, removendo antes chaves de API, cabeçalhos de autorização e conteúdo privado.
