# Cover Letter

Dear Editor,

We are pleased to submit "Protocol-Aware Validation of COVID-19 Respiratory-Audio Screening Under Temporal Drift, External Dataset Shift, and Metadata Confounding" for consideration in IEEE Journal of Biomedical and Health Informatics.

The manuscript is a biomedical AI validation study for respiratory-audio COVID-19 screening. It evaluates cough, breath, and speech models across participant-disjoint internal validation, time-stratified validation, strict early-to-late temporal validation, cough-only COUGHVID external transfer, and metadata-only confounding audits. The central argument is that internal respiratory-audio accuracy is not enough unless participant separation, calendar structure, external transfer, and non-audio shortcut risk are evaluated together.

The key results are deliberately conservative. The strongest internal Coswara ComParE+IS10 fusion result reached AUROC 0.897, while time-stratified validation reached AUROC 0.849 and strict temporal validation reached AUROC 0.698. In the model-matched cough-only comparison, Coswara internal AUROC was 0.849-0.868 and Coswara-to-COUGHVID transfer AUROC was 0.523-0.543. Metadata-only models reached AUROC 0.964, indicating substantial confounding risk. COUGHVID is framed only as cough-domain external transfer and not as validation of multimodal fusion.

The manuscript does not claim clinical deployment readiness, diagnostic use, or state-of-the-art superiority. Its contribution is an integrated validation framework and evidence package for trustworthy biomedical machine learning under temporal shift, external dataset shift, and metadata shortcut risk. The revised manuscript makes the admissible claim level explicit for each protocol: source-domain feasibility, temporal robustness, external cough portability, and metadata shortcut risk are reported separately rather than collapsed into one leaderboard.

All numerical results were computed from the reproducible analysis pipeline; code and derived result tables will be released with the repository.

Sincerely,

[Corresponding Author Name]
