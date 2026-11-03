# Como funcionam o roteamento inteligente e a quantização

A arquitetura pública da Rate Cloud descreve uma combinação de capacidade computacional estável, capacidade empresarial adicional disponível, perfis de precisão aprovados para os modelos e roteamento atento a cada solicitação. O objetivo é usar os recursos com eficiência e preservar a identidade e os requisitos funcionais do modelo escolhido.

Este artigo explica a arquitetura publicada. Não é uma verificação independente de cada implantação de produção nem uma promessa de disponibilidade contínua de toda combinação de hardware e precisão.

## Capacidade computacional e réplicas do modelo

O serviço descreve o aluguel de capacidade ociosa de proprietários de clusters empresariais, além de uma reserva estável. A Rate Cloud gerencia a alocação dos pesos do modelo, os mecanismos de inferência, os perfis de precisão e a distribuição das solicitações.

A arquitetura cita sistemas Huawei Atlas e aceleradores Ascend, incluindo Atlas 800I A2 e A3 para modelos grandes e Atlas 900 A2 PoD e A3 SuperPoD para grupos distribuídos. A compatibilidade do hardware é avaliada para cada modelo. Mover uma solicitação entre sites é diferente de dividir cálculos fortemente acoplados do modelo entre sites arbitrários: o cálculo fortemente acoplado de uma réplica usa uma rede local compatível.

Uma réplica utilizável exige mais que memória disponível. Ela precisa de pesos compatíveis, suporte ao ambiente de execução e aos recursos necessários da API, estado carregado, aquecimento e uma verificação de prontidão bem-sucedida.

## O que a quantização altera

Os parâmetros do modelo e os cálculos intermediários podem usar formatos numéricos diferentes. Formatos mais compactos reduzem os requisitos de memória e podem mudar a eficiência de execução, mas também podem afetar a qualidade da saída. Por isso, a precisão reduzida precisa ser avaliada em relação à versão de origem pertinente e aos tipos de tarefa.

O projeto publicado usa perfis de qualidade, equilibrado e econômico do mesmo modelo. Um perfil de qualidade pode usar o formato original validado, W8A8 ou outra configuração aprovada. Um perfil equilibrado pode combinar componentes com precisões diferentes, como 4 e 8 bits. Uma média efetiva próxima de 6 bits não implica uma implementação INT6 universal. Perfis econômicos podem usar configurações validadas W4A16, W4A8 ou MXFP4 quando o modelo e o hardware forem compatíveis.

A disponibilidade de um formato depende da versão do modelo, hardware, ambiente de execução e verificações de qualidade. Ele não é oferecido indiscriminadamente para todos os modelos. Aumentar a precisão nominal de pesos já quantizados não recupera informações perdidas na quantização anterior.

## Verificações de qualidade antes do roteamento

Os perfis são avaliados em relação à versão exata do modelo de origem com tarefas públicas, sintéticas e preparadas especificamente sobre código, matemática, contexto longo, ferramentas e JSON estrito. O processo publicado considera a qualidade das respostas, o consumo de memória, a velocidade e o comportamento da API. Conversas de usuários não são usadas para treinar ou calibrar modelos.

Um perfil compacto só é elegível para tarefas que consegue executar adequadamente. Código difícil, matemática, fluxos com ferramentas, esquemas estritos e solicitações incertas priorizam a qualidade. Uma solicitação curta também pode descrever um problema difícil. Alterar `reasoning_effort` é um controle separado e não deve ser apresentado como efeito da quantização.

## Como o roteador escolhe

O roteador considera requisitos de contexto, imagens, ferramentas e formato de saída, complexidade da tarefa, memória disponível, estado da fila e da réplica e o período restante de alocação de recursos. Primeiro determina as rotas adequadas; depois considera o custo entre essas opções.

O modelo escolhido permanece fixo. A operação também fixa a revisão de pesos aplicável e os recursos permitidos. Servidores incompatíveis são excluídos antes da atribuição. Se não houver capacidade adequada, o sistema pode aguardar dentro do orçamento interno ou retornar um erro explícito de indisponibilidade temporária, em vez de substituir silenciosamente o modelo por outro.

## Ciclo de vida da solicitação

1. Estabelecer a conexão protegida e validar a chave de API, a assinatura e a disponibilidade de um slot.
2. Determinar os requisitos da solicitação e escolher um perfil elegível do modelo solicitado.
3. Atribuir uma réplica pronta e compatível e iniciar a execução.
4. Entregar a resposta, liberar o slot e limpar o conteúdo temporário conforme as regras de tratamento de dados.

Uma operação lógica tem um `request_id`; cada tentativa computacional tem um `attempt_id`. Antes de começar a saída, a recuperação pode repetir a operação em uma réplica compatível dentro do prazo total original. Isso pode aumentar a latência.

Depois que a transmissão começa, o prefixo de uma geração não deve ser unido à continuação de uma nova geração. Uma transmissão interrompida está incompleta e o cliente deve tratá-la como tal.

## Recursos estáveis e interrompíveis

Grupos estáveis sustentam a carga básica e a recuperação. Grupos interrompíveis adicionais ampliam a capacidade. Uma réplica que recebe um aviso de revogação de recursos deixa de aceitar novas operações. A perda de um acelerador crítico torna indisponível a réplica que depende dele. Grupos de falha independentes reduzem o impacto de uma única falha, mas o projeto de recuperação não garante disponibilidade contínua de todos os modelos.

Fonte: [Rate Cloud: como funciona](https://rate-cloud.com/how-it-works), consultada em 3 de novembro de 2026. [Voltar ao índice](../README.md).
