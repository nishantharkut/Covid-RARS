# IEEE/JBHI Manuscript Package

This folder contains the IEEE/JBHI manuscript package for the COVID respiratory-audio validation-under-shift study.

## Files

- `main.tex` - IEEEtran journal-format LaTeX manuscript.
- `references.bib` - BibTeX references.
- `cover_letter.md` - JBHI cover letter.
- `author_checklist.md` - author checklist.
- `response_to_scope.md` - scope-fit note for the submission.
- `README.md` - package and build notes.

## Result Basis

All numerical results were copied from the local rebuilt result summaries and support analyses. Code and derived result tables will be released with the repository.

## Figure Policy

`main.tex` includes original study figures shared across the manuscript package. These figures are integrated as validation, degradation, fusion-scope, and confounding evidence. They should not be replaced with copied figures from prior papers.

## Build Note

The manuscript uses IEEEtran journal conventions:

```powershell
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Compilation requires the IEEEtran class and standard LaTeX packages such as `booktabs`.
