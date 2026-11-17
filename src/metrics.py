"""
Evaluation Metrics Module for AITR Lab 02.
Computes Token F1, Exact Match (EM), Source Attribution Precision/Recall,
Citation Swap Rate, and Degradation Slopes.
"""

import re
import string
from collections import Counter
from typing import List, Dict, Tuple, Set

def normalize_text(text: str) -> str:
    """Lower text and remove punctuation, articles and extra whitespace."""
    def remove_articles(text):
        return re.sub(r'\b(a|an|the)\b', ' ', text)

    def white_space_fix(text):
        return ' '.join(text.split())

    def remove_punc(text):
        exclude = set(string.punctuation)
        return ''.join(ch for ch in text if ch not in exclude)

    def lower(text):
        return text.lower()

    return white_space_fix(remove_articles(remove_punc(lower(text))))

def compute_exact_match(prediction: str, ground_truth: str) -> float:
    """Compute binary exact match (1.0 or 0.0) after text normalization."""
    return float(normalize_text(prediction) == normalize_text(ground_truth))

def compute_token_f1(prediction: str, ground_truth: str) -> float:
    """Compute token-level F1 score between prediction and ground truth."""
    pred_tokens = normalize_text(prediction).split()
    gt_tokens = normalize_text(ground_truth).split()

    if len(pred_tokens) == 0 or len(gt_tokens) == 0:
        return float(pred_tokens == gt_tokens)

    common = Counter(pred_tokens) & Counter(gt_tokens)
    num_same = sum(common.values())

    if num_same == 0:
        return 0.0

    precision = 1.0 * num_same / len(pred_tokens)
    recall = 1.0 * num_same / len(gt_tokens)
    f1 = (2 * precision * recall) / (precision + recall)
    return f1

def extract_citations(text: str) -> List[str]:
    """
    Extract cited document identifiers from model text, e.g., '[Doc 1]', '[Doc 2]'.
    Returns normalized IDs like ['Doc 1', 'Doc 2'].
    """
    matches = re.findall(r'\[(Doc\s*\d+)\]', text, re.IGNORECASE)
    normalized = []
    for m in matches:
        # Standardize to 'Doc X'
        parts = m.split()
        if len(parts) == 2:
            normalized.append(f"Doc {parts[1]}")
    return list(dict.fromkeys(normalized)) # preserve order, remove duplicates

def compute_attribution_metrics(
    predicted_text: str, 
    gold_doc_ids: List[str], 
    all_context_doc_ids: List[str]
) -> Dict[str, float]:
    """
    Evaluate source attribution fidelity.
    - precision: proportion of cited docs that are genuinely gold
    - recall: proportion of gold docs that were cited
    - swap_error: whether any cited doc is a distractor
    """
    predicted_cites = set(extract_citations(predicted_text))
    gold_set = set(gold_doc_ids)
    distractor_set = set(all_context_doc_ids) - gold_set

    if not predicted_cites:
        return {
            "attribution_precision": 0.0,
            "attribution_recall": 0.0,
            "attribution_f1": 0.0,
            "citation_swap_error": 0.0,
            "citation_count": 0
        }

    true_positives = len(predicted_cites & gold_set)
    precision = true_positives / len(predicted_cites) if predicted_cites else 0.0
    recall = true_positives / len(gold_set) if gold_set else 0.0
    
    if precision + recall > 0:
        f1 = 2 * (precision * recall) / (precision + recall)
    else:
        f1 = 0.0

    # Citation swap error: cited at least one distractor document
    swap_error = 1.0 if len(predicted_cites & distractor_set) > 0 else 0.0

    return {
        "attribution_precision": float(precision),
        "attribution_recall": float(recall),
        "attribution_f1": float(f1),
        "citation_swap_error": float(swap_error),
        "citation_count": len(predicted_cites)
    }

def compute_u_curve_dip(
    beginning_score: float, 
    middle_score: float, 
    end_score: float
) -> float:
    """
    Measures the positional U-curve degradation ratio:
    Dip = Middle / (0.5 * (Beginning + End))
    Dip < 1.0 indicates Lost-in-the-Middle degradation.
    """
    edge_avg = 0.5 * (beginning_score + end_score)
    if edge_avg == 0:
        return 1.0
    return middle_score / edge_avg
