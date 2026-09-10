from audit import *
from copy import deepcopy

D=json.loads((ROOT/'evidence.json').read_text());R=json.loads((ROOT/'derived.json').read_text());RI={(r['group'],r['language']):r for r in R}
E=[]
def types(o):
    t=o.get('@type',[]);return t if isinstance(t,list) else [t]
def propertext(el):
    return norm(''.join(el.xpath('.//text()[not(ancestor::*[@aria-hidden="true"]) and not(ancestor::script) and not(ancestor::style)]')))
for d in D:
    raw=Path(d['local_path']).read_text();dom=html.fromstring(raw);r=RI[d['group'],d['language']];hp=Tokens();hp.feed(raw)
    for el,q,c in zip(cls(dom,'faq-item'),d['faq_visible'],d['faq_comparison']):
        qel=cls(el,'faq-q')[0];ael=cls(el,'faq-a')[0]
        q['question']=propertext(qel);q['answer']=propertext(ael)
        c['visible']=q;c['question_exact_normalized']=q['question']==c['schema']['question'];c['answer_exact_normalized']=q['answer']==c['schema']['answer']
    r['tests']['faq_visible_schema']=all(q['question_exact_normalized'] and q['answer_exact_normalized'] for q in d['faq_comparison'])
    x={'group':d['group'],'language':d['language'],'global_checks':[],'page_checks':[],'article_checks':[],'visible_times':[],'editorial_dates':[],'semantic_blocks':[],'money_blocks':[],'policy_blocks':[],'critical_metadata_outside_head':[],'nested_interactive_source':[]}
    expected={'name':'RSB Rental Scooter Barcelona','alternateName':'RSB','telephone':'+34 640 559 468','email':'info@rentalscooterbarcelona.com'}
    for e in d['entities']:
        o=e['value'];ts=types(o)
        if set(ts)&{'Organization','WebSite','LocalBusiness'} and o.get('@id') in [BASE+'#organization',BASE+'#website',BASE+'#business']:
            for k,v in expected.items():
                if k in o:x['global_checks'].append({'path':e['path'],'property':k,'actual':o[k],'expected':v,'pass':o[k]==v})
        if 'PostalAddress' in ts:
            for k,v in {'streetAddress':'Carrer de Salvador Espriu, 63','addressLocality':'Barcelona','addressRegion':'Catalonia','postalCode':'08005','addressCountry':'ES'}.items():
                x['global_checks'].append({'path':e['path'],'property':k,'actual':o.get(k),'expected':v,'pass':o.get(k)==v})
        if 'AggregateRating' in ts:
            for k,v in {'ratingValue':4.6,'reviewCount':226,'bestRating':5,'worstRating':1}.items():
                x['global_checks'].append({'path':e['path'],'property':k,'actual':o.get(k),'expected':v,'pass':str(o.get(k))==str(v)})
        if set(ts)&{'WebPage','CollectionPage','BlogPosting','Article','NewsArticle'}:
            for k in ['@id','url']:
                if k in o:x['page_checks'].append({'path':e['path'],'property':k,'actual':o[k],'expected_page':d['expected_url_from_path'],'pass':o[k].split('#')[0]==d['expected_url_from_path']})
            if 'inLanguage' in o:x['page_checks'].append({'path':e['path'],'property':'inLanguage','actual':o['inLanguage'],'expected':d['html_lang'],'pass':o['inLanguage'].replace('_','-').lower()==d['html_lang'].replace('_','-').lower()})
            for k in ['datePublished','dateModified']:
                if k in o:x['editorial_dates'].append({'block':e['block'],'path':e['path'],'type':ts,'id':o.get('@id'),'property':k,'value':o[k]})
        if set(ts)&{'Article','BlogPosting','NewsArticle'}:
            me=o.get('mainEntityOfPage',{});me=me.get('@id','') if isinstance(me,dict) else me
            checks={'mainEntityOfPage_own':me.split('#')[0]==d['expected_url_from_path'],'headline_present':bool(o.get('headline')),'date_order':str(o.get('dateModified','9999'))[:10]>=str(o.get('datePublished','0000'))[:10],'language_matches':o.get('inLanguage','').split('-')[0]==d['language']}
            x['article_checks'].append({'block':e['block'],'path':e['path'],'value':o,'checks':checks})
    for el in dom.xpath('//time'):
        x['visible_times'].append({'line':el.sourceline,'attrs':dict(el.attrib),'text':propertext(el),'context':propertext(el.getparent()),'in_reviews':bool(el.xpath('ancestor::*[@id="reviews"]'))})
    # Complete paragraph/list/heading/card text inventory, deduplicated only by DOM selection, never by language.
    for el in dom.xpath('//main//p|//main//li|//main//h1|//main//h2|//main//h3|//main//div[@class="article-fact"]|//main//article[contains(@class,"quick-price-card")]|//main//div[contains(@class,"post-meta")]'):
        if el.xpath('ancestor::*[@id="reviews"]'):continue
        rec={'line':el.sourceline,'tag':el.tag,'class':el.get('class'),'text':propertext(el)};x['semantic_blocks'].append(rec)
        if re.search(r'€|\bEUR\b|\d\s*%',rec['text']):x['money_blocks'].append(rec)
        if re.search(r'dep[oóôò]s|cau[cçz]|kaution|borg|kaucj|deposit|helm|cas[ckq]|capac|hj[aä]lm|kask|prot[eé]|guard|rodill|kne[eä]|genou|ginoc|joelh|coder|elbow|coud|gomit|cotovel|wrist|mu[ñn]eq|pols|poign|pulse|verzeker|segur|assicur|insurance|assuran|hotel|hotell|h[oô]tel|ID|licen|permis|f[uü]hrer|rijbewijs|prawo|k[oö]rkort|transfer|bank|banc|pag|pay|betal|bezah|płat|cancel|annul|storn|storlek|talla|taille|size|gr[oö][sß]|maat|rozmiar',rec['text'],re.I):x['policy_blocks'].append(rec)
    for t in hp.tags:
        a=t['attrs']
        if not t['in_head'] and (t['tag']=='title' or t['tag']=='meta' and any(k in a for k in ['name','property','charset','http-equiv']) or t['tag']=='link' and a.get('rel') in ['canonical','alternate']):x['critical_metadata_outside_head'].append(t)
    # Raw source a/button nesting independent of lxml's repairs.
    class Inter(HTMLParser):
        def __init__(self):super().__init__();self.stack=[];self.bad=[]
        def handle_starttag(self,t,a):
            if t in ['a','button']:
                if self.stack:self.bad.append({'line':self.getpos()[0],'tag':t,'inside':self.stack[:]})
                self.stack.append(t)
        def handle_endtag(self,t):
            if t in self.stack:self.stack=self.stack[:len(self.stack)-1-self.stack[::-1].index(t)]
    it=Inter();it.feed(raw);x['nested_interactive_source']=it.bad
    x['meta_head_full']={k:[v['value'] for v in vs] for k,vs in d['metas'].items()}
    E.append(x)
(ROOT/'evidence.json').write_text(json.dumps(D,ensure_ascii=False,indent=2));(ROOT/'derived.json').write_text(json.dumps(R,ensure_ascii=False,indent=2));(ROOT/'extras.json').write_text(json.dumps(E,ensure_ascii=False,indent=2))
print('FAQ mismatches',[(d['group'],d['language']) for d in D if any(not(q['question_exact_normalized'] and q['answer_exact_normalized']) for q in d['faq_comparison'])])
for x in E:
    bad=[v for k in ['global_checks','page_checks'] for v in x[k] if not v['pass']]
    bad+= [v for v in x['article_checks'] if not all(v['checks'].values())]
    if bad:print(x['group'],x['language'],json.dumps(bad,ensure_ascii=False))
print('extra_head_or_nesting',[(x['group'],x['language']) for x in E if x['critical_metadata_outside_head'] or x['nested_interactive_source']])
