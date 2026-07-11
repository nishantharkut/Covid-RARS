# Corrected Coswara No-Leakage Results - Windows

Date: 2026-06-12
Platform: Windows
Dataset: Coswara
Scope: Corrected internal Coswara audio pipeline

Important:
- Fusion weights use data/outputs/metrics/ml_validation_metrics.csv.
- ml_validation_metrics.csv contains metric_split = validation.
- Old leaked validation-weighted fusion results must not be cited.
- CNN was disabled.
- COUGHVID was disabled.
- Spectrogram index is absent by design.
- Feature shift report is absent by design.

Main corrected result:
- validation_weighted_auprc fusion AUROC = 0.878167
- validation_weighted_auprc fusion AUPRC = 0.841995
- validation_weighted_auprc balanced accuracy = 0.810793
- validation_weighted_auprc F1 = 0.745098

Use this bundle as the corrected Coswara no-leakage result artifact.
