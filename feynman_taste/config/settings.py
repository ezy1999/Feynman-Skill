"""
Global configuration for the Feynman Research Taste system.

Defines taste axes, temporal periods, model parameters, and data paths.
All taste axes are derived from documented historical evidence about Feynman's
scientific methodology, philosophy, and personal accounts.

Feynman's distinctive approach:
- Bottom-up computation over top-down principle theories
- Physical intuition and visualization over abstract formalism
- Playful curiosity and diverse problem-solving over systematic pursuit
- Fierce intellectual independence and anti-dogmatic methodology
"""

from pathlib import Path
from pydantic import BaseModel, Field


# ── Project paths ──────────────────────────────────────────────────────────────

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DATA_DIR = PROJECT_ROOT / "feynman_taste" / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EMBEDDINGS_DIR = DATA_DIR / "embeddings"


# ── Taste Axes ─────────────────────────────────────────────────────────────────

class TasteAxis(BaseModel):
    """A single dimension of scientific taste with historical grounding."""
    name: str
    description: str
    weight: float = Field(ge=0.0, le=1.0)
    evidence_sources: list[str] = Field(default_factory=list)
    keywords: list[str] = Field(default_factory=list)


# Feynman's core taste axes
FEYNMAN_TASTE_AXES: list[TasteAxis] = [
    TasteAxis(
        name="physical_intuition",
        description=(
            "Primacy of physical pictures and intuitive understanding over abstract formalism. "
            "Feynman insisted on being able to 'see' the physics before trusting the math. "
            "He developed Feynman diagrams specifically to make quantum field theory visualizable."
        ),
        weight=0.95,
        evidence_sources=[
            "Feynman, 'The Character of Physical Law' (1965 Messenger Lectures)",
            "Gleick, 'Genius' (1992), on Feynman's visualization methods",
            "Schweber, 'QED and the Men Who Made It' (1994), on path integrals",
        ],
        keywords=["intuition", "picture", "visualize", "physical", "understand", "see", "feel"],
    ),
    TasteAxis(
        name="computational_pragmatism",
        description=(
            "Preference for theories that can actually compute observable quantities. "
            "Feynman's path integral formulation and QED renormalization were driven by "
            "the desire to calculate, not just describe. He valued 'shut up and calculate' "
            "over philosophical interpretation."
        ),
        weight=0.90,
        evidence_sources=[
            "Feynman, 'QED: The Strange Theory of Light and Matter' (1985)",
            "Feynman, Nobel Lecture 'The Development of the Space-Time View of QED' (1965)",
            "Mehra, 'The Beat of a Different Drum' (1994)",
        ],
        keywords=["calculate", "compute", "predict", "number", "result", "quantitative", "practical"],
    ),
    TasteAxis(
        name="anti_formalism",
        description=(
            "Deep skepticism toward purely mathematical or axiomatic approaches that lack "
            "physical content. Feynman famously disliked the Dirac/von Neumann axiomatic "
            "approach to quantum mechanics and preferred his own path integral formulation "
            "precisely because it stayed closer to physical intuition."
        ),
        weight=0.80,
        evidence_sources=[
            "Feynman, 'The Character of Physical Law' (1965), Ch. 2",
            "Gleick, 'Genius' (1992), on Feynman's approach to mathematics",
            "Dyson, 'Disturbing the Universe' (1979), on Feynman vs. Schwinger",
        ],
        keywords=["anti-formal", "concrete", "physical meaning", "not abstract", "grounded"],
    ),
    TasteAxis(
        name="empirical_ruthlessness",
        description=(
            "Uncompromising insistence on agreement with experiment. Feynman's 'Cargo Cult "
            "Science' lecture (1974) is a manifesto for intellectual honesty: 'The first "
            "principle is that you must not fool yourself—and you are the easiest person "
            "to fool.' He valued theories that make precise, testable predictions."
        ),
        weight=0.90,
        evidence_sources=[
            "Feynman, 'Cargo Cult Science' Caltech Commencement (1974)",
            "Feynman, 'The Character of Physical Law' (1965), Ch. 7",
            "Feynman, 'The Meaning of It All' (1998)",
        ],
        keywords=["experiment", "test", "measure", "verify", "honest", "evidence", "data", "prediction"],
    ),
    TasteAxis(
        name="playful_exploration",
        description=(
            "Value placed on curiosity-driven, playful exploration without concern for "
            "practical applications or prestige. Feynman famously 'played' with spinning "
            "plates in the Cornell cafeteria, leading to work on QED. He pursued problems "
            "for fun, not for Nobel Prizes. His motto: 'What I cannot create, I do not understand.'"
        ),
        weight=0.85,
        evidence_sources=[
            "Feynman, 'Surely You're Joking, Mr. Feynman!' (1985), 'The Dignified Professor'",
            "Gleick, 'Genius' (1992), on the wobbling plates episode",
            "Feynman, 'The Pleasure of Finding Things Out' (1999)",
        ],
        keywords=["play", "fun", "curious", "explore", "puzzle", "game", "wonder", "joy"],
    ),
    TasteAxis(
        name="independent_thinking",
        description=(
            "Fierce intellectual independence and distrust of authority, dogma, and received "
            "wisdom. Feynman re-derived most of physics from scratch, distrusting textbook "
            "accounts. He challenged established figures (Bohr, Dirac) and resisted groupthink. "
            "His approach: understand it yourself or don't claim to understand it."
        ),
        weight=0.85,
        evidence_sources=[
            "Feynman, 'What Do You Care What Other People Think?' (1988)",
            "Feynman, 'Surely You're Joking' (1985), on challenging Bohr",
            "Gleick, 'Genius' (1992), Ch. on Los Alamos and authority",
        ],
        keywords=["independent", "original", "first principles", "skeptical", "challenge", "authority"],
    ),
    TasteAxis(
        name="multiple_representations",
        description=(
            "Belief that understanding requires multiple representations of the same phenomenon. "
            "Feynman simultaneously used path integrals, operator methods, and diagrams for QED. "
            "He argued that having only one formulation means you don't truly understand it. "
            "Having only one formulation means you don't truly understand it."
        ),
        weight=0.75,
        evidence_sources=[
            "Feynman, 'The Character of Physical Law' (1965), Ch. 2 on alternative formulations",
            "Feynman, Nobel Lecture (1965), on path integral vs. operator approaches",
            "Schweber, 'QED and the Men Who Made It' (1994)",
        ],
        keywords=["alternative", "representation", "different way", "reformulate", "equivalent", "many approaches"],
    ),
    TasteAxis(
        name="bottom_up_reasoning",
        description=(
            "Preference for building understanding from specific examples and calculations "
            "rather than from general principles. Feynman typically started with specific "
            "problems and generalized, rather than starting from general principles "
            "and deducing specific predictions."
        ),
        weight=0.80,
        evidence_sources=[
            "Feynman, 'Feynman's Tips on Physics' (2006), on problem-solving",
            "Gleick, 'Genius' (1992), on Feynman's working methods",
            "Krauss, 'Quantum Man' (2011), on Feynman's bottom-up style",
        ],
        keywords=["example", "specific", "concrete", "bottom-up", "case", "particular", "calculate first"],
    ),
    TasteAxis(
        name="cross_domain_versatility",
        description=(
            "Willingness and ability to apply methods across very different domains. "
            "Feynman contributed to QED, superfluidity, weak interactions, parton model, "
            "quantum computing, nanotechnology, biology (ribosomes), and even safe-cracking. "
            "He valued breadth and the transfer of techniques between fields."
        ),
        weight=0.70,
        evidence_sources=[
            "Feynman, 'There's Plenty of Room at the Bottom' (1959)",
            "Feynman, 'Simulating Physics with Computers' (1982)",
            "Gleick, 'Genius' (1992), on Feynman's range",
        ],
        keywords=["cross-domain", "versatile", "transfer", "different field", "broad", "interdisciplinary"],
    ),
    TasteAxis(
        name="simplicity_of_explanation",
        description=(
            "Ability to explain complex ideas simply is a test of understanding. "
            "Feynman's famous dictum: 'If you can't explain it to a freshman, you "
            "don't understand it.' He valued clarity of explanation as evidence of "
            "depth of understanding, not just a pedagogical convenience."
        ),
        weight=0.75,
        evidence_sources=[
            "Feynman, 'Feynman Lectures on Physics' (1964), Preface",
            "Feynman, 'QED: The Strange Theory of Light and Matter' (1985)",
            "Gleick, 'Genius' (1992), on Feynman's teaching",
        ],
        keywords=["explain", "simple", "clear", "teach", "understand", "freshman", "plain language"],
    ),
]


# ── Temporal Periods ───────────────────────────────────────────────────────────

class TemporalPeriod(BaseModel):
    name: str
    start_year: int
    end_year: int
    description: str
    dominant_axes: list[str] = Field(default_factory=list)


FEYNMAN_PERIODS: list[TemporalPeriod] = [
    TemporalPeriod(
        name="graduate_los_alamos",
        start_year=1939,
        end_year=1945,
        description=(
            "Graduate work at Princeton under Wheeler, then Manhattan Project at Los Alamos. "
            "Developed the path integral formulation. Learned to challenge authority. "
            "Computational pragmatism forged under wartime pressure."
        ),
        dominant_axes=["physical_intuition", "computational_pragmatism", "independent_thinking"],
    ),
    TemporalPeriod(
        name="qed_revolution",
        start_year=1946,
        end_year=1953,
        description=(
            "Post-war period at Cornell and Caltech. Development of QED, Feynman diagrams, "
            "and renormalization. The 'wobbling plates' period of playful rediscovery. "
            "Competition with Schwinger and Tomonaga."
        ),
        dominant_axes=["physical_intuition", "computational_pragmatism", "playful_exploration", "multiple_representations"],
    ),
    TemporalPeriod(
        name="broad_physics",
        start_year=1954,
        end_year=1970,
        description=(
            "Caltech years. Superfluidity, weak interactions (V-A theory), parton model, "
            "Feynman Lectures on Physics. Cross-domain work and teaching. Nobel Prize (1965)."
        ),
        dominant_axes=["cross_domain_versatility", "bottom_up_reasoning", "simplicity_of_explanation"],
    ),
    TemporalPeriod(
        name="later_career",
        start_year=1971,
        end_year=1988,
        description=(
            "Quantum computing vision, nanotechnology, Challenger investigation, popularization. "
            "Cargo Cult Science lecture. Emphasis on intellectual honesty and independent thinking."
        ),
        dominant_axes=["empirical_ruthlessness", "independent_thinking", "playful_exploration"],
    ),
]


# ── Model Configuration ───────────────────────────────────────────────────────

class ModelConfig(BaseModel):
    llm_provider: str = "anthropic"
    llm_model: str = "claude-sonnet-4-20250514"
    temperature: float = 0.3
    max_tokens: int = 4096
    embedding_model: str = "all-MiniLM-L6-v2"
    top_k_evidence: int = 10
    similarity_threshold: float = 0.5
    normalize_scores: bool = True
    require_evidence: bool = True
    min_evidence_count: int = 1
    default_cutoff_year: int = 1988  # Feynman's death
    enforce_temporal_cutoff: bool = True


DEFAULT_CONFIG = ModelConfig()
