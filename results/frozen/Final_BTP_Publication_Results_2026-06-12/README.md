# Final BTP / Publication Results Bundle

Date: 2026-06-12

Completed:
- Corrected no-leakage Coswara internal pipeline.
- COUGHVID v3 extraction, indexing, MFCC features.
- COUGHVID internal baseline.
- Coswara-to-COUGHVID external validation.
- External model grid: Logistic Regression, Random Forest, XGBoost, LightGBM, CatBoost.
- Feature-shift report.
- Paper metric table and experiment manifest.

Key results:
- Corrected Coswara validation-weighted fusion: AUROC about 0.882, AUPRC about 0.844.
- COUGHVID internal best: LightGBM AUROC about 0.781, AUPRC about 0.178.
- Coswara-to-COUGHVID external best: AUROC about 0.535, AUPRC about 0.042.

Interpretation:
- COUGHVID is moderately learnable internally.
- Coswara-to-COUGHVID transfer is near chance.
- The strongest research finding is cross-dataset/domain shift, not deployment-grade COVID detection.

Do not cite old leaked fusion results.
