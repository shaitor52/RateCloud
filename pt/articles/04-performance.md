# Velocidade e desempenho da Rate Cloud

A pergunta prática sobre desempenho é quanto tempo leva para receber um resultado útil para sua tarefa. Uma alta taxa de tokens durante a geração, por si só, não descreve toda a experiência: espera, processamento da entrada, tamanho da saída e recuperação também influenciam.

## Dados atuais de desempenho

Os valores foram informados pelo proprietário em 9 de novembro de 2026. O tempo até o primeiro texto e a velocidade de geração são métricas distintas. O contexto de entrada é de aproximadamente 200.000 tokens; os resultados dependem da carga de trabalho.

| Modelo | Tempo até o primeiro texto (s) | Geração da resposta (tokens/s) |
| --- | ---: | ---: |
| GLM 5.3 | 15,6 | 52,7 |
| GLM 5.3 Flash | 18,9 | 50,7 |
| DeepSeek V4.1 Flash | 11,2 | 150,8 |
| DeepSeek V4 Pro | 10,0 | 142,6 |
| Qwen 3.8 Max | 13,0-13,5 | 59,0-63,4 |

[Dados atuais de desempenho em CSV](../../data/performance-2026-11-09.csv). Os intervalos do Qwen abrangem duas execuções.

O [CSV de 3 de novembro](../../data/performance-2026-11-03.csv) foi mantido como dado histórico.

## Por que sua tarefa pode demorar mais

Um documento longo exige mais processamento de entrada que uma pergunta breve. Uma resposta detalhada leva mais tempo para ser gerada que uma curta. Agentes que usam ferramentas podem precisar de várias chamadas para concluir uma tarefa. Carga atual, elegibilidade do perfil, prontidão da réplica e recuperação também podem afetar o tempo decorrido.

## Concorrência e vazão total

Quatro slots pagos permitem que operações independentes avancem ao mesmo tempo. Eles não deixam uma solicitação individual quatro vezes mais rápida. O paralelismo ajuda quando o trabalho pode ser dividido em tarefas independentes; uma cadeia sequencial de raciocínio ou ferramentas ainda precisa aguardar suas dependências.

Para uma avaliação prática, meça seu próprio tempo até obter um resultado útil, a correção da saída, solicitações incompletas, erros e a proporção de tarefas que exigem novas tentativas. Registre o modelo, o tamanho da entrada e da saída, a concorrência e o período de observação para manter os resultados interpretáveis.

Fonte: [tabela de desempenho e explicações publicadas pela Rate Cloud](https://rate-cloud.com/). Consulte também [a documentação de conexão](https://rate-cloud.com/docs). [Voltar ao índice](../README.md).
