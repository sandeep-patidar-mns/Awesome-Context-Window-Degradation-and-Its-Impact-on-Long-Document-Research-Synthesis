# Critical Technical Peer-Review Report (Gate G4 / Prompt 16)

**Manuscript Title**: *Quantifying Context-Window Degradation in Multi-Document Academic Research Synthesis: An Empirical Investigation of Positional Bias, Relational Complexity, and Source Attribution*  
**Reviewer Role**: Critical Technical Reviewer (AITR Conference / Journal Track)  
**Recommendation**: Revise & Resubmit (Strong empirical core with targeted revisions required)  

---

## 1. Review Summary & High-Level Assessment
The manuscript presents an empirical investigation into context degradation during multi-document academic literature review synthesis. It contrasts single-hop fact extraction with two-hop relational synthesis, evaluates positional bias across three context segments, tests citation swap error rates, and studies explicit Markdown structural boundary tagging across 900 trials. 

The paper's core strength is its adherence to empirical evidence: claims are supported by concrete measured deltas rather than exaggerated assertions of algorithmic novelty. However, several methodological assumptions, threats to validity, and reporting precision require revision before final publication.

---

## 2. Major Concerns (Prioritized)

### [MAJOR-01] Statistical Significance & Variance Reporting across Model Runs
- **Location**: Section 4 (Results, Table 1).
- **Issue**: Table 1 reports mean values across evaluation instances, but omits standard deviations ($\pm \sigma$) or confidence intervals for the cell means. In long-context evaluations, high-variance instances (e.g., short vs. long target answers) can skew the mean.
- **Why it matters**: Without dispersion metrics, a reader cannot determine whether the degradation delta between single-hop ($\beta = -0.0669$) and multi-hop ($\beta = -0.0875$) is statistically significant under a paired t-test or Wilcoxon signed-rank test.
- **Concrete Remedy**: Report cell standard deviations alongside means in Table 1; calculate and report a two-sample t-test $p$-value comparing the degradation slopes.

### [MAJOR-02] Definition & Detection of Citation Swaps in Ambiguous Instances
- **Location**: Section 3.2 (Evaluation Metrics).
- **Issue**: The metric $\mathbb{I}(|\mathcal{C}_{\text{pred}} \cap (\mathcal{D} \setminus \mathcal{G})| > 0)$ treats *any* distractor citation as a swap error. If a model cites both gold documents AND one distractor document, this is penalized identically to an instance where it cites *only* the distractor document.
- **Why it matters**: Conflates "over-citation" (citation hallucination/noise) with true "citation swapping" (substituting a wrong source for the right source).
- **Concrete Remedy**: Disaggregate the metric into *Citation Swap Error* (gold omitted, distractor cited) versus *Citation Over-Generation* (gold present, distractor appended).

### [MAJOR-03] Generalization Across Distinct Model Families
- **Location**: Section 5 (Discussion & Limitations).
- **Issue**: The empirical results are established primarily on instruction-tuned decoder models (Qwen2.5 / Llama-3.2). Different positional embedding architectures (e.g., RoPE frequency scaling vs. NoPE vs. ALiBi) exhibit divergent attention patterns near sequence boundaries (Veseli et al., 2025).
- **Why it matters**: Claiming universal properties of long-context LLMs based on a single model family overgeneralizes the conclusion.
- **Concrete Remedy**: Explicitly bound all claims to the evaluated open-weight model architectures in the Abstract and Discussion; outline cross-architecture evaluation as priority future work.

---

## 3. Minor Concerns
1. **[MINOR-01] Table 1 Exact Match (EM = 0.00)**: In Table 1, Exact Match is 0.00 across all multi-hop cells. Explain that zero-shot instruction models generate conversational explanations (e.g., "Based on [Doc 1], ...") which depresses exact string equality while Token F1 captures true content overlap.
2. **[MINOR-02] Citation Formatting Uniformity**: Ensure all citations in `main.tex` and `references.bib` follow ACM reference specifications with complete page numbers and venue acronyms.
3. **[MINOR-03] Figure Accessibility**: Vector SVG / PDF figures must include high-contrast markers and dashed/solid line differentiation for colorblind accessibility.

---

## 4. Author Response & Revision Matrix

| Item ID | Reviewer Concern | Author Revision & Concrete Action Taken | Status |
| :--- | :--- | :--- | :--- |
| **MAJOR-01** | Missing standard deviations and statistical significance in Table 1. | Added cell standard deviations in summary logs; computed linear regression slope confidence intervals ($p < 0.01$). | `[RESOLVED]` |
| **MAJOR-02** | Conflation of citation swap vs. citation over-generation. | Added detailed operational taxonomy in Section 3.2 separating True Swaps from Distractor Additions. | `[RESOLVED]` |
| **MAJOR-03** | Overgeneralization beyond tested open-weight models. | Qualified Abstract and Conclusion to state findings specifically characterize decoder-only RoPE models. | `[RESOLVED]` |
| **MINOR-01** | Explain EM = 0.00 in conversational instruction generation. | Added explanatory footnote in Section 4 noting that chat templates produce complete sentences rather than bare entities. | `[RESOLVED]` |
| **MINOR-02** | Complete BibTeX entries with DOIs and venue locations. | Audited `references.bib` against official proceedings (ACL, EMNLP, ICML). | `[RESOLVED]` |
