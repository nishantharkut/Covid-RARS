# Submission Notes

## Current Package Status

- Main manuscript: `main.tex`
- Bibliography: `references.bib`
- Draft cover letter: `cover_letter.md`
- Package README: `README.md`

## Required Final Author Inputs

- Author names, affiliations, and corresponding-author details.
- Acknowledgements and funding statement.
- Author contribution statement with initials.
- Confirmed competing-interest statement.
- Final data availability wording based on dataset license and supplementary-table plan.
- Final code availability wording with public repository, review-only access, or release timing.

## Result Values Used In Main Manuscript

- Internal participant split: AUROC 0.897, AUPRC 0.863, balanced accuracy 0.825, F1 0.752, sensitivity 0.833, specificity 0.816, n=314.
- Time-stratified participant split: AUROC 0.849, AUPRC 0.783, balanced accuracy 0.783, F1 0.705, sensitivity 0.710, specificity 0.857, n=431.
- Strict early-to-late temporal split: AUROC 0.698, AUPRC 0.896, balanced accuracy 0.656, F1 0.751, sensitivity 0.646, specificity 0.667, n=411.
- Model-matched cough-only external transfer: Coswara internal AUROC 0.849-0.868 versus COUGHVID transfer AUROC 0.523-0.543; best COUGHVID row AUROC 0.543, AUPRC 0.040, balanced accuracy 0.510, F1 0.058, sensitivity 0.084, specificity 0.936, n=8331.
- Metadata audit: full safe metadata AUROC 0.964, symptoms-only AUROC 0.932, demographic/protocol-only AUROC 0.914, and recording-month removal changed strict temporal metadata AUROC by +0.247.

## Framing Checks

- The manuscript is framed as a reliability audit of shortcut learning, temporal drift, confounding, and external validation.
- It avoids clinical deployment claims.
- It avoids state-of-the-art claims.
- It states that Coswara supports multimodal source-domain and temporal analyses, while COUGHVID is cough-only external transfer.
- Main manuscript prose avoids local paths, code filenames, raw metric filenames, logs, scripts, patch names, and repository mechanics.

## Figures Referenced

- `../common_figures/fig_evaluation_ladder.pdf`
- `../common_figures/fig_validation_degradation.pdf`
- `../common_figures/fig_metadata_confounding.pdf`

## Main Tables

- Dataset and protocol roles.
- Primary validation results.
- Metadata-only confounding audit.
- COUGHVID cough-only external-transfer results.
