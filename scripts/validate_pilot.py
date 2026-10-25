#!/usr/bin/env python3
"""Valida estrutura do piloto; não substitui revisão de mérito jurídico."""
from pathlib import Path
import re
p=Path(__file__).resolve().parents[1]
q=(p/'simulados/BLOCO_PILOTO_2026_01.md').read_text(encoding='utf8')
g=(p/'simulados/BLOCO_PILOTO_2026_01_GABARITO.md').read_text(encoding='utf8')
items=re.findall(r'(?ms)^## (\d{2})\s+—.*?(?=^## \d{2}\s+—|^### Discursiva|\Z)',q)
blocks=re.split(r'(?m)^## (?=\d{2} —)',q)[1:]
answers=re.findall(r'(?m)^\| (\d{2}) \| ([A-E]) \|',g)
assert len(items)==12 and items==[f'{i:02d}' for i in range(1,13)],items
assert len(blocks)==12
assert len(answers)==12 and [a for a,_ in answers]==items
options=[]
for b in blocks:
 x=re.findall(r'(?m)^([A-E])\)\s+(.*)$',b)
 assert len(x)==5 and [letter for letter,_ in x]==list('ABCDE'),b[:100]
 options += [t.strip() for _,t in x]
assert len(options)==len(set(options)), 'Alternativa textualmente idêntica em outra questão'
assert q.count('### Discursiva')==2
print('PILOTO OK: 12 objetivas x cinco alternativas distintas; 12 gabaritos; duas discursivas.')
