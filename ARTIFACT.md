# Artifact Review Guide

This repository is a research artifact for reliability-aware COVID/respiratory audio evaluation. It contains code, scripts, notebooks, frozen result bundles, research briefing documents, manuscript drafts if present, and source registries.

## Artifact Scope

In scope:

- Coswara respiratory-audio processing and evaluation.
- COUGHVID cough-only external transfer checks.
- Acoustic feature extraction, OpenSMILE-related branches, classical ML, CNN-BiGRU, WavLM, calibration, fusion, and validation-ladder analyses.
- Metadata-confounding, temporal robustness, feature stability, support-overlap, decision-curve, bootstrap, and incremental audio+metadata checks.
- Evidence documents that explain safe manuscript claims.

Out of scope:

- Clinical diagnosis or triage deployment.
- Claiming universal SOTA across all COVID-audio papers.
- Redistributing raw datasets without explicit source permission.

## Primary Review Path

1. Read the root [`README.md`](README.md).
2. Read the project brief: [`covid_audio_btp/docs/research_briefing/COVID_AUDIO_BTP_E2E_PROJECT_BRIEF.md`](covid_audio_btp/docs/research_briefing/COVID_AUDIO_BTP_E2E_PROJECT_BRIEF.md).
3. Read the evidence ledger: [`covid_audio_btp/docs/research_briefing/COVID_AUDIO_BTP_RESULTS_EVIDENCE.md`](covid_audio_btp/docs/research_briefing/COVID_AUDIO_BTP_RESULTS_EVIDENCE.md).
4. Check source/claim guardrails: [`covid_audio_btp/references/verified_source_registry.md`](covid_audio_btp/references/verified_source_registry.md).
5. Use [`docs/repository/REPOSITORY_MAP.md`](docs/repository/REPOSITORY_MAP.md) to locate code and artifacts.

## Reproducibility Notes

The package metadata is in [`covid_audio_btp/pyproject.toml`](covid_audio_btp/pyproject.toml). Core dependencies are in [`covid_audio_btp/requirements.txt`](covid_audio_btp/requirements.txt), with optional GPU, development, and extended dependencies separated into package-level requirement files.

Basic install:

```powershell
cd covid_audio_btp
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e .
```

Tests:

```powershell
cd covid_audio_btp
python -m pip install -r requirements-dev.txt
python -m pytest
```

Some full experiments require raw Coswara and/or COUGHVID data and optional dependencies. Raw data access must follow dataset-source terms.

## Where Evidence Lives

| Area | Location |
|---|---|
| Active code and tests | `covid_audio_btp/` |
| Final/frozen result folders | `results/frozen/` |
| Representation result folders | `results/representations/` |
| Compressed bundles | `artifacts/bundles/` |
| Manuscript drafts and shared figures | `manuscripts/` |
| Historical patches and review exports | `archive/` |
| Repository-level maps and status notes | `docs/` |

## Evidence Boundaries

The key result is a reliability contrast, not a deployment model:

- Internal Coswara validation is strong.
- Time-aware and early-to-late validation reduce confidence.
- COUGHVID cough-only transfer is weak.
- Metadata/context variables are strong predictors and must be treated as confounders.

Every manuscript claim should point to a table, report, or script in this repository.
