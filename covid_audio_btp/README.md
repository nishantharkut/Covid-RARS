# COVID/Respiratory Audio BTP

Reliability-aware and confounding-controlled respiratory audio screening from cough, breath, and speech.

This project is a research prototype only. It is not a clinical diagnostic tool.

## Master Record

Read this first:

```text
MASTER_PROJECT_GUIDE.md
```

It contains the project status, decisions, code map, dataset notes, workflow, redundancy audit, and remaining risks.

## Main Notebook

Run only this notebook for the full workflow:

```text
notebooks/00_RUN_EVERYTHING_PUBLICATION.ipynb
```

It has 20 cells total: 10 code and 10 markdown.

Other notebooks are optional review/debug notebooks.

## Local Setup

```bash
cd /home/ubuntu/nishn_workspce/test_pdfs_generic/.covid_audio_btp_private/covid_audio_btp
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
pytest tests -q
jupyter lab
```

Place Coswara under:

```text
data/raw/coswara/
```

Optional COUGHVID path can be configured inside the main notebook.
