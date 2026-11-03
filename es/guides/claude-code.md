# Conectar Claude Code a Rate Cloud

Claude Code utiliza el endpoint dedicado de compatibilidad de Rate Cloud y nombres de modelo específicos del cliente. Se trata de acceso por API a GLM, DeepSeek o Qwen mediante Rate Cloud; no convierte esos modelos en modelos de Anthropic.

Referencias oficiales: [guía de conexión de Rate Cloud](https://rate-cloud.com/docs) y [documentación de Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview).

## Crear y preparar una clave de API

En el panel de Rate Cloud, crea una clave, copia el secreto completo al generarla y activa **Codex / Claude Code compatibility**. Autoriza el modelo que quieras usar y comprueba que la cuenta tenga una prueba activa o una suscripción para él. La lista de modelos no confirma el acceso de ejecución.

## Nombres de modelo para Claude Code

Claude Code usa el prefijo `ocx-claude-ratecloud--` seguido del ID exacto del modelo. Esto difiere de la API HTTP directa, que utiliza el ID sin prefijo.

| Modelo | ID de API directa | `ANTHROPIC_MODEL` para Claude Code |
| --- | --- | --- |
| GLM 5.3 | `glm-5.3` | `ocx-claude-ratecloud--glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` | `ocx-claude-ratecloud--glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` | `ocx-claude-ratecloud--deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` | `ocx-claude-ratecloud--deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` | `ocx-claude-ratecloud--qwen-3.8-max` |

## Iniciar en macOS o Linux

En un terminal Bash o zsh, primero lee la clave sin mostrarla. Luego define las tres variables e inicia Claude Code desde el mismo terminal. El valor permanece en el entorno de esa shell hasta que la cierres o elimines las variables.

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

Continúa en ese mismo terminal:

```sh
export ANTHROPIC_BASE_URL='https://llm.rate-cloud.com/claude'
export ANTHROPIC_AUTH_TOKEN="$RATE_CLOUD_API_KEY"
export ANTHROPIC_MODEL='ocx-claude-ratecloud--glm-5.3'
claude
```

Si es necesario, sustituye el modelo por otro nombre completo de Claude Code de la tabla. Al terminar, cierra el terminal o ejecuta `unset RATE_CLOUD_API_KEY ANTHROPIC_AUTH_TOKEN ANTHROPIC_BASE_URL ANTHROPIC_MODEL`.

## Iniciar en Windows PowerShell

Define las variables en la ventana de PowerShell desde la que iniciarás Claude Code. `Read-Host` muestra los caracteres escritos; si necesitas ocultar la entrada, usa un gestor local de secretos que hayas aprobado.

```powershell
$env:RATE_CLOUD_API_KEY = Read-Host 'Rate Cloud API key'
$env:ANTHROPIC_BASE_URL = 'https://llm.rate-cloud.com/claude'
$env:ANTHROPIC_AUTH_TOKEN = $env:RATE_CLOUD_API_KEY
$env:ANTHROPIC_MODEL = 'ocx-claude-ratecloud--glm-5.3'
claude
```

Al cerrar Claude Code, elimina los valores de la sesión actual de PowerShell:

```powershell
Remove-Item Env:RATE_CLOUD_API_KEY, Env:ANTHROPIC_BASE_URL, Env:ANTHROPIC_AUTH_TOKEN, Env:ANTHROPIC_MODEL
```

## Solución de problemas

- **Error de autenticación o compatibilidad:** comprueba que la clave tenga activada la opción **Codex / Claude Code compatibility**. Es necesaria para este endpoint.
- **Modelo desconocido:** usa el nombre completo `ocx-claude-ratecloud--` y el sufijo exacto de la tabla. No uses el ID HTTP sin prefijo en `ANTHROPIC_MODEL`.
- **Acceso al modelo denegado:** comprueba la prueba o suscripción activa, los permisos de modelo de la clave, su caducidad y la lista de IP permitidas.
- **Funciona en un terminal, pero no desde el lanzador de una aplicación:** los programas iniciados desde un terminal heredan sus variables de entorno. Inicia Claude Code desde la shell configurada o usa la guía actual del panel para configurar el cliente de forma persistente.
- **Falla la conexión:** verifica que la URL base sea exactamente `https://llm.rate-cloud.com/claude`; es la URL de compatibilidad de Claude Code, no el endpoint genérico `/v1`.

Para solicitar ayuda, indica la versión del cliente, el sistema operativo, el modelo, la hora y el texto del error. Retira primero secretos de API, encabezados de autorización y contenido privado de las instrucciones.
