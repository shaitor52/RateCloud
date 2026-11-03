# Models and choosing the right one

English · [Русский](../ru/articles/02-models.md)

Rate Cloud's published catalog contains five models. Each has a separate subscription and an exact identifier for direct HTTP requests. Select a model by the work you need it to perform, then test representative inputs.

## Published catalog

| Model | Direct API ID | Main positioning | Image input | Published 30-day price |
| --- | --- | --- | --- | ---: |
| GLM 5.3 | `glm-5.3` | Complex development and autonomous agents | No | RUB 2,784 |
| GLM 5.3 Flash | `glm-5.3-flash` | Frequent requests, daily coding, automation, subagents | Yes | RUB 2,442 |
| DeepSeek V4.1 Flash | `deepseek-v4.1-flash` | Coding agents and parallel programming tasks | Yes | RUB 2,442 |
| DeepSeek V4 Pro | `deepseek-v4-pro` | Multistep reasoning, architecture, and code review | No | RUB 2,232 |
| Qwen 3.8 Max | `qwen-3.8-max` | Large repositories, documents, research, and long context | Yes | RUB 2,550 |

Prices and capabilities above reflect the website on November 3, 2026. Confirm current purchase conditions in the dashboard. Each listed paid subscription includes four concurrent requests and no cumulative token quota during its term. Image input means the model accepts images; it does not imply image generation.

## Matching a model to a workflow

GLM 5.3 is positioned for sustained work on complex software projects, repository analysis, tool use, and coordination of subagents. GLM 5.3 Flash targets repeated everyday work and automation where many separate calls are expected.

DeepSeek V4.1 Flash is positioned for generating and changing code, coding agents, and workloads with many programming tasks. DeepSeek V4 Pro emphasizes reasoning and deeper analysis, including architectural decisions and reviews where answer quality matters more than minimizing delay.

Qwen 3.8 Max is positioned for larger bodies of material, including repositories and documents. Long-context positioning is not a numerical context-window specification. Check the live documentation and actual request limits before designing large-input workflows.

These are product use cases, not a universal ranking or a guarantee that one model wins on every task. A useful evaluation includes task correctness, adherence to instructions, tool-call behavior, image requirements, response time, and the amount of manual correction needed.

## Model identity and execution profile

A model can have several approved precision profiles. The routing system selects a suitable profile of the model requested by the user. Choosing a compact execution profile does not mean replacing the requested model with another catalog entry. Flash and Pro are distinct models.

Use the exact IDs in the table for the direct API. Client-specific model names may add a provider prefix; that prefix is not part of the direct HTTP identifier. A model appearing in a client's list does not by itself prove that the account or key has permission to execute it.

Sources: [model catalog and prices](https://rate-cloud.com/), [API model IDs](https://rate-cloud.com/docs), and [model profiles](https://rate-cloud.com/how-it-works). [Back to overview](../README.md).
