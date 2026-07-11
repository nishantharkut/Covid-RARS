# Elsevier ESWA Manuscript Package

This folder contains an Elsevier `elsarticle` preprint package for:

**A Protocol-Aware Expert-System Framework for COVID-19 Respiratory-Audio Screening Under Temporal and External Dataset Shift**

## Files

- `main.tex`: ESWA-style manuscript focused on expert-system reliability, validation protocols, and source-scoped claims.
- `references.bib`: BibTeX entries for datasets, feature/model families, temporal drift, confounding, symptom-assisted modeling, and the ESWA DNDT/DNDF comparison.
- `highlights.md`: Elsevier highlights as editable plain text.
- `graphical_abstract_caption.md`: status note and caption guidance for a separate graphical abstract asset.
- `cover_letter.md`: ESWA cover letter.
- `declarations.md`: declarations draft requiring author confirmation.
- `README.md`: package and build note.

## Result Basis

All numerical results in the manuscript are drawn from the reproducible result tables and support analyses. The paper distinguishes Coswara multimodal source-domain and temporal evidence from COUGHVID cough-only external transfer.

## Figure Policy

The LaTeX file references original study figures shared across the manuscript package. No figures are copied from prior papers. If a separate graphical abstract is prepared for submission, it should be derived from the validation-framework figure rather than from third-party artwork.

## Build

From this folder:

```powershell
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Fallback:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The manuscript uses `elsarticle`; install the Elsevier LaTeX class if your TeX distribution does not already include it.
