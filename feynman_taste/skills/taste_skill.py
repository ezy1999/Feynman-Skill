"""
Taste Skill Module
===================

Wraps the taste agent as a Claude Code skill for community distribution.

The skill provides:
- evaluate_taste: Evaluate a theory against Feynman's taste
- rank_theories: Rank multiple theories
- compare_theories: Compare two theories
- get_taste_axes: Get information about Feynman's taste axes
- get_evidence: Query the evidence store
"""

from __future__ import annotations

import json
from typing import Any

from feynman_taste.agents.taste_agent import TasteAgent
from feynman_taste.config.settings import FEYNMAN_TASTE_AXES, FEYNMAN_PERIODS
from feynman_taste.core.evidence import EvidenceStore
from feynman_taste.data.loader import load_evidence_store
from feynman_taste.config.settings import PROCESSED_DATA_DIR


class FeynmanTasteSkill:
    """
    Claude Code skill wrapper for Feynman's research taste modeling.

    Designed to be packaged and published to the Claude Code community.
    """

    def __init__(self):
        self._agent: TasteAgent | None = None
        self._store: EvidenceStore | None = None

    @property
    def agent(self) -> TasteAgent:
        if self._agent is None:
            self._agent = TasteAgent()
        return self._agent

    @property
    def store(self) -> EvidenceStore:
        if self._store is None:
            self._store = load_evidence_store(PROCESSED_DATA_DIR)
        return self._store

    def evaluate_taste(self, theory: str, cutoff_year: int = 1955) -> dict:
        """
        Evaluate how a scientific theory aligns with Feynman's research taste.

        Args:
            theory: Description of the theory or scientific question
            cutoff_year: Year to evaluate Feynman's taste at (avoids anachronism)

        Returns:
            Dict with overall score, per-axis scores, and evidence-based explanations
        """
        from feynman_taste.utils.formatting import evaluation_to_dict

        evaluation = self.agent.pipeline.evaluate(theory, cutoff_year=cutoff_year)
        return evaluation_to_dict(evaluation)

    def rank_theories(self, theories: list[str], cutoff_year: int = 1955) -> list[dict]:
        """
        Rank multiple theories by their alignment with Feynman's taste.

        Args:
            theories: List of theory descriptions
            cutoff_year: Temporal cutoff year

        Returns:
            Ranked list of evaluation dicts (best first)
        """
        from feynman_taste.utils.formatting import evaluation_to_dict

        evaluations = self.agent.pipeline.rank_candidates(theories, cutoff_year=cutoff_year)
        return [evaluation_to_dict(ev) for ev in evaluations]

    def compare_theories(self, theory_a: str, theory_b: str, cutoff_year: int = 1955) -> dict:
        """Compare two theories head-to-head."""
        return self.agent.pipeline.compare(theory_a, theory_b, cutoff_year=cutoff_year)

    def get_taste_axes(self) -> list[dict]:
        """Get information about Feynman's taste axes."""
        return [
            {
                "name": a.name,
                "description": a.description,
                "weight": a.weight,
                "evidence_sources": a.evidence_sources,
                "keywords": a.keywords,
            }
            for a in FEYNMAN_TASTE_AXES
        ]

    def get_periods(self) -> list[dict]:
        """Get Feynman's career periods and their dominant taste axes."""
        return [
            {
                "name": p.name,
                "years": f"{p.start_year}-{p.end_year}",
                "description": p.description,
                "dominant_axes": p.dominant_axes,
            }
            for p in FEYNMAN_PERIODS
        ]

    def get_evidence_summary(self) -> dict:
        """Get a summary of the evidence store."""
        return self.store.summary()

    def query_evidence(
        self,
        axis: str | None = None,
        cutoff_year: int | None = None,
        source_type: str | None = None,
    ) -> list[dict]:
        """Query the evidence store with filters."""
        from feynman_taste.core.evidence import SourceType

        kwargs: dict[str, Any] = {}
        if cutoff_year:
            kwargs["cutoff_year"] = cutoff_year
        if axis:
            kwargs["axes"] = [axis]
        if source_type:
            kwargs["source_types"] = [SourceType(source_type)]

        records = self.store.filter(**kwargs)
        return [
            {
                "id": r.id,
                "content": r.content[:200],
                "source": r.source_text,
                "type": r.source_type.value,
                "confidence": r.confidence.value,
                "year": r.year,
                "axes": r.relevant_axes,
            }
            for r in records
        ]
