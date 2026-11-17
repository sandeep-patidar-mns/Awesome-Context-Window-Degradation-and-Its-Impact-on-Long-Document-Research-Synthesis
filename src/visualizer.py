"""
Visualizer Module for Context Degradation Experiments.
Produces publication-quality plots (PDF and PNG) matching ACM/IEEE formatting standards.
"""

import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def setup_plot_style():
    """Sets standard academic styling for figures."""
    plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
    plt.rcParams.update({
        'font.size': 11,
        'axes.labelsize': 12,
        'axes.titlesize': 13,
        'xtick.labelsize': 11,
        'ytick.labelsize': 11,
        'legend.fontsize': 10,
        'figure.titlesize': 14,
        'lines.linewidth': 2.0,
        'lines.markersize': 7
    })

def plot_u_curve(df: pd.DataFrame, output_dir: str = "results"):
    """
    Plots the positional U-curve (Token F1 vs Position) across different context lengths.
    """
    setup_plot_style()
    fig, ax = plt.subplots(figsize=(7, 4.5))
    
    positions = ["beginning", "middle", "end"]
    context_lengths = sorted(df["context_length"].unique())
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]
    
    for idx, c_len in enumerate(context_lengths):
        sub_df = df[df["context_length"] == c_len]
        means = [sub_df[sub_df["position"] == p]["token_f1"].mean() for p in positions]
        stds = [sub_df[sub_df["position"] == p]["token_f1"].std() / np.sqrt(max(1, len(sub_df[sub_df["position"] == p]))) for p in positions]
        
        c = colors[idx % len(colors)]
        ax.errorbar(
            ["Beginning\n(0-25%)", "Middle\n(25-75%)", "End\n(75-100%)"],
            means,
            yerr=stds,
            marker='o',
            label=f"{c_len} tokens",
            color=c,
            capsize=4
        )
        
    ax.set_xlabel("Relative Gold Evidence Position")
    ax.set_ylabel("Answer Correctness (Token F1)")
    ax.set_title("Positional Degradation ('Lost in the Middle') Across Context Lengths")
    ax.set_ylim(-0.05, 1.05)
    ax.legend(title="Context Window", loc="lower right", frameon=True)
    plt.tight_layout()
    
    png_path = os.path.join(output_dir, "fig_u_curve.png")
    pdf_path = os.path.join(output_dir, "fig_u_curve.pdf")
    fig.savefig(png_path, dpi=300)
    fig.savefig(pdf_path)
    plt.close(fig)
    print(f"[+] U-curve plot saved to: {png_path} and {pdf_path}")

def plot_length_degradation_by_task(df: pd.DataFrame, output_dir: str = "results"):
    """
    Plots context length degradation comparing Single-Hop vs Multi-Hop synthesis.
    """
    setup_plot_style()
    fig, ax = plt.subplots(figsize=(7, 4.5))
    
    task_types = df["task_type"].unique()
    c_lengths = sorted(df["context_length"].unique())
    styles = {"single_hop_extraction": ("#1f77b4", "s", "--", "Single-Hop Fact Extraction"),
              "multi_hop_synthesis": ("#d62728", "^", "-", "Multi-Hop Cross-Doc Synthesis")}
    
    for task in task_types:
        color, marker, lstyle, label = styles.get(task, ("black", "o", "-", task))
        sub_df = df[df["task_type"] == task]
        means = [sub_df[sub_df["context_length"] == l]["token_f1"].mean() for l in c_lengths]
        
        ax.plot(
            [str(l) for l in c_lengths],
            means,
            color=color,
            marker=marker,
            linestyle=lstyle,
            label=label
        )
        
    ax.set_xlabel("Nominal Context Length (Tokens)")
    ax.set_ylabel("Mean Token F1 Score")
    ax.set_title("Context Length Degradation: Single-Hop vs. Multi-Hop Synthesis")
    ax.set_ylim(-0.05, 1.05)
    ax.legend(loc="upper right", frameon=True)
    plt.tight_layout()
    
    png_path = os.path.join(output_dir, "fig_length_degradation.png")
    pdf_path = os.path.join(output_dir, "fig_length_degradation.pdf")
    fig.savefig(png_path, dpi=300)
    fig.savefig(pdf_path)
    plt.close(fig)
    print(f"[+] Length degradation plot saved to: {png_path} and {pdf_path}")

def plot_attribution_errors(df: pd.DataFrame, output_dir: str = "results"):
    """
    Plots Citation Swap Error Rate and Attribution Recall across positions.
    """
    setup_plot_style()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))
    
    positions = ["beginning", "middle", "end"]
    pos_labels = ["Beginning", "Middle", "End"]
    
    swap_rates = [df[df["position"] == p]["citation_swap_error"].mean() for p in positions]
    att_recalls = [df[df["position"] == p]["attribution_recall"].mean() for p in positions]
    
    ax1.bar(pos_labels, swap_rates, color="#d95f02", width=0.5, edgecolor="black")
    ax1.set_ylabel("Citation Swap Error Rate")
    ax1.set_xlabel("Relative Evidence Position")
    ax1.set_title("Citation Misattribution Rate by Position")
    ax1.set_ylim(0, 1.0)
    
    ax2.bar(pos_labels, att_recalls, color="#7570b3", width=0.5, edgecolor="black")
    ax2.set_ylabel("Attribution Recall")
    ax2.set_xlabel("Relative Evidence Position")
    ax2.set_title("Source Attribution Recall by Position")
    ax2.set_ylim(0, 1.0)
    
    plt.tight_layout()
    png_path = os.path.join(output_dir, "fig_attribution_errors.png")
    pdf_path = os.path.join(output_dir, "fig_attribution_errors.pdf")
    fig.savefig(png_path, dpi=300)
    fig.savefig(pdf_path)
    plt.close(fig)
    print(f"[+] Attribution error plot saved to: {png_path} and {pdf_path}")
