# Venue Guidance

Scope: manuscript-style and submission-format guidance for four possible targets:
npj Digital Medicine, IEEE Journal of Biomedical and Health Informatics (JBHI),
Elsevier Expert Systems with Applications (ESWA), and Elsevier Computers in
Biology and Medicine (CBM).

Core style rule for all targets: the main manuscript prose should not mention
internal code filenames, CSV filenames, local paths, patches, logs, generated
build artifacts, or repository mechanics. Put reproducibility details in Code
Availability, Data Availability, cited software/data references, or, where the
venue permits, Supplementary Methods/Supplementary Information.

## Quick Comparison

| Target | Initial format | Review identity | Abstract | Highlights | Graphical abstract | Data/code posture |
| --- | --- | --- | --- | --- | --- | --- |
| npj Digital Medicine | Initial submission need not follow final formatting; compiled PDF or Word with figures is encouraged | Not stated as double-anonymous in the npj guidance | Article abstract up to 150 words, no subheadings | Not requested in official npj content-type guidance | Not requested in official npj content-type guidance | Data Availability mandatory; Code Availability where applicable |
| IEEE JBHI | Use IEEE/JBHI author instructions and IEEE journal article structure; verify current journal-specific page limits in the submission portal | IEEE peer review policy applies; journal-specific process should be checked in JBHI instructions | IEEE journal abstract: single paragraph up to 250 words | Not part of IEEE journal article requirements | Optional only if the submission system/journal accepts it; it must be submitted for peer review if used | Data/code sharing encouraged for reproducibility; human/animal ethics statements required when applicable |
| Elsevier ESWA | Editable source files; double-anonymous title page and anonymized manuscript as separate files | Double anonymized | Up to 250 words | Encouraged: 3-5 bullets, max 85 characters each | No ESWA-specific graphical abstract requirement found in the official guide | Research data deposit/link/statement required under Elsevier Option C; data statement required |
| Elsevier CBM | No journal-final formatting needed for first submission; editable source files required | Single anonymized | Up to 250 words | Required: 3-5 bullets, max 85 characters each | Encouraged; separate file, minimum 531 x 1328 px or proportional | Research data deposit/link encouraged under Elsevier Option B; data statement encouraged |

## npj Digital Medicine

Sources: [npj submission guidelines](https://www.nature.com/npjdigitalmed/for-authors-and-referees/submission-guidelines), [npj content types](https://www.nature.com/npjdigitalmed/for-authors-and-referees/about/content-types), [npj guide to authors](https://www.nature.com/npjdigitalmed/for-authors-and-referees/guide-to-authors).

Initial submission:
- Submit through the Springer Nature online submission system. Include a cover letter with corresponding-author affiliation/contact details and a concise explanation of fit; do not repeat the abstract/introduction.
- Initial submissions do not need to meet final formatting requirements. npj encourages manuscript text and figures in a single PDF or Word file; LaTeX is accepted at acceptance stage, but before then supply compiled PDFs.
- All submissions should include a cover letter, an English manuscript file in editable format, figures, optional Supplementary Information, and relevant reporting checklists.
- Authors are encouraged to submit Nature Portfolio Reporting Summary and Editorial Policy Checklist at initial submission; these become required later if peer reviewed/accepted.

Article structure for a primary research Article:
- Title page: title up to 15 words, no punctuation/idioms/puns, full author list, affiliations, corresponding author email.
- Abstract: unstructured, no subheadings, up to 150 words.
- Introduction: no subheadings.
- Results: use subheadings.
- Discussion: no subheadings, and no separate Limitations or Conclusions section.
- Methods: use subheadings; all Methods must be in the main manuscript file, not Supplementary Information.
- Data Availability: mandatory.
- Code Availability: include where applicable.
- Acknowledgments: include funding here; do not create a separate Funding statement.
- Author Contributions: mandatory, refer to each author by initials.
- Competing Interests: mandatory, including a no-competing-interests statement when applicable.
- References: Article guidance says around 60 references, not strictly enforced; Nature numeric style.
- Figure legends: up to 350 words per figure.

Required statements and policies:
- Data Availability must state how the minimal dataset needed to interpret, replicate, and build on the work can be accessed, or why it cannot be shared.
- Code Availability is required for custom code central to the conclusions, indicating access route and restrictions.
- For human participants, human material, animal participants/material, or human data, include ethics approval details and participant consent details.
- If LLMs or AI tools were used, document use in Methods or another suitable manuscript section; AI tools cannot be authors.
- Competing interests and author contributions are required.

Figures, supplementary information, highlights, graphical abstract:
- Figure files may be included in the manuscript or uploaded separately. Multi-panel figures should be on one page and panels labeled a), b), c).
- Prepare figures at 300 dpi or higher, preferably as editable/vector files; use accessible colors and avoid red/green-only contrast and rainbow color scales.
- Supplementary Information should be one merged PDF where possible; it is not edited or typeset. Avoid tracked changes.
- No official npj Digital Medicine guidance found requiring highlights or a graphical abstract for Articles.

Do not include in manuscript prose:
- Internal filenames, CSV names, local paths, patches, logs, or repository mechanics.
- "Data not shown"; npj asks authors to make supporting data available instead.
- Supplementary Methods; all Methods belong in the main manuscript.
- A separate Conclusion or Limitations section under an Article Discussion.
- Anonymous reviewer/editor thanks or effusive acknowledgments.

## IEEE Journal of Biomedical and Health Informatics

Sources: [IEEE JBHI Information for Authors record](https://ieeexplore.ieee.org/document/11118970), [IEEE article structure](https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/create-the-text-of-your-article/structure-your-article/), [IEEE submission checklist](https://journals.ieeeauthorcenter.ieee.org/submit-your-article-for-peer-review/checklist-for-submitting-your-article-for-peer-review/), [IEEE graphics resolution and size](https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/create-graphics-for-your-article/resolution-and-size/), [IEEE graphics file formatting](https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/create-graphics-for-your-article/file-formatting/), [IEEE supplementary materials](https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/prepare-supplementary-materials/), [IEEE reproducibility guidance](https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/research-reproducibility/), [IEEE submission and peer-review policies](https://journals.ieeeauthorcenter.ieee.org/become-an-ieee-journal-author/publishing-ethics/guidelines-and-policies/submission-and-peer-review-policies/).

Initial submission:
- Use the current JBHI instructions in IEEE Xplore/Author Portal and the IEEE journal template. Confirm page limits, article type, and any JBHI-specific cover-letter requirements in the portal before submission.
- IEEE's submission checklist asks authors to review target-publication requirements, agree on the corresponding author, check that all necessary files are ready, and obtain ORCID if needed.
- Disclose related prior publications/current submissions and clearly explain how this manuscript differs from similar prior work.

Article structure:
- Use IEEE journal structure: Title, Authors, Abstract, Keywords, First Footnote, Introduction, Methodology, Equations where needed, Results, Discussion, Conclusion, References, and optional Acknowledgments.
- Abstract should be one paragraph, up to 250 words, self-contained, with no footnotes, references, abbreviations left undefined, or mathematical equations.
- Include 3-5 keywords or phrases; define abbreviations.
- First footnote should include support/funding, prior presentation details when applicable, corresponding-author details, and human/animal research statement when applicable.
- Methodology should be sufficiently detailed for reproducibility.
- Conclusion should not overstate implications.

Required statements and policies:
- Human/animal research: include IRB/ethics oversight body name, or explain why review was not conducted; for human-subject work, report consent or explain why consent was not obtained.
- AI-generated content in text, figures, images, or code must be disclosed in Acknowledgments, identifying the system, affected sections, and level of use. Grammar/editing use is generally outside the policy intent but should still be checked carefully.
- Disclose prior publication and multiple submissions. Cite and explain overlap with conference/preprint versions where applicable.
- IEEE encourages data and code sharing for reproducibility through accessible data/code repositories.

Figures, supplementary information, highlights, graphical abstract:
- Use vector graphics where possible. IEEE accepts PS, EPS, PDF, PNG, and TIFF graphics; Microsoft Office files are acceptable only if the graphic was originally drawn there.
- Non-vector graphics should be high resolution: more than 300 dpi for color/grayscale and more than 600 dpi for black-and-white line art.
- Size figures for one column (3.5 in) or two columns (7.16 in) where possible.
- Supplementary materials should be labeled as supplementary and uploaded separately; accepted formats include text, image, video, and audio formats listed by IEEE.
- IEEE has guidance for graphical abstracts. If used for JBHI, upload it at submission so it can undergo peer review; static image guidance is 660 x 295 px, at least 300 dpi. No IEEE JBHI source reviewed here requires highlights.

Do not include in manuscript prose:
- Internal filenames, CSV names, local paths, patches, logs, or repository mechanics.
- "New" or "novel" in the title just to claim novelty; IEEE advises concise, descriptive titles and says readers already understand the work should be new.
- Math symbols in title or abstract.
- Inflated references or citations that do not directly support the work.
- AI-generated material without the required acknowledgment disclosure.

## Elsevier Expert Systems with Applications

Sources: [ESWA Guide for Authors](https://www.sciencedirect.com/journal/expert-systems-with-applications/publish/guide-for-authors).

Initial submission:
- Submit through Editorial Manager. Provide editable source files for the full submission, including text, figures, tables, and text graphics; PDF alone is not an acceptable source file.
- ESWA uses double-anonymized review. Submit the title page with author details separately from an anonymized manuscript. The anonymized manuscript should contain the main body, references, and tables but no author names, affiliations, acknowledgments, or other identifying information.
- Title page should include author details, acknowledgments, competing-interest declaration if not supplied separately, and full corresponding-author address/email.

Article structure:
- Abstract: concise and factual, up to 250 words; avoid references and non-standard abbreviations.
- Keywords: 1-7 keywords.
- Main article: clearly defined and numbered sections and subsections. Do not number the abstract.
- Use editable equations and editable tables, not images of equations/tables.
- References: APA Seventh Edition style; reference list alphabetized.
- CRediT author contribution statement is encouraged, not stated as mandatory in the ESWA guide.

Required statements and policies:
- Complete the Elsevier Declaration of Competing Interest tool and upload the resulting Word document when required.
- Funding sources and sponsor role must be declared; if none, include the no-funding statement.
- Generative AI use in manuscript preparation must be declared at the end of the manuscript before references if AI tools were used beyond basic grammar/spelling/reference checks.
- Data: ESWA follows Elsevier research-data Option C. Authors are required to deposit research data in a relevant repository, cite/link it, or explain why data cannot be shared.
- Data statement: required at submission.
- Authorship is expected to be settled at original submission; post-submission changes are restricted.

Figures, highlights, graphical abstract:
- Highlights are encouraged at submission as a separate editable file named with "highlights"; use 3-5 bullets, each no more than 85 characters including spaces.
- Figures should be supplied as separate files, cited in text, numbered in order, and captioned. Preferred final artwork includes EPS/PDF for vector art; TIFF/JPG/PNG at 300 dpi for photos, 1000 dpi for line art, and 500 dpi for combination art.
- ESWA guide reviewed here lists Highlights but not a journal-specific Graphical abstract requirement.
- Elsevier policy does not permit generative AI or AI-assisted tools to create or alter submitted images or graphical abstracts, unless the use is part of the research design and described reproducibly in Methods.

Do not include in manuscript prose:
- Internal filenames, CSV names, local paths, patches, logs, or repository mechanics.
- Author-identifying acknowledgments or affiliations in the anonymized manuscript body.
- Applications to military/defense systems; ESWA says it no longer considers them.
- Superficial natural-metaphor algorithm framing or renamed existing concepts without formal, mathematically grounded contribution.
- Low-resolution figures, oversized images with unreadable text, tables as images, or vertical rules/shading in tables.

## Elsevier Computers in Biology and Medicine

Sources: [CBM Guide for Authors](https://www.sciencedirect.com/journal/computers-in-biology-and-medicine/publish/guide-for-authors).

Initial submission:
- Submit through Editorial Manager. CBM says manuscripts do not need special formatting for first submission, and manuscripts reproducing the final journal layout will be sent back.
- Provide editable source files for the full submission; PDF alone is not an acceptable source file.
- Choose the correct submission section in the online platform. For this manuscript, likely sections to evaluate are Data Analytics and Predictive Analysis in Healthcare or Biomedical and Biological Signal Processing. Avoid "Other"; CBM asks authors not to submit there.
- CBM no longer accepts multiple corresponding authors; make one corresponding author consistent between manuscript and Editorial Manager.

Article structure:
- Article types include Full Length Article, Review, Letter to the Editor, Discussion, and Tutorial.
- Abstract: concise and factual, up to 250 words; avoid references and define essential abbreviations.
- Keywords: 1-7 keywords.
- Main manuscript should be divided into clearly defined sections covering essential elements.
- Acknowledgments must be a separate section directly before the reference list, not on the title page or footnote.
- CRediT author contribution statement is required.
- References: no strict formatting requirement at submission if consistent and complete; final style is numbered references in order of appearance.

Required statements and policies:
- Ethics statement: at submission authors must confirm whether the work needs one. If needed, state legal/institutional compliance, ethics approval date/reference number, and informed consent. If not needed, state why.
- Human-subject manuscripts must include approval, compliance, privacy, and informed-consent statements where applicable.
- Clinical trials must be registered at or before enrollment; registration number should be in the manuscript, preferably at the end of the abstract.
- Funding sources and sponsor role must be declared; if none, include the no-funding statement.
- Competing interests must be disclosed through Elsevier's declaration process.
- Generative AI use in manuscript preparation must be declared before references if applicable.
- Data: CBM follows Elsevier research-data Option B. Authors are encouraged to deposit, cite, and link research data or explain why data cannot be shared.
- Data statement: encouraged at submission.

Figures, highlights, graphical abstract:
- Highlights are required at submission as a separate editable file named with "highlights"; use 3-5 bullets, each no more than 85 characters including spaces.
- Graphical abstract is encouraged at submission as a separate file. Minimum size is 531 x 1328 px (height x width) or proportional; it should be readable at 5 x 13 cm. Preferred file types are TIFF, EPS, PDF, or MS Office files.
- Figures should be supplied as separate files, cited in text, numbered in order, and captioned. Preferred final artwork includes EPS/PDF for vector art; TIFF/JPG/PNG at 300 dpi for photos, 1000 dpi for line art, and 500 dpi for combination art.
- CBM may screen images for irregularities. No feature may be enhanced, obscured, moved, removed, or introduced. Nonlinear adjustments such as gamma changes must be disclosed in the figure legend.
- Elsevier policy does not permit generative AI or AI-assisted tools to create or alter submitted images or graphical abstracts, unless the use is part of the research design and described reproducibly in Methods.

Do not include in manuscript prose:
- Internal filenames, CSV names, local paths, patches, logs, or repository mechanics.
- A manuscript layout that imitates final CBM journal formatting at first submission.
- Patient names, initials, hospital/social-security numbers, dates of birth, or other personal identifiers, even with consent.
- Unclear train/validation/test splits, imprecise downstream-task analysis, minor architecture modifications with only slight metric gains, or claims without comparison to real state-of-the-art methods.
- Low-resolution figures, oversized images with unreadable text, tables as images, or vertical rules/shading in tables.

## Submission Prose Placement Rules

- Main text: scientific narrative, methods, results, limitations, and interpretation only.
- Methods: model architecture, training/evaluation protocol, dataset construction, statistical analysis, ethics/consent details where required, and reproducible methodological details. Mention software names or packages only when scientifically relevant.
- Data Availability: dataset access, restrictions, repository identifiers, third-party data permissions, and why any data cannot be shared.
- Code Availability: public repository/archival DOI or access restrictions. Describe what code enables at a high level; do not list local filenames.
- Supplementary Information/Methods: expanded tables, ablation details, extra methods, checklists, or robustness analyses only where the venue permits them. npj Articles do not permit Supplementary Methods; all Methods should be in the main manuscript.
- Cover letter: journal fit, confidential conflicts, related manuscripts, suggested/excluded reviewers, and administrative notes. Do not use manuscript prose for submission logistics.
