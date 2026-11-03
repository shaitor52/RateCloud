"""Build the public Markdown collection into a GitHub Pages documentation site."""
import argparse
import html
import hashlib
import json
import re
import shutil
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit
from xml.etree import ElementTree as ET

import markdown
from product import render_product
from markdown.extensions.toc import slugify_unicode

ROOT = Path(__file__).resolve().parents[1]
LANGS = {'en':'English', 'ru':'Русский', 'es':'Español', 'pt':'Português', 'de':'Deutsch', 'fr':'Français'}
EN_HOME_DESCRIPTION = "Explore Rate Cloud models with unlimited tokens, compare 3-, 7- and 30-day subscriptions, and connect your tools with practical API guides."
LABELS = ['docs','home','articles','guides','search','toc','website','start','copy','copied','close','menu','empty','raw','source','next','previous','hero','intro','explore','api','image','snapshot','data','skip','language','searchhint']
TEXT = {
'en': ['Documentation','Overview','Explore Rate Cloud','Connect your tools','Search documentation','On this page','Main website','Open dashboard','Copy','Copied','Close','Menu','No matching pages found.','Read Markdown','View source','Next','Previous','Let your agents work.','Models, practical guides, and API access with unlimited tokens.','Explore the models','Connect a tool','The official connection guide, shown in English.','Public information snapshot: November 3, 2026. Check current terms on the main website.','Sources and data','Skip to content','Language','Search articles, models, or tools'],
'ru': ['Документация','Обзор','О сервисе Rate Cloud','Подключение программ','Поиск по документации','На этой странице','Основной сайт','Открыть кабинет','Копировать','Скопировано','Закрыть','Меню','Подходящие страницы не найдены.','Читать Markdown','Исходный файл','Далее','Назад','Пусть агенты работают.','Модели, практические инструкции и API с безлимитными токенами.','Выбрать модель','Подключить программу','Официальная инструкция по подключению, английская версия.','Публичный снимок информации: 3 ноября 2026 года. Действующие условия проверяйте на основном сайте.','Источники и данные','Перейти к содержимому','Язык','Поиск статей, моделей и программ'],
'es': ['Documentación','Resumen','Descubre Rate Cloud','Conecta tus herramientas','Buscar documentación','En esta página','Sitio principal','Abrir panel','Copiar','Copiado','Cerrar','Menú','No se encontraron páginas.','Leer Markdown','Ver fuente','Siguiente','Anterior','Deja trabajar a tus agentes.','Modelos, guías prácticas y acceso a la API con tokens ilimitados.','Explorar modelos','Conectar una herramienta','La guía oficial de conexión, en inglés.','Información pública consultada el 3 de noviembre de 2026. Consulta las condiciones actuales en el sitio principal.','Fuentes y datos','Ir al contenido','Idioma','Buscar artículos, modelos o herramientas'],
'pt': ['Documentação','Visão geral','Conheça a Rate Cloud','Conecte suas ferramentas','Buscar documentação','Nesta página','Site principal','Abrir painel','Copiar','Copiado','Fechar','Menu','Nenhuma página encontrada.','Ler Markdown','Ver fonte','Próximo','Anterior','Deixe seus agentes trabalhar.','Modelos, guias práticos e acesso à API com tokens ilimitados.','Explorar modelos','Conectar ferramenta','O guia oficial de conexão, em inglês.','Informações públicas consultadas em 3 de novembro de 2026. Confira as condições atuais no site principal.','Fontes e dados','Ir para o conteúdo','Idioma','Buscar artigos, modelos ou ferramentas'],
'de': ['Dokumentation','Überblick','Rate Cloud entdecken','Tools verbinden','Dokumentation durchsuchen','Auf dieser Seite','Hauptwebsite','Dashboard öffnen','Kopieren','Kopiert','Schließen','Menü','Keine passenden Seiten gefunden.','Markdown lesen','Quelldatei','Weiter','Zurück','Lassen Sie Ihre Agenten arbeiten.','Modelle, praktische Anleitungen und API-Zugang mit unbegrenzten Tokens.','Modelle entdecken','Tool verbinden','Die offizielle Verbindungsanleitung auf Englisch.','Öffentlicher Informationsstand: 3. November 2026. Aktuelle Bedingungen stehen auf der Hauptwebsite.','Quellen und Daten','Zum Inhalt','Sprache','Artikel, Modelle oder Tools suchen'],
'fr': ['Documentation','Vue d’ensemble','Découvrir Rate Cloud','Connecter vos outils','Rechercher dans la documentation','Sur cette page','Site principal','Ouvrir le tableau de bord','Copier','Copié','Fermer','Menu','Aucune page trouvée.','Lire le Markdown','Voir la source','Suivant','Précédent','Laissez vos agents travailler.','Modèles, guides pratiques et accès API avec tokens illimités.','Découvrir les modèles','Connecter un outil','Le guide officiel de connexion, en anglais.','Informations publiques consultées le 3 novembre 2026. Consultez les conditions actuelles sur le site principal.','Sources et données','Aller au contenu','Langue','Rechercher des articles, modèles ou outils'],
}
UI = {lang: dict(zip(LABELS, values)) for lang, values in TEXT.items()}
PROMO = json.loads((ROOT/'website/promo.json').read_text())


def escape(value):
    return html.escape(str(value), quote=True)


def plain(value):
    value = re.sub(r'<[^>]*>', ' ', value)
    value = re.sub(r'!?(\[.*?\])\([^)]*\)', r'\1', value)
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'[`*#\[\]]', '', value))).strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base-url', default='https://shaitor52.github.io/RateCloud/')
    args = parser.parse_args()
    origin = args.base_url.rstrip('/') + '/'
    assert urlsplit(origin).scheme in ('http', 'https'), 'Use an HTTP(S) base URL'
    base = urlsplit(origin).path
    asset_versions = {name: hashlib.sha256((ROOT/'website/assets'/name).read_bytes()).hexdigest()[:12] for name in ['docs.css','docs.js']}
    output = ROOT / 'docs'
    output.mkdir(exist_ok=True)
    pages = []
    routes = {}
    for lang in LANGS:
        folder = ROOT if lang == 'en' else ROOT / lang
        sources = [folder/'README.md', folder/'FAQ.md', folder/'guides/README.md']
        sources += sorted((folder/'articles').glob('*.md')) + sorted((folder/'guides').glob('*.md'))
        for source in dict.fromkeys(sources):
            rel = source.relative_to(folder).as_posix()
            if rel == 'README.md': route = '' if lang == 'en' else lang + '/'
            elif rel == 'FAQ.md': route = lang + '/faq/'
            elif rel == 'guides/README.md': route = lang + '/guides/'
            else: route = lang + '/' + re.sub(r'^\d+-', '', rel.removesuffix('.md').split('/')[-1]) + '/'
            # Keep categories in URLs to avoid title collisions.
            if rel.startswith(('articles/', 'guides/')) and rel != 'guides/README.md':
                route = lang + '/' + rel.split('/')[0] + '/' + re.sub(r'^\d+-', '', source.stem) + '/'
            raw = source.read_text()
            title = re.search(r'^# (.+)$', raw, re.M).group(1)
            desc = next((plain(line) for line in raw.splitlines() if len(plain(line)) > 100 and not line.startswith(('#', '|', '- ', 'Sources:', 'Источник'))), UI[lang]['intro'])[:195]
            if lang == 'en' and rel == 'README.md':
                desc = EN_HOME_DESCRIPTION
            page = dict(source=source, lang=lang, rel=rel, route=route, raw=raw, title=title, desc=desc)
            pages.append(page); routes[source.resolve()] = route
    for source, route in [(ROOT/'SOURCES.md','en/sources/'), (ROOT/'data/README.md','en/data/'), (ROOT/'ru/data/README.md','ru/data/')]:
        raw = source.read_text(); lang = 'ru' if route.startswith('ru/') else 'en'
        page = dict(source=source, lang=lang, rel='shared/' + source.parent.name + '/' + source.name, route=route, raw=raw, title=re.search(r'^# (.+)$',raw,re.M).group(1), desc=UI[lang]['snapshot'])
        pages.append(page);routes[source.resolve()] = route

    def url(route): return base + route

    def link(source, href):
        target = urlsplit(html.unescape(href))
        if target.scheme or target.netloc or not target.path: return href
        resolved = (source.parent / unquote(target.path)).resolve()
        if not resolved.is_relative_to(ROOT): raise ValueError(f'Link leaves repository: {source}: {href}')
        if resolved in routes: result = url(routes[resolved])
        elif resolved.is_file():
            rel = resolved.relative_to(ROOT).as_posix()
            dest = ('ru/downloads/' + rel[3:]) if rel.startswith('ru/') else 'downloads/' + rel
            destination = output / dest; destination.parent.mkdir(parents=True,exist_ok=True)
            shutil.copyfile(resolved,destination);result = url(dest)
        else: raise ValueError(f'Broken source link: {source}: {href}')
        if target.fragment: result += '#' + target.fragment
        return escape(result)

    def nav(page):
        lang=page['lang'];t=UI[lang];out=[]
        for group, selected in [('home',[p for p in pages if p['lang']==lang and p['rel']=='README.md']), ('articles',[p for p in pages if p['lang']==lang and p['rel'].startswith('articles/')]), ('guides',[p for p in pages if p['lang']==lang and p['rel'].startswith('guides/') and p['rel']!='guides/README.md']), ('data',[p for p in pages if p['lang']==lang and p['rel']=='FAQ.md'])]:
            out.append(f'<div class="sidebar-group"><h2>{escape(t[group])}</h2>')
            for item in selected:
                label=t['home'] if item['rel']=='README.md' else item['title']
                active=' active' if item['source']==page['source'] else ''
                out.append(f'<a class="nav-link{active}" href="{url(item["route"])}"'+(' aria-current="page"' if active else '')+f'>{escape(label)}</a>')
            out.append('</div>')
        out.append(f'<div class="sidebar-group"><a class="nav-link" href="{url("en/sources/")}">{escape(t["data"])}</a><a class="nav-link" href="https://github.com/shaitor52/RateCloud">GitHub ↗</a></div>')
        return ''.join(out)

    def cards(items, klass):
        return ''.join(f'<a class="{klass}" href="{url(p["route"])}"><span>{escape(p["title"])}</span><p>{escape(p["desc"][:130])}</p><b aria-hidden="true">↗</b></a>' for p in items)

    search = {lang:[] for lang in LANGS}
    for page in pages:
        lang=page['lang']; t=UI[lang];promo=PROMO[lang];is_home=page['rel']=='README.md'; source=page['source']
        locale_site='https://rate-cloud.com/' + ('' if lang=='ru' else lang)
        white_url=locale_site.rstrip('/')+'/white-label'
        md=markdown.Markdown(extensions=['tables','fenced_code','toc','sane_lists'],extension_configs={'toc':{'slugify':slugify_unicode}})
        body_source=re.sub(r'^# .+\n','',page['raw'],count=1)
        # Locale navigation is supplied by the shell, rather than repeated in the article.
        lines=body_source.splitlines()
        lines=[line for line in lines if not (line.startswith(('English ·','[English]','[English version]','**Languages:**')) or (line.startswith('[English') and 'Русский' in line))]
        content=md.convert('\n'.join(lines))
        content=re.sub(r'href="([^"]+)"',lambda m:'href="'+link(source,m.group(1))+'"',content)
        content=re.sub(r'(<pre>.*?</pre>)',lambda m:f'<div class="code-block"><button class="code-copy" data-error-label="{escape(t["copy"])}" type="button">{escape(t["copy"])}</button>{m.group(1)}</div>',content,flags=re.S)
        content=re.sub(r'(<table>.*?</table>)',r'<div class="table-scroll" tabindex="0">\1</div>',content,flags=re.S)
        if page['rel']=='articles/09-unlimited-use-cases.md':
            content=re.sub(r'<p>(.*?)</p>', lambda m: '<div class="case-trial-cta">'+m.group(0)+'</div>' if 'https://rate-cloud.com/register' in m.group(1) else m.group(0), content, flags=re.S)
        screenshot=''
        if page['rel'] in ('guides/README.md','articles/05-api-and-integrations.md'):
            screenshot=f'<figure class="source-preview"><a href="https://rate-cloud.com/en/docs"><img src="{url("assets/connection-preview.jpg")}" width="924" height="1340" loading="lazy" alt="{escape(t["image"])}"></a><figcaption>{escape(t["image"])}</figcaption></figure>'
        if is_home:
            article_pages=[p for p in pages if p['lang']==lang and p['rel'].startswith('articles/')]
            guide_pages=[p for p in pages if p['lang']==lang and p['rel'].startswith('guides/') and p['rel']!='guides/README.md']
            content=f'''<section class="home-hero"><div class="hero-copy"><p class="eyebrow">RATE CLOUD / {escape(t['docs'])}</p><h1 class="page-title">{escape(t['hero'])}</h1><p class="page-description">{escape(t['intro'])}</p><div class="hero-actions"><a class="button primary" href="https://rate-cloud.com/register">{escape(promo['trial'])} ↗</a><a class="button" href="#models-and-plans">{escape(UI[lang]['explore'])} →</a></div><p class="trial-note">{escape(promo['trial_text'])}</p><div class="hero-facts"><span>GLM · DeepSeek · Qwen</span><span>API · ∞ tokens</span></div></div><div class="hero-visual"><img src="{url('assets/brand-hero.webp')}" alt="Rate Cloud" width="1024" height="1024" fetchpriority="high"></div></section>
            {render_product(lang, base)}
            <section class="infrastructure-banner" id="our-infrastructure"><h2>{escape(promo['infra_title'])}</h2><p>{escape(promo['infra_text'])}</p><a href="{url(lang+'/articles/infrastructure/')}">{escape(promo['infra_link'])} →</a></section>
            <h2 class="section-heading">{escape(promo['offers_title'])}</h2><section class="offers-grid" id="get-started" aria-label="{escape(promo['offers_title'])}"><article class="offer-card"><h3>{escape(promo['trial_title'])}</h3><p>{escape(promo['trial_text'])}</p><div class="offer-actions"><a class="button primary" href="https://rate-cloud.com/register">{escape(promo['trial_link'])} ↗</a></div></article><article class="offer-card"><h3>{escape(promo['ref_title'])}</h3><p>{escape(promo['ref_text'])}</p><div class="offer-actions"><a href="{url(lang+'/articles/referral-program/')}">{escape(promo['ref_link'])} →</a></div></article><article class="offer-card"><h3>{escape(promo['white_title'])}</h3><p>{escape(promo['white_text'])}</p><div class="offer-actions"><a href="{url(lang+'/articles/white-label/')}">White Label →</a><a href="{white_url}">{escape(promo['white_link'])} ↗</a></div></article></section>
            <section class="infrastructure-banner use-cases-banner" id="continuous-work"><h2>{escape(promo['cases_title'])}</h2><p>{escape(promo['cases_text'])}</p><a href="{url(lang+'/articles/unlimited-use-cases/')}">{escape(promo['cases_link'])} →</a></section>
            <div class="quick-grid">{cards([article_pages[0],next(p for p in article_pages if p['rel'].startswith('articles/08')),next(p for p in article_pages if p['rel'].startswith('articles/09'))],'quick-card')}</div>
            <h2 class="section-heading">{escape(t['guides'])}</h2><div class="portal-grid">{cards(guide_pages,'portal-card')}</div>
            <h2 class="section-heading">{escape(t['articles'])}</h2><div class="portal-grid">{cards(article_pages,'portal-card')}</div>'''
        alternates=[p for p in pages if p['rel']==page['rel']]
        options=''.join(f'<option value="{url(p["route"])}"'+(' selected' if p['lang']==lang else '')+f'>{LANGS[p["lang"]]}</option>' for p in alternates)
        hreflang=''.join(f'<link rel="alternate" hreflang="{p["lang"]}" href="{origin+p["route"]}">' for p in alternates)
        fallback=next((p for p in alternates if p['lang']=='en'),None)
        if fallback:hreflang+=f'<link rel="alternate" hreflang="x-default" href="{origin+fallback["route"]}">'
        raw_dest=(lang+'/raw/'+page['rel']);(output/raw_dest).parent.mkdir(parents=True,exist_ok=True);(output/raw_dest).write_text(page['raw'])
        canonical=origin+page['route']
        schema={'@context':'https://schema.org','@type':'WebPage' if is_home else 'TechArticle','headline':page['title'],'description':page['desc'],'inLanguage':lang,'url':canonical,'isPartOf':{'@type':'WebSite','name':'Rate Cloud Documentation','url':origin},'publisher':{'@type':'Organization','name':'Rate Cloud','url':'https://rate-cloud.com/'}}
        title=t['docs']+' | Rate Cloud' if is_home else page['title']+' | Rate Cloud Docs'
        heading='' if is_home else f'<div class="breadcrumb"><a href="{url("" if lang=="en" else lang+"/")}">{escape(t["docs"])}</a><span>/</span>{escape(t["guides"] if page["rel"].startswith("guides/") else t["articles"])}</div><p class="eyebrow">RATE CLOUD / {escape(t["docs"])}</p><h1 class="page-title">{escape(page["title"])}</h1>'
        toc_html=md.toc.replace('class="toc"', 'class="toc-list"')
        toc='' if is_home else f'<aside class="toc" aria-label="{escape(t["toc"])}"><h2>{escape(t["toc"])}</h2>{toc_html}</aside>'
        article_cta=f'<section class="article-cta" aria-label="{escape(promo["trial_title"])}"><h2>{escape(promo["trial_title"])}</h2><p>{escape(promo["trial_text"])}</p><div class="offer-actions"><a class="button primary" href="https://rate-cloud.com/register">{escape(promo["register"])} ↗</a><a href="{url(lang+"/articles/referral-program/")}">{escape(promo["ref_link"])} →</a><a href="{white_url}">White Label ↗</a></div></section>'
        html_page=f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(title)}</title><meta name="description" content="{escape(page['desc'])}"><meta name="robots" content="index,follow,max-image-preview:large"><link rel="canonical" href="{canonical}">{hreflang}<link rel="alternate" type="text/markdown" href="{url(raw_dest)}" title="Markdown source"><meta name="theme-color" content="#151719"><meta property="og:type" content="{'website' if is_home else 'article'}"><meta property="og:title" content="{escape(title)}"><meta property="og:description" content="{escape(page['desc'])}"><meta property="og:url" content="{canonical}"><meta property="og:image" content="{origin}assets/brand-hero.webp"><meta name="twitter:card" content="summary_large_image"><link rel="icon" href="{url('assets/brand-logo.png')}"><link rel="stylesheet" href="{url('assets/docs.css')}?v={asset_versions['docs.css']}"><script type="application/ld+json">{json.dumps(schema,ensure_ascii=False).replace('<','&lt;')}</script><script src="{url('assets/docs.js')}?v={asset_versions['docs.js']}" defer></script></head>
        <body data-base="{base}" data-lang="{lang}" data-copy="{escape(t['copy'])}" data-copied="{escape(t['copied'])}"><a class="skip-link" href="#main">{escape(t['skip'])}</a><header class="topbar"><a class="brand" href="{url('' if lang=='en' else lang+'/')}"><img class="brand-mark" src="{url('assets/brand-logo.png')}" width="32" height="32" alt=""><span>Rate Cloud<small>{escape(t['docs'])}</small></span></a><div class="header-actions"><button id="menu-toggle" class="icon-button" aria-label="{escape(t['menu'])}" aria-controls="sidebar" aria-expanded="false" data-open-label="{escape(t['menu'])}" data-close-label="{escape(t['close'])}">☰</button><button class="icon-button" data-search-open aria-label="{escape(t['search'])}"><span>⌕</span><span class="search-label">{escape(t['search'])}</span><kbd class="search-shortcut">⌘ K</kbd></button><label class="sr-only" for="language-switch">{escape(t['language'])}</label><select id="language-switch">{options}</select><a class="header-site" href="{locale_site}">{escape(t['website'])} ↗</a></div></header>
        <div class="layout"><nav id="sidebar" class="sidebar" aria-label="{escape(t['docs'])}">{nav(page)}</nav><main id="main" class="{'home-main' if is_home else ''}">{heading}<div class="article-grid"><article class="article-content">{content}{screenshot}</article>{toc}</div>{article_cta}<footer class="page-footer"><p>{escape(t['snapshot'])}</p><div><a href="{url(raw_dest)}">{escape(t['raw'])}</a> · <a href="https://github.com/shaitor52/RateCloud/blob/main/{quote(source.relative_to(ROOT).as_posix())}">{escape(t['source'])}</a></div><p><a href="{locale_site}">{escape(t['website'])} ↗</a> · <a href="https://rate-cloud.com/user/instructions">{escape(t['start'])} ↗</a></p></footer></main></div>
        <dialog id="search-dialog" aria-labelledby="search-title"><div class="search-dialog-header"><h2 id="search-title">{escape(t['search'])}</h2><button class="icon-button" id="search-close" aria-label="{escape(t['close'])}">×</button></div><label class="sr-only" for="search-input">{escape(t['search'])}</label><input id="search-input" placeholder="{escape(t['searchhint'])}" type="search" autocomplete="off"><ul id="search-results" aria-live="polite" data-empty="{escape(t['empty'])}"></ul></dialog></body></html>'''
        dest=output/page['route']/'index.html';dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(html_page)
        search[lang].append(dict(title=page['title'],url=url(page['route']),excerpt=page['desc'],text=plain(content)))
    shutil.copytree(ROOT/'website/assets',output/'assets',dirs_exist_ok=True)
    (output/'search').mkdir(exist_ok=True)
    for lang,items in search.items():(output/'search'/f'{lang}.json').write_text(json.dumps(items,ensure_ascii=False))
    ET.register_namespace('', 'http://www.sitemaps.org/schemas/sitemap/0.9');ET.register_namespace('xhtml','http://www.w3.org/1999/xhtml')
    root=ET.Element('{http://www.sitemaps.org/schemas/sitemap/0.9}urlset')
    for page in pages:
        item=ET.SubElement(root,'{http://www.sitemaps.org/schemas/sitemap/0.9}url');ET.SubElement(item,'{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text=origin+page['route']
        for alt in [p for p in pages if p['rel']==page['rel']]:ET.SubElement(item,'{http://www.w3.org/1999/xhtml}link',{'rel':'alternate','hreflang':alt['lang'],'href':origin+alt['route']})
    ET.ElementTree(root).write(output/'sitemap.xml',encoding='utf-8',xml_declaration=True)
    (output/'.nojekyll').write_text('')
    index_lines=['# Rate Cloud Documentation','', '> Multilingual documentation, model articles and integration guides.','',f'- [Main website](https://rate-cloud.com/)','']
    index_lines += [f'- [{p["lang"]}: {p["title"]}]({origin+p["route"]})\n  - [Markdown]({origin+p["lang"]}/raw/{p["rel"]})' for p in pages]
    (output/'llms.txt').write_text('\n'.join(index_lines)+'\n')
    (output/'robots.txt').write_text(f'User-agent: *\nAllow: {base}\nSitemap: {origin}sitemap.xml\n')
    (output/'404.html').write_text(f'<!doctype html><html lang="en"><meta charset="utf-8"><meta name="robots" content="noindex"><title>Page not found | Rate Cloud</title><link rel="stylesheet" href="{url("assets/docs.css")}"><main style="max-width:45rem;margin:15vh auto;padding:2rem"><h1>Page not found</h1><p><a href="{base}">Open Rate Cloud documentation →</a></p></main></html>')
    print(f'Built {len(pages)} HTML pages, {len(LANGS)} search indexes, raw Markdown, downloads and sitemap in {output}')


if __name__=='__main__': main()
