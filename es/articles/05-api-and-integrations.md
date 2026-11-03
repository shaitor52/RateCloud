# Conectar herramientas y aplicaciones a Rate Cloud

Rate Cloud ofrece una API HTTP compatible con OpenAI y endpoints de compatibilidad dedicados para clientes de programación compatibles. El panel oficial contiene instrucciones de configuración específicas para cada aplicación. Sigue las instrucciones correspondientes a la versión del cliente y al sistema operativo que tienes instalados.

## Endpoints publicados

| Uso | Endpoint |
| --- | --- |
| URL base compatible con OpenAI | `https://llm.rate-cloud.com/v1` |
| Catálogo de modelos | `GET https://llm.rate-cloud.com/v1/models` |
| Chat completions | `POST https://llm.rate-cloud.com/v1/chat/completions` |
| Responses | `POST https://llm.rate-cloud.com/v1/responses` |
| URL base de compatibilidad con Codex | `https://llm.rate-cloud.com/codex/v1` |
| URL base de compatibilidad con Claude Code | `https://llm.rate-cloud.com/claude` |

Las solicitudes directas a `/v1` se autentican con una clave de API tipo bearer. Usa un ID de modelo exacto del [catálogo](02-models.md), como `glm-5.3`. No añadas el prefijo de cliente `ratecloud/` al identificador HTTP directo.

## Del registro a la primera solicitud

Regístrate o inicia sesión en [Rate Cloud](https://rate-cloud.com/). Completa las verificaciones necesarias para la prueba o compra el acceso al modelo que necesites. En la configuración de claves de API del panel, crea una clave con nombre, elige los modelos permitidos, las direcciones IP admitidas y la fecha de caducidad; luego copia de inmediato el secreto que se muestra.

La suscripción concede el derecho a ejecutar un modelo; los permisos de la clave determinan si una clave concreta puede utilizar ese derecho. Una clave limitada a ciertos modelos no obtiene automáticamente acceso a un modelo recién comprado. Que un modelo aparezca en el catálogo no demuestra que tengas acceso de ejecución.

Para Codex o Claude Code, la guía pública indica que se active en la clave la opción de compatibilidad Codex / Claude Code.

## Una solicitud HTTP mínima

Define `RATE_CLOUD_API_KEY` en tu entorno local con el método de gestión de secretos que prefieras y ejecuta:

```sh
curl --fail-with-body https://llm.rate-cloud.com/v1/chat/completions \
  -H "Authorization: Bearer $RATE_CLOUD_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"model":"glm-5.3","messages":[{"role":"user","content":"Reply with a short greeting."}]}'
```

La variable es un marcador de posición para tu secreto local. Nunca pongas una clave real en un repositorio público, captura de pantalla, mensaje de soporte o configuración de cliente guardada en el repositorio. Usa el endpoint del catálogo para comprobar los identificadores y luego envía una solicitud pequeña a un modelo al que tu cuenta y clave tengan acceso.

## Clientes de programación y otras aplicaciones

La guía pública de conexión cubre OpenCode, Codex, Claude Code, OpenClaw, Continue, Hermes y otros clientes compatibles. El panel ofrece comandos automáticos y ejemplos de configuración manual para sistemas operativos compatibles.

La configuración depende de la versión del cliente. Por ejemplo, la guía oficial diferencia los formatos de configuración de OpenCode v1 y v2. Da prioridad a las instrucciones actuales del panel en lugar de copiar un bloque antiguo de un artículo externo.

El cliente aporta la interfaz del editor o terminal, las herramientas locales, las conexiones MCP, las instrucciones del proyecto y la gestión de conversaciones. Las funciones disponibles del modelo dependen tanto del modelo seleccionado como de la integración. Un endpoint compatible no implica que estén disponibles todas las funciones de cualquier API de primera parte.

## Solución de problemas sin exponer secretos

Comprueba la URL base y el identificador exacto del modelo, la suscripción o prueba activa, los permisos de modelo de la clave, su caducidad, las restricciones de IP y la opción de compatibilidad cuando sea necesaria. Si se solapan solicitudes, ten en cuenta el conjunto compartido de espacios. Al contactar con soporte, conserva la hora y el identificador de solicitud, y elimina los encabezados de autorización y el contenido privado.

Fuente: [documentación de API y conexión de Rate Cloud](https://rate-cloud.com/docs), consultada el 3 de noviembre de 2026. [Volver al índice](../README.md).
