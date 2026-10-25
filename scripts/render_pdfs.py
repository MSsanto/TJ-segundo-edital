#!/usr/bin/env python3
"""Render local PDFs from versioned Markdown. Requires Pandoc + XeLaTeX.

This is a *layout export*. Mermaid source diagrams remain printable text;
for interactive Mermaid rendering, read the Markdown on GitHub.
"""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
targets = [
    *sorted((ROOT / "livros" / "v2").glob("semana_*.md")),
    *sorted((ROOT / "simulados").glob("simulado_*.md")),
]
for source in targets:
    section = "livros" if "livros" in source.parts else "simulados"
    out_dir = ROOT / "pdfs" / section
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / (source.stem + ".pdf")
    cmd = [
        "pandoc", str(source), "-f", "gfm", "-o", str(out),
        "--pdf-engine=xelatex", "-V", "mainfont=DejaVu Sans",
        "-V", "geometry:margin=1.8cm", "-V", "fontsize=9pt",
    ]
    subprocess.run(cmd, check=True)
    print(f"Gerado: {out.relative_to(ROOT)}")
