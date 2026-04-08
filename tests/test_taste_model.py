"""Tests for Feynman taste scoring model."""

import pytest
from feynman_taste.core.taste_model import AxisScore, TasteEvaluation, TasteScorer
from feynman_taste.core.evidence import EvidenceStore


@pytest.fixture
def scorer():
    return TasteScorer(EvidenceStore())


class TestTasteScorer:
    def test_get_active_period(self, scorer):
        p = scorer.get_active_period(1948)
        assert p is not None
        assert p.name == "qed_revolution"

        p = scorer.get_active_period(1975)
        assert p is not None
        assert p.name == "later_career"

    def test_aggregate_scores(self, scorer):
        scores = [
            AxisScore(axis_name="physical_intuition", score=0.9, confidence=0.8, is_evidence_based=True),
            AxisScore(axis_name="computational_pragmatism", score=0.7, confidence=0.9, is_evidence_based=True),
        ]
        overall, conf = scorer.aggregate_scores(scores, cutoff_year=1950)
        assert -1.0 <= overall <= 1.0
        assert 0.0 <= conf <= 1.0

    def test_aggregate_empty(self, scorer):
        assert scorer.aggregate_scores([], cutoff_year=1950) == (0.0, 0.0)

    def test_rank(self, scorer):
        evals = [
            TasteEvaluation(candidate_description="A", cutoff_year=1950, active_period="qed_revolution", overall_score=0.3, overall_confidence=0.8),
            TasteEvaluation(candidate_description="B", cutoff_year=1950, active_period="qed_revolution", overall_score=0.9, overall_confidence=0.9),
        ]
        assert scorer.rank_candidates(evals)[0].candidate_description == "B"

    def test_period_weights(self, scorer):
        p = scorer.get_active_period(1950)
        w = scorer.get_period_weights(p)
        # QED revolution: physical_intuition and computational_pragmatism should be boosted
        assert w["physical_intuition"] > w["simplicity_of_explanation"]
