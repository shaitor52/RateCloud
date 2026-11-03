# Rate Cloud versus APIs oficiais: custo fixo para trabalho contínuo

English · [Русский](../../ru/articles/08-cost-and-service-comparison.md) · [Español](../../es/articles/08-cost-and-service-comparison.md) · Português

**A vantagem da Rate Cloud é o preço fixo da assinatura, sem cota acumulada de tokens. Conforme o uso aumenta, o preço da assinatura do modelo continua igual.** Uma API por consumo cobra cada token faturável. Isso pode tornar programação, análise e automação contínuas muito mais baratas na Rate Cloud, desde que a carga de trabalho se ajuste à velocidade, concorrência, recursos e disponibilidade do serviço.

A Rate Cloud não é automaticamente mais barata para uso leve. Os provedores oficiais oferecem descontos úteis de cache, lote, horários fora de pico e outros. Esta comparação explicita essas compensações. Verificado em 3 de novembro de 2026; não é promessa de preços futuros.

## Tarifas oficiais de API e assinaturas da Rate Cloud

As tarifas de API são por um milhão de tokens. As tarifas de entrada desta tabela são **sem cache**. Os preços da Rate Cloud estão em USD por 30 dias para uma assinatura de modelo com quatro slots. Eles refletem a exibição de moeda do site consultada em 3 de novembro de 2026 e podem mudar antes do pagamento.

| API oficial e condição de cobrança | Entrada USD/M | Saída USD/M | Modelo Rate Cloud / USD por 30 dias |
| --- | ---: | ---: | --- |
| Z.ai GLM-5.3 | 1,40 | 4,40 | GLM 5.3 / 34,38 |
| Z.ai GLM-5.3-Flash | 0,15 | 0,50 | GLM 5.3 Flash / 30,16 |
| DeepSeek V4.1 Flash, fora de pico | 0,15 | 0,60 | DeepSeek V4.1 Flash / 30,16 |
| DeepSeek V4.1 Flash, pico | 0,30 | 1,20 | DeepSeek V4.1 Flash / 30,16 |
| DeepSeek V4 Pro, fora de pico | 0,66 | 1,98 | DeepSeek V4 Pro / 27,56 |
| DeepSeek V4 Pro, pico | 1,32 | 3,96 | DeepSeek V4 Pro / 27,56 |
| QwenCloud Qwen3.8-Max, endpoint de Singapura | 2,00 | 6,00 | Qwen 3.8 Max / 31,49 |
| OpenAI GPT-6.1 Sol, Standard e contexto curto | 2,00 | 10,00 | Alternativa de outro modelo; GPT não é vendido aqui |

Fontes: [preços da Z.ai](https://docs.z.ai/guides/overview/pricing), [preços e faixas horárias da DeepSeek](https://api-docs.deepseek.com/quick_start/pricing/), [preços do modelo QwenCloud e endpoint de Singapura](https://www.qwencloud.com/models/qwen3.8-max), [preços do GPT-6.1 Sol](https://developers.openai.com/api/docs/models/gpt-6.1-sol) e [catálogo da Rate Cloud](https://rate-cloud.com/).

O nome oficial da API DeepSeek Flash é `deepseek-flash` para a versão V4.1-Flash-1017; a Rate Cloud usa `deepseek-v4.1-flash`. Os horários de pico da DeepSeek são 01:00-04:00 e 06:00-10:00 UTC, de segunda a sexta-feira, exceto feriados públicos chineses; os demais horários são fora de pico. As linhas de GLM e DeepSeek comparam versões correspondentes. Qwen compartilha o rótulo da família do produto; os recursos hospedados e perfis de execução podem diferir. GPT é uma alternativa para trabalho semelhante, não tem pesos, recursos ou qualidade de saída idênticos.

## Quanto custa o uso repetido

Considere o total de tokens faturados como 80% de entrada e 20% de saída, sem acertos de cache, ferramentas, lote, impostos, descontos especiais ou sobretaxa de contexto longo. Quando aplicável, tokens de raciocínio devem ser incluídos na saída faturável. Estes são **cenários aritméticos de carga de trabalho**, não uso real de clientes nem uma quantidade que a Rate Cloud garanta processar em 30 dias.

| API oficial | 10M de tokens totais | 100M | 500M | 1 bilhão |
| --- | ---: | ---: | ---: | ---: |
| GLM-5.3 | $20 | $200 | $1 000 | $2 000 |
| GLM-5.3-Flash | $2,20 | $22 | $110 | $220 |
| DeepSeek Flash fora de pico / pico | $2,40 / $4,80 | $24 / $48 | $120 / $240 | $240 / $480 |
| DeepSeek Pro fora de pico / pico | $9,24 / $18,48 | $92,40 / $184,80 | $462 / $924 | $924 / $1 848 |
| Qwen3.8-Max | $28 | $280 | $1 400 | $2 800 |
| GPT-6.1 Sol Standard | $36 | $360 | $1 800 | $3 600 |

**Os preços publicados em USD das assinaturas de modelo da Rate Cloud por 30 dias permanecem entre $27,56 e $34,38 nesses cenários de volume.** Isso descreve a estrutura de preços, não garante a conclusão de um bilhão de tokens. Várias assinaturas, slots adicionais, hospedagem do cliente, serviços de busca na web, computação de CI e outras ferramentas do aplicativo podem acrescentar custos.

## Ponto de equilíbrio em vez de uma alegação universal de economia

Com preços em USD, 500 milhões de tokens sem cache custam $1 000 na API oficial GLM-5.3, contra $34,38 por uma assinatura GLM da Rate Cloud: cerca de 29,1 vezes o custo de acesso ao modelo. Na API econômica DeepSeek Flash fora de pico, a mesma conta resulta em $120 contra $30,16: cerca de 4,0 vezes. Os preços da Rate Cloud refletem a exibição em USD do site consultada em 3 de novembro de 2026 e podem mudar antes do pagamento.

Com esses preços, o volume de equilíbrio sem cache é de cerca de 17,19 milhões de tokens para GLM-5.3, 137,09 milhões para GLM Flash, 125,67 milhões para DeepSeek Flash fora de pico, 29,83 milhões para DeepSeek Pro fora de pico e 11,25 milhões para Qwen. Abaixo do limite correspondente, a conta por tokens do provedor oficial pode ser menor. Uma parcela alta de acertos de cache eleva esses limites.

Fórmula geral, com o volume em milhões:

```text
weighted USD per million = input_fraction * input_price + output_fraction * output_price
break_even_millions = subscription_USD / weighted_USD_per_million
```

Exemplo de sensibilidade com todos os tokens de entrada em cache para DeepSeek Flash fora de pico: a $0,003 de entrada e $0,60 de saída, 500M em 80/20 custam $61,20, não $120. Comparados aos $30,16 da assinatura DeepSeek Flash da Rate Cloud, são cerca de 2,0 vezes o custo. A elegibilidade real ao cache não é garantida, e gravações de cache ou outras tarifas podem importar. Qwen, Z.ai e OpenAI também publicam descontos de cache; a OpenAI oferece tarifas menores de Batch/Flex e cobra mais por modos de contexto longo/Fast. Compare a tarifa específica que você usaria.

Reproduza cenários offline com os [dados de preços datados](../../data/pricing-2026-11-03.json) e a [calculadora](../../tools/compare_costs.py):

```sh
python3 tools/compare_costs.py --million-tokens 500
python3 tools/compare_costs.py --million-tokens 500 --cached-input-share 1
```

Execute a partir da raiz do repositório. Nenhuma chamada de API é feita. Os valores da assinatura são o snapshot de exibição em USD indicado acima, não uma cotação para compras futuras.

## Velocidade e compensações do serviço

Escolha a Rate Cloud quando o custo previsível para trabalho contínuo for mais importante que minimizar a latência de cada resposta. Um provedor direto ou plano premium de velocidade pode ser mais adequado se seus próprios testes indicarem latência menor ou se você precisar de recursos hospedados, concorrência muito maior ou termos contratuais. Quatro slots da Rate Cloud não equivalem às franquias de concorrência das APIs oficiais.

Este repositório **não** contém um benchmark de velocidade controlado com o mesmo prompt e o mesmo nível de esforço em todos esses serviços. Portanto, não publicamos tokens por segundo inventados para concorrentes nem afirmamos uma classificação universal de velocidade medida. O retrato completo de velocidade publicado pela Rate Cloud está em [desempenho](04-performance.md). Ele inclui a espera e difere da velocidade pura de geração de tokens. Esta comparação reconhece explicitamente as compensações de latência e capacidade, sem apresentá-las como resultado de uma comparação direta estabelecida.

Assinaturas oficiais de programação e aplicativos gratuitos de chat são produtos diferentes do acesso a API cobrado por uso. Esta tabela compara as APIs listadas, não todos os planos de cada provedor. Avalie qualidade e recursos além do preço.

[Casos em que uma conta fixa de tokens ajuda](09-unlimited-use-cases.md) · [Voltar ao índice](../README.md)
