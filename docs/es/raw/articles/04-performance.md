# Velocidad y rendimiento de Rate Cloud

La pregunta práctica sobre rendimiento es cuánto tarda en llegar un resultado útil para tu tarea. Una tasa alta de tokens durante la generación no describe toda la experiencia: también influyen la espera, el procesamiento de la entrada, la longitud de la salida y la recuperación.

## Datos de rendimiento actuales

Los valores fueron comunicados por el propietario el 9 de noviembre de 2026. El tiempo hasta el primer texto y la velocidad de generación son métricas distintas. El contexto de entrada es de aproximadamente 200.000 tokens; los resultados dependen de la carga de trabajo.

| Modelo | Tiempo hasta el primer texto (s) | Generación de respuesta (tokens/s) |
| --- | ---: | ---: |
| GLM 5.3 | 15,6 | 52,7 |
| GLM 5.3 Flash | 18,9 | 50,7 |
| DeepSeek V4.1 Flash | 11,2 | 150,8 |
| DeepSeek V4 Pro | 10,0 | 142,6 |
| Qwen 3.8 Max | 13,0-13,5 | 59,0-63,4 |

[Datos actuales de rendimiento en CSV](../../data/performance-2026-11-09.csv). Los intervalos de Qwen abarcan dos ejecuciones.

El [CSV del 3 de noviembre](../../data/performance-2026-11-03.csv) se conserva como dato histórico.

## Por qué tu tarea puede tardar más

Un documento largo requiere más procesamiento de entrada que una pregunta breve. Una respuesta detallada tarda más en generarse que una corta. Los agentes que usan herramientas pueden necesitar varias llamadas para completar una tarea. La carga actual, la elegibilidad del perfil, la preparación de la réplica y la recuperación también pueden afectar al tiempo transcurrido.

## Concurrencia y rendimiento total

Cuatro espacios de pago permiten que avancen varias operaciones independientes al mismo tiempo. No hacen que una solicitud individual sea cuatro veces más rápida. El paralelismo ayuda cuando el trabajo puede dividirse en tareas independientes; una cadena secuencial de razonamiento o herramientas sigue esperando a que se completen sus dependencias.

Para una evaluación práctica, mide tu propio tiempo hasta obtener un resultado útil, la corrección de la salida, las solicitudes incompletas, los errores y la proporción de tareas que requieren reintentos. Anota el modelo, el tamaño de entrada y salida, la concurrencia y el periodo de observación para que los resultados sean interpretables.

Fuente: [tabla de rendimiento y explicaciones publicadas por Rate Cloud](https://rate-cloud.com/). Consulta también [la documentación de conexión](https://rate-cloud.com/docs). [Volver al índice](../README.md).
