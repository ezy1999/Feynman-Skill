"""Download real Feynman data from public web sources."""

import json, time, requests
from pathlib import Path

RAW_DIR = Path(__file__).parent.parent / "feynman_taste" / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)
HEADERS = {"User-Agent": "FeynmanResearchTaste/0.1 (academic research)"}

def fetch(url, delay=1.0):
    time.sleep(delay)
    try:
        r = requests.get(url, headers=HEADERS, timeout=30)
        r.raise_for_status()
        return r
    except Exception as e:
        print(f"  FAIL: {url}: {e}")
        return None

def main():
    print("=" * 60)
    print("DOWNLOADING REAL FEYNMAN DATA")
    print("=" * 60)

    # 1. Wikipedia detailed articles
    print("\n=== Wikipedia Articles ===")
    pages = {
        "Richard_Feynman": "feynman_biography",
        "Feynman_diagram": "feynman_diagram",
        "Path_integral_formulation": "path_integral",
        "Quantum_electrodynamics": "qed",
        "Feynman_Lectures_on_Physics": "feynman_lectures",
        "Cargo_cult_science": "cargo_cult_science",
        "Parton_(particle_physics)": "parton_model",
        "Rogers_Commission_Report": "challenger_commission",
        "Quantum_computing": "quantum_computing",
        "Nanotechnology": "nanotechnology",
        "The_Character_of_Physical_Law": "character_physical_law",
        "Surely_You%27re_Joking,_Mr._Feynman!": "surely_joking",
    }
    wiki_data = {}
    for page, key in pages.items():
        # Summary
        r = fetch(f"https://en.wikipedia.org/api/rest_v1/page/summary/{page}")
        if r:
            d = r.json()
            wiki_data[key] = {"title": d.get("title",""), "extract": d.get("extract",""), "url": d.get("content_urls",{}).get("desktop",{}).get("page","")}
            print(f"  OK: {key} ({len(d.get('extract',''))} chars)")

    # Full extracts for key pages
    for page in ["Richard_Feynman", "Cargo_cult_science"]:
        key = pages[page]
        r = fetch(f"https://en.wikipedia.org/w/api.php?action=query&titles={page}&prop=extracts&exintro=false&explaintext=true&format=json")
        if r:
            d = r.json()
            pd = list(d.get("query",{}).get("pages",{}).values())
            if pd:
                text = pd[0].get("extract","")
                wiki_data[key]["full_extract"] = text[:30000]
                print(f"  FULL: {key} ({len(text)} chars)")

    (RAW_DIR / "wikipedia_detailed.json").write_text(json.dumps(wiki_data, indent=2, ensure_ascii=False), encoding="utf-8")

    # 2. Wikiquote Feynman
    print("\n=== Wikiquote Feynman ===")
    r = fetch("https://en.wikiquote.org/w/api.php?action=query&titles=Richard_Feynman&prop=extracts&explaintext=true&format=json")
    if r:
        d = r.json()
        pd = list(d.get("query",{}).get("pages",{}).values())
        if pd:
            text = pd[0].get("extract","")
            (RAW_DIR / "wikiquote_feynman.json").write_text(json.dumps({"quotes_text": text[:50000]}, indent=2, ensure_ascii=False), encoding="utf-8")
            print(f"  OK: {len(text)} chars")

    # 3. Semantic Scholar
    print("\n=== Semantic Scholar (Feynman scholarship) ===")
    r = fetch("https://api.semanticscholar.org/graph/v1/paper/search?query=Feynman scientific methodology philosophy physics&limit=10&fields=title,year,authors,abstract,citationCount", delay=3)
    if r:
        papers = r.json().get("data", [])
        (RAW_DIR / "semantic_scholar.json").write_text(json.dumps(papers, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"  OK: {len(papers)} papers")

    # Summary
    print("\n=== Download Summary ===")
    total = 0
    for f in sorted(RAW_DIR.glob("*.json")):
        s = f.stat().st_size
        total += s
        print(f"  {f.name}: {s:,} bytes")
    print(f"  TOTAL: {total:,} bytes ({total/1024:.1f} KB)")

if __name__ == "__main__":
    main()
