# Research Decisions Log: Context-Window Degradation in Long-Document Synthesis

**Project**: AITR Lab 02 — Implementation & Evidence-Based Research Study  
**Topic**: Context-Window Degradation and Its Impact on Long-Document Research Synthesis  
**Student Enrollment**: MNS2026001  
**Status**: Stage 1 — Accountable Workspace Setup & Literature Scope Summary  

---

## 1. Evidence Classification Standards
Every decision, finding, and claim in this project is tagged with one of three labels:
- **`[VERIFIED]`**: Directly extracted and confirmed from the source literature review manuscript (`main.tex`, `references.bib`), peer-reviewed publication, official repository, or verified code execution logs.
- **`[INFERRED]`**: Methodologically plausible synthesis, interpretation, or engineering design hypothesis that requires empirical testing or external validation before acceptance.
- **`[UNKNOWN]`**: Missing information, unverified access to weights/code/datasets, or unconfirmed empirical behavior.

---

## 2. Decision Record

| Entry ID | Date | Phase / Stage | Decision Made | Rationale & Evidence Base | Evidence Level | Next Actions |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **DEC-001** | 2026-11-17 | Phase I (Prompt 01) | Established dedicated research workspace `AITR_Lab02_ContextDegradation` conforming to course repository structure. | Required standard structure for reproducible code, configurations, logs, and artifacts. | `[VERIFIED]` Course Spec (Sec 9) | Initialize subdirectories: `configs/`, `data/`, `notebooks/`, `src/`, `scripts/`, `results/`, `paper/`. |
| **DEC-002** | 2026-11-17 | Phase I (Prompt 01) | Bounded study domain strictly to the scope established in literature review: *Context-Window Degradation and Its Impact on Long-Document Research Synthesis*. | Preserves research continuity from previous review without topical drift or ungrounded claims. | `[VERIFIED]` (`main.tex` L20-25) | Summarize exact review scope, 20-paper evidence corpus, and 4 thematic pillars. |
| **DEC-003** | 2026-11-17 | Phase I (Prompt 01) | Adopted three-label evidence ledger (`[VERIFIED]`, `[INFERRED]`, `[UNKNOWN]`) across all documentation and logs. | Enforces strict research integrity, preventing hallucinated citations, imaginary datasets, or synthetic benchmarks disguised as real experiments. | `[VERIFIED]` Course Spec (Sec 6, Sec 10) | Apply label tags across gap extraction (Prompt 02) and experiment mapping (Prompt 03). |
| **DEC-004** | 2026-11-17 | Phase I (Prompt 02) | Extracted 5 computationally testable research gaps grounded in review Sections 6 & 8; ranked top 3 based on compute feasibility on local/colab environments. | Ensures experimental question directly addresses verified literature limitations rather than synthetic toys. | `[VERIFIED]` (`main.tex` L167-186) | Select target gap and map to runnable baseline in Prompt 03. |
| **DEC-005** | 2026-11-17 | Phase I (Prompt 03) | Mapped literature to 3 published methods (Liu et al. 2024, Du et al. 2025, Modarressi et al. 2025); selected Controlled Comparative Study (Pathway B) comparing Single-Document Retrieval vs. Cross-Document Synthesis under positional shift. | High scientific validity, zero weight retraining required, executable on standard Colab T4/L4 GPU with quantized open-weights (Qwen2.5 / Llama-3.2). | `[VERIFIED]` (Liu et al. 2024, Du et al. 2025) | Perform feasibility and novelty check (Prompt 04). |
| **DEC-006** | 2026-11-17 | Phase I (Prompt 04) | Conducted novelty and feasibility verification; established formal Go/No-Go criteria and fallback architecture (Qwen2.5-1.5B/3B for CPU fallback). | Confirms dataset, open-weights, and compute boundaries without incurring training costs. | `[VERIFIED]` Hugging Face model cards, Apache 2.0 licenses | Frame formal research questions and success criteria (Prompt 05). |
| **DEC-007** | 2026-11-17 | Phase I (Prompt 05) | Drafted and froze Gate G1 One-Page Research Brief with 3 testable RQs, explicit independent/dependent variables, falsification criteria, and decision thresholds. | Meets all Gate G1 approval criteria; grounds study in literature without claiming unverified novelty. | `[VERIFIED]` (`paper/research_brief_G1.md`) | Proceed to Phase II: Dataset and Comparator Verification (Prompt 06). |
| **DEC-008** | 2026-11-17 | Phase II (Prompt 06) | Verified primary dataset (HotpotQA multi-hop distractor split, CC BY-SA 4.0) and established two baseline comparators (Single-Hop Extraction replicating Liu et al. 2024, Flat Scaling replicating Du et al. 2025). | Data format directly matches multi-document academic literature synthesis requirements. | `[VERIFIED]` (`configs/dataset_baseline_validation.md`) | Design and freeze experimental blueprint (Prompt 07). |
| **DEC-009** | 2026-11-17 | Phase II (Prompt 07) | Froze reproducible experiment blueprint including architecture diagram, 4-level context grid (2k-16k), positional splits, metrics (Token F1, EM, Attribution P/R/Swap), and seed controls (SEED=42). | Freezing protocol before viewing results prevents p-hacking, cherry-picking, and data leakage. | `[VERIFIED]` (`configs/frozen_experiment_blueprint.md`) | Proceed to Phase III: Environment Configuration & Baseline Vibe-Coding (Prompts 08-11). |
| **DEC-010** | 2026-11-17 | Phase III (Prompts 08–11) | Configured environment, authored modular Python src/ suite (`metrics.py`, `data_loader.py`, `context_packer.py`, `evaluator.py`, `visualizer.py`), and reproduced Liu et al. (2024) baseline. Fixed `.NET Math.Log2` runtime bug. | Genuine executed baseline outputs in `results/baseline_reproduction_results.csv` confirm 43.9% middle-context drop (Dip Ratio = 0.5950). | `[VERIFIED]` (`baseline_validation.md`) | Proceed to Phase IV: Controlled Comparative Study (Prompts 12–14). |
| **DEC-011** | 2026-11-17 | Phase IV (Prompts 12–14) | Executed 900 trials in controlled comparative study; answered RQ1 (30.8% steeper slope for multi-hop), RQ2 (citation swap error surges to 60.0% in middle), and RQ3 (Markdown tags recover +0.0823 F1 in middle). | All numbers derived from actual CSV output in `results/comparative_study_results.csv` and `results/comparative_summary.csv`. | `[VERIFIED]` (`results/results_and_discussion_outline.md`) | Proceed to Phase V: Paper drafting & Critical Peer Review (Prompts 15–17). |
| **DEC-012** | 2026-11-17 | Phase V (Prompts 15–17) | Authored complete ACM CSUR-style implementation manuscript (`paper/main.tex`), verified bibliography (`paper/references.bib`), conducted rigorous peer review (`paper/peer_review_report.md`), and updated `README.md`. | Synthesizes genuine evidence into publication-ready form without fabricated numbers. | `[VERIFIED]` (`paper/main.tex`, `paper/peer_review_report.md`) | Proceed to Phase VI: Human-AI Collaboration Audit (Prompt 18). |
| **DEC-013** | 2026-11-17 | Phase VI (Prompt 18) | Documented complete AI activity provenance, 3 real limitation/debugging case studies, and vibe coding reflections in `paper/ai_provenance_report.md`. | Fulfills academic integrity requirements and responsible AI disclosure for coursework submission. | `[VERIFIED]` (`paper/ai_provenance_report.md`) | Package project for final submission. |

---

## 6. Novelty and Feasibility Verification Matrix (Prompt 04)

### 6.1 Neighboring Literature Matrix
| Published Method | VERIFIED Contribution (Source) | Limitation | Proposed Difference in Our Study | Evidence Still Missing |
| :--- | :--- | :--- | :--- | :--- |
| **Liu et al. (2024)** | Showed U-shaped retrieval degradation in long contexts (`main.tex` L27–35, L96–98). | Tested single fact retrieval embedded in distractors; did not measure citation attribution or multi-hop synthesis. | Measures cross-document multi-hop reasoning + source attribution under positional shift. | Empirical attribution error rates under varying distractor density `[UNKNOWN]`. |
| **Du et al. (2025)** | Proved context length itself hurts accuracy even with perfect retrieval (`main.tex` L80–85, L99). | Did not isolate whether the degradation affects multi-hop relational reasoning more severely than single-hop extraction. | Directly isolates Single-Hop vs. Two-Hop relational synthesis under identical context lengths (2k, 4k, 8k, 16k). | Quantitative degradation slope delta between single-hop and multi-hop `[UNKNOWN]`. |
| **Veseli et al. (2025)** | Positional biases shift dynamically near context window limits (`main.tex` L88–94, L100). | Focused on language modeling perplexity / synthetic probes rather than research synthesis. | Examines multi-document scientific document synthesis and citation faithfulness. | Model-specific shift thresholds on instruction-tuned weights `[UNKNOWN]`. |

### 6.2 Resource & Access Verification
- **Model Access**: `Qwen/Qwen2.5-7B-Instruct` (Apache 2.0 license, open weights on Hugging Face) and `meta-llama/Llama-3.2-3B-Instruct` (Llama 3.2 community license). `[VERIFIED]`
- **Dataset Access**: HotpotQA (multi-hop QA with gold evidence and distractors, CC-BY-SA 4.0) + scientific paper abstract corpus. `[VERIFIED]`
- **Compute Feasibility**:
  - Model footprint in 4-bit (`bitsandbytes` NF4): ~5.2 GB VRAM.
  - Context budget: 2k, 4k, 8k, 16k tokens.
  - Evaluation batch: 100 controlled instances $\times$ 4 context lengths $\times$ 3 positions = 1,200 inference passes.
  - Estimated Colab T4 runtime: ~60–75 minutes.
- **Fallback Plan**:
  - If GPU VRAM is restricted, scale to `Qwen/Qwen2.5-1.5B-Instruct` or `Qwen/Qwen2.5-0.5B-Instruct`, which executes on standard CPU (8GB RAM) within 30 minutes for a 50-example evaluation slice.
- **Decision Rule (Go/No-Go)**:
  - **GO**: Weights, dataset, and inference pipelines are 100% open-access; no proprietary API dependencies, no training costs, fully deterministic random seeds.


---

## 5. Literature-to-Experiment Mapping (Prompt 03)

### 5.1 Published Methods Comparison
| Paper | Method / Protocol | Dataset / Benchmark | Verified Code / Weights Access | Evaluation Metric | Compute Burden |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Liu et al. (2024)** [TACL] | Positional shift of relevant passage across $k$ documents in context ($k \in [1, 20]$). | Multi-document QA (NaturalQuestions, HotpotQA) | `[VERIFIED]` Official GitHub `nelson-liu/lost-in-the-middle`; open HuggingFace weights. | Accuracy, Token F1, Exact Match (EM) | Low to Medium (Inference only, fits 1x T4 GPU). |
| **Du et al. (2025)** [EMNLP] | Disentangling context length from retrieval: padding oracle evidence with distractor tokens (1k to 32k). | HotpotQA, NarrativeQA, synthetic distractors | `[VERIFIED]` Standard HuggingFace pipeline; open evaluation scripts. | Degradation slope ($\Delta \text{F1}/\Delta L$), retention rate | Low to Medium (Inference-only scaling test). |
| **Modarressi et al. (2025)** [ICML] | Non-literal long-context reasoning removing lexical overlap cues. | NoLiMa benchmark | `[VERIFIED]` PMLR paper; open benchmark repository. | Non-lexical extraction accuracy | Medium (Requires NoLiMa data pipeline). |

### 5.2 Comparative Analysis of Three Candidate Study Pathways
1. **Pathway A (Reproduction + Extension)**:
   - *Baseline*: Reproduce Liu et al. (2024) single-needle retrieval U-curve on an open-weight instruction model (e.g. `Qwen2.5-7B-Instruct` or `Llama-3.2-3B-Instruct`).
   - *Extension*: Introduce academic paper distractors rather than general Wikipedia articles to measure domain sensitivity.
2. **Pathway B (Controlled Comparative Study — RECOMMENDED)**:
   - *Baseline*: Reproduce the position and length degradation protocol.
   - *Controlled Comparison*: Evaluate two task complexities under the exact same context lengths (2k, 4k, 8k, 16k) and positions (Beginning, Middle, End):
     - Task 1: *Single-Document Fact Extraction* (isolated passage).
     - Task 2: *Cross-Document Synthesis* (two-hop dependency split across two separate papers).
   - *Secondary Metric*: Source Attribution Accuracy (does the model correctly attribute the claim to the source document or swap citations?).
3. **Pathway C (Targeted Modification / Ablation)**:
   - *Modification*: Compare raw concatenated context vs. structural markdown/XML tagging (`<doc id="...">...</doc>`).

### 5.3 Recommended Minimum Viable Experiment (MVE)
- **Pathway**: **Pathway B (Controlled Comparative Study)** with structural logging.
- **Hardware Profile**: Google Colab Free T4 (15GB VRAM) using 4-bit NF4 quantization (`bitsandbytes`) or Colab Pro L4 / A100; executable locally on CPU for sanity checks.
- **Model**: `Qwen/Qwen2.5-7B-Instruct` or `meta-llama/Llama-3.2-3B-Instruct` (accessible, standard permissive licenses, verified 32k–128k native context support).
- **Verification Checklist before coding**:
  1. Confirm exact open-weight model license and Hugging Face tokenizer limits.
  2. Confirm dataset source (HotpotQA multi-hop subset + academic abstract corpus) without data leakage.
  3. Validate exact metric implementations: Token F1, Exact Match, and Source Attribution Precision/Recall.


---

## 4. Gap Matrix (Prompt 02)

| Gap ID | Source Evidence & Cited Passage in Review | Author-Reported Limitation vs. Our Inference | Proposed Experimental Question | Evidence / Test Setup Needed | Ranking & Feasibility |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GAP-1** | `main.tex` L169, L178–180; Du et al. (2025); Liu et al. (2024) | **Author Reported**: Models suffer steep degradation under increasing context even with perfect retrieval (Du et al.).<br>**Our Inference**: In multi-paper synthesis, degradation is compounded when evidence requires cross-document synthesis rather than single-needle retrieval. | *How does effective context degradation differ between single-needle retrieval vs. two-hop cross-document claim verification under increasing distractor contexts?* | Evaluate open-weight model (e.g. Llama-3-8B / Mistral-7B / Qwen2.5-7B) on controlled multi-document evidence pairs across 2k, 4k, 8k, 16k context lengths. | **Rank 1** (High significance; runnable on modest GPU/Colab; clean testable independent variables). |
| **GAP-2** | `main.tex` L171, L181–182; Modarressi et al. (2025); Liu et al. (2024) | **Author Reported**: Models rely on surface lexical cues and struggle with semantic synthesis (Modarressi et al.).<br>**Our Inference**: Models may produce fluent summaries while misattributing findings to the wrong paper (citation hallucination) when evidence is buried in the middle. | *Does positional degradation ("Lost in the Middle") disproportionately increase source misattribution (citation swap errors) compared to factual extraction errors?* | Controlled positioning (Beginning, Middle, End) of 5–10 academic paper abstracts; measure claim accuracy vs. citation attribution accuracy. | **Rank 2** (High relevance to academic research synthesis; clearly measurable precision/recall). |
| **GAP-3** | `main.tex` L173, L183–184; Veseli et al. (2025); Arjmandi (2026) | **Author Reported**: Positional biases shift dynamically as sequence length approaches limit (Veseli et al.).<br>**Our Inference**: Scientific document structure (preserving section headers vs. stripping headers into raw text) mitigates positional bias by providing structural anchor tokens. | *Does preserving explicit document section metadata (Introduction, Methods, Results) alleviate middle-context degradation during multi-document QA?* | Controlled ablation: structured markdown headers vs. raw concatenated text with target evidence placed at varying relative depths [0.1 to 0.9]. | **Rank 3** (Feasible; requires no training; directly tests structural ablation). |
| **GAP-4** | `main.tex` L175, L185; Tang et al. (2025); McKinnon (2025) | **Author Reported**: RAG lowers computation but can drop cross-document dependencies (McKinnon 2025).<br>**Our Inference**: An adaptive threshold based on query complexity can outperform rigid top-$k$ RAG or brute-force full context. | *At what context length and document count does BM25/dense retrieval degrade cross-document synthesis compared to direct full-context ingestion?* | Comparative evaluation of Full-Context vs. Top-$k$ RAG across variable document sets (1 to 20 papers). | Feasible, but Rank 4 due to confounding retrieval-ranker variables. |
| **GAP-5** | `main.tex` L174; Dsouza et al. (2024); Yan et al. (2025) | **Author Reported**: Sparse attention reduces FLOPs but does not resolve semantic degradation (Yan et al.).<br>**Our Inference**: Inference-time attention head temperature scaling or calibration mitigates working-memory decay. | *Can inference-time attention logit re-weighting recover lost-in-the-middle degradation without weight updates?* | Requires custom attention mask / kernel hook intervention in PyTorch. Higher implementation complexity on consumer hardware. | Rank 5 (Higher engineering risk for short lab timeline). |


---

## 3. Scope Summary of Completed Literature Review

### 3.1 Review Overview
- **Title**: *Context-Window Degradation and Its Impact on Long-Document Research Synthesis* `[VERIFIED: main.tex L20]`
- **Target Venue / Format**: ACM Computing Surveys (CSUR) format, manuscript style `[VERIFIED: main.tex L1, L18]`
- **Corpus Size**: 20 scholarly papers discovered via ResearchRabbit, Litmaps, Semantic Scholar, and Elicit `[VERIFIED: main.tex L24, L61]`
- **Core Premise**: A larger nominal context window (e.g., 32k, 128k, 1M tokens) does not guarantee reliable, uniform information retrieval or multi-document reasoning. Effective context use is a task-, position-, and evidence-dependent reliability property `[VERIFIED: main.tex L24, L54-58]`.

### 3.2 Thematic Organization
The reviewed literature is organized into four distinct thematic pillars:
1. **Context Extension & Nominal Capacity**: Methods scaling sequence representations (e.g., ALiBi linear biases [Press et al., 2022], Positional Interpolation [Chen et al., 2023], Granite Code 128k context scaling [Stallone et al., 2024]) `[VERIFIED: main.tex L91-95, L147]`.
2. **Empirical Context Degradation & Positional Effects**: Empirical demonstrations of performance loss with sequence length and positional bias ("Lost in the Middle" U-shaped curve [Liu et al., 2024]; context length hurting performance despite perfect oracle retrieval [Du et al., 2025]; positional biases shifting near context limits [Veseli et al., 2025]; distractor accumulation [Arjmandi, 2026]) `[VERIFIED: main.tex L96-100, L108-111]`.
3. **Long-Context Reasoning & Multi-Document Synthesis**: Benchmarks evaluating evidence distributed across documents, complex label spaces, and semantic reasoning without literal keyword matching (LongBench [Bai et al., 2024]; Long In-Context Learning [Li et al., 2025]; NoLiMa [Modarressi et al., 2025]; BABILong [Kuratov et al., 2024]; LongReason [Ling et al., 2025]) `[VERIFIED: main.tex L101-105]`.
4. **Mitigation Approaches**: Retrieval-Augmented Generation (RAG) and context compression, efficient/sparse attention (Adamas [Yan et al., 2025]), and long-context alignment/training (LOGO preference optimization [Tang et al., 2025]; Untie the Knots continued pretraining data augmentation [Tian et al., 2025]) `[VERIFIED: main.tex L111-115, L123-144]`.

### 3.3 Identified Limitations in Prior Literature
- Benchmarks often rely on synthetic "needle-in-a-haystack" or simple single-passage retrieval rather than complex multi-document research synthesis `[VERIFIED: main.tex L162-166, L178-180]`.
- Existing evaluations infrequently measure claim-level source attribution and faithfulness simultaneously with reasoning accuracy `[VERIFIED: main.tex L159-161, L181-182]`.
- Document structure (headings, tables, academic paper formatting) and realistic distractor placement are rarely treated as systematic experimental variables `[VERIFIED: main.tex L173, L183-184]`.
