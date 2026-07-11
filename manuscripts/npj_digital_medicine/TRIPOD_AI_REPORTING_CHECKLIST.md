# TRIPOD+AI Reporting Checklist Map for the npj Digital Medicine Draft

Sources checked:

- EQUATOR Network TRIPOD statement page: https://www.equator-network.org/reporting-guidelines/tripod-statement/
- BMJ TRIPOD+AI statement: https://www.bmj.com/content/385/bmj-2023-078378
- TRIPOD+AI expanded checklist PDF: https://www.tripod-statement.org/wp-content/uploads/2024/04/TRIPODAI-Supplement.pdf

This is a working author checklist map, not the final official submission checklist. After the final PDF is frozen, add page numbers to the "Manuscript location" column.

| TRIPOD+AI area | Status | Manuscript location | Notes/action before submission |
|---|---|---|---|
| Title identifies target population, prediction/evaluation task, and outcome | Partial | Title page | Title is reliability-audit focused. Keep COVID-19 respiratory-audio and benchmark reliability explicit. |
| Abstract reports study context, design, data sources, endpoints, and main performance | Met | Abstract | Abstract now states Coswara source-domain, COUGHVID cough-only transfer, metadata controls, and IPW sensitivity. |
| Healthcare context and rationale | Met | Introduction | Frames COVID-19 audio screening as diagnostic/screening reliability rather than raw model optimization. |
| Objectives | Met | Introduction | Objectives separate source-domain discrimination, temporal robustness, confounding, and external cough transfer. |
| Source of data | Met | Methods/Data | Coswara and COUGHVID roles are distinguished; COUGHVID is cough-only. |
| Eligibility/inclusion and exclusion | Partial | Methods/Data and dataset role table | Add a supplementary data-flow table if final submission allows. Unknown labels and quality-screened rows should remain visible. |
| Outcome definition | Partial | Methods/Outcome | State that labels are dataset-provided binary COVID-19 status and are not independently adjudicated. |
| Predictors/features | Met | Methods/Audio representations and metadata controls | Acoustic features, metadata groups, and frozen ComParE+IS10 top-800 feature strategy are described. |
| Sample size | Partial | Dataset role table and result tables | Endpoint-specific n is reported. Add a sentence that n varies by modality availability, feature completeness, label availability, and validation protocol. |
| Missing data and unknown labels | Partial | Methods/Data | Unknown labels are excluded from supervised metrics. If space permits, include the unknown-label count in supplementary material. |
| Statistical methods and model development | Met | Methods/Model bank, fusion, validation protocols | Includes feature selection, SMOTE, model families, threshold selection, and fusion scope. |
| Internal validation | Met | Results/Primary validation results | Participant-disjoint and time-stratified Coswara endpoints are described. |
| Temporal validation | Met | Results/Primary validation results | Strict early-to-late temporal validation is reported. |
| External validation/evaluation | Partial | Results/Cough-only COUGHVID transfer | External validation is cough-only and ComParE+IS10 based. Do not overstate as multimodal or deep external validation. |
| Model performance measures | Partial | Results tables | AUROC, AUPRC, balanced accuracy, F1, sensitivity, specificity, calibration metrics where available. Structural confidence intervals are not available for all final ladder rows. |
| Calibration | Partial | Limitations | Calibration behavior is acknowledged, but final calibration plots/intervals are not complete for all endpoints. |
| Model specification/reproducibility | Partial | Methods and availability statement | Methods identify model families and feature strategy. For submission, provide code and aggregate outputs in a public repository or supplement. |
| Risk of bias/limitations | Met | Discussion/Limitations | COUGHVID modality asymmetry, missing structural CIs, retrospective labels, and measured-confounding limits are explicit. |
| Interpretation by validation target | Met | Results/Discussion | Manuscript separates source-domain, temporal, external cough, and metadata-control claims. |
| Fairness/subgroups | Partial | Limitations | Demographic/protocol metadata are audited, but subgroup fairness/calibration is not fully evaluated. Keep as limitation/future work. |
| Registration/protocol | Not registered | Methods or submission notes | State that this is a retrospective benchmark audit and was not prospectively registered, unless institutional documentation exists. |
| Data and code availability | Partial | Data availability | Raw datasets must be obtained from maintainers; release code, aggregate metrics, figures, and derived tables where allowed. |
| Funding/conflicts/ethics | Needs final author input | End matter | Add final funding, conflicts, and ethics/data-use statements from the team. |

## Submission-facing paragraph to keep consistent

This study evaluates existing public datasets retrospectively. It should be reported as development plus evaluation of benchmark models under multiple validation targets, not as a prospective clinical trial and not as a deployment-ready diagnostic tool. The strongest TRIPOD+AI alignment is transparent reporting of data roles, predictors, validation targets, model performance, and limitations. The weakest areas are structural confidence intervals/calibration for every final ladder row, prospective registration, and subgroup/fairness validation.
