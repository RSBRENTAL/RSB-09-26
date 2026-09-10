from audit import *

D=json.loads((ROOT/'evidence.json').read_text())
derived=[]
for d in D:
    dom=html.fromstring(Path(d['local_path']).read_text())
    out={'group':d['group'],'language':d['language'],'tests':{},'price_rows':[],'selectors':[],'review_checks':[]}
    test=out['tests']
    test['one_title']=len(d['titles'])==1
    test['one_description']=len(d['metas'].get('description',[]))==1
    test['one_canonical']=len(d['canonicals'])==1
    test['canonical_own_path']=d['canonical']==d['expected_url_from_path']
    test['no_duplicate_head_singletons']=all(len(v)==1 for k,v in d['metas'].items() if k!='og:locale:alternate')
    test['no_noindex_nofollow']=all(not re.search(r'\b(?:noindex|nofollow|none)\b',v['value'],re.I) for k,vs in d['metas'].items() if k.lower() in ['robots','googlebot','bingbot'] for v in vs)
    test['one_h1']=len([x for x in d['headings'] if x['tag']=='h1'])==1
    test['nonempty_headings']=all(x['text'] for x in d['headings'])
    loc={'en':'en_GB','es':'es_ES','fr':'fr_FR','it':'it_IT','de':'de_DE','nl':'nl_NL','pt':'pt_PT','ca':'ca_ES','sv':'sv_SE','pl':'pl_PL'}
    test['og_locale']=d['metas'].get('og:locale',[{}])[0].get('value')==loc[d['language']]
    test['og_alternates']=sorted(v['value'] for v in d['metas'].get('og:locale:alternate',[]))==sorted(v for k,v in loc.items() if k!=d['language'])
    test['og_url']=d['metas'].get('og:url',[{}])[0].get('value')==d['canonical']
    test['no_meta_refresh_base']=not dom.xpath('//base|//meta[translate(@http-equiv,"REFSH","refsh")="refresh"]')
    test['json_all_valid']=all(b['valid'] and not b['duplicate_keys'] for b in d['jsonld'])
    test['all_references_resolved']=not d['unresolved_ids']
    test['html_stack_balanced']=not d['token_errors'] and not d['unclosed_stack']
    test['textual_structure_balanced']=all(v['text_open']==v['text_close']==v['parsed'] for v in d['structure'].values())
    test['ids_unique']=not d['duplicate_ids']
    test['id_references_exist']=all(x['exists'] for x in d['id_references']+d['js_id_refs'])
    test['internal_fragments_exist']=all(x.get('same_page_fragment_exists') is not False and x.get('target_fragment_exists') is not False for x in d['links'])
    test['img_alt_present']=all('alt' in x for x in d['images'] if x['tag']=='img')
    test['links_named']=all(x['accessible_name_static'] for x in d['links'] if x['tag']=='a')
    test['no_nested_interactives']=not any(x['parent_interactive'] for x in d['controls'])
    test['no_positive_tabindex']=not any(int(x['attrs'].get('tabindex','0'))>0 for x in d['controls'] if re.fullmatch(r'-?\d+',x['attrs'].get('tabindex','0')))
    test['no_javascript_hrefs']=not any(x['raw_href'].strip().lower().startswith('javascript:') for x in d['links'])
    test['blank_rel']=all(set((x.get('rel') or '').split())&{'noopener','noreferrer'} for x in d['links'] if x.get('target')=='_blank')
    test['faq_visible_schema']=all(x['question_exact_normalized'] and x['answer_exact_normalized'] for x in d['faq_comparison'])
    out['forms']=[{'line':x.sourceline,'attrs':dict(x.attrib)} for x in dom.xpath('//form')]
    out['buttons_without_names']=[{'line':x.sourceline,'attrs':dict(x.attrib)} for x in dom.xpath('//button') if not (txt(x) or x.get('aria-label') or x.get('aria-labelledby') or x.get('title'))]
    test['buttons_named']=not out['buttons_without_names']
    out['selectors']=[]
    selector_lines=set()
    for x in cls(dom,'dropdown-menu'):
        aa=x.xpath('.//a[@href]')
        if not aa: continue
        arr=[{'line':a.sourceline,'text':txt(a),'href':a.get('href'),'attrs':dict(a.attrib)} for a in aa]
        selector_lines.update((a['line'],a['href']) for a in arr)
        out['selectors'].append({'line':x.sourceline,'id':x.get('id'),'links':arr,'selected':[a for a in arr if a['attrs'].get('aria-current') or 'active' in (a['attrs'].get('class') or '').split()]})
    expected=d['hreflang_checks']['expected']; expected.pop('x-default',None)
    test['selectors_match_hreflang']=len(out['selectors'])==2 and all(Counter(a['href'] for a in sel['links'])==Counter(expected.values()) for sel in out['selectors'])
    test['selectors_current_page']=all(len(sel['selected'])==1 and sel['selected'][0]['href']==d['canonical'] for sel in out['selectors'])
    out['cross_language_nonselector']=[x for x in d['links'] if x['tag']=='a' and x['internal'] and x['destination_language']!=d['language'] and (x['line'],x['raw_href']) not in selector_lines]
    test['links_language']=not out['cross_language_nonselector']
    for x in cls(dom,'price-line'):
        a=cls(x,'label'); v=cls(x,'value')
        if a and v:
            ancestors=x.xpath('ancestor::section[@id]'); sec=ancestors[-1].get('id') if ancestors else None
            out['price_rows'].append({'section':sec,'line':x.sourceline,'label':txt(a[0]),'value':txt(v[0])})
    out['home_from_prices']=[]
    if d['group']=='HOME':
        for x in dom.xpath('//article'):
            values=x.xpath('.//text()[contains(.,"€")]')
            if values: out['home_from_prices'].append({'line':x.sourceline,'headings':[txt(e) for e in x.xpath('.//h2|.//h3')],'prices':[norm(str(v)) for v in values]})
    out['schema_offers']=[e for e in d['entities'] if e['value'].get('@type') in ['Offer','AggregateOffer']]
    out['id_property_conflicts']=[]
    props=defaultdict(lambda:defaultdict(list))
    for e in d['json_objects']:
        v=e['value']
        if '@id' not in v or len(v)==1: continue
        for key,value in v.items():
            if key in ['@id','@type']: continue
            props[v['@id']][key].append({'block':e['block'],'path':e['path'], 'value':value})
    for id,ps in props.items():
        for p,vs in ps.items():
            if len({json.dumps(v['value'],sort_keys=True,ensure_ascii=False) for v in vs})>1: out['id_property_conflicts'].append({'id':id,'property':p,'values':vs})
    for e in [e for e in d['entities'] if e['value'].get('@type')=='Review']:
        v=e['value']; author=v.get('author',{}).get('name'); body=norm(v.get('reviewBody','')).strip('"“”„«»')
        card=next((c for c in d['review_cards'] if author in c['text']),None)
        allbody=norm(' '.join(t['text'] for t in d['body_text_nodes']))
        source=card['text'] if card else allbody
        out['review_checks'].append({'schema':v,'line':card['line'] if card else None,'visible_card':card,'author_visible':author in source,'body_exact_substring':body in source,'date_visible':v.get('datePublished') in source if v.get('datePublished') else None})
    test['reviews_visible_schema']=all(x['author_visible'] and x['body_exact_substring'] and x['date_visible'] is not False for x in out['review_checks'])
    out['global_entities']=[e for e in d['entities'] if e['value'].get('@type') in ['Organization','WebSite','LocalBusiness']]
    out['global_checks']=[]
    expectedids={'Organization':BASE+'#organization','WebSite':BASE+'#website','LocalBusiness':BASE+'#business'}
    for e in out['global_entities']:
        v=e['value']; typ=v['@type']
        if '@id' in v: out['global_checks'].append({'path':e['path'],'property':'@id','actual':v['@id'],'expected':expectedids[typ],'equal':v['@id']==expectedids[typ]})
        if 'url' in v and '@id' in v: out['global_checks'].append({'path':e['path'],'property':'url','actual':v['url'],'expected':BASE,'equal':v['url']==BASE})
        if typ=='LocalBusiness' and 'address' in v:
            expected_address={'streetAddress':'Carrer de Salvador Espriu, 63','addressLocality':'Barcelona','addressRegion':'Catalonia','postalCode':'08005','addressCountry':'ES'}
            for key,val in expected_address.items():out['global_checks'].append({'path':e['path']+'.address','property':key,'actual':v['address'].get(key),'expected':val,'equal':v['address'].get(key)==val})
            periods={ (tuple(z['dayOfWeek']),z['opens'],z['closes']) for z in v.get('openingHoursSpecification',[]) }
            days=tuple('Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split())
            test['schema_hours_canonical']=periods=={(days,'10:30','13:30'),(days,'16:30','20:00')}
    test['global_identity_canonical']=all(x['equal'] for x in out['global_checks'])
    test['coordinates_canonical']=all(tuple(x['pair'])==('41.3906488','2.1984312') for x in d['coordinates'])
    full=Path(d['local_path']).read_text()
    test['no_old_coordinates']=not re.search(r'41\.390577|2\.198362',full)
    out['numeric_body_sequence']=re.findall(r'\d+(?:[.,]\d+)?',norm(' '.join(x['text'] for x in d['body_text_nodes'])))
    out['all_phones']=sorted(set(re.findall(r'(?:\+34\s*|tel:\+?34|wa\.me/34)\d[\d\s]{7,16}',full)))
    out['all_emails']=sorted(set(re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',full)))
    out['map_ids']={k:sorted(set(re.findall(rx,full))) for k,rx in {'Google CID':r'cid=(\d+)','Apple Place ID':r'place-id=([A-Za-z0-9]+)','Bing YPID':r'ypid=([^&"\s]+)'}.items()}
    # Readable per-file extraction of all text in main, with separately verified reviews preserved in evidence.
    main=dom.xpath('//main')[0]
    semantic=[]
    for child in main:
        if not isinstance(child.tag,str): continue
        if child.tag in ['script','style']:continue
        if child.get('id')=='reviews':continue
        semantic.append(f'L{child.sourceline}: '+txt(child))
    out['semantic_main']='\n'.join(semantic)
    derived.append(out)
(ROOT/'derived.json').write_text(json.dumps(derived,ensure_ascii=False,indent=2))
print('FALSE TESTS')
for d in derived:
    failed=[k for k,v in d['tests'].items() if not v]
    if failed:print(d['group'],d['language'],failed)
print('REVIEW MISMATCHES')
for d in derived:
    for x in d['review_checks']:
        if not x['author_visible'] or not x['body_exact_substring'] or x['date_visible'] is False:print(d['group'],d['language'],x['schema']['author'],x['schema']['reviewBody'],x['visible_card'])
print('GRAPH CONFLICTS')
for d in derived:
    if d['id_property_conflicts']: print(d['group'],d['language'],[(x['property'], [v['value'] for v in x['values']] if x['property']!='sameAs' else 'Listas complementarias; no es contradicción') for x in d['id_property_conflicts']])
