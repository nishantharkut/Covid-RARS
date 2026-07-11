# Elsevier CBM Manuscript Package

This folder contains the Elsevier `elsarticle` preprint package for the Computers in Biology and Medicine manuscript track.

## Files

- `main.tex`: manuscript with CBM-style biomedical signal-processing validation framing, result tables, and original study figures.
- `references.bib`: BibTeX entries for dataset, confounding, temporal drift, HST, ESWA cross-dataset, and openSMILE sources.
- `highlights.md`: Elsevier highlights.
- `graphical_abstract_caption.md`: graphical abstract caption text.
- `cover_letter.md`: CBM cover letter.
- `declarations.md`: declarations template.
- `README.md`: package and build note.

## Result Basis

All numerical results were computed from the reproducible analysis pipeline. Code and derived result tables will be released with the repository. Dataset and quality-count tables retain the descriptive counts used as the factual basis. Coswara supports multimodal source-domain and temporal analysis. COUGHVID is treated as cough-only external transfer and is not described as multimodal external validation.

## Figure Policy

`main.tex` includes LaTeX figure environments for original study figures:

- Pipeline diagram
- Evaluation protocol ladder
- Temporal degradation plot
- Confounding evidence diagram/table
- Multimodal fusion schematic
- Dataset/quality flow diagram
- Clinical reliability interpretation figure

Do not copy figures from cited papers.

## Build

Typical local build:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```
