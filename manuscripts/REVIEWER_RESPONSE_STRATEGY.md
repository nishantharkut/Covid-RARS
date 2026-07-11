# Reviewer Response Strategy

This is a pre-emptive response bank for the current COVID-19 respiratory-audio manuscripts. It is not submission text by itself. Use it to keep the paper's claims precise during revision, presentation, and peer review.

## 1. Why is COUGHVID external validation not run with WavLM or CNN-BiGRU?

The completed external validation is a Coswara-to-COUGHVID cough-only transfer experiment using frozen ComParE+IS10 handcrafted descriptors and source-domain model selection. It is not a WavLM or CNN-BiGRU external-transfer experiment.

The defensible framing is:

> We deliberately used ComParE+IS10 for the COUGHVID endpoint as a standardized, reproducible paralinguistic-feature stress test. This representation is close to the classical handcrafted-feature paradigm used in much of the respiratory-audio baseline literature and can be applied to the target corpus without target-domain tuning. The result therefore tests whether a common Coswara-trained cough pipeline transports to an independent cough dataset. It does not claim that every possible deep representation would fail externally.

Numbers to use:

- COUGHVID external LightGBM SMOTE: AUROC 0.5428, AUPRC 0.0405, balanced accuracy 0.5102, F1 0.0583, sensitivity 0.0842, specificity 0.9361, n=8331.
- COUGHVID external SVC-RBF: AUROC 0.5226, AUPRC 0.0370, balanced accuracy 0.5002, F1 0.0582, n=8331.
- COUGHVID external CatBoost: AUROC 0.5313, AUPRC 0.0405, balanced accuracy 0.5064, F1 0.0594, n=8331.
- COUGHVID external XGBoost: AUROC 0.5318, AUPRC 0.0395, balanced accuracy 0.5051, F1 0.0627, n=8331.

Boundary statement:

> The manuscript should not say that WavLM, CNN-BiGRU, or multimodal fusion failed externally on COUGHVID. It should say that a frozen ComParE+IS10 cough branch failed to transport robustly from Coswara to COUGHVID.

## 2. Why is the 0.897 fusion result higher than WavLM and CNN-BiGRU?

The rows are not the same experiment. The 0.897 AUROC row is a selected Coswara source-domain multimodal fusion endpoint. The WavLM and CNN-BiGRU rows are non-final, source-domain, single-stream branch checks.

Numbers to use:

- Final Coswara participant-split fusion: cough+speech stacked logistic fusion, AUROC 0.8971, AUPRC 0.8627, balanced accuracy 0.8247, F1 0.7522, n=314.
- WavLM shallow cough test: AUROC 0.7898, AUPRC 0.7306, balanced accuracy 0.7126, F1 0.6139, n=310.
- WavLM heavy cough test: AUROC 0.7888, AUPRC 0.6955, balanced accuracy 0.7300, F1 0.6355, n=312.
- WavLM shallow breath test: AUROC 0.7903, AUPRC 0.6540, balanced accuracy 0.7306, F1 0.6271, n=296.
- WavLM deep breath test: AUROC 0.7820, AUPRC 0.6737, balanced accuracy 0.7139, F1 0.6023, n=298.
- CNN-BiGRU cough: AUROC 0.7298, AUPRC 0.5563, balanced accuracy 0.6863, F1 0.5858, n=636.
- CNN-BiGRU breath: AUROC 0.7097, AUPRC 0.5899, balanced accuracy 0.6492, F1 0.5497, n=636.
- CNN-BiGRU speech: AUROC 0.6762, AUPRC 0.4896, balanced accuracy 0.6382, F1 0.5237, n=1590.

Response wording:

> The 0.897 row is a multimodal source-domain fusion endpoint, whereas WavLM and CNN-BiGRU were evaluated as isolated source-domain branches. Their lower AUROC values do not contradict the fusion result; they show that no single practical branch displaced the fused ComParE+IS10 endpoint in this retrospective audit.

## 3. How should the IPW sensitivity analysis be defended?

Do not overclaim causality. The IPW result is a measured-confounding sensitivity analysis. It shows that measured adjustment changes the estimate materially, but an above-chance residual audio signal remains under moderate truncation.

Primary defensive rows:

- Unweighted quality-weighted audio fusion: AUROC 0.8787, AUPRC 0.8324, balanced accuracy 0.8044, ESS 318.0, mean absolute SMD 0.2240, max absolute SMD 1.3838.
- IPW cap 2, q=0.95: AUROC 0.8074, AUPRC 0.6238, balanced accuracy 0.7417, ESS 238.7, mean absolute SMD 0.1491, max absolute SMD 0.7240.
- IPW cap 5, q=0.95: AUROC 0.7926, AUPRC 0.5725, balanced accuracy 0.7306, ESS 173.2, mean absolute SMD 0.1294, max absolute SMD 0.5233.
- IPW cap 10, q=0.99: AUROC 0.7799, AUPRC 0.5372, balanced accuracy 0.7211, ESS 130.4, mean absolute SMD 0.1178, max absolute SMD 0.3815.

Do not lead with cap 20 q=1.00 because ESS collapses to 69.5. It should be treated as a stress boundary, not as the main inferential row.

Response wording:

> IPW does not prove a causal COVID-specific acoustic biomarker. It shows that measured adjustment reduces AUROC from 0.879 to 0.780-0.807 under defensible truncation settings. The cap-10 row improves measured balance substantially while retaining ESS 130.4 and AUROC 0.780. This supports qualified residual signal, while confirming that unadjusted source-domain performance was inflated by observational imbalance.

## 4. Does cough-only COUGHVID make the external comparison unfair?

COUGHVID is cough-only, so it cannot validate breath, speech, or multimodal fusion. That limitation must remain explicit.

The fair comparison is not Coswara multimodal fusion versus COUGHVID cough transfer. The fair comparison is Coswara cough-only internal rows versus COUGHVID cough-only external rows under the same feature strategy.

Numbers to use:

- Coswara cough-only internal AUROC range: 0.849-0.868.
- COUGHVID cough-only external AUROC range: 0.523-0.543.

Response wording:

> We agree that COUGHVID cannot validate multimodal fusion. For that reason, the manuscript separates the selected validation ladder from the model-matched cough-only ladder. The matched cough comparison shows that even when modality is held to cough, portability is weak.

## 5. Why are structural confidence intervals not in every final ladder row?

Honest limitation:

> The paper-comparable 10-fold cross-validation rows include fold-level variability, but the primary selected validation ladder currently reports point estimates. We therefore use the final ladder to support large validation-pattern changes, not small pairwise model rankings. DeLong, bootstrap, or paired-resampling intervals are a necessary extension before making fine-grained statistical comparisons.

Numbers to use:

- Paper-comparable cough SVC: AUROC 0.819 +/- 0.029, AUPRC 0.728 +/- 0.036.
- Paper-comparable cough LightGBM: AUROC 0.819 +/- 0.027, AUPRC 0.732 +/- 0.035.

## 6. How should SMOTE and feature-selection artifacts be discussed?

Do not deny the risk. The correct defense is that feature selection and SMOTE were source-domain operations and not tuned on COUGHVID.

Response wording:

> The final top-800 feature strategy was selected in the Coswara source-domain workflow and frozen before COUGHVID transfer. COUGHVID labels were not used for feature selection or retuning. This does not remove the risk that the selected source features capture source-domain batch or protocol effects; that risk is part of the reason external transfer is treated as a stress test rather than as deployment validation.

## 7. Did we prove audio adds incremental value over symptoms?

No. The manuscript should not claim formal incremental clinical utility over symptoms.

Response wording:

> Symptoms-only metadata reached AUROC 0.932, and full safe metadata reached AUROC 0.964. These results show strong non-audio label structure. We did not perform formal incremental-value testing such as net reclassification improvement, decision-curve analysis, or paired delta-AUROC for audio added to symptoms. The manuscript therefore frames symptoms as a confounding control, not as a combined clinical model.

## 8. One-line defense of the whole paper

> This is not a raw SOTA engineering paper. It is a reliability audit showing that internally strong COVID-19 respiratory-audio results must be interpreted through modality scope, temporal shift, external transfer, metadata shortcut risk, and measured-confounding sensitivity.
