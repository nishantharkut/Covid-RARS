# Cover Letter

Dear Editor,

We are pleased to submit "Reliability Validation of COVID-19 Respiratory-Audio Screening Under Temporal Drift, External Dataset Shift, and Metadata Confounding" for consideration in Computers in Biology and Medicine.

The manuscript addresses a biomedical signal-processing validation problem: internally strong respiratory-audio COVID-19 classifiers may not remain reliable under temporal drift, external dataset shift, and metadata confounding. Using Coswara as the multimodal source dataset and COUGHVID only as a cough-only external target, the study evaluates signal quality, acoustic representation, participant-disjoint validation, time-aware validation, strict early-to-late temporal validation, external cough transfer, and metadata-only controls.

The selected ComParE+IS10 source-domain fusion model reached AUROC 0.897 on the existing participant split, while strict temporal validation reached AUROC 0.698. For the fair cough-only external comparison, Coswara internal AUROC was 0.849-0.868 and COUGHVID transfer AUROC was 0.523-0.543. Metadata-only models reached AUROC 0.964, showing that non-audio variables carry substantial label information. The revised manuscript explicitly separates the biomedical claim supported by each protocol: source-domain signal detection, temporal robustness, external cough portability, and metadata-confounding risk. These findings support a conservative biomedical conclusion: respiratory-audio screening papers should foreground modality scope, temporal validation, external validation, calibration behavior, operating-point interpretation, and confounding audits before making clinical utility claims.

The manuscript does not claim deployment readiness, diagnostic use, or causal COVID-specific acoustic biomarkers. All numerical results were computed from the reproducible analysis pipeline; code and derived result tables will be released through an appropriate public archive.

Sincerely,

[Corresponding Author Name]
