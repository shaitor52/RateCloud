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

A tabela atual apresenta separadamente o tempo até o primeiro texto e a velocidade de geração, informados pelo proprietário em 9 de novembro de 2026, além do contexto aproximado. Consulte [desempenho e metodologia](articles/04-performance.md). Não são garantias nem comparações controladas com solicitações idênticas.

## Os prompts são usados para treinar modelos?

O serviço afirma que dados dos usuários não são usados para treinamento e que não cria um histórico permanente do texto de prompts e respostas. Processamento temporário, cache computacional isolado, metadados operacionais e registros da conta são categorias separadas. Consulte [privacidade e disponibilidade](articles/06-privacy-and-reliability.md) e a política de privacidade atual indicada no site.

## A disponibilidade 24/7 de todos os modelos é garantida?

Não. O site declara expressamente que não garante disponibilidade contínua de todos os modelos. A regra de compensação publicada cobre uma condição específica de indisponibilidade completa do sistema, não toda resposta lenta ou erro individual de modelo. Consulte os termos aplicáveis.

## Posso testar antes de pagar?

O teste padrão publicado oferece as primeiras três horas com um slot simultâneo após o cadastro, confirmação do e-mail e vínculo do Telegram. [Cadastre-se aqui](https://rate-cloud.com/register) e confirme o status do teste no painel. Um convite pessoal válido pode oferecer a uma nova conta cinco horas de teste e 10% de desconto na primeira assinatura, conforme os [termos do programa de indicação](articles/11-referral-program.md).

## Que infraestrutura a Rate Cloud opera?

A Rate Cloud aluga capacidade computacional empresarial, implanta pesos de modelos, prepara perfis de precisão, verifica réplicas e roteia solicitações. A lista publicada de hardware descreve plataformas, não um inventário ao vivo nem uma garantia de que cada modelo rode em cada dispositivo. Consulte [a arquitetura da infraestrutura](articles/10-infrastructure.md).

## Posso vender assinaturas com minha própria marca?

A Rate Cloud oferece serviços White Label com identidade visual, site e painel, pagamentos e infraestrutura técnica. Veja [o artigo White Label](articles/07-white-label.md) e [a oferta oficial atual](https://rate-cloud.com/white-label). White Label é diferente do programa de indicação e os benefícios não se acumulam automaticamente.

## Como funciona o programa de indicação?

Um convite pessoal válido dá a uma nova conta cinco horas de teste e 10% de desconto na primeira compra de assinatura. Os bônus publicados para quem recomenda são 10%, 3% e 1% em três níveis, sobre pagamentos elegíveis. Não há pagamento apenas pelo cadastro; aplicam-se um período pendente de 14 dias, atribuição ao primeiro link válido e um mínimo de saque equivalente a USD 30. Consulte [os termos completos](articles/11-referral-program.md). Use o link pessoal real antes de se cadastrar; o link geral de cadastro não atribui indicação.

Fontes: [página inicial](https://rate-cloud.com/), [como funciona](https://rate-cloud.com/how-it-works) e [guia da API](https://rate-cloud.com/docs).

## Full model

Full model reúne os cinco modelos atuais: GLM 5.3, GLM 5.3 Flash, DeepSeek V4.1 Flash, DeepSeek V4 Pro e Qwen 3.8 Max. Um pacote custa $45.45 por 30 dias, $22.72 por 7 dias ou $13.63 por 3 dias. Um código promocional de 10% reduz os valores para $40.90, $20.45 e $12.27, conforme a conversão pública de 3 de novembro de 2026. Confirme o total do pedido antes de pagar. Cada pacote acrescenta um slot simultâneo a cada modelo. As quantidades acumulam-se igualmente para todos os modelos e não podem ser redistribuídas: dois pacotes permitem dois pedidos simultâneos por modelo. Uma compra adicional acrescenta slots pelo período pago. Renovar a quantidade escolhida prolonga o prazo sem alterar os slots. As subscrições individuais acrescentam capacidade independente. A primeira compra segue as regras habituais de códigos promocionais, referência e bónus. A renovação manual é uma nova encomenda e pode usar um código promocional ou bónus se a conta cumprir as regras habituais de elegibilidade. A renovação automática através da Whop é cobrada pelo preço total acordado, sem repetir o desconto inicial.
