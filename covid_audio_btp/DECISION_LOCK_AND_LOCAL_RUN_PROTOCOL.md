# Decision Lock And Local Run Protocol

Last updated: 2026-06-03

This file records the current decisions so the next local run and later debugging stay consistent.

## Role Split

User machine:

- Holds raw Coswara and COUGHVID datasets.
- Runs Jupyter, feature extraction, model training, and result generation.
- Sends generated artifacts or failed cell output back for review.

EC2/Codex side:

- Holds generated project code and documentation.
- Reviews outputs, fixes code, updates plans, and designs next experiments.
- Does not assume raw datasets are present here.

## Current Research Strategy

Use a hybrid, staged plan:

1. First prove the current Coswara baseline pipeline works.
2. Then run cough-only external validation with COUGHVID.
3. Then add acoustic-domain proxy analysis.
4. Add SSL/GRL/adversarial modules only as an advanced ablation after baseline evidence exists.

Do not replace the current implementation with the Gemini adversarial plan. Treat that plan as a future publication extension, not the survival path.

## Immediate Local Run Target

Run Coswara only.

Main notebook:

```text
notebooks/00_RUN_EVERYTHING_PUBLICATION.ipynb
```

Use these first-run settings:

```python
RAW_COSWARA_DIR = PROJECT_ROOT / "data/raw/coswara"
COUGHVID_RAW = None
RUN_CNN = False
RUN_COUGHVID_FEATURES = False
RUN_FEATURE_SHIFT_REPORT = False
```

Leave advanced toggles off until the Coswara artifacts and metrics exist.

## Dataset Placement On Local Machine

Inside your local extracted project:

```text
covid_audio_btp/
  data/
    raw/
      coswara/
      coughvid/
```

Coswara should contain:

```text
data/raw/coswara/combined_data.csv
data/raw/coswara/csv_labels_legend.json
data/raw/coswara/annotations/
data/raw/coswara/<date folders>/
```

COUGHVID should stay optional until Coswara works. When enabled later, use either:

```text
data/raw/coughvid/public_dataset_v3.zip
```

or an extracted COUGHVID folder. COUGHVID is cough-only, so it is used only for cough external validation.

## Compute Decision

Coswara baseline:

```text
CPU: 4-8 cores
RAM: 16 GB minimum, 32 GB preferred
GPU: not required
Disk: 30-50 GB free
```

Compact CNN:

```text
GPU: 6-8 GB VRAM minimum
RAM: 16-32 GB
```

Future Wav2Vec/HuBERT/GRL extension:

```text
GPU: 12-16 GB VRAM minimum
RAM: 32 GB preferred
Disk: 80-150 GB free
```

Current decision: do not enable CNN or SSL/GRL before the Coswara baseline completes.

## First Success Gate

The first local run is successful only if these exist and look sensible:

```text
reports/tables/coswara_layout_audit.csv
reports/tables/validation_issues.csv
data/interim/coswara_index.csv
data/processed/metadata_clean.csv
data/processed/audio_quality.csv
data/outputs/metrics/ml_baseline_metrics.csv
data/outputs/metrics/calibration_metrics.csv
data/outputs/metrics/fusion_metrics.csv
```

Stop before advanced work if:

- labels are mostly unknown;
- participant leakage is detected;
- positives or negatives are missing from train, validation, or test;
- most audio files are corrupt or silent;
- classical models do not beat dummy baselines;
- calibration/fusion outputs are missing or malformed.

## What To Send Back

If the run succeeds, send these files:

```text
reports/tables/coswara_layout_audit.csv
reports/tables/validation_issues.csv
data/interim/coswara_index.csv
data/processed/metadata_clean.csv
data/processed/audio_quality.csv
data/outputs/metrics/ml_baseline_metrics.csv
data/outputs/metrics/calibration_metrics.csv
data/outputs/metrics/fusion_metrics.csv
```

If it fails, send:

- the exact failed notebook cell;
- full traceback;
- any artifacts already created from the list above.

## When To Enable COUGHVID

Only after Coswara baseline succeeds:

```python
COUGHVID_RAW = PROJECT_ROOT / "data/raw/coughvid/public_dataset_v3.zip"
RUN_COUGHVID_INDEX = True
RUN_COUGHVID_FEATURES = False
```

First build only the COUGHVID index. Full COUGHVID feature extraction can be enabled later with a small smoke test:

```python
RUN_COUGHVID_FEATURES = True
COUGHVID_FEATURE_MAX_ROWS = 25
```

Then remove the row cap only if the smoke test works.

## Advanced Extension Gate

Do not implement or run Wav2Vec/HuBERT/GRL until these are known:

- Coswara baseline metrics.
- Coswara calibration metrics.
- Whether cough-only COUGHVID external validation collapses.
- Whether acoustic domain/source/quality can be predicted from current features.

If domain leakage is visible, the next advanced scripts are:

```text
25_acoustic_domain_proxy.py
26_extract_ssl_embeddings.py
27_train_adversarial_ssl.py
28_compare_adversarial_vs_baselines.py
```

These are ablations, not replacements for the current baseline. Detailed requirements from the two reviewed PDFs are recorded in `ADVANCED_EXTENSION_FROM_GEMINI_PDFS.md`.

## Locked Claims

Allowed:

```text
We evaluate reliability, calibration, quality sensitivity, and domain shift in respiratory-audio screening.
```

Not allowed:

```text
This diagnoses COVID-19.
Wav2Vec/HuBERT is guaranteed to beat MFCC.
GRL is guaranteed to remove bias.
COUGHVID supports full cough-breath-speech external validation.
Tier-2 acceptance is guaranteed.
```

