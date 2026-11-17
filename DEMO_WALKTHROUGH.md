# 5-Minute Technical Viva & Demonstration Walkthrough (Item E)

**Student Enrollment**: MNS2026001  
**Project**: Quantifying Context-Window Degradation in Multi-Document Academic Research Synthesis  
**Target Duration**: 5 Minutes  

---

## 1. Minute-by-Minute Presentation Plan

### Minute 0:00 – 1:00 | Research Continuity & Literature-Grounded Question
* **What to say**:  
  *"My first paper mapped the long-context landscape across 20 papers, establishing that nominal context windows do not guarantee reliable effective use. Most existing benchmarks only test single-passage retrieval. For my second paper, I investigated multi-document research synthesis—where evidence is distributed across distinct papers and requires both joint synthesis and source attribution without citation hallucination."*
* **What to show**:  
  Point to [`paper/research_brief_G1.md`](paper/research_brief_G1.md) and show the three research questions (RQ1: Relational Complexity Slope, RQ2: Positional Citation Swapping, RQ3: Structural Formatting Ablation).

### Minute 1:00 – 2:00 | Baseline Reproduction & Audit (Gate G2)
* **What to say**:  
  *"I reproduced the positional degradation protocol of Liu et al. (2024) ('Lost in the Middle') on single-hop fact extraction across 2k, 4k, and 8k contexts. In my verified baseline run, performance dropped by 43.9% in the middle position, yielding a U-curve dip ratio of 0.5950."*
* **What to show**:  
  Open [`baseline_validation.md`](baseline_validation.md) and show the exact reproduction numbers in Table 2.

### Minute 2:00 – 3:30 | Core Experimental Findings (Gate G3)
* **What to say**:  
  *"I then conducted a controlled comparative study with 900 evaluation trials across 50 frozen instances. We discovered three core findings:*  
  *1. Multi-hop relational synthesis degrades 30.8% faster ($\beta = -0.0875$) than single-hop fact extraction ($\beta = -0.0669$).*  
  *2. In the middle position, citation swap errors surge from 20% to 60%. The model often extracts the right term but attributes it to an adjacent distractor paper.*  
  *3. Explicit Markdown document boundaries act as anchor tokens, recovering +0.0823 F1 in the middle and preventing complete collapse at 8k tokens."*
* **What to show**:  
  Display [`results/fig_u_curve.svg`](results/fig_u_curve.svg) and [`results/fig_attribution_errors.svg`](results/fig_attribution_errors.svg).

### Minute 3:30 – 4:15 | Human–AI Collaboration & Debugging Case Study
* **What to say**:  
  *"I maintained an active AI audit log. When running the baseline script, an API failure occurred because PowerShell 5.1 runs on .NET Framework 4.8 which lacks `Math.Log2`. I diagnosed the runtime exception and refactored the expression to `[math]::Log($x, 2)`, restoring clean execution. I also corrected the AI's metric ambiguity regarding citation swapping vs. citation over-generation."*
* **What to show**:  
  Point to Section 3 of [`paper/ai_provenance_report.md`](paper/ai_provenance_report.md).

### Minute 4:15 – 5:00 | Live Verification Rerun (Ready if requested by examiner)
* **What to execute live**:
  ```powershell
  powershell -NoProfile -ExecutionPolicy Bypass -File scripts/run_baseline_validation.ps1
  ```
* Shows the summary output printing F1 scores and citation swap percentages in under 5 seconds.
