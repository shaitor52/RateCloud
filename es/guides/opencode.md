# Conectar OpenCode a Rate Cloud

Esta guía configura OpenCode para usar la API compatible con OpenAI de Rate Cloud. Incluye el formato de configuración documentado de OpenCode v1. La página vigente de conexión de Rate Cloud distingue los formatos v1 y v2; para v2, usa el ejemplo v2 actual del panel, no pegues en él una configuración v1.

Fuentes oficiales: [guía de conexión de Rate Cloud](https://rate-cloud.com/docs) y [configuración de OpenCode](https://opencode.ai/docs/config/).

## Antes de empezar

1. Inicia sesión en Rate Cloud y crea una clave de API en **Settings → API keys**. Cópiala al crearla, ya que el secreto completo solo se muestra una vez.
2. Asegúrate de que la clave permita el modelo que piensas usar y de que la cuenta tenga una prueba activa o una suscripción para ese modelo. La lista puede mostrar modelos sin conceder permiso para ejecutarlos.
3. La configuración de proveedor de OpenCode v1 usa el prefijo `ratecloud/` al seleccionar el proveedor configurado. Este prefijo es para el cliente. El ID enviado por la API HTTP directa no lo incluye.

Los ID exactos de la API directa son:

| Modelo | ID de API directa | Selección en OpenCode v1 |
| --- | --- | --- |
| GLM 5.3 | `glm-5.3` | `ratecloud/glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` | `ratecloud/glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` | `ratecloud/deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` | `ratecloud/deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` | `ratecloud/qwen-3.8-max` |

## Define la clave en la shell

Los siguientes ejemplos leen la clave sin mostrarla. Usa el bloque correspondiente a Bash o zsh, la shell predeterminada de macOS. Escribe el secreto en el aviso. La variable estará disponible para los programas que abras desde esa shell; al terminar, cierra el terminal o elimínala con `unset`.

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

No pegues la clave en un archivo de configuración compartido, un repositorio, una captura de pantalla o un mensaje de soporte. En Windows, define `RATE_CLOUD_API_KEY` en el entorno usado para abrir OpenCode, con tu método habitual y seguro de gestión local de secretos.

## Configura OpenCode v1

Abre la configuración existente de OpenCode en `~/.config/opencode/opencode.json` en macOS/Linux. Conserva los otros proveedores y ajustes. Combina la entrada `provider` de abajo con el objeto existente y luego establece o combina el valor `model` de nivel superior. Si el archivo es nuevo, este ejemplo mínimo completo selecciona GLM 5.3:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "ratecloud/glm-5.3",
  "provider": {
    "ratecloud": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Rate Cloud",
      "options": {
        "baseURL": "https://llm.rate-cloud.com/v1",
        "apiKey": "{env:RATE_CLOUD_API_KEY}"
      },
      "models": {
        "glm-5.3": { "name": "GLM 5.3" },
        "glm-5.3-flash": { "name": "GLM 5.3 Flash" },
        "deepseek-v4.1-flash": { "name": "DeepSeek V4.1 Flash" },
        "deepseek-v4-pro": { "name": "DeepSeek V4 Pro" },
        "qwen-3.8-max": { "name": "Qwen 3.8 Max" }
      }
    }
  }
}
```

Al cargar la configuración, OpenCode sustituye `{env:RATE_CLOUD_API_KEY}` por el valor del entorno. Si la variable no está definida, se reemplaza por una cadena vacía, así que expórtala antes de abrir OpenCode. La configuración almacena solo la referencia a la variable, no el secreto.

En Windows, la ruta de configuración de usuario documentada es `%USERPROFILE%\.config\opencode\opencode.json`. OpenCode v1 y v2 utilizan estructuras de proveedor distintas. Para OpenCode v2, sigue el ejemplo manual específico de v2 en el panel de Rate Cloud; no adaptes este ejemplo v1 por intuición.

## Elige un modelo y comprueba la conexión

Reinicia OpenCode después de cambiar la configuración, abre el selector de modelos (`/models` en la TUI) y selecciona un modelo `Rate Cloud`. Empieza con una solicitud breve y sin contenido sensible. Usa el ID correspondiente de la columna de selección de OpenCode v1.

## Solución de problemas

- **Rate Cloud no aparece en la lista:** confirma que guardaste la configuración en la ruta correspondiente a tu sistema y que el JSON es válido. Comprueba que `provider.ratecloud` y el `model` seleccionado estén en el nivel superior correcto.
- **Solicitud no autorizada o denegada:** comprueba que `RATE_CLOUD_API_KEY` se exportó en la misma shell que abrió OpenCode. Revisa en el panel la caducidad, las restricciones de IP, los permisos del modelo y el acceso de prueba o suscripción.
- **La clave parece vacía:** OpenCode reemplaza una variable de entorno no definida por un valor vacío. Defínela antes de iniciar el cliente y reinícialo.
- **Se rechaza la solicitud para el modelo:** usa el ID exacto en minúsculas, incluida la puntuación, y asegúrate de que la cuenta y la clave puedan ejecutar ese modelo. Que aparezca en el catálogo no prueba que tengas acceso.
- **Usas OpenCode v2:** utiliza su formato `providers` del panel. No insertes este ejemplo v1 con el campo `provider` en un archivo v2.

Al contactar con soporte, indica la versión del cliente, el sistema operativo, el ID del modelo, la hora y el texto del error, después de retirar claves de API, encabezados de autorización y contenido privado.
