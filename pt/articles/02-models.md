# Modelos e como escolher

O catálogo publicado da Rate Cloud contém cinco modelos. Cada um tem uma assinatura separada e um identificador exato para solicitações HTTP diretas. Escolha o modelo de acordo com o trabalho e teste entradas representativas.

## Catálogo publicado

| Modelo | ID da API direta | Foco principal | Entrada de imagem | Preço publicado por 30 dias |
| --- | --- | --- | --- | ---: |
| GLM 5.3 | `glm-5.3` | Desenvolvimento complexo e agentes autônomos | Não | $34,38 USD |
| GLM 5.3 Flash | `glm-5.3-flash` | Solicitações frequentes, programação diária, automação e subagentes | Sim | $30,16 USD |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` | Agentes de programação e tarefas paralelas de desenvolvimento | Sim | $30,16 USD |
| DeepSeek V4 Pro | `deepseek-v4-pro` | Raciocínio em várias etapas, arquitetura e revisão de código | Não | $27,56 USD |
| Qwen 3.8 Max | `qwen-3.8-max` | Grandes repositórios, documentos, pesquisa e contexto longo | Sim | $31,49 USD |

Os preços em USD e recursos acima refletem a exibição de moeda do site em 3 de novembro de 2026. Os preços podem mudar antes do pagamento; confira o painel antes de comprar. Cada assinatura paga listada inclui quatro solicitações simultâneas e não tem cota acumulada de tokens durante sua vigência. Entrada de imagem significa que o modelo aceita imagens; não significa geração de imagens.

## Escolha um modelo para seu fluxo de trabalho

GLM 5.3 é indicado para trabalho prolongado em projetos de software complexos, análise de repositórios, uso de ferramentas e coordenação de subagentes. GLM 5.3 Flash atende ao trabalho cotidiano repetido e à automação que exige muitas chamadas separadas.

DeepSeek V4.1 Flash é indicado para gerar e alterar código, agentes de programação e cargas com muitas tarefas de programação. DeepSeek V4 Pro enfatiza raciocínio e análise aprofundada, inclusive decisões de arquitetura e revisões em que a qualidade da resposta importa mais que a menor demora.

Qwen 3.8 Max é apresentado para grandes volumes de material, incluindo repositórios e documentos. A indicação de contexto longo não é uma especificação numérica da janela de contexto. Consulte a documentação atual e os limites reais das solicitações antes de projetar fluxos com entradas grandes.

Esses são casos de uso do produto, não uma classificação universal nem uma garantia de que um modelo seja melhor em todas as tarefas. Uma avaliação útil considera correção, cumprimento de instruções, comportamento de chamadas de ferramentas, requisitos de imagem, tempo de resposta e quantidade de correção manual necessária.

## Identidade do modelo e perfil de execução

Um modelo pode ter vários perfis de precisão aprovados. O roteador seleciona um perfil adequado do modelo solicitado pelo usuário. Escolher um perfil compacto de execução não significa substituir o modelo solicitado por outra opção do catálogo. Flash e Pro são modelos diferentes.

Use os IDs exatos da tabela para a API direta. Nomes específicos de clientes podem incluir um prefixo de provedor, que não faz parte do identificador HTTP direto. A presença de um modelo na lista de um cliente não prova, por si só, que a conta ou chave tenha permissão para executá-lo.

Fontes: [catálogo e preços](https://rate-cloud.com/), [IDs de modelos da API](https://rate-cloud.com/docs) e [perfis de modelo](https://rate-cloud.com/how-it-works). [Voltar ao índice](../README.md).
