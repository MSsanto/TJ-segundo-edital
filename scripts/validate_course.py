#!/usr/bin/env python3
"""Teste de integridade estrutural. Não é revisão jurídica nem calibração de concurso."""
from pathlib import Path
import re,sys,json
root=Path(__file__).resolve().parents[1]
books=sorted((root/'livros'/'v2').glob('semana_*.md'))
legacy=sorted((root/'livros'/'v1_1').glob('Livro_Texto_Semana_*.md'))
errors=[]
if len(books)!=20:errors.append(f'Livros v2: {len(books)} (esperado 20)')
if len(legacy)!=20:errors.append(f'Livros legados: {len(legacy)} (esperado 20)')
for n,book in enumerate(books,1):
 t=book.read_text('utf8')
 if not re.search(fr'Semana {n:02d}',t,re.I):errors.append(f'Nome semana divergente: {book.name}')
 if '```mermaid' not in t:errors.append(f'Diagrama Mermaid ausente: {book.name}')
 if not any(z in t.lower() for z in ['discursiv','questões discursivas']):errors.append(f'Sem discursiva: {book.name}')
 if len(t)<5500:errors.append(f'Texto curto: {book.name}')
 if '{w["parallel"]}' in t:errors.append(f'Template não renderizado: {book.name}')
roteiro=(root/'legislacao'/'roteiro_corrigido.md').read_text('utf8')
if '{w["parallel"]}' in roteiro:errors.append('Template do roteiro ainda aparece')
for n in range(1,21):
 if f'Semana {n:02d}' not in roteiro:errors.append(f'Semana {n:02d} não aparece no roteiro')
q=(root/'simulados'/'simulado_A_70.md').read_text('utf8')
g=(root/'simulados'/'simulado_A_gabarito.md').read_text('utf8')
items=re.findall(r'^## (\d{2})\. ',q,re.M)
answers=re.findall(r'^(\d{2})\. \*\*[ABCDE]\*\*',g,re.M)
if len(items)!=70 or items!=[f'{i:02d}' for i in range(1,71)]:errors.append('Questões não são 70 numeradas de 01 a 70')
if len(answers)!=70 or answers!=items:errors.append('Gabarito incompleto ou desalinhado')
if 'TJSP2302' not in (root/'provas_antigas'/'CATALOGO.md').read_text('utf8'):errors.append('2023 não catalogado')
if 'TJSP2403' not in (root/'provas_antigas'/'CATALOGO.md').read_text('utf8'):errors.append('2024 não catalogado')
print(json.dumps({'ok':not errors,'livros_v2':len(books),'legado':len(legacy),'questoes_simulado_A':len(items),'respostas_A':len(answers),'errors':errors},ensure_ascii=False,indent=2))
sys.exit(1 if errors else 0)