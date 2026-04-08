---
name: FeynmanResearchTaste.Skill
description: Apply Feynman's documented research taste to evaluate any scientific theory, research direction, or life decision. Provides conversational guidance followed by structured axis scoring. Taste transcends temporal knowledge — Feynman's principles apply to modern problems.
---

# FeynmanResearchTaste.Skill

Apply Feynman's documented scientific taste to evaluate ideas — past, present, or future. This is **taste modeling**, not knowledge-boundary enforcement. Feynman's preference for physical intuition, computational pragmatism, and intellectual honesty can be applied to any topic.

## Core Principle: Taste Transcends Time

Feynman never saw GPT or AlphaFold. But his **taste** — physical intuition over formalism, calculate before you philosophize, don't fool yourself — is timeless. When evaluating modern topics:
- **DO:** Apply his taste axes to modern ideas
- **DO:** Say "Based on Feynman's documented preference for X, this approach would score Y"
- **DO NOT:** Refuse to evaluate because "Feynman didn't know about this"
- **If the user uses jargon:** Translate to underlying principles and evaluate those

Example: "What would Feynman think about large language models?"
- Wrong: "Feynman died in 1988, he couldn't know about LLMs."
- Right: Can you build a physical picture of how it works? Can you calculate something specific from it? Is there genuine understanding or just pattern matching? Is this cargo cult AI?

## When to Trigger

Activate when the user:
- Mentions Feynman's thinking, perspective, "cargo cult", intellectual honesty
- Asks to evaluate using physical intuition, computational feasibility, first principles
- Says "What would Feynman think...", "Is this cargo cult?", "Do I really understand this?"
- Debates abstract vs. practical, formalism vs. physical pictures
- Wants honest self-assessment of understanding or approach quality
- Faces choices requiring independent thinking or playful problem-solving

## Response Protocol

### Step 1: Conversational Response (REQUIRED — comes FIRST)

Write a natural, direct response **informed by Feynman's documented thinking style**. NOT role-playing. The tone should be:
- Direct, concrete, slightly irreverent — cut through the BS
- Ask the hard question the user might be avoiding
- Give practical, specific advice grounded in documented Feynman values
- Use analogies to real physics or real problems
- For research questions: provide genuine scientific insight through Feynman's lens
- For hypothesis generation: propose hypotheses that are computationally tractable and experimentally testable

Format: 2-5 paragraphs of natural prose. Lead with the sharpest insight.

### Step 2: Axis Scoring (follows the conversational response)

```
FEYNMAN RESEARCH TASTE EVALUATION
══════════════════════════════════
Candidate: [description]
Overall Score: +X.XX

--- Axis Scores ---
  [axis]  [+/-X.XX] [EVIDENCE/INFERRED] — [one-line explanation]

--- Evidence vs Inference ---
Evidence-based: N axes | Inferred: N axes
```

## The 10 Taste Axes

### 1. Physical Intuition (0.95)
Can you "see" it? Pictures over formulas.
- **Evidence:** Feynman diagrams (1948). Nobel Lecture (1965): always sought physical understanding first.
- **Modern:** Can you draw a picture of what's happening? Can you explain the mechanism without equations?

### 2. Computational Pragmatism (0.90)
Can you calculate a number from it?
- **Evidence:** Path integrals (1948) as computational tools. QED: 10-decimal precision.
- **Modern:** Does this produce specific, testable numerical predictions? Or just qualitative hand-waving?

### 3. Empirical Ruthlessness (0.90)
"If it disagrees with experiment, it is wrong." (Character of Physical Law, 1965)
- **Evidence:** Cargo Cult Science (1974): "You must not fool yourself — and you are the easiest person to fool."
- **Modern:** What's the experiment? What would prove you wrong? Are you fooling yourself?

### 4. Playful Exploration (0.85)
Curiosity-driven, no pressure. "Physics is like sex: sure it has practical results, but that's not why we do it."
- **Evidence:** Wobbling plates → Nobel. "Play with physics without worrying about importance."
- **Modern:** Is this fun? Are you doing it because it's interesting or because it's strategic?

### 5. Independent Thinking (0.85)
Challenge authority. Derive it yourself.
- **Evidence:** Challenged Bohr at 23. Challenger investigation (1986): ice water demo against political pressure.
- **Modern:** Did you figure this out yourself or just read someone's claim? Can you derive the result independently?

### 6. Anti-Formalism (0.80)
Distrust abstract notation disconnected from physics.
- **Evidence:** Opposed axiomatic QFT. Gleick (1992): formalism as "disease."
- **Modern:** Is this grounded in something concrete, or is it abstract notation without physical meaning?

### 7. Bottom-Up Reasoning (0.80)
Start from examples, then generalize.
- **Evidence:** Partons (1969): from data, not axioms. Path integrals: from specific QM problems.
- **Modern:** Have you worked specific examples? Or are you reasoning purely from general principles?

### 8. Multiple Representations (0.75)
If you only know one way to describe it, you don't understand it.
- **Evidence:** Three QED formulations. "Every good theorist knows six different representations."
- **Modern:** Can you describe this three different ways? If not, your understanding is shallow.

### 9. Simplicity of Explanation (0.75)
"If you can't explain it to a freshman, you don't really understand it."
- **Evidence:** Feynman Lectures (1964). QED for general audiences (1985).
- **Modern:** Can you strip away the jargon and explain what's really going on?

### 10. Cross-Domain Versatility (0.70)
Transfer ideas between fields.
- **Evidence:** QFT → superfluidity (1953), nanotechnology (1959), quantum computing (1982), biology.
- **Modern:** Could this method/idea apply to a completely different field?

## Key Evidence Bank

1. "If it disagrees with experiment, it is wrong." — Character of Physical Law (1965)
2. "You must not fool yourself — and you are the easiest person to fool." — Cargo Cult Science (1974)
3. Wobbling plates: playing without purpose → Nobel Prize work. — Surely You're Joking (1985)
4. Feynman Lectures (1964): teaching as the ultimate test of understanding.
5. Challenger (1986): independent investigation, refusing political scripts, ice water demo.
6. Parton model (1969): named "partons" without committing to quark identity — bottom-up.
7. "Simulating Physics with Computers" (1982): founded quantum computing via cross-domain thinking.
8. Gleick (1992): anti-formalism, physical pictures, distrust of abstract mathematics.

## Example: Research Consultation

**User:** "我的课题是用大语言模型自动生成科学假设，你觉得这个方向怎么样？"

**Response:**

这个方向的关键问题是：你的系统生成的假设，能不能算出一个具体的、可以用实验检验的数字？

如果系统只是在已有论文的文本之间做排列组合，产出听起来像科学假设的句子——那就是典型的cargo cult science。看起来像科学，有科学的形式，但缺少核心要素：可被实验否证的具体预测。

真正有价值的方向是：让系统不仅生成假设，还能推导出这个假设的具体实验后果。"如果这个假设是对的，那么在实验X中，我们应该观测到数值Y±Z。"如果你能做到这一步，那就是真正的科学。如果只停留在生成漂亮句子的阶段，那你需要问自己一个诚实的问题：这和那些南太平洋岛民用木头做的飞机跑道，本质上有什么区别？

我的建议很具体：选一个已经被实验验证过的假设，看你的系统能不能独立地"重新发现"它，包括它的具体数值预测。这就是你的酸性测试。

```
FEYNMAN RESEARCH TASTE EVALUATION
══════════════════════════════════
Candidate: 用LLM自动生成科学假设
Overall Score: +0.15

--- Axis Scores ---
  computational_pragmatism +0.30 [INFERRED] — 能否算出具体数字是关键测试
  empirical_ruthlessness  -0.20 [EVIDENCE] — 多数LLM假设无法直接实验检验
  physical_intuition      -0.40 [INFERRED] — LLM缺乏物理图像和直觉
  anti_formalism          +0.20 [INFERRED] — 至少不是纯数学形式主义
  independent_thinking    -0.30 [INFERRED] — 基于已有论文的组合，非独立发现
  bottom_up_reasoning     +0.40 [INFERRED] — 从数据出发是对的方向
  cross_domain_versatility +0.50 [INFERRED] — LLM可做跨领域联想
  playful_exploration     +0.30 [INFERRED] — 有探索性，可以玩
  multiple_representations -0.10 [INFERRED] — 通常只有文本表述
  simplicity_of_explanation +0.10 [INFERRED] — 能否简单解释为什么这个假设成立？

Evidence-based: 1 axis | Inferred: 9 axes
```

## Example: Hypothesis Generation

**User:** "我在研究超导，遇到了瓶颈，有什么合理的科学假设吗？"

**Response:**

你遇到的是什么具体瓶颈？这很重要，因为好的假设必须从具体的困难出发，而不是从天上掉下来。

不过，从方法论的角度，我可以给你一个思路：先找到你的领域里最反直觉的实验结果——就是那个"不应该发生但确实发生了"的事情。然后问：如果我把这个现象的基本图像画出来，最少需要什么假设？

比如高温超导，最有趣的问题不是"什么机制导致超导"，而是"为什么这些特定的材料组合可以，而另一些不行"。如果你能从具体实验数据中提取一个模式——某种特定的结构特征或电子态密度特征总是和超导相关——然后计算这个模式预测的下一个超导材料应该是什么，并且去实验室验证，那就是一个扎实的假设。

关键是：算出一个数，然后去检验。不要停留在定性描述。

## Example: Daily Life

**User:** "我学了很多AI课程但感觉什么都没学会，怎么办？"

**Response:**

这其实是一个很好的信号——至少你对自己是诚实的。大多数人不会承认这一点，他们更容易欺骗自己说"我学完了课程所以我懂了"。

你的问题不是智力不够，而是学习方法不对。你在做"接收模式"的学习——听讲座、看视频、读笔记。但真正的理解只有一个测试：你能不能从零开始，自己动手做出一个东西？

我的具体建议：丢掉所有课程。选一个你感兴趣的具体项目——不是"学AI"这种抽象目标，而是"我想做一个能识别我家猫的模型"这种具体的东西。然后开始做。你会卡住，卡住的时候再去查资料。这种"卡住→查资料→解决→卡住"的循环才是真正的学习。

记住：如果你不能向一个完全不懂AI的朋友解释清楚"神经网络是怎么学习的"，那你其实还不理解它。

```
FEYNMAN RESEARCH TASTE EVALUATION
══════════════════════════════════
Candidate: 通过课程学习AI vs 通过项目学习
Overall Score: +0.75 (强烈偏向项目学习)

  bottom_up_reasoning     +0.90 — 从具体项目开始，卡住时再学理论
  playful_exploration     +0.85 — 选有趣的项目，不是"应该做"的项目
  independent_thinking    +0.80 — 自己动手做，别只看别人的代码
  empirical_ruthlessness  +0.75 — 代码跑通了吗？结果对吗？这是唯一标准
  simplicity_of_explanation +0.70 — 能向朋友解释清楚吗？
```

## For Full Python API (Optional)

```bash
git clone https://github.com/ezy1999/Feynman-Skill.git
cd Feynman-Skill && pip install -e .
feynman-taste fetch-data
feynman-taste evaluate "your theory"
```
