# Rate Cloud: perguntas frequentes

[English](../FAQ.md) · [Русский](../ru/FAQ.md) · [Español](../es/FAQ.md) · Português · [Início](README.md)

As informações do produto refletem o site oficial em 3 de novembro de 2026. Antes de comprar, consulte o painel e os termos atuais.

## O que é a Rate Cloud?

A Rate Cloud oferece acesso por assinatura às APIs de GLM, DeepSeek e Qwen para desenvolvimento, agentes de IA, automação e aplicativos. A assinatura seleciona um modelo e um período de acesso, em vez de cobrar por milhão de tokens. Veja [a visão geral do serviço](articles/01-about-rate-cloud.md).

## Há limite de tokens?

Durante uma assinatura ativa, não há cota acumulada de tokens de entrada ou saída. Cada operação ainda tem capacidade finita de contexto, prazo e limitações técnicas. O volume real de processamento depende da velocidade, do tamanho das entradas e saídas, dos slots disponíveis e da disponibilidade do serviço.

## Quatro slots significam apenas quatro solicitações?

Não. Uma assinatura paga permite executar quatro solicitações ao mesmo tempo. Quando uma operação termina, libera seu slot para novos trabalhos. Várias chaves de API da mesma conta usam o conjunto compartilhado do modelo correspondente.

## Posso aumentar a capacidade paralela?

A oferta pública permite combinar assinaturas. Duas assinaturas do mesmo modelo oferecem oito slots para ele. Assinaturas de modelos diferentes têm conjuntos próprios.

## Quais modelos posso usar?

O catálogo publicado lista GLM 5.3, GLM 5.3 Flash, DeepSeek V4.1 Flash, DeepSeek V4 Pro e Qwen 3.8 Max. Consulte [o catálogo datado](articles/02-models.md) para ver IDs exatos da API, preços, usos previstos e entrada de imagens.

## Um modelo Flash é igual a um Pro?

Não. São opções distintas do catálogo. Perfis de precisão são variantes de execução do modelo escolhido; não autorizam a substituição silenciosa por outro modelo. Veja [roteamento e quantização](articles/03-routing-and-quantization.md).

## Como o roteamento inteligente escolhe um perfil de precisão?

O projeto publicado verifica os requisitos da tarefa e as réplicas elegíveis, prioriza qualidade em trabalhos difíceis ou incertos e considera o custo apenas entre rotas adequadas. Contexto, imagens, ferramentas, formato de saída, memória disponível, filas e estado da réplica influenciam a elegibilidade. O suporte ao perfil depende do modelo e do hardware específicos.

## A quantização garante respostas idênticas?

Não. A precisão numérica pode afetar a qualidade da saída. A arquitetura pública descreve validação em relação à versão de origem e critérios de qualidade específicos por tarefa. Um perfil econômico só é elegível quando sua qualidade é adequada. Quantização é diferente dos ajustes de esforço de raciocínio.

## Quais aplicativos podem se conectar?

O guia oficial cobre OpenCode, Codex, Claude Code, OpenClaw, Continue, Hermes e outros clientes compatíveis. Nossos [guias práticos](guides/README.md) cobrem configurações selecionadas. Os recursos dependem do cliente e do modelo; conectar o cliente não transforma o modelo escolhido em um modelo próprio do fornecedor do cliente.

## Qual URL base meu aplicativo deve usar?

A URL base geral compatível com OpenAI é `https://llm.rate-cloud.com/v1`. Alguns clientes têm URLs de compatibilidade dedicadas. Use a [documentação oficial](https://rate-cloud.com/docs) e o guia adequado, sem misturar famílias de endpoint.

## Por que um modelo listado pode rejeitar minha solicitação?

A presença no catálogo não comprova acesso à execução. Verifique teste ou assinatura ativa, permissões de modelo da chave, expiração, restrições de IP e configurações de compatibilidade do cliente. Confira também os slots ocupados e o erro retornado. Informe ao suporte o horário e o identificador da solicitação, sem enviar a chave nem conteúdo privado.

## Qual é a velocidade da Rate Cloud?

O site publica uma tabela histórica de desempenho. Ela mede a latência da solicitação completa e taxas efetivas de tokens que incluem a espera. Sua tarefa pode ser diferente. Consulte [desempenho e metodologia](articles/04-performance.md); os números não são um SLA garantido nem uma comparação controlada com prompts idênticos.

## Os prompts são usados para treinar modelos?

O serviço afirma que dados dos usuários não são usados para treinamento e que não cria um histórico permanente do texto de prompts e respostas. Processamento temporário, cache computacional isolado, metadados operacionais e registros da conta são categorias separadas. Consulte [privacidade e disponibilidade](articles/06-privacy-and-reliability.md) e a política de privacidade atual indicada no site.

## A disponibilidade 24/7 de todos os modelos é garantida?

Não. O site declara expressamente que não garante disponibilidade contínua de todos os modelos. A regra de compensação publicada cobre uma condição específica de indisponibilidade completa do sistema, não toda resposta lenta ou erro individual de modelo. Consulte os termos aplicáveis.

## Posso testar antes de pagar?

O teste inicial publicado oferece as primeiras três horas com um slot simultâneo após o cadastro e a confirmação de e-mail e Telegram. Confirme o status do teste no painel.

## Posso vender assinaturas com minha própria marca?

A Rate Cloud oferece serviços White Label com identidade visual, site e painel, pagamentos e infraestrutura técnica. Veja [o artigo White Label](articles/07-white-label.md) e [a oferta oficial atual](https://rate-cloud.com/white-label).

Fontes: [página inicial](https://rate-cloud.com/), [como funciona](https://rate-cloud.com/how-it-works) e [guia da API](https://rate-cloud.com/docs).
