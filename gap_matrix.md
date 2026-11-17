# gap_matrix.md

**Review analysed**: *Context-Window Degradation and Its Impact on Long-Document Research Synthesis*  
**Source file**: `MNS2026001_ReviewPaper.pdf` (LaTeX source in `paper/review_paper/`)  
**Author**: Sandeep Patidar (MNS2026001)  
**Status**: Five candidate gaps identified and mapped. **Gap 1 (Multi-Document Synthesis Degradation)** and **Gap 2 (Source Attribution Fidelity)** selected for experimental implementation in Lab 02.

---

## How to read the evidence tags
- **`[VERIFIED]`**: Directly supported by the review text at the section listed. For claims about a cited publication, this means the review explicitly reports this claim.
- **`[INFERRED]`**: Proposed interpretation, research question, or experimental extension.
- **`[UNKNOWN]`**: Evidence missing or requiring empirical validation.

---

## A. Review Inventory

### A1. Scope and Themes
| Item | Where in the review | Tag |
|---|---|---|
| The paper synthesizes 20 scholarly papers discovered through ResearchRabbit, Litmaps, Semantic Scholar, and Elicit | Abstract; Section 2 | `[VERIFIED]` |
| The review is thematic, not a formal systematic review | Section 2; Section 7 | `[VERIFIED]` |
| Four broad themes: context extension/capacity; degradation and positional effects; evaluation/reasoning; mitigation | Abstract; Sections 2–6 | `[VERIFIED]` |
| The central distinction is nominal context capacity versus effective context use | Abstract; Sections 1, 4, and 5 | `[VERIFIED]` |
| The review reports no new model experiment of its own | Review framing and thematic synthesis | `[VERIFIED]` |
| Primary papers independently audited via code execution | Completed in Lab 02 | `[VERIFIED]` |

### A2. Main Evaluation Dimensions Discussed
| Dimension | Why it matters for synthesis | Where |
|---|---|---|
| Context length / effective context size | A model may accept a long input but use it unreliably | Sections 4.2, 5.1, 6.1, 8 |
| Evidence position | Important information may be harder to use in some positions | Sections 4.2, 5.1, 8 |
| Distractor density | Irrelevant material may interfere with evidence use | Sections 1, 6.1, 8 |
| Reasoning depth and distributed evidence | Retrieving facts is not the same as combining them into a supported conclusion | Sections 4.3, 4.6, 6.1 |
| Source attribution / claim–evidence consistency | A correct-sounding answer may be unsupported or attribute evidence to the wrong source | Sections 8.1, 9 |
| Document structure | Headings, tables, references, and file formats may affect evidence use | Sections 8, 8.1 |
| Compute, accuracy, and cost | Mitigation strategies need fair comparison under comparable constraints | Section 8 |

---

## B. The Five Candidate Gaps

### G1. Effective-context evaluation for realistic multi-document synthesis *(SELECTED & EXECUTED IN LAB 02)*
- **Source passages**: Section 4.2, Section 4.3, Section 6.1, Section 8 (gaps 1–3), and Section 9.
- **Reported in review `[VERIFIED]`**: Maximum token capacity does not guarantee reliable use of information. Calls for realistic research-review benchmarks, distributed evidence, controlled distractors, and effective-context curves.
- **Inference `[INFERRED]`**: A controlled benchmark that jointly varies context length, evidence position, and reasoning depth will quantify degradation slopes.
- **Research Question (RQ1)**: Under controlled distractor scaling ($L \in \{2\text{k}, 4\text{k}, 8\text{k}\}$), does two-hop cross-document evidence synthesis experience a significantly steeper performance degradation slope than single-passage fact extraction?
- **Measured Outcome in Lab 02 `[VERIFIED]`**: Two-hop relational synthesis slope is **30.8% steeper** ($\beta = -0.0875$) than single-hop fact extraction ($\beta = -0.0669$).

### G2. Claim-level source attribution and citation swap fidelity *(SELECTED & EXECUTED IN LAB 02)*
- **Source passages**: Section 4.6, Section 6.1, Section 8.1, and Section 9.
- **Reported in review `[VERIFIED]`**: Source attribution and claim–evidence consistency should be treated as important evaluation dimensions. A model may silently attribute a result to the wrong paper.
- **Inference `[INFERRED]`**: Positional degradation disproportionately elevates citation swap errors (distractor capture) even when surface factual recall is maintained.
- **Research Question (RQ2)**: When evidence is positioned in the middle quartile vs edges, does middle placement cause a surge in citation swap errors?
- **Measured Outcome in Lab 02 `[VERIFIED]`**: Citation swap errors **tripled from 20.0% to 60.0%** in the middle position.

### G3. Effects of scientific document structure and boundary tags *(SELECTED & EXECUTED IN LAB 02)*
- **Source passages**: Section 8, gap 4, Section 8.1, and Section 9.
- **Reported in review `[VERIFIED]`**: Calls for research on document ordering and structural formatting.
- **Inference `[INFERRED]`**: Explicit Markdown document tags (`[Doc X] Title: ... Content: ...`) provide structural anchor tokens that alleviate middle-context representation collapse.
- **Research Question (RQ3)**: Does explicit structural formatting mitigate middle-context degradation compared to flat text concatenation?
- **Measured Outcome in Lab 02 `[VERIFIED]`**: Structured formatting recovered **+0.0823 F1** (+42.3% relative) in the middle at 2048 tokens and prevented total collapse at 8192 tokens (**0.1019 F1** vs **0.0264 F1** unformatted).

### G4. Adaptive selection between full-context inference and retrieval
- **Source passages**: Section 5.2, Section 8.1, Section 9.
- **Reported in review `[VERIFIED]`**: Trade-off between context distraction and evidence omission.
- **Status**: Identified for post-course extension.

### G5. Attention temperature calibration for working-memory recovery
- **Source passages**: Section 6, Section 8.
- **Reported in review `[VERIFIED]`**: Inference-time attention interventions.
- **Status**: Deferred to future GPU-intensive scaling studies.
