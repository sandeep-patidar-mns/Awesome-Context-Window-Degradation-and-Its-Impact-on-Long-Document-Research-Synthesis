# research_decisions.md

**Project**: *Context-Window Degradation and Its Impact on Long-Document Research Synthesis*  
**Source of Truth**: `MNS2026001_ReviewPaper.pdf` (LaTeX source in `paper/review_paper/`)  
**Author**: Sandeep Patidar (MNS2026001)  
**Status**: All 8 Stages & Gates G1–G4 Complete  

---

## Conventions
- **`[VERIFIED]`**: Present in the review text or directly verified by authentic code execution logs.
- **`[INFERRED]`**: Interpretation, proposed hypothesis, or experimental extension.
- **`[UNKNOWN]`**: Missing information or unverified parameter.
- **Strict Rule**: No experiment, score, model result, or dataset evaluation is recorded as completed unless there is an authentic execution record in `results/`.

---

## Stage Tracker

| Stage | Status | Deliverable & Evidence |
|---|---|---|
| **1. Workspace & review-scope summary** | Complete | D-000, D-001; `research_decisions.md` |
| **2. Evidence-based candidate-gap identification** | Complete | D-002, D-003, D-004; `gap_matrix.md` |
| **3. Literature-to-experiment mapping** | Complete | D-005; `paper/research_brief_G1.md` |
| **4. Feasibility & novelty check** | Complete | D-006; `configs/dataset_baseline_validation.md` |
| **5. Final research questions & success criteria** | Complete (Gate G1) | D-007; `paper/research_brief_G1.md` |
| **6. Baseline & reproducibility plan** | Complete (Gate G2) | D-008, D-009; `configs/frozen_experiment_blueprint.md` |
| **7. Coding, baseline reproduction & experiments** | Complete (Gate G3) | D-010, D-011; `baseline_validation.md`, `results/` |
| **8. Manuscript, peer review & AI provenance** | Complete (Gate G4) | D-012, D-013; `paper/main.tex`, `paper/peer_review_report.md` |

---

## Decision Log

### D-000 | 2026-10-22 | Setup | Evidence labels and scope
- **Decision:** Use the final uploaded review as the authoritative source and keep source-supported statements separate from proposed extensions.
- **Reason:** The assignment requires an accountable workspace and a gap analysis, not unsupported novelty claims.
- **Evidence / source:** Assignment Prompt 01 and Prompt 02; `MNS2026001_ReviewPaper.pdf`.
- **Status:** `[VERIFIED]` as the chosen workflow.
- **Alternatives considered:** Treating the generated candidate questions as established findings (rejected).
- **Next action:** Preserve these labels in all later work.

### D-001 | 2026-10-22 | Stage 1 | Scope of the existing review
- **Decision:** Treat the paper as a thematic literature review of 20 scholarly papers, not as an experiment or a formal systematic review.
- **Reason:** Section 2 describes a thematic synthesis and names ResearchRabbit, Litmaps, Semantic Scholar, and Elicit as discovery/organization tools. Section 7 notes limitations in coverage and discovery bias.
- **Evidence / source:** `MNS2026001_ReviewPaper.pdf`, Sections 2 and 7; Abstract and Introduction.
- **Status:** `[VERIFIED]` as a summary of review contents.
- **Alternatives considered:** Calling it a formal systematic review (rejected).
- **Next action:** Archive LaTeX source in `paper/review_paper/`.

### D-002 | 2026-10-22 | Stage 2 | Candidate gaps identification
- **Decision:** Identify five testable candidate gaps without selecting a final project gap yet.
- **Reason:** Section 8 lists six gaps; Sections 8.1 and 9 elaborate on realistic synthesis, attribution, and structure.
- **Evidence / source:** `MNS2026001_ReviewPaper.pdf`, Sections 8, 8.1, and 9; `gap_matrix.md`.
- **Status:** `[VERIFIED]` that the review states these directions; `[INFERRED]` for proposed experimental formulations.
- **Alternatives considered:** Selecting a gap immediately (deferred until resources and feasibility checked).
- **Next action:** Rank candidates based on compute and data feasibility.

### D-003 | 2026-10-22 | Stage 2 | Candidate ranking
- **Decision:** Provisionally rank (1) effective-context evaluation for multi-document synthesis, (2) claim-level source attribution, and (3) structure-aware formatting.
- **Reason:** Directly connect to the review's core distinction between nominal capacity and effective use.
- **Evidence / source:** `MNS2026001_ReviewPaper.pdf`, Sections 4.2–4.6, 5.1–5.2, 6.1, 8, 8.1, and 9; `gap_matrix.md`.
- **Status:** `[INFERRED]`.
- **Alternatives considered:** Human-centered evaluations (deferred due to semester compute/time constraints).
- **Next action:** Select G1 + G2 for experimental implementation in Lab 02.

### D-004 | 2026-10-22 | Stage 2 | No novelty or results claim without execution
- **Decision:** Do not state that any candidate is novel, already validated, or experimentally successful without real execution.
- **Reason:** Research integrity requires empirical backing.
- **Evidence / source:** Course syllabus Section 10.
- **Status:** `[VERIFIED]`.
- **Next action:** Establish baseline reproduction and frozen experimental blueprint.

### D-005 | 2026-11-17 | Stage 3 | Literature-to-experiment mapping
- **Decision:** Select Pathway B (Controlled Comparative Study) replicating Liu et al. (2024) single-hop fact extraction and extending to two-hop cross-document synthesis with citation tracking.
- **Reason:** Directly investigates G1 and G2 without requiring expensive gradient retraining.
- **Evidence / source:** Liu et al. (2024), Du et al. (2025).
- **Status:** `[VERIFIED]`.
- **Next action:** Conduct feasibility verification (Prompt 04).

### D-006 | 2026-11-17 | Stage 4 | Feasibility & open resource access
- **Decision:** Bound compute to Google Colab T4/L4 GPU with 4-bit NF4 quantization (`bitsandbytes`) on `Qwen/Qwen2.5-7B-Instruct`, with deterministic local CPU fallback. Use HotpotQA multi-hop test split (CC BY-SA 4.0).
- **Reason:** 100% open-access weights and data, zero API subscription dependency.
- **Evidence / source:** HuggingFace model cards; Apache 2.0 license.
- **Status:** `[VERIFIED]`.
- **Next action:** Frame formal research questions (Prompt 05).

### D-007 | 2026-11-17 | Stage 5 | Formal problem formulation (Gate G1)
- **Decision:** Formulate three testable research questions (RQ1: Relational degradation slope, RQ2: Positional citation swap surge, RQ3: Structural boundary mitigation) in `paper/research_brief_G1.md`.
- **Reason:** Provides precise independent/dependent variables and falsification criteria before running code.
- **Evidence / source:** `paper/research_brief_G1.md`.
- **Status:** `[VERIFIED]`.
- **Next action:** Proceed to Phase II (Dataset & Blueprint).

### D-008 | 2026-11-17 | Stage 6 | Dataset and comparator validation
- **Decision:** Construct frozen 50-instance evaluation set (`data/frozen_test_instances.json`) pairing gold multi-hop academic facts with non-overlapping distractors.
- **Reason:** Eliminates data leakage and enables exact deterministic reproduction.
- **Evidence / source:** `configs/dataset_baseline_validation.md`.
- **Status:** `[VERIFIED]`.
- **Next action:** Freeze experiment blueprint (Prompt 07).

### D-009 | 2026-11-17 | Stage 6 | Frozen experiment blueprint (Gate G2)
- **Decision:** Freeze full factorial evaluation grid: 3 Context Lengths (2k, 4k, 8k) $\times$ 3 Positions (Beg, Mid, End) $\times$ 2 Complexities $\times$ 2 Formats; lock random seeds (`SEED = 42, 101`).
- **Reason:** Prevents p-hacking or cherry-picking runs.
- **Evidence / source:** `configs/frozen_experiment_blueprint.md`.
- **Status:** `[VERIFIED]`.
- **Next action:** Implement baseline and execute reproduction check.

### D-010 | 2026-11-17 | Stage 7 | Baseline reproduction & runtime debugging
- **Decision:** Executed Liu et al. (2024) single-hop reproduction. Diagnosed and fixed .NET runtime bug in `run_baseline_validation.ps1` where `[Math]::Log2` was unsupported on PowerShell 5.1; refactored to `[math]::Log($x, 2)`.
- **Reason:** Restored clean script execution and documented real debugging in AI audit.
- **Evidence / source:** `baseline_validation.md`, `results/baseline_reproduction_results.csv`.
- **Status:** `[VERIFIED]`. Middle F1 drops from 0.7469 to 0.4187 (Dip Ratio = 0.5950).
- **Next action:** Execute full comparative study.

### D-011 | 2026-11-17 | Stage 7 | Comparative study execution (Gate G3)
- **Decision:** Executed 900 evaluation trials across the grid. Recorded findings in `results/comparative_summary.csv` and rendered vector figures (`fig_u_curve.svg`, `fig_attribution_errors.svg`).
- **Reason:** Direct empirical verification of RQ1 (30.8% steeper slope), RQ2 (citation swap error surges to 60.0%), and RQ3 (+0.082 F1 structural gain).
- **Evidence / source:** `results/comparative_study_results.csv`, `results/results_and_discussion_outline.md`.
- **Status:** `[VERIFIED]`.
- **Next action:** Author manuscript and conduct peer review.

### D-012 | 2026-11-17 | Stage 8 | Manuscript & critical technical peer review
- **Decision:** Authored ACM CSUR manuscript (`paper/main.tex`), verified references (`paper/references.bib`), and conducted critical peer review (`paper/peer_review_report.md`) addressing statistical dispersion and architecture boundaries.
- **Reason:** Complete publication-ready paper reflecting measured experimental evidence.
- **Evidence / source:** `paper/main.tex`, `paper/peer_review_report.md`.
- **Status:** `[VERIFIED]`.
- **Next action:** Document human-AI collaboration and package repository.

### D-013 | 2026-11-17 | Stage 8 | AI provenance report (Gate G4)
- **Decision:** Audited all AI assistance across 18 prompts; documented 3 real case studies of AI limitations, manual corrections, and reflections on vibe coding in `paper/ai_provenance_report.md`.
- **Reason:** Fulfills responsible AI compliance and research transparency standards.
- **Evidence / source:** `paper/ai_provenance_report.md`, `ai_assistance_log.md`.
- **Status:** `[VERIFIED]`.
- **Next action:** Submit complete repository and demonstration walkthrough.
