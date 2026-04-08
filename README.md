# Feynman Research Taste Modeling System

> **Evidence-based computational modeling of Richard Feynman's scientific research taste.**
> Evaluate, rank, and explain how Feynman would have assessed candidate scientific theories — grounded in historical evidence, not role-playing.

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)]()
[![Tests](https://img.shields.io/badge/tests-16%20passed-brightgreen.svg)]()
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)]()

---

## What Is This?

This system models Richard Feynman's **research taste** — his distinctive preferences for certain kinds of scientific approaches. It answers questions like:

- *"Would Feynman prefer a path-integral approach or an axiomatic formulation?"*
- *"How would Feynman evaluate a purely formal mathematical theory?"*
- *"Would 1950s Feynman or 1980s Feynman be more interested in cross-domain work?"*

**This is NOT role-playing.** Every evaluation is grounded in documented evidence from Feynman's published papers, lectures, books, and biographical scholarship.

## Feynman's Distinctive Scientific Style

Feynman's approach to science was unique and recognizable:

| Dimension | Feynman's Approach |
|-----------|-------------------|
| **Strategy** | Bottom-up: start from calculations and specific examples |
| **Math** | Tool for getting numbers, not an end in itself |
| **Formalism** | Anti-formalist — distrusted pure abstraction |
| **Exploration** | Playful, curiosity-driven ("wobbling plates" → Nobel Prize) |
| **Authority** | Fiercely irreverent, re-derived everything from scratch |
| **Domains** | Broad versatility (QED → biology → nanotech → quantum computing) |
| **Explanation** | "If you can't explain it to a freshman, you don't understand it" |

## The 10 Taste Axes

| # | Axis | Weight | What It Means | Key Evidence |
|---|------|--------|---------------|-------------|
| 1 | **Physical Intuition** | 0.95 | Pictures and visualization over abstract formalism | Character of Physical Law (1965); Feynman diagrams |
| 2 | **Computational Pragmatism** | 0.90 | Can you actually calculate a number? | Path integrals (1948); QED precision to 10 decimals |
| 3 | **Empirical Ruthlessness** | 0.90 | "If it disagrees with experiment, it is wrong" | Cargo Cult Science (1974); Character of Physical Law |
| 4 | **Playful Exploration** | 0.85 | Curiosity-driven, no pressure, just fun | Wobbling plates → Nobel Prize; "Surely You're Joking" |
| 5 | **Independent Thinking** | 0.85 | Challenge authority, think from first principles | Challenging Bohr at Los Alamos; Challenger investigation |
| 6 | **Anti-Formalism** | 0.80 | Distrust purely mathematical approaches | Dislike of axiomatic QM; resistance to S-matrix theory |
| 7 | **Bottom-Up Reasoning** | 0.80 | Start from examples, then generalize | Parton model (1969): data first, theory second |
| 8 | **Multiple Representations** | 0.75 | Multiple formulations = deeper understanding | Path integral vs operator vs diagrams for same physics |
| 9 | **Simplicity of Explanation** | 0.75 | "If you can't explain it to a freshman, you don't understand it" | Feynman Lectures (1964); QED popular book (1985) |
| 10 | **Cross-Domain Versatility** | 0.70 | Apply methods across very different fields | QED → superfluidity → partons → nanotech → quantum computing |

## Career Periods

| Period | Years | Dominant Axes | Context |
|--------|-------|---------------|---------|
| Graduate & Los Alamos | 1939–1945 | Physical intuition, Computational pragmatism, Independence | Path integral genesis; challenging Bohr |
| QED Revolution | 1946–1953 | Physical intuition, Computation, Play, Multiple representations | Feynman diagrams; wobbling plates; Nobel work |
| Broad Physics | 1954–1970 | Cross-domain, Bottom-up, Simplicity of explanation | Superfluidity, V-A, partons, Feynman Lectures, Nobel Prize |
| Later Career | 1971–1988 | Empirical ruthlessness, Independence, Play | Quantum computing vision; Challenger; Cargo Cult Science |

## Quick Start

### Installation

```bash
cd FeynmanResearchTaste
pip install -e ".[dev]"
feynman-taste fetch-data
feynman-taste info
```

### Set Up API Key (optional)

```bash
export ANTHROPIC_API_KEY="your-key-here"
```

Offline demo works without a key:
```bash
python scripts/run_demo_offline.py
```

### CLI Usage

```bash
# Evaluate a theory
feynman-taste evaluate "A computational approach to quantum gravity using path integrals"

# Evaluate at a specific year
feynman-taste evaluate "quantum computing" --cutoff-year 1975

# Rank candidates
feynman-taste rank "path integral QFT" "axiomatic QFT" "S-matrix bootstrap"

# Compare two approaches
feynman-taste compare "data-driven analysis" "formal mathematical proof"

# Run benchmark
feynman-taste benchmark
```

### Python API

```python
from feynman_taste.core.pipeline import TastePipeline

pipeline = TastePipeline.default()

result = pipeline.evaluate(
    "A playful computational approach using physical pictures to calculate cross-sections",
    cutoff_year=1965
)
pipeline.print_evaluation(result)

ranked = pipeline.rank_candidates([
    "Path integral formulation with physical intuition",
    "Axiomatic quantum field theory with formal proofs",
    "Data-driven phenomenological model",
], cutoff_year=1970)
```

## Project Structure

```
FeynmanResearchTaste/
├── feynman_taste/                  # Main Python package
│   ├── config/settings.py          # 10 taste axes, 4 periods, config
│   ├── core/
│   │   ├── evidence.py             # Evidence data model + store
│   │   ├── retriever.py            # RAG evidence retrieval
│   │   ├── evaluator.py            # LLM-based evaluation
│   │   ├── taste_model.py          # Scoring + aggregation
│   │   └── pipeline.py             # End-to-end orchestration
│   ├── data/
│   │   ├── seed_evidence.py        # 16 built-in evidence records
│   │   ├── fetcher.py              # Online data fetching
│   │   └── loader.py               # Data I/O
│   ├── evaluation/benchmark.py     # 6 benchmark cases
│   ├── agents/taste_agent.py       # Conversational agent
│   ├── skills/taste_skill.py       # Claude Code skill wrapper
│   └── cli.py                      # Command-line interface
├── tests/                          # 16 tests (all passing)
├── scripts/                        # Demo + data scripts
├── .claude/skills/feynman-taste/   # Claude Code skill definition
├── pyproject.toml
└── README.md
```

## Understanding the Output

```
FEYNMAN RESEARCH TASTE EVALUATION
==================================================================
Candidate: A computational approach using physical intuition...
Cutoff Year: 1965
Active Period: broad_physics

Overall Score: +0.388 (confidence: 0.57)

--- Taste Axis Scores ---
  physical_intuition        +1.000 (conf: 1.00) [EVIDENCE]
  computational_pragmatism  +1.000 (conf: 1.00) [EVIDENCE]
  empirical_ruthlessness    +1.000 (conf: 1.00) [EVIDENCE]
  anti_formalism            -0.100 (conf: 0.30) [INFERRED]
```

- **[EVIDENCE]** = Score backed by specific historical sources
- **[INFERRED]** = Model's inference, no direct evidence
- **Overall Score** ranges from -1.0 (strongly against Feynman's taste) to +1.0 (strongly aligned)

## Key References

- Feynman, R. P. (1965). *The Character of Physical Law*
- Feynman, R. P. (1974). "Cargo Cult Science" (Caltech Commencement)
- Feynman, R. P. (1985). *Surely You're Joking, Mr. Feynman!*
- Gleick, J. (1992). *Genius: The Life and Science of Richard Feynman*
- Krauss, L. (2011). *Quantum Man: Richard Feynman's Life in Science*
- Schweber, S. S. (1994). *QED and the Men Who Made It*
- Dyson, F. (1979). *Disturbing the Universe*

## License

MIT
