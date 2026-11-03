# Conectar OpenClaw a Rate Cloud

OpenClaw permite registrar un proveedor personalizado con una URL base compatible con OpenAI. Esta guía usa el transporte documentado `openai-completions` y la API Chat Completions compatible con OpenAI de Rate Cloud.

**Documentación consultada:** 3 de noviembre de 2026. Es un ejemplo de configuración estático basado en la documentación publicada. No se ha probado en directo con una instalación de OpenClaw ni con una cuenta de Rate Cloud. La documentación de OpenClaw se actualiza continuamente y aquí no especifica una versión mínima; usa el formato actual para tu versión instalada.

Referencias oficiales: [guía de conexión de Rate Cloud](https://rate-cloud.com/docs), [ejemplo de OpenClaw de Rate Cloud](https://rate-cloud.com/docs), [proveedores personalizados de OpenClaw](https://docs.openclaw.ai/concepts/model-providers/custom-providers), [ejemplos de proveedores de OpenClaw](https://docs.openclaw.ai/gateway/config-tools/provider-examples) y [referencias de secretos de OpenClaw](https://docs.openclaw.ai/reference/secretref-credential-surface).

## Requisitos y acceso

Crea una clave de API de Rate Cloud en el panel. Permite el modelo que quieras usar, confirma que tienes una prueba o suscripción activa y copia el secreto completo al crearlo. Que un modelo aparezca en el catálogo no concede por sí solo acceso de ejecución.

Rate Cloud documenta este endpoint para solicitudes compatibles con OpenAI:

```text
https://llm.rate-cloud.com/v1
```

Selecciona el adaptador `openai-completions`. No añadas `/chat/completions` a la URL base. Los ID directos de modelo de Rate Cloud son:

| Modelo | ID de API directa | Referencia de modelo de OpenClaw |
| --- | --- | --- |
| GLM 5.3 | `glm-5.3` | `ratecloud/glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` | `ratecloud/glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` | `ratecloud/deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` | `ratecloud/deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` | `ratecloud/qwen-3.8-max` |

La referencia de modelo de OpenClaw incluye el ID del proveedor; la solicitud ascendente utiliza el ID de modelo sin prefijo.

## Proporciona la clave sin incluirla en la configuración

OpenClaw admite la sustitución `${VARIABLE_NAME}` en los valores `apiKey` del proveedor. Define `RATE_CLOUD_API_KEY` en el entorno del proceso Gateway de OpenClaw. Un aviso en la shell puede evitar que quede en el historial:

```sh
# Bash
read -r -s -p 'Rate Cloud API key: ' RATE_CLOUD_API_KEY
printf '\n'
export RATE_CLOUD_API_KEY
```

```sh
# zsh
read -r -s 'RATE_CLOUD_API_KEY?Rate Cloud API key: '
printf '\n'
export RATE_CLOUD_API_KEY
```

Luego inicia o reinicia Gateway desde ese entorno. Para un gestor de servicios o Windows, define la variable mediante el mecanismo local seguro de secretos de ese entorno. No pongas la clave literal en un `openclaw.json` compartido, repositorio o incidencia pública.

## Añade el proveedor personalizado

Abre el `~/.openclaw/openclaw.json` existente en macOS/Linux o `%USERPROFILE%\.openclaw\openclaw.json` en Windows. Haz una copia de seguridad y combina los campos `models` y `agents` siguientes con la configuración existente. No reemplaces ajustes que no estén relacionados. OpenClaw usa JSON5, por lo que esta muestra sin comentarios también es JSON válido.

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

Este ejemplo usa los campos de la documentación actual de proveedores personalizados de OpenClaw y el ejemplo de Rate Cloud: `baseUrl`, `apiKey`, `api`, `models` y `agents.defaults.model.primary`. No afirma un límite de contexto, soporte de imágenes, compatibilidad de herramientas ni comportamiento de razonamiento. Déjalos sin especificar salvo que los hayas verificado para el endpoint y el modelo.

## Selección y solución de problemas

Reinicia Gateway después de guardar la configuración y elige el modelo de Rate Cloud configurado. Para una comprobación estática, confirma que la referencia del modelo principal coincida exactamente con un ID de proveedor/modelo del archivo. No uses un comando de lista de modelos ni de generación en directo salvo que quieras enviar una solicitud autenticada a la API.

- **Proveedor o modelo desconocido:** comprueba que `models.providers.ratecloud.models[]` tenga el ID exacto sin prefijo y que la referencia seleccionada sea `ratecloud/<mismo-id>`.
- **No autorizado:** confirma que el proceso Gateway pueda leer `RATE_CLOUD_API_KEY`, que la clave esté activa y que sus restricciones de IP permitan el host Gateway.
- **Acceso denegado:** revisa los permisos de modelo de la clave y el acceso de prueba o suscripción para ese modelo.
- **Fallan las herramientas o imágenes:** el protocolo genérico no garantiza todas las funciones. No añadas `reasoning`, `input`, `contextWindow` ni ajustes de compatibilidad salvo que el endpoint/modelo los admita realmente.
- **Usas una configuración antigua de OpenClaw:** la documentación puede cambiar. Consulta la referencia actual de proveedores personalizados en vez de copiar un esquema antiguo `models.json` a `openclaw.json`.

Retira credenciales e instrucciones privadas antes de compartir diagnósticos. Estos ejemplos solo documentan la configuración; no se ejecutó ninguna llamada a la API.

Versión en ruso: [Conectar OpenClaw a Rate Cloud](../../ru/guides/openclaw.md). Volver a [todas las guías en español](README.md).

[Referencia](https://docs.openclaw.ai/help/environment)
