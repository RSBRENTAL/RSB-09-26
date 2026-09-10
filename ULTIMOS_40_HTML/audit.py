from pathlib import Path
from html.parser import HTMLParser
from lxml import html, etree
from collections import Counter, defaultdict
from urllib.parse import urlsplit, urljoin, unquote
import json, re, hashlib, subprocess, os, unicodedata

ROOT = Path(__file__).resolve().parent
BASE = 'https://rentalscooterbarcelona.com/'
LANGS = ['en','es','fr','it','de','nl','pt','ca','sv','pl']
GROUPS = ['04_BIKE', '06_QUADS', '07_SKATEBOARD', '09_LOCATION_CONTACT']
VOID = set('area base br col embed hr img input link meta param source track wbr'.split())
OPTIONAL = set('p li dt dd rt rp optgroup option colgroup thead tbody tfoot tr td th'.split())
COUNTTAGS = 'html head body header main nav section article footer form table'.split()

def norm(s):
    return ' '.join(unicodedata.normalize('NFC',s or '').split())

def txt(el):
    return norm(' '.join(el.xpath('.//text()[not(ancestor::script) and not(ancestor::style) and not(ancestor::svg)]')))

def cls(el, name):
    return el.xpath('.//*[contains(concat(" ",normalize-space(@class)," ")," '+name+' ")]')

def walk(x, path='$'):
    if isinstance(x,dict):
        yield path,x
        for k,v in x.items(): yield from walk(v,path+'.'+k)
    elif isinstance(x,list):
        for i,v in enumerate(x): yield from walk(v,f'{path}[{i}]')

class Tokens(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.starts=Counter(); self.ends=Counter(); self.stack=[]; self.errors=[]; self.tags=[]; self.comments=[]
        self.head=False; self.body=False; self.scripts=[]; self.active_script=None
    def handle_starttag(self,tag,attrs):
        line=self.getpos()[0]; aa=dict(attrs)
        self.starts[tag]+=1
        names=[k for k,v in attrs]
        dup=[k for k,v in Counter(names).items() if v>1]
        if dup: self.errors.append({'line':line,'kind':'duplicate-attribute','tag':tag,'attributes':dup})
        self.tags.append({'tag':tag,'line':line,'attrs':aa,'in_head':self.head or tag=='head','raw':self.get_starttag_text()})
        if tag=='head': self.head=True
        if tag=='body': self.body=True
        if tag=='script':
            self.active_script={'line':line,'attrs':aa,'text':''}; self.scripts.append(self.active_script)
        if tag not in VOID:
            if tag in OPTIONAL and self.stack and self.stack[-1][0]==tag: self.stack.pop()
            self.stack.append((tag,line))
    def handle_startendtag(self,tag,attrs):
        self.handle_starttag(tag,attrs)
        if tag not in VOID: self.handle_endtag(tag)
    def handle_endtag(self,tag):
        self.ends[tag]+=1; line=self.getpos()[0]
        if tag=='head': self.head=False
        if tag=='body': self.body=False
        if tag=='script': self.active_script=None
        if tag in VOID: return
        if self.stack and self.stack[-1][0]==tag: self.stack.pop(); return
        ix=next((i for i in range(len(self.stack)-1,-1,-1) if self.stack[i][0]==tag),None)
        if ix is None:
            self.errors.append({'line':line,'kind':'unexpected-close','tag':tag})
        else:
            crossed=[x for x in self.stack[ix+1:] if x[0] not in OPTIONAL]
            if crossed: self.errors.append({'line':line,'kind':'crossed-close','tag':tag,'unclosed':crossed})
            self.stack=self.stack[:ix]
    def handle_data(self,data):
        if self.active_script is not None: self.active_script['text']+=data
    def handle_comment(self,data): self.comments.append({'line':self.getpos()[0],'text':data})

def category(url):
    pp=urlsplit(url).path; parts=pp.strip('/').split('/')
    lang=parts.pop(0) if parts and parts[0] in ['es','fr','it','de','nl','pt','cat','sv','pl','ca'] else 'en'
    page=parts[0] if parts and parts[0] else 'HOME'
    if page=='blog': page='BLOG HOME' if len(parts)<2 or not parts[1] else 'BLOG ARTICLE'
    return ('ca' if lang=='cat' else lang),page

def run():
    inv=json.loads((ROOT/'inventory.json').read_text()); allrows=[]; jschecks=[]
    for row in sorted(inv,key=lambda x:(GROUPS.index(x['group']),LANGS.index(x['language']))):
        p=Path(row['local_path']); b=p.read_bytes(); s=b.decode('utf-8-sig'); lines=s.splitlines()
        hp=Tokens(); hp.feed(s); hp.close()
        parser=html.HTMLParser(encoding='utf-8'); dom=html.fromstring(b,parser=parser)
        d=dict(row); d['read_full']={'bytes_read':len(b),'characters':len(s),'sha256':hashlib.sha256(b).hexdigest(),'htmlparser_fed_all':True,'lxml_parsed_all':True}
        d['raw_head']=re.search(r'<head\b[^>]*>(.*?)</head\s*>',s,re.I|re.S).group(1)
        d['head_tags']=[x for x in hp.tags if x['in_head']]
        d['metas']=defaultdict(list); d['head_links']=[]
        for x in d['head_tags']:
            a=x['attrs']
            if x['tag']=='meta': d['metas'][a.get('property',a.get('name','charset' if 'charset' in a else a.get('http-equiv','unknown')))].append({'value':a.get('content',a.get('charset')),'line':x['line']})
            if x['tag']=='link': d['head_links'].append({'line':x['line'],**a})
        d['titles']=[{'line':x.sourceline,'value':txt(x)} for x in dom.xpath('//title')]
        d['canonicals']=[x for x in d['head_links'] if 'canonical' in (x.get('rel') or '').split()]
        d['hreflang']=[x for x in d['head_links'] if 'hreflang' in x]
        d['structure']={t:{'text_open':len(re.findall(r'<'+t+r'(?=[\s>/])',s,re.I)),'text_close':len(re.findall(r'</'+t+r'\s*>',s,re.I)),'token_open':hp.starts[t],'token_close':hp.ends[t],'parsed':len(dom.xpath('//'+t))} for t in COUNTTAGS}
        d['token_errors']=hp.errors; d['unclosed_stack']=hp.stack
        d['lxml_diagnostics']=[{'line':e.line,'message':e.message,'level':e.level_name} for e in parser.error_log]
        d['comments']=hp.comments
        ids=defaultdict(list)
        for x in hp.tags:
            if x['attrs'].get('id') is not None: ids[x['attrs']['id']].append({'tag':x['tag'],'line':x['line']})
        d['ids']=dict(ids); d['duplicate_ids']={k:v for k,v in ids.items() if len(v)>1}; d['id_references']=[]
        for x in hp.tags:
            for att in ['aria-labelledby','aria-describedby','aria-controls','aria-owns','for','list']:
                if x['attrs'].get(att):
                    for ref in x['attrs'][att].split(): d['id_references'].append({'line':x['line'],'attribute':att,'ref':ref,'exists':ref in ids})
        d['headings']=[{'tag':x.tag,'line':x.sourceline,'text':txt(x)} for x in dom.xpath('//h1|//h2|//h3|//h4|//h5|//h6')]
        d['sections']=[{'tag':x.tag,'id':x.get('id'),'class':x.get('class'),'line':x.sourceline} for x in dom.xpath('//section|//article|//main|//nav|//footer|//header')]
        d['body_text_nodes']=[]
        for x in dom.xpath('//body//text()[not(ancestor::script) and not(ancestor::style) and not(ancestor::svg)]'):
            if norm(str(x)):
                d['body_text_nodes'].append({'line':x.getparent().sourceline,'text':norm(str(x))})
        d['body_full_text']='\n'.join(f"L{x['line']}: {x['text']}" for x in d['body_text_nodes'])
        d['images']=[{'tag':x.tag,'line':x.sourceline,**dict(x.attrib)} for x in dom.xpath('//img|//picture/source|//picture')]
        d['iframes']=[{'line':x.sourceline,**dict(x.attrib)} for x in dom.xpath('//iframe')]
        d['links']=[]
        for x in dom.xpath('//*[@href]'):
            raw=x.get('href'); absolute=urljoin(d['canonical'],raw); u=urlsplit(absolute)
            internal=u.scheme in ['http','https'] and u.netloc.lower() in ['rentalscooterbarcelona.com','www.rentalscooterbarcelona.com']
            alabel=x.get('aria-label') or norm(' '.join(txt(dom.xpath('//*[@id=$id]',id=k)[0]) for k in x.get('aria-labelledby','').split() if dom.xpath('//*[@id=$id]',id=k))) or txt(x) or norm(' '.join(x.xpath('.//img/@alt'))) or x.get('title')
            item={'tag':x.tag,'line':x.sourceline,**dict(x.attrib),'raw_href':raw,'absolute_url':absolute,'text':txt(x),'accessible_name_static':alabel,'internal':internal,'ancestors':[{'tag':a.tag,'id':a.get('id'),'class':a.get('class')} for a in x.iterancestors() if a.tag in ['nav','header','footer'] or any(t in (a.get('class') or '') for t in ['lang','mobile','menu'])]}
            if internal:
                item['destination_language'],item['destination_category']=category(absolute)
                item['same_page_fragment_exists']=unquote(u.fragment) in ids if u.fragment and u.path==urlsplit(d['canonical']).path else None
            d['links'].append(item)
        d['controls']=[{'tag':x.tag,'line':x.sourceline,'text':txt(x),'attrs':dict(x.attrib),'parent_interactive':[a.tag for a in x.iterancestors() if a.tag in ['a','button']]} for x in dom.xpath('//button|//input|//select|//textarea|//*[@tabindex]|//a[ancestor::a or ancestor::button]')]
        d['faq_visible']=[]
        for x in cls(dom,'faq-item'):
            q=cls(x,'faq-q'); a=cls(x,'faq-a')
            d['faq_visible'].append({'line':x.sourceline,'question':norm(' '.join(q[0].xpath('.//text()[not(ancestor::*[@aria-hidden="true"])]'))) if q else None,'answer':txt(a[0]) if a else None,'links':a[0].xpath('.//a/@href') if a else []})
        d['tables']=[{'line':x.sourceline,'rows':[[txt(c) for c in tr.xpath('./th|./td')] for tr in x.xpath('.//tr')]} for x in dom.xpath('//table')]
        d['price_cards']=[{'line':x.sourceline,'text':txt(x)} for x in cls(dom,'service-price-card')]
        d['review_cards']=[{'line':x.sourceline,'text':txt(x),'links':x.xpath('.//a/@href')} for x in dom.xpath('//article') if 'review' in (x.get('class') or '') or x.xpath('ancestor::*[@id="reviews"]')]
        d['money_contexts']=[{'line':i+1,'text':line} for i,line in enumerate(lines) if re.search(r'€|\bEUR\b|"(?:price|lowPrice|highPrice|priceRange)"',line)]
        d['time_contexts']=[{'line':i+1,'text':line} for i,line in enumerate(lines) if re.search(r'\b\d{1,2}[:h]\d{2}\b|"(?:opens|closes|openingHours|openingHoursSpecification)"',line)]
        d['jsonld']=[]; d['entities']=[]; d['references']=[]; d['json_objects']=[]
        for n,x in enumerate(hp.scripts):
            typ=(x['attrs'].get('type') or '').lower()
            if typ=='application/ld+json':
                raw=x['text']; dupkeys=[]
                def pairs(ps):
                    cc=Counter(k for k,v in ps); dupkeys.extend(k for k,v in cc.items() if v>1); return dict(ps)
                block={'block':len(d['jsonld'])+1,'line':x['line'],'bytes':len(raw.encode()),'raw':raw,'duplicate_keys':dupkeys}
                try:
                    val=json.loads(raw,object_pairs_hook=pairs); block.update(valid=True,data=val)
                    for jp,obj in walk(val):
                        record={'block':block['block'],'path':jp,'value':obj}; d['json_objects'].append(record)
                        if '@type' in obj: d['entities'].append(record)
                        if '@id' in obj:
                            d['references'].append({'block':block['block'],'path':jp,'id':obj['@id'],'reference_only':set(obj)=={'@id'},'keys':list(obj)})
                except Exception as e: block.update(valid=False,error=str(e))
                d['jsonld'].append(block)
            elif not x['attrs'].get('src') and typ in ['', 'text/javascript','application/javascript','module']:
                jschecks.append({'file':d['group']+'/'+d['language'],'line':x['line'],'code':x['text'],'kind':'script'})
        for x in hp.tags:
            for k,v in x['attrs'].items():
                if k.startswith('on') and v: jschecks.append({'file':d['group']+'/'+d['language'],'line':x['line'],'code':v,'kind':'handler'})
        d['scripts']=hp.scripts
        d['js_id_refs']=[]
        for x in hp.scripts:
            if x['attrs'].get('type')=='application/ld+json': continue
            for m in re.finditer(r'(?:getElementById\(\s*[\'"]([^\'"]+)[\'"]|querySelector\(\s*[\'"]#([\w-]+)[\'"])',x['text']):
                ref=m.group(1) or m.group(2); d['js_id_refs'].append({'id':ref,'line':x['line']+x['text'][:m.start()].count('\n'),'exists':ref in ids})
        d['faq_schema']=[]
        for e in d['entities']:
            if e['value'].get('@type')=='Question':
                v=e['value']; ans=v.get('acceptedAnswer',{}); at=ans.get('text','') if isinstance(ans,dict) else str(ans)
                try: plain=norm(html.fragment_fromstring(at,create_parent='div').text_content())
                except Exception: plain=norm(at)
                d['faq_schema'].append({'path':e['path'],'question':norm(v.get('name','')),'answer':plain,'answer_raw':at})
        d['faq_comparison']=[]
        for i in range(max(len(d['faq_visible']),len(d['faq_schema']))):
            v=d['faq_visible'][i] if i<len(d['faq_visible']) else None; j=d['faq_schema'][i] if i<len(d['faq_schema']) else None
            d['faq_comparison'].append({'index':i+1,'visible':v,'schema':j,'question_exact_normalized':bool(v and j and v['question']==j['question']),'answer_exact_normalized':bool(v and j and v['answer']==j['answer'])})
        d['coordinates']=[]
        # All numeric pairs in raw text, percent-decoded URLs, and explicit JSON latitude/longitude objects.
        coord_rx=re.compile(r'(?<![\w.])(-?\d{1,2}\.\d{3,})\s*(?:[,;]|%2[Cc])\s*(-?\d{1,3}\.\d{3,})(?![\w.])')
        for i,line in enumerate(lines):
            decoded=unquote(line)
            for m in coord_rx.finditer(decoded):
                a,c=map(float,m.groups())
                if -90<=a<=90 and -180<=c<=180: d['coordinates'].append({'line':i+1,'pair':list(m.groups()),'context':decoded})
        for e in d['json_objects']:
            v=e['value']
            if 'latitude' in v and 'longitude' in v: d['coordinates'].append({'path':e['path'],'pair':[str(v['latitude']),str(v['longitude'])],'context':v})
        defined={x['id'] for x in d['references'] if not x['reference_only']}
        d['unresolved_ids']=[x for x in d['references'] if x['reference_only'] and x['id'] not in defined]
        d['defined_ids']=dict(Counter(x['id'] for x in d['references'] if not x['reference_only']))
        allrows.append(d)
    byurl={d['canonical']:d for d in allrows}
    for d in allrows:
        for a in d['links']:
            if a['internal']:
                u=urlsplit(a['absolute_url']); key=u._replace(fragment='',query='').geturl(); dest=byurl.get(key)
                a['destination_in_scope']=dest is not None
                if dest is not None and u.fragment: a['target_fragment_exists']=unquote(u.fragment) in dest['ids']
        targets={x['language']:x['expected_url_from_path'] for x in allrows if x['group']==d['group']}
        expected={**targets,'x-default':targets['en']}
        actual=defaultdict(list)
        for x in d['hreflang']: actual[x['hreflang']].append(x['href'])
        d['hreflang_checks']={'expected':expected,'actual':dict(actual),'matches_exactly':dict(actual)=={k:[v] for k,v in expected.items()}}
    (ROOT/'evidence.json').write_text(json.dumps(allrows,ensure_ascii=False,indent=2))
    (ROOT/'js_checks_input.json').write_text(json.dumps(jschecks))
    node=os.environ.get('CODEX_PRIMARY_RUNTIME_NODE','node')
    checker='const fs=require("fs"),vm=require("vm");const data=JSON.parse(fs.readFileSync(process.argv[1],"utf8"));const out=data.map(x=>{try{if(x.kind==="handler")new Function(x.code);else new vm.Script(x.code);return {file:x.file,line:x.line,kind:x.kind,valid:true};}catch(e){return {file:x.file,line:x.line,kind:x.kind,valid:false,error:String(e)};}});process.stdout.write(JSON.stringify(out,null,2));'
    result=subprocess.run([node,'-e',checker,str(ROOT/'js_checks_input.json')],capture_output=True,text=True)
    (ROOT/'js_syntax.json').write_text(result.stdout if result.returncode==0 else json.dumps({'error':result.stderr}))
    print(json.dumps({'files':len(allrows),'jsonld_blocks':sum(len(d['jsonld']) for d in allrows),'json_errors':sum(not b['valid'] for d in allrows for b in d['jsonld']),'js_checks':len(jschecks),'node_exit':result.returncode,'evidence_bytes':(ROOT/'evidence.json').stat().st_size},indent=2))

if __name__=='__main__': run()
