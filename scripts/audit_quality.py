#!/usr/bin/env python3
"""Auditoria reproduzível de qualidade editorial; NÃO afirma validade jurídica.
Execução: python scripts/audit_quality.py [--strict]
"""
from pathlib import Path
from collections import Counter
import argparse, re, json
root = Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--strict',action='store_true');args=p.parse_args()
books=sorted((root/'livros/v2').glob('semana_*.md'))
sim=(root/'simulados/simulado_A_70.md').read_text(encoding='utf-8')
qblocks=re.split(r'(?m)^## (?=\d{2}\. )',sim)[1:]
options=Counter(x.strip() for q in qblocks for x in re.findall(r'(?m)^[A-E]\)\s+(.*)$',q))
book_repetition={}
for b in books:
    txt=b.read_text(encoding='utf-8')
    book_repetition[b.stem]={
        'words':len(txt.split()),
        'generic_formula':txt.count('Não basta memorizar o nome do instituto'),
        'generic_distractor_tip':txt.count('Antes de escolher a alternativa'),
        'mermaid':txt.count('```mermaid')}
refs=[]
for q in qblocks:
    if len(re.findall(r'(?m)^[A-E]\)\s+',q)) !=5: refs.append(q.splitlines()[0])
weak={k:v for k,v in options.items() if v>=5}
problems=[]
if len(books)!=20:problems.append('Não existem 20 livros v2')
if len(qblocks)!=70:problems.append('Simulado A não possui 70 questões')
if refs:problems.append(f'Questões com alternativas em número irregular: {refs}')
if any(v>=10 for v in options.values()):problems.append('ALTO: distratores textualmente repetidos >= 10 vezes no simulado')
if any(x['generic_formula']>=4 for n,x in book_repetition.items() if n!='semana_01'):
    problems.append('ALTO: formulação genérica repetida em módulos 02-20')
if 'simulado_B_reaplicacao.md' in [f.name for f in (root/'simulados').glob('*.md')]:
    problems.append('MÉDIO: Simulado B é reaplicação, não novo banco independente')
report={
 'cargo':'Oficial de Justiça TJSP, Edital 01/2026',
 'auditoria':'editorial/estrutural, não revisão jurídica individual',
 'books_v2':len(books),'simulado_A_questoes':len(qblocks),
 'simulado_A_alternativas':sum(options.values()),
 'repeated_options_5_or_more':dict(weak),
 'books':book_repetition,'problems':problems,
 'course_homologated':False}
if '--json' in __import__('sys').argv: pass
print(json.dumps(report,ensure_ascii=False,indent=2))
raise SystemExit(1 if args.strict and problems else 0)
