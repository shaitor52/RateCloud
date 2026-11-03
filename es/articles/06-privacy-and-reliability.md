# Privacidad, tratamiento de datos y disponibilidad

La arquitectura pública de Rate Cloud distingue entre el contenido de las solicitudes, el estado temporal de cálculo, los metadatos operativos y los datos de cuenta o de pago. Estas categorías tienen distintos fines y reglas de conservación. Este artículo resume el diseño y las políticas publicados, no una auditoría de seguridad independiente.

## Contenido de las solicitudes y búferes temporales

El servicio declara que no crea un historial permanente del texto de las instrucciones y respuestas, y que no entrena modelos con datos de usuarios. El contenido de las solicitudes se procesa en memoria temporal. Para los búferes de aplicación gestionados y accesibles, el objetivo documentado de limpieza es de hasta cinco segundos tras una entrega correcta y hasta treinta segundos tras un error definitivo, una cancelación o una desconexión.

Estos objetivos para búferes de aplicación no deben generalizarse como garantía de que se borre cada copia física de cada acelerador en esos plazos exactos. La arquitectura pública reconoce un límite de confianza separado para el hardware alquilado.

## Caché de cálculo aislada

La caché KV de cálculo tiene una vigencia distinta: hasta cinco minutos sin reutilización y una antigüedad absoluta máxima de quince minutos. Las entradas caducadas dejan de ser aptas para nuevos aciertos de caché. Una operación que ya utiliza una entrada puede terminar dentro de su plazo; la memoria se limpia cuando se libera la última referencia.

La caché documentada no se guarda en disco ni se incluye en instantáneas. La compatibilidad comprende cuenta, modelo, revisión de pesos, cuantización, tokenizador, plantilla de conversación e instrucciones del sistema. El índice está protegido con HMAC y un usuario no puede seleccionar el área de caché de otra cuenta. Una política del proyecto puede especificar un perfil sin caché entre solicitudes.

El historial del lado del cliente es independiente. Un editor, agente, bot o aplicación puede conservar sus propias conversaciones y archivos según su configuración.

## Metadatos operativos

La arquitectura pública describe metadatos como identificadores, modelo y perfil, marcas de tiempo, duración, uso, estado de espacios y códigos de error. Los registros detallados se eliminan después de treinta días. No incluyen instrucciones, respuestas, argumentos de herramientas, archivos ni tokens de autorización. Los datos de cuenta, pago y soporte enviados voluntariamente tienen fines y plazos de conservación distintos.

«No hay historial permanente de instrucciones» no significa «no hay registros de cuenta u operación». Consulta la política de privacidad vigente enlazada desde el sitio para conocer los detalles legales aplicables.

## Límites de transporte e infraestructura

La arquitectura describe TLS para el transporte externo, comprobaciones de identidad y mTLS entre servicios, acceso según necesidad del servicio y separación de claves, cuentas, proyectos y ámbitos de caché. Según las reglas documentadas, los secretos de API y los cuerpos de las solicitudes no deben incluirse en registros ni copias de seguridad.

El transporte protegido y el cálculo protegido por hardware son garantías distintas. El sitio no promete protección de computación confidencial en todos los aceleradores. Si un nodo pierde la gestión de confianza, se excluye, se revoca su autoridad y su reincorporación requiere verificación y limpieza.

## Disponibilidad e interrupciones

No se garantiza la disponibilidad continua 24/7 de todos los modelos. Antes de que empiece la salida, la recuperación puede reintentar una operación en una réplica compatible dentro del plazo original. Esto puede añadir latencia. Si una transmisión ya empezó y se interrumpe, debe seguir apareciendo como una operación incompleta, no como una respuesta falsamente terminada.

La regla de compensación publicada se aplica a una interrupción completa y continua del sistema de más de cuatro horas con respuestas HTTP 503. Ofrece extensiones de doce horas para una suscripción de tres días, un día para una de siete días y tres días para una de treinta días. Los fallos de un modelo concreto, las respuestas lentas, los límites de concurrencia y otros códigos de error no están cubiertos por esa regla específica. Prevalecen las condiciones aplicables y los derechos obligatorios del usuario.

Al informar de un incidente, facilita la hora y los identificadores de operación. No envíes secretos de API ni contenido confidencial de solicitudes.

Fuente: [Rate Cloud: tratamiento de datos, seguridad y disponibilidad](https://rate-cloud.com/how-it-works). Consulta las condiciones y la política de privacidad vigentes enlazadas desde el [sitio oficial](https://rate-cloud.com/). Consulta de fuentes: 3 de noviembre de 2026. [Volver al índice](../README.md).
