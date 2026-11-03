# Conectar o Claude Code à Rate Cloud

O Claude Code usa o endpoint dedicado de compatibilidade da Rate Cloud e nomes de modelo específicos do cliente. Isso é acesso por API a GLM, DeepSeek ou Qwen via Rate Cloud; não transforma esses modelos em modelos da Anthropic.

Referências oficiais: [guia de conexão da Rate Cloud](https://rate-cloud.com/docs) e [documentação do Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview).

## Crie e prepare uma chave de API

No painel da Rate Cloud, crie uma chave, copie o segredo completo ao criá-la e ative **Codex / Claude Code compatibility**. Permita o modelo que pretende usar e confirme que a conta tem teste ou assinatura ativa para ele. A lista de modelos não confirma acesso à execução.

## Nomes de modelos para Claude Code

O Claude Code usa o prefixo `ocx-claude-ratecloud--` seguido do ID exato do modelo. Isso difere da API HTTP direta, que usa o ID sem prefixo.

| Modelo | ID da API direta | `ANTHROPIC_MODEL` para Claude Code |
| --- | --- | --- |
| GLM 5.3 | `glm-5.3` | `ocx-claude-ratecloud--glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` | `ocx-claude-ratecloud--glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` | `ocx-claude-ratecloud--deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` | `ocx-claude-ratecloud--deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` | `ocx-claude-ratecloud--qwen-3.8-max` |

## Inicie no macOS ou Linux

Em um terminal Bash ou zsh, primeiro leia a chave sem exibi-la. Depois defina as três variáveis e inicie o Claude Code no mesmo terminal. Os valores permanecem no ambiente desse shell até que ele seja fechado ou as variáveis sejam removidas.

```sh
# Bash
read -r -s -p 'Rate Cloud API key: ' RATE_CLOUD_API_KEY
printf '\n'
```

```sh
# zsh
read -r -s 'RATE_CLOUD_API_KEY?Rate Cloud API key: '
printf '\n'
```

Continue no mesmo terminal:

```sh
export ANTHROPIC_BASE_URL='https://llm.rate-cloud.com/claude'
export ANTHROPIC_AUTH_TOKEN="$RATE_CLOUD_API_KEY"
export ANTHROPIC_MODEL='ocx-claude-ratecloud--glm-5.3'
claude
```

Se necessário, substitua o modelo por outro nome completo do Claude Code na tabela. Ao terminar, feche o terminal ou execute `unset RATE_CLOUD_API_KEY ANTHROPIC_AUTH_TOKEN ANTHROPIC_BASE_URL ANTHROPIC_MODEL`.

## Inicie no Windows PowerShell

Defina as variáveis na janela do PowerShell em que iniciará o Claude Code. `Read-Host` mostra os caracteres digitados; se precisar ocultar a entrada, use um gerenciador local de segredos aprovado por você.

```powershell
$env:RATE_CLOUD_API_KEY = Read-Host 'Rate Cloud API key'
$env:ANTHROPIC_BASE_URL = 'https://llm.rate-cloud.com/claude'
$env:ANTHROPIC_AUTH_TOKEN = $env:RATE_CLOUD_API_KEY
$env:ANTHROPIC_MODEL = 'ocx-claude-ratecloud--glm-5.3'
claude
```

Depois de fechar o Claude Code, remova os valores da sessão atual do PowerShell:

```powershell
Remove-Item Env:RATE_CLOUD_API_KEY, Env:ANTHROPIC_BASE_URL, Env:ANTHROPIC_AUTH_TOKEN, Env:ANTHROPIC_MODEL
```

## Solução de problemas

- **Erro de autenticação ou compatibilidade:** confira se a chave tem a opção **Codex / Claude Code compatibility** ativada. Ela é necessária para este endpoint.
- **Modelo desconhecido:** use o nome completo com `ocx-claude-ratecloud--` e o sufixo exato da tabela. Não use o ID HTTP sem prefixo em `ANTHROPIC_MODEL`.
- **Acesso ao modelo negado:** verifique teste ou assinatura ativa, permissões de modelo da chave, expiração e lista de IPs permitidos.
- **Funciona no terminal, mas não no inicializador de um aplicativo:** programas iniciados pelo terminal herdam as variáveis de ambiente dele. Inicie o Claude Code pelo shell configurado ou use a instrução atual do painel para configuração persistente.
- **Falha de conexão:** confirme que a URL base é exatamente `https://llm.rate-cloud.com/claude`; ela é a URL de compatibilidade do Claude Code, não o endpoint genérico `/v1`.

Ao pedir suporte, informe versão do cliente, sistema operacional, nome do modelo, horário e texto do erro. Remova antes segredos de API, cabeçalhos de autorização e conteúdo privado.
