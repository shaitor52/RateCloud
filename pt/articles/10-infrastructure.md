# Nossa infraestrutura: alugamos capacidade, implantamos modelos e operamos a inferência

[English](../../articles/10-infrastructure.md) · [Русский](../../ru/articles/10-infrastructure.md) · [Español](../../es/articles/10-infrastructure.md) · Português

**A Rate Cloud aluga capacidade computacional empresarial, implanta pesos de modelos e gerencia sua execução.** Nosso trabalho cobre a infraestrutura e o fluxo de inferência: escolher hardware e ambientes de execução compatíveis, preparar perfis de modelo, colocar réplicas em serviço, rotear solicitações e gerenciar recuperação.

Os clientes escolhem um modelo e conectam suas ferramentas pela API. A Rate Cloud opera a camada computacional por trás desse acesso. O hardware é alugado de proprietários empresariais; a propriedade do equipamento alugado e as responsabilidades operacionais do ambiente que executa os modelos são diferentes.

## O que a Rate Cloud gerencia

| Área | Nosso trabalho |
| --- | --- |
| Capacidade computacional | Alugar capacidade empresarial e combinar uma reserva estável com recursos adicionais disponíveis |
| Implantação de modelos | Posicionar pesos de modelo compatíveis e preparar o mecanismo de inferência para a versão selecionada |
| Perfis de precisão | Validar perfis elegíveis do formato original, de precisão mista ou quantizados do mesmo modelo |
| Prontidão de réplicas | Carregar os pesos, aquecer a execução, verificar a prontidão e admitir somente réplicas adequadas |
| Roteamento de solicitações | Considerar contexto, imagens, ferramentas, formato de saída, memória, fila e saúde da réplica |
| Operação e recuperação | Monitorar a execução, retirar réplicas não saudáveis e, quando possível, recuperar dentro do prazo original da operação |

Por isso, a descrição do serviço inclui posicionamento de pesos, ambientes de inferência, precisão e ciclo de vida de réplicas, além do endpoint de API. Essas responsabilidades operacionais são centrais na arquitetura pública.

## Famílias de hardware na arquitetura publicada

A arquitetura cita sistemas Huawei Atlas e aceleradores Ascend. São descrições públicas de plataformas, não um inventário ao vivo de todas as máquinas nem uma promessa de que todos os modelos funcionem em todos os dispositivos listados.

| Plataforma | Função publicada |
| --- | --- |
| Atlas 800I A2 | Inferência de modelos grandes; oito NPUs de 64 GB cada |
| Atlas 800I A3 | Inferência de modelos grandes; oito NPUs físicas de 128 GB cada, apresentadas como dezesseis dispositivos lógicos |
| Atlas 900 A2 PoD e A3 SuperPoD | Grupos de aceleradores distribuídos para execução de modelos grandes |
| Atlas 500 e 500 A2 | Tarefas de serviço menores |
| Atlas 800 com Atlas 300I Duo | Classe de compatibilidade separada, avaliada de forma independente |

As descrições físicas e lógicas do A3 referem-se à mesma memória e não devem ser somadas. A compatibilidade é verificada para cada combinação de modelo, formato de pesos, mecanismo e hardware. Cálculos fortemente acoplados usam uma rede local compatível; mover solicitações inteiras entre sites é uma operação distinta.

## Dos pesos do modelo a uma API utilizável

Uma réplica precisa da versão correta e de um ambiente de execução compatível, memória suficiente, recursos permitidos, aquecimento concluído e verificação de prontidão bem-sucedida. Hardware livre, por si só, não significa que haja um modelo disponível.

O roteador seleciona um perfil validado adequado do modelo solicitado pelo usuário. A qualidade tem prioridade para código difícil, matemática, ferramentas, esquemas estritos e solicitações incertas. Flash e Pro continuam sendo modelos diferentes. Consulte [roteamento e quantização](03-routing-and-quantization.md) para ver o processo de seleção.

Grupos estáveis dão suporte à carga básica e à recuperação. Recursos adicionais interrompíveis ampliam a capacidade disponível. Um aviso de revogação de recursos interrompe novas atribuições à réplica afetada. Antes do início da saída, a recuperação pode repetir a solicitação em uma réplica compatível dentro do prazo original. Uma transmissão interrompida deve continuar visivelmente incompleta.

## Por que isso viabiliza o acesso por assinatura

Operar conjuntamente capacidade computacional, perfis de modelo e roteamento permite à Rate Cloud controlar como os recursos adequados são utilizados. Os clientes pagam pelo acesso ao modelo e pela concorrência durante um período de assinatura, sem cota acumulada de tokens. O processamento permanece limitado pela velocidade do modelo, contexto, prazos de operação, slots e disponibilidade; isso não garante um volume mensal fixo nem serviço ininterrupto 24/7.

Este artigo descreve o modelo operacional público e as responsabilidades assumidas pela Rate Cloud. Ele não afirma que cada solicitação use um único caminho de execução exclusivo nem certifica o inventário atual de equipamentos. A arquitetura e os termos oficiais atuais continuam sendo a referência.

## Conheça o serviço

[Crie uma conta e teste a Rate Cloud](https://rate-cloud.com/register). O teste padrão de três horas exige confirmação do e-mail e vínculo do Telegram, e usa um slot simultâneo. Consulte [os benefícios por convite](11-referral-program.md) para conhecer as condições separadas de convites elegíveis.

Já tem uma conta? [Abra as instruções de conexão](https://rate-cloud.com/user/instructions). Quer criar um serviço com sua marca? [Conheça White Label](https://rate-cloud.com/en/white-label).

Fontes, consultadas em 3 de novembro de 2026: [como a Rate Cloud funciona](https://rate-cloud.com/how-it-works), [termos de serviço](https://rate-cloud.com/offer) e [acesso aos modelos](https://rate-cloud.com/). [Voltar à documentação](../README.md).
