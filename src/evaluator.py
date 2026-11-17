"""
Evaluator Module for Context Degradation Experiments.
Executes the evaluation matrix, tracks metrics, and exports traceable CSV results.
"""

import os
import time
import json
import pandas as pd
from typing import List, Dict, Any
from src.context_packer import ContextPacker
from src.metrics import (
    compute_exact_match,
    compute_token_f1,
    compute_attribution_metrics,
    compute_u_curve_dip
)

class ExperimentEvaluator:
    """
    Executes reproducible benchmark grids, collects genuine output logs,
    and calculates statistical summaries.
    """

    def __init__(
        self,
        dataset,
        packer: ContextPacker,
        inference_engine,
        output_dir: str = "results"
    ):
        self.dataset = dataset
        self.packer = packer
        self.engine = inference_engine
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def run_evaluation_slice(
        self,
        context_lengths: List[int] = [2048, 4096, 8192],
        positions: List[str] = ["beginning", "middle", "end"],
        num_instances: int = 20,
        structured: bool = True
    ) -> pd.DataFrame:
        """
        Runs an evaluation slice over the specified grid.
        Returns a DataFrame containing per-instance results.
        """
        records = []
        instances = self.dataset.instances[:num_instances]
        
        total_runs = len(instances) * len(context_lengths) * len(positions)
        print(f"[*] Starting evaluation: {total_runs} total runs across {len(instances)} instances.")
        
        start_time = time.time()
        completed = 0
        
        for c_len in context_lengths:
            for pos in positions:
                for inst in instances:
                    context_str, gold_ids, all_ids = self.packer.pack_context(
                        gold_docs=inst["gold_docs"],
                        distractor_docs=inst["distractor_docs"],
                        position=pos,
                        target_token_length=c_len,
                        structured=structured
                    )
                    
                    # Run inference
                    t0 = time.time()
                    prediction = self.engine.generate(context_str, inst["question"])
                    lat = time.time() - t0
                    
                    # Compute metrics
                    em = compute_exact_match(prediction, inst["answer"])
                    f1 = compute_token_f1(prediction, inst["answer"])
                    att_metrics = compute_attribution_metrics(prediction, gold_ids, all_ids)
                    
                    record = {
                        "instance_id": inst["id"],
                        "task_type": inst["type"],
                        "context_length": c_len,
                        "position": pos,
                        "structured": structured,
                        "question": inst["question"],
                        "gold_answer": inst["answer"],
                        "prediction": prediction,
                        "exact_match": em,
                        "token_f1": f1,
                        "attribution_precision": att_metrics["attribution_precision"],
                        "attribution_recall": att_metrics["attribution_recall"],
                        "citation_swap_error": att_metrics["citation_swap_error"],
                        "latency_sec": round(lat, 4)
                    }
                    records.append(record)
                    completed += 1
                    
        elapsed = time.time() - start_time
        print(f"[+] Evaluation completed in {elapsed:.2f} seconds.")
        
        df = pd.DataFrame(records)
        raw_csv_path = os.path.join(self.output_dir, "raw_eval_results.csv")
        df.to_csv(raw_csv_path, index=False)
        print(f"[+] Raw results saved to: {raw_csv_path}")
        
        # Compute and export summary table
        summary = df.groupby(["context_length", "position", "task_type"]).agg({
            "token_f1": ["mean", "std"],
            "exact_match": "mean",
            "attribution_precision": "mean",
            "attribution_recall": "mean",
            "citation_swap_error": "mean"
        }).reset_index()
        
        summary_csv_path = os.path.join(self.output_dir, "summary_metrics.csv")
        summary.to_csv(summary_csv_path, index=False)
        print(f"[+] Summary metrics saved to: {summary_csv_path}")
        
        return df
