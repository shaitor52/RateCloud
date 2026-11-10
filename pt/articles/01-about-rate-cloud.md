# O que a Rate Cloud oferece

A Rate Cloud usa um modelo de compra simples: você paga pelo acesso a um modelo de IA escolhido durante um período definido e depois usa a API sem uma cota acumulada de tokens. Isso é especialmente útil quando um aplicativo faz muitas chamadas ao modelo e fica difícil prever uma conta baseada em tokens.

Um agente autônomo de programação pode ler um repositório, planejar uma mudança, editar arquivos, executar ferramentas, analisar erros e repetir o processo muitas vezes. Cada ciclo pode envolver uma nova solicitação e mais tokens de entrada e saída. O preço da assinatura da Rate Cloud não aumenta com a quantidade de tokens consumidos durante sua vigência.

## Tokens ilimitados e capacidade de processamento finita

Tokens ilimitados significa que a Rate Cloud não impõe uma cota diária, semanal ou mensal ao total de tokens de entrada e saída usados no período pago. Isso não significa que uma solicitação possa conter contexto ilimitado ou ser executada para sempre. Capacidade de contexto, prazos das operações, execução simultânea, limites de proteção, capacidade de hardware e disponibilidade do serviço continuam finitos.

O volume mensal real de processamento depende do modelo, do tamanho da entrada e da saída, da velocidade de resposta e do paralelismo disponível. Exemplos com centenas de milhões ou bilhões de tokens ilustram o princípio de preços; não prometem esse volume mensal de processamento.

## Quatro slots simultâneos por assinatura paga

Cada assinatura paga oferece quatro solicitações simultâneas para seu modelo. Um slot representa uma solicitação em processamento. Quando a operação termina, o slot fica disponível novamente. Não é um limite de quatro solicitações por dia ou mês.

Além disso, há um limite de frequência para toda a conta: 20 novas solicitações a LLM em qualquer janela móvel de 60 segundos. Ele é compartilhado entre todos os modelos, chaves de API, assinaturas, pacotes Full model e as duas origens do serviço. Assinaturas ou pacotes Full model adicionais aumentam os slots simultâneos descritos abaixo, mas não elevam esse limite de frequência. Uma resposta 429 por limite de frequência significa que a conta atingiu sua cota de solicitações na janela móvel. Uma resposta 429 por limite de slots significa que todos os slots simultâneos aplicáveis estão ocupados. São limites distintos.

Um desenvolvedor pode usar os quatro slots para um agente principal e três subagentes, quatro sessões de trabalho separadas ou tarefas independentes de automação. As chaves de API da mesma conta compartilham o conjunto de slots do modelo correspondente. Criar chaves adicionais não aumenta a capacidade.

É possível combinar assinaturas. Duas assinaturas do mesmo modelo oferecem oito slots para esse modelo. Assinaturas de modelos diferentes têm conjuntos separados: por exemplo, quatro slots de GLM e quatro de DeepSeek. O fluxo de trabalho deve enviar as solicitações ao modelo adequado para usar cada conjunto.

## Períodos de acesso e primeiros passos

O site oferece assinaturas de 3, 7 e 30 dias. Novos usuários podem testar os modelos nas primeiras três horas após o cadastro e as verificações necessárias de e-mail e Telegram, com um slot simultâneo. O teste e as assinaturas pagas têm condições diferentes.

Comece com uma tarefa representativa: um repositório em que você realmente trabalha, um documento típico ou um fluxo de automação real. Antes de escolher um modelo e o período da assinatura, avalie a resposta, o comportamento das ferramentas e o tempo total até obter um resultado útil.

## Onde o serviço se encaixa

A Rate Cloud pode ser a camada de modelos para agentes de programação, assistentes internos, bots, pipelines de extração de dados, fluxos de documentos e produtos próprios. Um cliente compatível oferece sua própria interface, ferramentas, instruções do projeto e histórico. Os recursos disponíveis que dependem do modelo são determinados pelo modelo escolhido e pela integração da API.

O serviço vende acesso à API. Conectar um aplicativo conhecido não transforma o modelo GLM, DeepSeek ou Qwen escolhido em um modelo próprio daquele aplicativo.

Fontes: [página inicial da Rate Cloud](https://rate-cloud.com/) e [como funciona](https://rate-cloud.com/how-it-works). Consulta: 3 de novembro de 2026. [Voltar ao índice](../README.md).

## Full model

Full model reúne os cinco modelos atuais: GLM 5.3, GLM 5.3 Flash, DeepSeek V4.1 Flash, DeepSeek V4 Pro e Qwen 3.8 Max.

Um pacote custa $45.45 por 30 dias, $22.72 por 7 dias ou $13.63 por 3 dias. Um código promocional de 10% reduz os valores para $40.90, $20.45 e $12.27, conforme a conversão pública de 3 de novembro de 2026. Confirme o total do pedido antes de pagar.

Cada pacote acrescenta um slot simultâneo a cada modelo. As quantidades acumulam-se igualmente para todos os modelos e não podem ser redistribuídas: dois pacotes permitem dois pedidos simultâneos por modelo. Uma compra adicional acrescenta slots pelo período pago. Renovar a quantidade escolhida prolonga o prazo sem alterar os slots. As subscrições individuais acrescentam capacidade independente. A primeira compra segue as regras habituais de códigos promocionais, referência e bónus. A renovação manual é uma nova encomenda e pode usar um código promocional ou bónus se a conta cumprir as regras habituais de elegibilidade. A renovação automática através da Whop é cobrada pelo preço total acordado, sem repetir o desconto inicial.
