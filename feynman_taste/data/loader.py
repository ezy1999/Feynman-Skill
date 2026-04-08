"""
Data Loader Module
===================

Loads evidence records from various formats (JSON, JSONL) into
the EvidenceStore. Handles both the built-in seed data and
user-provided evidence files.
"""

from __future__ import annotations

import json
from pathlib import Path

from feynman_taste.core.evidence import EvidenceRecord, EvidenceStore


def load_evidence_store(data_dir: Path) -> EvidenceStore:
    """
    Load all evidence records from a data directory.

    Looks for:
    - *.json files containing lists of evidence records
    - *.jsonl files with one record per line

    Args:
        data_dir: Directory containing evidence data files

    Returns:
        EvidenceStore populated with all found records
    """
    store = EvidenceStore()

    if not data_dir.exists():
        # Return empty store with seed data if directory doesn't exist
        from feynman_taste.data.seed_evidence import get_seed_evidence
        store.add_batch(get_seed_evidence())
        return store

    loaded = False

    # Load JSON files
    for json_file in sorted(data_dir.glob("*.json")):
        try:
            data = json.loads(json_file.read_text(encoding="utf-8"))
            if isinstance(data, list):
                for item in data:
                    store.add(EvidenceRecord(**item))
                    loaded = True
            elif isinstance(data, dict) and "records" in data:
                for item in data["records"]:
                    store.add(EvidenceRecord(**item))
                    loaded = True
        except Exception as e:
            print(f"Warning: Failed to load {json_file}: {e}")

    # Load JSONL files
    for jsonl_file in sorted(data_dir.glob("*.jsonl")):
        try:
            for line in jsonl_file.read_text(encoding="utf-8").strip().split("\n"):
                if line.strip():
                    store.add(EvidenceRecord(**json.loads(line)))
                    loaded = True
        except Exception as e:
            print(f"Warning: Failed to load {jsonl_file}: {e}")

    # If nothing was loaded, use seed data
    if not loaded:
        from feynman_taste.data.seed_evidence import get_seed_evidence
        store.add_batch(get_seed_evidence())

    return store


def save_evidence_store(store: EvidenceStore, output_path: Path) -> None:
    """Save evidence store to a JSON file."""
    records = [r.model_dump() for r in store.all_records()]
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps({"records": records}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
