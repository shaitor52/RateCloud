# Conectar o Hermes Agent à Rate Cloud

O Hermes Agent aceita endpoints personalizados compatíveis com OpenAI. Este guia usa a configuração documentada de provedor personalizado com o endpoint Chat Completions `/v1` da Rate Cloud compatível com OpenAI.

**Documentação consultada:** 3 de novembro de 2026. Os exemplos seguem a documentação publicada do Hermes e da Rate Cloud e não foram testados ao vivo em uma instalação do Hermes Agent ou conta. A documentação do Hermes é contínua; as páginas consultadas não informam uma versão mínima para esta configuração. A configuração do provedor mudou ao longo do tempo, portanto use os nomes atuais dos campos abaixo, não trechos antigos.

Referências oficiais: [guia de conexão da Rate Cloud](https://rate-cloud.com/docs), [guia de provedores do Hermes Agent](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/integrations/providers.md), [variáveis de ambiente do Hermes](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/reference/environment-variables.md) e [arquivos de configuração do Hermes](https://hermes-agent.nousresearch.com/docs).

## Prepare o acesso

Crie uma chave de API da Rate Cloud no painel, permita o modelo que pretende usar e confirme que a conta tem acesso de teste ou assinatura ativa. A chave completa é mostrada somente na criação. Mantenha-a fora do código-fonte e de mensagens ao suporte.

O endpoint compatível genérico da Rate Cloud é:

```text
https://llm.rate-cloud.com/v1
```

O ID do modelo é o identificador direto, sem prefixo. O Hermes não exige o prefixo `ratecloud/` usado por alguns outros clientes.

| Modelo | ID da API direta |
| --- | --- |
| GLM 5.3 | `glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` |

## Armazene o segredo no arquivo de ambiente local do Hermes

A documentação atual do Hermes coloca segredos gerenciados pelo usuário em `~/.hermes/.env`. Adicione esta linha localmente e substitua o marcador pela chave:

```dotenv
RATE_CLOUD_API_KEY=<your-key>
```

No Windows, use `%USERPROFILE%\.hermes\.env`. Não versione esse arquivo nem cole uma chave real em um exemplo compartilhado. O Hermes também aceita uma variável no ambiente do processo; a configuração `key_env` abaixo nomeia essa variável.

## Configure um endpoint personalizado

Edite `~/.hermes/config.yaml` no macOS/Linux ou `%USERPROFILE%\.hermes\config.yaml` no Windows. Mescle estes campos à seção `model` existente em vez de substituir configurações não relacionadas:

```yaml
model:
  default: glm-5.3
  provider: custom
  base_url: https://llm.rate-cloud.com/v1
  key_env: RATE_CLOUD_API_KEY
```

Isso usa as chaves documentadas de endpoint personalizado do Hermes: `provider: custom`, `base_url` e `key_env`. O endpoint usa Chat Completions; não o altere para o transporte Anthropic Messages ou Responses. Não adicione um limite de contexto sem um valor verificado para o serviço e o modelo.

Para selecionar outro modelo da Rate Cloud, altere `model.default` para um dos outros IDs exatos da tabela. Mantenha `provider: custom` e a URL base da Rate Cloud.

## Configuração interativa opcional

O Hermes documenta `hermes model` como assistente de configuração de endpoint personalizado. O assistente solicita URL base, chave de API e nome do modelo e salva a escolha. Se usá-lo, informe `https://llm.rate-cloud.com/v1` e um ID sem prefixo da tabela. Prefira o arquivo de ambiente e a configuração manual acima se quiser evitar salvar a chave literal em `config.yaml`.

## Solução de problemas

- **Credencial ausente:** confirme que `RATE_CLOUD_API_KEY` está definida em `~/.hermes/.env` ou no ambiente do processo e que `key_env` tem a mesma grafia.
- **Erro de conexão:** use URL base terminada em `/v1`, não `/v1/chat/completions`; o cliente acrescenta a rota de API.
- **Modelo desconhecido ou acesso negado:** use o ID direto exato. Verifique permissões de modelo da chave e acesso de teste ou assinatura ativa.
- **Chamadas de ferramenta aparecem como texto:** o transporte compatível com OpenAI não garante que todos os modelos e endpoints aceitem chamadas de ferramentas no formato esperado pelo agente. Verifique a capacidade real do modelo antes de depender disso.
- **O limite de contexto parece incorreto:** o Hermes pode inferir metadados de `/v1/models`, mas a listagem não garante todos os detalhes. Não copie para a configuração um limite de contexto não verificado.
- **Você encontrou um exemplo antigo:** documentos mais velhos podem mostrar `api_key` ou outra estrutura de provedor personalizado. Use o guia atual de provedores do Hermes e confirme os campos para a versão instalada.

Nenhuma solicitação à API ou instalação foi executada durante a preparação deste guia.

Versão em russo: [Conectar o Hermes Agent à Rate Cloud](../../ru/guides/hermes-agent.md). Voltar para [todos os guias em português](README.md).
