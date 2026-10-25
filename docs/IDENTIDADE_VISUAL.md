# Identidade visual do curso — Matheus Santo

**Projeto:** Preparatório independente para Oficial de Justiça do TJSP (Edital de Abertura 01/2026).

## Símbolo e lema

- **Brasão:** `assets/identidade/brasao_pessoal.png` — recorte do emblema heráldico pessoal aprovado anteriormente, preservando desenho, cores e proporção.
- **Lema original:** **Ad astra per scientiam**.
- **Tradução livre de apoio:** *Até as estrelas pelo conhecimento*.
- **Cores da coleção:** azul-marinho profundo (#0A182B), dourado suave (#D19E52), papel branco.
- **Aplicação:** capa temática com brasão em destaque; assinatura reduzida e uma linha no rodapé das páginas seguintes.
- **Distinção institucional:** brasão é **marca pessoal**, não emblema do TJSP/VUNESP. PDFs devem exibir claramente que o conteúdo não é publicação oficial.

## Arquivos que receberam a identidade

1. `pdfs/livros/semana_01_identidade.pdf` a `semana_20_identidade.pdf`.
2. `pdfs/simulados/*_identidade.pdf` (questões e gabaritos dos simulados A e B).
3. `pdfs/legado/*_identidade.pdf` (Cadernos 01 e 01B, com gabaritos, mantidos como material legado).

**Importante:** livros 02–20 permanecem em estágio didático a revisar quanto à profundidade e à legislação; a aplicação de identidade visual **não equivale** à aprovação jurídica.

## Reproduzir

```bash
python -m pip install pymupdf pillow
python scripts/apply_branding.py --all
python scripts/validate_course.py
```

A rotina gera novo PDF e não substitui o conteúdo original. Ela insere uma capa e uma marca discreta nas margens inferiores das páginas. Para reprocessar apenas um volume:

```bash
python scripts/apply_branding.py --input pdfs/livros/semana_01.pdf --output pdfs/livros/semana_01_identidade.pdf --week 01
```

## Acessibilidade e manutenção

- O texto do lema é escrito no PDF como **texto selecionável**, além de existir no brasão.
- Os livros continuam contendo conteúdo pesquisável, sem converter páginas em imagens.
- Não inserir brasão por cima de enunciados, gráficos e respostas.
- Conferir a capa e ao menos uma página interna após cada atualização do gerador.
- Não divulgar fontes de tipos comerciais; o gerador usa fontes instaladas no ambiente.

## Proveniência

Arte utilizada do próprio acervo de identidade visual do autor (arquivo **Identidade Heráldica Ad Astra per Scientiam.png**). Nenhuma imagem do tribunal ou da VUNESP foi utilizada na nova capa.
