**🌐 Langue :** [中文 (par defaut)](../README.md) | [English](./README_EN.md) | [日本語](./README_JA.md) | [Francais](#) | [Deutsch](./README_DE.md)

---

# Feynman-Skill : Systeme de Modelisation du Gout Scientifique de Feynman

> **Modelisation computationnelle du gout scientifique de Richard Feynman basee sur des preuves historiques.**

## Qu'est-ce que c'est ?

Ce systeme modelise le **gout de recherche** de Feynman - ses preferences distinctives pour certaines approches scientifiques.

**Ce n'est PAS du jeu de role.** Chaque evaluation est fondee sur des preuves historiques.

## Les 10 axes de gout

| # | Axe | Poids | Signification |
|---|-----|-------|---------------|
| 1 | **Intuition physique** | 0.95 | Images et visualisation avant le formalisme |
| 2 | **Pragmatisme computationnel** | 0.90 | Peut-on calculer un nombre ? |
| 3 | **Rigueur empirique** | 0.90 | « Si ca ne correspond pas a l'experience, c'est faux » |
| 4 | **Exploration ludique** | 0.85 | Curiosite, sans pression |
| 5 | **Pensee independante** | 0.85 | Defier l'autorite, premiers principes |
| 6 | **Anti-formalisme** | 0.80 | Mefiance envers l'abstraction pure |
| 7 | **Raisonnement ascendant** | 0.80 | Partir des exemples, puis generaliser |
| 8 | **Representations multiples** | 0.75 | Plusieurs vues = comprehension plus profonde |
| 9 | **Simplicite d'explication** | 0.75 | « Si vous ne pouvez pas l'expliquer a un debutant... » |
| 10 | **Versatilite interdisciplinaire** | 0.70 | Transferer des idees entre domaines |

## Demarrage rapide

```bash
git clone https://github.com/ezy1999/Feynman-Skill.git
cd Feynman-Skill
pip install -e ".[dev]"
feynman-taste fetch-data
python scripts/run_demo_offline.py
```

## Licence

MIT
