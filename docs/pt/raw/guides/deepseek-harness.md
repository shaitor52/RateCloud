# Conectar o DeepSeek Harness à Rate Cloud

O DeepSeek Harness tem um formulário documentado **Custom model API** para gateways compatíveis com OpenAI. A Rate Cloud documenta um endpoint Chat Completions compatível com OpenAI. A configuração a seguir usa esse protocolo e IDs de modelo manuais.

**Documentação consultada:** 3 de novembro de 2026. O DeepSeek Harness se identifica como versão prévia para desenvolvedores, com mudanças incompatíveis. Este guia segue a documentação publicada da interface web e da Rate Cloud; é um mapeamento estático de compatibilidade, não uma integração testada ao vivo. Nenhuma instalação ou solicitação à API foi executada.

Referências oficiais: [guia de conexão da Rate Cloud](https://rate-cloud.com/docs), [repositório e aviso de versão prévia do DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness), [configuração de modelos do DeepSeek Harness](https://deepseek-harness.github.io/deepseek-harness/en/guide/providers), [início rápido do DeepSeek Harness](https://deepseek-harness.github.io/deepseek-harness/en/guide/quickstart) e [catálogo de configuração de plugins](https://deepseek-harness.github.io/deepseek-harness/en/reference/config-catalog).

## Limites de compatibilidade

A Rate Cloud documenta estes endpoints e IDs diretos de modelo:

| Finalidade | Valor |
| --- | --- |
| URL base | `https://llm.rate-cloud.com/v1` |
| Rota Chat Completions | `POST /v1/chat/completions` |
| GLM 5.3 | `glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` |

O Harness documenta provedores personalizados com URL base, protocolo, credencial e lista de modelos fornecidos pelo usuário. Para este endpoint, selecione **OpenAI Chat Completions**. Não selecione Responses nem Anthropic Messages neste exemplo. A documentação publicada não confirma um provedor Rate Cloud integrado ao Harness nem compatibilidade testada ao vivo.

## Prepare a conta e as permissões da chave

No painel da Rate Cloud, crie uma chave de API, permita o modelo que usará e confirme que a conta tem acesso de teste ou assinatura ativa para ele. A chave completa é exibida uma vez na criação. A presença do modelo no catálogo não prova que a chave pode chamá-lo.

## Adicione uma API de modelo personalizada na interface web

Este é um passo a passo apenas da interface. Não executa instalador nem envia solicitação ao modelo.

1. Inicie a interface web do Harness seguindo as etapas do README oficial. Este guia não reproduz comandos de instalação.
2. Abra **Settings → Models** e escolha **Add model provider**.
3. Altere o formulário para **Custom model API**.
4. Defina um ID de provedor em minúsculas, como `ratecloud`. O Harness documenta que esse ID é permanente porque sessões, padrões, solicitações e referências de credencial o utilizam.
5. Defina o nome de exibição como `Rate Cloud` e a URL base como `https://llm.rate-cloud.com/v1`.
6. Escolha **OpenAI Chat Completions** como protocolo da API.
7. Insira a chave da Rate Cloud no campo de credencial do formulário. O Harness documenta que chaves salvas são somente para gravação na interface; a credencial fica em `$DSH_HOME/.credentials.yaml` e as configurações mantêm uma referência à credencial. Não coloque a chave em repositório ou issue pública.
8. Adicione um modelo manualmente usando um dos IDs exatos da tabela. Dê a ele um nome de exibição claro. Deixe janela de contexto, saída máxima, entrada de imagem e opções de raciocínio sem definição, a menos que tenha valor ou capacidade verificados para aquele modelo.
9. Salve o provedor e selecione o modelo configurado no seletor para torná-lo o padrão de novas sessões.

É possível adicionar mais modelos ao mesmo provedor usando seus IDs exatos sem prefixo. Não acrescente um prefixo de cliente como `ratecloud/` ao ID informado nesse formulário de API personalizada.

## Descoberta opcional de modelos

O Harness pode buscar uma lista de modelos usando a URL, o protocolo e a credencial do provedor. Essa ação envia uma solicitação HTTP autenticada ao endpoint. A descoberta é opcional e não há garantia de que funcione com todos os formatos de listagem. Para configurar sem fazer uma solicitação, adicione os IDs manualmente conforme descrito. Nenhuma solicitação de descoberta foi feita ao preparar este guia.

## Solução de problemas

- **`MISSING_CREDENTIAL`:** confirme que uma chave foi salva para o provedor ou que a referência de credencial configurada está disponível.
- **`UNKNOWN_MODEL`:** adicione o ID ao provedor personalizado e depois selecione essa entrada. Use exatamente as minúsculas e a pontuação do ID.
- **HTTP 401:** verifique chave, expiração e permissão de modelo na Rate Cloud. A lista de modelos da interface não verifica acesso.
- **HTTP 404 ou rota incompatível:** use `https://llm.rate-cloud.com/v1` como URL base e selecione OpenAI Chat Completions. Não inclua `/chat/completions` na URL base.
- **A busca de modelos não retorna entradas:** o formato de listagem do endpoint pode não ser reconhecido pelo recurso de descoberta do Harness. Adicione o ID manualmente; uma descoberta malsucedida não prova que a inferência esteja indisponível.
- **Falha em chamadas de ferramenta, imagens ou raciocínio:** declarar esses recursos no Harness não testa nem cria suporte na API. Configure apenas recursos documentados para o modelo escolhido e confirmados por trabalho real de compatibilidade.
- **Os caminhos de configuração diferem:** o Harness está em versão prévia para desenvolvedores e pode mudar rapidamente. Use a página atual de configuração de modelos e o catálogo gerado de configuração de plugins para a versão instalada.

Nenhuma solicitação ao vivo foi feita, portanto autenticação do endpoint e comportamento dos recursos não foram verificados no próprio Harness.

Versão em russo: [Conectar o DeepSeek Harness à Rate Cloud](../../ru/guides/deepseek-harness.md). Voltar para [todos os guias em português](README.md).
