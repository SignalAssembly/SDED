"""Build the reading edition using ReportLab. Requires reportlab and local fonts."""
import html
import os
import re
from pathlib import Path
from reportlab import rl_config
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
    Spacer, PageBreak, LongTable, TableStyle)
from reportlab.platypus.tableofcontents import TableOfContents

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output/pdf/SDED-2.0.pdf'
OUT.parent.mkdir(parents=True, exist_ok=True)
rl_config.warnOnMissingFontGlyphs = 1
fontdir = Path(os.environ.get('SDED_FONT_DIR', '/Library/Fonts'))
for name, filename in [('Body','Lato-Regular.ttf'),('BodyBold','Lato-Bold.ttf'),
                       ('BodyItalic','Lato-Italic.ttf'),('BodyBoldItalic','Lato-BoldItalic.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(fontdir / filename)))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='BodyBold',italic='BodyItalic',boldItalic='BodyBoldItalic')
fallback = Path(os.environ.get('SDED_FALLBACK_FONT', '/Library/Fonts/Arial Unicode.ttf'))
pdfmetrics.registerFont(TTFont('Fallback', str(fallback)))
body_chars = pdfmetrics.getFont('Body').face.charToGlyph
fallback_chars = pdfmetrics.getFont('Fallback').face.charToGlyph
source = (ROOT / 'paper/SDED-2.0.md').read_text()
missing = sorted({c for c in source if ord(c)>31 and ord(c) not in body_chars and ord(c) not in fallback_chars})
if missing:
    raise ValueError(f'No font coverage for {missing!r}')

def esc(s):
    return ''.join(html.escape(c) if ord(c) in body_chars or c.isspace()
                   else '<font name="Fallback">'+html.escape(c)+'</font>' for c in s)

inline_pattern = re.compile(r'\[([^\]]+)\]\((https?://[^\s)]+(?:\([^)]*\)[^\s)]*)?)\)|\*\*(.+?)\*\*|`([^`]+)`|\*([^*]+)\*')
def rich(s):
    if re.match(r'\*\*.+?\.\*\* Concept:', s):
        s = re.sub(r'\b(Concept|Current names|Current usage|Name says|Names say|Hidden|Origin|History value|Descriptor|Loss|Alias):', r'**\1:**', s)
    out=[]; last=0
    for m in inline_pattern.finditer(s):
        out.append(esc(s[last:m.start()]))
        if m.group(1):
            out.append('<link href="'+html.escape(m.group(2),quote=True)+'" color="#235e77">'+esc(m.group(1))+'</link>')
        elif m.group(3): out.append('<b>'+esc(m.group(3))+'</b>')
        elif m.group(4): out.append('<font color="#2b5361">'+esc(m.group(4))+'</font>')
        else: out.append('<i>'+esc(m.group(5))+'</i>')
        last=m.end()
    out.append(esc(s[last:]))
    return ''.join(out)

styles={
 'body':ParagraphStyle('body',fontName='Body',fontSize=10.3,leading=14.5,spaceAfter=8.5,textColor=colors.HexColor('#202c34'),splitLongWords=True),
 'title':ParagraphStyle('title',fontName='BodyBold',fontSize=25,leading=30,spaceAfter=17,textColor=colors.HexColor('#163e4d')),
 'subtitle':ParagraphStyle('subtitle',fontName='Body',fontSize=14,leading=19,spaceAfter=16,textColor=colors.HexColor('#526772')),
 'h2':ParagraphStyle('h2',fontName='BodyBold',fontSize=16,leading=20,spaceBefore=19,spaceAfter=9,keepWithNext=True,textColor=colors.HexColor('#163e4d')),
 'h3':ParagraphStyle('h3',fontName='BodyBold',fontSize=12.2,leading=16,spaceBefore=13,spaceAfter=7,keepWithNext=True,textColor=colors.HexColor('#235e77')),
 'table':ParagraphStyle('table',fontName='Body',fontSize=8.3,leading=11.3,spaceAfter=0,splitLongWords=True),
 'bullet':ParagraphStyle('bullet',fontName='Body',fontSize=10.3,leading=14.5,leftIndent=14,firstLineIndent=-10,spaceAfter=6.5),
 'reference':ParagraphStyle('reference',fontName='Body',fontSize=8.3,leading=11.5,spaceAfter=8,splitLongWords=True),
}
class Document(BaseDocTemplate):
    def afterFlowable(self, flowable):
        if hasattr(flowable,'toc_label'):
            key=flowable.toc_key
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(flowable.toc_label,key,0,False)
            self.notify('TOCEntry',(0,flowable.toc_label,self.page,key))

def page(c, doc):
    c.saveState()
    c.setStrokeColor(colors.HexColor('#cbd7da')); c.setLineWidth(.5)
    c.line(48,749,564,749)
    c.setFillColor(colors.HexColor('#526772'));c.setFont('Body',8)
    c.drawString(48,759,'SDED 2.0  /  Brian Wijaya  /  Publication candidate')
    c.drawRightString(564,30,str(doc.page))
    c.drawString(48,30,'Self-Documenting Terminology for the Arts and Humanities')
    c.restoreState()

doc=Document(str(OUT),pagesize=letter,leftMargin=48,rightMargin=48,topMargin=57,bottomMargin=51,
             title='SDED 2.0: Self-Documenting Terminology for the Arts and Humanities',
             author='Brian Wijaya',subject='Conceptual framework, naming protocol, and research agenda')
doc.addPageTemplates(PageTemplate(id='main',frames=[Frame(48,51,516,684,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=page))
story=[]; lines=source.splitlines(); i=0; keynum=0
while i<len(lines):
    line=lines[i].strip()
    if not line: i+=1;continue
    if line.startswith('|'):
        rows=[]
        while i<len(lines) and lines[i].strip().startswith('|'):
            row=lines[i].strip().strip('|').split('|')
            if not all(re.fullmatch(r'\s*:?-+:?\s*',x) for x in row):
                rows.append([Paragraph(rich(x.strip()),styles['table']) for x in row])
            i+=1
        n=len(rows[0]); widths=[516/n]*n
        if n==2: widths=[170,346]
        table=LongTable(rows,colWidths=widths,repeatRows=1,hAlign='LEFT')
        table.setStyle(TableStyle([
          ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dce9ec')),
          ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.HexColor('#f6f8f9'),colors.white]),
          ('VALIGN',(0,0),(-1,-1),'TOP'),
          ('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),
          ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),
          ('LINEBELOW',(0,0),(-1,0),.6,colors.HexColor('#7998a3')),
          ('LINEBELOW',(0,1),(-1,-1),.25,colors.HexColor('#d8e1e4'))]))
        story += [table,Spacer(1,10)];continue
    if line.startswith('#'):
        hashes=len(line)-len(line.lstrip('#')); title=line.lstrip('# ')
        if title.startswith('1. The problem'):
            story.append(PageBreak())
            story.append(Paragraph('Contents',styles['h2']))
            toc=TableOfContents();toc.levelStyles=[ParagraphStyle('toc',fontName='Body',fontSize=9.5,leading=12,spaceBefore=0,spaceAfter=0)]
            story += [toc,PageBreak()]
        style='title' if hashes==1 else ('subtitle' if title=='Naming as an Engineered Knowledge Interface' else 'h2' if hashes==2 else 'h3')
        p=Paragraph(rich(title),styles[style])
        if hashes==2 and (re.match(r'\d+\.',title) or title.startswith('Appendix')):
            keynum+=1;p.toc_label=title;p.toc_key=f'section-{keynum}'
        story.append(p);i+=1;continue
    if re.match(r'^(- |\d+\. )',line):
        story.append(Paragraph(rich(line),styles['bullet']));i+=1;continue
    para=[line];i+=1
    while i<len(lines) and lines[i].strip() and not lines[i].startswith(('#','|','- ')):
        para.append(lines[i].strip());i+=1
    story.append(Paragraph(rich(' '.join(para)),styles['body']))

p=Paragraph('Cited source index',styles['h2']);p.toc_label='Cited source index';p.toc_key='source-index';story.append(p)
story.append(Paragraph('Sources linked in the manuscript, in first-citation order. Access and discovery date: September 8, 2026. Some publisher pages were available through indexed text or metadata only; the historical PDF access limitation is stated in Sections 2 and 16.',styles['body']))
seen=set()
for m in inline_pattern.finditer(source):
    if not m.group(1): continue
    label,url=m.group(1),m.group(2)
    if url in seen:continue
    seen.add(url)
    story.append(Paragraph(rich(f'[{label}]({url})')+'<br/>'+esc(url),styles['reference']))
doc.multiBuild(story)
print(f'Built {OUT}; {len(seen)} unique source links.')
