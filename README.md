# Quantifying Context-Window Degradation in Multi-Document Research Synthesis

**Author**: Sandeep Patidar (MNS2026001)  
**Affiliation**: Postgraduate Student Research  
**Topic Continuity**: Second Paper (Implementation & Experimental Study) extending my previous ACM CSUR Literature Review on *Context-Window Degradation and Its Impact on Long-Document Research Synthesis*  
**Repository**: [sandeep-patidar-mns/Awesome-Context-Window-Degradation-and-Its-Impact-on-Long-Document-Research-Synthesis](https://github.com/sandeep-patidar-mns/Awesome-Context-Window-Degradation-and-Its-Impact-on-Long-Document-Research-Synthesis)

---

## 1. Why I Did This Research
In my first paper, I conducted a literature review analyzing 20 papers on context-window degradation. A consistent pattern emerged: while frontier LLMs advertise context windows reaching 32k, 128k, or even 1M tokens, they often fail to retrieve or use information in the middle of long inputs (*Lost in the Middle*, Liu et al., 2024), and performance degrades purely from context length scaling even when the gold passage is present (*Du et al., Findings of EMNLP 2025*).

However, almost all existing benchmarks use **single-passage fact lookup** (such as needle-in-a-haystack or synthetic key-value retrieval). In real academic work—like writing a literature review or synthesizing research—we don't just look up one fact. We have to:
1. Connect findings across multiple distinct papers (multi-hop relational reasoning).
2. Correctly cite which paper said what, without mixing up citations.
3. Deal with papers structured with headings, abstracts, and methodologies.

I wanted to find out:
- Does multi-hop synthesis degrade faster than single-fact extraction as context length grows?
- When evidence is placed in the middle, does the model simply lose accuracy, or does it start swapping citations and attributing findings to the wrong paper?
- Can simple structural formatting (like Markdown headers) prevent this degradation without needing fine-tuning?

---

## 2. Key Findings & Honest Outcomes

Across 900 controlled experimental trials on a frozen multi-document benchmark, here is what the data showed:

1. **Multi-Hop Relational Synthesis Drops Faster**:
   - Single-hop fact extraction in the middle drops from **0.414 F1** (2k context) to **0.280 F1** (8k context), a degradation slope of $\beta = -0.0669$ per context doubling.
   - Multi-hop cross-document synthesis in the middle drops from **0.277 F1** (2k context) down to **0.102 F1** (8k context), a degradation slope of $\beta = -0.0875$.
   - **Conclusion**: Multi-document synthesis is **30.8% more fragile** to context expansion because self-attention must bridge distant document chunks across a sea of distractors.

2. **The "Citation Swap" Failure Mode**:
   - In multi-hop synthesis, when evidence is in the beginning, the citation swap error rate is **20.0%**.
   - When evidence is in the middle, the citation swap rate jumps to **60.0%**.
   - **Crucial insight**: The model often still generates a plausible factual term, but attributes it to a completely different distractor paper. Citation fidelity degrades more aggressively than surface entity recall.

3. **Structural Formatting Helps, But Has Clear Limits**:
   - Explicit Markdown tags (`[Doc X] Title: ... Content: ...`) recovered **+0.082 F1** in the middle at 2048 tokens and prevented total failure at 8192 tokens (**0.102 F1** vs **0.026 F1** unformatted).
   - **Negative finding / Honest limitation**: An F1 of 0.102 at 8192 tokens is still not reliable enough for fully automated review generation. Structure helps, but it is not a silver bullet. Hierarchical section retrieval remains necessary for long-document tasks.

---

## 3. Project Structure
```
├── paper/
│   ├── main.tex                   # Complete ACM CSUR-style manuscript
│   ├── references.bib             # 20 verified literature references
│   ├── peer_review_report.md      # Technical peer-review and revision matrix
│   ├── research_brief_G1.md       # Gate G1 One-Page Research Brief
│   ├── ai_provenance_report.md    # Transparent AI assistance audit
│   └── review_paper/              # Archived source of Paper 1 (Literature Review)
├── results/
│   ├── baseline_reproduction_results.csv # Liu et al. (2024) reproduction
│   ├── comparative_study_results.csv     # 900 trials raw output
│   ├── comparative_summary.csv           # Aggregated summary table
│   ├── fig_u_curve.svg                   # U-Curve positional plot
│   ├── fig_length_degradation.svg        # Degradation slopes plot
│   └── fig_attribution_errors.svg        # Citation swap error plot
├── src/
│   ├── metrics.py                 # Token F1, Exact Match, Attribution Precision/Recall, Dip Ratio
│   ├── data_loader.py             # Schema assertion & multi-doc dataset container
│   ├── context_packer.py          # Positional injection & distractor scaling
│   ├── inference_engine.py        # 4-bit quantized model loader & greedy generator
│   ├── evaluator.py               # Evaluation grid runner
│   └── visualizer.py              # Publication vector plot generator
├── scripts/
│   ├── run_baseline_validation.ps1# Baseline reproduction runner
│   ├── run_comparative_study.ps1  # Comparative study runner (900 trials)
│   ├── generate_plots.ps1         # SVG figure generator
│   └── verify_environment.py      # Diagnostic script
├── notebooks/
│   └── AITR_Lab02_Colab_Runner.ipynb # Executable Google Colab notebook
├── configs/
│   ├── dataset_baseline_validation.md
│   └── frozen_experiment_blueprint.md
├── research_decisions.md          # Chronological log of research decisions & evidence
├── baseline_validation.md         # Baseline verification report
├── ai_assistance_log.md           # Authentic human-AI collaboration & debugging log
└── DEMO_WALKTHROUGH.md            # 5-minute technical viva guide
```

---

## 4. How to Reproduce Everything

### Quick Reproduction on Local Machine
All evaluation scripts use fixed random seeds (`SEED = 42, 101`):

1. **Baseline Reproduction** (Liu et al., 2024 Single-Hop):
   ```powershell
   powershell -NoProfile -ExecutionPolicy Bypass -File scripts/run_baseline_validation.ps1
   ```
   *Expected output*: prints summary showing middle-position F1 drops from ~0.74 to ~0.41 (U-curve dip ratio 0.595).

2. **Full Comparative Study** (900 trials):
   ```powershell
   powershell -NoProfile -ExecutionPolicy Bypass -File scripts/run_comparative_study.ps1
   ```
   *Expected output*: generates `results/comparative_study_results.csv` and `results/comparative_summary.csv`.

3. **Render Figures**:
   ```powershell
   powershell -NoProfile -ExecutionPolicy Bypass -File scripts/generate_plots.ps1
   ```
   *Expected output*: creates `results/fig_u_curve.svg`, `results/fig_length_degradation.svg`, and `results/fig_attribution_errors.svg`.

### GPU Execution on Google Colab
Open [`notebooks/AITR_Lab02_Colab_Runner.ipynb`](notebooks/AITR_Lab02_Colab_Runner.ipynb) in Google Colab (Free T4 or L4 GPU) to run full `Qwen/Qwen2.5-7B-Instruct` 4-bit quantized inference.

---

## 5. Reflections on AI Assistance & Vibe Coding
In accordance with course integrity policies:
- AI (Antigravity/Gemini) was used as a pair programming assistant for generating script boilerplate and formatting LaTeX tables.
- **Human judgment and verification were critical**:
  - The AI initially proposed PowerShell code using `[Math]::Log2`, which crashed because Windows PowerShell 5.1 runs on .NET Framework 4.8. I debugged the runtime error and refactored it to `[math]::Log($x, 2)`.
  - The AI's initial metric definition conflated citation over-generation with true citation swapping; I corrected the error taxonomy.
  - The AI initially drafted overly broad claims that "all long-context LLMs fail"; I narrowed this to decoder-only RoPE architectures based on Veseli et al. (2025).
- All decisions, failures, and manual corrections are documented in [`paper/ai_provenance_report.md`](paper/ai_provenance_report.md) and [`research_decisions.md`](research_decisions.md).

---

## 6. Citation
```bibtex
@inproceedings{patidar2026contextdegradation,
  author    = {Sandeep Patidar},
  title     = {Quantifying Context-Window Degradation in Multi-Document Academic Research Synthesis: An Empirical Investigation of Positional Bias, Relational Complexity, and Source Attribution},
  booktitle = {AITR Research Studies in Computing},
  year      = {2026}
}
```
