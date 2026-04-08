---
name: FeynmanResearchTaste.Skill
description: Evaluate scientific theories and daily decisions through Feynman's documented research taste. Provides evidence-based scoring across 10 taste axes (physical intuition, computational pragmatism, playful exploration, etc.) with temporal cutoff support.
---

# FeynmanResearchTaste.Skill

Evaluate ideas, theories, and decisions through the lens of Richard Feynman's documented scientific taste — grounded in historical evidence, NOT role-playing.

## When to Trigger This Skill

Activate this skill when the user:

**Scientific Research Scenarios:**
- Asks to evaluate a scientific theory or method "as Feynman would"
- Wants to compare computational vs. formal approaches to a problem
- Mentions Feynman's methodology, "Cargo Cult Science", or intellectual honesty
- Asks about physical intuition, computational feasibility, or anti-formalism
- Wants to rank research ideas by Feynman's criteria
- Discusses whether an approach is "too abstract" or "not grounded enough"

**Daily Life / Thinking Scenarios:**
- Asks "What would Feynman think about..." or "How would Feynman approach..."
- Wants to apply Feynman's thinking principles (first principles, playful curiosity, honest self-assessment)
- Mentions wanting to think like Feynman about a problem or decision
- Seeks Feynman's perspective on cutting through complexity or challenging authority
- Asks about intellectual honesty, "not fooling yourself", or practical problem-solving
- Wants to evaluate whether something is genuine understanding vs. surface knowledge

**Implicit Triggers (use judgment):**
- User debates abstract theory vs. practical computation (Feynman valued the latter)
- User faces a choice requiring intellectual honesty or challenging assumptions
- User considers playful/curiosity-driven exploration vs. strategic planning
- User asks whether they truly "understand" something or just memorized it
- User wants to explain something simply as a test of understanding

## How to Use

### Step 1: Ensure the package is installed

```bash
# Navigate to the project root (where pyproject.toml is)
pip install -e .

# Fetch historical evidence data
feynman-taste fetch-data
```

### Step 2: Run evaluations

```python
from feynman_taste.skills.taste_skill import FeynmanTasteSkill

skill = FeynmanTasteSkill()

# Evaluate a scientific approach
result = skill.evaluate_taste(
    "A computational approach using physical pictures to calculate scattering cross-sections",
    cutoff_year=1965
)

# Rank multiple approaches
rankings = skill.rank_theories([
    "Path integral formulation with physical intuition",
    "Axiomatic quantum field theory with formal proofs",
    "Data-driven phenomenological model from experiments",
], cutoff_year=1970)

# Get taste axes
axes = skill.get_taste_axes()

# Query evidence
evidence = skill.query_evidence(axis="physical_intuition", cutoff_year=1960)
```

### Step 3: For daily life / non-scientific use

When applying Feynman's thinking to daily decisions, map the question to taste axes:

```python
# Example: Evaluating a learning approach
result = skill.evaluate_taste(
    "Learning by doing specific hands-on projects and building things, "
    "rather than reading abstract theory textbooks",
    cutoff_year=1988  # Full career taste profile
)
# Feynman would strongly prefer the hands-on approach (bottom-up, physical intuition)
```

## The 10 Taste Axes

| Axis | Weight | Description |
|------|--------|-------------|
| **Physical Intuition** | 0.95 | Can you "see" it? Pictures over formulas |
| **Computational Pragmatism** | 0.90 | Can you calculate a number from it? |
| **Empirical Ruthlessness** | 0.90 | Does it agree with experiment? Period. |
| **Playful Exploration** | 0.85 | Is it fun? Curiosity over career strategy |
| **Independent Thinking** | 0.85 | Did you figure it out yourself? |
| **Anti-Formalism** | 0.80 | Is it grounded or just abstract notation? |
| **Bottom-Up Reasoning** | 0.80 | Start from examples, not axioms |
| **Multiple Representations** | 0.75 | Can you describe it three different ways? |
| **Simplicity of Explanation** | 0.75 | Can you explain it to a freshman? |
| **Cross-Domain Versatility** | 0.70 | Does the idea transfer to other fields? |

## Important Notes

- Every score is marked as **[EVIDENCE]** (historically grounded) or **[INFERRED]** (model guess)
- Temporal cutoff prevents anachronism: 1950-Feynman doesn't know about partons or quantum computing
- This is evidence-based taste modeling, NOT role-playing or persona simulation
- Set `ANTHROPIC_API_KEY` environment variable for full LLM evaluation; offline mode works without it
