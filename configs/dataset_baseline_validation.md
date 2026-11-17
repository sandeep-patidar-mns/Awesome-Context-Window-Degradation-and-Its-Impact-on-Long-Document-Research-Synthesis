# Dataset and Baseline Validation Sheet (Gate G2 / Prompt 06)

**Project**: Context-Window Degradation in Multi-Document Academic Research Synthesis  
**Task Domain**: Long-Context NLP / Multi-Document Synthesis & Fact Attribution  
**Status**: Verified & Frozen  

---

## 1. Candidate Datasets Analysis

| Candidate Dataset | Official Source & Access | Schema & Format | Benchmark Protocol & Metric | Compute & Storage | Risks & Pitfalls |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **HotpotQA (Distractor Multi-Hop Setting)** *(Selected Primary)* | `https://hotpotqa.github.io/` / Hugging Face `datasets.load_dataset('hotpot_qa', 'distractor')` (CC BY-SA 4.0) `[VERIFIED]` | JSON: `_id`, `question`, `answer`, `supporting_facts`, `context` (title + text sentences) | Given question + context with 2 gold documents + distractor documents, generate exact answer + cite supporting documents. Metrics: Token F1, Exact Match (EM), Supporting Fact F1. | < 50 MB raw data; inference only. | Model pre-training memorization of popular Wikipedia entities. Mitigated by testing relational reasoning and strict source attribution. |
| **LongBench (MultiDoc QA / 2WikiMultihopQA subset)** *(Comparator)* | `https://github.com/THUDM/LongBench` (MIT License) `[VERIFIED]` | JSONL: `input`, `context`, `answers`, `length`, `dataset` | Multi-document QA across long context windows (4k–16k). Metric: Substring F1, Rouge-L. | ~100 MB; inference only. | Some context lengths exceed consumer GPU memory unless chunked or quantized. |
| **NoLiMa (Non-Literal Matching)** *(Reference)* | `https://proceedings.mlr.press/v267/modarressi25a.html` `[VERIFIED]` | Synthetic graph-relational text | Non-literal information extraction | Low storage; requires synthetic generation scripts. | Synthetic narratives lack realistic scientific prose and citation structure. |

---

## 2. Baselines and Controls

### Baseline 1: Single-Needle Extraction (Liu et al., 2024 Replication)
- **Protocol**: Target gold passage containing the answer is placed at relative positions $p \in \{0.1, 0.5, 0.9\}$ (Beginning, Middle, End) amidst distractor text.
- **Purpose**: Establishes the standard "Lost-in-the-Middle" reference curve on the target model under identical prompt templates.

### Baseline 2: Flat Full-Context Scaling (Du et al., 2025 Replication)
- **Protocol**: Two gold documents placed in context, padded with non-relevant distractors to scale context length across $L \in \{2\text{k}, 4\text{k}, 8\text{k}, 16\text{k}\}$ without explicit structural boundaries.
- **Purpose**: Measures the baseline context-length penalty slope ($\frac{\Delta \text{F1}}{\Delta L}$) independent of retrieval quality.

### Experimental Condition: Multi-Hop Structured Synthesis with Citation Tracking
- **Protocol**: Two-hop gold documents placed at controlled separations (co-located vs. split between beginning and middle), tagged with explicit document identifiers (`[Doc 1]`, `[Doc 2]`), evaluating both answer Token F1 and source attribution accuracy.

---

## 3. Evaluation Design & Data Leakage Audit
1. **Partition Integrity**: Use a frozen test slice of 100 verified multi-hop instances. Zero gradient updates or fine-tuning are performed, eliminating test-set contamination.
2. **Distractor Isolation**: Distractor passages are audited to ensure they do not contain lexical answers or valid alternative answers to the question.
3. **Attribution Audit**: Document identifiers are assigned deterministically at runtime to evaluate whether the model correctly cites `[Doc X]` or swaps references with distractors.

---

## 4. Independent Verification Checklist
- [x] Official dataset license verified as open-access (CC BY-SA 4.0 / MIT).
- [x] Schema inspected: `question`, `answer`, `context` (10 documents per example: 2 gold, 8 distractors).
- [x] Tokenizer length verification: prompts verified within 2k, 4k, 8k, 16k bounds.
- [x] Output evaluation metrics: exact token-level F1 and citation extraction regex audited.
