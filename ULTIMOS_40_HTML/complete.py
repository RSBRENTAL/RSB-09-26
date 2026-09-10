from pathlib import Path
import json,re,collections
from lxml import html
R=Path(__file__).resolve().parent
def read(n):return json.loads((R/n).read_text())
def save(n,x):(R/n).write_text(json.dumps(x,ensure_ascii=False,indent=2))
D=read('evidence.json');DR=read('derived.json');P=read('price_validation.json');F=[]
for d,r,p in zip(D,DR,P):
 raw=Path(d['local_path']).read_text();dom=html.fromstring(raw)
 if d['group']=='09_LOCATION_CONTACT':
  d['faq_visible']=[{'line':e.sourceline,'question':' '.join(e.xpath('.//h3')[0].text_content().split()),'answer':' '.join(e.xpath('.//p')[0].text_content().split()),'links':[]} for e in dom.xpath('//*[@id="faq"]//article')]
  d['faq_comparison']=[{'index':i+1,'visible':v,'schema':s,'question_exact_normalized':v['question']==s['question'],'answer_exact_normalized':v['answer']==s['answer']} for i,(v,s) in enumerate(zip(d['faq_visible'],d['faq_schema']))]
  r['tests']['faq_visible_schema']=len(d['faq_visible'])==len(d['faq_schema']) and all(v['question_exact_normalized'] and v['answer_exact_normalized'] for v in d['faq_comparison'])
 compact=[]
 for e in dom.xpath('//main//div[count(span)=2]'):
  spans=e.xpath('./span');t=' '.join(spans[-1].text_content().split());m=re.fullmatch(r'€\s*(\d+)|(\d+)\s*€',t)
  if m:compact.append({'line':e.sourceline,'text':' '.join(e.text_content().split()),'price':float(m.group(1) or m.group(2))})
 p['compact']=compact
 if p['cards']:
  p['comparisons'].append({'test':'compact_matches_cards','actual':[v['price'] for v in compact],'expected':[v['price'] for v in p['cards']],'pass':[v['price'] for v in compact]==[v['price'] for v in p['cards']]})
 for c in r['id_property_conflicts']:
  if c['property']!='dateModified':continue
  ev=[{'line':i+1,'code':line.strip()} for i,line in enumerate(raw.splitlines()) if '"dateModified"' in line]
  F.append({'unified_id':'U03','group':d['group'],'language':d['language'],'canonical':d['canonical'],'archive_path':d['archive_path'],'element':c['id']+'.dateModified','current':' / '.join(v['value'] for v in c['values']),'recommended':'Conservar una única fecha real de última modificación, pendiente de registro editorial. No elegir automáticamente la más reciente.','evidence':ev,'why':'Dos valores de dateModified para la misma entidad WebPage.','impact':'Ambigüedad temporal del grafo; el JSON sigue siendo válido.','expected_edits':'Consolidar la propiedad en los dos bloques; fecha real pendiente.'})
 if (d['group'],d['language']) in [('06_QUADS','de'),('07_SKATEBOARD','nl')]:
  el=next(e for e in dom.xpath('//main//p') if '/blog/' in ''.join(e.xpath('.//@href')));verb='lesen' if d['language']=='de' else 'lezen';ln=next((i+1,l) for i,l in enumerate(raw.splitlines()) if 'Für lokale Routenideen' in l or 'Voor lokale route-ideeën' in l)
  before='</a>.';after='</a> '+verb+'.';assert before in ln[1]
  F.append({'unified_id':'U05','group':d['group'],'language':d['language'],'canonical':d['canonical'],'archive_path':d['archive_path'],'element':'Párrafo de enlace a la guía','current':' '.join(el.text_content().split()),'recommended':ln[1].replace(before,after),'evidence':[{'line':ln[0],'code':ln[1].strip()}],'why':'La construcción modal queda sin infinitivo final.','impact':'Frase incompleta en alemán/neerlandés.','expected_edits':'Una inserción de '+verb+' al final del enlace; conservar URL.'})
save('evidence.json',D);save('derived.json',DR);save('price_validation.json',P);save('findings.json',F)
print('findings',collections.Counter(f['unified_id'] for f in F));print('prices failures',[(p['group'],p['language'],c) for p in P for c in p['comparisons'] if not c['pass']]);print('derived failures',collections.Counter(k for d in DR for k,v in d['tests'].items() if v is False))
