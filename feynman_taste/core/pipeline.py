"""
Main Pipeline Module
=====================

Orchestrates the full taste evaluation pipeline:
1. Load evidence store
2. Accept candidate theory/question
3. Retrieve relevant evidence
4. Evaluate via LLM
5. Score and rank
6. Output results with evidence/inference separation

This is the primary entry point for the taste modeling system.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from feynman_taste.config.settings import DEFAULT_CONFIG, ModelConfig
from feynman_taste.core.evidence import EvidenceStore
from feynman_taste.core.retriever import EvidenceRetriever
from feynman_taste.core.evaluator import TasteEvaluator
from feynman_taste.core.taste_model import TasteEvaluation, TasteScorer


class TastePipeline:
    """
    End-to-end pipeline for evaluating scientific candidates against
    Feynman's research taste.

    Usage:
        pipeline = TastePipeline.from_data_dir("path/to/data")
        result = pipeline.evaluate("Is light a wave or a particle?", cutoff_year=1905)
        pipeline.print_evaluation(result)
    """

    def __init__(
        self,
        evidence_store: EvidenceStore,
        config: ModelConfig | None = None,
    ):
        self.evidence_store = evidence_store
        self.config = config or DEFAULT_CONFIG
        self.retriever = EvidenceRetriever(evidence_store)
        self.evaluator = TasteEvaluator(self.config)
        self.scorer = TasteScorer(evidence_store)

    @classmethod
    def from_data_dir(cls, data_dir: str | Path, config: ModelConfig | None = None) -> "TastePipeline":
        """Create a pipeline by loading evidence from a data directory."""
        from feynman_taste.data.loader import load_evidence_store
        evidence_store = load_evidence_store(Path(data_dir))
        return cls(evidence_store, config)

    @classmethod
    def default(cls, config: ModelConfig | None = None) -> "TastePipeline":
        """Create a pipeline with the built-in evidence data."""
        from feynman_taste.config.settings import PROCESSED_DATA_DIR
        from feynman_taste.data.loader import load_evidence_store
        evidence_store = load_evidence_store(PROCESSED_DATA_DIR)
        return cls(evidence_store, config)

    def evaluate(
        self,
        candidate: str,
        cutoff_year: int = 1955,
        top_k_evidence: int | None = None,
    ) -> TasteEvaluation:
        """
        Evaluate a single candidate theory/question.

        Args:
            candidate: Description of the theory/question to evaluate
            cutoff_year: Year cutoff to prevent anachronism
            top_k_evidence: Number of evidence records to retrieve

        Returns:
            TasteEvaluation with scores, explanations, and evidence links
        """
        k = top_k_evidence or self.config.top_k_evidence

        # Step 1: Retrieve relevant evidence
        evidence = self.retriever.retrieve(
            query=candidate,
            top_k=k,
            cutoff_year=cutoff_year,
        )

        # Step 2: Evaluate via LLM
        evaluation = self.evaluator.evaluate(
            candidate=candidate,
            evidence=evidence,
            cutoff_year=cutoff_year,
            scorer=self.scorer,
        )

        return evaluation

    def rank_candidates(
        self,
        candidates: list[str],
        cutoff_year: int = 1955,
    ) -> list[TasteEvaluation]:
        """
        Evaluate and rank multiple candidates.

        Args:
            candidates: List of theory/question descriptions
            cutoff_year: Temporal cutoff year

        Returns:
            List of TasteEvaluations sorted by overall score (highest first)
        """
        evaluations = [
            self.evaluate(c, cutoff_year=cutoff_year)
            for c in candidates
        ]
        return self.scorer.rank_candidates(evaluations)

    def compare(
        self,
        candidate_a: str,
        candidate_b: str,
        cutoff_year: int = 1955,
    ) -> dict:
        """Compare two candidates head-to-head."""
        eval_a = self.evaluate(candidate_a, cutoff_year=cutoff_year)
        eval_b = self.evaluate(candidate_b, cutoff_year=cutoff_year)
        return self.scorer.compare_candidates(eval_a, eval_b)

    @staticmethod
    def format_evaluation(evaluation: TasteEvaluation) -> str:
        """Format an evaluation as a human-readable string."""
        lines = []
        lines.append("=" * 70)
        lines.append("FEYNMAN RESEARCH TASTE EVALUATION")
        lines.append("=" * 70)
        lines.append(f"\nCandidate: {evaluation.candidate_description}")
        lines.append(f"Cutoff Year: {evaluation.cutoff_year}")
        lines.append(f"Active Period: {evaluation.active_period}")
        lines.append(f"\nOverall Score: {evaluation.overall_score:+.3f} "
                      f"(confidence: {evaluation.overall_confidence:.2f})")

        lines.append("\n--- Taste Axis Scores ---")
        for score in sorted(evaluation.axis_scores, key=lambda s: s.score, reverse=True):
            evidence_tag = "EVIDENCE" if score.is_evidence_based else "INFERRED"
            lines.append(
                f"  {score.axis_name:25s} {score.score:+.3f} "
                f"(conf: {score.confidence:.2f}) [{evidence_tag}]"
            )
            if score.explanation:
                # Indent explanation
                for exp_line in score.explanation.split("\n"):
                    lines.append(f"    {exp_line}")

        if evaluation.summary:
            lines.append(f"\n--- Summary ---\n{evaluation.summary}")

        if evaluation.evidence_summary:
            lines.append(f"\n--- Evidence-Based Assessment ---\n{evaluation.evidence_summary}")

        if evaluation.inference_summary:
            lines.append(f"\n--- Model Inference (NOT historically grounded) ---\n{evaluation.inference_summary}")

        if evaluation.caveats:
            lines.append("\n--- Caveats ---")
            for caveat in evaluation.caveats:
                lines.append(f"  ! {caveat}")

        lines.append("\n" + "=" * 70)
        return "\n".join(lines)

    def print_evaluation(self, evaluation: TasteEvaluation) -> None:
        """Print a formatted evaluation to stdout."""
        print(self.format_evaluation(evaluation))
