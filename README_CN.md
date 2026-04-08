# Feynman 科研品味建模系统

> **基于史料证据的费曼科研品味计算建模**
> 评估、排序和解释费曼会如何评价候选科学理论——基于历史证据，而非角色扮演。

---

## 这是什么？

本系统对理查德·费曼的**科研品味**进行建模——即他对不同科学方法和理论的独特偏好。例如：

- *"费曼会更喜欢路径积分方法还是公理化量子力学？"*
- *"费曼会如何评价一个纯形式化的数学理论？"*
- *"1950年代的费曼和1980年代的费曼，谁对跨领域研究更感兴趣？"*

**这不是角色扮演。** 每个评估都以费曼的发表论文、演讲、书籍和传记学术研究为证据基础。

## 费曼独特的科学风格

费曼的科学方法独树一帜：

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
| 2 | **计算实用主义** | 0.90 | 能不能算出一个数字？ | 路径积分 (1948); QED精度达10位小数 |
| 3 | **经验严酷性** | 0.90 | "与实验不符就是错的" | 货物崇拜科学 (1974) |
| 4 | **玩乐式探索** | 0.85 | 好奇心驱动，无压力 | 旋转盘子→诺贝尔奖; "别闹了，费曼先生" |
| 5 | **独立思考** | 0.85 | 挑战权威，从第一性原理思考 | 在Los Alamos挑战玻尔; 挑战者号调查 |
| 6 | **反形式主义** | 0.80 | 不信任纯数学方法 | 不喜欢公理化QM; 抵制S矩阵理论 |
| 7 | **自下而上推理** | 0.80 | 从具体例子开始，然后推广 | 部分子模型 (1969): 先看数据，再做理论 |
| 8 | **多重表示** | 0.75 | 多种表述 = 更深理解 | 路径积分 vs 算符 vs 图 |
| 9 | **解释简单性** | 0.75 | "如果不能向大一新生解释，你就不理解" | 费曼物理学讲义 (1964) |
| 10 | **跨领域多能** | 0.70 | 将方法应用到完全不同的领域 | QED → 超流 → 纳米技术 → 量子计算 |

## 职业时期

| 时期 | 年份 | 主导轴 | 背景 |
|------|------|--------|------|
| 研究生与Los Alamos | 1939–1945 | 物理直觉, 计算实用主义, 独立思考 | 路径积分萌芽; 挑战玻尔 |
| QED革命 | 1946–1953 | 物理直觉, 计算, 玩乐, 多重表示 | 费曼图; 旋转盘子; 诺贝尔奖工作 |
| 广泛物理 | 1954–1970 | 跨领域, 自下而上, 解释简单性 | 超流, V-A, 部分子, 费曼讲义, 诺贝尔奖 |
| 晚期职业 | 1971–1988 | 经验严酷性, 独立思考, 玩乐 | 量子计算愿景; 挑战者号; 货物崇拜科学 |

## 快速开始

```bash
cd FeynmanResearchTaste
pip install -e ".[dev]"        # 安装
feynman-taste fetch-data        # 获取数据
feynman-taste info              # 验证安装

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

### Python API

```python
from feynman_taste.core.pipeline import TastePipeline

pipeline = TastePipeline.default()
result = pipeline.evaluate(
    "用物理图像进行计算的散射截面方法",
    cutoff_year=1965
)
pipeline.print_evaluation(result)
```

## 理解输出

- **[EVIDENCE]** = 有具体历史来源支持的评分
- **[INFERRED]** = 模型推断，无直接证据
- **Overall Score** 从 -1.0（与费曼品味强烈冲突）到 +1.0（高度契合）
- **Caveats** = 局限性和警告

## 项目结构

```
FeynmanResearchTaste/
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
- Schweber, S. S. (1994). *QED and the Men Who Made It*

## 许可证

MIT
