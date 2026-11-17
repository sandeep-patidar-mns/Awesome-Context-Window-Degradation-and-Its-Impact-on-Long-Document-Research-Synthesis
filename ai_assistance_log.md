# Human-AI Collaboration and Research Integrity Log

**Project**: AITR Lab 02 — Context-Window Degradation in Long-Document Synthesis  
**Student Enrollment**: MNS2026001  
**Integrity Rule**: All AI assistance must be disclosed, verified, and grounded in authentic code execution and primary source literature. Hallucinated benchmarks, synthetic results presented as real, or unverified claims are strictly prohibited.

---

## AI Activity Audit Trail

| Entry | Phase / Step | Human Prompt / Task | AI Proposal / Action | Verification Method | Outcome & Human Decision |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **AI-001** | Phase I (Prompt 01) | Unpack uploaded review zip (`media_...zip`) and set up accountable research workspace. | Extracted LaTeX manuscript, verified all 20 cited works in `references.bib`, initialized project structure. | Checked file integrity, directory hierarchy, and matched claims against `main.tex`. | Approved directory setup and initialized `research_decisions.md` with 3-tier evidence labeling. |
| **AI-002** | Phase I (Prompt 02) | Extract 5 evidence-based research gaps from review manuscript and rank top 3 by feasibility. | Analyzed `main.tex` Section 8, mapped author-reported findings (Liu 2024, Du 2025, Veseli 2025, Modarressi 2025) to testable experiments. | Grounded in exact line citations of `main.tex`; distinguished literature findings from author inferences. | Gap Matrix recorded in `research_decisions.md`; ranked GAP-1, GAP-2, and GAP-3 for human selection. |
| **AI-003** | Phase II (Prompts 06–07) | Verify dataset, comparators, and freeze experimental blueprint before viewing results. | Designed reproducible architecture, metrics (Token F1, EM, Attribution P/R/Swap), deterministic seed controls (SEED=42). | Verified open licenses (HotpotQA CC BY-SA 4.0), confirmed zero-training zero-leakage design. | Blueprint frozen in `configs/frozen_experiment_blueprint.md`. |
| **AI-004** | Phase III (Prompt 11 Debugging) | Fix runtime execution error in PowerShell baseline runner: `[System.Math]::Log2` method not found. | Identified that PowerShell 5.1 runs on .NET Framework 4.8 (which lacks .NET Core's `Math.Log2`); refactored math expression to `[math]::Log($x, 2)`. | Re-executed script; confirmed clean exit with code 0 and valid CSV generation. | Baseline results generated and validated in `baseline_validation.md`. |
