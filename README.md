# Awesome Context-Window Degradation in Long-Document Research Synthesis

A dual-phase research repository on **context-window degradation in Large Language Models (LLMs)** and its impact on long-document research, retrieval, reasoning, and evidence synthesis.

**Author:** Sandeep Patidar  
**Enrollment:** MNS2026001  
**Institution:** Indian Institute of Information Technology Allahabad (IIIT Allahabad)  
**Department:** Information Technology (IT)  
**Program:** MNS | Academic Year: 2026  
**GitHub:** [sandeep-patidar-mns](https://github.com/sandeep-patidar-mns)

---

## Repository Overview: Two Research Papers

This repository brings together two interconnected phases of research:

```
┌────────────────────────────────────────────────────────────────────────┐
│ PHASE 1: Literature Review & Curated Knowledge Base                    │
│ "Context-Window Degradation and Its Impact on Long-Document Synthesis" │
│ 20 Papers Thematically Mapped · Citation Integrity Audit · Tools       │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Extracted Gaps & Testable Hypotheses
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ PHASE 2: Empirical Implementation Study (AITR Lab 02 / Gates G1–G4)    │
│ "Quantifying Context-Window Degradation in Multi-Document Synthesis"   │
│ Reproducible Code · 900 Controlled Trials · ACM CSUR LaTeX Manuscript  │
└────────────────────────────────────────────────────────────────────────┘
```

---

## Table of Contents

- [Phase 1: Literature Review & Curated Resources](#phase-1-literature-review--curated-resources)
  - [Research Question](#research-question)
  - [Curated Research Components](#curated-research-components)
- [Phase 2: Empirical Implementation Study (Lab 02)](#phase-2-empirical-implementation-study-lab-02)
  - [Problem Statement & Research Questions (RQs)](#problem-statement--research-questions-rqs)
  - [Key Findings & Measured Results (900 Trials)](#key-findings--measured-results-900-trials)
  - [Factorial Results Table](#factorial-results-table)
  - [Publication Figures](#publication-figures)
- [Repository Structure](#repository-structure)
- [Quick Start & Reproducibility Guide](#quick-start--reproducibility-guide)
- [Human–AI Research Integrity & Provenance](#humanai-research-integrity--provenance)
- [License](#license)

---

## Phase 1: Literature Review & Curated Resources

Large Language Models advertise context windows reaching 32k, 128k, or even 1M tokens. However, a large nominal window does not guarantee that a model can reliably use all information contained within that context. Research has demonstrated position-dependent effects such as the **Lost-in-the-Middle** phenomenon (Liu et al., 2024), where evidence in the middle quartile suffers severe retrieval and attention decay.

### Research Question
> **How does increasing context length affect the ability of Large Language Models to retrieve, reason over, and synthesize information from long documents?**

```text
Context Length
      ↓
Information Position
      ↓
Retrieval and Attention
      ↓
Reasoning and Evidence Aggregation
      ↓
Research Synthesis Quality
```

### Curated Research Components
- **Initial Review Paper (PDF)**: [`Review_Paper_Initially_Submitted.pdf`](Review_Paper_Initially_Submitted.pdf) or [`paper/AI_Assisted_Research_Paper.pdf`](paper/AI_Assisted_Research_Paper.pdf) (Complete 16-page Literature Review: *Context-Window Degradation and Its Impact on Long-Document Research Synthesis*, IIIT Allahabad).
- **Citation Integrity Audit**: [`citation-audit/Citation_Integrity_Audit.pdf`](citation-audit/Citation_Integrity_Audit.pdf) (Provenance audit of reviewed sources).
- **Primary References**: [`references/references.md`](references/references.md) (Annotated literature base).
- **Datasets & Benchmarks**: [`datasets/datasets.md`](datasets/datasets.md) (LongBench, HotpotQA, BABILong, NoLiMa).
- **Implementations**: [`implementations/github-repositories.md`](implementations/github-repositories.md) (Relevant open-source repositories).
- **Tools**: [`tools/tools.md`](tools/tools.md) (ResearchRabbit, Litmaps, Semantic Scholar, Elicit).
- **Tutorials**: [`tutorials/learning-resources.md`](tutorials/learning-resources.md) (Long-context reasoning resources).

---

## Phase 2: Empirical Implementation Study (Lab 02)

Extending from the literature review gaps, Phase 2 conducts a **controlled experimental investigation** into multi-document academic literature synthesis, evaluating open-weight models across **900 controlled trials**.

### Problem Statement & Research Questions (RQs)
1. **RQ1 (Relational Complexity Degradation)**: Under controlled distractor scaling ($L \in \{2\text{k}, 4\text{k}, 8\text{k}\}$), does two-hop cross-document synthesis experience a significantly steeper degradation slope than single-passage fact extraction?
2. **RQ2 (Positional Attribution Vulnerability)**: When gold evidence is situated in the Middle quartile versus Edges (Beginning, End), does middle placement cause a disproportionate surge in citation swap errors?
3. **RQ3 (Structural Boundary Mitigation)**: Does explicit Markdown document formatting provide structural anchor tokens that alleviate middle-context representation collapse?

---

### Key Findings & Measured Results (900 Trials)

1. **Multi-Hop Synthesis Degrades 30.8% Faster**:
   - Single-hop fact extraction in the middle drops from **0.414 F1** (2k) to **0.280 F1** (8k), a slope of $\beta = -0.0669$ per context doubling.
   - Multi-hop cross-document synthesis in the middle drops from **0.277 F1** (2k) down to **0.102 F1** (8k), a slope of $\beta = -0.0875$.
   - *Relational reasoning across documents disperses attention weights across distant distractors.*

2. **Middle-Context Citation Swaps Triple to 60.0%**:
   - In multi-hop synthesis, citation swap error rate is **20.0%** at the beginning, but surges to **60.0%** in the middle.
   - *The model frequently generates the right factual entity, but attributes it to an adjacent distractor paper. Attribution fidelity decays faster than surface factual recall.*

3. **Structural Formatting Provides Positional Anchoring**:
   - Explicit Markdown tags (`[Doc X] Title: ... Content: ...`) recovered **+0.082 F1** in the middle at 2048 tokens and prevented total failure at 8192 tokens (**0.102 F1** structured vs **0.026 F1** unformatted).
   - *Negative finding / Honest limitation*: An F1 of 0.102 at 8192 tokens is still modest; structural tagging helps, but hierarchical section retrieval remains necessary for long inputs.

---

### Factorial Results Table

| Task Complexity | Context Length | Position | Format | Mean Token F1 | Exact Match | Attribution Recall | Citation Swap Error |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Single-Hop Extraction | 2048 | Beginning | Structured | 0.7347 | 0.00 | 0.9339 | 0.00 |
| Single-Hop Extraction | 2048 | Middle | Structured | **0.4142** | 0.00 | 0.7011 | **0.4500** |
| Single-Hop Extraction | 2048 | End | Structured | 0.6905 | 0.00 | 0.9039 | 0.1000 |
| Single-Hop Extraction | 4096 | Beginning | Structured | 0.7016 | 0.00 | 0.9443 | 0.0500 |
| Single-Hop Extraction | 4096 | Middle | Structured | **0.3513** | 0.00 | 0.7025 | **0.5000** |
| Single-Hop Extraction | 4096 | End | Structured | 0.6270 | 0.00 | 0.9090 | 0.1500 |
| Single-Hop Extraction | 8192 | Beginning | Structured | 0.6582 | 0.00 | 0.9484 | 0.0500 |
| Single-Hop Extraction | 8192 | Middle | Structured | **0.2804** | 0.00 | 0.7052 | **0.5000** |
| Single-Hop Extraction | 8192 | End | Structured | 0.5753 | 0.00 | 0.9082 | 0.2000 |
| **Multi-Hop Synthesis** | 2048 | Beginning | Structured | 0.6530 | 0.00 | 0.8316 | 0.2000 |
| **Multi-Hop Synthesis** | 2048 | Middle | Structured | **0.2769** | 0.00 | 0.5366 | **0.6000** |
| **Multi-Hop Synthesis** | 2048 | End | Structured | 0.5797 | 0.00 | 0.7883 | 0.3000 |
| **Multi-Hop Synthesis** | 4096 | Beginning | Structured | 0.5719 | 0.00 | 0.8289 | 0.2000 |
| **Multi-Hop Synthesis** | 4096 | Middle | Structured | **0.1816** | 0.00 | 0.5287 | **0.6000** |
| **Multi-Hop Synthesis** | 4096 | End | Structured | 0.5255 | 0.00 | 0.7949 | 0.1667 |
| **Multi-Hop Synthesis** | 8192 | Beginning | Structured | 0.5129 | 0.00 | 0.8234 | 0.2333 |
| **Multi-Hop Synthesis** | 8192 | Middle | Structured | **0.1019** | 0.00 | 0.5353 | **0.4000** |
| **Multi-Hop Synthesis** | 8192 | End | Structured | 0.4608 | 0.00 | 0.7930 | 0.3000 |
| *Ablation: Multi-Hop* | 2048 | Middle | Unstructured | 0.1946 | 0.00 | 0.4598 | 0.7333 |
| *Ablation: Multi-Hop* | 4096 | Middle | Unstructured | 0.1114 | 0.00 | 0.4607 | 0.6000 |
| *Ablation: Multi-Hop* | 8192 | Middle | Unstructured | **0.0264** | 0.00 | 0.4570 | 0.6667 |

---

### Publication Figures
- **Positional U-Curve**: [`results/fig_u_curve.svg`](results/fig_u_curve.svg)
- **Degradation Slopes**: [`results/fig_length_degradation.svg`](results/fig_length_degradation.svg)
- **Citation Swap Errors**: [`results/fig_attribution_errors.svg`](results/fig_attribution_errors.svg)

---

## Repository Structure

```text
├── README.md                              # Unified dual-phase repository guide
├── requirements.txt                       # Verified dependencies (torch, transformers, bitsandbytes)
├── research_decisions.md                  # Chronological research decisions ledger (Stages 1–8)
├── gap_matrix.md                          # Literature gap extraction and ranking (Gaps 1–5)
├── baseline_validation.md                 # Baseline reproduction report (Liu et al. 2024 audit)
├── ai_assistance_log.md                   # Authentic AI collaboration & debugging ledger
├── DEMO_WALKTHROUGH.md                    # 5-minute technical viva walkthrough
│
├── configs/
│   ├── dataset_baseline_validation.md     # Primary dataset, licensing, leakage audit (Prompt 04, 06)
│   └── frozen_experiment_blueprint.md     # Architecture diagram, frozen metrics & 900-trial grid (Prompt 07)
│
├── data/
│   ├── README.md                          # Data schema and licensing terms
│   └── frozen_test_instances.json         # 50 frozen academic multi-hop evaluation instances
│
├── notebooks/
│   └── AITR_Lab02_Colab_Runner.ipynb      # Executable Google Colab notebook for GPU execution
│
├── src/                                   # Reusable modular code package
│   ├── metrics.py                         # Token F1, Exact Match, Citation Attribution & U-Dip metrics
│   ├── data_loader.py                     # Schema validation & multi-doc dataset wrapper
│   ├── context_packer.py                  # Positional injector (Beg/Mid/End) & distractor scaler
│   ├── inference_engine.py                # 4-bit quantized open-weights LLM loader (greedy decoding)
│   ├── evaluator.py                       # Full factorial experimental slice evaluator
│   └── visualizer.py                      # Vector figure plotting routines
│
├── scripts/
│   ├── run_baseline_validation.ps1        # PowerShell baseline reproduction runner
│   ├── run_comparative_study.ps1          # 900-trial comparative study runner
│   ├── generate_plots.ps1                 # Publication vector SVG generator
│   ├── run_experiments.py                 # Python CLI experimental entrypoint
│   └── verify_environment.py              # Environment sanity check script
│
├── tests/
│   └── test_metrics.py                    # Unit tests for metrics and parsers
│
├── results/                               # Genuine measured experimental outputs
│   ├── baseline_reproduction_results.csv  # Liu et al. (2024) single-hop reproduction data
│   ├── comparative_study_results.csv      # Raw 900-trial experimental execution log
│   ├── comparative_summary.csv            # Aggregated factorial summary matrix
│   └── results_and_discussion_outline.md  # Findings, physical mechanisms, and follow-ups
│
├── paper/                                 # Paper manuscripts and reports
│   ├── main.tex                           # Full ACM CSUR research paper LaTeX source
│   ├── references.bib                     # 20 verified bibliographic references
│   ├── research_brief_G1.md               # One-page formal research brief (Gate G1)
│   ├── peer_review_report.md              # Technical peer review & revision table (Gate G4)
│   ├── ai_provenance_report.md            # AI disclosure & human-AI collaboration audit (Prompt 18)
│   └── AI_Assisted_Research_Paper.pdf     # Phase 1 literature review PDF
│
├── citation-audit/                        # Phase 1 citation audit report
├── datasets/                              # Phase 1 benchmark directory
├── implementations/                       # Phase 1 open-source repository list
├── references/                            # Phase 1 annotated references
├── tools/                                 # Phase 1 discovery tools documentation
└── tutorials/                             # Phase 1 learning resources
```

---

## Quick Start & Reproducibility Guide

### Local Fast Rerun (PowerShell)
```powershell
# 1. Reproduce Liu et al. (2024) baseline (Gate G2)
powershell -ExecutionPolicy Bypass -File scripts/run_baseline_validation.ps1

# 2. Run full 900-trial comparative study (Gate G3)
powershell -ExecutionPolicy Bypass -File scripts/run_comparative_study.ps1

# 3. Regenerate publication vector figures
powershell -ExecutionPolicy Bypass -File scripts/generate_plots.ps1
```

### Google Colab GPU Execution
Open [`notebooks/AITR_Lab02_Colab_Runner.ipynb`](notebooks/AITR_Lab02_Colab_Runner.ipynb) in Google Colab with a free T4 GPU to run end-to-end inference with `Qwen/Qwen2.5-7B-Instruct`.

---

## Human–AI Research Integrity & Provenance

In compliance with institute guidelines, AI (Antigravity / Gemini) was used as an interactive technical pair programmer and writing scaffold under supervised human review.

- **Integrity Rule**: No citations, benchmark numbers, or execution logs were fabricated. Every number in Table 1 is traceable to `results/comparative_study_results.csv`.
- **Detailed Audit**: See [`paper/ai_provenance_report.md`](paper/ai_provenance_report.md) and [`ai_assistance_log.md`](ai_assistance_log.md) for the 3 documented debugging cases and human decisions.

---

## License
MIT License. See [LICENSE](LICENSE) for details.
