"""
Context Packer Module for Context-Window Degradation Experiments.
Reproduces Liu et al. (2024) positional injection and Du et al. (2025) distractor scaling.
"""

import math
from typing import List, Dict, Any, Tuple

class ContextPacker:
    """
    Synthesizes multi-document evaluation contexts with controlled:
    1. Gold document position (Beginning [0-25%], Middle [25-75%], End [75-100%])
    2. Context length scaling (padding with distractor tokens to target length)
    3. Structural tagging (Structured Markdown Tags vs Raw Text Concatenation)
    """

    def __init__(self, target_lengths: List[int] = [2048, 4096, 8192, 16384]):
        self.target_lengths = target_lengths

    def approximate_tokens(self, text: str) -> int:
        """Rough token approximation: ~1.3 tokens per whitespace word for English scientific text."""
        return int(len(text.split()) * 1.3) + 1

    def format_document(self, doc_id: str, title: str, text: str, structured: bool = True) -> str:
        """Format an individual document block."""
        if structured:
            return f"[{doc_id}] Title: {title}\nContent: {text}\n"
        else:
            return f"{title}. {text}\n"

    def pack_context(
        self,
        gold_docs: List[Dict[str, str]],
        distractor_docs: List[Dict[str, str]],
        position: str = "middle",
        target_token_length: int = 2048,
        structured: bool = True
    ) -> Tuple[str, List[str], List[str]]:
        """
        Packs documents into a unified context string.
        Returns:
            context_string: formatted context prompt
            gold_doc_ids: assigned tags for gold documents (e.g. ['Doc 5', 'Doc 6'])
            all_doc_ids: list of all assigned document tags
        """
        # Determine number of distractor repetitions needed to hit approximate target length
        base_distractor_tokens = sum(self.approximate_tokens(d["text"]) for d in distractor_docs)
        if base_distractor_tokens == 0:
            base_distractor_tokens = 1
            
        multiplier = max(1, math.ceil(target_token_length / (base_distractor_tokens + 500)))
        expanded_distractors = (distractor_docs * multiplier)
        
        # Total documents = len(expanded_distractors) + len(gold_docs)
        total_docs = len(expanded_distractors) + len(gold_docs)
        
        # Calculate insertion index for gold documents
        if position == "beginning":
            insert_idx = 0
        elif position == "end":
            insert_idx = len(expanded_distractors)
        else: # "middle"
            insert_idx = max(0, len(expanded_distractors) // 2)

        # Assemble document list
        ordered_docs = []
        gold_indices = set()
        
        for i in range(insert_idx):
            ordered_docs.append(expanded_distractors[i])
            
        for g_idx, g_doc in enumerate(gold_docs):
            gold_indices.add(len(ordered_docs))
            ordered_docs.append(g_doc)
            
        for i in range(insert_idx, len(expanded_distractors)):
            ordered_docs.append(expanded_distractors[i])

        # Format into context string and assign document IDs
        formatted_blocks = []
        all_doc_ids = []
        gold_doc_ids = []
        
        current_tokens = 0
        for idx, doc in enumerate(ordered_docs):
            doc_tag = f"Doc {idx + 1}"
            all_doc_ids.append(doc_tag)
            if idx in gold_indices:
                gold_doc_ids.append(doc_tag)
                
            block = self.format_document(doc_tag, doc["title"], doc["text"], structured=structured)
            formatted_blocks.append(block)
            current_tokens += self.approximate_tokens(block)
            
            # If we exceeded target length and have included all gold docs, stop
            if current_tokens >= target_token_length and len(gold_doc_ids) == len(gold_docs):
                break

        context_string = "\n".join(formatted_blocks)
        return context_string, gold_doc_ids, all_doc_ids
