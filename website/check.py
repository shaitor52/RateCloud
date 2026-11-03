"""Validate generated Pages output without network access or API credentials."""
import json
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
        if tag=='link' and a.get('rel')=='alternate':self.alternates[a['hreflang']]=a['href']
        if tag=='meta' and a.get('name')=='description':self.descriptions.append(a.get('content'))
        if tag=='script' and a.get('type')=='application/ld+json':self.in_schema=True;self.schema=''
    def handle_data(self,data):
        if self.in_schema:self.schema+=data
    def handle_endtag(self,tag):
        if tag=='script' and self.in_schema:self.schemas.append(json.loads(self.schema));self.in_schema=False


def main():
    pages={f:Page(f.read_text()) for f in OUTPUT.rglob('*.html')}
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
    assert (OUTPUT/'.nojekyll').is_file()
    print(f'PASS: {len(pages)-1} content pages, {refs} local links/assets/anchors, 6 search indexes, reciprocal language metadata, currencies and sitemap')


if __name__=='__main__':main()
