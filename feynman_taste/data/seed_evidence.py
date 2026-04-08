"""
Seed Evidence Data for Feynman
================================

Built-in evidence records from documented historical sources about
Feynman's scientific taste. Feynman's taste profile is distinctive:
- Physical intuition over mathematical formalism
- Computational pragmatism ("shut up and calculate")
- Playful, curiosity-driven exploration
- Ruthless empiricism and intellectual honesty
- Fierce independence from authority and dogma
"""

from feynman_taste.core.evidence import (
    EvidenceRecord,
    SourceType,
    ConfidenceLevel,
)


def get_seed_evidence() -> list[EvidenceRecord]:
    return [
        # ── Physical Intuition ─────────────────────────────────────────
        EvidenceRecord(
            id="seed_intuition_001",
            content=(
                "Feynman developed Feynman diagrams not as mere calculational tools but as "
                "visual representations of physical processes. Freeman Dyson described how "
                "Feynman 'had a physical picture of everything,' seeing particle interactions "
                "as stories unfolding in spacetime. While Schwinger's approach was algebraically "
                "elegant but opaque, Feynman's diagrams made the physics visible and computable."
            ),
            source_text="Dyson, 'Disturbing the Universe' (1979); Schweber, 'QED and the Men Who Made It' (1994)",
            source_type=SourceType.SECONDARY,
            confidence=ConfidenceLevel.STRONG,
            year=1949,
            period="qed_revolution",
            relevant_axes=["physical_intuition", "multiple_representations"],
            axis_valence={"physical_intuition": 1.0, "multiple_representations": 0.8},
            tags=["feynman_diagrams", "qed", "visualization"],
        ),
        EvidenceRecord(
            id="seed_intuition_002",
            content=(
                "In 'The Character of Physical Law' (1965), Feynman stated: 'It is whether or "
                "not the theory gives predictions that agree with experiment. It is not a question "
                "of whether a theory is philosophically delightful, or easy to understand, or "
                "perfectly reasonable from the standpoint of common sense.' Yet he simultaneously "
                "insisted on physical pictures, saying 'I have to have the physical picture that "
                "way...I need it in order to think.'"
            ),
            source_text="Feynman, 'The Character of Physical Law' (1965), BBC Messenger Lectures",
            source_type=SourceType.PRIMARY,
            confidence=ConfidenceLevel.DIRECT,
            year=1965,
            period="broad_physics",
            relevant_axes=["physical_intuition", "empirical_ruthlessness"],
            axis_valence={"physical_intuition": 1.0, "empirical_ruthlessness": 0.9},
            tags=["methodology", "character_physical_law"],
            is_quote=True,
        ),

        # ── Computational Pragmatism ───────────────────────────────────
        EvidenceRecord(
            id="seed_compute_001",
            content=(
                "Feynman's path integral formulation of quantum mechanics (1948) was motivated "
                "by the desire to compute. While mathematically equivalent to the Schrodinger "
                "and Heisenberg pictures, the path integral provided new computational tools "
                "and physical insight. Feynman valued the formulation because it yielded numbers "
                "that matched experiments to extraordinary precision (QED predictions accurate "
                "to 10 decimal places)."
            ),
            source_text="Feynman, 'Space-Time Approach to Non-Relativistic Quantum Mechanics', Reviews of Modern Physics 20 (1948)",
            source_type=SourceType.PRIMARY,
            confidence=ConfidenceLevel.DIRECT,
            year=1948,
            period="qed_revolution",
            relevant_axes=["computational_pragmatism", "physical_intuition"],
            axis_valence={"computational_pragmatism": 1.0, "physical_intuition": 0.8},
            tags=["path_integral", "qed", "computation"],
        ),
        EvidenceRecord(
            id="seed_compute_002",
            content=(
                "In his Nobel Lecture (1965), Feynman described how his approach to QED was "
                "driven by the goal of getting concrete answers: 'The rest of my work was simply "
                "to try to see what the consequences would be.' He contrasted his computational "
                "approach with Schwinger's more formal algebraic methods, noting that while both "
                "gave the same answers, his approach 'brought quantum electrodynamics to the "
                "point of being a computable science.'"
            ),
            source_text="Feynman, Nobel Lecture, 'The Development of the Space-Time View of Quantum Electrodynamics' (1965)",
            source_type=SourceType.PRIMARY,
            confidence=ConfidenceLevel.DIRECT,
            year=1965,
            period="broad_physics",
            relevant_axes=["computational_pragmatism"],
            axis_valence={"computational_pragmatism": 1.0},
            tags=["nobel_lecture", "qed", "computation"],
            is_quote=True,
        ),

        # ── Anti-Formalism ─────────────────────────────────────────────
        EvidenceRecord(
            id="seed_antiformal_001",
            content=(
                "Feynman's distrust of pure formalism is documented by Gleick (1992): 'He "
                "distrusted the conventional mathematical formalism...He was bored by formal "
                "proofs. He liked to say he could not understand something unless he could "
                "reduce it to a freshman-level explanation.' When S-matrix theory became "
                "fashionable in the 1960s, Feynman resisted its purely formal, non-visual "
                "approach to particle physics."
            ),
            source_text="Gleick, 'Genius: The Life and Science of Richard Feynman' (1992)",
            source_type=SourceType.SECONDARY,
            confidence=ConfidenceLevel.STRONG,
            year=1992,
            relevant_axes=["anti_formalism", "physical_intuition"],
            axis_valence={"anti_formalism": 1.0, "physical_intuition": 0.7},
            tags=["formalism", "methodology", "gleick"],
        ),

        # ── Empirical Ruthlessness ─────────────────────────────────────
        EvidenceRecord(
            id="seed_empirical_001",
            content=(
                "In his 1974 Caltech Commencement address 'Cargo Cult Science,' Feynman "
                "articulated his core scientific ethic: 'The first principle is that you must "
                "not fool yourself\u2014and you are the easiest person to fool.' He criticized "
                "sciences that adopted the superficial appearance of scientific method without "
                "its substance, comparing them to Pacific Island cargo cults. He demanded "
                "'a kind of scientific integrity, a principle of scientific thought that "
                "corresponds to a kind of utter honesty.'"
            ),
            source_text="Feynman, 'Cargo Cult Science', Caltech Commencement Address (1974)",
            source_type=SourceType.PRIMARY,
            confidence=ConfidenceLevel.DIRECT,
            year=1974,
            period="later_career",
            relevant_axes=["empirical_ruthlessness", "independent_thinking"],
            axis_valence={"empirical_ruthlessness": 1.0, "independent_thinking": 0.8},
            tags=["cargo_cult", "intellectual_honesty", "methodology"],
            is_quote=True,
        ),
        EvidenceRecord(
            id="seed_empirical_002",
            content=(
                "Feynman stated in 'The Character of Physical Law': 'It doesn't matter how "
                "beautiful your guess is. It doesn't matter how smart you are, who made the "
                "guess, or what his name is\u2014if it disagrees with experiment it is wrong. "
                "In that simple statement is the key to science.' This encapsulates his "
                "prioritization of empirical evidence over all other considerations, including "
                "mathematical beauty and authority."
            ),
            source_text="Feynman, 'The Character of Physical Law' (1965), Ch. 7 'Seeking New Laws'",
            source_type=SourceType.PRIMARY,
            confidence=ConfidenceLevel.DIRECT,
            year=1965,
            period="broad_physics",
            relevant_axes=["empirical_ruthlessness", "independent_thinking"],
            axis_valence={"empirical_ruthlessness": 1.0, "independent_thinking": 0.7},
            tags=["experiment", "character_physical_law"],
            is_quote=True,
        ),

        # ── Playful Exploration ────────────────────────────────────────
        EvidenceRecord(
            id="seed_play_001",
            content=(
                "Feynman described in 'Surely You're Joking' how after his early career burnout, "
                "he decided to 'play with physics' with no pressure. Watching a spinning plate "
                "in the Cornell cafeteria, he worked out the wobble-to-spin ratio purely for fun. "
                "'There was no importance to what I was doing, but ultimately it led me to the "
                "diagrams and the whole business that I got the Nobel Prize for.' This episode "
                "epitomizes his belief that playful curiosity produces the best science."
            ),
            source_text="Feynman, 'Surely You're Joking, Mr. Feynman!' (1985), 'The Dignified Professor'",
            source_type=SourceType.PRIMARY,
            confidence=ConfidenceLevel.DIRECT,
            year=1985,
            relevant_axes=["playful_exploration"],
            axis_valence={"playful_exploration": 1.0},
            tags=["wobbling_plates", "play", "curiosity", "surely_joking"],
            is_quote=True,
        ),

        # ── Independent Thinking ───────────────────────────────────────
        EvidenceRecord(
            id="seed_independent_001",
            content=(
                "At Los Alamos, the young Feynman challenged Niels Bohr directly, the only "
                "junior scientist willing to do so. Bohr reportedly began seeking Feynman out "
                "specifically because 'he's the only one who's not afraid of me.' This pattern "
                "of intellectual fearlessness persisted: Feynman routinely re-derived results "
                "from scratch rather than accepting others' proofs."
            ),
            source_text="Gleick, 'Genius' (1992), Ch. on Los Alamos; Feynman, 'Surely You're Joking' (1985)",
            source_type=SourceType.SECONDARY,
            confidence=ConfidenceLevel.STRONG,
            year=1943,
            period="graduate_los_alamos",
            relevant_axes=["independent_thinking"],
            axis_valence={"independent_thinking": 1.0},
            tags=["los_alamos", "bohr", "authority"],
        ),
        EvidenceRecord(
            id="seed_independent_002",
            content=(
                "Feynman's investigation of the Challenger disaster (1986) exemplified his "
                "independent thinking. Rather than accepting NASA management's assurances, he "
                "conducted his own investigation, famously demonstrating the O-ring failure "
                "with ice water during the televised hearing. His appendix to the Rogers "
                "Commission report concluded: 'For a successful technology, reality must take "
                "precedence over public relations, for Nature cannot be fooled.'"
            ),
            source_text="Feynman, 'What Do You Care What Other People Think?' (1988), Personal Appendix to the Rogers Commission Report",
            source_type=SourceType.PRIMARY,
            confidence=ConfidenceLevel.DIRECT,
            year=1986,
            period="later_career",
            relevant_axes=["independent_thinking", "empirical_ruthlessness"],
            axis_valence={"independent_thinking": 1.0, "empirical_ruthlessness": 1.0},
            tags=["challenger", "integrity", "nature_cannot_be_fooled"],
            is_quote=True,
        ),

        # ── Multiple Representations ───────────────────────────────────
        EvidenceRecord(
            id="seed_multiple_001",
            content=(
                "In his Nobel Lecture, Feynman reflected on having developed the path integral "
                "formulation as an alternative to Schrodinger/Heisenberg approaches: 'Theories "
                "of the known, which are described by different physical ideas, may be "
                "equivalent in all their predictions and are hence scientifically "
                "indistinguishable. However, they are not psychologically identical...For "
                "different views suggest different kinds of modifications which might be made "
                "and hence are not equivalent in the hypotheses one generates from them.'"
            ),
            source_text="Feynman, Nobel Lecture (1965)",
            source_type=SourceType.PRIMARY,
            confidence=ConfidenceLevel.DIRECT,
            year=1965,
            period="broad_physics",
            relevant_axes=["multiple_representations"],
            axis_valence={"multiple_representations": 1.0},
            tags=["nobel_lecture", "alternative_formulations"],
            is_quote=True,
        ),

        # ── Bottom-Up Reasoning ────────────────────────────────────────
        EvidenceRecord(
            id="seed_bottomup_001",
            content=(
                "Feynman's approach to the parton model (1969) exemplifies his bottom-up style. "
                "Rather than starting from fundamental theory, he analyzed deep inelastic "
                "scattering data and proposed that protons contain point-like constituents "
                "(partons). He deliberately avoided identifying partons with quarks initially, "
                "preferring to let the data guide theory rather than imposing a theoretical "
                "framework. This was validated when partons were identified with quarks and gluons."
            ),
            source_text="Feynman, 'Very High-Energy Collisions of Hadrons', Physical Review Letters 23 (1969); Krauss, 'Quantum Man' (2011)",
            source_type=SourceType.SECONDARY,
            confidence=ConfidenceLevel.STRONG,
            year=1969,
            period="broad_physics",
            relevant_axes=["bottom_up_reasoning", "empirical_ruthlessness"],
            axis_valence={"bottom_up_reasoning": 1.0, "empirical_ruthlessness": 0.8},
            tags=["parton_model", "data_driven"],
        ),

        # ── Cross-Domain Versatility ───────────────────────────────────
        EvidenceRecord(
            id="seed_crossdomain_001",
            content=(
                "Feynman's 1959 lecture 'There's Plenty of Room at the Bottom' is considered "
                "the founding vision of nanotechnology. A quantum field theorist venturing into "
                "materials science and engineering, Feynman proposed manipulating individual atoms "
                "and miniaturizing machines\u2014decades before the technology existed. This exemplifies "
                "his willingness to apply physical thinking across domain boundaries."
            ),
            source_text="Feynman, 'There's Plenty of Room at the Bottom', APS meeting at Caltech (1959)",
            source_type=SourceType.PRIMARY,
            confidence=ConfidenceLevel.DIRECT,
            year=1959,
            period="broad_physics",
            relevant_axes=["cross_domain_versatility", "playful_exploration"],
            axis_valence={"cross_domain_versatility": 1.0, "playful_exploration": 0.6},
            tags=["nanotechnology", "cross_domain"],
        ),
        EvidenceRecord(
            id="seed_crossdomain_002",
            content=(
                "Feynman's 1982 paper 'Simulating Physics with Computers' proposed that quantum "
                "systems could only be efficiently simulated by quantum computers\u2014effectively "
                "founding the field of quantum computing. He showed that classical computers "
                "face exponential slowdown simulating quantum mechanics, arguing for 'a quantum "
                "mechanical computer.' This cross-domain leap from physics to computer science "
                "was characteristic of his taste for transferring ideas between fields."
            ),
            source_text="Feynman, 'Simulating Physics with Computers', International Journal of Theoretical Physics 21 (1982)",
            source_type=SourceType.PRIMARY,
            confidence=ConfidenceLevel.DIRECT,
            year=1982,
            period="later_career",
            relevant_axes=["cross_domain_versatility", "computational_pragmatism"],
            axis_valence={"cross_domain_versatility": 1.0, "computational_pragmatism": 0.8},
            tags=["quantum_computing", "cross_domain", "simulation"],
        ),

        # ── Simplicity of Explanation ──────────────────────────────────
        EvidenceRecord(
            id="seed_explain_001",
            content=(
                "The Feynman Lectures on Physics (1964) arose from Feynman's belief that "
                "explanation is the test of understanding. As recalled by colleagues, he once "
                "prepared a freshman lecture on spin-statistics but concluded: 'I couldn't "
                "reduce it to the freshman level. That means we don't really understand it.' "
                "This test\u2014can you explain it simply?\u2014became a defining feature of his taste."
            ),
            source_text="Feynman, 'Feynman Lectures on Physics' (1964), Preface by Feynman; Gleick, 'Genius' (1992)",
            source_type=SourceType.SECONDARY,
            confidence=ConfidenceLevel.STRONG,
            year=1964,
            period="broad_physics",
            relevant_axes=["simplicity_of_explanation"],
            axis_valence={"simplicity_of_explanation": 1.0},
            tags=["feynman_lectures", "teaching", "understanding"],
        ),

        # ── Cross-cutting methodology ──────────────────────────────────
        EvidenceRecord(
            id="seed_methodology_001",
            content=(
                "Krauss (2011) summarizes Feynman's methodological taste: 'Feynman approached "
                "every problem as if he were the first person to think about it. He refused to "
                "read the literature systematically, preferring to work things out for himself. "
                "This sometimes led him to rediscover known results, but it also meant that "
                "when he did find something new, he understood it more deeply than anyone else.' "
                "This encapsulates his taste for independent, bottom-up, intuition-driven science."
            ),
            source_text="Krauss, 'Quantum Man: Richard Feynman's Life in Science' (2011)",
            source_type=SourceType.SECONDARY,
            confidence=ConfidenceLevel.STRONG,
            year=2011,
            relevant_axes=["independent_thinking", "bottom_up_reasoning", "physical_intuition"],
            axis_valence={
                "independent_thinking": 1.0,
                "bottom_up_reasoning": 0.9,
                "physical_intuition": 0.8,
            },
            tags=["methodology", "krauss", "working_style"],
        ),
    ]
