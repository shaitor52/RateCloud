# Sources and maintenance

This repository is a multilingual editorial adaptation of Rate Cloud's public product information, retrieved on November 3, 2026. It is not the private application source repository.

| Official source | Used for |
| --- | --- |
| [Homepage](https://rate-cloud.com/) | Product positioning, subscriptions, trial, model catalog, prices, vision capabilities, performance table |
| [How it works](https://rate-cloud.com/how-it-works) | Compute, quantization, routing, quality checks, recovery, data handling, availability |
| [API documentation](https://rate-cloud.com/docs) | Public endpoints, model IDs, keys, and integration guidance |
| [White Label](https://rate-cloud.com/white-label) | Partner services, setup price, markup, responsibilities, and illustrative interfaces |

## How to use this material

Each article links to its official sources. The retrieval date identifies when the source was consulted; it does not establish the measurement period for performance data. Architectural descriptions are attributed to the public design and do not certify current production implementation.

Check the website and dashboard before relying on prices, purchase terms, limits, supported client versions, or model availability. The current legal terms and privacy policy linked from the website govern service use. This repository does not replace them.

## Suggested maintenance

When product information changes, update the relevant article, its date, and its source link together. Preserve units and methodology for performance figures. Never add unsupported uptime claims, throughput guarantees, context-window sizes, hardware capacity totals, certifications, or deployment details.

Report corrections through a GitHub issue without secrets or private request content. For account and service incidents, use the support channel linked from the official website.

## Official API comparison sources

Rates checked November 3, 2026:

- [Z.ai GLM API rates](https://docs.z.ai/guides/overview/pricing).
- [DeepSeek rates, release mapping, peak and off-peak windows](https://api-docs.deepseek.com/quick_start/pricing/).
- [QwenCloud Qwen3.8-Max rates and Singapore endpoint](https://www.qwencloud.com/models/qwen3.8-max).
- [OpenAI GPT-6.1 Sol model and Standard API pricing](https://developers.openai.com/api/docs/models/gpt-6.1-sol).

Price calculations use dated public facts, explicit token proportions, and a user-supplied exchange-rate assumption. They are not measured customer bills, a live FX quotation, quality equivalence, or guaranteed monthly capacity. Competitor speed is not supplied as a measured ranking because no controlled paired dataset is available here. The use-case article contains proposed workflow designs rather than customer testimonials.

Client guides cite official configuration references and label the scope of static verification. Documentation review does not establish that a particular client version and every model feature have been tested end to end against Rate Cloud.
