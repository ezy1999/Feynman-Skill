"""
Benchmark for Feynman Research Taste Model.

Test cases derived from Feynman's documented preferences and choices.
"""

from __future__ import annotations
from pydantic import BaseModel, Field


class BenchmarkCase(BaseModel):
    id: str
    description: str
    candidates: list[str] = Field(description="List of candidate theories/questions")
    expected_ranking: list[int] = Field(description="Expected ranking indices, best first")
    cutoff_year: int
    evidence_basis: str
    difficulty: str = "medium"
    tags: list[str] = Field(default_factory=list)


def get_benchmark_cases() -> list[BenchmarkCase]:
    return [
        # ── Easy: Clear Feynman preferences ────────────────────────────
        BenchmarkCase(
            id="bench_path_integral_vs_axiomatic",
            description="Path integral vs axiomatic QM. Feynman created the former, distrusted the latter.",
            candidates=[
                "A formulation of quantum mechanics using a sum over all possible paths, "
                "providing physical pictures of particle behavior and direct computational tools.",
                "An axiomatic formulation of quantum mechanics using abstract Hilbert space operators, "
                "mathematically rigorous but physically opaque.",
            ],
            expected_ranking=[0, 1],
            cutoff_year=1950,
            evidence_basis="Feynman invented the path integral specifically as a physically intuitive alternative. Nobel Lecture (1965).",
            difficulty="easy",
            tags=["path_integral", "physical_intuition", "anti_formalism"],
        ),
        BenchmarkCase(
            id="bench_compute_vs_interpret",
            description="Computing predictions vs philosophical interpretation of QM.",
            candidates=[
                "An approach focused on calculating precise, experimentally testable predictions "
                "for observable quantities like cross-sections and decay rates.",
                "An approach focused on interpreting the philosophical meaning of quantum mechanics, "
                "debating the measurement problem and the nature of wave function collapse.",
            ],
            expected_ranking=[0, 1],
            cutoff_year=1965,
            evidence_basis="Feynman's 'shut up and calculate' attitude. Character of Physical Law (1965): experiment is the sole judge.",
            difficulty="easy",
            tags=["computational_pragmatism", "empirical_ruthlessness"],
        ),

        # ── Medium: Nuanced preferences ────────────────────────────────
        BenchmarkCase(
            id="bench_parton_vs_quark_model",
            description="Data-driven parton model vs theory-driven quark model.",
            candidates=[
                "A phenomenological model describing proton constituents as point-like partons, "
                "derived from scattering data without committing to specific theoretical identity.",
                "A theoretical model where hadrons are composed of fundamental quarks with "
                "specific quantum numbers, based on SU(3) group theory symmetry.",
            ],
            expected_ranking=[0, 1],
            cutoff_year=1969,
            evidence_basis="Feynman deliberately avoided identifying partons with quarks, preferring data over theory. Krauss (2011).",
            difficulty="medium",
            tags=["bottom_up_reasoning", "empirical_ruthlessness"],
        ),
        BenchmarkCase(
            id="bench_playful_vs_strategic",
            description="Curiosity-driven vs strategically planned research.",
            candidates=[
                "Pursuing an interesting puzzle purely because it is fun, without concern for "
                "practical applications or career advancement.",
                "Strategically selecting research problems based on their likelihood of producing "
                "high-impact publications and advancing one's career.",
            ],
            expected_ranking=[0, 1],
            cutoff_year=1970,
            evidence_basis="Wobbling plates episode in 'Surely You're Joking' (1985). Feynman explicitly valued play over strategy.",
            difficulty="medium",
            tags=["playful_exploration", "independent_thinking"],
        ),

        # ── Hard: Temporal and nuanced ─────────────────────────────────
        BenchmarkCase(
            id="bench_cross_domain_early",
            description="Cross-domain work in Feynman's early career (less dominant).",
            candidates=[
                "Developing new mathematical tools specific to quantum electrodynamics, "
                "pushing the frontier of a single field.",
                "Applying quantum field theory techniques to an unrelated area like "
                "condensed matter physics or biology.",
            ],
            expected_ranking=[0, 1],  # Early Feynman focused on QED
            cutoff_year=1950,
            evidence_basis="Pre-1953, Feynman was laser-focused on QED. Cross-domain work came later.",
            difficulty="hard",
            tags=["cross_domain_versatility", "temporal_sensitivity"],
        ),
        BenchmarkCase(
            id="bench_cross_domain_late",
            description="Same question but late career: Feynman should prefer cross-domain.",
            candidates=[
                "Developing new mathematical tools specific to quantum electrodynamics, "
                "pushing the frontier of a single field.",
                "Applying quantum field theory techniques to an unrelated area like "
                "condensed matter physics or biology.",
            ],
            expected_ranking=[1, 0],  # Late Feynman embraced cross-domain
            cutoff_year=1980,
            evidence_basis="Post-1960, Feynman actively pursued cross-domain work: superfluidity, weak force, partons, nanotechnology, quantum computing, biology.",
            difficulty="hard",
            tags=["cross_domain_versatility", "temporal_sensitivity"],
        ),
    ]


def run_benchmark(pipeline, verbose: bool = True) -> dict:
    cases = get_benchmark_cases()
    results = []
    for case in cases:
        if verbose:
            print(f"\nRunning: {case.id} - {case.description}")
        evaluations = pipeline.rank_candidates(case.candidates, cutoff_year=case.cutoff_year)
        actual_ranking = [case.candidates.index(ev.candidate_description) for ev in evaluations]
        correct = actual_ranking == case.expected_ranking
        results.append({
            "case_id": case.id, "difficulty": case.difficulty,
            "correct": correct, "expected": case.expected_ranking,
            "actual": actual_ranking, "scores": [ev.overall_score for ev in evaluations],
        })
        if verbose:
            print(f"  {'PASS' if correct else 'FAIL'}: expected {case.expected_ranking}, got {actual_ranking}")

    total = len(results)
    correct = sum(1 for r in results if r["correct"])
    by_difficulty = {}
    for diff in ["easy", "medium", "hard"]:
        dr = [r for r in results if r["difficulty"] == diff]
        dc = sum(1 for r in dr if r["correct"])
        by_difficulty[diff] = {"total": len(dr), "correct": dc, "accuracy": dc / len(dr) if dr else 0}
    return {"total": total, "correct": correct, "accuracy": correct / total if total else 0, "by_difficulty": by_difficulty, "cases": results}
