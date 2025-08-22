import argparse
import os
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

def add_box(ax, x, y, w, h, title, lines):
    box = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.3,rounding_size=0.2",
        linewidth=1.8,
        edgecolor="black",
        facecolor="white"
    )
    ax.add_patch(box)
    ax.text(x + 0.4, y + h - 0.6, title, fontsize=18, weight="bold", va="top", ha="left")
    start_y = y + h - 1.3
    line_h = 0.6
    for i, line in enumerate(lines):
        ax.text(x + 0.4, start_y - i * line_h, f"• {line}", fontsize=13, va="top", ha="left", wrap=True)

def add_arrow(ax, x1, y1, x2, y2, text=None):
    arr = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=20, linewidth=2)
    ax.add_patch(arr)
    if text:
        ax.text((x1 + x2) / 2, (y1 + y2) / 2 + 0.2, text, fontsize=12, ha="center", va="bottom")

def make_figure():
    fig_w, fig_h, dpi = 16, 9, 150
    fig = plt.figure(figsize=(fig_w, fig_h), dpi=dpi)
    ax = plt.gca()
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.axis("off")

    ax.text(0.5, 8.5, "Agentic AI for Local Governance & Laws",
            fontsize=24, weight="bold", ha="left", va="center")
    ax.text(0.5, 7.9, "Data → Agentic AI → Reasoning → Citizen Dashboard → Impact",
            fontsize=14, ha="left", va="center")

    W, H = 4.2, 4.5
    x1, y1 = 0.7, 2.3
    x2, y2 = 5.0, 2.3
    x3, y3 = 9.3, 2.3
    x4, y4 = 13.6, 2.3

    data_lines = [
        "Panchayat budgets & expenditures",
        "Legal codes & welfare schemes",
        "RTI & grievance portals",
        "Open data registries (land, roads)",
    ]
    agent_lines = [
        "Ingestion → cleaning → structuring",
        "Retrieval-augmented generation (RAG)",
        "Tool use: budget queries, eligibility checks",
        "Explainable, evidence-linked reasoning",
    ]
    dashboard_lines = [
        "Ask: \"Road spend last year in my district?\"",
        "Check: \"MNREGA eligibility for my household\"",
        "Know: \"Rights if land is acquired\"",
        "Multilingual + offline-first (SMS/IVR)",
    ]
    impact_lines = [
        "Transparent fund tracking",
        "Actionable rights awareness",
        "Lower grievance resolution time",
        "Data-driven policy decisions",
    ]

    add_box(ax, x1, y1, W, H, "Data Sources", data_lines)
    add_box(ax, x2, y2, W, H, "Agentic AI Layer", agent_lines)
    add_box(ax, x3, y3, W, H, "Citizen Dashboard", dashboard_lines)
    add_box(ax, x4, y4, W, H, "Impact", impact_lines)

    add_arrow(ax, x1 + W, y1 + H / 2, x2, y2 + H / 2, text="ETL + document loaders")
    add_arrow(ax, x2 + W, y2 + H / 2, x3, y3 + H / 2, text="Reasoned answers + citations")
    add_arrow(ax, x3 + W, y3 + H / 2, x4, y4 + H / 2, text="Insights & KPIs")

    plt.tight_layout()
    return fig

def main(outdir: str):
    os.makedirs(outdir, exist_ok=True)
    fig = make_figure()
    png_path = os.path.join(outdir, "agentic_ai_workflow.png")
    svg_path = os.path.join(outdir, "agentic_ai_workflow.svg")
    fig.savefig(png_path, bbox_inches="tight", dpi=150)
    fig.savefig(svg_path, bbox_inches="tight")
    print(f"Saved:\n- {png_path}\n- {svg_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Agentic AI workflow diagram")
    parser.add_argument("--outdir", default="outputs", help="Output directory (default: outputs)")
    args = parser.parse_args()
    main(args.outdir)
