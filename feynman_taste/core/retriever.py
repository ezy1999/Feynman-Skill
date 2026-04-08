"""
Evidence Retriever Module
==========================

RAG (Retrieval-Augmented Generation) component that retrieves relevant
historical evidence for a given candidate theory/question.

Uses sentence embeddings and FAISS for fast similarity search over the
evidence corpus. Supports temporal filtering to prevent anachronism.
"""

from __future__ import annotations

import json
import numpy as np
from pathlib import Path
from typing import Any

from feynman_taste.core.evidence import EvidenceRecord, EvidenceStore


class EvidenceRetriever:
    """
    Retrieves relevant evidence records for a given query using
    semantic similarity search.

    For initial prototype, uses a simple TF-IDF / keyword approach.
    Can be upgraded to use sentence-transformers + FAISS for production.
    """

    def __init__(self, evidence_store: EvidenceStore):
        self.evidence_store = evidence_store
        self._embeddings: dict[str, np.ndarray] | None = None
        self._use_embeddings = False

    def _keyword_score(self, query: str, record: EvidenceRecord) -> float:
        """Simple keyword overlap scoring for prototype."""
        query_tokens = set(query.lower().split())
        content_tokens = set(record.content.lower().split())
        # Also include axis keywords
        axis_tokens = set(
            kw.lower() for axis_name in record.relevant_axes
            for kw in self._get_axis_keywords(axis_name)
        )
        all_record_tokens = content_tokens | axis_tokens

        if not query_tokens:
            return 0.0
        overlap = query_tokens & all_record_tokens
        return len(overlap) / len(query_tokens)

    def _get_axis_keywords(self, axis_name: str) -> list[str]:
        """Get keywords for an axis from the settings."""
        from feynman_taste.config.settings import FEYNMAN_TASTE_AXES
        for axis in FEYNMAN_TASTE_AXES:
            if axis.name == axis_name:
                return axis.keywords
        return []

    def retrieve(
        self,
        query: str,
        top_k: int = 10,
        cutoff_year: int | None = None,
        min_confidence: str | None = None,
        source_types: list[str] | None = None,
    ) -> list[tuple[EvidenceRecord, float]]:
        """
        Retrieve the most relevant evidence records for a query.

        Args:
            query: The candidate theory/question description
            top_k: Maximum number of records to return
            cutoff_year: Temporal cutoff for evidence
            min_confidence: Minimum confidence level filter
            source_types: Allowed source types filter

        Returns:
            List of (record, relevance_score) tuples, sorted by relevance
        """
        from feynman_taste.core.evidence import ConfidenceLevel, SourceType

        # Get all eligible records
        filter_kwargs: dict[str, Any] = {}
        if cutoff_year is not None:
            filter_kwargs["cutoff_year"] = cutoff_year
        if min_confidence is not None:
            filter_kwargs["min_confidence"] = ConfidenceLevel(min_confidence)
        if source_types is not None:
            filter_kwargs["source_types"] = [SourceType(st) for st in source_types]

        candidates = self.evidence_store.filter(**filter_kwargs)

        # Score each record
        scored = [(record, self._keyword_score(query, record)) for record in candidates]

        # Sort by relevance, take top_k
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:top_k]

    def retrieve_for_axis(
        self,
        query: str,
        axis_name: str,
        top_k: int = 5,
        cutoff_year: int | None = None,
    ) -> list[tuple[EvidenceRecord, float]]:
        """Retrieve evidence specifically relevant to a given taste axis."""
        axis_records = self.evidence_store.get_axes_evidence(axis_name, cutoff_year)

        scored = [(record, self._keyword_score(query, record)) for record in axis_records]
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:top_k]

    def save_embeddings(self, path: Path) -> None:
        """Save computed embeddings to disk."""
        if self._embeddings is not None:
            data = {k: v.tolist() for k, v in self._embeddings.items()}
            path.write_text(json.dumps(data))

    def load_embeddings(self, path: Path) -> None:
        """Load pre-computed embeddings from disk."""
        if path.exists():
            data = json.loads(path.read_text())
            self._embeddings = {k: np.array(v) for k, v in data.items()}
            self._use_embeddings = True
