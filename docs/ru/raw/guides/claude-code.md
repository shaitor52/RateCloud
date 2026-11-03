# Подключение Claude Code к Rate Cloud

Claude Code использует отдельный адрес совместимости Rate Cloud и имена моделей с префиксом клиента. Через Rate Cloud вы получаете API-доступ к GLM, DeepSeek или Qwen. Это не делает эти модели моделями Anthropic.

Официальные источники: [инструкция Rate Cloud](https://rate-cloud.com/docs) и [документация Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview).

## Создайте и подготовьте API-ключ

В кабинете Rate Cloud создайте ключ и скопируйте полный секрет при создании. Включите флажок **Поддержка Codex / Claude Code**. Разрешите ключу выбранную модель и проверьте, что у аккаунта есть пробный доступ или активная подписка на неё. Список моделей сам по себе не подтверждает доступ к их выполнению.

## Имена моделей для Claude Code

Claude Code использует префикс `ocx-claude-ratecloud--`, за которым следует точный ID модели. В прямом HTTP API используется ID без префикса.

| Модель | ID прямого API | Значение `ANTHROPIC_MODEL` для Claude Code |
| --- | --- | --- |
| GLM 5.3 | `glm-5.3` | `ocx-claude-ratecloud--glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` | `ocx-claude-ratecloud--glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` | `ocx-claude-ratecloud--deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` | `ocx-claude-ratecloud--deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` | `ocx-claude-ratecloud--qwen-3.8-max` |

## Запуск в macOS или Linux

В терминале Bash или zsh сначала прочитайте ключ без отображения символов. Затем задайте три переменные и запустите Claude Code из этого же терминала. Значения остаются в окружении оболочки, пока вы её не закроете или не удалите переменные.

```sh
# Bash
read -r -s -p 'API-ключ Rate Cloud: ' RATE_CLOUD_API_KEY
printf '\n'
```

```sh
# zsh
read -r -s 'RATE_CLOUD_API_KEY?API-ключ Rate Cloud: '
printf '\n'
```

В той же оболочке выполните:

```sh
export ANTHROPIC_BASE_URL='https://llm.rate-cloud.com/claude'
export ANTHROPIC_AUTH_TOKEN="$RATE_CLOUD_API_KEY"
export ANTHROPIC_MODEL='ocx-claude-ratecloud--glm-5.3'
claude
```

При необходимости замените значение модели на другое полное имя из таблицы. По завершении закройте терминал или выполните `unset RATE_CLOUD_API_KEY ANTHROPIC_AUTH_TOKEN ANTHROPIC_BASE_URL ANTHROPIC_MODEL`.

## Запуск в Windows PowerShell

Задайте переменные в том окне PowerShell, из которого запускаете Claude Code. `Read-Host` отображает вводимые символы. Для скрытого ввода используйте одобренное вами локальное средство хранения секретов.

```powershell
$env:RATE_CLOUD_API_KEY = Read-Host 'API-ключ Rate Cloud'
$env:ANTHROPIC_BASE_URL = 'https://llm.rate-cloud.com/claude'
$env:ANTHROPIC_AUTH_TOKEN = $env:RATE_CLOUD_API_KEY
$env:ANTHROPIC_MODEL = 'ocx-claude-ratecloud--glm-5.3'
claude
```

После выхода из Claude Code удалите переменные из текущей сессии PowerShell:

```powershell
Remove-Item Env:RATE_CLOUD_API_KEY, Env:ANTHROPIC_BASE_URL, Env:ANTHROPIC_AUTH_TOKEN, Env:ANTHROPIC_MODEL
```

## Если не работает

- **Ошибка авторизации или совместимости:** проверьте, что у ключа включена опция **Поддержка Codex / Claude Code**. Она обязательна для этого адреса совместимости.
- **Неизвестная модель:** укажите полное имя с префиксом `ocx-claude-ratecloud--` и точным суффиксом из таблицы. Не указывайте в `ANTHROPIC_MODEL` ID прямого HTTP API без префикса.
- **Нет доступа к модели:** проверьте пробный доступ или подписку, разрешённые модели ключа, его срок действия и список разрешённых IP в кабинете.
- **В терминале работает, из запуска приложения нет:** переменные из терминала наследуются программами, запущенными из этой оболочки. Запустите Claude Code из настроенного терминала либо используйте актуальную инструкцию кабинета для постоянной настройки клиента.
- **Нет соединения:** проверьте точный адрес `https://llm.rate-cloud.com/claude`. Это адрес совместимости Claude Code, а не общий адрес `/v1`.

Для поддержки укажите версию клиента, ОС, имя модели, время и текст ошибки. Сначала удалите API-секреты, заголовки авторизации и личное содержимое запросов.
