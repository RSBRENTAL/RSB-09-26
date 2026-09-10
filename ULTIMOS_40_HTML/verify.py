from pathlib import Path
from html.parser import HTMLParser
from lxml import html
from urllib.parse import urljoin,urlsplit,unquote
from collections import Counter,defaultdict,deque
import json,re,hashlib,zipfile,datetime
from contextlib import ExitStack

ROOT=Path(__file__).resolve().parent;BASE='https://rentalscooterbarcelona.com/'
D=json.loads((ROOT/'evidence.json').read_text());R=json.loads((ROOT/'derived.json').read_text());E=json.loads((ROOT/'extras.json').read_text())
DI={(d['group'],d['language']):d for d in D};EI={(d['group'],d['language']):d for d in E}
def plain(e):return ' '.join(''.join(e.xpath('.//text()[not(ancestor::*[@aria-hidden="true"])]')).split())
def types(o):return o.get('@type',[]) if isinstance(o.get('@type',[]),list) else [o.get('@type')]
MONTHS={'january':1,'february':2,'march':3,'april':4,'may':5,'june':6,'july':7,'august':8,'mayo':5,'junio':6,'abril':4,'juliol':7,'julho':7,'juillet':7,'luglio':7,'juli':7,'juli.':7,'julio':7,'lipca':7,'juin':6,'juni':6,'juny':6,'czerwca':6,'avril':4,'aprile':4}
def visible_date(s):
    words=re.findall(r'[\wÀ-ž]+',s.lower());nums=[int(w) for w in words if w.isdigit()];month=next((MONTHS[w] for w in words if w in MONTHS),None)
    if not month or len(nums)!=2:return None
    return f'{nums[-1]:04d}-{month:02d}-{nums[0]:02d}'
for e in E:
    d=DI[e['group'],e['language']];dom=html.fromstring(Path(d['local_path']).read_bytes());e['visible_editorial_dates']=[]
    for el in dom.xpath('//span[contains(concat(" ",normalize-space(@class)," ")," post-pill ")]'):
        t=plain(el)
        if '2026' not in t:continue
        v=visible_date(t);assert v,(e['group'],e['language'],t)
        mods=[a['value'].get('dateModified','')[:10] for a in e['article_checks']]
        e['visible_editorial_dates'].append({'line':el.sourceline,'text':t,'iso_date':v,'article_dateModified':mods,'matches_article':v in mods})
    for c in e['page_checks']:
        if c['property']=='inLanguage':c['literal_equal']=c['pass'];c['pass']=c['actual'].replace('_','-').split('-')[0].lower()==d['language'];c['interpretation']='Idioma principal coincidente; región opcional, no es error por granularidad.'
(ROOT/'extras.json').write_text(json.dumps(E,ensure_ascii=False,indent=2))

class Collect(HTMLParser):
    def __init__(self):super().__init__();self.tags=[];self.opens=Counter();self.closes=Counter()
    def handle_starttag(self,t,a):self.tags.append((t,dict(a),self.getpos()[0]));self.opens[t]+=1
    def handle_startendtag(self,t,a):self.handle_starttag(t,a)
    def handle_endtag(self,t):self.closes[t]+=1

SECOND=[];PRICES=[];urlset={d['expected_url_from_path']:d for d in D}
with ExitStack() as stack:
    archives={n:stack.enter_context(zipfile.ZipFile(ROOT.parent/'upload'/n)) for n in {d['source_zip'] for d in D}}
    for d in D:
        z=archives[d['source_zip']]
        b=z.read(d['archive_path']);s=b.decode('utf-8-sig');c=Collect();c.feed(s);c.close();dom=html.fromstring(b)
        graphs=[json.loads(m.group(1)) for m in re.finditer(r'<script\b[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script\s*>',s,re.S|re.I)]
        q=deque(graphs);objects=[]
        while q:
            v=q.popleft()
            if isinstance(v,dict):objects.append(v);q.extend(v.values())
            elif isinstance(v,list):q.extend(v)
        can=[a['href'] for t,a,l in c.tags if t=='link' and a.get('rel')=='canonical']
        hre=[(a['hreflang'],a['href']) for t,a,l in c.tags if t=='link' and 'hreflang' in a]
        expected=[(x['language'],x['expected_url_from_path']) for x in D if x['group']==d['group']];expected+=[('x-default',DI[d['group'],'en']['expected_url_from_path'])]
        meta=[(a.get('name',a.get('property','')),a.get('content')) for t,a,l in c.tags if t=='meta'];ids=[a['id'] for t,a,l in c.tags if 'id' in a]
        gp={'Organization':'organization','WebSite':'website','LocalBusiness':'business'};globals_=[o for o in objects if set(types(o))&set(gp) and o.get('@id') in [BASE+'#'+v for v in gp.values()]]
        adds=[o for o in objects if 'PostalAddress' in types(o)];page=[o for o in objects if set(types(o))&{'WebPage','BlogPosting','CollectionPage','Article'}]
        dates=defaultdict(set)
        for o in objects:
            if '@id' in o and 'dateModified' in o:dates[o['@id']].add(o['dateModified'])
        faq=[o for o in objects if 'Question' in types(o)];vf=dom.xpath('//*[contains(concat(" ",normalize-space(@class)," ")," faq-item ")]')
        vp=[]
        for el in vf:
            qe=el.xpath('.//*[contains(concat(" ",normalize-space(@class)," ")," faq-q ")]')[0];ae=el.xpath('.//*[contains(concat(" ",normalize-space(@class)," ")," faq-a ")]')[0];vp.append((plain(qe),plain(ae)))
        if not vf:
            vp=[(plain(el.xpath('.//h3')[0]),plain(el.xpath('.//p')[0])) for el in dom.xpath('//*[@id="faq"]//article')]
        sp=[(' '.join(o['name'].split()),' '.join(html.fragment_fromstring(o['acceptedAnswer']['text'],create_parent='div').text_content().split())) for o in faq]
        hours=[o for o in objects if 'OpeningHoursSpecification' in types(o)];ratings=[o for o in objects if 'AggregateRating' in types(o)]
        localrefs=[(t,a,k,ref) for t,a,l in c.tags for k in ['aria-controls','aria-labelledby','aria-describedby','for'] for ref in a.get(k,'').split()]
        links=[a['href'] for t,a,l in c.tags if 'href' in a];frags=[]
        for href in links:
            u=urlsplit(urljoin(d['expected_url_from_path'],href));key=u._replace(query='',fragment='').geturl()
            if u.fragment and key in urlset:frags.append(unquote(u.fragment) in urlset[key]['ids'])
        checks={
            'original_bytes_match':hashlib.sha256(b).hexdigest()==d['sha256'],
            'canonical_own':can==[d['expected_url_from_path']],
            'hreflang_full_reciprocal':Counter(hre)==Counter(expected),
            'og_url_own':[v for k,v in meta if k=='og:url']==can,
            'no_robot_block':not any(re.search(r'\b(noindex|nofollow|none)\b',v or '',re.I) for k,v in meta if k in ['robots','googlebot','bingbot']),
            'no_duplicate_metadata':all(n==1 for k,n in Counter(k for k,v in meta if k and k!='og:locale:alternate').items()),
            'all_json_reparsed':len(graphs)==len(d['jsonld'])==2,
            'global_urls_root':all(o.get('url',BASE)==BASE for o in globals_),
            'nap_address_exact':all(all(o.get(k)==v for k,v in {'streetAddress':'Carrer de Salvador Espriu, 63','addressLocality':'Barcelona','addressRegion':'Catalonia','postalCode':'08005','addressCountry':'ES'}.items()) for o in adds),
            'name_phone_email':all(o.get(k,v)==v for o in globals_ for k,v in {'name':'RSB Rental Scooter Barcelona','alternateName':'RSB','telephone':'+34 640 559 468','email':'info@rentalscooterbarcelona.com'}.items()),
            'ratings_canonical':all(str(o.get(k))==str(v) for o in ratings for k,v in {'ratingValue':4.6,'reviewCount':226,'bestRating':5,'worstRating':1}.items()),
            'hours_canonical':{(tuple(o['dayOfWeek']),o['opens'],o['closes']) for o in hours}=={(tuple('Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split()),'10:30','13:30'),(tuple('Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split()),'16:30','20:00')},
            'page_id_url_own':all(o[k].split('#')[0]==d['expected_url_from_path'] for o in page for k in ['@id','url'] if k in o),
            'one_date_per_entity':all(len(v)==1 for v in dates.values()),
            'no_old_coordinates':not re.search(r'41\.390577|2\.198362',unquote(s)),
            'map_identifiers':all(v in unquote(s) for v in ['912877649802486634','IA5C7938C1925731A','YND84466019C726C1']),
            'unique_dom_ids':len(ids)==len(set(ids)),
            'aria_references_resolve':all(ref in ids for t,a,k,ref in localrefs),
            'faq_content_matches':Counter(vp)==Counter(sp),
            'article_open_close_dom':c.opens['article']==c.closes['article']==len(dom.xpath('//article')),
            'fragments_in_scope_resolve':all(frags),
            'tel_mail_wa_canonical':all(href in ['tel:+34640559468','mailto:info@rentalscooterbarcelona.com'] or href.startswith('https://wa.me/34640559468') for href in links if href.startswith(('tel:','mailto:','https://wa.me/'))),
            'visible_article_date_matches':all(v['matches_article'] for v in EI[d['group'],d['language']].get('visible_editorial_dates',[]))}
        # EI points to E objects updated above.
        SECOND.append({'group':d['group'],'language':d['language'],'archive_path':d['archive_path'],'checks':checks,'facts':{'json_blocks':len(graphs),'faq_count':len(vp),'article_count':c.opens['article'],'dateModified_by_id':{k:sorted(v) for k,v in dates.items()},'visible_editorial_dates':EI[d['group'],d['language']].get('visible_editorial_dates',[])}})
        cards=dom.xpath('//main//article[contains(@class,"quick-price-card")]|//main//article[contains(@class,"service-price-card")]')
        pricing=[]
        for el in cards:
            tx=plain(el);m=re.search(r'€\s*(\d+(?:[.,]\d+)?)|(\d+(?:[.,]\d+)?)\s*€',tx)
            if m:pricing.append({'line':el.sourceline,'text':tx,'price':float(m.group(1) or m.group(2))})
        accessories=pricing[6:] if d['group']=='04_BIKE' else []
        if accessories:pricing=pricing[:6]
        compact=[]
        for el in dom.xpath('//*[contains(concat(" ",normalize-space(@class)," ")," price-line ")]'):
            tx=plain(el);m=re.search(r'€\s*(\d+)|(\d+)\s*€',tx)
            if m:compact.append({'line':el.sourceline,'text':tx,'price':float(m.group(1) or m.group(2))})
        offer=[o for o in objects if 'Offer' in types(o)]
        moneyparas=[{'line':el.sourceline,'text':plain(el)} for el in dom.xpath('//main//p') if '€' in plain(el) and not el.xpath('ancestor::*[@id="reviews"]')]
        PRICES.append({'group':d['group'],'language':d['language'],'cards':pricing,'accessories':accessories,'compact':compact,'offers':offer,'money_paragraphs':moneyparas})
for r in PRICES:
    same=next(p for p in PRICES if p['group']==r['group'] and p['language']=='en');ref=same['cards']
    if r['group'].startswith('15_'):ref=next(p['cards'] for p in PRICES if p['group'].startswith('16_') and p['language']==r['language'])
    r['comparisons']=[]
    if r['cards'] and ref:r['comparisons'].append({'test':'all_card_prices_match_same_group_EN_or_inline_service_context','actual':[v['price'] for v in r['cards']],'expected':[v['price'] for v in ref],'pass':[v['price'] for v in r['cards']]==[v['price'] for v in ref]})
    if r['compact']:r['comparisons'].append({'test':'compact_matches_cards','pass':[v['price'] for v in r['compact']]==[v['price'] for v in r['cards']]})
    if r['offers']:r['comparisons'].append({'test':'offer_prices_match_cards','pass':[float(v['price']) for v in r['offers']]==[v['price'] for v in r['cards']]})
    if r['group'].startswith('11_'):
        amounts=[]
        for p in r['money_paragraphs']:amounts.extend(float(a or b) for a,b in re.findall(r'€\s*(\d+(?:[.,]\d+)?)|(\d+(?:[.,]\d+)?)\s*€',p['text']))
        ref=next(p for p in PRICES if p['group'].startswith('19_') and p['language']==r['language'])['cards']
        r['comparisons'].append({'test':'scooter_article_prices_match_scooter_guide_same_language','actual':amounts,'expected':[v['price'] for v in ref],'pass':amounts==[v['price'] for v in ref]})
    if r['group'].startswith('17_'):
        ref=next(p for p in PRICES if p['group'].startswith('08_') and p['language']==r['language'])['cards'];r['comparisons'].append({'test':'longboard_guide_matches_longboard_service','pass':[v['price'] for v in r['cards']]==[v['price'] for v in ref]})
(ROOT/'second_pass.json').write_text(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':SECOND},ensure_ascii=False,indent=2));(ROOT/'price_validation.json').write_text(json.dumps(PRICES,ensure_ascii=False,indent=2))
print('second',len(SECOND),'checks',sum(len(x['checks']) for x in SECOND),'failures',dict(Counter(k for x in SECOND for k,v in x['checks'].items() if not v)))
print('price comparisons',sum(len(x['comparisons']) for x in PRICES),'failed',[(x['group'],x['language'],c) for x in PRICES for c in x['comparisons'] if not c['pass']])
