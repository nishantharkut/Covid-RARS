# COVID Audio Repository Map

This map explains the current repository without moving or deleting existing evidence files.

## Top-Level Structure

| Path | Role |
|---|---|
| `covid_audio_btp/` | Active Python package, notebooks, scripts, runbooks, tests, research briefing docs, source registry, and optional manuscript material |
| `results/frozen/` | Frozen publication, Coswara, CNN, and external-validation result folders |
| `results/representations/` | Frozen OpenSMILE/BEATs/PANNs representation result folders |
| `artifacts/bundles/` | Compressed zip/tar.gz bundles preserved as evidence packages |
| `manuscripts/` | Venue-specific manuscript drafts, generated PDFs, shared figures, and source artifacts |
| `archive/patches/` | Historical patch files retained for traceability |
| `archive/updates/` | Historical update notes |
| `archive/review_materials/` | Gemini/PDF review exports and duplicate root review snapshots |
| `docs/status/` | Status, decision, and implementation summary notes |
| `docs/runbooks/` | Historical execution/runbook notes |
| `docs/repository/` | Repository-level maps and hygiene documentation |

## Active Package Map

| Path | Role |
|---|---|
| `covid_audio_btp/src/covid_audio_btp/` | Importable Python implementation |
| `covid_audio_btp/scripts/` | Numbered command-line workflow scripts |
| `covid_audio_btp/tests/` | Pytest suite for package modules and CLI behavior |
| `covid_audio_btp/notebooks/` | Notebook workflow and review notebooks |
| `covid_audio_btp/docs/research_briefing/` | Evidence docs for research discussion and manuscript defense |
| `covid_audio_btp/references/` | Verified source registry and source planning material |
| `covid_audio_btp/research_protocol/` | Research protocol and dataset schema inspection notes |
| `covid_audio_btp/requirements*.txt` | Core, development, optional, and GPU dependency sets |
| `covid_audio_btp/pyproject.toml` | Package metadata and pytest configuration |

## Main Evidence Documents

| File | Use |
|---|---|
| `covid_audio_btp/docs/research_briefing/COVID_AUDIO_BTP_E2E_PROJECT_BRIEF.md` | End-to-end explanation of the research pipeline |
| `covid_audio_btp/docs/research_briefing/COVID_AUDIO_BTP_RESULTS_EVIDENCE.md` | Metrics ledger and safe interpretations |
| `covid_audio_btp/docs/research_briefing/COVID_AUDIO_BTP_PLAIN_LANGUAGE_EXPLANATION_GUIDE.md` | Simple explanations for meeting and review questions |
| `covid_audio_btp/docs/research_briefing/COVID_AUDIO_BTP_RESULTS_COMPARISON.md` | Paper/result comparison guidance |
| `covid_audio_btp/references/verified_source_registry.md` | Source-backed guardrail for scope and claims |

## Main Code Families

| Area | Representative files |
|---|---|
| Data indexing and metadata | `datasets.py`, `data_index.py`, `metadata.py`, `labels.py`, `validation.py` |
| Preprocessing and quality | `audio_io.py`, `preprocess.py`, `quality.py`, `split.py` |
| Acoustic features | `features.py`, `strong_features.py`, `opensmile_features.py`, `representation_features.py`, `ssl_extractors.py` |
| Classical models and fusion | `models_ml.py`, `fusion.py`, `calibration.py`, `strong_baseline.py`, `compare_is10_final_validation.py` |
| Deep/representation models | `models_cnn.py`, `train_cnn.py`, `sota_ssl.py`, `spectrograms.py` |
| Reliability audits | `domain_shift_audit.py`, `metadata_confounding.py`, `temporal_holdout.py`, `temporal_month_causal.py`, `ipw_sensitivity.py`, `clinical_operating_points.py` |
| Reporting | `reporting.py`, `final_report.py`, `publication_evidence.py`, `manifest.py`, `related_papers.py` |

## Claim Discipline

Use this repository as a reliability and domain-shift artifact. The most defensible claim is that strong internal respiratory-audio performance does not imply deployment robustness without temporal validation, external transfer, calibration, metadata-confounding checks, and decision-oriented evaluation.

Do not describe the repository as a clinical diagnostic system.
