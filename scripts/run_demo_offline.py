"""Offline demo of Feynman Research Taste system."""

from feynman_taste.core.pipeline import TastePipeline
from feynman_taste.core.evidence import EvidenceStore, SourceType
from feynman_taste.core.taste_model import AxisScore, TasteEvaluation, TasteScorer
from feynman_taste.core.retriever import EvidenceRetriever
from feynman_taste.data.loader import load_evidence_store
from feynman_taste.config.settings import PROCESSED_DATA_DIR, FEYNMAN_TASTE_AXES
from feynman_taste.utils.formatting import format_ranking


class MockEvaluator:
    def evaluate(self, candidate, evidence, cutoff_year=1988, scorer=None):
        candidate_lower = candidate.lower()
        axis_scores = []
        for axis in FEYNMAN_TASTE_AXES:
            kw_hits = sum(1 for kw in axis.keywords if kw.lower() in candidate_lower)
            ev_hits = sum(1 for r, rel in evidence if axis.name in r.relevant_axes and rel > 0)
            score = min(1.0, kw_hits * 0.3 + ev_hits * 0.2) if (kw_hits or ev_hits) else -0.1
            neg = {"anti_formalism": ["abstract", "axiomatic", "formal proof", "rigorous"],
                   "empirical_ruthlessness": ["philosophical", "interpretation", "metaphysical"],
                   "playful_exploration": ["strategic", "career", "prestigious"]}
            for nk in neg.get(axis.name, []):
                if nk in candidate_lower:
                    score = max(-1.0, score - 0.5)
            pos = {"physical_intuition": ["picture", "visualiz", "intuiti", "physical"],
                   "computational_pragmatism": ["calculat", "comput", "predict", "number"],
                   "empirical_ruthlessness": ["experiment", "test", "measur", "data"],
                   "playful_exploration": ["play", "fun", "curious", "puzzle"],
                   "independent_thinking": ["original", "first principles", "challenge"],
                   "bottom_up_reasoning": ["example", "specific", "bottom-up", "data-driven"]}
            for pk in pos.get(axis.name, []):
                if pk in candidate_lower:
                    score = min(1.0, score + 0.3)
            axis_scores.append(AxisScore(
                axis_name=axis.name, score=max(-1.0, min(1.0, score)),
                confidence=min(1.0, 0.3 + kw_hits * 0.2 + ev_hits * 0.1),
                evidence_ids=[r.id for r, _ in evidence[:2] if axis.name in r.relevant_axes],
                explanation=f"{'Evidence' if ev_hits else 'Inferred'}: {kw_hits} kw, {ev_hits} ev.",
                is_evidence_based=ev_hits > 0,
            ))
        if scorer:
            overall, conf = scorer.aggregate_scores(axis_scores, cutoff_year)
        else:
            overall = sum(s.score for s in axis_scores) / len(axis_scores)
            conf = sum(s.confidence for s in axis_scores) / len(axis_scores)
        from feynman_taste.config.settings import FEYNMAN_PERIODS
        period = next((p.name for p in FEYNMAN_PERIODS if p.start_year <= cutoff_year <= p.end_year), "unknown")
        return TasteEvaluation(
            candidate_description=candidate, cutoff_year=cutoff_year, active_period=period,
            axis_scores=axis_scores, overall_score=overall, overall_confidence=conf,
            summary=f"Mock evaluation at year {cutoff_year}.",
            evidence_summary=f"{sum(1 for s in axis_scores if s.is_evidence_based)} evidence-grounded.",
            inference_summary=f"{sum(1 for s in axis_scores if not s.is_evidence_based)} inferred.",
            caveats=["Mock evaluation. Set ANTHROPIC_API_KEY for LLM-based scoring."],
        )


def main():
    print("=" * 70)
    print("FEYNMAN RESEARCH TASTE - OFFLINE DEMO")
    print("=" * 70)

    store = load_evidence_store(PROCESSED_DATA_DIR)
    retriever = EvidenceRetriever(store)
    scorer = TasteScorer(store)
    mock = MockEvaluator()
    print(f"\nEvidence: {store.count()} records")

    # Demo 1: Theory Feynman would love
    print("\n" + "=" * 70)
    print("DEMO 1: Theory Feynman would appreciate")
    c1 = "A computational approach using physical intuition and Feynman diagrams to calculate scattering cross-sections, with testable experimental predictions."
    ev1 = retriever.retrieve(c1, top_k=10, cutoff_year=1965)
    r1 = mock.evaluate(c1, ev1, cutoff_year=1965, scorer=scorer)
    print(TastePipeline.format_evaluation(r1))

    # Demo 2: Theory Feynman would dislike
    print("\n" + "=" * 70)
    print("DEMO 2: Theory Feynman would reject")
    c2 = "A rigorous axiomatic formal proof of quantum field theory using abstract algebraic structures without physical interpretation or experimental predictions."
    ev2 = retriever.retrieve(c2, top_k=10, cutoff_year=1965)
    r2 = mock.evaluate(c2, ev2, cutoff_year=1965, scorer=scorer)
    print(TastePipeline.format_evaluation(r2))

    # Demo 3: Ranking
    print("\n" + "=" * 70)
    print("DEMO 3: Ranking")
    candidates = [
        "A playful exploration of quantum computing using physical intuition",
        "A data-driven bottom-up analysis with testable experimental predictions",
        "A formal axiomatic treatment of quantum gravity with philosophical interpretation",
    ]
    evals = []
    for c in candidates:
        ev = retriever.retrieve(c, top_k=10, cutoff_year=1985)
        evals.append(mock.evaluate(c, ev, cutoff_year=1985, scorer=scorer))
    print(format_ranking(sorted(evals, key=lambda e: e.overall_score, reverse=True)))

    print("=" * 70)
    print("Demo complete!")


if __name__ == "__main__":
    main()
