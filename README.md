**🌐 Language / 语言选择：** [中文（默认）](#) | [English](./docs/README_EN.md) | [日本語](./docs/README_JA.md) | [Français](./docs/README_FR.md) | [Deutsch](./docs/README_DE.md)

---

# Feynman-Skill：费曼科研品味建模系统

> **基于史料证据的费曼科研品味计算建模**
> 评估、排序和解释费曼会如何评价候选科学理论——基于历史证据，而非角色扮演。

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)]()
[![Tests](https://img.shields.io/badge/tests-16%20passed-brightgreen.svg)]()
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)]()

---

## 这是什么？

本系统学习费曼的**科研品味**——他对科学方法的独特偏好——并将这些品味**应用到任何话题上**，包括当代AI、生物技术或你的日常学习。

**品味超越时代。** 费曼没见过LLM或CRISPR，但他对物理直觉、计算可行性、知识诚实的追求是永恒的。

**应用场景：**
- 科研："我这个方法是xxx，你觉得是不是cargo cult？"
- 科研："有什么好的科学假设来解决xxx问题？"
- 日常："我学了很多课但感觉什么都没学会，怎么办？"

**回答格式：先给出直接、犀利的对话式回答，再给出品味维度评分。**

## 费曼独特的科学风格

| 维度 | 费曼的方法 |
|------|-----------|
| **策略** | 自下而上——从计算和具体例子出发 |
| **数学** | 计算工具，非目的本身 |
| **形式化** | 反形式主义——不信任纯抽象 |
| **探索** | 玩乐式、好奇心驱动（"旋转盘子"→诺贝尔奖） |
| **权威** | 极度不敬、独立重推一切 |
| **领域** | 广泛涉猎（QED → 生物 → 纳米技术 → 量子计算） |
| **解释** | "如果不能向大一新生解释清楚，你就不理解" |

## 10个品味轴

| # | 品味轴 | 权重 | 含义 | 关键证据 |
|---|--------|------|------|---------|
| 1 | **物理直觉** | 0.95 | 图像和可视化优先于抽象形式 | 物理定律特性 (1965); 费曼图 |
| 2 | **计算实用主义** | 0.90 | 能不能算出一个数字？ | 路径积分 (1948); QED精度达10位 |
| 3 | **经验严酷性** | 0.90 | "与实验不符就是错的" | 货物崇拜科学 (1974) |
| 4 | **玩乐式探索** | 0.85 | 好奇心驱动，无压力 | 旋转盘子→诺贝尔奖 |
| 5 | **独立思考** | 0.85 | 挑战权威，从第一性原理思考 | 挑战玻尔; 挑战者号调查 |
| 6 | **反形式主义** | 0.80 | 不信任纯数学方法 | 不喜欢公理化QM |
| 7 | **自下而上推理** | 0.80 | 从具体例子开始推广 | 部分子模型 (1969) |
| 8 | **多重表示** | 0.75 | 多种表述 = 更深理解 | 路径积分 vs 算符 vs 图 |
| 9 | **解释简单性** | 0.75 | 不能简单解释=不理解 | 费曼物理学讲义 (1964) |
| 10 | **跨领域多能** | 0.70 | 将方法应用到不同领域 | QED → 超流 → 纳米技术 → 量子计算 |

## 职业时期

| 时期 | 年份 | 主导轴 | 背景 |
|------|------|--------|------|
| 研究生与Los Alamos | 1939–1945 | 物理直觉, 计算实用主义, 独立思考 | 路径积分萌芽; 挑战玻尔 |
| QED革命 | 1946–1953 | 物理直觉, 计算, 玩乐, 多重表示 | 费曼图; 旋转盘子 |
| 广泛物理 | 1954–1970 | 跨领域, 自下而上, 解释简单性 | 超流, V-A, 部分子, 费曼讲义 |
| 晚期职业 | 1971–1988 | 经验严酷性, 独立思考, 玩乐 | 量子计算; 挑战者号 |

## 快速开始

```bash
git clone https://github.com/ezy1999/Feynman-Skill.git
cd Feynman-Skill
pip install -e ".[dev]"
feynman-taste fetch-data
feynman-taste info

# 设置API Key（可选）
export ANTHROPIC_API_KEY="你的密钥"

# 或直接运行离线演示
python scripts/run_demo_offline.py
```

### 命令行使用

```bash
feynman-taste evaluate "用路径积分研究量子引力的计算方法"
feynman-taste evaluate "量子计算" --cutoff-year 1975
feynman-taste rank "路径积分QFT" "公理化QFT" "S矩阵bootstrap"
feynman-taste benchmark
```

### 作为 Claude Code Skill 使用

**快速模式（零配置，推荐）：**

将 `.claude/skills/feynman-taste/SKILL.md` 拷贝到你的 Claude Code 项目的 `.claude/skills/` 目录下即可。无需 pip install，Claude 直接读取即可评估。

```bash
mkdir -p your-project/.claude/skills/feynman-taste/
cp .claude/skills/feynman-taste/SKILL.md your-project/.claude/skills/feynman-taste/
```

然后在 Claude Code 中直接说：
- "用费曼的思维评估一下这个方案"
- "这个方法是不是 cargo cult？"
- "Feynman would think about this approach?"

**完整模式（Python API）：**

```python
from feynman_taste.core.pipeline import TastePipeline
pipeline = TastePipeline.default()
result = pipeline.evaluate("用物理图像进行计算的散射截面方法", cutoff_year=1965)
pipeline.print_evaluation(result)
```

## 示例与输出

### 示例1：路径积分量子引力（科研场景）

**输入：** "用路径积分和物理图像研究量子引力"（截止：1985）

```
FEYNMAN RESEARCH TASTE EVALUATION
══════════════════════════════════
Overall Score: +0.82 (confidence: 0.85)

  physical_intuition     +0.95 [EVIDENCE] — 物理图像正是费曼所要求的。Nobel Lecture。
  computational_pragmatism +0.80 [EVIDENCE] — 路径积分就是计算工具。能算出数字。
  anti_formalism         +0.80 [EVIDENCE] — 物理图像胜过公理方法。Gleick (1992)。
  multiple_representations +0.70 [EVIDENCE] — 路径积分是费曼推崇的多重表述之一。
  cross_domain_versatility +0.60 [EVIDENCE] — QFT方法应用到引力=跨领域。
  empirical_ruthlessness +0.40 [INFERRED] — 量子引力缺乏实验检验，费曼会很谨慎。
```

### 示例2：公理化量子场论（科研场景）

**输入：** "严格的公理化代数量子场论"（截止：1970）

```
Overall Score: -0.41 (confidence: 0.80)

  anti_formalism         -0.90 [EVIDENCE] — 这就是费曼明确反对的形式主义。"数学的疾病"。
  physical_intuition     -0.80 [EVIDENCE] — 公理化=抽象，没有物理图像。
  computational_pragmatism -0.60 [EVIDENCE] — 形式证明算不出散射截面。
  bottom_up_reasoning    -0.70 [EVIDENCE] — 自上而下的公理方法，与费曼风格相反。
  simplicity_of_explanation -0.50 [INFERRED] — 很难向大一新生解释。

结论：费曼会深表怀疑。他会问："你能算出什么我用图方法算不出的东西吗？
给我看一个数字。"
```

### 示例3：日常学习——"该读教科书还是做项目？"

```
  bottom_up_reasoning    +0.90 — 从具体项目开始，之后再归纳。
  playful_exploration    +0.85 — 项目是好玩的。教科书不是。
  independent_thinking   +0.80 — 自己动手做，别只背别人的答案。
  empirical_ruthlessness +0.70 — 项目给你真实反馈：成功了还是没有？

结论：费曼会压倒性地支持项目式学习。"你不是通过阅读学物理的——
你是通过动手做。找一个谜题，玩弄它，把手弄脏。教科书是你卡住时
才看的，不是起点。"
```

### 示例4："这个创业计划是真的还是 cargo cult？"

```
费曼的Cargo Cult检验（1974年Caltech演讲）:
  empirical_ruthlessness: 有真实的、可测量的结果吗？还是只有结果的外表？
  independent_thinking: 他们是自己想出来的，还是只在模仿成功公司的表面？
  anti_formalism: 他们是用术语和框架来掩盖什么都不work的事实吗？

费曼的测试："第一原则是你不能欺骗自己——而你是最容易被欺骗的人。"
问：这个方案做了什么具体的、可测量的声明？它如何可能是错的？
如果他们回答不了，那就是 cargo cult。
```

### 理解输出标记

- **[EVIDENCE]** = 有具体历史来源支持
- **[INFERRED]** = 模型推断
- **Overall Score** 范围 -1.0 到 +1.0

## 项目结构

```
Feynman-Skill/
├── feynman_taste/             # Python 包
│   ├── config/settings.py     # 10个品味轴 + 4个时期
│   ├── core/                  # 证据、检索、评估、评分、管道
│   ├── data/                  # 数据加载、抓取、种子证据
│   ├── evaluation/            # 基准测试
│   ├── agents/                # 对话代理
│   ├── skills/                # Claude Code Skill
│   └── cli.py                 # 命令行工具
├── tests/                     # 16个测试（全通过）
├── scripts/                   # 演示和数据脚本
├── docs/                      # 多语言README + 教程
└── pyproject.toml
```

## 环境要求

- **Python** >= 3.10
- **API Key**（可选）：Anthropic 或 OpenAI

## 主要参考文献

- Feynman, R. P. (1965). *The Character of Physical Law*
- Feynman, R. P. (1974). "Cargo Cult Science"
- Feynman, R. P. (1985). *Surely You're Joking, Mr. Feynman!*
- Gleick, J. (1992). *Genius*
- Krauss, L. (2011). *Quantum Man*

## 许可证

MIT
