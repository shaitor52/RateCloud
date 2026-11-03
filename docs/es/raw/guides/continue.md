# Conectar Continue a Rate Cloud

Continue admite modelos compatibles con OpenAI mediante su proveedor OpenAI y un `apiBase` personalizado. Esta guía usa el formato actual `config.yaml` de Continue y guarda la clave en el archivo local de resolución de secretos de Continue, no en el YAML.

**Documentación consultada:** 3 de noviembre de 2026. Es una configuración estática basada en documentación, no una solicitud en directo desde Continue o una cuenta de Rate Cloud. La documentación actual de Continue prefiere YAML; `config.json` está obsoleto. Las páginas consultadas no indican una versión mínima del cliente Continue para esta configuración. Si tu versión no acepta un campo, sigue el esquema actual enlazado abajo.

Referencias oficiales: [guía de conexión de Rate Cloud](https://rate-cloud.com/docs), [configuración de modelos compatibles con OpenAI en Continue](https://docs.continue.dev/customize/model-providers/top-level/openai), [referencia YAML de Continue](https://docs.continue.dev/reference), [preguntas frecuentes de secretos de Continue](https://docs.continue.dev/faqs) y [ubicaciones de configuración de Continue](https://docs.continue.dev/guides/understanding-configs).

## Comprueba el acceso y los ID de modelo

Crea una clave de API de Rate Cloud, permite el modelo que necesitas y confirma que tu cuenta tenga una prueba o suscripción activa para él. La clave completa se muestra al crearla. La lista de modelos de Continue no concede acceso por sí sola.

La URL base compatible con OpenAI de Rate Cloud es `https://llm.rate-cloud.com/v1`. Usa los ID exactos de API directa de abajo. Continue muestra el `name` que configures en el selector y no requiere el prefijo `ratecloud/` que usan otros clientes.

| Modelo | ID de API directa |
| --- | --- |
| GLM 5.3 | `glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` |

## Guarda el secreto para la extensión del IDE

Las extensiones IDE de Continue resuelven `${{ secrets.NAME }}` desde archivos `.env`. Su documentación especifica este orden de búsqueda: `.env` del espacio de trabajo, `.continue/.env` del espacio de trabajo y, por último, `~/.continue/.env` global. La documentación advierte que las extensiones IDE no heredan directamente las variables de entorno de la shell.

Crea o actualiza el archivo global `~/.continue/.env` (Windows: `%USERPROFILE%\.continue\.env`) con esta entrada local:

```dotenv
RATE_CLOUD_API_KEY=<your-key>
```

Mantén este archivo local fuera del control de versiones. No pongas una clave real en `config.yaml` ni compartas el archivo `.env`. Según la documentación de Continue, la CLI de Continue también puede resolver el secreto desde el entorno del proceso.

## Configura el YAML local de Continue

Continue guarda su configuración local en `~/.continue/config.yaml` en macOS/Linux y `%USERPROFILE%\.continue\config.yaml` en Windows. Usa el selector de configuración y el icono de engranaje de la barra lateral de Continue para abrirlo. Conserva las secciones existentes que no sean de modelos. Añade una entrada por cada modelo que quieras mostrar; este ejemplo incluye los cinco:

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

`useResponsesApi: false` selecciona la ruta documentada de Chat Completions. Los modelos aparecen con los roles chat, edit y apply. Esta guía no asigna una capacidad Agent o de uso de herramientas porque depende de que el modelo/API admita llamadas a herramientas; activa esa capacidad solo después de verificarla para el modelo que usarás.

Guarda la configuración. La guía actual de Continue indica que los cambios se recargan automáticamente. Selecciona una entrada de Rate Cloud en el selector de modelos. No es necesario enviar una solicitud al modelo solo para comprobar la configuración estática y la entrada del selector.

## Solución de problemas

- **No se resuelve la clave de API:** comprueba la escritura exacta `RATE_CLOUD_API_KEY` y que la clave esté en una ubicación `.env` compatible. En extensiones IDE, no dependas solo de un `export` en un terminal.
- **No aparece ningún modelo Rate Cloud:** confirma que el YAML esté en la ruta local, que exista `schema: v1` y que el archivo guardado siga siendo YAML válido. Usa el selector de configuración de Continue para comprobar que editas la configuración activa.
- **401 o acceso denegado:** comprueba que el secreto esté activo y que Rate Cloud permita el modelo tanto a la clave como a la cuenta. Que el nombre aparezca en Continue no demuestra acceso.
- **404 o ruta de API incorrecta:** conserva `apiBase` como `https://llm.rate-cloud.com/v1`; no añadas `/chat/completions` a la URL base.
- **Fallan llamadas a herramientas del modo Agent:** los roles y la compatibilidad de herramientas del endpoint son cosas distintas. Continue documenta `tool_use` como requisito del modo Agent, pero aquí no se probó en directo la compatibilidad de Rate Cloud. No lo declares salvo que lo verifiques.
- **La forma de configuración es distinta en tu versión:** la referencia de Continue es la fuente de los campos YAML admitidos. Prefiere `config.yaml`; los JSON se documentan como obsoletos.

Retira secretos y contenido privado de las instrucciones de los registros antes de compartir diagnósticos. No se realizaron instalaciones ni solicitudes a la API al preparar esta guía.

Versión en ruso: [Conectar Continue a Rate Cloud](../../ru/guides/continue.md). Volver a [todas las guías en español](README.md).
