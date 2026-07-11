# Publication External Validation Artifacts

Date: 2026-06-12
Scope: COUGHVID v3 external validation after corrected no-leakage Coswara baseline.

Completed:
- COUGHVID v3 extraction
- COUGHVID index
- COUGHVID MFCC feature extraction
- Coswara-to-COUGHVID cough-only external validation
- Feature-shift report
- Paper metric table refresh
- Experiment manifest refresh

Key result:
- Logistic regression cough-only Coswara-to-COUGHVID AUROC: 0.52948
- AUPRC: 0.043007
- Balanced accuracy: 0.522575
- F1: 0.071313
- External labeled rows: 8331
- High-shift features: 21 / 253

Interpretation:
This is evidence of strong cross-dataset shift. It should be framed as an external stress test, not a failed implementation.
