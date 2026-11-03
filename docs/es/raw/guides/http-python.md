# Acceso HTTP y Python genérico

Rate Cloud ofrece una API compatible con OpenAI para clientes que permiten definir una URL base personalizada, además de un ejemplo de llamadas directas con la biblioteca estándar de Python. Estos ejemplos no instalan paquetes ni envían solicitudes hasta que decidas ejecutarlos.

Fuente oficial: [documentación de API y conexión de Rate Cloud](https://rate-cloud.com/docs).

## Endpoints

| Uso | Método y URL |
| --- | --- |
| URL base compatible con OpenAI | `https://llm.rate-cloud.com/v1` |
| Listar modelos | `GET https://llm.rate-cloud.com/v1/models` |
| Chat completions | `POST https://llm.rate-cloud.com/v1/chat/completions` |
| API Responses | `POST https://llm.rate-cloud.com/v1/responses` |

Para solicitudes `/v1`, envía `Authorization: Bearer <API key>`. Usa el ID exacto de la tabla:

| Modelo | ID de API directa |
| --- | --- |
| GLM 5.3 | `glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` |

No añadas un prefijo de proveedor como `ratecloud/` a un ID HTTP directo. Las formas `ratecloud/` y `ocx-claude-ratecloud--` se usan en integraciones de clientes concretos.

## Define una variable de entorno

En macOS o Linux, usa el bloque correspondiente a tu shell. Ambos leen el secreto sin mostrarlo. La variable se elimina al ejecutar `unset` o cerrar el terminal.

```sh
# Bash
read -r -s -p 'Rate Cloud API key: ' RATE_CLOUD_API_KEY
printf '\n'
export RATE_CLOUD_API_KEY
```

```sh
# zsh (la shell predeterminada de macOS)
read -r -s 'RATE_CLOUD_API_KEY?Rate Cloud API key: '
printf '\n'
export RATE_CLOUD_API_KEY
```

En Windows PowerShell, define `$env:RATE_CLOUD_API_KEY` en la sesión que ejecutará el cliente. No pongas una clave real en el código fuente, un archivo `.env` versionado ni un reporte público.

## Comprobación opcional con curl

Esto envía una solicitud sencilla al catálogo de modelos. Confirma que el endpoint responde y acepta la clave, pero no prueba que la clave tenga una suscripción o permiso para un modelo concreto.

```sh
curl --fail-with-body 'https://llm.rate-cloud.com/v1/models' \
  -H "Authorization: Bearer $RATE_CLOUD_API_KEY"
```

## Ejemplo de Python 3 con biblioteca estándar

Guarda este código en un archivo `.py` local. Solo usa la biblioteca estándar de Python (`urllib.request`), lee el secreto del entorno y envía una solicitud pequeña de chat completions cuando se ejecuta. Si quieres, cambia `MODEL` por otro ID exacto de API directa.

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

Ejecuta el script desde la shell donde esté definida `RATE_CLOUD_API_KEY`. No imprimas la respuesta completa en registros compartidos si las instrucciones o las salidas pueden contener datos privados.

## Solución de problemas

- **401 o error de autenticación:** confirma que la variable esté en el entorno del proceso, que la clave siga activa y no haya caducado, y que el encabezado `Authorization` use `Bearer` antes de la clave.
- **403 o acceso denegado:** verifica el acceso de prueba o suscripción al modelo, los permisos de la clave, las restricciones de IP y cualquier opción de compatibilidad requerida por un endpoint dedicado.
- **404 o modelo no encontrado:** revisa la ruta del endpoint y la escritura exacta del modelo. En estos ejemplos usa `/v1`, no los endpoints de compatibilidad de Codex o Claude Code.
- **El catálogo muestra el modelo, pero se deniega la generación:** el catálogo no demuestra los permisos de la cuenta o la clave. Confirma en el panel la suscripción al modelo y el acceso de la clave.
- **Tiempo de espera agotado o salida incompleta:** comprueba el estado de la respuesta antes de reintentar. El tiempo de espera no demuestra que la operación haya terminado; no repitas a ciegas solicitudes que ejecuten efectos secundarios en tu aplicación.

Al pedir ayuda al soporte, indica la hora, el ID del modelo, la ruta del endpoint, el estado HTTP y el identificador de solicitud si está disponible. Retira claves de API, encabezados de autorización y contenido privado de solicitudes y respuestas.
