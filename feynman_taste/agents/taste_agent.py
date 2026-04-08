"""
Taste Agent Module
===================

Conversational agent that wraps the taste pipeline for interactive use.
Handles user queries about Feynman's likely evaluation of scientific
theories and questions.

This agent:
1. Parses user input to extract candidate theories/questions
2. Determines appropriate temporal cutoff
3. Runs the taste evaluation pipeline
4. Formats and presents results with clear evidence/inference separation
"""

from __future__ import annotations

import re
from typing import Any

from feynman_taste.config.settings import DEFAULT_CONFIG, ModelConfig, FEYNMAN_PERIODS
from feynman_taste.core.pipeline import TastePipeline


class TasteAgent:
    """
    Interactive agent for Feynman research taste queries.

    Provides a conversational interface for evaluating scientific
    theories/questions against Feynman's documented preferences.
    """

    def __init__(self, config: ModelConfig | None = None):
        self.config = config or DEFAULT_CONFIG
        self._pipeline: TastePipeline | None = None

    @property
    def pipeline(self) -> TastePipeline:
        """Lazy-initialize the pipeline."""
        if self._pipeline is None:
            self._pipeline = TastePipeline.default(self.config)
        return self._pipeline

    def process_query(self, user_input: str) -> str:
        """
        Process a user query and return a formatted response.

        Supports query types:
        - "evaluate: <theory description>" - evaluate a single theory
        - "rank: <theory1> | <theory2> | ..." - rank multiple theories
        - "compare: <theory1> vs <theory2>" - compare two theories
        - Free-form questions about Feynman's taste
        """
        user_input = user_input.strip()

        # Detect query type
        if user_input.lower().startswith("evaluate:"):
            return self._handle_evaluate(user_input[9:].strip())
        elif user_input.lower().startswith("rank:"):
            return self._handle_rank(user_input[5:].strip())
        elif user_input.lower().startswith("compare:"):
            return self._handle_compare(user_input[8:].strip())
        else:
            # Default: treat as evaluation query
            return self._handle_evaluate(user_input)

    def _extract_cutoff_year(self, text: str) -> tuple[str, int]:
        """Extract temporal cutoff from text if specified."""
        # Look for patterns like "in 1905", "by 1920", "around 1935"
        year_match = re.search(r'\b(?:in|by|around|circa|before|at)\s+(\d{4})\b', text, re.IGNORECASE)
        if year_match:
            year = int(year_match.group(1))
            # Remove the year specification from the text
            clean_text = text[:year_match.start()] + text[year_match.end():]
            return clean_text.strip(), year
        return text, 1955  # Default: full career

    def _handle_evaluate(self, text: str) -> str:
        """Handle a single evaluation query."""
        clean_text, cutoff_year = self._extract_cutoff_year(text)

        evaluation = self.pipeline.evaluate(
            candidate=clean_text,
            cutoff_year=cutoff_year,
        )

        return self.pipeline.format_evaluation(evaluation)

    def _handle_rank(self, text: str) -> str:
        """Handle a ranking query. Candidates separated by '|'."""
        parts = [p.strip() for p in text.split("|") if p.strip()]
        if len(parts) < 2:
            return "Please provide at least 2 candidates separated by '|'."

        # Extract cutoff year from last part or use default
        _, cutoff_year = self._extract_cutoff_year(text)

        from feynman_taste.utils.formatting import format_ranking
        evaluations = self.pipeline.rank_candidates(parts, cutoff_year=cutoff_year)
        return format_ranking(evaluations)

    def _handle_compare(self, text: str) -> str:
        """Handle a comparison query. Candidates separated by 'vs'."""
        parts = re.split(r'\bvs\.?\b', text, flags=re.IGNORECASE)
        if len(parts) != 2:
            return "Please provide exactly 2 candidates separated by 'vs'."

        a, b = parts[0].strip(), parts[1].strip()
        _, cutoff_year = self._extract_cutoff_year(text)

        import json
        result = self.pipeline.compare(a, b, cutoff_year=cutoff_year)
        return json.dumps(result, indent=2, ensure_ascii=False)

    def get_system_info(self) -> str:
        """Return information about the system's capabilities."""
        periods = "\n".join(
            f"  - {p.name} ({p.start_year}-{p.end_year}): {p.description[:80]}..."
            for p in FEYNMAN_PERIODS
        )

        return (
            "Feynman Research Taste Modeling System\n"
            "=" * 40 + "\n\n"
            "This system evaluates scientific theories and questions against\n"
            "Feynman's documented research preferences.\n\n"
            "Query formats:\n"
            "  evaluate: <description>    - Evaluate a theory/question\n"
            "  rank: <A> | <B> | <C>      - Rank multiple candidates\n"
            "  compare: <A> vs <B>        - Compare two candidates\n\n"
            "Temporal periods:\n"
            f"{periods}\n\n"
            "Add 'in <year>' to set a temporal cutoff.\n"
            "Example: 'evaluate: quantum field theory in 1935'\n"
        )
