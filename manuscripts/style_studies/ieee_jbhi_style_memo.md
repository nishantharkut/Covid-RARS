# IEEE JBHI Style Study Memo

Worker JBHI. Scope: five representative IEEE Journal of Biomedical and Health Informatics papers in biomedical AI, signal processing, digital validation, and respiratory/audio modeling. Sources include IEEE records and accessible full-text/preprint mirrors where needed.

## Papers inspected

1. Idil Aytekin et al., "COVID-19 Detection From Respiratory Sounds With Hierarchical Spectrogram Transformers," 2024, IEEE JBHI 28(3):1273-1284. DOI: https://doi.org/10.1109/JBHI.2023.3339700. Full text inspected via arXiv/ar5iv: https://arxiv.org/abs/2207.09529.
2. Yuhan Chen et al., "Robust Cough Detection With Out-of-Distribution Detection," 2023, IEEE JBHI 27(7):3210-3221. DOI: https://doi.org/10.1109/JBHI.2023.3264783. Full text inspected via author/ResearchGate mirror: https://www.researchgate.net/publication/366231688_Robust_Cough_Detection_with_Out-of-Distribution_Detection.
3. Theresa Bender et al., "Analysis of a Deep Learning Model for 12-Lead ECG Classification Reveals Learned Features Similar to Diagnostic Criteria," 2024, IEEE JBHI 28(4):1848-1859. DOI: https://doi.org/10.1109/JBHI.2023.3271858. Full text inspected via ResearchGate mirror: https://www.researchgate.net/publication/370443864_Analysis_of_a_Deep_Learning_Model_for_12-Lead_ECG_Classification_Reveals_Learned_Features_Similar_to_Diagnostic_Criteria.
4. Saeed Saadatnejad et al., "LSTM-Based ECG Classification for Continuous Monitoring on Personal Wearable Devices," 2020, IEEE JBHI 24(2):515-523. DOI: https://doi.org/10.1109/JBHI.2019.2911367. Full text inspected via ResearchGate/arXiv mirror: https://arxiv.org/abs/1812.04818.
5. Yikai Yang et al., "A Multimodal AI System for Out-of-Distribution Generalization of Seizure Detection," 2022, IEEE JBHI 26(7):3529-3538. DOI: https://doi.org/10.1109/JBHI.2022.3157877. Full text inspected via bioRxiv/ResearchGate mirror: https://www.biorxiv.org/content/10.1101/2021.07.02.450974v1.

## Per-paper observations

### 1. Respiratory-sound HST COVID paper

Structure is canonical IEEE AI-methods style: Abstract and Index Terms, Introduction with clinical motivation and explicit contributions, Related Work split into shallow/deep classifiers, Methods, Results, Discussion, Conclusion. The paper places Methods before Results and uses a long, technical Methods section for datasets, preprocessing, architecture, loss, baselines, implementation, and cross-validation.

Visual presentation is dense and architecture-forward. Early figures establish domain signal evidence: time-domain breathing waveforms with spectrograms, then the HST architecture, local-windowed attention hierarchy, training/validation loss curves, performance plots, and Grad-CAM-like explanatory maps. Tables carry model comparisons, hyperparameters, and task-specific performance across datasets/modalities. Captions are explanatory and often interpret the panel contents, not just name them. Equations are used for STFT/spectrogram construction, attention, and loss; they justify modeling choices without turning the article into a theory paper.

Limitations/future framing appears in Discussion, especially around evaluation of Grad-CAM and uncertainty methods. The claims remain tied to screening and generalization to other respiratory disorders, not clinical deployment.

### 2. Robust cough detection with OOD detection

Section flow is Introduction, Related Work, Proposed Methods, Results and Discussion, Conclusion and Future Work. The paper is problem-driven: it first defines in-distribution versus OOD sounds, then introduces the pipeline and only later moves into experiments.

Figures emphasize operational pipeline and diagnostic behavior: a workflow diagram from audio to mel spectrogram to feature extraction and OOD/cough decisions, schematic confidence/OOD modules, density plots for thresholding, metric comparisons, and sampling-rate/window-size behavior. Tables summarize datasets, confusion/performance metrics, and ablations across sampling frequency/window settings. Captions often include enough detail to understand the experiment without scanning the whole paragraph.

Equation use is moderate and method-specific, mostly around confidence and entropy/OOD loss formulations. Limitations are integrated into the motivation and conclusion: real-world sounds, low sampling rates, and window size are treated as deployment stressors. The conclusion includes future work rather than a separate "Limitations" heading.

### 3. XAI analysis of 12-lead ECG classifier

This paper has a strong clinical-explanation structure: Introduction, Methods, Results, Discussion, Conclusion. Methods begins with a short physiological introduction before technical background, datasets, XAI methods, and quantitative relevance-score analyses. That clinical primer is important: it makes later XAI visualizations interpretable to biomedical readers.

Visual density is high. The paper uses a pipeline overview first, then many multi-panel ECG/relevance plots, lead-level summaries, beat-level heatmaps, and comparisons across CPSC/PTB-XL. It uses few or no main-body tables; figures carry most evidence. Captions are long and self-contained, describing cohorts, color meaning, model outputs, and clinical interpretation of relevance values.

Equation use is heavier than in the cough papers: Integrated Gradients and Layer-wise Relevance Propagation are formally defined with numbered equations before visual results. Limitations are framed in Discussion around XAI validity, dataset differences, and clinical interpretability rather than as a standalone checklist.

### 4. LSTM ECG wearable paper

The article follows the compact engineering-study pattern: Introduction, Proposed Algorithm, Datasets/Experimental Setup, Results, Discussion, Conclusion. It places implementation and resource constraints alongside classification accuracy, which is typical for JBHI wearable or embedded biomedical signal papers.

Figures are compact and practical: model architecture, wavelet/beat processing, performance comparisons, ablation plots, and hardware execution-time breakdowns. Tables are central: heartbeat class definitions, confusion matrices, binary-class metrics, and comparisons to prior work. Captions are shorter than in the XAI paper but still specify panels and measurement context.

Equations are minimal to moderate; the paper leans more on block diagrams and tabulated metrics than derivations. Discussion contains ablation and model-design rationale. Limitations are not strongly separated, but real-time feasibility and wearable constraints are explicitly tested rather than merely asserted.

### 5. Multimodal EEG/ECG seizure generalization paper

The article is validation-heavy and clinically framed. Flow is Introduction, Dataset, Methods, Results, Discussion, Conclusion. Dataset comes before Methods, which works because the claim depends on pseudo-prospective out-of-distribution testing across hospitals/continents.

Visual presentation is less numerous but high-leverage: a multimodal network architecture diagram plus ROC/performance summaries, accompanied by many tables. Tables define TUH, EPILEPSIAE, and RPAH cohorts; report recording hours, seizure counts, and subgroup/test-set composition; and compare EEG-only, ECG-only, fusion, missing-modality, and OOD performance. This table-first style suits clinical validation because cohort definition and test-set provenance are part of the result.

Equations are light relative to the architecture and validation sections. Limitations are discussed through generalization risk, missing modalities, heterogeneous recording equipment, and pseudo-prospective inference. The key style lesson is that JBHI accepts strong negative/robustness framing when the validation design is explicit.

## Cross-paper JBHI style patterns

JBHI AI papers generally put Methods before Results. If Results comes early, the paper still needs a conventional technical section flow with explicit datasets, preprocessing, model, evaluation protocol, and statistical/metric definitions.

Successful papers use the first figure to anchor the study: either signal examples plus spectrograms, a full pipeline, or a model architecture. They do not rely on text-only method descriptions.

Figures are information-dense and multi-panel. Captions usually explain cohort/task, color encodings, metric definitions, and what each panel shows. Captions are longer than generic conference captions but remain factual.

Tables are used for cohort/dataset summaries, model comparison, hyperparameters, confusion matrices, ablations, and external validation. JBHI papers often combine 4-8 figures with 3-8 tables depending on whether the article is visual/XAI-heavy or validation/table-heavy.

Equations are acceptable but purposeful. They define signal transforms, loss functions, attention/XAI methods, or evaluation quantities. Purely decorative equations are uncommon.

Limitations are often embedded in Discussion and Conclusion rather than isolated under a formal "Limitations" header. The strongest papers tie limitations to deployment risks: dataset shift, sampling rate, window size, OOD classes, missing modalities, interpretability validity, and clinical screening versus diagnosis.

## Concrete corrections for the current IEEE JBHI manuscript package

1. Make the article read as a validation study, not a model leaderboard. Lead with clinical and health-informatics risk: temporal drift, metadata shortcut learning, and external transfer failure.

2. Ensure the section order is recognizably JBHI: Introduction with explicit contributions; Related Work or Background; Materials/Data; Methods; Evaluation Protocol; Results; Discussion; Conclusion. If space is tight, combine Materials and Methods, but keep evaluation protocol visible before results.

3. Put a full pipeline or validation-ladder figure first. It should show audio modalities, participant-disjoint/time-aware splits, strict temporal testing, external transfer, metadata-only audit, model training, and final interpretation. JBHI examples use Figure 1 to make the whole study legible.

4. Add or strengthen a dataset/cohort table. It should report modality, source population, sample counts, participant counts when available, COVID/control definition, recording period or time split, and whether each dataset is internal, temporal, external, or metadata-only.

5. Use one compact table for the key validation results rather than scattering metrics in prose. Include internal AUROC, strict temporal AUROC, external-transfer AUROC, and metadata-only AUROC in the same visual field so the degradation argument is immediate.

6. Caption style needs to be self-contained. Every figure caption should define cohorts/tasks, metrics, modalities, split type, and panel labels. Avoid captions that only say "pipeline" or "results"; JBHI captions usually let a reader understand the figure without hunting through the text.

7. Add a short clinical/technical interpretation paragraph after each main result block. The style in JBHI is not just "model A scored X"; it explains what X implies for screening, confounding, robustness, or deployment readiness.

8. Be conservative with diagnostic language. Use "screening model," "validation framework," "risk stratification," or "reliability audit"; avoid wording that implies deployment-ready diagnosis.

9. Include an explicit limitations paragraph in Discussion even if no standalone heading is used. It should cover retrospective/crowdsourced audio, uncertain labels, device/environment variability, metadata confounding, temporal drift, external transfer weakness, and lack of prospective clinical validation.

10. Keep equations minimal unless they clarify the evaluation framework. A compact definition of AUROC/threshold-independent evaluation or metadata-only audit logic is acceptable, but the current manuscript likely benefits more from tables and flow diagrams than extra math.

11. Make architecture diagrams secondary to validation diagrams. The representative JBHI papers include architecture figures when the architecture is the contribution; for this manuscript, the contribution is validation and failure analysis, so visual priority should go to protocol, cohort provenance, performance degradation, and confounding.

12. Align claims with the cover-letter framing: the paper's strongest JBHI fit is trustworthy biomedical ML under shift, not superior COVID detection. The title, abstract conclusion, final discussion, and figure ordering should all reinforce that message.
