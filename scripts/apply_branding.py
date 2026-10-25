#!/usr/bin/env python3
"""Acrescenta capa autoral e assinatura gráfica aos PDFs, sem sobrepor o corpo dos originais.

Uso:
  python scripts/apply_branding.py --input pdfs/livros/semana_01.pdf --output /tmp/semana_01_identidade.pdf --week 01
  python scripts/apply_branding.py --all

Requer: pymupdf (fitz); o brasão-fonte em assets/identidade/brasao_pessoal.png.
"""
from pathlib import Path
import argparse
import fitz

ROOT = Path(__file__).resolve().parents[1]
CREST = ROOT / 'assets' / 'identidade' / 'brasao_pdf_otimizado.jpg'
NAVY = (0.040, 0.095, 0.170)
GOLD = (0.82, 0.62, 0.32)
OFF = (0.96, 0.95, 0.92)
DARK = (0.17, 0.23, 0.31)
MOTTO = 'AD ASTRA PER SCIENTIAM'
DEJAVU = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
DEJAVU_BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'


def textbox(page, txt, rect, fontsize=13, color=OFF, bold=False, align=1):
    font = 'custom_b' if bold else 'custom'
    page.insert_font(fontname=font, fontfile=DEJAVU_BOLD if bold else DEJAVU)
    return page.insert_textbox(fitz.Rect(rect), txt, fontsize=fontsize, fontname=font,
                               color=color, align=align, lineheight=1.24)


def cover(doc, name, subtitle, kind='Livro-texto'):
    p=doc.new_page(pno=0,width=595.28,height=841.89)
    p.draw_rect(p.rect, color=NAVY, fill=NAVY)
    p.draw_rect(fitz.Rect(30,30,565,812),color=GOLD,width=1.2)
    p.draw_line(fitz.Point(78,144),fitz.Point(517,144),color=GOLD,width=1)
    textbox(p,'TJSP 2027  /  OFICIAL DE JUSTIÇA', (70,72,525,114), 12, GOLD, bold=True)
    textbox(p,kind.upper(), (70,163,525,190), 14, OFF, bold=True)
    textbox(p,name, (62,205,533,250), 23, OFF, bold=True)
    textbox(p,subtitle, (65,265,530,313), 12, GOLD)
    p.insert_image(fitz.Rect(207,330,388,552), filename=str(CREST),keep_proportion=True)
    textbox(p,MOTTO, (70,583,525,613), 15, GOLD, bold=True)
    textbox(p,'Até as estrelas pelo conhecimento', (90,618,505,644), 10, OFF)
    p.draw_line(fitz.Point(78,702),fitz.Point(517,702),color=GOLD,width=.65)
    textbox(p,'Material de estudo independente • VUNESP • Edital TJSP 01/2026', (60,720,535,760), 9, OFF)
    textbox(p,'Não é publicação oficial do TJSP ou da VUNESP', (80,763,515,787), 8, OFF)


def inside_marks(doc):
    # O número central original e as margens de texto permanecem livres.
    for i in range(1,len(doc)):
        p=doc[i]; w,h=p.rect.width,p.rect.height
        # Somente marcação dentro da margem inferior existente.
        p.insert_image(fitz.Rect(28,h-39,52,h-10),filename=str(CREST),keep_proportion=True,overlay=True)
        p.insert_text((62,h-20),MOTTO,fontsize=7,fontname='helv',color=DARK,overlay=True)
        p.draw_line(fitz.Point(29,h-46),fitz.Point(w-29,h-46),color=GOLD,width=.5,overlay=True)


def apply(src,dst,name,subtitle,kind):
    inp=fitz.open(src)
    out=fitz.open()
    out.insert_pdf(inp)
    inp.close()
    cover(out,name,subtitle,kind)
    inside_marks(out)
    dst.parent.mkdir(parents=True,exist_ok=True)
    out.set_metadata({'title':f'{name} — Oficial de Justiça TJSP 2027',
                      'author':'Matheus Santo — material de estudo',
                      'subject':f'{MOTTO} — Edital 01/2026'})
    out.save(dst,garbage=4,deflate=True)
    out.close()


def all_docs():
    for n in range(1,21):
        name=f'semana_{n:02d}.pdf'
        src=ROOT/'pdfs'/'livros'/name
        if not src.exists(): raise FileNotFoundError(src)
        dst=ROOT/'pdfs'/'livros'/f'semana_{n:02d}_identidade.pdf'
        apply(src,dst,f'SEMANA {n:02d}', 'Livro-texto ilustrado | Versão didática 2.0','Livro de estudos')
        print(dst.relative_to(ROOT))
    for nm in ('simulado_A_70','simulado_A_gabarito','simulado_B_reaplicacao','simulado_B_gabarito'):
        src=ROOT/'pdfs'/'simulados'/f'{nm}.pdf'
        dst=ROOT/'pdfs'/'simulados'/f'{nm}_identidade.pdf'
        apply(src,dst,nm.replace('_',' ').upper(),'Material autoral | Treinamento TJSP','Simulado e correção')
        print(dst.relative_to(ROOT))
    originals=[
        ('TJSP_2027_Caderno_01_Portugues_Constitucional.pdf','Caderno 01: Português e Constitucional'),
        ('TJSP_2027_Caderno_01B_Processo_Civil_VUNESP.pdf','Caderno 01B: Processo Civil'),
        ('TJSP_2027_Caderno_01_Gabarito_Comentado.pdf','Gabarito Caderno 01'),
        ('TJSP_2027_Caderno_01B_Gabarito_Comentado.pdf','Gabarito Caderno 01B')]
    for fn,title in originals:
        src=Path('/mnt/data')/fn
        if src.exists():
            dst=ROOT/'pdfs'/'legado'/fn.replace('.pdf','_identidade.pdf')
            apply(src,dst,title,'Coleção introdutória | Material legado','Caderno')
            print(dst.relative_to(ROOT))


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--input'); ap.add_argument('--output'); ap.add_argument('--week',default='01'); ap.add_argument('--all',action='store_true'); args=ap.parse_args()
    if args.all: all_docs()
    else:
        if not(args.input and args.output): ap.error('use --all ou --input + --output')
        apply(Path(args.input),Path(args.output),f'SEMANA {args.week}','Livro de estudos','Livro de estudos')
if __name__=='__main__':main()
