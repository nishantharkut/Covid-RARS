# Contributing And Evidence Hygiene

This repository is in research/manuscript mode. Changes should preserve traceability from code to generated artifacts to manuscript claims.

## Rules

- Do not delete or overwrite frozen result bundles unless a replacement run is explicitly documented.
- Do not report a metric in prose unless the source CSV, JSON, log, or generated report is named.
- Keep clinical wording conservative: this is a research prototype, not a diagnostic tool.
- Keep COUGHVID claims cough-only unless a true multimodal external dataset is added.
- Treat metadata and recording protocol variables as confounding risks, not harmless covariates.
- Keep raw dataset redistribution out of the repository unless the dataset license explicitly permits it.

## Before Committing

Recommended checks:

```powershell
cd covid_audio_btp
python -m compileall -q src scripts tests
python -m pytest
```

If full dependencies are not installed, document which checks were skipped and why.

## Manuscript Claims

Strong claims should cite one of:

- `covid_audio_btp/docs/professor/COVID_AUDIO_BTP_RESULTS_EVIDENCE.md`
- `covid_audio_btp/docs/professor/COVID_AUDIO_BTP_E2E_PROFESSOR_BRIEF.md`
- `covid_audio_btp/references/verified_source_registry.md`
- Generated CSV/JSON artifacts under result directories or package-level `reports/` and `data/outputs/`.

Avoid adding unsupported language such as "clinical diagnosis", "deployment-ready", or "beats all SOTA".
