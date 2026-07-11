# npj Digital Medicine Style Study Memo

Scope: five representative npj Digital Medicine articles relevant to AI/ML, digital biomarkers, and clinical validation. I inspected article text beyond abstracts, including PDF structure, figure/table placement, captions, section flow, and limitations framing.

## Cross-article pattern

npj Digital Medicine research articles are compact and evidence-dense. The standard flow is a one-paragraph abstract, short clinical/digital-health introduction, Results with descriptive subheadings, Discussion, then Methods and reporting/data/code statements. The Results usually starts with cohort/data description and a study-design figure or cohort table, then moves quickly to validation performance, subgroup/sensitivity analyses, and clinical interpretation. Methods are detailed but placed late.

Visual presentation is data-first. Most articles use one overview schematic at most, then performance curves, boxplots, cumulative-incidence curves, segmentation examples, or tabular validation comparisons. Captions are not decorative: they define cohorts, metrics, thresholds, panels, and interpretation. Limitations are usually embedded near the end of Discussion and are explicit about generalizability, label quality, cohort imbalance, retrospective design, prospective validation needs, or implementation constraints.

## Articles inspected

### 1. Digital biomarkers of mood disorders and symptom change (2019)

DOI/URL: https://doi.org/10.1038/s41746-019-0078-0

Structure: 3-page short article. Flow is Introduction, Results, Discussion, Methods-style sections ("Measures", "Actigraphy", "Planned analyses"), Reporting summary, Data availability. Results are only a few paragraphs and immediately report diagnostic classification and symptom-change prediction.

Visuals: 2 main figures, no main tables. Fig. 1 is a simple confusion matrix with accuracy and kappa embedded visually. Fig. 2 overlays observed vs predicted standardized symptom-change values by patient index. Captions are brief but specify prediction target and visualization scale.

Style notes: This paper is very compact and relies on clear numeric claims in prose. Figures are plain statistical graphics, not conceptual diagrams. Limitations are direct: combined MDD/bipolar grouping, missing medication/treatment data, inpatient participants with constrained movement, and baseline diagnostic status.

### 2. Crowdsourcing digital health measures to predict Parkinson's disease severity: the Parkinson's Disease Digital Biomarker DREAM Challenge (2021)

DOI/URL: https://doi.org/10.1038/s41746-021-00414-7

Structure: 12-page article. Flow is Introduction, Results with subchallenge-specific performance, Discussion, Methods. Methods are extensive because they describe datasets, challenge design, scoring, bootstrapping, and winning methods.

Visuals: about 4 main figures and 1 main demographics table, with many supplementary analyses. Fig. 1 is a workflow schematic showing training/test data, withheld labels, participant feature submissions, organizer models, and scoring. Fig. 2 is a dense multi-panel bootstrap/boxplot performance ranking across teams and symptoms. Later figures emphasize feature clustering and task-level performance. Captions are long enough to define subchallenges, metrics, bootstrapping, and baselines.

Style notes: The article balances one accessible workflow diagram with dense validation graphics. It frames validation as unbiased benchmarking, repeatedly contrasts participant submissions with baseline models, and treats demographic/metadata baselines as substantive evidence rather than a side check. Limitations are discussion-integrated: dataset imbalance, weaker performance in sex/age subgroups, small validation datasets for deep learning, and interpretability limits.

### 3. Derivation, external and clinical validation of a deep learning approach for detecting intracranial hypertension (2024)

DOI/URL: https://doi.org/10.1038/s41746-024-01227-0

Structure: 7-page article. Flow is Introduction with Fig. 1 before Results, Results with cohort description, model performance, phenotype associations, explainability, then Discussion and Methods. Methods detail waveform filtering, model architecture, validation sets, metrics, and phenotype association analysis.

Visuals: 2 main figures and 2 main tables. Fig. 1 is a two-part schematic: dataset preprocessing/filtering and model architecture/output. Fig. 2 presents AUROC/AUPRC performance. Table 1 gives cohort demographics; Table 2 gives internal/external model performance with confidence intervals. Some waveform explainability is pushed to supplementary figures.

Style notes: This is a strong model for validation-paper structure: overview schematic, cohort table, performance table, then concise curves. It explicitly separates internal test and external validation. Limitations emphasize external cohort size, demographic/socioeconomic distribution differences, exclusions due to waveform drift, non-time-locked diagnoses, and need for prospective implementation studies.

### 4. A real-world clinical validation for AI-based MRI monitoring in multiple sclerosis (2023)

DOI/URL: https://doi.org/10.1038/s41746-023-00940-6

Structure: 9-page article. Flow is Introduction, Results, Discussion, Methods. Results are clinically organized: cohort/scans, tool integration, lesion metrics, volumetrics, comparison against radiology reports and core lab.

Visuals: 1 main figure and 6 main tables. Fig. 1 is a PACS-style clinical imaging example with MRI overlays and masks. The validation burden is carried by tables comparing lesion metrics, incidental findings, lesion activity sensitivity/specificity/accuracy/F1, volumetrics, and clinical correlations.

Style notes: This article shows that npj Digital Medicine accepts table-heavy validation when clinical comparison is central. The sole figure is concrete clinical evidence, not an abstract schematic. Limitations are specific: scanner concentration, protocol stability, core-lab dependency on related segmentation methods, imperfect blinding of consensus review, and comparator availability.

### 5. A deep learning digital biomarker to detect hypertension and stratify cardiovascular risk from the electrocardiogram (2025)

DOI/URL: https://doi.org/10.1038/s41746-025-01491-8

Structure: 9-page article. Flow is Introduction, Results, Discussion, Methods, Data availability, Code availability. Results begin with population characteristics, then digital biomarker validation, cardiovascular risk stratification, and model interpretability.

Visuals: 4 to 5 main display items, including 1 main patient-characteristics table. Fig. 1 is a study-design/model overview. Fig. 2 and Fig. 3 are cumulative-incidence/risk-stratification plots. Fig. 4 compares adjusted hazard ratios for HTN-AI, systolic BP, and pulse pressure. Interpretability graphics are largely supplementary. Captions are paragraph-length and explain cohorts, outcomes, stratification, and clinical interpretation.

Style notes: The paper uses a strong validation ladder: internal validation, external validation, gold-standard ambulatory BP subset, incident diagnosis proxy, downstream cardiovascular outcomes, and interpretability. Limitations are framed after clinical implications and include imperfect EHR/office-BP training labels, need for prospective validation against ambulatory BP monitoring, and uncertainty about whether the score captures modifiable risk.

## Concrete corrections for the current npj manuscript package

1. Rebalance main displays toward npj norms. Six main figures is likely high for this article type unless each is data-rich and indispensable. Use one study-design/evaluation-ladder schematic as Fig. 1, then prioritize validation results and confounding evidence. Move secondary conceptual or interpretive graphics to supplement.

2. Add or elevate main tables. Representative npj validation papers almost always include a cohort/data table and often a compact performance table. The current package should have a main dataset/partition table with sample sizes, positives, modalities, time windows, and validation role, plus a main validation table summarizing internal, time-stratified, temporal, metadata-only, and external-transfer results.

3. Make captions more explanatory. Each main caption should define the dataset split, n, metric, comparator, panel labels, and what conclusion the reader should draw. Captions should be closer to the HTN-AI and DREAM style than to terse figure labels.

4. Make Results section order mirror validation logic. Start with data sources and evaluation design, then participant-disjoint/internal performance, temporal degradation, external transfer, metadata-only/confounding analyses, and clinical-reliability interpretation. Avoid putting methods mechanics before the reader sees the validation question and result hierarchy.

5. Strengthen limitation framing in Discussion. Include a dedicated limitations paragraph covering observational labels, crowdsourced/self-reported data, symptom and protocol confounding, temporal drift, cross-dataset modality mismatch, lack of prospective clinical validation, and why results should not be read as deployment readiness.

6. Keep the claim level conservative. npj examples make clinical relevance explicit but avoid overclaiming when evidence is retrospective. The manuscript should consistently present itself as a reliability/validation audit of respiratory-audio benchmarks, not as a clinical screening model or a new state-of-the-art detector.

7. Shift visual style from conceptual to clinical-evidence density. Prefer neutral, clean, panelled plots: validation ladder, performance degradation across splits, external-transfer failure, metadata-only/confounding comparison, and a concise clinical interpretation graphic. Avoid decorative icons or repeated process diagrams unless they directly encode evidence.

8. Bring metadata baselines into the main scientific story. The DREAM paper treats demographic/meta-data baselines as a core validation benchmark. This manuscript should similarly make metadata-only performance and month/protocol confounding central, not ancillary.

9. Use Methods-after-Discussion density. Keep detailed preprocessing, model families, split construction, metric definitions, and statistical comparisons in Methods, while Results should report only enough design detail to interpret the evidence.

10. Final submission package should read like a journal article, not an analysis report. Remove any remaining provenance-style phrasing from manuscript prose and captions; describe datasets, validations, and availability in plain scientific terms.
