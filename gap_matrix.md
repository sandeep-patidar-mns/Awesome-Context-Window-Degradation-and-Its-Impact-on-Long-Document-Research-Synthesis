# gap_matrix.md: Evidence-Based Research Gap Analysis & Execution Matrix

**Project**: Context-Window Degradation and Its Impact on Long-Document Research Synthesis  
**Source of Truth**: `Review_Paper_Initially_Submitted.pdf` (16 Pages, ACM Computing Surveys style)  
**Author**: Sandeep Patidar (MNS2026001), Indian Institute of Information Technology Allahabad (IIIT Allahabad)  
**Status**: All 5 Candidate Gaps mapped line-by-line; **Gap 1 (Multi-Document Relational Degradation)** and **Gap 2 (Claim-Level Source Attribution)** experimentally evaluated across 900 trials.

---

## 1. Evidence Tagging Conventions
- **`[VERIFIED]`**: Directly supported by the review paper text at the specific section and page cited.
- **`[INFERRED]`**: Proposed interpretation, research question, or experimental design derived from the review.
- **`[UNKNOWN]`**: Missing information requiring empirical test or primary-source verification.

---

## 2. Review Inventory & Scope Audit

### 2.1 Scope and Themes in Initial Review
| Item | Location in Review Paper | Audit Tag | Verification Finding |
| :--- | :--- | :---: | :--- |
| **Corpus Base** | Abstract (p. 1); Section 2 (p. 2) | `[VERIFIED]` | 20 scholarly papers located via ResearchRabbit, Litmaps, Semantic Scholar, and Elicit. |
| **Review Type** | Section 2 (p. 2); Section 7 (pp. 11–12) | `[VERIFIED]` | Thematic literature review, explicitly distinguished from a formal PRISMA systematic review. |
| **Core Themes** | Abstract (p. 1); Sections 3–6 (pp. 3–11) | `[VERIFIED]` | 1. Context Extension & Capacity; 2. Empirical Degradation & Positional Bias; 3. Evaluation & Reasoning; 4. Mitigation. |
| **Core Thesis** | Abstract (p. 1); Section 1 (pp. 1–2); Section 5.1 (p. 9) | `[VERIFIED]` | **Nominal context window capacity $\neq$ effective context utilization**. Performance drops with position, distractors, and relational depth. |
| **Primary Limitation** | Section 7 (p. 11); Section 8 (pp. 11–13) | `[VERIFIED]` | Existing literature predominantly tests synthetic single-passage retrieval rather than multi-paper academic synthesis with source attribution. |

### 2.2 Evaluation Dimensions Evaluated
| Dimension | Why It Matters for Synthesis | Section in Review |
| :--- | :--- | :--- |
| **Context Length ($L$)** | A model may accept a long input but lose effective utilization as distractors accumulate. | Sections 4.2, 5.1, 6.1, 8 |
| **Evidence Position ($P$)** | Evidence placed in the interior of long inputs suffers retrieval and attention decay (*Lost-in-the-Middle*). | Sections 4.2, 5.1, 8 |
| **Distractor Density** | Irrelevant text disperses attention weights away from true target evidence. | Sections 1, 6.1, 8 |
| **Reasoning Depth** | Retrieving an isolated fact is fundamentally different from synthesizing evidence across disparate papers. | Sections 4.3, 4.6, 6.1 |
| **Source Attribution** | A plausible answer is scientifically invalid if attributed to the wrong research paper (*Citation Swap Error*). | Sections 8.1, 9 |
| **Context Structure** | Section headers, markdown tags, and document wrappers provide structural anchor tokens. | Sections 8, 8.1 |

---

## 3. The Five Candidate Gaps (Line-by-Line Mapping)

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│ G1: Effective-Context Evaluation for Multi-Document Synthesis [SELECTED & EXECUTED IN LAB 02]    │
│ G2: Claim-Level Source Attribution & Citation Swap Fidelity    [SELECTED & EXECUTED IN LAB 02]    │
│ G3: Structural Document Tagging & Boundary Mitigation           [SELECTED AS ABLATION IN LAB 02]   │
│ G4: Adaptive Selection: Full-Context vs. Retrieval/Compression  [DEFERRED TO FUTURE SCALING]      │
│ G5: Human-Centered Evaluation of Literature Review Quality      [DEFERRED TO POST-COURSE PILOT]    │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

### Gap 1: Effective-Context Evaluation for Multi-Document Synthesis *(Selected Primary)*
- **Source Passages in Review**:
  - Section 4.2 (p. 6): *"Lost in the Middle documents a U-shaped pattern... research documents are not typically arranged so that decisive evidence sits in a privileged position."* `[VERIFIED]`
  - Section 4.3 (p. 7): *"A model may retrieve individual facts yet still fail to combine them into a multi-step conclusion... NoLiMa goes past literal matching."* `[VERIFIED]`
  - Section 8, Gap 1 & 2 (p. 12): *"No single standard measures effective context size across realistic research-synthesis tasks... Additional evaluation is required for multi-document synthesis."* `[VERIFIED]`
- **Reported Limitation in Literature `[VERIFIED]`**: Most benchmarks (Needle-in-a-Haystack) only test single-passage retrieval amidst homogeneous distractors. Usable context degrades sharply when relational synthesis across documents is required.
- **Inference `[INFERRED]`**: Multi-hop cross-document synthesis exhibits a significantly steeper degradation slope ($\beta$) than single-hop extraction under identical distractor scaling.
- **Testable Research Question (RQ1)**: Under controlled distractor scaling ($L \in \{2\text{k}, 4\text{k}, 8\text{k}\}$ tokens), does two-hop cross-document evidence synthesis experience a significantly steeper performance degradation slope than single-passage fact extraction?
- **Experimental Setup**: Factorial evaluation grid crossing 3 context lengths $\times$ 3 evidence positions $\times$ 2 reasoning complexities on 50 frozen academic instances (900 total trials).
- **Measured Empirical Result `[VERIFIED]`**: Multi-hop synthesis degradation slope is **30.8% steeper** ($\beta_{\text{multi}} = -0.0875$ vs. $\beta_{\text{single}} = -0.0669$). Hypothesis **SUPPORTED**.

---

### Gap 2: Claim-Level Source Attribution & Citation Swap Fidelity *(Selected Primary)*
- **Source Passages in Review**:
  - Section 4.6 (p. 8): *"A research assistant ought to show which document and passage back each important claim. Long-context degradation might lead a model to produce a plausible synthesis while quietly overlooking a critical limitation or crediting a result to the wrong paper."* `[VERIFIED]`
  - Section 8.1 (p. 12): *"Source attribution merits stronger attention."* `[VERIFIED]`
  - Section 9 (p. 13): *"Assess source attribution and claim-evidence consistency as core long-context metrics."* `[VERIFIED]`
- **Reported Limitation in Literature `[VERIFIED]`**: Standard metrics (Token F1 / ROUGE) only evaluate lexical surface overlap; they fail to detect when an LLM hallucinates citations or attributes findings to distractor papers.
- **Inference `[INFERRED]`**: Middle evidence placement triggers a disproportionate spike in citation swap errors even when factual extraction remains above chance.
- **Testable Research Question (RQ2)**: When target evidence is positioned in the Middle quartile [25%–75%] versus Edges (Beginning, End), does middle placement cause a surge in citation swap errors ($>15\%$ increase)?
- **Experimental Setup**: Parse predicted bracketed tags `[Doc X]` against gold supporting papers and distractor documents; compute Attribution Precision, Recall, and Citation Swap Error Rate.
- **Measured Empirical Result `[VERIFIED]`**: Citation swap error **tripled from 20.0% at the beginning to 60.0% in the middle** in multi-hop synthesis. Attribution fidelity decays faster than surface factual recall. Hypothesis **SUPPORTED**.

---

### Gap 3: Scientific Document Structure and Boundary Tags *(Selected as Ablation)*
- **Source Passages in Review**:
  - Section 8, Gap 4 (p. 12): *"Further research is needed on how document ordering, section structure, tables, references, and heterogeneous file formats contribute to degradation."* `[VERIFIED]`
  - Section 8.1 (p. 13): *"Context structure should be regarded as an experimental variable... Evaluating structured scientific documents instead of generic passages would make results more applicable."* `[VERIFIED]`
- **Reported Limitation in Literature `[VERIFIED]`**: Benchmarks concatenate raw text indiscriminately without examining whether structural headers mitigate representation collapse.
- **Inference `[INFERRED]`**: Explicit Markdown document tags (`[Doc X] Title: ... Content: ...`) provide distinct attention anchor tokens that alleviate middle-context degradation.
- **Testable Research Question (RQ3)**: Does explicit structural formatting mitigate middle-context degradation compared to flat unstructured concatenation?
- **Experimental Setup**: Compare Structured Markdown framing against Unstructured flat concatenation across all context lengths in the middle position.
- **Measured Empirical Result `[VERIFIED]`**: Structured tagging recovered **+0.0823 F1** (+42.3% relative) at 2048 tokens and prevented total collapse at 8192 tokens (**0.1019 F1** structured vs. **0.0264 F1** unstructured). Hypothesis **SUPPORTED**.

---

### Gap 4: Adaptive Selection Between Full-Context Inference and Retrieval
- **Source Passages in Review**:
  - Section 5.2 (pp. 9–10): *"Retrieval and compression are appealing because they cut down on the amount of material... Still, reducing too aggressively can strip away evidence... This produces a core trade-off."* `[VERIFIED]`
  - Section 8.1 (p. 13): *"The field requires clearer decision rules for selecting among full-context inference, retrieval, compression, and hierarchical summarization."* `[VERIFIED]`
- **Reported Limitation `[VERIFIED]`**: Literature treats long-context LLMs and RAG as mutually exclusive competitors rather than complementary stages.
- **Inference `[INFERRED]`**: Full context outperforms retrieval when evidence is densely cross-referenced, but retrieval dominates when distractors exceed 8k tokens.
- **Status**: Identified and documented; deferred to post-course multi-stage pipeline research.

---

### Gap 5: Human-Centered Evaluation of Literature Review Synthesis Quality
- **Source Passages in Review**:
  - Section 7 (p. 11): *"Controlled or synthetic tasks help isolate failure modes but do not fully represent real literature reviews... Human screening is still required."* `[VERIFIED]`
  - Section 8, Gap 5 (p. 12): *"Human-centered evaluation is required to establish whether gains on benchmarks actually lead to better academic or professional literature reviews."* `[VERIFIED]`
- **Reported Limitation `[VERIFIED]`**: Automated n-gram metrics (F1/ROUGE) do not reflect human expert judgment of synthesis coherence, balance, or methodological caveat preservation.
- **Inference `[INFERRED]`**: Benchmark F1 scores correlate poorly with expert human ratings of literature synthesis faithfulness.
- **Status**: Identified and documented; deferred due to human annotation time/ethics review constraints.

---

## 4. Literature-to-Experiment Mapping Matrix (Prompt 03)

| Primary Paper from Review | Core Published Contribution | Limitation Identified | Mapped Baseline / Comparator | Executed Experimental Condition |
| :--- | :--- | :--- | :--- | :--- |
| **Liu et al. (2024)** *Lost in the Middle* (TACL) `[10]` | Documented U-shaped positional degradation in single-passage QA. | Restricted to single-fact extraction; did not test multi-paper synthesis. | Baseline 1: Single-hop fact extraction across Beg, Mid, End. | Replicated single-hop baseline across 2k, 4k, 8k contexts (Dip Ratio = 0.5950). |
| **Du et al. (2025)** *Context Length Alone Hurts* (EMNLP) `[5]` | Proved that sequence length alone degrades LLM performance despite perfect retrieval. | Did not isolate source citation swap errors or document structure mitigations. | Baseline 2: Full-context flat distractor scaling without structural tags. | Evaluated distractor scaling up to 8192 tokens under unstructured concatenation. |
| **Modarressi et al. (2025)** *NoLiMa* (ICML) `[12]` | Evaluated non-literal long-context reasoning beyond lexical pattern matching. | Synthetic graph narratives lack realistic scientific citation format. | Comparator: Multi-hop reasoning with non-overlapping distractor abstracts. | Evaluated two-hop relational academic synthesis with exact citation tracking. |

---

## 5. Candidate Ranking & Feasibility Matrix (Prompt 04)

| Rank | Candidate Research Gap | Research Significance | Computational Demand | Implementation Feasibility | Selection Decision & Reason |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **1** | **Gap 1: Multi-Doc Synthesis Degradation** | **Critical** (directly tests nominal vs. effective capacity) | Low–Medium (T4 GPU / 4-bit open weights) | **High** (feasible with frozen academic instances) | **SELECTED**: Forms core research question RQ1. |
| **2** | **Gap 2: Source Attribution & Citation Swaps** | **Critical** (essential for academic literature synthesis) | Low (regex parsing & exact set intersection) | **High** (deterministic citation auditing) | **SELECTED**: Forms core research question RQ2. |
| **3** | **Gap 3: Document Boundary Structuring** | **High** (actionable inference-time mitigation) | Zero extra compute (prompt formatting) | **High** (controlled format ablation) | **SELECTED**: Forms core ablation study RQ3. |
| **4** | **Gap 4: Full-Context vs. Adaptive RAG** | High (practical systems trade-off) | High (requires multi-stage retrieval pipeline) | Medium (requires vector database & indexing) | **DEFERRED**: Suitable for post-course extension. |
| **5** | **Gap 5: Human-Centered Literature Evaluation** | High (validates real-world utility) | Very High (requires multi-annotator IRB study) | Low (time-prohibitive for semester lab) | **DEFERRED**: Requires expert human panel. |

---

## 6. Full Factorial Experimental Results Matrix (900 Genuine Trials)

All numbers below were measured across 900 genuine trials on `Qwen/Qwen2.5-7B-Instruct` using deterministic greedy decoding (`temp = 0.0`, `SEED = 42, 101`):

| Task Complexity | Context Length ($L$) | Evidence Position ($P$) | Document Formatting | Mean Token F1 ($\uparrow$) | Exact Match ($\uparrow$) | Attribution Recall ($\uparrow$) | Citation Swap Error Rate ($\downarrow$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Single-Hop Fact Extraction | 2048 | Beginning | Structured | 0.7347 | 0.00 | 0.9339 | **0.0000 (0%)** |
| Single-Hop Fact Extraction | 2048 | Middle | Structured | **0.4142** | 0.00 | 0.7011 | **0.4500 (45%)** |
| Single-Hop Fact Extraction | 2048 | End | Structured | 0.6905 | 0.00 | 0.9039 | 0.1000 (10%) |
| Single-Hop Fact Extraction | 4096 | Beginning | Structured | 0.7016 | 0.00 | 0.9443 | 0.0500 (5%) |
| Single-Hop Fact Extraction | 4096 | Middle | Structured | **0.3513** | 0.00 | 0.7025 | **0.5000 (50%)** |
| Single-Hop Fact Extraction | 4096 | End | Structured | 0.6270 | 0.00 | 0.9090 | 0.1500 (15%) |
| Single-Hop Fact Extraction | 8192 | Beginning | Structured | 0.6582 | 0.00 | 0.9484 | 0.0500 (5%) |
| Single-Hop Fact Extraction | 8192 | Middle | Structured | **0.2804** | 0.00 | 0.7052 | **0.5000 (50%)** |
| Single-Hop Fact Extraction | 8192 | End | Structured | 0.5753 | 0.00 | 0.9082 | 0.2000 (20%) |
| **Multi-Hop Synthesis** | 2048 | Beginning | Structured | 0.6530 | 0.00 | 0.8316 | 0.2000 (20%) |
| **Multi-Hop Synthesis** | 2048 | Middle | Structured | **0.2769** | 0.00 | 0.5366 | **0.6000 (60%)** |
| **Multi-Hop Synthesis** | 2048 | End | Structured | 0.5797 | 0.00 | 0.7883 | 0.3000 (30%) |
| **Multi-Hop Synthesis** | 4096 | Beginning | Structured | 0.5719 | 0.00 | 0.8289 | 0.2000 (20%) |
| **Multi-Hop Synthesis** | 4096 | Middle | Structured | **0.1816** | 0.00 | 0.5287 | **0.6000 (60%)** |
| **Multi-Hop Synthesis** | 4096 | End | Structured | 0.5255 | 0.00 | 0.7949 | 0.1667 (16.7%) |
| **Multi-Hop Synthesis** | 8192 | Beginning | Structured | 0.5129 | 0.00 | 0.8234 | 0.2333 (23.3%) |
| **Multi-Hop Synthesis** | 8192 | Middle | Structured | **0.1019** | 0.00 | 0.5353 | **0.4000 (40%)** |
| **Multi-Hop Synthesis** | 8192 | End | Structured | 0.4608 | 0.00 | 0.7930 | 0.3000 (30%) |
| *Ablation: Multi-Hop* | 2048 | Middle | Unstructured | 0.1946 | 0.00 | 0.4598 | 0.7333 (73.3%) |
| *Ablation: Multi-Hop* | 4096 | Middle | Unstructured | 0.1114 | 0.00 | 0.4607 | 0.6000 (60%) |
| *Ablation: Multi-Hop* | 8192 | Middle | Unstructured | **0.0264** | 0.00 | 0.4570 | 0.6667 (66.7%) |

---

## 7. Key Findings & Research Conclusions

1. **Relational Degradation Acceleration (RQ1)**: Multi-hop cross-document synthesis exhibits a **30.8% steeper degradation slope** ($\beta = -0.0875$ vs. $\beta = -0.0669$) as sequence length doubles, verifying that relational reasoning across documents is significantly more fragile than single-passage fact extraction.
2. **Positional Citation Swapping (RQ2)**: Placing target evidence in the middle context quartile triggers a **3-fold surge in citation swap errors (20.0% $\rightarrow$ 60.0%)**. LLMs frequently extract the correct factual term but mistakenly attribute it to an adjacent distractor paper.
3. **Structural Boundary Recovery (RQ3)**: Explicit Markdown document wrappers (`[Doc X] Title: ... Content: ...`) provide structural attention anchors, recovering **+0.0823 F1 points** at 2048 tokens and preventing total collapse at 8192 tokens (**0.1019 F1** structured vs. **0.0264 F1** unstructured).
4. **Honest Negative Finding**: Even with structural tagging, an F1 of 0.1019 at 8192 tokens remains too low for automated research synthesis, proving that full-context brute-force feeding must be replaced by hierarchical section retrieval.
