"""
Formatting Utilities
=====================

Output formatting for taste evaluations, including Rich console display
and structured export formats.
"""

from __future__ import annotations

from feynman_taste.core.taste_model import TasteEvaluation, AxisScore


def evaluation_to_dict(evaluation: TasteEvaluation) -> dict:
    """Convert a TasteEvaluation to a plain dict for JSON export."""
    return {
        "candidate": evaluation.candidate_description,
        "cutoff_year": evaluation.cutoff_year,
        "period": evaluation.active_period,
        "overall_score": round(evaluation.overall_score, 4),
        "overall_confidence": round(evaluation.overall_confidence, 4),
        "axes": [
            {
                "name": s.axis_name,
                "score": round(s.score, 4),
                "confidence": round(s.confidence, 4),
                "evidence_based": s.is_evidence_based,
                "evidence_ids": s.evidence_ids,
                "explanation": s.explanation,
            }
            for s in evaluation.axis_scores
        ],
        "summary": evaluation.summary,
        "evidence_summary": evaluation.evidence_summary,
        "inference_summary": evaluation.inference_summary,
        "caveats": evaluation.caveats,
    }


def score_bar(score: float, width: int = 20) -> str:
    """Create a text-based score bar: [-1.0 ████████░░░░░░░░░░░░ +1.0]"""
    normalized = (score + 1.0) / 2.0  # Map [-1, 1] to [0, 1]
    filled = int(normalized * width)
    empty = width - filled
    bar = "#" * filled + "-" * empty
    return f"[{bar}] {score:+.2f}"


def format_ranking(evaluations: list[TasteEvaluation]) -> str:
    """Format a ranked list of evaluations."""
    lines = ["RANKING BY EINSTEIN'S RESEARCH TASTE", "=" * 50, ""]
    for i, ev in enumerate(evaluations, 1):
        bar = score_bar(ev.overall_score)
        conf = f"(conf: {ev.overall_confidence:.2f})"
        lines.append(f"  #{i}  {bar} {conf}")
        lines.append(f"      {ev.candidate_description[:70]}")
        lines.append("")
    return "\n".join(lines)
