# What Rate Cloud offers

English · [Русский](../ru/articles/01-about-rate-cloud.md)

Rate Cloud is built around a simple purchasing model: pay for access to a selected AI model for a defined period, then use its API without a cumulative token allowance. This is particularly useful when an application makes many model calls and a token-based bill becomes hard to predict.

An autonomous coding agent can read a repository, plan a change, edit files, run tools, inspect errors, and repeat the process many times. Each cycle can involve another request and additional input and output tokens. Rate Cloud's subscription price does not increase with the number of tokens consumed during the active subscription.

## Unlimited tokens and finite processing capacity

Unlimited tokens means Rate Cloud does not impose a daily, weekly, or monthly quota on the total input and output tokens used during the paid period. It does not mean a single request can contain an unlimited context or run forever. Context capacity, operation deadlines, concurrent execution, protective limits, hardware capacity, and service availability remain finite.

Actual monthly processing volume depends on the model, input length, output length, response speed, and available parallelism. Examples involving hundreds of millions or billions of tokens illustrate the pricing principle; they are not a promised monthly processing volume.

## Four concurrent slots per paid subscription

Each paid subscription supplies four concurrent requests for its model. A slot represents one request currently being processed. Once that operation finishes, the slot becomes available again. It is not a limit of four requests per day or month.

A developer might use all four slots for a main agent and three subagents, four separate work sessions, or independent automation jobs. API keys belonging to the same account share the relevant model's slot pool. Creating additional keys does not create additional capacity.

Subscriptions can be combined. Two subscriptions to the same model provide eight slots for that model. Subscriptions to two different models provide separate pools: for example, four GLM slots and four DeepSeek slots. A workflow must send its requests to the appropriate model to use those pools.


## Full model subscription

Full model includes all five current models: GLM 5.3, GLM 5.3 Flash, DeepSeek V4.1 Flash, DeepSeek V4 Pro, and Qwen 3.8 Max. Using the public display-currency snapshot dated November 3, 2026, the listed prices convert to $45.45 for 30 days, $22.72 for 7 days, and $13.63 for 3 days. A 10% promo code reduces those amounts to $40.90, $20.45, and $12.27. The live order total is authoritative before purchase.

One Full model package provides one concurrent slot for each of the five models. The number of packages sets the same number of slots for every model; slots cannot be reassigned. For example, two packages allow two concurrent requests to each model. An additional Full model purchase adds slots. Renewing the selected package quantity extends its access period without changing the slot count. Separate subscriptions to individual models remain independent and add their own paid capacity.

The first purchase follows the normal promo-code, referral-discount, and bonus-credit rules. A manual renewal is a new order and may use promo codes or bonuses when the account meets the usual eligibility rules. Automatic renewal through Whop is charged at the full agreed price without repeating the introductory discount. Check the current order total before payment.

## Access periods and getting started

The website offers 3-, 7-, and 30-day subscriptions. New users can test the models during the first three hours after registration and the required email and Telegram verification, with one concurrent slot. Trial access and paid subscriptions have different allowances.

Start with a representative task: a repository you actually work on, a typical document, or a real automation pattern. Evaluate the answer, tool behavior, and complete time to a usable result before choosing a model and subscription period.

## Where the service fits

Rate Cloud can serve as the model layer behind coding agents, internal assistants, bots, data extraction pipelines, document workflows, and custom products. A compatible client provides its own interface, tools, project instructions, and history. The selected model and API integration determine which model-dependent features work.

The service sells API access. Connecting a familiar application does not turn the selected GLM, DeepSeek, or Qwen model into that application's first-party model.

Sources: [Rate Cloud homepage](https://rate-cloud.com/) and [how it works](https://rate-cloud.com/how-it-works). Snapshot: November 3, 2026. [Back to overview](../README.md).
