# ESWA Style Memo: ML/Health/Signal-Processing Papers

This memo is based on five Expert Systems with Applications papers inspected beyond the abstract, with attention to article structure, figure/table presentation, captions, and limitations/future-work framing. The main pattern is that ESWA papers are application-first but still method-heavy: they open with a concrete applied problem, show a workflow figure early, use many comparison/ablation tables, and end with a bounded conclusion rather than deployment rhetoric.

## Papers Inspected

### 1. Robust COVID-19 Detection from Cough Sounds using Deep Neural Decision Tree and Forest: A Comprehensive Cross-Datasets Evaluation

Rofiqul Islam, Nihad Karim Chowdhury, Muhammad Ashad Kabir, 2026, ESWA 310, 131235. DOI/URL: https://doi.org/10.1016/j.eswa.2026.131235; accessible preprint: https://arxiv.org/pdf/2501.01117.

Structure: Abstract and keywords, then Introduction, Related work, Research questions, Methodology, Results and discussion, Conclusion. The introduction explicitly lists contributions and ends with a section roadmap. The methodology is long and staged: datasets, feature extraction, feature selection, classifiers, optimization, SMOTE, thresholding, and cross-dataset design.

Visuals/tables: approximately 7 figures and 10 tables in the accessible version. Figures are mostly workflow, feature-selection, confusion-matrix, and distribution plots. Tables carry much of the evidence: prior-study comparison, dataset sample counts, default/optimized hyperparameters, strategy combinations, strategy comparisons, final strategy metrics, state-of-the-art comparison, cross-dataset performance, and combined-dataset comparison. Captions are self-contained and specify classifier, strategy, validation setting, and dataset panels.

Limitations/future framing: limitations are folded into discussion/conclusion rather than isolated in a separately titled limitations section. The paper discusses transfer/generalizability trade-offs across datasets and treats demographic/geographic dataset differences as scientific interpretation, not just error.

### 2. A deep learning method for predicting the COVID-19 ICU patient outcome fusing X-rays, respiratory sounds, and ICU parameters

Yunan Wu et al., 2024, ESWA 235, 121089. DOI/URL: https://doi.org/10.1016/j.eswa.2023.121089; PDF: https://eden.dei.uc.pt/~ruipedro/publications/Journals/ESWA_2024_Wu.pdf.

Structure: Introduction, Materials and methods, Results, Discussion. The paper uses a clinical prediction framing throughout: ICU mortality and 90-day mortality are the endpoints, and the methods section is organized by data modalities and fusion model.

Visuals/tables: 8 figures and 6 tables. The first figure is a full multimodal fusion workflow. Other figures show distribution of longitudinal CXR counts, respiratory-sound preprocessing, model pipeline, example sequential CXRs, spectrograms, generated missing CXRs, and feature distributions by modality. Tables include respiratory-sound feature descriptions, demographic/clinical variables, modality-comparison performance, longitudinal-day ablation, lung-sound window-length ablation, and state-of-the-art comparison. This is a strong ESWA pattern: one early schematic, one or more data/example figures, then ablation and comparison tables.

Limitations/future framing: Discussion has an explicit limitations paragraph. It states dataset scale and single/limited-center issues, notes that longer longitudinal inputs may be needed, and names future work such as more centers and transformer modules. Clinical claims remain bounded to retrospective prediction.

### 3. Efficient fall detection in four directions based on smart insoles and RDAE-LSTM model

Zhirong Lin, Zengwei Wang, Houde Dai, Xuke Xia, 2022, ESWA 205, 117661. DOI/URL: https://doi.org/10.1016/j.eswa.2022.117661; PDF: https://moticon.com/wp-content/uploads/2024/07/pdf-pub-088-Lin-2022-Efficient-fall-detection-in-four-directions-based-on-smart-insoles-and-RDAE-LSTM-model.pdf.

Structure: Introduction, Material and method, RDAE-LSTM model for four-directional fall detection, Experimental results and analysis, Discussion, Conclusion. The first page is final Elsevier style: journal header, article info, keywords, abstract, then two-column body.

Visuals/tables: 7 figures and 5 tables in a compact 9-page article. The visual sequence is device/system diagram, preprocessing signal example, proposed-method flowchart, autoencoder architecture, LSTM cell diagram, ablation plot, and confusion matrices. Tables cover approach comparison, fall-task protocol, model parameters, model-performance comparison, and leave-one-subject-out results. Captions are descriptive and often explain what each subpanel or model component represents.

Limitations/future framing: Discussion and conclusion are practical and restrained. Future work is framed around more IoT deployment data and more samples from elderly or motor-dysfunction users. The article does not oversell clinical readiness.

### 4. Covid-19 vaccine hesitancy: Text mining, sentiment analysis and machine learning on COVID-19 vaccination Twitter dataset

Miftahul Qorib, Timothy Oladunni, Max Denis, Esther Ososanya, Paul Cotae, 2023, ESWA 212, 118715. DOI/URL: https://doi.org/10.1016/j.eswa.2022.118715; accessible text: https://www.researchgate.net/publication/363286328_Covid-19_Vaccine_Hesitancy_Text_Mining_Sentiment_Analysis_and_Machine_Learning_on_COVID-19_Vaccination_Twitter_Dataset.

Structure: Background, Literature review, Methodology, Results, Discussion, Contributions, Conclusions, Future work, Acknowledgment. The introduction explicitly previews the section order. A separate "Gap in literature" subsection lists numbered gaps before methods.

Visuals/tables: at least 5 figures are exposed in the accessible version: experimental design, overview of prior approaches, top word-frequency plot, vaccine-brand tweet plot, and TF-IDF representation example. Table 1 is a long comparative literature table with title, authors, dataset, sentiment technique, classification method, and conclusion. The paper uses more explanatory/descriptive tables than mathematical derivation, which is common for NLP/public-health ESWA papers.

Limitations/future framing: Future work is a separate section. Contributions are also separated before conclusion, which helps ESWA readers see novelty without hunting through discussion.

### 5. RobIn: A robust interpretable deep network for schizophrenia diagnosis

Daniel Organisciak, Hubert P. H. Shum, Ephraim Nwoye, Wai Lok Woo, 2022, ESWA 201, 117158. DOI/URL: https://doi.org/10.1016/j.eswa.2022.117158; project page/PDF: https://hubertshum.com/pbl_eswa2022robin.htm.

Structure: Introduction, Data collection, Deep neural networks, Interpretable artificial neural network, Evaluation, Conclusion and discussions. The accessible version is longer/preprint-like, but the scientific organization is clear: problem, data, model, interpretability, stress tests, conclusion.

Visuals/tables: 9 figures and 4 tables. Figures include overall method overview, network architecture, loss curves, global feature importance, attention heatmaps, three robustness/stress-test plots, and UMAP visualization. Tables cover DSM-5-related dataset attributes, baseline comparisons, robustness/testing comparisons, and state-of-the-art comparison using brain-imaging data. This paper shows that ESWA accepts detailed explanation/stress-test visualization when interpretability is part of the claim.

Limitations/future framing: Future work is stated directly: collect a larger clinical dataset. Robustness limitations are handled through designed stress tests, not only prose.

## Cross-Paper ESWA Style Patterns

- First figure is usually a workflow, system, or model-pipeline figure, not a result plot.
- Tables are central. ESWA papers often use tables for literature positioning, dataset description, hyperparameters, ablation, model comparisons, and state-of-the-art comparisons.
- Captions are self-contained and technical: they name the model, validation setting, dataset/panels, and metric context.
- Section order is flexible, but strong papers make the contribution/gap explicit before methods and include a roadmap paragraph.
- Limitations are accepted and expected. They are often in Discussion/Conclusion, sometimes as a separate future-work section.
- Graphical abstracts/highlights are generally submission assets, not part of the article PDF. Elsevier guidance says graphical abstracts usually appear online rather than in the PDF, and highlights are short separate bullets.

## Concrete Corrections Needed for the Current ESWA Package

1. Replace the graphical-abstract caption-only asset with an actual graphical abstract image if the package includes one. It should be a left-to-right visual pipeline: respiratory-audio datasets -> participant/time/external validation -> model fusion and metadata audit -> observed temporal/external-shift degradation. A caption alone is not a graphical abstract.

2. Keep the five highlights, but submit them as a clean editable highlights file without Markdown scaffolding. The current bullets are within the 85-character norm; the strongest ones are the temporal AUROC drop, COUGHVID transfer, and metadata-only confounding audit.

3. Resolve declaration placeholders before submission: funding, ethics determination, CRediT roles, competing interests, and data/code availability. ESWA style expects complete declarations, not bracketed reminders.

4. Replace "will be released" language with a concrete data/code availability statement before submission. If public release is not ready, state the intended archive, DOI, access conditions, or restriction rationale precisely and avoid vague promises.

5. Ensure the anonymized manuscript has no author-identifying acknowledgments, institution-specific wording, project-ownership clues, or title-page material. ESWA uses double-anonymized review; title page and anonymized manuscript should remain separate.

6. Make the first manuscript figure a polished validation-framework schematic. The studied ESWA papers rely on an early visual overview to teach the reader the experiment before metrics appear.

7. Include at least one compact comparison table against relevant COVID respiratory-audio/COVID cough studies, including the DNDT/DNDF paper, but frame it by validation design and dataset shift rather than claiming raw accuracy superiority.

8. Use captions that state dataset, split, metric, and interpretation. Avoid captions that only name the plotted object; ESWA captions frequently carry enough context to understand the figure independently.

9. Add or sharpen a limitations/future-work paragraph: retrospective datasets, dataset shift, metadata confounding, possible label noise, lack of prospective clinical validation, and the need for multi-site external respiratory-audio validation.

10. Keep the scientific stance conservative. The package already avoids deployment claims; preserve that tone and make the contribution a validation/audit framework for expert-system reliability under temporal and external shift.
