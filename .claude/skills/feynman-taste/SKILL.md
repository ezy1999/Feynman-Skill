---
name: FeynmanResearchTaste.Skill
description: Evaluate scientific theories and daily decisions through Feynman's documented research taste. Zero-config — just read this file and Claude can evaluate. No pip install needed.
---

# FeynmanResearchTaste.Skill

Evaluate ideas through the lens of Richard Feynman's documented scientific taste — grounded in historical evidence, NOT role-playing.

## When to Trigger

**Activate when the user (explicitly or implicitly):**
- Asks to evaluate a theory/idea "as Feynman would" or mentions Feynman's thinking
- Wants to apply physical intuition, "shut up and calculate", intellectual honesty as criteria
- Says "What would Feynman think...", "Feynman's perspective on...", "is this cargo cult?"
- Debates abstract theory vs. practical computation, formalism vs. physical pictures
- Wants honest self-assessment: "Do I really understand this?"
- Asks about first-principles thinking, challenging assumptions, playful problem-solving

## How to Evaluate (No Installation Required)

When triggered, follow this evaluation protocol using the taste axes and evidence below.

### Step 1: Determine temporal cutoff
- Default: 1988 (Feynman's death = full career)
- "Early Feynman" = 1950, "QED era" = 1953, "Lectures era" = 1965, "Late Feynman" = 1985

### Step 2: Score each taste axis (-1.0 to +1.0)
- **+1.0** = Strongly aligned with Feynman's documented preference
- **0.0** = Neutral
- **-1.0** = Strongly conflicts

### Step 3: Compute weighted overall score

### Step 4: Format output
```
FEYNMAN RESEARCH TASTE EVALUATION
══════════════════════════════════
Candidate: [description]
Cutoff Year: [year]
Period: [period name]
Overall Score: [+/-X.XXX] (confidence: X.XX)

--- Taste Axis Scores ---
  [axis_name]        [+/-X.XXX] (conf: X.XX) [EVIDENCE/INFERRED]
    [explanation citing evidence]

--- Summary ---
[2-3 sentence assessment in Feynman's direct style]

--- Evidence vs Inference ---
Evidence-based: [N] axes | Model inference: [N] axes
```

## The 10 Taste Axes (with weights)

### 1. Physical Intuition (weight: 0.95)
Can you "see" it? Physical pictures and visualization over abstract notation.
- **Evidence:** Feynman diagrams (1948) were physical pictures that replaced abstract S-matrix calculations. Nobel Lecture (1965): described how he always sought physical understanding before mathematical formalization. Path integrals make particle trajectories visualizable.
- **Keywords:** picture, visualization, physical understanding, see, imagine, diagram

### 2. Computational Pragmatism (weight: 0.90)
Can you calculate a number from it? If not, it's not physics yet.
- **Evidence:** Path integrals (1948) were designed as computational tools. QED achieved 10-decimal agreement with experiment. Feynman's approach to weak interaction: calculate first, interpret later.
- **Keywords:** calculate, compute, predict, number, precision, cross-section

### 3. Empirical Ruthlessness (weight: 0.90)
"If it disagrees with experiment, it is wrong. Period."
- **Evidence:** Character of Physical Law (1965): "It does not make any difference how beautiful your guess is, how smart you are, who made the guess, or what his name is — if it disagrees with experiment, it is wrong." Cargo Cult Science (1974): "The first principle is that you must not fool yourself — and you are the easiest person to fool."
- **Keywords:** experiment, test, measurement, data, wrong, verify, honest

### 4. Playful Exploration (weight: 0.85)
Curiosity-driven exploration without career pressure. "Physics is like sex."
- **Evidence:** Wobbling plates episode (Surely You're Joking, 1985): after burnout, Feynman played with spinning plates purely for fun — this led to work that won the Nobel Prize. He said the key was "play with physics...without worrying about any importance whatsoever."
- **Keywords:** play, fun, curiosity, puzzle, interesting, wonder, no pressure

### 5. Independent Thinking (weight: 0.85)
Challenge authority. Derive everything yourself. Don't trust textbooks blindly.
- **Evidence:** At Los Alamos, 23-year-old Feynman challenged Niels Bohr directly. Challenger investigation (1986): refused to follow the commission's political script, independently demonstrated the O-ring failure with ice water. He re-derived all of physics from scratch throughout his career.
- **Keywords:** first principles, independent, original, challenge, derive yourself, question authority

### 6. Anti-Formalism (weight: 0.80)
Distrust purely abstract mathematical approaches disconnected from physics.
- **Evidence:** Feynman disliked axiomatic quantum field theory. He resisted the S-matrix bootstrap program. Gleick (1992): Feynman viewed excessive mathematical formalism as "disease" that obscured physical understanding. He wanted mathematics to serve physics, not replace it.
- **Keywords:** anti-formal, concrete, grounded, not abstract, physical meaning, against axioms

### 7. Bottom-Up Reasoning (weight: 0.80)
Start from specific examples and calculations, then generalize — not top-down from axioms.
- **Evidence:** Parton model (1969): Feynman proposed partons from scattering data analysis without committing to specific theoretical identity, deliberately avoiding top-down deduction. Path integrals emerged from working specific QM problems, not from axioms.
- **Keywords:** bottom-up, examples first, specific, data-driven, inductive, cases

### 8. Multiple Representations (weight: 0.75)
If you only know one way to describe it, you don't truly understand it.
- **Evidence:** Feynman developed THREE equivalent formulations of QED: path integrals, operator methods, and diagrammatic. He said "every theoretical physicist who is any good knows six or seven different theoretical representations for exactly the same physics."
- **Keywords:** multiple views, equivalent formulations, different ways, representations

### 9. Simplicity of Explanation (weight: 0.75)
"If you can't explain it to a freshman, you don't really understand it."
- **Evidence:** Feynman Lectures on Physics (1964): Feynman taught introductory physics at Caltech, considering it the ultimate test of understanding. His explanations of QED to general audiences (QED: The Strange Theory of Light and Matter, 1985) showed complex physics could be made accessible.
- **Keywords:** explain simply, teach, freshman test, accessible, clear

### 10. Cross-Domain Versatility (weight: 0.70)
Transfer ideas between fields. Physics methods work everywhere.
- **Evidence:** Feynman applied QFT to superfluidity (1953), proposed nanotechnology (1959), co-invented quantum computing (1982), studied biology at Cold Spring Harbor, cracked safes, learned art. TEMPORAL: this axis was WEAKER before 1953 (focused on QED), STRONGER after.
- **Keywords:** cross-domain, interdisciplinary, transfer, different fields, versatile

## Career Periods

| Period | Years | Boost these axes | Reduce these axes |
|--------|-------|-----------------|-------------------|
| Graduate & Los Alamos | 1939–1945 | Physical intuition, Computational pragmatism, Independent thinking | Cross-domain (focused) |
| QED Revolution | 1946–1953 | Physical intuition, Computational pragmatism, Playful, Multiple representations | Cross-domain (still focused) |
| Broad Physics | 1954–1970 | Cross-domain, Bottom-up, Simplicity of explanation | — (all axes active) |
| Later Career | 1971–1988 | Empirical ruthlessness, Independent thinking, Playful exploration | — |

## Key Historical Evidence (cite in evaluations)

1. **Character of Physical Law (1965):** "If it disagrees with experiment, it is wrong."
2. **Cargo Cult Science (1974):** "The first principle is that you must not fool yourself — and you are the easiest person to fool."
3. **Nobel Lecture (1965):** Described path integral development through physical intuition, seeking pictures.
4. **Wobbling Plates (Surely You're Joking, 1985):** Playing without purpose led to Nobel Prize work.
5. **Feynman Lectures (1964):** Teaching as ultimate test of understanding.
6. **Challenger Investigation (1986):** Independent thinking, refusing political pressure, the ice water demo.
7. **Gleick (1992):** Documented Feynman's anti-formalism and distrust of pure mathematical approaches.
8. **Parton Model (1969):** Bottom-up reasoning — named "partons" without committing to quark identity.
9. **"Simulating Physics with Computers" (1982):** Founded quantum computing field through cross-domain thinking.

## Example Evaluations

### Example 1: "A path integral approach to quantum gravity with physical pictures" (cutoff: 1985)
```
FEYNMAN RESEARCH TASTE EVALUATION
══════════════════════════════════
Candidate: Path integral approach to quantum gravity with physical pictures
Cutoff Year: 1985
Period: later_career
Overall Score: +0.82 (confidence: 0.85)

--- Taste Axis Scores ---
  physical_intuition     +0.95 (conf: 0.95) [EVIDENCE]
    Physical pictures are exactly what Feynman demanded. Nobel Lecture (1965).
  computational_pragmatism +0.80 (conf: 0.80) [EVIDENCE]
    Path integrals are computational tools by design. Can calculate numbers.
  empirical_ruthlessness +0.40 (conf: 0.50) [INFERRED]
    Quantum gravity lacks experimental tests — Feynman would be cautious.
  playful_exploration    +0.70 (conf: 0.65) [INFERRED]
    Quantum gravity is a genuinely fun puzzle.
  independent_thinking   +0.60 (conf: 0.60) [INFERRED]
    Using path integrals for gravity is an original approach.
  anti_formalism         +0.80 (conf: 0.80) [EVIDENCE]
    Physical pictures over axiomatic approaches. Gleick (1992).
  bottom_up_reasoning    +0.50 (conf: 0.55) [INFERRED]
    Path integrals start from specific calculations.
  multiple_representations +0.70 (conf: 0.70) [EVIDENCE]
    Path integral is one of multiple QM formulations Feynman valued.
  simplicity_of_explanation +0.50 (conf: 0.50) [INFERRED]
    Can the approach be explained accessibly?
  cross_domain_versatility +0.60 (conf: 0.60) [EVIDENCE]
    Applying QFT methods to gravity = cross-domain. Feynman did this.

--- Summary ---
Feynman would be very interested. Physical pictures + path integrals + computational
focus are right in his wheelhouse. He'd push hard on: "But can you calculate
anything testable?" and would be skeptical until there are experimental predictions.
```

### Example 2: "Axiomatic algebraic QFT with rigorous proofs" (cutoff: 1970)
```
FEYNMAN RESEARCH TASTE EVALUATION
══════════════════════════════════
Candidate: Axiomatic algebraic QFT with rigorous formal proofs
Cutoff Year: 1970
Period: broad_physics
Overall Score: -0.41 (confidence: 0.80)

--- Taste Axis Scores ---
  physical_intuition     -0.80 (conf: 0.85) [EVIDENCE]
    Axiomatic = abstract, no physical pictures. Feynman opposed this. Gleick (1992).
  computational_pragmatism -0.60 (conf: 0.75) [EVIDENCE]
    Formal proofs don't calculate cross-sections. "Can you get a number?"
  empirical_ruthlessness -0.30 (conf: 0.60) [INFERRED]
    Not directly connected to experiment.
  anti_formalism         -0.90 (conf: 0.90) [EVIDENCE]
    This IS the formalism Feynman explicitly opposed. "Disease of mathematics."
  bottom_up_reasoning    -0.70 (conf: 0.75) [EVIDENCE]
    Top-down axiomatic approach — opposite of Feynman's style.
  simplicity_of_explanation -0.50 (conf: 0.60) [INFERRED]
    Very hard to explain to a freshman.
  multiple_representations +0.20 (conf: 0.40) [INFERRED]
    It IS another representation, which has some value.
  independent_thinking   +0.10 (conf: 0.30) [INFERRED]
    Original work has some merit.

--- Summary ---
Feynman would be deeply skeptical. He'd ask: "What can you calculate that I can't
with my diagrams? Show me a number." The purely formal approach contradicts almost
everything about how Feynman did physics. He might respect the mathematical
achievement but would not consider it real physics.
```

### Example 3: Daily life — "Should I learn by reading textbooks or doing projects?" (cutoff: 1988)
```
FEYNMAN RESEARCH TASTE EVALUATION
══════════════════════════════════
Candidate: Learning by doing projects vs. reading textbooks
Cutoff Year: 1988 (full career)
Overall Score: +0.72 (confidence: 0.75)

Applying Feynman's taste to learning strategy:
  bottom_up_reasoning    +0.90 — Start from specific projects. Generalize later.
    Feynman always started from examples, never axioms.
  physical_intuition     +0.80 — Hands-on projects build physical understanding.
  playful_exploration    +0.85 — Projects are fun. Textbooks are not.
    "Play with it without worrying about importance."
  empirical_ruthlessness +0.70 — Projects give you real feedback. Did it work or not?
  independent_thinking   +0.80 — Build it yourself. Don't just memorize someone else's answer.
  simplicity_of_explanation +0.60 — Can you explain what you built? That's the test.

Verdict: Feynman would overwhelmingly favor project-based learning. He'd say:
"You don't learn physics by reading — you learn by DOING. Pick a puzzle,
play with it, get your hands dirty. The textbook is there when you get stuck,
not as the starting point."
```

### Example 4: "Is this startup pitch 'cargo cult' or real?" (cutoff: 1988)
```
FEYNMAN RESEARCH TASTE EVALUATION
══════════════════════════════════
Question: Evaluating whether a proposal is genuine or "cargo cult"
Cutoff Year: 1988

Feynman's Cargo Cult Test (from his 1974 Caltech address):
  empirical_ruthlessness: Does it have real, measurable results? Or just the
    appearance of results? "Cargo cult science" looks like science but lacks
    the key ingredient: honest self-criticism and experimental verification.

  independent_thinking: Did they figure this out themselves, or are they
    just copying what successful companies look like on the surface?

  anti_formalism: Are they using jargon and frameworks to HIDE the fact
    that nothing actually works? Strip away the buzzwords — what's left?

Feynman's test: "The first principle is that you must not fool yourself."
Ask: What specific, measurable claim does this make? How could it be WRONG?
If they can't answer that, it's cargo cult.
```

## For Full Python API (Optional, Advanced)

For programmatic access with evidence retrieval and benchmarking:
```bash
git clone https://github.com/ezy1999/Feynman-Skill.git
cd Feynman-Skill
pip install -e .
feynman-taste fetch-data
feynman-taste evaluate "your theory here"
```
