# Velocidade e desempenho da Rate Cloud

A pergunta prática sobre desempenho é quanto tempo leva para receber um resultado útil para sua tarefa. Uma alta taxa de tokens durante a geração, por si só, não descreve toda a experiência: espera, processamento da entrada, tamanho da saída e recuperação também influenciam.

## Retrato de desempenho publicado

Os valores a seguir foram exibidos na página inicial da Rate Cloud em 3 de novembro de 2026. Essa é a data da consulta, não um período de medição estabelecido de forma independente.

| Modelo | Resposta completa típica, segundos | Tokens/s efetivos típicos, incluindo espera | Tokens/s efetivos de respostas rápidas, incluindo espera |
| --- | ---: | ---: | ---: |
| GLM 5.3 | 21,48 | 14,05 | 58,47 |
| GLM 5.3 Flash | 23,32 | 14,58 | 61,92 |
| DeepSeek V4 Pro | 15,67 | 25,83 | 127,84 |
| DeepSeek V4.1 Flash | 14,99 | 19,22 | 78,38 |
| Qwen 3.8 Max | 21,37 | 13,13 | 80,68 |

São observações publicadas do serviço, não tempos de resposta garantidos, benchmarks fixos de hardware nem comparação controlada com solicitações idênticas. A página inicial não informa o tamanho da amostra nem o intervalo completo de medição junto à tabela, portanto os valores não devem ser tratados como prova de disponibilidade sustentada ou de um SLA.

## O que significam as colunas

O tempo de resposta completa vai do envio da solicitação até o recebimento do resultado pronto. Inclui espera, processamento da entrada e geração da resposta.

O site descreve “típico” como o ponto médio dos resultados: metade termina mais rápido e metade mais devagar. As taxas efetivas de tokens incluem toda a solicitação e o tempo de espera. Elas não devem ser chamadas de velocidade pura de decodificação ou tempo até o primeiro token.

A coluna de respostas rápidas descreve as dez solicitações mais rápidas em cada cem. Ela mostra a faixa mais rápida da distribuição observada, sem prometer essa taxa para uma nova solicitação. Não derive o tamanho médio da saída multiplicando valores resumidos separadamente de latência e vazão.

## Por que sua tarefa pode demorar mais

Um documento longo exige mais processamento de entrada que uma pergunta breve. Uma resposta detalhada leva mais tempo para ser gerada que uma curta. Agentes que usam ferramentas podem precisar de várias chamadas para concluir uma tarefa. Carga atual, elegibilidade do perfil, prontidão da réplica e recuperação também podem afetar o tempo decorrido.

Um modelo anunciado para tarefas frequentes ou rápidas pode ter uma duração mediana observada maior que outro se a composição das solicitações observadas for diferente. A tabela, sozinha, não separa a velocidade do modelo da complexidade da solicitação, do tamanho da resposta ou do comportamento do usuário.

## Concorrência e vazão total

Quatro slots pagos permitem que operações independentes avancem ao mesmo tempo. Eles não deixam uma solicitação individual quatro vezes mais rápida. O paralelismo ajuda quando o trabalho pode ser dividido em tarefas independentes; uma cadeia sequencial de raciocínio ou ferramentas ainda precisa aguardar suas dependências.

Para uma avaliação prática, meça seu próprio tempo até obter um resultado útil, a correção da saída, solicitações incompletas, erros e a proporção de tarefas que exigem novas tentativas. Registre o modelo, o tamanho da entrada e da saída, a concorrência e o período de observação para manter os resultados interpretáveis.

Fonte: [tabela de desempenho e explicações publicadas pela Rate Cloud](https://rate-cloud.com/). Consulte também [a documentação de conexão](https://rate-cloud.com/docs). [Voltar ao índice](../README.md).

## Resultados públicos completos disponíveis e dados para download

A tabela acima contém os 15 resultados numéricos publicados na tabela de desempenho dos cinco modelos da página inicial no momento da consulta. Uma [cópia CSV](../../data/performance-2026-11-03.csv) preserva os IDs dos modelos, unidades, data da consulta e URL da fonte para reutilização. Nenhum novo benchmark foi realizado para criá-la.

| Item de evidência | Disponível nesta cópia? |
| --- | --- |
| Duração típica da resposta completa, todos os cinco modelos | Sim, tabela e CSV |
| Taxa efetiva típica de tokens incluindo espera, todos os cinco modelos | Sim, tabela e CSV |
| Taxa efetiva do decil mais rápido, todos os cinco modelos | Sim, tabela e CSV |
| Tempos brutos por solicitação, tamanho da amostra e intervalo observado | Não fornecidos junto à tabela pública |
| Tempo até o primeiro token, velocidade pura de decodificação e percentis de latência | Não fornecidos na tabela pública |
| Comparação controlada com a mesma carga de trabalho e provedores oficiais | Não disponível neste repositório |

A página inicial vincula a metodologia a `/docs#statistics`; na consulta, a documentação atual de conexão não expunha uma seção detalhada de estatísticas correspondente. Preservamos essa lacuna de evidência em vez de inventar resultados adicionais. Para a compensação de preços, consulte [comparação com APIs oficiais](08-cost-and-service-comparison.md).
