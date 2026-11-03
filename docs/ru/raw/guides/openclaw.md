# Подключение OpenClaw к Rate Cloud

OpenClaw позволяет добавить собственного провайдера с OpenAI-совместимым базовым адресом. В этом руководстве используется документированный транспорт `openai-completions` и OpenAI-совместимый Chat Completions API Rate Cloud.

**Документация проверена:** 3 ноября 2026 года. Это статический пример конфигурации по опубликованной документации. Он не проверялся живой установкой OpenClaw или аккаунтом Rate Cloud. Документация OpenClaw обновляется и здесь не указывает минимальную поддерживаемую версию приложения; используйте актуальный формат для своей версии.

Официальные источники: [инструкция Rate Cloud](https://rate-cloud.com/docs), [пример OpenClaw от Rate Cloud](https://rate-cloud.com/docs), [собственные провайдеры OpenClaw](https://docs.openclaw.ai/concepts/model-providers/custom-providers), [примеры провайдеров OpenClaw](https://docs.openclaw.ai/gateway/config-tools/provider-examples), [переменные окружения OpenClaw](https://docs.openclaw.ai/help/environment) и [ссылки на секреты OpenClaw](https://docs.openclaw.ai/reference/secretref-credential-surface).

## Требования и доступ

Создайте API-ключ в кабинете Rate Cloud. Разрешите ему выбранную модель, проверьте пробный доступ или активную подписку и скопируйте секрет сразу после создания. Наличие модели в каталоге само по себе не даёт права выполнять запросы.

Rate Cloud публикует следующий адрес для OpenAI-совместимых запросов:

```text
https://llm.rate-cloud.com/v1
```

Выберите адаптер `openai-completions`. Не добавляйте `/chat/completions` к базовому адресу. Точные ID моделей Rate Cloud:

| Модель | ID прямого API | Ссылка на модель в OpenClaw |
| --- | --- | --- |
| GLM 5.3 | `glm-5.3` | `ratecloud/glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` | `ratecloud/glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` | `ratecloud/deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` | `ratecloud/deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` | `ratecloud/qwen-3.8-max` |

Ссылка модели OpenClaw содержит ID провайдера. Сам запрос отправляет базовый ID модели.

## Передайте ключ без записи в конфигурацию

OpenClaw поддерживает подстановку `${ИМЯ_ПЕРЕМЕННОЙ}` в поле `apiKey` провайдера. В актуальной документации OpenClaw для ключей провайдеров рекомендуется глобальный файл `~/.openclaw/.env`; он загружается и когда Gateway работает как служба. Добавьте туда локальную строку (Windows: `%USERPROFILE%\.openclaw\.env`):

```dotenv
RATE_CLOUD_API_KEY=<ваш-ключ>
```

Храните этот файл локально и ограничьте доступ к нему. Загрузчик dotenv в OpenClaw не подставляет ссылки внутри значений `.env`, поэтому справа укажите сам ключ. Не сохраняйте его в общем `openclaw.json`, репозитории или публичном обращении. Перезапустите Gateway, если его текущий процесс ещё не загрузил новую переменную.

## Добавьте собственного провайдера

Откройте существующий `~/.openclaw/openclaw.json` в macOS/Linux или `%USERPROFILE%\.openclaw\openclaw.json` в Windows. Сделайте резервную копию, затем объедините поля `models` и `agents` ниже с текущей конфигурацией. Не заменяйте другие параметры. OpenClaw использует JSON5, а этот пример без комментариев также является корректным JSON.

```json
{
  "models": {
    "mode": "merge",
    "providers": {
      "ratecloud": {
        "baseUrl": "https://llm.rate-cloud.com/v1",
        "apiKey": "${RATE_CLOUD_API_KEY}",
        "api": "openai-completions",
        "models": [
          { "id": "glm-5.3", "name": "GLM 5.3" },
          { "id": "glm-5.3-flash", "name": "GLM 5.3 Flash" },
          { "id": "deepseek-v4.1-flash", "name": "DeepSeek V4.1 Flash" },
          { "id": "deepseek-v4-pro", "name": "DeepSeek V4 Pro" },
          { "id": "qwen-3.8-max", "name": "Qwen 3.8 Max" }
        ]
      }
    }
  },
  "agents": {
    "defaults": {
      "model": {
        "primary": "ratecloud/glm-5.3"
      }
    }
  }
}
```

Пример использует поля из текущей документации OpenClaw для собственного провайдера и из примера Rate Cloud: `baseUrl`, `apiKey`, `api`, `models` и `agents.defaults.model.primary`. Здесь не заявляется поддержка размера контекста, изображений, вызовов инструментов или рассуждений. Не добавляйте для них параметры без проверки реальной поддержки API и модели.

## Выбор модели и диагностика

После сохранения конфигурации перезапустите Gateway и выберите модель Rate Cloud. Для статической проверки убедитесь, что основной идентификатор точно совпадает с провайдером и ID модели в конфигурации. Не используйте команды проверки каталога или генерации, если не хотите отправить аутентифицированный API-запрос.

- **Неизвестный провайдер или модель:** проверьте точный базовый ID в `models.providers.ratecloud.models[]` и ссылку `ratecloud/<тот же ID>`.
- **Ошибка авторизации:** убедитесь, что процесс Gateway видит `RATE_CLOUD_API_KEY`, ключ активен, а IP-ограничение разрешает адрес узла Gateway.
- **Нет доступа:** проверьте разрешения модели для ключа и пробную или платную подписку на эту модель.
- **Не работают инструменты или изображения:** общий протокол не гарантирует поддержку всех функций. Не добавляйте `reasoning`, `input`, `contextWindow` или настройки совместимости без подтверждения, что API и модель их поддерживают.
- **Старая версия конфигурации OpenClaw:** документация меняется. Сверяйте схему `openclaw.json` с актуальным разделом о собственных провайдерах, не копируйте туда устаревшую схему `models.json`.

Перед передачей диагностики удалите секреты и частные запросы. Это руководство описывает конфигурацию; API-запросы не выполнялись.

English version: [Connect OpenClaw to Rate Cloud](../../guides/openclaw.md). К списку [русских инструкций](README.md).
