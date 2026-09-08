"""Recover previous vocabulary without executing historical PDF builders."""
import ast
import hashlib
import html
import json
import re
from collections import OrderedDict
from pathlib import Path
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]
PAIR=re.compile(r'(?P<name>.*?)\s*\((?P<legacy>[^()]*(?:\([^()]*\)[^()]*)?)™\s*,?\s*est\.\s*(?P<date>[^)]+)\)',re.S)
records=OrderedDict()
counts={}

def clean(s):
 return ' '.join(html.unescape(re.sub(r'<[^>]+>','',s)).split())

def add(name,legacy,date,domain,subdomain,source,primary=False):
 name=clean(name).strip(' .,:;•\x7f')
 legacy=clean(legacy);date=clean(date)
 if not name or len(name)>160:raise ValueError((name,legacy,source))
 key=(name,legacy,date)
 if key not in records:
  records[key]={'id':'sded:inherited:'+hashlib.sha256('\0'.join(key).encode()).hexdigest()[:12],
   'descriptive_name':name,'historical_name':legacy,'established_date':date,
   'domain':domain,'subdomain':subdomain,'status':'inherited vocabulary',
   'date_status':'as recorded in prior version; not independently revalidated',
   'sources':[],'latest_revision_b':False}
 item=records[key]
 if source not in item['sources']:item['sources'].append(source)
 if primary:
  item.update(domain=domain,subdomain=subdomain,latest_revision_b=True)
 counts[source]=counts.get(source,0)+1

def pairs(s,domain,subdomain,source,primary=False,definitions=False):
 s=clean(s)
 for m in PAIR.finditer(s):
  name=m['name'].strip(' .,:;•\x7f')
  if source.endswith('.pdf'):
   name=name.rsplit('. ',1)[-1]
   if '] ' in name:name=name.rsplit('] ',1)[-1]
   name=re.sub(r'^\d+\s+','',name)
  if definitions:name=name.split(':')[0]
  add(name,m['legacy'],m['date'],domain,subdomain,source,primary)

for filename in ['build_sded_v1_2_RevisionB_full.py','expanded_libraries.py']:
 tree=ast.parse((ROOT/filename).read_text());domain='';subdomain='GENERAL'
 calls=sorted([n for n in ast.walk(tree) if isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id=='Paragraph'],key=lambda n:n.lineno)
 for n in calls:
  if not n.args or not isinstance(n.args[0],ast.Constant):continue
  s=n.args[0].value
  if not isinstance(s,str):continue
  style=n.args[1].id if len(n.args)>1 and isinstance(n.args[1],ast.Name) else ''
  if style=='domain_style':domain=clean(s).split("'")[1]
  elif style=='subdomain_style':subdomain=re.search(r'\[([^\]]+)\]',s)[1]
  elif style=='library_entry_style':pairs(s,domain,subdomain,filename,filename.startswith('build_'))

filename='build_sded_v1_2_full.py'
tree=ast.parse((ROOT/filename).read_text())
for n in tree.body:
 if isinstance(n,ast.Assign) and isinstance(n.value,ast.List) and isinstance(n.targets[0],ast.Name) and n.targets[0].id.endswith('_entries'):
  domain=n.targets[0].id[:-8].replace('_',' ').upper()
  domain={'MATH':'MATHEMATICS','CS':'COMPUTER SCIENCE'}.get(domain,domain)
  for v in n.value.elts:
   if not isinstance(v,ast.Constant):continue
   s=v.value;title=re.search(r'<b>(.*?)</b>',s)[1].rstrip(':')
   m=PAIR.search(clean(s))
   if m:add(title,m['legacy'],m['date'],domain,'EARLIER VOCABULARY',filename)

# The PDFs include material absent from the currently retained builders.
for path in sorted(ROOT.glob('*.pdf')):
 text='\n'.join(page.extract_text() for page in PdfReader(path).pages)
 # Ignore specification examples; begin at the actual vocabulary body.
 starts=list(re.finditer(r'^\'?MATHEMATICS(?:\' Approved| \[)',text,re.M))
 if not starts:raise ValueError(f'Vocabulary start not found: {path.name}')
 text=text[starts[0].start():]
 domain='MATHEMATICS';subdomain='EARLIER VOCABULARY';buf=[]
 def flush():
  if buf:
   pairs(' '.join(buf),domain,subdomain,path.name,definitions='RevisionB' not in path.name and 'Protocol_' not in path.name)
   buf.clear()
 for line in text.splitlines():
  line=line.strip()
  d=re.match(r"^'([A-Z &]+)' Approved (?:Vocabulary|Library)$",line)
  oldd=re.match(r'^([A-Z &]+) \[',line)
  sub=re.match(r'^[•\x7f]?\s*\[([^\]]+)\]:',line)
  if d or oldd:
   flush();domain=(d or oldd)[1];subdomain='EARLIER VOCABULARY';continue
  if sub:
   flush();subdomain=sub[1];continue
  if line.startswith(('Appendix','Suggested Zenodo','{','"title"')):
   flush();break
  if line:buf.append(line)
 flush()

(ROOT/'data/inherited-vocabulary.json').write_text(json.dumps({'source_counts':counts,'records':list(records.values())},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'source_counts':counts,'unique_mappings':len(records),'latest_revision_b':sum(r['latest_revision_b'] for r in records.values())},indent=2))

# The new library contains actual name pairs, not the prose audit records.
import csv
new=list(csv.DictReader((ROOT/'data/new-vocabulary.tsv').open(),delimiter='\t'))
for row in new:
 row['id']='sded:new:'+hashlib.sha256((row['domain']+'\0'+row['historical_name']+'\0'+row['descriptive_name']).encode()).hexdigest()[:12]
 row['status']='proposed addition'
 row['trademark_marker_required']=False
 row['source']='SDED 2.0 case studies; naming expansion prepared in this revision'
(ROOT/'data/new-vocabulary.json').write_text(json.dumps(new,ensure_ascii=False,indent=2)+'\n')

out=['# SDED 2.0: Vocabulary Index',
 'Brian Wijaya | September 8, 2026 | Publication candidate',
 'This is the compact vocabulary layer of SDED 2.0. It restores the names from earlier Approved Vocabulary libraries and adds explicit new name pairs. Domain and bracketed subdomain headings organize period-separated entries, as in the prior reference format.',
 f'The recovered prior library contains **{len(records)} distinct name/date mappings**: **{sum(r["latest_revision_b"] for r in records.values())}** from the latest Revision B and **{sum(not r["latest_revision_b"] for r in records.values())}** additional mappings from earlier artifacts. The new library contains **{len(new)} proposed name pairs**. An earlier wording is retained as an earlier variant rather than silently disappearing.',
 'Format: `Descriptive Name ("Historical Name", est. date)`. Neither ™ nor `(TM)` is necessary; either remains acceptable. Earlier dates are reproduced as recorded, not newly verified. Unknown dates on new entries mean that first use has not been established. The dates 1963, 1980, and 1641 refer to the specified Gettier, Searle, and Descartes publications, not verified coinage of their later labels.',
 'The inherited label *Approved Vocabulary* records the earlier version\'s status. It does not erase the specific semantic concerns identified in the 2.0 paper. Those mappings remain findable, with a short review note after the libraries. Descriptive guides in Part C are marked as such because they orient the reader without replacing a historical or cultural identity.',
 '## A. New vocabulary additions']

def entry(r):
 return r['descriptive_name']+' ("'+r['historical_name']+'", est. '+r['established_date']+')'

def groups(items,heading_suffix):
 groups=OrderedDict()
 for r in items:groups.setdefault(r['domain'],OrderedDict()).setdefault(r['subdomain'],[]).append(r)
 result=[]
 for domain,subs in groups.items():
  result.append('### '+domain+' — '+heading_suffix)
  for sub,items in subs.items():
   result.append('#### ['+sub+']')
   result.append('. '.join(entry(r) for r in items)+'.')
 return result

out.append('These are proposed construction or sense-specific names. The historical alias remains available. In music, seventh and extension intervals are measured above the chord root; mode alterations use major-reference degrees. Scale-degree terms are indexed in their degree sense, not every functional sense. Symbols and actual voicings remain separate.')
out+=groups([r for r in new if r['relation']=='scoped replacement'],'New Vocabulary')
out.append('## B. Earlier Approved Vocabulary, carried forward')
out.append('The following restores the complete latest Revision B library, including its established descriptive names, historical names, dates, and domain/subdomain placement. Formatting alone changes to the quoted-name convention. Content revisions require an explicit correction record.')
out+=groups([r for r in records.values() if r['latest_revision_b']],'Approved Vocabulary — Carried Forward')
out.append('## C. Descriptive guides with historical names retained')
out.append('The left-hand expressions below are orienting descriptions. They are not exact replacement aliases. The named argument, system, or cultural tradition remains the preferred identity where that is its role. These guides are separated from the new replacement names so that the familiar parenthetical display cannot imply false equivalence.')
out+=groups([r for r in new if r['relation']=='orientation'],'Descriptive Guides')
out.append('## D. Additional names from earlier versions')
out.append('These distinct earlier mappings supplement Part B. They include alternative descriptive names, additional historical aliases, and different recorded dates. Presence here preserves retrieval and lineage; it does not declare competing variants interchangeable in every use.')
out+=groups([r for r in records.values() if not r['latest_revision_b']],'Earlier Vocabulary Variants')
out.append('## E. Mapping notes')
out.append('### Inherited mappings needing semantic review')
out.append('The following previously established mappings remain in the index, with their issues explicit: **Unique-Factorization Domain / Dedekind Domain** conflates distinct algebraic properties; **Power Series / Taylor Series** is broader than the intended series type; **Topological-Completeness Space / Hilbert Space** omits the inner-product requirement; **Continuous-Map Fixed-Point Theorem / Brouwer Fixed-Point Theorem** omits distinguishing assumptions; **Energy-Function Stability / Lyapunov Stability** risks substituting a proof method for a property; **Thesis-Antithesis-Synthesis Dialectic / Hegelian Dialectic** compresses a disputed historical interpretation. These are carried forward for continuity, not silently reaffirmed as technically equivalent. See the manuscript\'s historical critique and its semantic-equivalence rule.')
out.append('### Scope of the new mappings')
out.append('| Historical name | Indexed descriptor and scope |\n|---|---|')
for r in new:out.append('| '+r['historical_name']+' | **'+r['descriptive_name']+'**. '+r['scope']+' |')
out.append('### Recovery coverage')
out.append('| Earlier artifact | Extracted vocabulary entries |\n|---|---|')
for source,count in counts.items():out.append('| '+source+' | '+str(count)+' |')
out.append('Counts are occurrences within each source; the same pair can occur in several artifacts. The union retains exact descriptive names, historical names, and date strings. The builder is parsed as data and is never executed during recovery. These files are the recovered v1.2 vocabulary artifacts; no claim is made here that an unavailable deposited v1.0/v1.1 PDF was recovered or that all its demonstration names have been independently compared.')
(ROOT/'vocabulary/SDED-2.0-vocabulary.md').write_text('\n\n'.join(out).replace('|\n\n|','|\n|')+'\n')

reverse=['# SDED 2.0: Alphabetical Historical-Name Lookup','Each line points from a historical name to its indexed descriptive name and library. This lookup does not merge distinct senses.']
for r in sorted(list(records.values())+new,key=lambda r:(r['historical_name'].casefold(),r['descriptive_name'].casefold())):
 lib='New proposal' if r in new else 'Latest prior library' if r['latest_revision_b'] else 'Earlier variant'
 reverse.append('- **'+r['historical_name']+'** → '+r['descriptive_name']+' — '+r['domain']+' / '+r['subdomain']+'; '+lib+'.')
(ROOT/'vocabulary/HISTORICAL-NAME-LOOKUP.md').write_text('\n\n'.join(reverse)+'\n')
print('Rendered compact index with',len(records),'inherited mappings and',len(new),'new pairs.')

analysis=(ROOT/'paper/SDED-2.0.md').read_text().split('## Abstract',1)[1]
index=(ROOT/'vocabulary/SDED-2.0-vocabulary.md').read_text().split('\n\n',2)[2]
combined='# SDED 2.0: Specification and Expanded Vocabulary\n\n## Self-Documenting Terminology in Music, Philosophy, and the Arts and Humanities\n\nBrian Wijaya | September 8, 2026 | Version 2.0 publication candidate | CC BY 4.0\n\n'+index+'\n\n## Framework and case studies\n\nThe following paper provides the rationale, audits, and research agenda supporting the vocabulary reference above.\n\n## Abstract'+analysis
(ROOT/'SDED-2.0.md').write_text(combined)
