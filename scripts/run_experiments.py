#!/usr/bin/env python3
"""
Main Experiment Runner for AITR Lab 02.
Coordinates data loading, context packing, inference, evaluation, and visualization.
"""

import os
import sys
import argparse
import pandas as pd
import numpy as np

# Ensure project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.data_loader import create_synthetic_multidoc_eval_corpus, MultiDocDataset
from src.context_packer import ContextPacker
from src.inference_engine import LongContextInferenceEngine
from src.evaluator import ExperimentEvaluator
from src.metrics import compute_u_curve_dip
from src.visualizer import plot_u_curve, plot_length_degradation_by_task, plot_attribution_errors

def main():
    parser = argparse.ArgumentParser(description="Run AITR Lab 02 Experiments")
    parser.add_argument("--model", type=str, default="Qwen/Qwen2.5-7B-Instruct", help="HuggingFace model ID")
    parser.add_argument("--lengths", nargs="+", type=int, default=[2048, 4096, 8192], help="Context token lengths")
    parser.add_argument("--positions", nargs="+", type=str, default=["beginning", "middle", "end"], help="Evidence positions")
    parser.add_argument("--num_instances", type=int, default=20, help="Number of instances per slice")
    parser.add_argument("--output_dir", type=str, default="results", help="Directory for output files")
    parser.add_argument("--data_path", type=str, default="data/frozen_test_instances.json", help="Path to frozen dataset")
    args = parser.parse_args()

    print("=" * 70)
    print("AITR Lab 02: Context-Window Degradation Experimental Evaluation")
    print(f"Model ID       : {args.model}")
    print(f"Context Lengths: {args.lengths}")
    print(f"Positions      : {args.positions}")
    print(f"Instances/cell : {args.num_instances}")
    print(f"Output Dir     : {args.output_dir}")
    print("=" * 70)

    # 1. Dataset Acquisition & Validation
    if os.path.exists(args.data_path):
        print(f"[+] Loading existing dataset from: {args.data_path}")
        dataset = MultiDocDataset.load_json(args.data_path)
    else:
        print("[*] Generating frozen multi-document evaluation corpus...")
        dataset = create_synthetic_multidoc_eval_corpus()
        dataset.save_json(args.data_path)
        print(f"[+] Saved frozen dataset ({len(dataset)} items) to: {args.data_path}")

    # 2. Initialize Modules
    packer = ContextPacker(target_lengths=args.lengths)
    engine = LongContextInferenceEngine(model_name_or_path=args.model)
    engine.initialize_model()

    evaluator = ExperimentEvaluator(
        dataset=dataset,
        packer=packer,
        inference_engine=engine,
        output_dir=args.output_dir
    )

    # 3. Execute Experiment Matrix
    print("\n[*] Executing full factorial evaluation matrix...")
    df_results = evaluator.run_evaluation_slice(
        context_lengths=args.lengths,
        positions=args.positions,
        num_instances=args.num_instances,
        structured=True
    )

    # 4. Generate Figures
    print("\n[*] Rendering publication-quality figures...")
    plot_u_curve(df_results, output_dir=args.output_dir)
    plot_length_degradation_by_task(df_results, output_dir=args.output_dir)
    plot_attribution_errors(df_results, output_dir=args.output_dir)

    # 5. Compute Quantitative Metrics
    print("\n" + "=" * 70)
    print("EXPERIMENTAL RESULTS SUMMARY & FINDINGS")
    print("=" * 70)

    beg_f1 = df_results[df_results["position"] == "beginning"]["token_f1"].mean()
    mid_f1 = df_results[df_results["position"] == "middle"]["token_f1"].mean()
    end_f1 = df_results[df_results["position"] == "end"]["token_f1"].mean()
    dip_ratio = compute_u_curve_dip(beg_f1, mid_f1, end_f1)

    print(f"Beginning Mean F1  : {beg_f1:.4f}")
    print(f"Middle Mean F1     : {mid_f1:.4f}")
    print(f"End Mean F1        : {end_f1:.4f}")
    print(f"U-Curve Dip Ratio  : {dip_ratio:.4f} (Values < 1.0 indicate degradation)")

    # Linear degradation slope across log2(length)
    lengths = sorted(df_results["context_length"].unique())
    f1_by_len = [df_results[df_results["context_length"] == l]["token_f1"].mean() for l in lengths]
    if len(lengths) > 1:
        slope, _ = np.polyfit(np.log2(lengths), f1_by_len, 1)
        print(f"Degradation Slope  : {slope:.4f} F1 points per context doubling")

    swap_rate = df_results["citation_swap_error"].mean()
    att_prec = df_results["attribution_precision"].mean()
    att_rec = df_results["attribution_recall"].mean()
    print(f"Attribution Prec   : {att_prec:.4f}")
    print(f"Attribution Recall : {att_rec:.4f}")
    print(f"Citation Swap Rate : {swap_rate:.4f}")
    print("=" * 70)

    # Save log report
    log_file = os.path.join(args.output_dir, "experiment_run_log.txt")
    with open(log_file, "w", encoding="utf-8") as f:
        f.write("AITR Lab 02 - Verified Experiment Run Log\n")
        f.write(f"Total instances evaluated: {len(df_results)}\n")
        f.write(f"Beginning F1: {beg_f1:.4f}\n")
        f.write(f"Middle F1: {mid_f1:.4f}\n")
        f.write(f"End F1: {end_f1:.4f}\n")
        f.write(f"Dip Ratio: {dip_ratio:.4f}\n")
        f.write(f"Attribution Recall: {att_rec:.4f}\n")
        f.write(f"Citation Swap Error Rate: {swap_rate:.4f}\n")
    print(f"[+] Run log written to: {log_file}")

if __name__ == "__main__":
    main()
