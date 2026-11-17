# Gate G1: Research Brief & Problem Formulation

**Project**: Context-Window Degradation in Multi-Document Academic Research Synthesis  
**Author**: MNS2026001  
**Course**: AI Tools for Research (AITR) — Lab 02  
**Approved Pathway**: Pathway B (Controlled Comparative Study) + Pathway C (Structural Ablation)  
**Status**: Gate G1 Approved & Frozen  

---

## 1. Project Information & Review Grounding
| Field | Verified Project Information |
| :--- | :--- |
| **Review Topic** | Context-Window Degradation and Its Impact on Long-Document Research Synthesis `[VERIFIED: main.tex L20]` |
| **Key Verified Papers** | 1. Liu et al. (2024) *Lost in the Middle: How Language Models Use Long Contexts* (TACL) `[VERIFIED]`<br>2. Du et al. (2025) *Context Length Alone Hurts LLM Performance Despite Perfect Retrieval* (EMNLP Findings) `[VERIFIED]`<br>3. Modarressi et al. (2025) *NoLiMa: Long-Context Evaluation Beyond Literal Matching* (ICML) `[VERIFIED]`<br>4. Veseli et al. (2025) *Positional Biases Shift as Inputs Approach Context Window Limits* `[VERIFIED]`<br>5. Bai et al. (2024) *LongBench: A Bilingual, Multitask Benchmark* (ACL) `[VERIFIED]` |
| **Research Gap** | Existing literature establishes context length degradation and positional bias for single-passage retrieval, but fails to test multi-document academic synthesis where evidence must be bridged across papers and accurately attributed without citation hallucination. `[VERIFIED: main.tex L167–186]` |

---

## 2. Precise Research Problem
Large language models advertise extensive context windows (32k–128k+ tokens), yet empirical studies confirm that nominal capacity does not equal effective information utilization. In academic literature review workflows, evidence is rarely concentrated in a single passage; it is distributed across separate papers and requires joint synthesis and faithful source attribution. It remains unresolved whether multi-hop cross-document synthesis degrades more steeply than single-passage retrieval under identical distractor scaling, and whether positional degradation triggers silent source misattribution (attributing facts to the wrong paper) even when factual content is preserved.

---

## 3. Formal Research Questions & Success Criteria

### RQ1: Relational Synthesis vs. Single-Hop Degradation Under Distractor Scaling
- **Question**: Under controlled context scaling ($L \in \{2\text{k}, 4\text{k}, 8\text{k}, 16\text{k}\}$ tokens), does two-hop cross-document evidence synthesis experience a significantly steeper performance degradation slope than single-passage fact extraction?
- **Independent Variables**: Context length $L$ (tokens); Reasoning Depth (Single-hop vs. Two-hop synthesis).
- **Dependent Variables**: Token F1 score; Exact Match (EM).
- **Hypothesis**: Two-hop synthesis exhibits a steeper negative slope ($\frac{\partial \text{F1}_{2\text{-hop}}}{\partial L} < \frac{\partial \text{F1}_{1\text{-hop}}}{\partial L}$) due to attention weight dispersion across distractor tokens.
- **Falsification / Contradiction**: If the degradation slopes are statistically indistinguishable, confirming that degradation is purely a sequence-length artifact independent of relational reasoning complexity.

### RQ2: Positional Degradation and Source Attribution Fidelity
- **Question**: When gold evidence is situated in the Middle quartile [25%–75%] versus the Edges (Beginning [0–25%], End [75–100%]), does middle placement cause a disproportionate surge in citation misattribution errors compared to factual answer loss?
- **Independent Variable**: Relative evidence depth $D \in \{\text{Beginning}, \text{Middle}, \text{End}\}$.
- **Dependent Variables**: Source Attribution Precision, Citation Swap Error Rate, Factual Token F1.
- **Hypothesis**: Middle-positioned evidence suffers higher citation confusion ($>15\%$ increase in citation swaps) even when factual extraction remains above chance.
- **Falsification / Contradiction**: If citation attribution accuracy perfectly tracks factual extraction across all positions without selective attribution degradation.

### RQ3: Structural Boundary Mitigation (Ablation)
- **Question**: Does explicit structural formatting (Markdown document wrappers and section headers) mitigate middle-context degradation compared to flat text concatenation?
- **Independent Variable**: Structural Framing (Raw Text Concatenation vs. Explicit Markdown/XML Document Tags).
- **Dependent Variable**: $\Delta \text{F1}_{\text{middle}}$ recovery score.

---

## 4. Experimental Setup & Feasibility Boundaries
- **Primary Benchmark**: Multi-document scientific synthesis corpus built from HotpotQA multi-hop pairs and open-access scientific abstract collections.
- **Comparators / Baselines**:
  - Baseline 1: Standard single-needle extraction (reproducing Liu et al., 2024).
  - Baseline 2: Full-context flat concatenation (reproducing Du et al., 2025).
  - Proposed Condition: Multi-hop synthesis with explicit source attribution and structural formatting.
- **Hardware Profile**: Google Colab T4 GPU (15GB) / L4 GPU or Local CPU fallback with 4-bit NF4 quantized open weights (`Qwen2.5-7B-Instruct` or `Llama-3.2-3B-Instruct`).
- **First Executable Milestone**: Implement deterministic dataset packer and run an environment/data sanity check pipeline producing verified token counts and input/output schema.
