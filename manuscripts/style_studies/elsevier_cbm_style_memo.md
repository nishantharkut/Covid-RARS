# Elsevier CBM Style Study Memo

Scope: five representative Computers in Biology and Medicine papers in medical AI, biomedical signal processing, and respiratory-audio modeling. I inspected accessible full text, accepted versions, final PDF layout where available, figure/table captions, section ordering, metric reporting, limitation language, and current CBM author guidance.

Important venue note: the current CBM guide says the journal was placed "On Hold" in April 2024 and that Web of Science Core Collection coverage was discontinued for content after Volume 172 (2024). Treat the style notes below as manuscript-preparation guidance, but make the submission decision with that indexing/status risk visible.

## Papers inspected

1. Madhurananda Pahar et al., "COVID-19 cough classification using machine learning and global smartphone recordings," Computers in Biology and Medicine 135, 104572, 2021. DOI: https://doi.org/10.1016/j.compbiomed.2021.104572. Full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC8213969/.

2. Nihad Karim Chowdhury et al., "Machine learning for detecting COVID-19 from cough sounds: An ensemble-based MCDM method," Computers in Biology and Medicine 145, 105405, 2022. DOI: https://doi.org/10.1016/j.compbiomed.2022.105405. Full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC8926945/.

3. Madhurananda Pahar et al., "COVID-19 detection in cough, breath and speech using deep transfer learning and bottleneck features," Computers in Biology and Medicine 141, 105153, 2022. DOI: https://doi.org/10.1016/j.compbiomed.2021.105153. Accepted version inspected: https://eprints.whiterose.ac.uk/id/eprint/221840/8/2104.02477v4.pdf.

4. Juan Miguel Lopez Alcaraz et al., "Enhancing clinical decision support with physiological waveforms - A multimodal benchmark in emergency care," Computers in Biology and Medicine 192, Part A, 110196, 2025. DOI: https://doi.org/10.1016/j.compbiomed.2025.110196. Accepted version inspected: https://arxiv.org/abs/2407.17856.

5. Abdul Jabbar et al., "Automated detection of pediatric congenital heart disease from phonocardiograms using deep and handcrafted feature fusion," Computers in Biology and Medicine 197, 110993, 2025. DOI: https://doi.org/10.1016/j.compbiomed.2025.110993. Final-style PDF inspected via arXiv record: https://arxiv.org/abs/2604.24767.

## Cross-paper CBM patterns

### Front matter and abstract

Final CBM layout uses the Elsevier/ScienceDirect front matter: journal banner, article title, author affiliations, article-info block, keywords, abstract block, DOI, received/revised/accepted dates, and corresponding-author note. First submission should not imitate that final layout; CBM explicitly says first submissions do not need journal-final formatting and final-layout reproductions can be returned.

Abstracts are concise and factual. The official limit is 250 words. Most article-body abstracts are one paragraph, but the 2025 waveform benchmark uses a structured accepted-version abstract with Background, Methods, Results, and Conclusions. Either form can feel native if it clearly states purpose, data, method, principal metrics, and conclusion. The strongest abstracts include dataset size and headline metrics, but do not become a full results table.

CBM requires 1 to 7 keywords. The current manuscript has 8 keywords, so it should drop or merge one.

### Highlights and graphical abstract

CBM requires 3 to 5 highlights, maximum 85 characters each, as a separate editable file. The current highlights file is compliant on count and length.

Graphical abstracts are encouraged, not part of the article body in the inspected PDFs. If submitted, it must be a separate file, readable at 5 x 13 cm, at least 531 x 1328 pixels or proportional. Elsevier guidance does not permit generative AI or AI-assisted tools to create or alter submitted figures or graphical abstracts unless that use is part of the research design and reproducibly described. A caption-only graphical abstract file is not enough; either prepare a separate original graphic from existing study visuals or omit it.

### Section ordering

The common article flow is conventional engineering/medical-AI structure:

- Introduction with clinical motivation and contribution claim.
- Related work or background early, especially in method-heavy papers.
- Data/materials and preprocessing before models.
- Methods/modeling/training/evaluation protocol before results.
- Results with subsectioned metric comparisons.
- Discussion, limitations/future work, conclusion.
- Declarations, CRediT, competing interests, funding, acknowledgments, data/code statements as required.

The COVID-audio papers are especially method-forward: Data, preprocessing, feature extraction, classifiers, hyperparameter optimization, cross-validation, then results. The 2025 waveform paper uses Introduction, Methods, Results, Discussion, Limitations, Future research directions, Potential implications, and statements. The pediatric PCG paper uses Introduction, Related works, Methods, Results, Discussion, Limitations leading to future work, Conclusion, then CRediT/declarations.

For the current manuscript, "Relation to Prior Evidence" should not sit inside Results. Move it to a Related Work/Background section before Methods or fold it into Discussion. "Clinical Motivation" can be merged into Introduction or renamed as Background and Related Work so the paper reads less like a position essay and more like a CBM empirical study.

### Figures, tables, and captions

Display density is high but functional. The inspected papers ranged from sparse benchmark articles with 2 main figures and several appendix tables to respiratory-audio papers with 7 to 11 figures and 5 to 10 tables. CBM accepts table-heavy evidence when tables define datasets, hyperparameters, training strategies, metric matrices, confusion matrices, feature selection, and state-of-the-art comparisons.

Figure 1 is usually orienting: dataset geography/distribution, proposed method overview, clinical workflow, or model pipeline. Later figures are evidence-bearing ROC/PR curves, confusion matrices, architecture diagrams, feature-contribution plots, or metric comparisons.

Captions are not terse labels. A native CBM caption has a brief title plus a description. It often defines the dataset, split, model, metric, panel labels, abbreviations, and what the reader is seeing. The current captions are generally too short, especially "Pipeline schematic," "Metadata confounding audit," and "COUGHVID cough-only external transfer." They should define cohorts, n, split/protocol, modalities, and metric interpretation in the caption or table note.

Tables must stay editable, avoid vertical rules and shading, and should not duplicate prose. The current use of booktabs is aligned with CBM guidance. The current 7 figures and 7 tables are within observed CBM density, but several figures are conceptual schematics. CBM-native display priority should be: dataset/protocol overview, validation degradation, external transfer, metadata confounding, and compact comparison tables. Secondary conceptual figures such as fusion and clinical interpretation maps can move to supplement unless they encode evidence that is not otherwise visible.

### Limitations and future work

Limitations language is explicit and practical. The pediatric PCG paper uses a standalone "Limitations leading to future work" section and directly names single-country data, single-device recording, need for geographic/device diversity, signal-quality assessment, multimodal additions, and multiclass subtype work. The waveform benchmark names label-source bias, single-center transferability limits, excluded modalities, and interpretability limits. COVID-audio papers often place future-work language in the conclusion rather than a separate limitation section.

The current manuscript already has a Limitations section, which is good. Make it more CBM-native by tying each limitation to an empirical risk and future validation step: retrospective crowdsourcing, self-reported or noisy labels, device/environment variation, symptom/protocol confounding, temporal drift, COUGHVID cough-only modality mismatch, lack of prospective clinical validation, missing confidence intervals/subgroup calibration, and need for event-level segmentation or standardized recording.

### Metric comparison style

CBM papers compare metrics in tables, not only prose. Common metrics include AUC/AUROC, accuracy, sensitivity/recall, specificity, F1-score, precision, false positive/negative rates, confusion matrices, and sometimes multi-criteria model selection. The better clinical-AI papers report split design and uncertainty; the 2025 waveform benchmark reports macro AUROC with 95% bootstrap confidence intervals.

The current manuscript has the right metric family and a strong validation ladder, but it should add uncertainty wherever possible. Add confidence intervals or bootstrap intervals for headline AUROC/AUPRC/balanced accuracy rows. Keep prevalence and n visible because AUPRC and threshold metrics are prevalence-sensitive. When comparing internal, temporal, external, and metadata-only models, keep metric columns consistent so degradation is visually obvious.

## Concrete corrections for the current CBM manuscript package

1. Reduce keywords from 8 to 7 or fewer. A likely merge is "external validation" with "clinical screening" or dropping "calibration" if calibration is not yet a main displayed result.

2. Add an early Related Work or Background and Related Work section. Move the current "Relation to Prior Evidence" material out of Results.

3. Consider this section order: Introduction; Background and Related Work; Datasets and Quality Control; Methods; Validation Protocols; Results; Discussion; Limitations and Future Work; Conclusion; required statements. This keeps the clinical motivation, but makes the paper read like a CBM empirical article.

4. Keep the validation framing. CBM explicitly screens against unclear train/validation/test splits and minor architecture gains, so the manuscript's strength is not a new architecture. Its strength is transparent participant, temporal, external-transfer, and metadata-confounding validation.

5. Expand captions and table notes. Every display should state dataset, split/protocol, modality, n, metrics, and abbreviation definitions where needed.

6. Consolidate conceptual figures if space or readability becomes tight. One overview/protocol figure is enough; the remaining main figures should carry data or clinical interpretation not already in tables.

7. Add confidence intervals or other uncertainty estimates to the headline validation table. If not possible, explicitly say why and avoid making small metric differences sound meaningful.

8. Keep the metadata-only audit central. The MCDM and waveform papers show that CBM accepts multi-metric comparison tables; a side-by-side table of audio, temporal, external, and metadata baselines is venue-native.

9. Strengthen limitations/future-work language. Name the exact clinical-validation gap and what future work would address it: prospective cohort, standardized recording, device/country stratification, event-level cough/breath/speech segmentation, calibration monitoring, and subgroup analysis.

10. Prepare required submission statements. The article package should include CRediT, competing interests, funding/sponsor role, ethics/informed-consent rationale, data availability, and any generative-AI declaration if applicable. A separate declarations file is useful, but the manuscript should not leave required statements ambiguous.

11. Do not imitate final ScienceDirect two-column layout for first submission. The current `elsarticle` preprint approach is appropriate; make it cleaner and more evidence-dense rather than more visually final.

12. If using a graphical abstract, build it from original project visuals such as the validation ladder or dataset/protocol flow, not from generated artwork. It should summarize the validation framework, not advertise a deployment-ready diagnostic tool.

