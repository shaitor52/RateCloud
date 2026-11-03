# Подключение Continue к Rate Cloud

Continue подключается к OpenAI-совместимым моделям через провайдера OpenAI и пользовательское поле `apiBase`. В этом руководстве используется актуальный формат `config.yaml`, а ключ хранится в локальном файле секретов Continue, а не в YAML.

**Документация проверена:** 3 ноября 2026 года. Это статический пример по документации, а не живой запрос через Continue или аккаунт Rate Cloud. Актуальная документация Continue рекомендует YAML; `config.json` считается устаревшим. В просмотренных инструкциях не указана минимальная версия клиента для этой конфигурации. Если ваша версия не принимает поле, сверьтесь с актуальной схемой по ссылке ниже.

Официальные источники: [инструкция Rate Cloud](https://rate-cloud.com/docs), [настройка OpenAI-совместимых моделей Continue](https://docs.continue.dev/customize/model-providers/top-level/openai), [справочник YAML Continue](https://docs.continue.dev/reference), [FAQ о секретах Continue](https://docs.continue.dev/faqs) и [пути конфигурации Continue](https://docs.continue.dev/guides/understanding-configs).

## Проверьте доступ и ID моделей

Создайте API-ключ Rate Cloud, разрешите нужные модели и проверьте пробный доступ или активную подписку. Полный секрет показывается при создании. Наличие модели в списке Continue само по себе не предоставляет доступ.

Базовый адрес OpenAI-совместимого API Rate Cloud: `https://llm.rate-cloud.com/v1`. Используйте точные ID моделей. Continue покажет название из поля `name`; префикс `ratecloud/`, который нужен некоторым другим клиентам, здесь не используется.

| Модель | ID прямого API |
| --- | --- |
| GLM 5.3 | `glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` |

## Сохраните секрет для расширения IDE

Расширения Continue для IDE разрешают `${{ secrets.ИМЯ }}` из файлов `.env`. В документации указан такой порядок поиска: `.env` в рабочей области, `.continue/.env` в ней же, затем глобальный `~/.continue/.env`. Документация предупреждает, что расширения IDE напрямую не наследуют переменные окружения из терминала.

Создайте или измените глобальный файл `~/.continue/.env` (Windows: `%USERPROFILE%\.continue\.env`) и добавьте локально:

```dotenv
RATE_CLOUD_API_KEY=<ваш-ключ>
```

Не коммитьте этот файл. Не вставляйте настоящий ключ в `config.yaml` и не передавайте файл `.env` другим. Согласно документации Continue, CLI также может получить секрет из окружения процесса.

## Настройте локальный YAML Continue

Локальный конфиг Continue находится в `~/.continue/config.yaml` в macOS/Linux и `%USERPROFILE%\.continue\config.yaml` в Windows. Откройте его через селектор конфигураций и значок шестерёнки в боковой панели Continue. Сохраните существующие настройки, не связанные с моделями. Добавьте запись для каждой нужной модели; в этом примере указаны все пять:

```yaml
name: Rate Cloud
version: 1.0.0
schema: v1
models:
  - name: Rate Cloud - GLM 5.3
    provider: openai
    model: glm-5.3
    apiBase: https://llm.rate-cloud.com/v1
    apiKey: ${{ secrets.RATE_CLOUD_API_KEY }}
    useResponsesApi: false
    roles: [chat, edit, apply]
  - name: Rate Cloud - GLM 5.3 Flash
    provider: openai
    model: glm-5.3-flash
    apiBase: https://llm.rate-cloud.com/v1
    apiKey: ${{ secrets.RATE_CLOUD_API_KEY }}
    useResponsesApi: false
    roles: [chat, edit, apply]
  - name: Rate Cloud - DeepSeek V4.1 Flash
    provider: openai
    model: deepseek-v4.1-flash
    apiBase: https://llm.rate-cloud.com/v1
    apiKey: ${{ secrets.RATE_CLOUD_API_KEY }}
    useResponsesApi: false
    roles: [chat, edit, apply]
  - name: Rate Cloud - DeepSeek V4 Pro
    provider: openai
    model: deepseek-v4-pro
    apiBase: https://llm.rate-cloud.com/v1
    apiKey: ${{ secrets.RATE_CLOUD_API_KEY }}
    useResponsesApi: false
    roles: [chat, edit, apply]
  - name: Rate Cloud - Qwen 3.8 Max
    provider: openai
    model: qwen-3.8-max
    apiBase: https://llm.rate-cloud.com/v1
    apiKey: ${{ secrets.RATE_CLOUD_API_KEY }}
    useResponsesApi: false
    roles: [chat, edit, apply]
```

`useResponsesApi: false` выбирает документированный маршрут Chat Completions. Для моделей перечислены роли чата, редактирования и применения изменений. Это руководство не включает возможность инструментов/Agent: она зависит от фактической поддержки вызовов инструментов моделью и API. Указывайте её только после проверки.

Сохраните конфиг. Согласно актуальному руководству Continue, изменения загружаются автоматически. Выберите модель Rate Cloud в списке моделей. Для проверки статической конфигурации и появления записи в списке не требуется выполнять запрос к модели.

## Если не работает

- **Ключ не находится:** проверьте точное имя `RATE_CLOUD_API_KEY` и наличие ключа в одном из поддерживаемых файлов `.env`. Для расширения IDE не полагайтесь только на `export` в терминале.
- **Моделей Rate Cloud нет:** проверьте путь локальной конфигурации, наличие `schema: v1` и синтаксис YAML. Через селектор Continue убедитесь, что открыт активный конфиг.
- **401 или отказ в доступе:** проверьте активность секрета и доступ к модели для ключа и аккаунта Rate Cloud. Наличие имени модели в Continue не подтверждает разрешение на запрос.
- **404 или неверный API-маршрут:** оставьте `apiBase` равным `https://llm.rate-cloud.com/v1`; не добавляйте к базовому адресу `/chat/completions`.
- **Не работают вызовы инструментов в Agent:** поле `roles` и поддержка вызовов инструментов API - разные вещи. Continue указывает `tool_use` как необходимое условие режима Agent, но фактическая совместимость Rate Cloud здесь не проверялась. Не заявляйте её без проверки.
- **В вашей версии другая схема:** источником актуальных полей является справочник Continue. Используйте `config.yaml`; JSON-конфигурация документирована как устаревшая.

Удалите секреты и личное содержимое запросов из журналов перед передачей диагностики. При подготовке руководства установщики и API-запросы не запускались.

English version: [Connect Continue to Rate Cloud](../../guides/continue.md). К списку [русских инструкций](README.md).
