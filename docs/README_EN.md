**🌐 Language:** [中文（默认）](../README.md) | [English](#) | [日本語](./README_JA.md) | [Français](./README_FR.md) | [Deutsch](./README_DE.md)

---

# Feynman-Skill: Feynman Research Taste Modeling System

> **Evidence-based computational modeling of Richard Feynman's scientific research taste.**
> Evaluate, rank, and explain how Feynman would have assessed candidate scientific theories.

## What Is This?

This system models Feynman's **research taste** — his distinctive preferences for certain scientific approaches:

- *"Would Feynman prefer a path-integral approach or an axiomatic formulation?"*
- *"How would Feynman evaluate a purely formal mathematical theory?"*

**NOT role-playing.** Every evaluation is grounded in Feynman's papers, lectures, books, and biographical scholarship.

## The 10 Taste Axes

| # | Axis | Weight | Meaning |
|---|------|--------|---------|
| 1 | **Physical Intuition** | 0.95 | Pictures and visualization over formalism |
| 2 | **Computational Pragmatism** | 0.90 | Can you calculate a number? |
| 3 | **Empirical Ruthlessness** | 0.90 | "If it disagrees with experiment, it is wrong" |
| 4 | **Playful Exploration** | 0.85 | Curiosity-driven, no pressure |
| 5 | **Independent Thinking** | 0.85 | Challenge authority, first principles |
| 6 | **Anti-Formalism** | 0.80 | Distrust pure abstraction |
| 7 | **Bottom-Up Reasoning** | 0.80 | Start from examples, then generalize |
| 8 | **Multiple Representations** | 0.75 | Many views = deeper understanding |
| 9 | **Simplicity of Explanation** | 0.75 | "If you can't explain it to a freshman..." |
| 10 | **Cross-Domain Versatility** | 0.70 | Transfer ideas between fields |

## Quick Start

```bash
git clone https://github.com/ezy1999/Feynman-Skill.git
cd Feynman-Skill
pip install -e ".[dev]"
feynman-taste fetch-data

export ANTHROPIC_API_KEY="your-key"  # optional
python scripts/run_demo_offline.py   # works without API key
```

## Requirements

- Python >= 3.10
- API Key (optional): Anthropic or OpenAI

## License

MIT
