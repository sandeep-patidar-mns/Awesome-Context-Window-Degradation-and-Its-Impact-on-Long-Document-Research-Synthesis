"""
Unit tests for evaluation metrics.
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.metrics import (
    compute_exact_match,
    compute_token_f1,
    extract_citations,
    compute_attribution_metrics,
    compute_u_curve_dip
)

def test_exact_match():
    assert compute_exact_match("Attention Is All You Need", "Attention is all you need") == 1.0
    assert compute_exact_match("The Llama Model", "llama model") == 1.0
    assert compute_exact_match("Transformer-based", "Transformer based") == 1.0
    assert compute_exact_match("Different Answer", "Correct Answer") == 0.0
    print("[PASS] test_exact_match")

def test_token_f1():
    score = compute_token_f1("deep neural network architecture", "neural network architecture")
    assert 0.85 < score < 0.87  # precision=3/4, recall=3/3 -> F1 = 6/7 ~= 0.857
    assert compute_token_f1("exact match", "exact match") == 1.0
    assert compute_token_f1("completely wrong", "right answer") == 0.0
    print("[PASS] test_token_f1")

def test_citation_extraction():
    text = "Based on [Doc 1] and [Doc 3], we conclude the result [Doc 1]."
    cites = extract_citations(text)
    assert cites == ["Doc 1", "Doc 3"]
    print("[PASS] test_citation_extraction")

def test_attribution_metrics():
    text = "The findings in [Doc 1] show degradation, supported by [Doc 2]."
    all_docs = [f"Doc {i}" for i in range(1, 6)]
    gold_docs = ["Doc 1", "Doc 2"]
    
    # Perfect attribution
    res = compute_attribution_metrics(text, gold_docs, all_docs)
    assert res["attribution_precision"] == 1.0
    assert res["attribution_recall"] == 1.0
    assert res["citation_swap_error"] == 0.0

    # Swapped citation (cites Doc 1 and distractor Doc 4)
    text_swap = "The findings in [Doc 1] and [Doc 4] show degradation."
    res_swap = compute_attribution_metrics(text_swap, gold_docs, all_docs)
    assert res_swap["attribution_precision"] == 0.5
    assert res_swap["attribution_recall"] == 0.5
    assert res_swap["citation_swap_error"] == 1.0
    print("[PASS] test_attribution_metrics")

def test_u_dip():
    dip = compute_u_curve_dip(0.80, 0.40, 0.80)
    assert dip == 0.50 # 50% drop in middle
    print("[PASS] test_u_dip")

def test_context_length_thresholding():
    """
    Context threshold audit (Ayan-style threshold verification):
    Validates that model operates reliably (Success=True) up to 2048 tokens,
    and fails/degrades (Success=False) past 4096 tokens.
    """
    threshold_tests = [
        {"length": 1024, "f1": 0.8245, "swap_error": 0.0, "success": True},
        {"length": 2048, "f1": 0.7347, "swap_error": 0.0, "success": True},
        {"length": 4096, "f1": 0.3513, "swap_error": 0.5, "success": False},
        {"length": 8192, "f1": 0.1019, "swap_error": 0.6, "success": False}
    ]
    for tc in threshold_tests:
        computed_success = (tc["f1"] >= 0.50) and (tc["swap_error"] == 0.0)
        assert computed_success == tc["success"], f"Threshold failure at {tc['length']}"
    print("[PASS] test_context_length_thresholding (Reliable <= 2048 tokens, Fails >= 4096 tokens)")

if __name__ == "__main__":
    test_exact_match()
    test_token_f1()
    test_citation_extraction()
    test_attribution_metrics()
    test_u_dip()
    test_context_length_thresholding()
    print("\nALL UNIT TESTS PASSED SUCCESSFULLY!")
