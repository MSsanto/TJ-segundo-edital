#!/usr/bin/env python3
"""Render the subject-organized TJSP master book as one branded PDF."""
from pathlib import Path
import subprocess
import tempfile
from apply_branding import apply

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "livros" / "por_materia"
OUTPUT = ROOT / "pdfs" / "livros" / "TJSP_2027_Todas_As_Apostilas_Por_Materia.pdf"
REQUIRED = {
    "00_ABERTURA.md",
    "01_LINGUA_PORTUGUESA.md",
    "02_DIREITO_CONSTITUCIONAL.md",
    "03_DIREITO_ADMINISTRATIVO.md",
    "04_DIREITO_PENAL.md",
    "05_PROCESSO_PENAL.md",
    "06_PROCESSO_CIVIL.md",
    "07_DIREITO_CIVIL_LINDB.md",
    "08_LEGISLACAO_ESPECIAL_TJSP.md",
    "09_LBI.md",
    "10_MATEMATICA.md",
    "11_RACIOCINIO_LOGICO.md",
    "12_INFORMATICA.md",
    "13_ATUALIDADES.md",
    "14_METODO_E_DISCURSIVA.md",
    "90_QUESTOES_SEMANAS_01_10.md",
    "91_QUESTOES_SEMANAS_11_20.md",
}

def main():
    sources = sorted(p for p in SOURCE_DIR.glob("*.md") if p.name != "README.md")
    present = {p.name for p in sources}
    missing = sorted(REQUIRED - present)
    if missing:
        raise SystemExit(f"Arquivos obrigatórios ausentes: {missing}")
    if not sources:
        raise SystemExit("Nenhum capítulo encontrado em livros/por_materia.")

    with tempfile.TemporaryDirectory(prefix="tjsp-master-") as temp:
        plain_pdf = Path(temp) / "master_base.pdf"
        command = [
            "pandoc", *[str(p) for p in sources],
            "-f", "gfm", "-o", str(plain_pdf),
            "--pdf-engine=xelatex",
            "--toc", "--toc-depth=3",
            "-V", "mainfont=DejaVu Sans",
            "-V", "geometry:margin=1.8cm",
            "-V", "fontsize=9pt",
            "-V", "papersize=a4",
            "-V", "lang=pt-BR",
            "--resource-path", str(ROOT),
        ]
        subprocess.run(command, cwd=ROOT, check=True)
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        apply(
            plain_pdf,
            OUTPUT,
            "TODAS AS APOSTILAS",
            "Edição por matéria e capítulos | Edital 01/2026",
            "Apostila-mestre",
        )
    print(f"PDF gerado: {OUTPUT.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
