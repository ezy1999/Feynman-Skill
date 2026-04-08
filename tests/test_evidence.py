"""Tests for Feynman evidence management module."""

import pytest
from feynman_taste.core.evidence import (
    EvidenceRecord, EvidenceStore, SourceType, ConfidenceLevel,
)


@pytest.fixture
def sample_records():
    return [
        EvidenceRecord(
            id="test_001", content="Feynman valued physical intuition",
            source_text="Gleick, 'Genius' (1992)", source_type=SourceType.SECONDARY,
            confidence=ConfidenceLevel.STRONG, year=1949, period="qed_revolution",
            relevant_axes=["physical_intuition"], axis_valence={"physical_intuition": 1.0},
        ),
        EvidenceRecord(
            id="test_002", content="Feynman proposed path integrals",
            source_text="Feynman, Rev. Mod. Phys. (1948)", source_type=SourceType.PRIMARY,
            confidence=ConfidenceLevel.DIRECT, year=1948, period="qed_revolution",
            relevant_axes=["computational_pragmatism"], axis_valence={"computational_pragmatism": 1.0},
        ),
        EvidenceRecord(
            id="test_003", content="Feynman: you must not fool yourself",
            source_text="Feynman, 'Cargo Cult Science' (1974)", source_type=SourceType.PRIMARY,
            confidence=ConfidenceLevel.DIRECT, year=1974, period="later_career",
            relevant_axes=["empirical_ruthlessness"], axis_valence={"empirical_ruthlessness": 1.0},
            is_quote=True,
        ),
    ]


@pytest.fixture
def store(sample_records):
    s = EvidenceStore()
    s.add_batch(sample_records)
    return s


class TestEvidenceRecord:
    def test_applies_at_year(self, sample_records):
        assert sample_records[0].applies_at_year(1950)
        assert not sample_records[0].applies_at_year(1948)

    def test_is_primary(self, sample_records):
        assert not sample_records[0].is_primary()
        assert sample_records[1].is_primary()


class TestEvidenceStore:
    def test_count(self, store):
        assert store.count() == 3

    def test_filter_by_year(self, store):
        assert len(store.filter(cutoff_year=1949)) == 2

    def test_filter_by_source(self, store):
        assert len(store.filter(source_types=[SourceType.PRIMARY])) == 2

    def test_filter_by_axes(self, store):
        assert len(store.filter(axes=["empirical_ruthlessness"])) == 1

    def test_summary(self, store):
        s = store.summary()
        assert s["total_records"] == 3
