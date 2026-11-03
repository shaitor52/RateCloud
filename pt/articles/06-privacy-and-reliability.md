# Privacidade, tratamento de dados e disponibilidade

A arquitetura pública da Rate Cloud distingue o conteúdo das solicitações, o estado temporário de computação, os metadados operacionais e os registros da conta ou de pagamentos. Essas categorias têm finalidades diferentes e regras próprias de retenção. Este artigo resume o projeto e as políticas publicados, não uma auditoria de segurança independente.

## Conteúdo das solicitações e buffers temporários

O serviço declara que não cria um histórico permanente do texto de prompts e respostas e não treina modelos com dados dos usuários. O conteúdo das solicitações é processado em memória temporária. Para buffers de aplicação acessíveis e gerenciados, a meta documentada de limpeza é de até cinco segundos após a entrega bem-sucedida e até trinta segundos após um erro final, cancelamento ou desconexão.

Essas metas para buffers de aplicação não devem ser generalizadas como garantia de que toda cópia física em todo acelerador seja apagada exatamente nesses prazos. A arquitetura pública reconhece uma fronteira de confiança separada para hardware alugado.

## Cache computacional isolado

O cache KV computacional tem prazo separado: até cinco minutos sem reutilização e idade absoluta máxima de quinze minutos. Entradas expiradas deixam de ser elegíveis para novos acertos de cache. Uma operação que já usa uma entrada pode terminar dentro do prazo; a memória é limpa após a liberação da última referência.

O cache documentado não é gravado em disco nem incluído em snapshots. A compatibilidade inclui conta, modelo, revisão dos pesos, quantização, tokenizador, template de conversa e instruções do sistema. O índice é protegido por HMAC, e o usuário não pode selecionar a área de cache de outra conta. Uma política de projeto pode especificar um perfil sem cache entre solicitações.

O histórico no lado do cliente é separado. Um editor, agente, bot ou aplicativo pode manter suas próprias conversas e arquivos conforme suas configurações.

## Metadados operacionais

A arquitetura pública descreve metadados como identificadores, modelo e perfil, horários, duração, uso, estado dos slots e códigos de erro. Os registros detalhados são removidos após trinta dias. Eles não incluem prompts, respostas, argumentos de ferramentas, arquivos nem tokens de autorização. Dados de conta, pagamentos e informações de suporte enviadas voluntariamente têm finalidades e prazos de retenção próprios.

“Não há histórico permanente de prompts” não significa “não há registros operacionais ou da conta”. Consulte a política de privacidade atual indicada no site para conhecer os detalhes legais aplicáveis.

## Limites de transporte e infraestrutura

A arquitetura descreve TLS para transporte externo, verificações de identidade e mTLS entre serviços, acesso conforme a necessidade operacional e separação de chaves, contas, projetos e escopos de cache. Segundo as regras documentadas, segredos de API e corpos das solicitações não devem entrar em logs ou backups.

Transporte protegido e computação protegida por hardware são garantias diferentes. O site não promete computação confidencial em todos os aceleradores. Um nó que perde o gerenciamento confiável é excluído, sua autoridade é revogada e seu retorno exige verificação e limpeza.

## Disponibilidade e trabalho interrompido

A disponibilidade contínua 24/7 de todos os modelos não é garantida. Antes do início da saída, a recuperação pode repetir uma operação em uma réplica compatível dentro do prazo original. Isso pode aumentar a latência. Depois que uma transmissão começa, uma interrupção deve continuar visível como operação incompleta, não como resposta falsamente concluída.

A regra de compensação publicada se aplica a uma indisponibilidade completa e contínua do sistema por mais de quatro horas, com respostas HTTP 503. Ela concede extensões de doze horas para uma assinatura de três dias, um dia para uma de sete dias e três dias para uma de trinta dias. Falhas de modelo individuais, respostas lentas, limites de concorrência e outros códigos de erro não são cobertos por essa regra específica. Os termos aplicáveis e os direitos obrigatórios do usuário prevalecem.

Ao relatar um incidente, informe o horário e os identificadores da operação. Não envie segredos de API nem conteúdo confidencial das solicitações.

Fonte: [Rate Cloud: tratamento de dados, segurança e disponibilidade](https://rate-cloud.com/how-it-works). Consulte os termos e a política de privacidade atuais indicados no [site oficial](https://rate-cloud.com/). Consulta: 3 de novembro de 2026. [Voltar ao índice](../README.md).
