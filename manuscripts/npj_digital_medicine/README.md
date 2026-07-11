# npj Digital Medicine manuscript package

This package contains the npj-style draft for a medical-AI reliability audit of COVID-19 respiratory-audio benchmarks. The manuscript is framed around confounding, temporal drift, dataset shift, and limited generalization in Coswara and COUGHVID.

## Contents

- `main.tex`: main manuscript.
- `references.bib`: bibliography used by the manuscript.
- `cover_letter.md`: draft cover letter for npj Digital Medicine.
- `submission_notes.md`: submission checklist, caveats, and final-author placeholders.

Figures are included from the shared project figure directory as PDF graphics. The main manuscript currently references:

- `../common_figures/fig_evaluation_ladder.pdf`
- `../common_figures/fig_validation_degradation.pdf`
- `../common_figures/fig_metadata_confounding.pdf`

The main evidence burden is carried by protocol, primary-results, metadata-control, and COUGHVID-transfer tables in `main.tex`.

## Build

From this directory:

```powershell
latexmk -pdf main.tex
```

If `latexmk` is unavailable, use a standard LaTeX plus BibTeX sequence:

```powershell
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

## Framing Guardrails

- This is a methodological audit paper, not a clinical deployment or state-of-the-art model paper.
- Coswara supports multimodal source-domain and temporal analyses.
- COUGHVID is used only as a cough-only external transfer target and does not validate multimodal fusion.
- Main result values should remain restricted to artifact-backed audit values.
- Main manuscript prose should avoid repository mechanics, local paths, script names, log names, patch names, and raw file provenance.
- Data and code provenance should be described in plain English in Data Availability and Code Availability.

## Before Submission

- Replace draft author and affiliation placeholders.
- Complete acknowledgements, funding, author contributions, and competing-interest checks.
- Decide whether the journal submission will include the aggregate result summaries as supplementary tables.
- Replace the provisional Code Availability wording with the final public repository or controlled-review access statement.
