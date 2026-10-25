# Auditoria do curso e do edital — 25/10/2026

**Resultado: NÃO homologado para uso autossuficiente.** O material serve de roteiro inicial acompanhado de lei seca, mas contém falhas editoriais relevantes. Este relatório distingue conferência do edital, QA automatizado, amostra jurídica e tarefas não verificadas.

## 1. Base oficial e recorte

- Edital de Abertura TJSP nº 01/2026, **Oficial de Justiça**, 62 páginas; Anexo VIII, pp. 60–62. Não confundir com Escrevente.
- Banca: VUNESP, código TJSP2602: https://www.vunesp.com.br/TJSP2602
- 132 vagas distribuídas + cadastro de reserva. **46ª CJ (São José dos Campos/Jacareí)** e **47ª CJ (Taubaté)**: apenas cadastro de reserva no quadro do edital, p. 9.
- Inscrição prevista 28/10 a 10/12/2026, pagamento até 11/12/2026, prova prevista 14/03/2027; 40 horas/semana; diploma superior de área livre até a posse.
- O valor numérico da remuneração no edital é R$ 9.856,95; o valor por extenso é divergente. Páginas institucionais da VUNESP/TJSP confirmam R$ 9.856,95, mas qualquer retificação deve prevalecer.
- Objetiva: **70** questões, **15 Português + 40 específicos + 15 gerais**, cinco alternativas; mínimo **8/15 Português, 20/40 específicos, 35/70 geral**. Gerais apenas classificatórios. Discursiva: **2 questões** de conhecimentos específicos, eliminatória, 0–40; mínimo 24 (lista geral) ou 19,2 (listas reservadas). Duração conjunta 5 horas.
- Na 46ª CJ, 8 candidatos da lista geral têm a discursiva corrigida, mais empatados no corte. Para habilitados nas cotas há regra específica de correção; isso não significa classificação ou nomeação automática (edital, pp. 35–39).
- PcD: reserva 5%, procedimento documental específico, eventuais adaptações, perícia biopsicossocial posterior. Seguir os capítulos III, IV, XII e XIII sem inferir aptidão ou indeferimento.

## 2. Dados de auditoria local — reproduzíveis

Comando: `python scripts/validate_course.py && python scripts/audit_quality.py`.

| Verificação | Resultado | Conclusão |
|---|---|---|
| 20 fontes Markdown `livros/v2/` | 20 presentes | Quantidade OK; não valida substância |
| 20 livros v1.1 preservados | Sim | Histórico rastreável |
| Simulado A | 70 itens e 70 respostas | Integridade OK; avaliação inadequada |
| Alternativas repetidas literalmente | 3 distratores ocorrem **40 vezes cada** | **Falha crítica de qualidade** |
| Livros 02–20 | 6 repetições por livro da fórmula “Não basta memorizar...” | **Modelo demasiadamente repetitivo** |
| Simulado B | Reaplica A | **Não é segundo banco independente** |
| Identidade pessoal | Brasão e lema nos PDFs destinados à impressão | Marca pessoal, não TJSP/VUNESP |
| Revisão legal de todos os dispositivos | **Não realizada** | Não declarar homologação jurídica |
| Provas anteriores | 2023/2024 localizadas; amostra de questões conferida | Mapeamento exaustivo de 200 itens pendente |
| Leitores de telas/alt text/estrutura | Não avaliado em leitor real | Acessibilidade não certificada |

### Problemas que podem prejudicar a nota

1. Distratores obviamente absurdos geram falso desempenho positivo. **Suspenda o Simulado A como medição preditiva**; use somente como aquecimento. Não há escore psicometricamente calibrado.
2. O volume de texto dos livros 02–20 infla pela repetição de quadros, sem explicar em profundidade cada exceção, prazo e sujeito. Exija revisão localizada com fonte legal antes de memorizar.
3. Exercícios e gabaritos antigos não têm rastreabilidade jurídica item a item. Um script que conta 70 questões não prova que a alternativa esteja correta.
4. O roteiro de lei seca diz abranger todo o Anexo VIII, mas **cobertura de números não é prova de cobertura pedagógica**. Matéria de Informática e Atualidades precisa de acompanhamento próprio, e as Normas da Corregedoria exigem revisão de sua edição atual.
5. Ao usar provas antigas de 100 questões, não converter o número de acertos diretamente em nota de 2027. Em 2023 houve **anulação definitiva dos itens 49 e 67**, versão 1 (gabarito definitivo publicado). O documento encontrado para 2024 está intitulado “Gabarito Oficial”; a condição de definitivamente consolidado precisa de confirmação antes de pontuar.
6. Não reproduzir provas integralmente no GitHub público, salvo licença/autorização aplicável; catalogar links e números das questões.

## 3. Confronto com provas antigas — amostra efetivamente vista

| Ano, versão/caderno | Nº | Assunto observado | Confronto com edital 2026 |
|---|---:|---|---|
| 2023 / 001 | 01–04 | compreensão de texto, colocação pronominal, pontuação | Português do Anexo VIII |
| 2023 / 001 | 35 | prisão e art. 283 CPP | CPP, art. 283 — incluso |
| 2023 / 001 | 36 | citação com hora certa e efeitos processuais no CPP | CPP, arts. 351–363 — incluso; **não confundir CPC** |
| 2023 / 001 | 37 | marco do prazo no procedimento do júri, art. 406 CPP | CPP art. 406 — incluso |
| 2024 / 001 | 01–02 | objetivo do texto e causalidade | Português do Anexo VIII |
| 2024 / 001 | 39 | princípio da não surpresa, art. 10 CPC | CPC art. 10 — incluso |
| 2024 / 001 | 75–76 | Normas da Corregedoria e mandados | conferir versão vigente das NSCGJ |
| 2024 / 001 | 91–92 | lógica condicional e sequências | Raciocínio Lógico do Anexo VIII |

Esta tabela **não** representa as 200 questões analisadas. É uma amostra rastreável. Não foram copiados enunciados.

Fontes das provas consultadas:
- 2023 PDF: https://arquivos.qconcursos.com/prova/arquivo_prova/100311/vunesp-2023-tj-sp-oficial-de-justica-prova.pdf
- 2023 gabarito definitivo: https://arquivos.qconcursos.com/prova/arquivo_gabarito/100311/vunesp-2023-tj-sp-oficial-de-justica-gabarito.pdf
- 2024 PDF: https://arquivos.qconcursos.com/prova/arquivo_prova/128359/vunesp-2024-tj-sp-oficial-de-justica-prova.pdf
- 2024 gabarito oficial: https://documento.vunesp.com.br/documento/stream/NjY1NTEyOQ%3D%3D
- VUNESP 2023: https://www.vunesp.com.br/TJSP2302
- VUNESP 2024: https://www.vunesp.com.br/TJSP2403

## 4. Conferência jurídica direcionada e limite

Verifiquei no portal oficial do Planalto, para o conteúdo da Semana 02: CF, art. 5º, XVI (reunião sem autorização, com aviso prévio); CP arts. 1º–6º (anterioridade, lei posterior benéfica, lei excepcional/temporária, teoria da atividade para tempo, territorialidade e teoria da ubiquidade para lugar do crime). Referências: https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm e https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848compilado.htm. Isso **não** equivale a conferir integralmente arts. 7º–12 ou todas as outras matérias.

## 5. Decisão de publicação

- **Pode usar:** edital, cronograma, índice da lei seca, links oficiais, Livro 01 como texto de apoio, revisão dos casos realmente conferidos.
- **Pode usar com aviso explícito:** livros v2 das semanas 02–20 e Simulado A/B — versão formativa, não homologada.
- **Não pode alegar:** gabaritos integralmente validados por jurista, 200 questões antigas classificadas e conferidas, Simulado B inédito, acessibilidade integral certificada.

## 6. Ordem de trabalho e critérios de aceite

1. **Auditoria jurídica prioritária**: exigir tabela por semana `tese → diploma → artigo → texto oficial/data → condição/exceção → revisão`. Itens sem fonte oficial não homologados.
2. **Reescrita didática** dos livros 02–20: converter fórmulas genéricas em exemplos e fluxogramas próprios; antes/depois por tópico. Priorizar CPP/CPC/Normas da Corregedoria.
3. **Catalogação dos 200 itens antigos**: identificação de caderno/versão, questão, disciplina, dispositivo edital, gabarito consolidado, mudança normativa — sem copiar integralmente provas.
4. **Simulados reais de treinamento**: criar A2 e B2 genuinamente distintos com 15/40/15, 2 discursivas, gabarito artigo a artigo e revisão independente; manter A/B antigos como aquecimento identificado.
5. **Identidade e acessibilidade**: PDF pesquisável, capas consistentes, fontes grandes, diagramas com explicações textuais, revisão assistiva.
6. **Sincronização e versionamento**: atualizar GitHub/Drive, changelog, testes reproduzíveis; não apagar materiais legados.

**Status em 25/10/2026: existem bloqueios críticos. Não aprovar o curso como versão final.**
