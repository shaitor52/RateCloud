# Understanding Rate Cloud speed and performance

The useful performance question is how long it takes to receive a usable result for your workload. A high token rate during generation alone does not describe the complete experience: waiting, input processing, output length, and recovery all contribute.

## Published performance snapshot

The following values were displayed on the Rate Cloud homepage on November 3, 2026. The date is the retrieval date, not an independently established measurement window.

| Model | Typical complete response, seconds | Typical effective tokens/second, including waiting | Fast-response effective tokens/second, including waiting |
| --- | ---: | ---: | ---: |
| GLM 5.3 | 21.48 | 14.05 | 58.47 |
| GLM 5.3 Flash | 23.32 | 14.58 | 61.92 |
| DeepSeek V4 Pro | 15.67 | 25.83 | 127.84 |
| DeepSeek V4.1 Flash | 14.99 | 19.22 | 78.38 |
| Qwen 3.8 Max | 21.37 | 13.13 | 80.68 |

These are published service observations, not guaranteed response times, fixed hardware benchmarks, or a controlled comparison on identical prompts. The homepage does not supply a cohort size or full measurement interval alongside this table, so the figures should not be treated as proof of sustained availability or an SLA.

## What the columns mean

Complete response time runs from sending the request to receiving the finished result. It includes waiting, processing the input, and producing the answer.

The website describes “typical” as the midpoint of the results: half are faster and half are slower. The effective token-rate figures include the whole request and its waiting time. They should not be relabeled as pure decode speed or time to first token.

The fast-response column describes the fastest ten requests out of a hundred. It shows the faster end of the observed distribution, without promising that rate for a new request. Do not derive an average output length by multiplying independently summarized latency and throughput values.

## Why your task can take longer

A long document requires more input processing than a brief question. A detailed answer takes longer to generate than a short one. Tool-driven agents may require multiple calls to finish one user task. Current load, profile eligibility, replica readiness, and recovery can also affect elapsed time.

A model advertised for frequent or fast workloads can have a higher observed median response duration than another model when the observed request mixes differ. The table alone does not isolate model speed from prompt complexity, answer length, or user behavior.

## Concurrency and total throughput

Four paid slots allow independent operations to progress at the same time. They do not make an individual request four times faster. Parallelism helps when the work can be split into independent tasks; a sequential reasoning or tool chain still waits for its dependencies.

For a practical evaluation, measure your own time to a useful result, output correctness, incomplete requests, errors, and the proportion of tasks requiring retries. Record the model, input size, output size, concurrency, and observation period so results remain interpretable.

Source: [Rate Cloud's published performance table and explanations](https://rate-cloud.com/). See also [the connection documentation](https://rate-cloud.com/docs). [Back to overview](../README.md).
