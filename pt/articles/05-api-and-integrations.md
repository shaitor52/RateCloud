# Conectar ferramentas e aplicativos à Rate Cloud

A Rate Cloud oferece uma API HTTP compatível com OpenAI e endpoints de compatibilidade dedicados para clientes de programação compatíveis. O painel oficial fornece instruções de configuração específicas de cada aplicativo. Use as instruções correspondentes à versão do cliente e ao sistema operacional instalados.

## Endpoints publicados

| Finalidade | Endpoint |
| --- | --- |
| URL base compatível com OpenAI | `https://llm.rate-cloud.com/v1` |
| Catálogo de modelos | `GET https://llm.rate-cloud.com/v1/models` |
| Chat completions | `POST https://llm.rate-cloud.com/v1/chat/completions` |
| Responses | `POST https://llm.rate-cloud.com/v1/responses` |
| URL base de compatibilidade com Codex | `https://llm.rate-cloud.com/codex/v1` |
| URL base de compatibilidade com Claude Code | `https://llm.rate-cloud.com/claude` |

Solicitações diretas a `/v1` usam uma chave de API bearer para autenticação. Use um ID de modelo exato do [catálogo](02-models.md), como `glm-5.3`. Não acrescente o prefixo de cliente `ratecloud/` ao identificador HTTP direto.

## Do cadastro à primeira solicitação

Cadastre-se ou entre em [Rate Cloud](https://rate-cloud.com/). Conclua as verificações necessárias para o teste ou compre acesso ao modelo desejado. Nas configurações de chaves de API do painel, crie uma chave nomeada, escolha os modelos permitidos, os endereços IP autorizados e a data de expiração; em seguida copie imediatamente o segredo exibido.

A assinatura concede o direito de executar um modelo; as permissões da chave determinam se uma chave específica pode usar esse direito. Uma chave limitada a modelos selecionados não ganha automaticamente acesso a um modelo recém-comprado. A presença de um modelo no catálogo não prova que você tenha acesso à execução.

Para Codex ou Claude Code, o guia público orienta ativar na chave a opção de compatibilidade Codex / Claude Code.

## Uma solicitação HTTP mínima

Defina `RATE_CLOUD_API_KEY` no ambiente local usando o método de gerenciamento de segredo que preferir e execute:

```sh
curl --fail-with-body https://llm.rate-cloud.com/v1/chat/completions \
  -H "Authorization: Bearer $RATE_CLOUD_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"model":"glm-5.3","messages":[{"role":"user","content":"Reply with a short greeting."}]}'
```

A variável é um marcador para seu segredo local. Nunca coloque uma chave real em repositório público, captura de tela, mensagem de suporte ou configuração de cliente versionada. Use o endpoint do catálogo para verificar identificadores e depois envie uma solicitação pequena a um modelo ao qual sua conta e chave tenham acesso.

## Clientes de programação e outros aplicativos

O guia público de conexão abrange OpenCode, Codex, Claude Code, OpenClaw, Continue, Hermes e outros clientes compatíveis. O painel oferece comandos automáticos e exemplos de configuração manual para sistemas operacionais compatíveis.

A configuração do cliente depende da versão. Por exemplo, o guia oficial diferencia os formatos de configuração do OpenCode v1 e v2. Prefira as instruções atuais do painel a copiar um bloco de configuração antigo de um artigo de terceiros.

O cliente fornece a interface de editor ou terminal, ferramentas locais, conexões MCP, instruções do projeto e gerenciamento de conversas. Os recursos disponíveis do modelo dependem tanto do modelo escolhido quanto da integração. Um endpoint compatível não implica que todos os recursos de qualquer API proprietária estejam disponíveis.

## Solução de problemas sem expor segredos

Verifique a URL base e o identificador exato do modelo, a assinatura ou o teste ativo, as permissões de modelo da chave, a expiração, as restrições de IP e a opção de compatibilidade quando necessária. Se as solicitações se sobrepõem, considere o conjunto compartilhado de slots. Ao contatar o suporte, informe o horário e o identificador da solicitação, removendo cabeçalhos de autorização e conteúdo privado.

Fonte: [documentação de API e conexão da Rate Cloud](https://rate-cloud.com/docs), consultada em 3 de novembro de 2026. [Voltar ao índice](../README.md).
