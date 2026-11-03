# Conectar o Continue à Rate Cloud

O Continue aceita modelos compatíveis com OpenAI pelo provedor OpenAI e por um `apiBase` personalizado. Este guia usa o formato atual `config.yaml` do Continue e guarda a chave no arquivo local de resolução de segredos do Continue, em vez de colocá-la no YAML.

**Documentação consultada:** 3 de novembro de 2026. Esta é uma configuração estática baseada em documentos, não uma solicitação ao vivo do Continue ou de uma conta da Rate Cloud. A documentação atual do Continue prefere YAML; `config.json` está obsoleto. As páginas consultadas não informam uma versão mínima do cliente para esta configuração. Se sua versão não aceitar algum campo, siga o esquema atual indicado abaixo.

Referências oficiais: [guia de conexão da Rate Cloud](https://rate-cloud.com/docs), [configuração de modelos compatíveis com OpenAI no Continue](https://docs.continue.dev/customize/model-providers/top-level/openai), [referência YAML do Continue](https://docs.continue.dev/reference), [FAQ de segredos do Continue](https://docs.continue.dev/faqs) e [locais de configuração do Continue](https://docs.continue.dev/guides/understanding-configs).

## Verifique acesso e IDs de modelo

Crie uma chave de API da Rate Cloud, permita o modelo necessário e confirme que sua conta tem teste ou assinatura ativa para ele. A chave completa é exibida na criação. A lista de modelos do Continue não concede acesso por si só.

A URL base da Rate Cloud compatível com OpenAI é `https://llm.rate-cloud.com/v1`. Use os IDs exatos da API direta abaixo. O Continue exibe o valor de `name` definido por você no seletor; não exige o prefixo `ratecloud/` usado por alguns outros clientes.

| Modelo | ID da API direta |
| --- | --- |
| GLM 5.3 | `glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` |

## Armazene o segredo para a extensão do IDE

As extensões de IDE do Continue resolvem `${{ secrets.NAME }}` a partir de arquivos `.env`. A documentação especifica esta ordem de busca: `.env` do workspace, `.continue/.env` do workspace e depois `~/.continue/.env` global. A documentação alerta que extensões de IDE não herdam diretamente as variáveis de ambiente do shell.

Crie ou atualize o arquivo global `~/.continue/.env` (Windows: `%USERPROFILE%\.continue\.env`) com esta entrada local:

```dotenv
RATE_CLOUD_API_KEY=<your-key>
```

Mantenha esse arquivo local fora do controle de versão. Não coloque uma chave real em `config.yaml` nem compartilhe o arquivo `.env`. Segundo a documentação do Continue, a CLI do Continue também pode resolver o segredo a partir do ambiente do processo.

## Configure o YAML local do Continue

O Continue mantém a configuração local em `~/.continue/config.yaml` no macOS/Linux e `%USERPROFILE%\.continue\config.yaml` no Windows. Use o seletor de configuração e o ícone de engrenagem na barra lateral do Continue para abri-la. Preserve as seções existentes que não sejam de modelos. Adicione uma entrada para cada modelo que deseja exibir; este exemplo inclui os cinco:

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

`useResponsesApi: false` seleciona a rota documentada Chat Completions. Os modelos são listados com os papéis chat, edit e apply. Este guia não atribui capacidade Agent/uso de ferramentas porque isso depende do suporte real do modelo/API a chamadas de ferramenta; ative tal capacidade somente depois de verificá-la para o modelo utilizado.

Salve a configuração. O guia atual do Continue informa que as mudanças são recarregadas automaticamente. Selecione uma entrada Rate Cloud no seletor de modelos. Não é necessário enviar uma solicitação ao modelo apenas para conferir a configuração estática e a entrada do seletor.

## Solução de problemas

- **A chave de API não é resolvida:** confira a grafia exata `RATE_CLOUD_API_KEY` e se a chave está em um local `.env` aceito. Para extensões de IDE, não dependa apenas de um `export` no terminal.
- **Nenhum modelo Rate Cloud aparece:** confirme que o YAML está no caminho local de configuração, que `schema: v1` está presente e que o arquivo salvo continua sendo YAML válido. Use o seletor de configuração para confirmar que está editando a configuração ativa.
- **401 ou acesso negado:** confirme que o segredo está ativo e que a Rate Cloud permite o modelo tanto para a chave quanto para a conta. A presença do nome no Continue não comprova acesso.
- **404 ou rota de API incorreta:** mantenha `apiBase` como `https://llm.rate-cloud.com/v1`; não acrescente `/chat/completions` à URL base.
- **Chamadas de ferramentas do modo Agent falham:** `roles` e suporte a chamadas de ferramenta do endpoint são coisas diferentes. O Continue documenta `tool_use` como requisito do modo Agent, mas a compatibilidade real da Rate Cloud não foi testada ao vivo aqui. Não declare isso sem verificar.
- **O formato da configuração difere na sua versão:** a referência do Continue é a fonte dos campos YAML aceitos. Prefira `config.yaml`; configurações JSON são documentadas como obsoletas.

Remova segredos e conteúdo privado dos prompts dos logs antes de compartilhar diagnósticos. Nenhuma instalação ou solicitação à API foi feita ao preparar este guia.

Versão em russo: [Conectar o Continue à Rate Cloud](../../ru/guides/continue.md). Voltar para [todos os guias em português](README.md).
