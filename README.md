# TJSP — Oficial de Justiça · Edital 01/2026

> **Cargo certo: Oficial de Justiça.** Não é material do concurso de Escrevente Técnico Judiciário.

Projeto de estudo aberto, organizado por 20 semanas, com livros-texto, legislação, questões autorais, catálogos de provas anteriores, respostas e registro de evolução. **Prova prevista: 14/03/2027.**

## Por onde começar

1. **Leia a [auditoria editorial de 25/10/2026](docs/AUDITORIA_INDEPENDENTE_2026_10_25.md) e as [limitações do curso](docs/STATUS_E_LIMITES.md).**
2. [Abra o calendário e rotina de estudos](docs/PLANO_DE_ESTUDOS.md).
3. Leia [Livro-texto v2 da Semana 01](livros/v2/semana_01.md); prossiga pelas semanas 02 a 20.
4. Consulte [lei seca por semana](legislacao/roteiro_corrigido.md) e [fontes oficiais](docs/FONTES_OFICIAIS.md).
5. Resolva [Simulado A: 70 questões + 2 discursivas](simulados/simulado_A_70.md) e use o [gabarito comentado](simulados/simulado_A_gabarito.md) depois de terminar.
6. Estude também as provas de 2023 e 2024 pelo [catálogo](provas_antigas/CATALOGO.md) e pela [matriz amostral verificada](provas_antigas/CONFERENCIA_AMOSTRAL_2023_2024.md). Para aplicação jurídica, prefira o [bloco piloto de 12 questões](simulados/BLOCO_PILOTO_2026_01.md), com [gabarito separado](simulados/BLOCO_PILOTO_2026_01_GABARITO.md), ao Simulado A como medição de proficiência.
7. Anote os resultados no [registro de evolução](docs/REGISTRO_DE_EVOLUCAO.md).

## Organização

| Pasta | Conteúdo | Situação |
|---|---|---|
| `livros/v2/` | 20 volumes: semana 01 aprofundada; semanas 02–20 ampliadas de maneira estruturada | Revisão jurídica granular pendente |
| `livros/v1_1/` | Coleção original preservada | Legado |
| `legislacao/` | Lei seca, intervalos do Anexo VIII, checklists | Cobertura documental, checagem dinâmica |
| `simulados/` | Um banco autoral A de 70 itens e uma reaplicação B da mesma base | Formativo, **não calibrado** |
| `provas_antigas/` | Links VUNESP 2023/2024 e metodologia de aproveitamento | Confirmado |
| `exercicios/legado/` | Exercícios anteriores usados como referência | Baixa fidelidade à prova |
| `gabaritos/` | Gabarito do Livro 01 v2 | Disponível |
| `pdfs/` | Edições para impressão geradas das fontes | Não editar manualmente, regenerar |
| `docs/` | Qualidade, metodologia, registro, fontes e changelog | Documentado |
| `scripts/` | Checagem automática de quantidade e de integridade | Incluído |

## Atenção sobre direitos autorais

O repositório **não hospeda cópias integrais** dos cadernos VUNESP de 2023/2024; aponta páginas oficiais e fornecedores autorizados para consulta. Os novos simulados e textos são autorais; a lei seca é apresentada por remissões, não pela reprodução massiva de legislação.

## PDFs e Google Drive

[**Pasta Curso oj no Google Drive**](https://drive.google.com/drive/folders/1W7GFjNtbbTmw45UpYIk_sPgCgpiQon4w) — PDFs antigos preservados e entregáveis revisados.

## Atualização

- Registrar toda edição em [CHANGELOG.md](CHANGELOG.md).
- Antes de revisar qualquer artigo, verificar o texto vigente, alterações posteriores e retificações da VUNESP.
- Executar `python scripts/validate_course.py` (CI automatizada no GitHub).
- O validador confere **estrutura** e gabaritos; ele **não substitui revisão jurídica humana**.

## Finalidade

Estudo pessoal, sem vínculo institucional com TJSP/VUNESP. Nenhuma garantia de classificação ou nomeação.

## Identidade pessoal dos cadernos

Os PDFs `*_identidade.pdf` trazem o [brasão pessoal e o lema *Ad astra per scientiam*](docs/IDENTIDADE_VISUAL.md). Os PDFs originais foram preservados. O roteiro `scripts/apply_branding.py` permite reproduzir a capa e os rodapés em todo o curso.

## Auditoria e material experimental

O curso **não está juridicamente homologado**. A edição de 25/10/2026 identificou três distratores textualmente idênticos em 40 itens do Simulado A, uso de fórmulas repetitivas nos livros 02–20 e reaplicação de questões no Simulado B. O [complemento da Semana 02](livros/suplementos/semana_02_conferencia_fundamentos.md) e o [bloco piloto](simulados/BLOCO_PILOTO_2026_01.md) são correções pontuais, não a revisão integral do programa.

QA: `python scripts/validate_course.py`; `python scripts/audit_quality.py`; `python scripts/validate_pilot.py`. Para verificar se já se pode aprovar a versão antiga como completa, rode `python scripts/audit_quality.py --strict` (esperado falhar até corrigir os bloqueios).
