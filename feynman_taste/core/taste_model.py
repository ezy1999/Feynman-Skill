"""
Taste Model Module
===================

Core module for scoring candidate scientific questions/theories against
Feynman's documented research taste axes.

The scoring pipeline:
1. Retrieve relevant historical evidence (via RAG)
2. Score each taste axis based on evidence alignment
3. Aggregate axis scores into an overall taste score
4. Generate explanations distinguishing evidence from inference
5. Apply temporal cutoff to prevent anachronism
"""

from __future__ import annotations

from pydantic import BaseModel, Field
import numpy as np

from feynman_taste.config.settings import (
    FEYNMAN_TASTE_AXES,
    FEYNMAN_PERIODS,
    TasteAxis,
    TemporalPeriod,
)
from feynman_taste.core.evidence import (
    EvidenceRecord,
    EvidenceStore,
    SourceType,
    ConfidenceLevel,
)


class AxisScore(BaseModel):
    """Score for a single taste axis with evidence and explanation."""
    axis_name: str
    score: float = Field(ge=-1.0, le=1.0, description="Score in [-1, 1]: positive=aligned")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence in this score")
    evidence_ids: list[str] = Field(
        default_factory=list,
        description="IDs of evidence records supporting this score"
    )
    explanation: str = ""
    is_evidence_based: bool = True  # False if score is model inference


class TasteEvaluation(BaseModel):
    """Complete evaluation of a candidate theory/question against Feynman's taste."""
    candidate_description: str
    cutoff_year: int
    active_period: str

    # Per-axis scores
    axis_scores: list[AxisScore] = Field(default_factory=list)

    # Aggregated score
    overall_score: float = Field(ge=-1.0, le=1.0)
    overall_confidence: float = Field(ge=0.0, le=1.0)

    # Explanations
    summary: str = ""  # Brief summary of the evaluation
    evidence_summary: str = ""  # What historical evidence supports the evaluation
    inference_summary: str = ""  # What the model inferred beyond evidence
    caveats: list[str] = Field(default_factory=list)  # Warnings and limitations

    def evidence_based_score(self) -> float:
        """Compute score using only evidence-based axis scores."""
        eb_scores = [s for s in self.axis_scores if s.is_evidence_based]
        if not eb_scores:
            return 0.0
        axes_by_name = {a.name: a for a in FEYNMAN_TASTE_AXES}
        total_weight = sum(axes_by_name.get(s.axis_name, TasteAxis(name="", description="", weight=0.5)).weight for s in eb_scores)
        if total_weight == 0:
            return 0.0
        weighted_sum = sum(
            s.score * axes_by_name.get(s.axis_name, TasteAxis(name="", description="", weight=0.5)).weight
            for s in eb_scores
        )
        return weighted_sum / total_weight


class TasteScorer:
    """
    Scores candidate theories/questions against Feynman's taste axes.

    This is the deterministic scoring component. It takes pre-computed axis scores
    (from the LLM evaluator) and aggregates them with proper weighting and
    evidence tracking.
    """

    def __init__(self, evidence_store: EvidenceStore):
        self.evidence_store = evidence_store
        self.axes = {a.name: a for a in FEYNMAN_TASTE_AXES}
        self.periods = {p.name: p for p in FEYNMAN_PERIODS}

    def get_active_period(self, year: int) -> TemporalPeriod | None:
        """Find the temporal period that contains the given year."""
        for period in FEYNMAN_PERIODS:
            if period.start_year <= year <= period.end_year:
                return period
        return None

    def get_period_weights(self, period: TemporalPeriod) -> dict[str, float]:
        """
        Adjust axis weights based on which period is active.
        Dominant axes for a period get a boost; others get a slight reduction.
        """
        weights = {}
        for axis_name, axis in self.axes.items():
            base_weight = axis.weight
            if axis_name in period.dominant_axes:
                # Boost dominant axes by 15%
                weights[axis_name] = min(1.0, base_weight * 1.15)
            else:
                # Slightly reduce non-dominant axes
                weights[axis_name] = base_weight * 0.90
        return weights

    def aggregate_scores(
        self,
        axis_scores: list[AxisScore],
        cutoff_year: int,
    ) -> tuple[float, float]:
        """
        Compute weighted aggregate score and confidence.

        Returns:
            (overall_score, overall_confidence) both in [-1, 1] and [0, 1]
        """
        if not axis_scores:
            return 0.0, 0.0

        period = self.get_active_period(cutoff_year)
        if period:
            weights = self.get_period_weights(period)
        else:
            weights = {name: ax.weight for name, ax in self.axes.items()}

        total_weight = 0.0
        weighted_score = 0.0
        weighted_confidence = 0.0

        for score in axis_scores:
            w = weights.get(score.axis_name, 0.5)
            total_weight += w
            weighted_score += score.score * w
            weighted_confidence += score.confidence * w

        if total_weight == 0:
            return 0.0, 0.0

        return weighted_score / total_weight, weighted_confidence / total_weight

    def rank_candidates(
        self,
        evaluations: list[TasteEvaluation],
    ) -> list[TasteEvaluation]:
        """Rank candidates by overall taste score, highest first."""
        return sorted(evaluations, key=lambda e: e.overall_score, reverse=True)

    def compare_candidates(
        self,
        eval_a: TasteEvaluation,
        eval_b: TasteEvaluation,
    ) -> dict:
        """
        Compare two candidates axis-by-axis.

        Returns a dict with per-axis comparison and a summary.
        """
        comparison = {
            "candidate_a": eval_a.candidate_description,
            "candidate_b": eval_b.candidate_description,
            "overall_preference": "a" if eval_a.overall_score > eval_b.overall_score else "b",
            "score_difference": eval_a.overall_score - eval_b.overall_score,
            "axis_comparison": [],
        }

        axes_a = {s.axis_name: s for s in eval_a.axis_scores}
        axes_b = {s.axis_name: s for s in eval_b.axis_scores}

        for axis_name in self.axes:
            sa = axes_a.get(axis_name)
            sb = axes_b.get(axis_name)
            if sa and sb:
                comparison["axis_comparison"].append({
                    "axis": axis_name,
                    "score_a": sa.score,
                    "score_b": sb.score,
                    "difference": sa.score - sb.score,
                    "winner": "a" if sa.score > sb.score else "b" if sb.score > sa.score else "tie",
                })

        return comparison
