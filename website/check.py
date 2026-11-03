"""Validate generated Pages output without network access or API credentials."""
import json
import csv
import html
from decimal import Decimal, ROUND_HALF_UP
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
OUTPUT=ROOT/'docs'
BASE='/RateCloud/'
ORIGIN='https://shaitor52.github.io'


class Page(HTMLParser):
    def __init__(self,text):
        super().__init__();self.ids=set();self.links=[];self.canonical=[];self.alternates={};self.headings=[];self.lang=None;self.descriptions=[];self.schemas=[];self.in_schema=False;self.schema='';self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.add(a['id'])
        if tag=='html':self.lang=a.get('lang')
        if tag=='h1':self.headings.append(tag)
        if tag in ('a','link') and a.get('href'):self.links.append(a['href'])
        if tag in ('img','script') and a.get('src'):self.links.append(a['src'])
        if tag=='link' and a.get('rel')=='canonical':self.canonical.append(a.get('href'))
        if tag=='link' and a.get('rel')=='alternate' and a.get('hreflang'):self.alternates[a['hreflang']]=a['href']
        if tag=='meta' and a.get('name')=='description':self.descriptions.append(a.get('content'))
        if tag=='script' and a.get('type')=='application/ld+json':self.in_schema=True;self.schema=''
    def handle_data(self,data):
        if self.in_schema:self.schema+=data
    def handle_endtag(self,tag):
        if tag=='script' and self.in_schema:self.schemas.append(json.loads(self.schema));self.in_schema=False


def main():
    pages={f:Page(f.read_text()) for f in OUTPUT.rglob('*.html')}
    home_description = pages[OUTPUT/'index.html'].descriptions[0]
    assert home_description.endswith('.') and 80 <= len(home_description) <= 180, 'Complete English homepage description required'
    assert 'unlimited tokens' in home_description and '3-, 7- and 30-day' in home_description, 'Homepage description must explain the offer'
    assert pages[OUTPUT/'index.html'].schemas[0]['description'] == home_description, 'Homepage schema description parity'
    og_description = re.search(r'<meta property="og:description" content="([^"]*)"', (OUTPUT/'index.html').read_text()).group(1)
    assert html.unescape(og_description) == home_description, 'Homepage Open Graph description parity'
    cumulative_quota = re.compile(r'\b(?:суммарн\w*|общ\w*\s+накопительн\w*)\s+квот\w*\b', re.I)
    for source in [*(ROOT/'ru').rglob('*.md'), *(ROOT/'website').glob('*.json')]:
        assert not cumulative_quota.search(source.read_text()), (source, 'Use clear unlimited-token wording instead of cumulative-quota wording')
    ru_home = (OUTPUT/'ru/index.html').read_text()
    visible_ru_home = html.unescape(re.sub(r'<[^>]+>', ' ', re.sub(r'<(?:script|style)\b[^>]*>.*?</(?:script|style)>', '', ru_home, flags=re.I | re.S)))
    assert not cumulative_quota.search(visible_ru_home), 'RU homepage must use clear unlimited-token wording'
    refs=0
    for file,page in pages.items():
        text=file.read_text()
        assert '\u2014' not in text and '\u2013' not in text,file
        if page.lang!='ru':assert not re.search(r'\bRUB\b|₽',text),file
        assert len(page.headings)==1,(file,'one h1 required')
        if file.name!='404.html':
            assert len(page.canonical)==1 and len(page.descriptions)==1,(file,'metadata')
            relative=file.parent.relative_to(OUTPUT).as_posix()
            expected=ORIGIN+BASE+(relative+'/' if relative!='.' else '')
            assert page.canonical[0]==expected,(file,'canonical')
            assert page.schemas,(file,'structured data')
            assert '<meta name="robots" content="index,follow,max-image-preview:large">' in text,(file,'indexable')
            assert re.search(r'<link rel="alternate" type="text/markdown" href="[^"]+">|<link rel="alternate" type="text/markdown" href="[^"]+" title="Markdown source">',text),(file,'machine-readable Markdown alternate')
            assert 'https://rate-cloud.com/register' in page.links,(file,'registration CTA')
            assert BASE+page.lang+'/articles/referral-program/' in page.links,(file,'referral link')
            if file.parent==OUTPUT or file.parent.relative_to(OUTPUT).as_posix() in ['ru','es','pt','de','fr']:
                assert 'our-infrastructure' in page.ids and 'get-started' in page.ids,(file,'homepage offers')
                assert BASE+page.lang+'/articles/infrastructure/' in page.links,(file,'infrastructure link')
        for href in page.links:
            u=urlsplit(href)
            if u.netloc and u.netloc!='shaitor52.github.io':continue
            if u.scheme and u.scheme not in ['https','http']:continue
            if u.path:
                assert u.path.startswith(BASE),(file,href)
                target=OUTPUT/unquote(u.path.removeprefix(BASE))
            else:target=file
            if target.is_dir():target=target/'index.html'
            assert target.is_file(),(file,href)
            if u.fragment and target.suffix=='.html':assert unquote(u.fragment) in pages[target].ids,(file,href,'missing anchor')
            refs+=1
        for locale,alt in page.alternates.items():
            if locale=='x-default':continue
            target=OUTPUT/urlsplit(alt).path.removeprefix(BASE)/'index.html'
            other=pages[target]
            assert other.lang==locale,(file,locale)
            assert other.alternates[page.lang]==page.canonical[0],(file,'non-reciprocal hreflang')
    for locale in ['en','ru','es','pt','de','fr']:
        index=json.loads((OUTPUT/'search'/f'{locale}.json').read_text())
        assert len(index)>=21,locale
        for slug in ["infrastructure", "referral-program"]:
            assert any(item["url"]==BASE+locale+"/articles/"+slug+"/" for item in index),(locale,slug)
        if locale!='ru':assert not re.search(r'\bRUB\b|₽',json.dumps(index,ensure_ascii=False)),locale
        for item in index:
            target=OUTPUT/item['url'].removeprefix(BASE)/'index.html';assert target.is_file(),item
    sitemap=ET.parse(OUTPUT/'sitemap.xml')
    assert len(sitemap.getroot())==129
    for locale in ['en','ru','es','pt','de','fr']:
        source=ROOT/('articles/09-unlimited-use-cases.md' if locale=='en' else locale+'/articles/09-unlimited-use-cases.md')
        text=source.read_text()
        cases=re.findall(r'^## (\d{2})\. .+?(?=^## |\Z)',text,re.M|re.S)
        assert cases==[f'{i:02d}' for i in range(1,21)],(locale,'20 ordered cases')
        sections=re.split(r'^## \d{2}\. ',text,flags=re.M)[1:]
        for i,section in enumerate(sections,1):
            # Stop the last case at the article-wide operating guidance.
            section=re.split(r'^## ',section,flags=re.M)[0]
            assert 'https://rate-cloud.com/register' in section,(locale,i,'case trial CTA')
            assert '../guides/README.md' in section,(locale,i,'case connection guide')
        rendered=OUTPUT/locale/'articles/unlimited-use-cases/index.html'
        assert rendered.read_text().count('class="case-trial-cta"')>=20,(locale,'visible case CTAs')
        home=OUTPUT/('index.html' if locale=='en' else locale+'/index.html')
        assert 'continuous-work' in pages[home].ids,(locale,'homepage workflow link')
    measurements={row['api_id']:row for row in csv.DictReader((ROOT/'data/performance-2026-11-03.csv').open())}
    rub_data=json.loads((ROOT/'ru/data/subscriptions-2026-11-03.json').read_text())
    usd_data=json.loads((ROOT/'data/subscriptions-2026-11-03.json').read_text())
    assert rub_data['currency']=='RUB' and usd_data['currency']=='USD'
    # Observed public homepage dialog amounts, ordered as 3/7/30 days.
    observed={
        'glm-5.3':['835.20','1392.00','2784.00'],
        'glm-5.3-flash':['732.60','1221.00','2442.00'],
        'deepseek-v4.1-flash':['732.60','1221.00','2442.00'],
        'deepseek-v4-pro':['669.60','1116.00','2232.00'],
        'qwen-3.8-max':['765.00','1275.00','2550.00'],
    }
    observed_usd_monthly=['34.38','30.16','30.16','27.56','31.49']
    for index,(rub,usd) in enumerate(zip(rub_data['models'],usd_data['models'])):
        assert rub['id']==usd['id']
        assert [rub['periods'][period] for period in ['3','7','30']]==observed[rub['id']]
        assert usd['periods']['30']==observed_usd_monthly[index]
        for period in ['3','7']:
            expected=(Decimal(rub['periods'][period])/Decimal('80.9734')).quantize(Decimal('.01'),rounding=ROUND_HALF_UP)
            assert Decimal(usd['periods'][period])==expected
    labels=json.loads((ROOT/'website/overview.json').read_text())
    order=['glm-5.3','glm-5.3-flash','deepseek-v4.1-flash','deepseek-v4-pro','qwen-3.8-max']
    for locale in ['en','ru','es','pt','de','fr']:
        home=OUTPUT/('index.html' if locale=='en' else locale+'/index.html')
        text=home.read_text()
        after_hero=text.split('<section class="home-hero">',1)[1].split('</section>',1)[1]
        assert re.match(r'\s*<section class="product-overview"',after_hero),(locale,'product is second screen')
        cards=re.findall(r'<article class="model-card" data-model="([^"]+)">(.*?)</article>',text,re.S)
        assert [model for model,body in cards]==order,(locale,'five models')
        dataset=ROOT/('ru/data/subscriptions-2026-11-03.json' if locale=='ru' else 'data/subscriptions-2026-11-03.json')
        prices={row['id']:row['periods'] for row in json.loads(dataset.read_text())['models']}
        source=ROOT/('README.md' if locale=='en' else locale+'/README.md')
        raw_home=source.read_text()
        assert labels[locale]['unlimited_title'] in text,(locale,'unlimited headline')
        for model,body in cards:
            price_rows=re.findall(r'<div data-period="(\d+)"><dt>(.*?)</dt><dd>(.*?)</dd></div>',body)
            assert [days for days,_,_ in price_rows]==['3','7','30'],(locale,model,'three prices')
            for days,period,price in price_rows:
                numeric=re.sub(r'[^0-9,.]','',html.unescape(price)).replace(',','.')
                assert Decimal(numeric)==Decimal(prices[model][days]),(locale,model,days,'price')
                assert html.unescape(price) in raw_home,(locale,model,days,'README price parity')
            assert re.search(r'class="model-trial-link" href="https://rate-cloud.com/register" aria-label="[^"]+"',body),(locale,model,'accessible model trial')
            for classname,field in [('response-value','typical_complete_response_seconds'),('speed-value','typical_effective_tokens_per_second')]:
                value=re.search(r'class="'+classname+r'">([0-9,.]+)',body).group(1).replace(',','.')
                assert Decimal(value)==Decimal(measurements[model][field]),(locale,model,field)
        assert text.count('class="period-chip"')==3,(locale,'3 periods')
        trial=re.search(r'<aside class="trial-panel">(.*?)</aside>',text,re.S).group(1)
        assert 'https://rate-cloud.com/register' in trial,(locale,'trial registration')
        assert 'models-and-plans' in pages[home].ids,(locale,'product anchor')
    llms=(OUTPUT/'llms.txt').read_text()
    for file,page in pages.items():
        if file.name=='404.html':continue
        assert page.canonical[0] in llms,(file,'AI index canonical')
        markdown_url=re.search(r'<link rel="alternate" type="text/markdown" href="([^"]+)"',file.read_text()).group(1)
        assert ORIGIN+markdown_url in llms,(file,'AI index Markdown')
    assert (OUTPUT/'.nojekyll').is_file()
    print(f'PASS: {len(pages)-1} content pages, {refs} local links/assets/anchors, 6 search indexes, reciprocal language metadata, currencies and sitemap')


if __name__=='__main__':main()
