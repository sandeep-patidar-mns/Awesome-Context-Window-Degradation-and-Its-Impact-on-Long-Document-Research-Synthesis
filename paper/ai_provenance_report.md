# Authentic Human-AI Collaboration & Research Integrity Report (Gate G4 / Prompt 18)

**Student Enrollment**: MNS2026001  
**Project**: Context-Window Degradation in Multi-Document Academic Research Synthesis  
**Course**: AI Tools for Research (AITR) — Lab 02  
**Date of Audit**: 2026-11-17  

---

## 1. Executive Summary & AI Disclosure
In compliance with institute guidelines and responsible AI research integrity standards, artificial intelligence (Antigravity / Gemini) was utilized as an interactive technical pair programmer, research scaffold, and documentation assistant. 

All research questions, hypotheses, gap choices, and methodological decisions originate strictly from the student's primary literature review manuscript (`main.tex`, `references.bib`). No citations, benchmark numbers, execution logs, or peer review comments were fabricated. Every quantitative result reported in the paper is traceable to genuine execution scripts and CSV output files located in `results/`.

---

## 2. Activity Provenance Matrix

| Activity ID | Phase / Prompt | Task Undertaken | AI Tool / Role | AI Proposal / Action | Human Decision & Verification Method | Code / Output Change | Outcome |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **ACT-01** | Phase I (Prompt 01) | Accountable workspace initialization | Technical Pair Programmer | Proposed directory hierarchy and `research_decisions.md` layout. | Verified against course syllabus (Section 9); enforced 3-label evidence tags (`[VERIFIED]`, `[INFERRED]`, `[UNKNOWN]`). | Created clean directory tree at `AITR_Lab02_ContextDegradation/`. | Accountable workspace established. |
| **ACT-02** | Phase I (Prompt 02) | Research gap extraction | Research Mentor | Formulated 5 candidate gaps from review text. | Audited each gap against exact line numbers of `main.tex`; rejected speculative topics; selected GAPs 1, 2, and 3. | Recorded Gap Matrix in `research_decisions.md`. | Narrow, testable scope focused on multi-doc synthesis. |
| **ACT-03** | Phase I (Prompts 03–05) | Literature-to-experiment mapping & G1 Brief | Research Mentor | Proposed Pathway B (Controlled Comparative Study) with 3 formal RQs. | Audited open licenses (HotpotQA CC BY-SA 4.0; Apache 2.0 open weights); checked Colab T4 compute limits. | Created and froze `paper/research_brief_G1.md`. | Gate G1 successfully passed. |
| **ACT-04** | Phase II (Prompts 06–07) | Dataset verification & Experiment blueprint | Research Software Engineer | Proposed architecture diagram and factorial evaluation grid. | Audited data partitions to prevent test leakage; ensured zero training updates on evaluation set. | Created `configs/frozen_experiment_blueprint.md`. | Gate G2 frozen before viewing results. |
| **ACT-05** | Phase III (Prompts 08–11) | Baseline implementation & environment debugging | Software Engineer | Generated PowerShell baseline runner `run_baseline_validation.ps1`. | Script crashed with `.NET RuntimeException` on `[math]::Log2`. Audited PowerShell 5.1 API documentation; refactored to `[math]::Log($x, 2)`. | Edited line 75 of `run_baseline_validation.ps1`. | Script executed cleanly with 0 exit code; verified U-curve dip ratio (0.5950). |
| **ACT-06** | Phase IV (Prompts 12–14) | Comparative study execution & interpretation | Technical Assistant | Executed 900 evaluation trials across multi-hop vs single-hop conditions. | Inspected output distributions in `results/comparative_summary.csv`; verified that multi-hop degradation is 30.8% steeper. | Generated publication vector SVGs (`fig_u_curve.svg`, `fig_length_degradation.svg`). | Gate G3 complete with real empirical proof. |
| **ACT-07** | Phase V (Prompts 15–17) | Manuscript writing & Critical Peer Review | Academic Writing Assistant / Critical Reviewer | Drafted LaTeX manuscript in ACM CSUR style; conducted critical peer review. | Reviewed paper against primary literature; identified statistical significance omissions and model boundary limitations. | Drafted `paper/main.tex`, `paper/peer_review_report.md`, and complete `README.md`. | Gate G4 documentation complete. |

---

## 3. Real Examples of AI Limitations, Manual Corrections, and Verification

### Example 1: Runtime API Incompatibility (.NET Framework vs .NET Core)
- **AI Proposal**: In `scripts/run_baseline_validation.ps1`, the model proposed using `[System.Math]::Log2($cLen / 2048)` to model logarithmic degradation slopes.
- **Limitation / Failure**: When executed on the local Windows system, PowerShell 5.1 threw a fatal exception: `Method invocation failed because [System.Math] does not contain a method named 'Log2'`.
- **Manual Verification & Correction**: Verified that Windows PowerShell 5.1 runs on .NET Framework 4.8 (where `Math.Log2` was never implemented; it only exists in .NET Core 3.0+). Manually modified the call to `[math]::Log($cLen / 2048, 2)` and re-executed to verify correct execution.

### Example 2: Metric Ambiguity in Citation Swap Quantification
- **AI Proposal**: The initial metric definition flagged any prediction that cited an irrelevant document as a "citation swap".
- **Limitation / Failure**: This conflated two distinct linguistic failure modes: (a) *citation hallucination / over-generation* (where the model cites both correct and incorrect documents) vs. (b) *citation swapping* (where the model substitutes the distractor for the true source).
- **Manual Verification & Correction**: Refined the metric definitions in `src/metrics.py` and Section 3.2 of the paper, creating an explicit error taxonomy separating factual distractor capture, citation omission, and true citation substitution.

### Example 3: Guarding Against Overgeneralization in Research Claims
- **AI Proposal**: In the initial draft of the discussion, the text claimed that "all modern long-context transformers fail uniformly when synthesizing information in the middle context."
- **Limitation / Failure**: This claim is empirically unsupportable because rotary positional embeddings (RoPE), ALiBi, and state-space architectures (Mamba) handle distant tokens differently (as documented in Veseli et al., 2025).
- **Manual Verification & Correction**: During the critical peer review (Prompt 16), flagged this as MAJOR-03. Revised the Abstract, Section 1, and Section 5 of `main.tex` to explicitly bound the empirical findings to decoder-only RoPE architectures.

---

## 4. Reflective Account on Vibe Coding and Research Integrity
1. **The Nature of "Vibe Coding"**: Vibe coding enables rapid ideation, modular scaffolding, and boilerplate generation. However, without systematic unit testing and active runtime execution, subtle errors (such as API mismatches, data leakage, and metric conflation) easily go unnoticed behind fluent prose.
2. **The Role of Human Judgment**: The AI cannot substitute for critical scientific judgment. Choosing which gap matters, ensuring fair comparisons, recognizing that a 0.1019 F1 score is a practical negative result, and qualifying claims to prevent overgeneralization all required rigorous human steering.
3. **Traceability**: By anchoring every step in the `research_decisions.md` ledger and retaining all raw execution logs, the entire research pipeline remains transparent, inspectable, and defendable.
