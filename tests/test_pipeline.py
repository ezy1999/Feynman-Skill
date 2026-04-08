"""Tests for Feynman pipeline (offline, no LLM)."""

import pytest
from feynman_taste.core.pipeline import TastePipeline
from feynman_taste.core.evidence import EvidenceStore
from feynman_taste.data.seed_evidence import get_seed_evidence
from feynman_taste.core.taste_model import TasteEvaluation, AxisScore


@pytest.fixture
def pipeline():
    store = EvidenceStore()
    store.add_batch(get_seed_evidence())
    return TastePipeline(store)


class TestPipeline:
    def test_creation(self, pipeline):
        assert pipeline.evidence_store.count() > 0

    def test_retrieval(self, pipeline):
        results = pipeline.retriever.retrieve(
            "path integral physical intuition quantum mechanics calculate",
            top_k=10, cutoff_year=1988,
        )
        assert len(results) > 0
        axes = set()
        for r, _ in results:
            axes.update(r.relevant_axes)
        assert "physical_intuition" in axes or "computational_pragmatism" in axes

    def test_temporal_cutoff(self, pipeline):
        results = pipeline.retriever.retrieve("quantum computing", top_k=20, cutoff_year=1945)
        for r, _ in results:
            if r.year is not None:
                assert r.year <= 1945

    def test_format(self):
        ev = TasteEvaluation(
            candidate_description="Test theory", cutoff_year=1965,
            active_period="broad_physics",
            axis_scores=[AxisScore(axis_name="physical_intuition", score=0.9, confidence=0.8, explanation="Strong", is_evidence_based=True)],
            overall_score=0.9, overall_confidence=0.8, summary="Good",
        )
        text = TastePipeline.format_evaluation(ev)
        assert "Test theory" in text
        assert "physical_intuition" in text
