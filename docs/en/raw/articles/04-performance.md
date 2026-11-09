# Understanding Rate Cloud speed and performance

English · [Русский](../ru/articles/04-performance.md)

The useful performance question is how long it takes to receive a usable result for your workload. A high token rate during generation alone does not describe the complete experience: waiting, input processing, output length, and recovery all contribute.

## Published performance data

Values below were provided by the owner on November 9, 2026. Time to first text and output generation speed are separate measures. Input context is approximately 200,000 tokens; results may vary by workload.

| Model | Time to first text (s) | Output generation (tokens/s) |
| --- | ---: | ---: |
| GLM 5.3 | 15.6 | 52.7 |
| GLM 5.3 Flash | 18.9 | 50.7 |
| DeepSeek V4.1 Flash | 11.2 | 150.8 |
| DeepSeek V4 Pro | 10.0 | 142.6 |
| Qwen 3.8 Max | 13.0-13.5 | 59.0-63.4 |

[Current performance data in CSV](../data/performance-2026-11-09.csv). Qwen ranges cover two runs.

The [November 3 CSV snapshot](../data/performance-2026-11-03.csv) is retained as historical data.

## Why your task can take longer

A long document requires more input processing than a brief question. A detailed answer takes longer to generate than a short one. Tool-driven agents may require multiple calls to finish one user task. Current load, profile eligibility, replica readiness, and recovery can also affect elapsed time.

## Concurrency and total throughput

Four paid slots allow independent operations to progress at the same time. They do not make an individual request four times faster. Parallelism helps when the work can be split into independent tasks; a sequential reasoning or tool chain still waits for its dependencies.

For a practical evaluation, measure your own time to a useful result, output correctness, incomplete requests, errors, and the proportion of tasks requiring retries. Record the model, input size, output size, concurrency, and observation period so results remain interpretable.

Source: [Rate Cloud's published performance table and explanations](https://rate-cloud.com/). See also [the connection documentation](https://rate-cloud.com/docs). [Back to overview](../README.md).
