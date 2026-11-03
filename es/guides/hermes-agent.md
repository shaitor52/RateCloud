# Conectar Hermes Agent a Rate Cloud

Hermes Agent admite endpoints personalizados compatibles con OpenAI. Esta guía usa su configuración documentada de proveedor personalizado con el endpoint Chat Completions `/v1` compatible con OpenAI de Rate Cloud.

**Documentación consultada:** 3 de noviembre de 2026. Los ejemplos siguen la documentación publicada de Hermes y Rate Cloud y no se han probado en directo con una instalación de Hermes Agent ni con una cuenta. La documentación de Hermes se actualiza continuamente; las páginas consultadas no indicaban una versión mínima para esta configuración. La configuración del proveedor ha cambiado con el tiempo, así que sigue los nombres actuales de campos que aparecen abajo, no fragmentos antiguos.

Referencias oficiales: [guía de conexión de Rate Cloud](https://rate-cloud.com/docs), [guía de proveedores de Hermes Agent](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/integrations/providers.md), [variables de entorno de Hermes](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/reference/environment-variables.md) y [archivos de configuración de Hermes](https://hermes-agent.nousresearch.com/docs).

## Prepara el acceso

Crea una clave de API de Rate Cloud en el panel, permite el modelo que piensas usar y confirma que la cuenta tenga una prueba o suscripción activa. La clave completa solo se muestra al crearla. No la incluyas en código fuente ni mensajes de soporte.

El endpoint compatible genérico de Rate Cloud es:

```text
https://llm.rate-cloud.com/v1
```

El ID de modelo es el identificador directo sin prefijo. Hermes no requiere el prefijo `ratecloud/` que usan algunos otros clientes.

| Modelo | ID de API directa |
| --- | --- |
| GLM 5.3 | `glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` |

## Guarda el secreto en el archivo de entorno local de Hermes

La documentación actual de Hermes indica que los secretos administrados por el usuario se guardan en `~/.hermes/.env`. Añade esta línea localmente y reemplaza el marcador con tu clave:

```dotenv
RATE_CLOUD_API_KEY=<your-key>
```

En Windows, usa `%USERPROFILE%\.hermes\.env`. No subas este archivo al repositorio ni pegues una clave real en un ejemplo compartido. Hermes también admite una variable de entorno del proceso; el ajuste `key_env` siguiente nombra esa variable.

## Configura un endpoint personalizado

Edita `~/.hermes/config.yaml` en macOS/Linux o `%USERPROFILE%\.hermes\config.yaml` en Windows. Combina estos campos con la sección `model` existente, sin reemplazar ajustes no relacionados:

```yaml
model:
  default: glm-5.3
  provider: custom
  base_url: https://llm.rate-cloud.com/v1
  key_env: RATE_CLOUD_API_KEY
```

Esto usa las claves documentadas del endpoint personalizado de Hermes: `provider: custom`, `base_url` y `key_env`. El endpoint habla Chat Completions; no lo cambies al transporte Anthropic Messages o Responses. No añadas un límite de contexto sin tener un valor verificado para el servicio y el modelo.

Para elegir otro modelo de Rate Cloud, cambia `model.default` por uno de los otros ID exactos de la tabla. Mantén `provider: custom` y la URL base de Rate Cloud.

## Configuración interactiva opcional

Hermes documenta `hermes model` como asistente para configurar endpoints personalizados. El asistente pide URL base, clave de API y nombre de modelo, y guarda la selección. Si lo usas, introduce `https://llm.rate-cloud.com/v1` y un ID sin prefijo de la tabla. Prefiere el archivo de entorno y la configuración manual de arriba si quieres evitar guardar la clave literal en `config.yaml`.

## Solución de problemas

- **Falta la credencial:** confirma que `RATE_CLOUD_API_KEY` esté definida en `~/.hermes/.env` o en el entorno del proceso y que `key_env` tenga la misma escritura.
- **Error de conexión:** usa una URL base que termine en `/v1`, no en `/v1/chat/completions`; el cliente añade la ruta de API.
- **Modelo desconocido o acceso denegado:** usa el ID directo exacto. Comprueba los permisos de modelo de la clave y el acceso de prueba o suscripción activa.
- **Las llamadas a herramientas aparecen como texto:** el transporte compatible con OpenAI no garantiza que todos los modelos y endpoints admitan llamadas a herramientas del modo que espera el agente. Comprueba la capacidad real del modelo antes de depender de ella.
- **El límite de contexto parece incorrecto:** Hermes puede inferir metadatos desde `/v1/models`, pero no se garantiza que el listado incluya todos los detalles. No copies a la configuración un límite de contexto sin verificarlo.
- **Encontraste un ejemplo antiguo:** la documentación anterior puede mostrar `api_key` u otra estructura de proveedor personalizado. Usa la guía actual de Hermes y confirma los campos para la versión instalada.

No se hizo ninguna solicitud a la API ni instalación al preparar esta guía.

Versión en ruso: [Conectar Hermes Agent a Rate Cloud](../../ru/guides/hermes-agent.md). Volver a [todas las guías en español](README.md).
