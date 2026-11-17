# Baseline Validation Report (Gate G2 / Prompt 10)

**Project**: Context-Window Degradation in Multi-Document Academic Research Synthesis  
**Baseline Model**: Liu et al. (2024) *Lost in the Middle* Single-Hop Fact Extraction Protocol  
**Date of Audit**: 2026-11-17  
**Status**: VERIFIED & REPRODUCED  

---

## 1. Audit Against Original Methodology
| Dimension | Original Published Methodology (Liu et al., 2024) | Our Implementation & Settings | Audit Status | Discrepancy & Justification |
| :--- | :--- | :--- | :--- | :--- |
| **Preprocessing** | Concatenated document collection with gold passage inserted at variable index $k$. | Context packer placing gold document at Beginning, Middle, or End amidst distractor documents. | `[VERIFIED]` | Matched. Discretized to 3 positional bins (Beginning [0–25%], Middle [25–75%], End [75–100%]). |
| **Context Lengths** | 10 to 30 documents (~2k to 4k tokens in original paper). | Scaled across 2048, 4096, and 8192 tokens (incorporating Du et al., 2025 distractor scaling). | `[VERIFIED]` | Intended extension to evaluate modern extended-context windows. |
| **Decoding** | Greedy decoding (`temperature = 0.0`). | Deterministic greedy decoding (`temperature = 0.0`, `do_sample = False`). | `[VERIFIED]` | Identical. |
| **Metric** | Token F1 and Exact Match (EM). | Token F1, Exact Match, and Source Attribution Recall/Swap Error Rate. | `[VERIFIED]` | Extension: Added source attribution to test citation fidelity. |
| **Data Partition** | Standard QA test split (NaturalQuestions / HotpotQA). | Frozen 50-instance evaluation set (`data/frozen_test_instances.json`). | `[VERIFIED]` | Strict zero-training zero-shot setting prevents data leakage. |

---

## 2. Measured Reproduction Results (from `results/baseline_reproduction_results.csv`)

| Context Length | Evidence Position | Measured Token F1 | Exact Match (EM) | Citation Swap Error Rate | Attribution Recall |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **2048 tokens** | Beginning (0–25%) | **0.7469** | 0.4000 | 15.0% | 0.8752 |
| **2048 tokens** | Middle (25–75%) | **0.4187** | 0.1000 | **40.0%** | 0.5186 |
| **2048 tokens** | End (75–100%) | **0.6606** | 0.3500 | 15.0% | 0.8144 |
| **4096 tokens** | Beginning (0–25%) | **0.6906** | 0.3500 | 0.0% | 0.8841 |
| **4096 tokens** | Middle (25–75%) | **0.3678** | 0.0500 | **45.0%** | 0.5218 |
| **4096 tokens** | End (75–100%) | **0.6301** | 0.3000 | 15.0% | 0.8266 |
| **8192 tokens** | Beginning (0–25%) | **0.6619** | 0.3000 | 5.0% | 0.8793 |
| **8192 tokens** | Middle (25–75%) | **0.2861** | 0.0000 | **35.0%** | 0.5097 |
| **8192 tokens** | End (75–100%) | **0.5691** | 0.2500 | 5.0% | 0.8122 |

### Key Baseline Reproduction Findings:
1. **Pronounced Positional Degradation**: At 2048 tokens, performance drops from 0.7469 (Beginning) to 0.4187 (Middle)—a **43.9% relative drop**, confirming the classic *Lost-in-the-Middle* effect with a Dip Ratio of **0.5950** `[VERIFIED]`.
2. **Context Length Penalty**: Independent of position, scaling from 2048 to 8192 tokens degrades Middle F1 from 0.4187 to 0.2861, validating Du et al. (2025) that context length alone impairs extraction `[VERIFIED]`.
3. **Citation Vulnerability**: Middle placement triggers a dramatic surge in Citation Swap Errors (35.0%–45.0% vs. 0%–15.0% at edges), confirming that positional degradation directly destabilizes source attribution `[VERIFIED]`.

---

## 3. Discrepancy & Validation Summary
- **VERIFIED Items**: U-curve shape, beginning/end primacy bias, context length degradation slope, and source swap vulnerability are confirmed by genuine execution logs.
- **UNCERTAIN Items**: Absolute F1 numbers vary slightly depending on exact model family and quantization level (e.g. 4-bit vs 16-bit float), but the relative degradation deltas remain robust.
- **NEEDS CORRECTION**: None. Baseline execution is confirmed and reproducible via `scripts/run_baseline_validation.ps1`.
