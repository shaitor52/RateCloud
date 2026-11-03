"""Render the dated, localized product overview from existing public datasets."""
import csv
import html
import json
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODEL_PRICES = {
    'glm-5.3': 'Z.ai GLM-5.3',
    'glm-5.3-flash': 'Z.ai GLM-5.3-Flash',
    'deepseek-v4.1-flash': 'DeepSeek Flash off-peak',
    'deepseek-v4-pro': 'DeepSeek Pro off-peak',
    'qwen-3.8-max': 'QwenCloud Qwen3.8-Max Singapore',
}


def number(value, lang):
    result = f'{Decimal(str(value)):.2f}'
    return result if lang == 'en' else result.replace('.', ',')


def render_product(lang, base):
    labels = json.loads((ROOT/'website/overview.json').read_text())[lang]
    rows = {row['api_id']: row for row in csv.DictReader((ROOT/'data/performance-2026-11-03.csv').open())}
    subscription_file = ROOT/('ru/data/subscriptions-2026-11-03.json' if lang=='ru' else 'data/subscriptions-2026-11-03.json')
    subscription_prices = {row['id']: row['periods'] for row in json.loads(subscription_file.read_text())['models']}
    esc = lambda value: html.escape(str(value), quote=True)
    website = 'https://rate-cloud.com/' + ('' if lang=='ru' else lang+'/')
    model_cards = []
    for model_id in MODEL_PRICES:
        row = rows[model_id]
        def format_subscription_price(days):
            amount = subscription_prices[model_id][str(days)]
            if lang == 'ru':
                rub = Decimal(str(amount))
                formatted = f'{rub:,.2f}'.replace(',', ' ').replace('.', ',')
                return formatted + ' ₽'
            return '$' + number(amount, lang)
        seconds = number(row['typical_complete_response_seconds'], lang)
        speed = number(row['typical_effective_tokens_per_second'], lang)
        subscription_rows = ''.join(
            f'<div data-period="{days}"><dt>{esc(labels[f"period_{days}"])}</dt><dd>{esc(format_subscription_price(days))}</dd></div>'
            for days in (3, 7, 30)
        )
        model_cards.append(f'''<article class="model-card" data-model="{model_id}">
<h3>{esc(row['model'])}</h3><p class="model-role">{esc(labels['roles'][model_id])}</p>
<dl class="model-subscription-prices">{subscription_rows}</dl>
<a class="model-trial-link" href="https://rate-cloud.com/register" aria-label="{esc(labels['trial_link'])}: {esc(row['model'])}">{esc(labels['try_label'])} ↗</a>
<dl class="model-metrics"><div><dt>{esc(labels['response_label'])}</dt><dd class="response-value">{seconds} <span>{esc(labels['seconds_unit'])}</span></dd></div><div><dt>{esc(labels['speed_label'])}</dt><dd class="speed-value">{speed} <span>{esc(labels['tps_unit'])}</span></dd></div></dl></article>''')
    periods = ''.join(f'<span class="period-chip">{esc(labels[key])}</span>' for key in ['period_3','period_7','period_30'])
    badges = ''.join(f'<span>{esc(labels[key])}</span>' for key in ['badge_tokens','badge_slots','badge_api'])
    return f'''<section class="product-overview" id="models-and-plans" aria-labelledby="product-title">
<div class="product-heading"><p class="eyebrow">{esc(labels['eyebrow'])}</p><h2 id="product-title">{esc(labels['title'])}</h2><p>{esc(labels['intro'])}</p></div>
<div class="unlimited-strip"><strong class="unlimited-symbol" aria-hidden="true">∞</strong><div><h3>{esc(labels['unlimited_title'])}</h3><p>{esc(labels['unlimited_text'])}</p></div><div class="product-badges">{badges}</div></div>
<div class="model-grid">{''.join(model_cards)}</div>
<p class="performance-note">{esc(labels['performance_note'])} <a href="{base}{lang}/articles/performance/">{esc(labels['performance_link'])} →</a></p>
<div class="subscription-layout"><div class="subscription-panel"><h3>{esc(labels['plans_title'])}</h3><p>{esc(labels['plans_text'])}</p><div class="period-options">{periods}</div><div class="product-actions"><a href="{website}pricing">{esc(labels['pricing_link'])} ↗</a></div></div>
<aside class="trial-panel"><strong class="trial-duration">{esc(labels['trial_duration'])}</strong><h3>{esc(labels['trial_title'])}</h3><p>{esc(labels['trial_text'])}</p><a class="button primary" href="https://rate-cloud.com/register">{esc(labels['trial_link'])} ↗</a></aside></div>
<div class="product-actions"><a href="{base}{lang}/articles/models/">{esc(labels['models_link'])} →</a><a href="{website}">Rate Cloud ↗</a></div></section>'''
