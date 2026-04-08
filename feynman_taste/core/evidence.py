"""
Evidence Management Module
===========================

Manages historical evidence about Feynman's scientific taste.
Each piece of evidence is tagged with:
- Source type (primary: Feynman's own writings; secondary: scholarly analysis)
- Temporal period (when the evidence applies)
- Relevant taste axes
- Confidence level (how directly the evidence supports a taste dimension)

The system strictly separates what Feynman actually wrote/said from
scholarly interpretations and model inferences.
"""

from __future__ import annotations

from enum import Enum
from datetime import date
from pydantic import BaseModel, Field


class SourceType(str, Enum):
    """Classification of evidence sources by proximity to Feynman."""
    PRIMARY = "primary"          # Feynman's own papers, letters, lectures
    SECONDARY = "secondary"      # Scholarly analysis of Feynman's work
    TERTIARY = "tertiary"        # General histories, textbooks
    MODEL_INFERENCE = "inference" # Inferred by the model, not directly supported


class ConfidenceLevel(str, Enum):
    """How directly the evidence supports a taste axis claim."""
    DIRECT = "direct"        # Feynman explicitly stated this preference
    STRONG = "strong"        # Clear from Feynman's actions/choices, well-documented
    MODERATE = "moderate"    # Reasonable inference from multiple sources
    WEAK = "weak"            # Plausible but limited supporting evidence
    SPECULATIVE = "speculative"  # Model inference, no direct evidence


class EvidenceRecord(BaseModel):
    """A single piece of historical evidence about Feynman's scientific taste."""

    id: str = Field(description="Unique identifier for this evidence record")
    content: str = Field(description="The actual evidence text/quote/observation")
    source_text: str = Field(description="Full citation of the source")
    source_type: SourceType
    confidence: ConfidenceLevel

    # Temporal information
    year: int | None = Field(default=None, description="Year the evidence pertains to")
    period: str | None = Field(default=None, description="Named period (e.g., 'early_revolutionary')")

    # Taste axis relevance
    relevant_axes: list[str] = Field(
        default_factory=list,
        description="Names of taste axes this evidence supports"
    )
    axis_valence: dict[str, float] = Field(
        default_factory=dict,
        description="For each axis, +1.0 means supports, -1.0 means contradicts"
    )

    # Metadata
    tags: list[str] = Field(default_factory=list)
    original_language: str = "en"
    is_quote: bool = False  # True if content is a direct quote from Feynman

    def applies_at_year(self, cutoff_year: int) -> bool:
        """Check if this evidence is valid for a given temporal cutoff."""
        if self.year is None:
            return True  # Undated evidence is always available
        return self.year <= cutoff_year

    def is_primary(self) -> bool:
        return self.source_type == SourceType.PRIMARY

    def is_model_generated(self) -> bool:
        return self.source_type == SourceType.MODEL_INFERENCE


class EvidenceStore:
    """
    In-memory store for evidence records with filtering capabilities.

    Supports filtering by:
    - Temporal cutoff (no historical anachronism)
    - Source type (primary vs. secondary)
    - Taste axis relevance
    - Confidence level
    """

    def __init__(self):
        self._records: dict[str, EvidenceRecord] = {}

    def add(self, record: EvidenceRecord) -> None:
        self._records[record.id] = record

    def add_batch(self, records: list[EvidenceRecord]) -> None:
        for r in records:
            self.add(r)

    def get(self, record_id: str) -> EvidenceRecord | None:
        return self._records.get(record_id)

    def all_records(self) -> list[EvidenceRecord]:
        return list(self._records.values())

    def filter(
        self,
        cutoff_year: int | None = None,
        source_types: list[SourceType] | None = None,
        axes: list[str] | None = None,
        min_confidence: ConfidenceLevel | None = None,
        tags: list[str] | None = None,
    ) -> list[EvidenceRecord]:
        """Filter evidence records by multiple criteria."""
        confidence_order = [
            ConfidenceLevel.SPECULATIVE,
            ConfidenceLevel.WEAK,
            ConfidenceLevel.MODERATE,
            ConfidenceLevel.STRONG,
            ConfidenceLevel.DIRECT,
        ]
        results = list(self._records.values())

        if cutoff_year is not None:
            results = [r for r in results if r.applies_at_year(cutoff_year)]

        if source_types is not None:
            results = [r for r in results if r.source_type in source_types]

        if axes is not None:
            results = [r for r in results if any(a in r.relevant_axes for a in axes)]

        if min_confidence is not None:
            min_idx = confidence_order.index(min_confidence)
            results = [
                r for r in results
                if confidence_order.index(r.confidence) >= min_idx
            ]

        if tags is not None:
            results = [r for r in results if any(t in r.tags for t in tags)]

        return results

    def get_axes_evidence(self, axis_name: str, cutoff_year: int | None = None) -> list[EvidenceRecord]:
        """Get all evidence for a specific taste axis, respecting temporal cutoff."""
        return self.filter(cutoff_year=cutoff_year, axes=[axis_name])

    def count(self) -> int:
        return len(self._records)

    def summary(self) -> dict:
        """Return a summary of the evidence store contents."""
        records = self.all_records()
        return {
            "total_records": len(records),
            "by_source_type": {
                st.value: sum(1 for r in records if r.source_type == st)
                for st in SourceType
            },
            "by_confidence": {
                cl.value: sum(1 for r in records if r.confidence == cl)
                for cl in ConfidenceLevel
            },
            "axes_coverage": {
                axis: sum(1 for r in records if axis in r.relevant_axes)
                for axis in set(a for r in records for a in r.relevant_axes)
            },
        }
