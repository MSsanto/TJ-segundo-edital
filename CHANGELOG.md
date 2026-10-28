# Changelog — TJSP Oficial de Justiça

## 2026-10-28 — Auditoria de cobertura do Anexo VIII

- Criada `docs/MATRIZ_COBERTURA_EDITAL_LIVROS_2026_10_28.md`, confrontando as 20 semanas versionadas com as disciplinas e os tópicos do edital de Oficial de Justiça.
- Conclusão documentada: cobertura didática parcial; roteiro de lei seca não equivale à explicação completa de todos os dispositivos.
- Registradas lacunas em Matemática, Raciocínio Lógico, Informática, Português, Atualidades/LBI e rastreabilidade jurídica artigo a artigo.
- Registrada divergência de versão: `livros/v2_1/` não está no branch `main`, embora o calendário aponte para material no Drive.
- README atualizado para expor o estado real do curso, sem alegar homologação.
- Criado `docs/BACKLOG_NUMERADO.md` com prioridades, estados reais e critérios de aceite.

## 2026-10-25 — 2.0.0 (base de estudo, sem homologação jurídica)

- Escopo explicitamente limitado ao concurso de **Oficial de Justiça**, Edital TJSP 01/2026.
- Importadas e preservadas 20 fontes textuais da coleção 1.1, identificadas como legado.
- Publicados 20 volumes `livros/v2`: 01 da edição aprofundada anterior; 02–20 ampliados com 6 aulas, casos, mapas Mermaid, lei seca, questões analíticas e atividade discursiva.
- Corrigido literal `{w["parallel"]}` no roteiro de leitura e incluído aviso sobre limite da revisão documental.
- Incluídas referências de provas antigas 2023/2024, sem republicar conteúdo protegido.
- Criado Simulado A com 70 questões autorais (15/40/15), gabarito, 2 discursivas e B de reaplicação da mesma base.
- Adicionados documentação editorial, fontes, plano, registro, validador e GitHub Actions.

## 2026-10-23 — 1.1 (coleção inicial)

- 20 livros de síntese + roteiro de leitura dos dispositivos do edital.

## 2026-10-25 — Identidade pessoal nos materiais

- Adicionado brasão próprio de Matheus Santo, preservado do acervo de identidade heráldica.
- Adicionado lema **Ad astra per scientiam** nas capas e nos rodapés.
- Gerados 20 livros-texto, 4 arquivos de simulados e 4 arquivos legados em versões `*_identidade.pdf`.
- Criado gerador reexecutável `scripts/apply_branding.py` e manual `docs/IDENTIDADE_VISUAL.md`.
- Documentada a separação entre identidade pessoal e símbolos oficiais de TJSP/VUNESP.

## 2026-10-25 — Auditoria editorial e piloto jurídico

- Confrontados edital 01/2026, amostra dos cadernos oficiais 2023 e 2024, e textos oficiais CF/CP/CPC.
- Identificadas repetições em 40 questões do Simulado A e fórmulas genéricas nos volumes 02–20; status **não homologado** mantido.
- Adicionados `scripts/audit_quality.py` e `scripts/validate_pilot.py`, com QA reprodutível e modo estrito.
- Criados `docs/AUDITORIA_INDEPENDENTE_2026_10_25.md`, matriz amostral, suplemento temático da Semana 02, e bloco piloto novo de 12 objetivas + 2 discursivas com gabarito fundamentado.
- Mantidos livros e simulados originais para transparência; não reproduzidos enunciados antigos na íntegra.


## 2026-10-28 — Apostila-mestre por matéria e capítulos

- Reorganizadas as aulas existentes nos 20 livros-texto v2.0 em arquivos por disciplina e capítulos.
- Preservados exercícios, propostas discursivas e correções nos apêndices, com referência à semana de origem.
- Acrescentadas listas explícitas de tópicos que ainda precisam de desenvolvimento ou conferência artigo por artigo.
- Adicionado fluxo automatizado para gerar um PDF consolidado com capa e identidade visual do curso.
- Esta entrega é estrutural: não declara o edital integralmente coberto nem substitui revisão jurídica substantiva.
