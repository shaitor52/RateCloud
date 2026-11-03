# Conectar DeepSeek Harness a Rate Cloud

DeepSeek Harness tiene un formulario documentado de **Custom model API** para gateways compatibles con OpenAI. Rate Cloud documenta un endpoint Chat Completions compatible con OpenAI. La configuración siguiente usa ese protocolo e ID manuales de modelo.

**Documentación consultada:** 3 de noviembre de 2026. DeepSeek Harness se identifica como una versión preliminar para desarrolladores con cambios incompatibles. Esta guía sigue su documentación publicada de la interfaz web y la documentación de Rate Cloud; es una correspondencia de compatibilidad estática, no una integración probada en directo. No se ejecutó ninguna instalación ni solicitud a la API.

Referencias oficiales: [guía de conexión de Rate Cloud](https://rate-cloud.com/docs), [repositorio y aviso de versión preliminar de DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness), [configuración de modelos de DeepSeek Harness](https://deepseek-harness.github.io/deepseek-harness/en/guide/providers), [inicio rápido de DeepSeek Harness](https://deepseek-harness.github.io/deepseek-harness/en/guide/quickstart) y [catálogo de configuración de plugins](https://deepseek-harness.github.io/deepseek-harness/en/reference/config-catalog).

## Límites de compatibilidad

Rate Cloud documenta estos endpoints e ID directos de modelo:

| Uso | Valor |
| --- | --- |
| URL base | `https://llm.rate-cloud.com/v1` |
| Ruta Chat Completions | `POST /v1/chat/completions` |
| GLM 5.3 | `glm-5.3` |
| GLM 5.3 Flash | `glm-5.3-flash` |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` |
| Qwen 3.8 Max | `qwen-3.8-max` |

Harness documenta proveedores personalizados con URL base, protocolo, credencial y lista de modelos definidos por el usuario. Para este endpoint selecciona **OpenAI Chat Completions**. No selecciones Responses ni Anthropic Messages para este ejemplo. La documentación publicada no confirma que Harness tenga un proveedor Rate Cloud integrado ni compatibilidad probada en directo.

## Prepara la cuenta y los permisos de la clave

En el panel de Rate Cloud, crea una clave de API, permite el modelo que usarás y confirma que la cuenta tenga acceso de prueba o suscripción activa a ese modelo. La clave completa se muestra una sola vez al crearla. Que un modelo aparezca en el catálogo no prueba que la clave pueda llamarlo.

## Añade una API de modelo personalizada en la interfaz web

Este recorrido configura solo la interfaz web. No ejecuta un instalador ni envía una solicitud al modelo.

1. Inicia la interfaz web de Harness siguiendo los pasos de su README oficial. Esta guía no reproduce comandos de instalación.
2. Abre **Settings → Models** y elige **Add model provider**.
3. Cambia el formulario a **Custom model API**.
4. Define un ID de proveedor en minúsculas, por ejemplo `ratecloud`. Harness documenta que este ID es permanente porque las sesiones, los valores predeterminados, las solicitudes y las referencias de credenciales lo utilizan.
5. Define el nombre visible como `Rate Cloud` y la URL base como `https://llm.rate-cloud.com/v1`.
6. Elige **OpenAI Chat Completions** como protocolo de API.
7. Introduce la clave de Rate Cloud en el campo de credenciales del formulario. Harness documenta que las claves guardadas son de solo escritura en la interfaz; la credencial se guarda en `$DSH_HOME/.credentials.yaml` y la configuración conserva una referencia. No pongas la clave en un repositorio ni una incidencia pública.
8. Añade manualmente un modelo con uno de los ID exactos de la tabla. Asígnale un nombre visible claro. Deja sin definir la ventana de contexto, la salida máxima, entrada de imágenes y opciones de razonamiento salvo que tengas un valor o capacidad verificados para ese modelo.
9. Guarda el proveedor y selecciona el modelo configurado en el selector para establecerlo como predeterminado en sesiones nuevas.

Puedes añadir más modelos al mismo proveedor usando sus ID exactos sin prefijo. No añadas un prefijo de cliente como `ratecloud/` al ID introducido en este formulario de API personalizada.

## Descubrimiento de modelos opcional

Harness puede obtener una lista de modelos con la URL, el protocolo y la credencial del proveedor. Esa acción envía una solicitud HTTP autenticada al endpoint. El descubrimiento es opcional y no está garantizado que funcione con todos los formatos de lista. Para configurar sin realizar solicitudes, añade manualmente los ID de modelo como se indicó arriba. No se envió ninguna solicitud de descubrimiento al preparar esta guía.

## Solución de problemas

- **`MISSING_CREDENTIAL`:** confirma que se guardó una clave para el proveedor o que está disponible la referencia a la credencial configurada.
- **`UNKNOWN_MODEL`:** añade el ID al proveedor personalizado y selecciona esa entrada. Usa exactamente las minúsculas y puntuación del ID.
- **HTTP 401:** verifica la clave, su caducidad y el permiso del modelo en Rate Cloud. La lista de modelos no comprueba el acceso.
- **HTTP 404 o ruta incorrecta:** usa `https://llm.rate-cloud.com/v1` como URL base y selecciona OpenAI Chat Completions. No incluyas `/chat/completions` en la URL base.
- **La opción de obtener modelos no devuelve entradas:** el formato de lista del endpoint puede no ser uno de los que reconoce el descubrimiento de Harness. Añade el ID manualmente; un fallo de descubrimiento no demuestra que la inferencia no esté disponible.
- **Fallan las herramientas, imágenes o razonamiento:** declarar estas capacidades en Harness no comprueba ni crea compatibilidad de API. Configura solo capacidades documentadas para el modelo elegido y confirmadas mediante trabajo de compatibilidad real.
- **Las rutas de configuración difieren:** Harness está en versión preliminar para desarrolladores y puede cambiar rápido. Usa la página actual de configuración de modelos y el catálogo generado de configuración de plugins para la versión instalada.

No se realizó ninguna solicitud en directo, por lo que la autenticación del endpoint y el comportamiento de las funciones no se verificaron dentro de Harness.

Versión en ruso: [Conectar DeepSeek Harness a Rate Cloud](../../ru/guides/deepseek-harness.md). Volver a [todas las guías en español](README.md).
