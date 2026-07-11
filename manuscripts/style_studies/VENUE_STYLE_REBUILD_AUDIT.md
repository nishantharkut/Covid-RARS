# Venue Style Rebuild Audit

This audit was prepared after inspecting representative papers from the four candidate venues and visually checking the current manuscript PDFs. It intentionally excludes the old project dossier as a scientific or style source. The dossier may be useful as an internal memory artifact, but it should not drive manuscript structure, wording, figures, or claims.

## Evidence Base

Four venue-specific memos were created from five papers each:

- `npj_digital_medicine_style_memo.md`
- `ieee_jbhi_style_memo.md`
- `elsevier_eswa_style_memo.md`
- `elsevier_cbm_style_memo.md`

The local full PDFs inspected directly were:

- Islam et al., "Robust COVID-19 detection from cough sounds using deep neural decision tree and forest: A comprehensive cross-datasets evaluation", Expert Systems with Applications, 2026.
- Aytekin et al., "COVID-19 Detection From Respiratory Sounds With Hierarchical Spectrogram Transformers", IEEE Journal of Biomedical and Health Informatics, 2024.
- Ganitidis et al., JMIR COVID-audio/temporal-drift paper, 2025.

The current generated manuscript PDFs were also visually inspected only to diagnose format and display problems:

- `manuscripts/npj_digital_medicine/main.pdf`
- `manuscripts/ieee_jbhi/main.pdf`
- `manuscripts/elsevier_eswa/main.pdf`
- `manuscripts/elsevier_cbm/main.pdf`

## High-Level Verdict

The current drafts are not yet venue-native. They are scientifically grounded, but they still read like converted analysis reports. The main weakness is not only wording; it is article architecture:

1. The papers do not yet stage evidence like target-journal articles.
2. The figures and tables are too generic and too often conceptual.
3. Captions do not consistently define cohort, split, modality, metric, and interpretation.
4. Literature comparison is too small and too compressed for ESWA/CBM/JBHI.
5. The same core draft has been adapted into multiple venues instead of writing venue-specific papers.
6. Some text still sounds like project provenance rather than scientific reporting.

The strongest publishable framing remains:

Respiratory-audio COVID screening models can appear strong under internal validation, but strict participant separation, chronological testing, metadata-only controls, and external transfer reveal substantial shortcut learning and generalization fragility.

The strongest empirical results to foreground are:

- Internal Coswara multimodal AUROC: 0.897.
- Time-stratified participant split AUROC: 0.849.
- Strict early-to-late temporal AUROC: 0.698.
- COUGHVID external transfer AUROC: 0.543.
- Metadata-only AUROC: 0.964.
- Symptoms-only AUROC: 0.932.
- Removing recording month reduced strict temporal metadata AUROC by 0.247.

## Cross-Venue Rebuild Rules

### 1. Stop writing it as a model leaderboard

The article should not be presented as "we tried many models and failed to beat SOTA." That framing is weak. The paper should be presented as a validation and reliability study showing why internal COVID-audio metrics are not enough.

Model breadth still matters, but as a robustness argument:

- MFCC baseline.
- Extended acoustic features.
- OpenSMILE ComParE2016 and IS10.
- Feature selection using validation-only ranking.
- LightGBM, XGBoost, CatBoost, SVM, random forest, extra trees.
- Multimodal late fusion.
- Paper-comparable 10-fold CV.
- Strict participant, temporal, and external validation.
- Metadata-only and temporal-confounding controls.

This should appear as a controlled validation ladder, not as a scattered model zoo.

### 2. Make Figure 1 do real work

All inspected venues expect an early orienting figure:

- npj: study design or validation ladder.
- JBHI: pipeline/model/evaluation diagram.
- ESWA: workflow or methodology diagram.
- CBM: dataset/protocol/model workflow.

Our Figure 1 should be a polished validation-framework schematic:

Raw respiratory audio and metadata -> quality control -> modality branches -> feature bank and model bank -> fusion -> validation ladder:

1. participant-disjoint internal split,
2. time-stratified participant split,
3. strict early-to-late temporal split,
4. COUGHVID external transfer,
5. metadata-only confounding audit.

The figure should encode evidence, not just a decorative pipeline.

### 3. Add a main cohort/protocol table

Every serious validation paper makes the cohort and split structure visible. A main table should include:

- Dataset.
- Modality.
- Number of recordings.
- Number of participants or recording IDs.
- Positive and negative counts.
- Split/protocol role.
- Time handling.
- External or internal status.
- What models were trained or tested.

This table is required for npj/JBHI/CBM and strongly recommended for ESWA.

### 4. Add one compact primary-results table

The primary table should place all key validation regimes side by side:

- Internal participant split.
- Time-stratified participant split.
- Strict temporal early-to-late split.
- COUGHVID external transfer.
- Metadata-only controls.

Columns should be consistent:

- AUROC.
- AUPRC.
- Balanced accuracy.
- F1.
- Sensitivity.
- Specificity.
- n.
- Modality.
- Feature strategy.
- Model/fusion method.

If confidence intervals are available or can be generated quickly, add them. If not, do not overstate small metric differences.

### 5. Make captions self-contained

Captions must not say only "Pipeline schematic" or "External transfer." A caption should state:

- dataset,
- split,
- modality,
- sample size,
- metric,
- panel meanings,
- conclusion supported by the display.

This is visible across npj, JBHI, ESWA, and CBM papers.

### 6. Expand literature comparison properly

The literature review cannot be four or five papers. The reviewed papers should be grouped by purpose:

- COVID cough classification on Coswara or COUGHVID.
- Multimodal respiratory audio.
- Transformer/spectrogram methods.
- Cross-dataset respiratory-audio validation.
- Medical-AI shortcut learning/confounding.
- Temporal drift and deployment shift.

For comparison tables, do not make raw SOTA claims unless validation designs match. Use two comparison modes:

- Apples-to-apples: our paper-comparable CV versus prior internal/CV results.
- Apples-to-oranges: strict temporal and COUGHVID external transfer versus prior internal results, explicitly labeled as stricter.

### 7. Keep code names out of manuscript prose

Do not write script filenames, folder paths, patch names, log filenames, or implementation history in the manuscript. Scientific papers describe:

- data sources,
- preprocessing,
- model classes,
- feature families,
- validation protocols,
- metrics,
- statistical controls,
- availability.

Implementation details belong in code availability or supplement.

### 8. Treat negative results as reliability evidence

The COUGHVID collapse and temporal drop should not be hidden. They are the central scientific contribution. The tone should be:

Internal benchmark performance alone overestimates likely deployment performance; stricter validation reveals dataset and temporal dependence.

Do not call prior papers fabricated. Say their reported numbers are not directly comparable because their validation designs differ.

## Venue-Specific Rebuild Direction

## npj Digital Medicine

### What inspected npj papers do

npj papers are compact and evidence-dense. They often use:

- one-paragraph abstract,
- short clinical/digital-health introduction,
- Results before Methods,
- cohort table,
- validation table,
- clinical interpretation,
- Methods after Discussion,
- explicit data/code/reporting statements.

Figures are not decorative. A typical npj article uses a study-design figure, performance curves/tables, subgroup or sensitivity analyses, and clinically meaningful interpretation. Limitations are explicit and conservative.

### What our npj draft must become

The npj version should be a methodological digital-health validation paper, not a new-model paper.

Recommended title style:

Confounding and Dataset Shift Limit Generalization in COVID-19 Respiratory-Audio Screening

Required changes:

1. Reduce main displays to the strongest evidence set.
2. Add a main cohort/protocol table.
3. Make the first figure the validation ladder.
4. Put metadata-only AUROC and temporal month-ablation evidence in the main story.
5. Put COUGHVID external transfer in the main story, not as an appendix-like result.
6. Move model-bank detail into Methods or Supplement.
7. Keep Discussion focused on digital-health reliability, shortcut learning, and prospective validation needs.

Best fit:

npj is the strongest venue if the paper is written as a medical-AI reliability audit.

Main risk:

npj will reject quickly if the paper reads like a COVID classifier paper or if external validation appears too weak without being framed as the central finding.

## IEEE JBHI

### What inspected JBHI papers do

JBHI papers are technical biomedical-informatics papers. They usually have:

- Abstract and Index Terms.
- Introduction with clear contributions.
- Related Work.
- Materials/Data.
- Methods before Results.
- Explicit evaluation protocol.
- Dense figures and tables.
- Equations only when they clarify signal processing, modeling, or metrics.

The HST paper uses an early waveform/spectrogram figure, a method architecture, multiple model-comparison tables, and Grad-CAM/saliency visuals because the model architecture is the contribution.

### What our JBHI draft must become

The JBHI version should be a trustworthy biomedical-ML validation framework paper.

Recommended title style:

Validation Under Temporal and External Dataset Shift for Multimodal COVID-19 Respiratory-Audio Screening

Required changes:

1. Use canonical JBHI order: Introduction, Related Work, Materials, Methods, Evaluation Protocol, Results, Discussion, Conclusion.
2. Add a clear Figure 1 pipeline/validation ladder.
3. Add a dataset/protocol table.
4. Use a compact metric table for all main validation regimes.
5. Move Grad-CAM discussion into Related Work or Discussion, not Methods, unless a spectrogram transformer is actually implemented.
6. Explain why interpretability in this work is validation-level: feature importance, metadata-only controls, temporal ablation, and external transfer.
7. Keep equations minimal: metrics and possibly fusion definition are enough.

Best fit:

JBHI is viable if the manuscript is technical, protocol-heavy, and strongly organized around validation under shift.

Main risk:

JBHI may expect stronger technical novelty than a pure audit. The novelty must be stated as an integrated validation framework and multimodal evidence package, not just model fusion.

## Expert Systems with Applications

### What inspected ESWA papers do

ESWA papers are application-first and method-heavy. Strong ESWA papers often include:

- Elsevier front matter in final PDF.
- Highlights.
- Graphical abstract as a separate asset.
- Introduction with contribution bullets.
- Related Work and research gap.
- Methodology with workflow figure.
- Many comparison and ablation tables.
- Results and Discussion combined or adjacent.
- Conclusion with limitations/future work.

The DNDT/DNDF ESWA COVID-cough paper is table-heavy and explicitly emphasizes cross-dataset evaluation, but its reported metrics still need protocol-aware interpretation.

### What our ESWA draft must become

The ESWA version should be an expert-system reliability and validation-framework article.

Recommended title style:

A Protocol-Aware Expert-System Framework for COVID-19 Respiratory-Audio Screening Under Temporal and External Dataset Shift

Required changes:

1. Use Elsevier assets correctly: title page, highlights, declarations, optional graphical abstract.
2. Replace any caption-only graphical abstract with an actual original visual, or omit it.
3. Add contribution bullets in the introduction.
4. Expand Related Work into a proper ESWA literature comparison.
5. Include DNDT/DNDF as a major comparison, but frame by validation protocol.
6. Add a state-of-the-art comparison table with columns for dataset, modality, split, participant isolation, temporal validation, external validation, and metric.
7. Keep final claims conservative: reliability framework, not deployment-ready diagnosis.

Best fit:

ESWA is the best fit if the professor wants an AI/ML venue and expects "method + model + comparison" presentation.

Main risk:

If written too negatively, ESWA reviewers may see it as a benchmark critique rather than an expert-system contribution. The article must show the built framework clearly.

## Computers in Biology and Medicine

### What inspected CBM papers do

CBM papers are conventional medical-AI articles with strong emphasis on:

- biomedical motivation,
- dataset description,
- preprocessing,
- method/fusion design,
- validation metrics,
- tables comparing prior work,
- limitations and clinical implications.

The CBM author guidance and inspected papers show that highlights are required as separate editable bullets, graphical abstracts are encouraged but separate, and first submissions do not need final ScienceDirect layout.

Important venue risk:

The CBM memo notes current indexing/status concerns in the author guidance. This should be checked before final submission decisions.

### What our CBM draft must become

The CBM version should be a biomedical validation and clinical-risk paper.

Recommended title style:

Temporal and External Validation of Multimodal Respiratory-Audio Models for COVID-19 Screening

Required changes:

1. Reduce keywords to at most seven.
2. Move "Relation to Prior Evidence" out of Results and into Related Work or Discussion.
3. Use section order: Introduction, Background and Related Work, Datasets and Quality Control, Methods, Validation Protocols, Results, Discussion, Limitations and Future Work, Conclusion.
4. Add confidence intervals if feasible.
5. Keep clinical interpretation careful: screening reliability, not diagnosis.
6. Strengthen future work around prospective validation, standardized recording, device/country stratification, calibration monitoring, and subgroup analysis.

Best fit:

CBM is scientifically aligned with biomedical audio and validation, but indexing/status risk makes it less attractive unless the professor specifically prefers it.

## Figure and Table Rebuild Checklist

Required main figures:

1. Validation-framework schematic.
2. Validation severity/degradation plot.
3. Metadata confounding or shortcut-risk plot.
4. Optional external-transfer summary plot.

Required main tables:

1. Dataset/cohort/protocol table.
2. Primary validation results table.
3. Literature/protocol comparison table.
4. Metadata/confounding audit table.
5. Optional model-bank/ablation summary table.

Potential supplementary figures/tables:

- Full model-bank results.
- Paper-comparable CV details.
- Feature-selection details.
- Swarm/SSL negative branch results.
- Quality-audit table.
- External COUGHVID feature-coverage details.

## What Not to Do

Do not claim SOTA in raw metric terms unless validation protocols match.

Do not call prior papers fabricated or dishonest.

Do not bury COUGHVID collapse.

Do not add Grad-CAM unless a spectrogram CNN/transformer model is actually part of the final selected model.

Do not over-explain code files in the manuscript.

Do not use AI-generated or decorative graphical abstracts for Elsevier submission.

Do not submit the same paper to all venues with only template changes.

## Recommended Immediate Next Step

Before editing LaTeX again, choose the primary venue:

1. npj Digital Medicine if the goal is a high-risk, high-reward medical-AI reliability paper.
2. ESWA if the goal is a method-heavy AI venue more likely to accept a framework and comparison-heavy article.
3. JBHI if the goal is biomedical informatics with strong validation-method framing.
4. CBM only after checking indexing/status and professor preference.

Then rebuild only that manuscript first. After that manuscript becomes venue-native, adapt the structure to the other venues if needed.

