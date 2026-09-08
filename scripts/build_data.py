"""Export scoped proposal records from the manuscript's eight-field audits."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
text = (ROOT / 'paper/SDED-2.0.md').read_text()
fields = {
    'Concept': 'concept', 'Current names': 'current_name_says',
    'Current usage': 'current_name_says', 'Name says': 'current_name_says', 'Names say': 'current_name_says',
    'Hidden': 'hidden_information', 'Origin': 'origin',
    'History value': 'history_value', 'Descriptor': 'candidate_descriptor',
    'Loss': 'loss_from_renaming', 'Alias': 'alias_treatment',
}
pattern = re.compile(r'\b(' + '|'.join(map(re.escape, fields)) + r'): ')
records = []
section = ''
for para in text.split('\n\n'):
    if para.startswith('##'):
        section = para.split('\n')[0].lstrip('# ')
    match = re.match(r'\*\*(.+?)\.\*\* (Concept: .+)', para, re.S)
    if not match:
        continue
    name, body = match.groups()
    marks = list(pattern.finditer(body))
    record = {'id': f'sded:proposal:{len(records)+1:03}', 'label': name,
              'language': 'en', 'section': section, 'status': 'proposed',
              'empirical_validation': 'not assessed',
              'historical_date': None, 'historical_date_status': 'not established in this audit'}
    for i, mark in enumerate(marks):
        end = marks[i+1].start() if i+1 < len(marks) else len(body)
        record[fields[mark.group(1)]] = body[mark.end():end].strip()
    required = set(fields.values())
    missing = required - record.keys()
    if missing:
        raise ValueError(f'{name}: missing {missing}')
    records.append(record)
(ROOT / 'data').mkdir(exist_ok=True)
(ROOT / 'data/examples.json').write_text(json.dumps({
    'protocol_version': '2.0', 'status': 'proposal collection',
    'source': 'paper/SDED-2.0.md',
    'note': 'IDs identify audit proposals, which may discuss multiple concepts. They are not universal concept identifiers. Descriptors and historical labels are not automatically exact aliases.',
    'trademark_marker_required': False, 'records': records,
}, ensure_ascii=False, indent=2) + '\n')
chords = []
for triad, seventh, semitones, symbol, alias in [
 ('major','major',[0,4,7,11],'Cmaj7','major seventh chord'),
 ('major','minor',[0,4,7,10],'C7','dominant seventh chord, quality sense'),
 ('minor','minor',[0,3,7,10],'Cm7','minor seventh chord'),
 ('minor','major',[0,3,7,11],'Cm(maj7)','minor-major seventh chord'),
 ('diminished','minor',[0,3,6,10],'Cm7(b5)','half-diminished seventh chord'),
 ('diminished','diminished',[0,3,6,9],'Cdim7','fully diminished seventh chord'),
 ('augmented','minor',[0,4,8,10],'C7(#5)','augmented seventh chord'),
 ('augmented','major',[0,4,8,11],'Cmaj7(#5)','augmented major seventh chord'),
]:
 chords.append({'id':f'sded:chord-quality:{triad}-{seventh}',
  'descriptive_name':f'{triad.capitalize()} triad with {seventh} seventh above its root',
  'triad_quality':triad,'seventh_quality':seventh,
  'root_relative_semitones_12tet':semitones,'example_symbol_on_C':symbol,
  'conventional_alias':alias,'contextual_function':None,
  'scope':'Tertian chord construction in the stated Western notation profile; actual voicing may omit tones.',
  'naming_recommendation_status':'proposed','trademark_marker_required':False})
(ROOT / 'data/chord-quality-matrix.json').write_text(json.dumps(chords,indent=2)+'\n')
print(f'Exported {len(records)} eight-field audits and {len(chords)} chord-quality records.')
