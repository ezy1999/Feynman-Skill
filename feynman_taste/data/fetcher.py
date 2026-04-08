"""
Data Fetcher for Feynman historical data from publicly available sources.
"""

from __future__ import annotations
import json
import time
from pathlib import Path
import requests
from bs4 import BeautifulSoup
from feynman_taste.config.settings import RAW_DATA_DIR, PROCESSED_DATA_DIR
from feynman_taste.core.evidence import EvidenceRecord, SourceType, ConfidenceLevel


class FeynmanDataFetcher:
    HEADERS = {"User-Agent": "FeynmanResearchTaste/0.1 (academic research project)"}
    REQUEST_DELAY = 1.0

    def __init__(self, raw_dir: Path | None = None, processed_dir: Path | None = None):
        self.raw_dir = raw_dir or RAW_DATA_DIR
        self.processed_dir = processed_dir or PROCESSED_DATA_DIR
        self.raw_dir.mkdir(parents=True, exist_ok=True)
        self.processed_dir.mkdir(parents=True, exist_ok=True)

    def _get(self, url: str) -> requests.Response | None:
        try:
            time.sleep(self.REQUEST_DELAY)
            resp = requests.get(url, headers=self.HEADERS, timeout=30)
            resp.raise_for_status()
            return resp
        except Exception as e:
            print(f"Warning: Failed to fetch {url}: {e}")
            return None

    def fetch_feynman_wikipedia(self) -> list[dict]:
        print("Fetching Feynman data from Wikipedia...")
        pages = [
            "Richard_Feynman", "Feynman_diagram", "Path_integral_formulation",
            "Quantum_electrodynamics", "Parton_(particle_physics)",
            "Feynman_Lectures_on_Physics", "Cargo_cult_science",
            "Rogers_Commission_Report",
        ]
        results = []
        for page in pages:
            url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{page}"
            resp = self._get(url)
            if resp:
                data = resp.json()
                results.append({
                    "title": data.get("title", page),
                    "extract": data.get("extract", ""),
                    "description": data.get("description", ""),
                })
        output_path = self.raw_dir / "wikipedia_feynman.json"
        output_path.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"  Saved {len(results)} Wikipedia entries")
        return results

    def fetch_feynman_publications(self) -> list[dict]:
        print("Fetching Feynman publication metadata...")
        papers = [
            {"title": "Space-Time Approach to Non-Relativistic Quantum Mechanics",
             "year": 1948, "journal": "Reviews of Modern Physics", "topic": "path_integral",
             "taste_relevance": "Physical intuition: reformulated QM as sum over paths, making particle trajectories visualizable"},
            {"title": "Space-Time Approach to Quantum Electrodynamics",
             "year": 1949, "journal": "Physical Review", "topic": "qed_spacetime",
             "taste_relevance": "Computational pragmatism: provided calculational framework for QED that was physically transparent"},
            {"title": "Mathematical Formulation of the Quantum Theory of Electromagnetic Interaction",
             "year": 1950, "journal": "Physical Review", "topic": "qed_formulation",
             "taste_relevance": "Multiple representations: showed equivalence of path integral and operator approaches"},
            {"title": "The Theory of Positrons",
             "year": 1949, "journal": "Physical Review", "topic": "positrons",
             "taste_relevance": "Physical intuition: reinterpreted positrons as electrons moving backward in time"},
            {"title": "Application of Quantum Mechanics to Liquid Helium",
             "year": 1953, "journal": "Physical Review", "topic": "superfluidity",
             "taste_relevance": "Cross-domain versatility: applied quantum field theory methods to condensed matter"},
            {"title": "Theory of the Fermi Interaction",
             "year": 1958, "journal": "Physical Review", "topic": "weak_interaction",
             "taste_relevance": "Bottom-up reasoning: V-A theory emerged from analyzing experimental data on weak decays"},
            {"title": "Very High-Energy Collisions of Hadrons",
             "year": 1969, "journal": "Physical Review Letters", "topic": "parton_model",
             "taste_relevance": "Bottom-up reasoning: proposed partons from data analysis without committing to specific theory"},
            {"title": "Simulating Physics with Computers",
             "year": 1982, "journal": "Int. J. Theoretical Physics", "topic": "quantum_computing",
             "taste_relevance": "Cross-domain versatility: founded quantum computing by connecting physics simulation to computation"},
            {"title": "There's Plenty of Room at the Bottom",
             "year": 1959, "journal": "APS meeting talk", "topic": "nanotechnology",
             "taste_relevance": "Playful exploration: visionary talk on manipulating individual atoms, driven by curiosity"},
        ]
        output_path = self.raw_dir / "feynman_papers.json"
        output_path.write_text(json.dumps(papers, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"  Saved {len(papers)} paper records")
        return papers

    def process_papers_to_evidence(self, papers: list[dict]) -> list[EvidenceRecord]:
        records = []
        for paper in papers:
            axes = self._infer_axes(paper)
            records.append(EvidenceRecord(
                id=f"paper_{paper['topic']}_{paper['year']}",
                content=(
                    f"Feynman published '{paper['title']}' in {paper['journal']} ({paper['year']}). "
                    f"Research taste relevance: {paper['taste_relevance']}"
                ),
                source_text=f"Feynman, '{paper['title']}', {paper['journal']} ({paper['year']})",
                source_type=SourceType.PRIMARY,
                confidence=ConfidenceLevel.STRONG,
                year=paper["year"],
                relevant_axes=axes,
                tags=[paper["topic"], "publication"],
            ))
        return records

    def _infer_axes(self, paper: dict) -> list[str]:
        taste = paper.get("taste_relevance", "").lower()
        axes = []
        kw_map = {
            "physical_intuition": ["intuition", "visualiz", "picture", "physical"],
            "computational_pragmatism": ["calculat", "comput", "pragmati", "number"],
            "anti_formalism": ["anti-formal", "not abstract"],
            "empirical_ruthlessness": ["experiment", "data", "empirical"],
            "playful_exploration": ["play", "curiosity", "fun", "wonder"],
            "independent_thinking": ["independent", "original", "challenge"],
            "multiple_representations": ["multiple", "representation", "equivalent", "alternative"],
            "bottom_up_reasoning": ["bottom-up", "data analysis", "specific"],
            "cross_domain_versatility": ["cross-domain", "versatil", "connecting", "different field"],
            "simplicity_of_explanation": ["explain", "simple", "clear", "teach"],
        }
        for axis, keywords in kw_map.items():
            if any(kw in taste for kw in keywords):
                axes.append(axis)
        return axes or ["physical_intuition"]

    def fetch_all(self) -> list[EvidenceRecord]:
        all_records = []
        self.fetch_feynman_wikipedia()
        papers = self.fetch_feynman_publications()
        paper_records = self.process_papers_to_evidence(papers)
        all_records.extend(paper_records)
        from feynman_taste.data.seed_evidence import get_seed_evidence
        all_records.extend(get_seed_evidence())
        from feynman_taste.core.evidence import EvidenceStore
        from feynman_taste.data.loader import save_evidence_store
        store = EvidenceStore()
        store.add_batch(all_records)
        save_evidence_store(store, self.processed_dir / "evidence.json")
        print(f"\nTotal evidence records: {store.count()}")
        return all_records
