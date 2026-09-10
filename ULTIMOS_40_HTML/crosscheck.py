from pathlib import Path
from lxml import html
from urllib.parse import urljoin,urlsplit,unquote
import json,csv,collections
R=Path(__file__).resolve().parent;old=R.parent/'unified_160';D=json.loads((R/'evidence.json').read_text());prices=json.loads((old/'AUDITORIAS_ORIGINALES/40_HTML/evidencia/evidence.json').read_text());P=json.loads((R/'price_validation.json').read_text());out=[]
for p in P:
 if not p['offers']:continue
 ref=next(x for x in prices if x['group']=='PRICES' and x['language']==p['language']);url=next(d['canonical'] for d in D if (d['group'],d['language'])==(p['group'],p['language']))
 offers=[e['value'] for e in ref['entities'] if e['value'].get('@type')=='Offer' and e['value'].get('url')==url]
 actual=[(o['name'],float(o['price'])) for o in p['offers']];expected=[(o['name'],float(o['price'])) for o in offers]
 out.append({'group':p['group'],'language':p['language'],'service_offers':actual,'prices_offers':expected,'base_prices_match':[x[1] for x in actual]==[x[1] for x in expected[:6]],'accessory':p.get('accessories',[])})
files=[]
with (old/'MATRICES/inventario_160.csv').open(encoding='utf-8-sig') as f:
 for x in csv.DictReader(f):files.append((x['canonical'],old/x['ruta_unificada']))
files += [(d['canonical'],Path(d['local_path'])) for d in D]
ids={u:set(html.fromstring(p.read_bytes()).xpath('//@id')) for u,p in files};links=[]
for u,p in files:
 dom=html.fromstring(p.read_bytes())
 for e in dom.xpath('//a[@href]'):
  dest=urlsplit(urljoin(u,e.get('href')));target=dest._replace(query='',fragment='').geturl()
  if dest.netloc!='rentalscooterbarcelona.com':continue
  links.append({'source':u,'line':e.sourceline,'href':e.get('href'),'target':target,'in_corpus':target in ids,'fragment_ok':not dest.fragment or unquote(dest.fragment) in ids.get(target,set()) if target in ids else None})
(R/'cross_200.json').write_text(json.dumps({'prices_against_PRICES':out,'links':links},ensure_ascii=False,indent=2))
print('price',len(out),'fail',[x for x in out if not x['base_prices_match']]);print('links',len(links),'outside',collections.Counter(x['target'] for x in links if not x['in_corpus']),'badfrags',[x for x in links if x['fragment_ok'] is False])
