# Доступ через HTTP и Python

Rate Cloud предоставляет OpenAI-совместимый API для программ с настройкой собственного базового адреса, а также пример прямого вызова через стандартную библиотеку Python. Примеры не устанавливают пакеты и не отправляют запросы, пока вы сами их не запустите.

Официальный источник: [документация API и подключения Rate Cloud](https://rate-cloud.com/docs).

## Адреса API

| Назначение | Метод и адрес |
| --- | --- |
| Базовый адрес OpenAI-совместимого API | `https://llm.rate-cloud.com/v1` |
| Список моделей | `GET https://llm.rate-cloud.com/v1/models` |
| Chat completions | `POST https://llm.rate-cloud.com/v1/chat/completions` |
| Responses API | `POST https://llm.rate-cloud.com/v1/responses` |

Для запросов `/v1` передавайте `Authorization: Bearer <API-ключ>`. Указывайте точный ID модели из таблицы:

| Модель | ID прямого API |
| --- | --- |
| GLM 5.3 | `glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` |

Не добавляйте к ID прямого HTTP API префикс провайдера, например `ratecloud/`. Форматы `ratecloud/` и `ocx-claude-ratecloud--` применяются в отдельных клиентских интеграциях.

## Переменная окружения

В macOS или Linux используйте вариант для своей оболочки. Оба фрагмента читают секрет без отображения символов. Переменная удаляется после команды `unset` или закрытия терминала.

```sh
# Bash
read -r -s -p 'API-ключ Rate Cloud: ' RATE_CLOUD_API_KEY
printf '\n'
export RATE_CLOUD_API_KEY
```

```sh
# zsh (оболочка по умолчанию в macOS)
read -r -s 'RATE_CLOUD_API_KEY?API-ключ Rate Cloud: '
printf '\n'
export RATE_CLOUD_API_KEY
```

В Windows PowerShell задайте `$env:RATE_CLOUD_API_KEY` в сессии, где запускаете программу. Не добавляйте настоящий ключ в исходный код, коммитимый файл `.env` или публичное обращение.

## Необязательная проверка через curl

Команда отправляет простой запрос к каталогу моделей. Она проверяет, что адрес отвечает и ключ принят, но не подтверждает подписку или разрешение ключа на конкретную модель.

```sh
curl --fail-with-body 'https://llm.rate-cloud.com/v1/models' \
  -H "Authorization: Bearer $RATE_CLOUD_API_KEY"
```

## Пример для Python 3 без сторонних библиотек

Сохраните этот код в локальный файл `.py`. Он использует только стандартную библиотеку Python (`urllib.request`), читает секрет из окружения и отправляет один небольшой запрос chat completions при запуске. При необходимости замените `MODEL` на другой точный ID прямого API.

```python
import json
import os
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

BASE_URL = "https://llm.rate-cloud.com/v1"
MODEL = "glm-5.3"
API_KEY = os.environ.get("RATE_CLOUD_API_KEY")

if not API_KEY:
    sys.exit("Set RATE_CLOUD_API_KEY in the environment before running this script.")

payload = {
    "model": MODEL,
    "messages": [
        {"role": "user", "content": "Reply with a short greeting."}
    ],
}
request = Request(
    f"{BASE_URL}/chat/completions",
    data=json.dumps(payload).encode("utf-8"),
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    },
    method="POST",
)

try:
    with urlopen(request, timeout=60) as response:
        result = json.load(response)
    print(result["choices"][0]["message"]["content"])
except HTTPError as error:
    # Avoid printing request headers or the API key in diagnostics.
    print(f"HTTP error: {error.code} {error.reason}", file=sys.stderr)
    sys.exit(1)
except URLError as error:
    print(f"Connection error: {error.reason}", file=sys.stderr)
    sys.exit(1)
except (KeyError, IndexError, json.JSONDecodeError) as error:
    print(f"Unexpected response format: {error}", file=sys.stderr)
    sys.exit(1)
```

Запускайте его из оболочки, где задан `RATE_CLOUD_API_KEY`. Не выводите полный ответ в общие журналы, если запросы или ответы могут содержать личные данные.

## Если не работает

- **401 или ошибка авторизации:** проверьте, что переменная окружения доступна процессу, ключ активен и не истёк, а заголовок содержит `Bearer` перед ключом.
- **403 или отказ в доступе:** проверьте пробный доступ или подписку на модель, разрешения ключа, IP-ограничения и флажок совместимости, если используете специальный клиентский адрес.
- **404 или модель не найдена:** проверьте путь и точное написание ID модели. Для этих примеров нужен `/v1`, а не адрес совместимости Codex или Claude Code.
- **Модель есть в каталоге, но генерация запрещена:** каталог не подтверждает разрешения аккаунта или ключа. Проверьте подписку и доступ ключа в кабинете.
- **Тайм-аут или неполный ответ:** проверьте состояние запроса перед повтором. Тайм-аут не доказывает, что операция завершилась. Не повторяйте вслепую запросы, которые запускают побочные действия в вашем приложении.

При обращении в поддержку сообщите время, ID модели, путь API, HTTP-статус и идентификатор запроса, если он есть. Удалите API-ключи, заголовки авторизации и личное содержимое запросов и ответов.
