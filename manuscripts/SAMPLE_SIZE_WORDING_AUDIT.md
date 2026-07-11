# Sample-Size Wording Audit

The manuscripts contain several different sample sizes because the endpoints are not all the same experiment. This is expected, but the text must keep the role of each n clear.

## Primary selected validation ladder

| n | Where it appears | Meaning |
|---:|---|---|
| 314 | Existing participant split | Final selected Coswara source-domain cough+speech stacked logistic fusion test endpoint. |
| 431 | Time-stratified participant split | Final selected Coswara cough+breath+speech uniform-mean fusion test endpoint. |
| 411 | Strict early-to-late temporal audio endpoint | Final selected Coswara breath top-4 validation ensemble temporal test endpoint. |
| 8331 | COUGHVID external transfer | Independent cough-only external target for Coswara-trained ComParE+IS10 cough models. |

Recommended wording:

> Endpoint sample sizes vary by modality availability, feature completeness, label availability, and validation protocol. Each result table therefore reports the analytic test size for that endpoint rather than implying a single global sample size.

## Model-matched and paper-comparable contexts

| n | Where it appears | Meaning |
|---:|---|---|
| 4094 | Paper-comparable cough 10-fold CV | Recording-level cough CV aggregate across folds, used for literature-context comparison, not for the primary validation ladder. |
| 9983 | Paper-comparable speech 10-fold CV | Recording-level speech CV aggregate across folds, used for literature-context comparison. |
| 636 | CNN cough/breath rows | Source-domain spectrogram CNN/BiGRU test rows for cough or breath branches. These are not COUGHVID transfer rows. |
| 1590 | CNN speech row | Source-domain spectrogram CNN/BiGRU speech branch test row. |
| 296-312 | WavLM branch rows | Source-domain WavLM submodality test rows, not multimodal fusion and not COUGHVID transfer. |

## Metadata and confounding controls

| n | Where it appears | Meaning |
|---:|---|---|
| 2862 | Metadata-only participant-split controls | Source-domain metadata-only, symptoms-only, and demographic/protocol-only test rows. |
| 3816 | Strict temporal metadata ablation | Temporal metadata rows with and without recording month. |
| 318 | IPW sensitivity row | Held-out quality-weighted audio fusion set used for measured-confounding sensitivity analysis. |

## Wording rules

- Do not compare n=314 multimodal fusion directly with n=8331 COUGHVID as if they are the same modality or model.
- Do not call the WavLM or CNN rows "external validation"; they are source-domain single-stream checks.
- Do not call the 10-fold CV rows the main validation result; they are paper-comparable context rows.
- Do state that COUGHVID is cough-only and cannot validate breath, speech, or multimodal fusion.
- Do state that the matched cough-only comparison is the fair comparison for COUGHVID transfer.

## One-sentence defense

> Apparent sample-size variation is a consequence of endpoint-specific modality availability and validation role, not inconsistent reporting; the manuscripts now state this explicitly and report n separately for every primary result row.
