# Rate Cloud vs official APIs: fixed cost for sustained work

English · [Русский](../ru/articles/08-cost-and-service-comparison.md)

**Rate Cloud's advantage is a fixed subscription price with no cumulative token quota. As usage grows, the model subscription price stays the same.** A metered API charges for each billable token. This can make sustained coding, analysis, and automation substantially cheaper on Rate Cloud, provided the workload fits its speed, concurrency, features, and availability.

Rate Cloud is not automatically cheaper at light usage. Official providers offer useful cache, batch, off-peak, and other discounts. This comparison makes those tradeoffs explicit. Checked November 3, 2026; not a promise of future prices.

## Official API rates and Rate Cloud subscriptions

USD rates are per one million tokens. Input rates in this table are **uncached**. Rate Cloud prices are USD per 30 days for one model subscription with four slots. Rate Cloud amounts are the website's USD display equivalents retrieved on November 3, 2026, not a guarantee of an unchanged checkout price.

| Official API and billing condition | Input USD/M | Output USD/M | Rate Cloud model / USD per 30 days |
| --- | ---: | ---: | --- |
| Z.ai GLM-5.3 | 1.40 | 4.40 | GLM 5.3 / 34.38 |
| Z.ai GLM-5.3-Flash | 0.15 | 0.50 | GLM 5.3 Flash / 30.16 |
| DeepSeek V4.1 Flash, off-peak | 0.15 | 0.60 | DeepSeek V4.1 Flash / 30.16 |
| DeepSeek V4.1 Flash, peak | 0.30 | 1.20 | DeepSeek V4.1 Flash / 30.16 |
| DeepSeek V4 Pro, off-peak | 0.66 | 1.98 | DeepSeek V4 Pro / 27.56 |
| DeepSeek V4 Pro, peak | 1.32 | 3.96 | DeepSeek V4 Pro / 27.56 |
| QwenCloud Qwen3.8-Max, Singapore endpoint | 2.00 | 6.00 | Qwen 3.8 Max / 31.49 |
| OpenAI GPT-6.1 Sol, Standard short-context | 2.00 | 10.00 | Different-model alternative; GPT is not sold here |

Sources: [Z.ai pricing](https://docs.z.ai/guides/overview/pricing), [DeepSeek pricing and time bands](https://api-docs.deepseek.com/quick_start/pricing/), [QwenCloud model pricing and Singapore endpoint](https://www.qwencloud.com/models/qwen3.8-max), [GPT-6.1 Sol pricing](https://developers.openai.com/api/docs/models/gpt-6.1-sol), and [Rate Cloud catalog](https://rate-cloud.com/) and [USD display-price source](https://rate-cloud.com/api/public/display-currency).

DeepSeek's official Flash API name is `deepseek-flash` for the V4.1-Flash-1017 version; Rate Cloud uses `deepseek-v4.1-flash`. DeepSeek peak hours are 01:00-04:00 and 06:00-10:00 UTC, Monday-Friday excluding Chinese public holidays; all other hours are off-peak. GLM and DeepSeek rows compare the corresponding named releases. Qwen shares the product-family label; hosted features and execution profiles can differ. GPT compares an alternative for similar work, not identical weights, capabilities, or output quality.

## What repeated usage costs

Assume total billed tokens are 80% input and 20% output, with no cache hits, tools, batch, taxes, special discounts, or long-context surcharge. Reasoning tokens must be included in billable output where applicable. These are **arithmetic workload scenarios**, not actual customer usage or a guaranteed amount Rate Cloud can process in 30 days.

| Official API | 10M total tokens | 100M | 500M | 1 billion |
| --- | ---: | ---: | ---: | ---: |
| GLM-5.3 | $20 | $200 | $1,000 | $2,000 |
| GLM-5.3-Flash | $2.20 | $22 | $110 | $220 |
| DeepSeek Flash off-peak / peak | $2.40 / $4.80 | $24 / $48 | $120 / $240 | $240 / $480 |
| DeepSeek Pro off-peak / peak | $9.24 / $18.48 | $92.40 / $184.80 | $462 / $924 | $924 / $1,848 |
| Qwen3.8-Max | $28 | $280 | $1,400 | $2,800 |
| GPT-6.1 Sol Standard | $36 | $360 | $1,800 | $3,600 |

**Rate Cloud's listed 30-day model prices remain $27.56-$34.38 across these volume scenarios.** That statement describes the price structure, not a guarantee of completing a billion tokens. Multiple model subscriptions, extra slots, client hosting, web-search services, CI compute, and your application's other tools can add costs.

## Break-even instead of a misleading universal savings claim

At the dated USD display prices, 500M uncached tokens cost $1000 on the official GLM-5.3 API versus $34.38 for a Rate Cloud GLM subscription: about 29.1 times the model-access cost. On the low-cost DeepSeek Flash off-peak API, the same arithmetic gives $120 versus $30.16: about 4.0 times. These ratios depend on the actual workload, discounts, and current subscription price.

The uncached break-even volume is about 17.19M tokens for GLM-5.3, 137.09M for GLM Flash, 125.67M for off-peak DeepSeek Flash, 29.83M for off-peak DeepSeek Pro, and 11.25M for Qwen. Below the relevant threshold, the official token bill can be lower. A high cache-hit share pushes these thresholds upward.

General formula, with volume in millions:

```text
weighted USD per million = input_fraction * input_price + output_fraction * output_price
break_even_millions = subscription_USD / weighted_USD_per_million
```

An all-input-cache-hit sensitivity example for off-peak DeepSeek Flash uses $0.003 input and $0.60 output: 500M at 80/20 costs $61.20, not $120. This is $61.20 versus a $30.16 Rate Cloud subscription, about 2.0 times the model-access cost. Real cache eligibility is not assured, and cache writes or other fees can matter. Qwen, Z.ai, and OpenAI also publish cache discounts; OpenAI offers lower Batch/Flex rates and charges more for long-context/Fast modes. Compare the actual rate tier you would use.

Reproduce scenarios offline with the [dated pricing data](../data/pricing-2026-11-03.json) and [calculator](../tools/compare_costs.py):

```sh
python3 tools/compare_costs.py --million-tokens 500
python3 tools/compare_costs.py --million-tokens 500 --cached-input-share 1
```

Run from the repository root. No API requests are made. The calculator uses the dated USD subscription snapshot.

## Speed and service tradeoffs

Choose Rate Cloud when predictable cost for sustained work matters more than minimizing each response's latency. A direct provider or premium speed tier can be a better fit when your own tests show shorter latency or when you need its hosted features, much larger concurrency, or contractual terms. Four Rate Cloud slots are not equivalent to the concurrency allowances of the official APIs.

We do **not** have a controlled, same-prompt, same-effort speed benchmark across all these services in this repository. Therefore we do not publish invented competitor tokens/second or claim a measured universal speed ranking. Rate Cloud's complete published speed snapshot is in [performance](04-performance.md). It includes waiting and differs from pure token-generation speed. This comparison explicitly accepts latency and capacity tradeoffs without presenting them as an established head-to-head result.

Official coding subscriptions and free chat apps are different products from metered API access. This table compares the listed APIs, not every provider plan. Test task quality and features as well as price.

[Use cases where a fixed token bill helps](09-unlimited-use-cases.md) · [Back to overview](../README.md)
