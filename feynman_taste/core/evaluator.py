"""
LLM-based Evaluator Module
============================

Uses a large language model to evaluate candidate scientific questions/theories
against Feynman's taste axes, grounded in retrieved historical evidence.

The evaluator:
1. Receives a candidate description and retrieved evidence
2. Prompts the LLM to score each taste axis
3. Requires the LLM to cite evidence for each score
4. Marks scores as evidence-based or model-inferred
5. Enforces temporal cutoff in the prompt
"""

from __future__ import annotations

import json
import os
from typing import Any

from feynman_taste.config.settings import FEYNMAN_TASTE_AXES, ModelConfig, DEFAULT_CONFIG
from feynman_taste.core.evidence import EvidenceRecord, SourceType
from feynman_taste.core.taste_model import AxisScore, TasteEvaluation, TasteScorer


# System prompt template for the evaluator LLM
EVALUATOR_SYSTEM_PROMPT = """You are an expert historian of science specializing in Richard Feynman's
scientific methodology, philosophy, and research taste. Your task is to evaluate
how a candidate scientific question or theory aligns with Feynman's documented
research preferences and scientific taste.

CRITICAL RULES:
1. You MUST ground your evaluation in historical evidence provided to you.
2. You MUST clearly distinguish between what is supported by evidence and what
   you are inferring.
3. You MUST respect the temporal cutoff: Feynman at year {cutoff_year} would NOT
   know about developments after that year.
4. You MUST NOT engage in role-playing. You are analyzing Feynman's documented
   preferences, not pretending to be Feynman.
5. For each taste axis, you MUST cite specific evidence or explicitly mark your
   assessment as inference.

The taste axes to evaluate are:
{axes_descriptions}

You will receive:
- A candidate scientific question/theory to evaluate
- Historical evidence about Feynman's preferences
- A temporal cutoff year

Respond in JSON format with the following structure:
{{
    "axis_scores": [
        {{
            "axis_name": "name",
            "score": float between -1.0 and 1.0,
            "confidence": float between 0.0 and 1.0,
            "evidence_ids": ["id1", "id2"],
            "explanation": "Why this score, citing evidence",
            "is_evidence_based": true/false
        }}
    ],
    "summary": "Brief overall assessment",
    "evidence_summary": "What historical evidence supports this evaluation",
    "inference_summary": "What was inferred beyond the evidence",
    "caveats": ["List of limitations or warnings"]
}}
"""


def format_evidence_for_prompt(records: list[tuple[EvidenceRecord, float]]) -> str:
    """Format retrieved evidence records for inclusion in the LLM prompt."""
    if not records:
        return "No historical evidence was retrieved for this query."

    lines = ["=== Historical Evidence ===\n"]
    for record, relevance in records:
        source_label = {
            SourceType.PRIMARY: "[PRIMARY - Feynman's own words]",
            SourceType.SECONDARY: "[SECONDARY - Scholarly analysis]",
            SourceType.TERTIARY: "[TERTIARY - General reference]",
            SourceType.MODEL_INFERENCE: "[MODEL INFERENCE]",
        }.get(record.source_type, "[UNKNOWN]")

        lines.append(f"Evidence ID: {record.id}")
        lines.append(f"Source: {record.source_text} {source_label}")
        if record.year:
            lines.append(f"Year: {record.year}")
        lines.append(f"Relevant axes: {', '.join(record.relevant_axes)}")
        lines.append(f"Content: {record.content}")
        lines.append(f"Confidence: {record.confidence.value}")
        lines.append("")

    return "\n".join(lines)


def format_axes_descriptions() -> str:
    """Format taste axes for inclusion in the system prompt."""
    lines = []
    for axis in FEYNMAN_TASTE_AXES:
        lines.append(f"- {axis.name}: {axis.description}")
        lines.append(f"  Default weight: {axis.weight}")
        lines.append(f"  Key evidence: {'; '.join(axis.evidence_sources[:2])}")
        lines.append("")
    return "\n".join(lines)


class TasteEvaluator:
    """
    LLM-based evaluator that scores candidates against Feynman's taste axes.

    Supports both Anthropic (Claude) and OpenAI APIs.
    """

    def __init__(self, config: ModelConfig | None = None):
        self.config = config or DEFAULT_CONFIG
        self._client = None

    def _get_client(self):
        """Lazy-initialize the LLM client."""
        if self._client is not None:
            return self._client

        if self.config.llm_provider == "anthropic":
            try:
                import anthropic
                self._client = anthropic.Anthropic()
            except ImportError:
                raise ImportError("pip install anthropic")
        elif self.config.llm_provider == "openai":
            try:
                import openai
                self._client = openai.OpenAI()
            except ImportError:
                raise ImportError("pip install openai")
        else:
            raise ValueError(f"Unsupported provider: {self.config.llm_provider}")

        return self._client

    def _call_llm(self, system: str, user: str) -> str:
        """Call the LLM and return the response text."""
        client = self._get_client()

        if self.config.llm_provider == "anthropic":
            response = client.messages.create(
                model=self.config.llm_model,
                max_tokens=self.config.max_tokens,
                temperature=self.config.temperature,
                system=system,
                messages=[{"role": "user", "content": user}],
            )
            return response.content[0].text
        elif self.config.llm_provider == "openai":
            response = client.chat.completions.create(
                model=self.config.llm_model,
                max_tokens=self.config.max_tokens,
                temperature=self.config.temperature,
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
            )
            return response.choices[0].message.content
        else:
            raise ValueError(f"Unsupported provider: {self.config.llm_provider}")

    def evaluate(
        self,
        candidate: str,
        evidence: list[tuple[EvidenceRecord, float]],
        cutoff_year: int = 1955,
        scorer: TasteScorer | None = None,
    ) -> TasteEvaluation:
        """
        Evaluate a candidate theory/question against Feynman's taste.

        Args:
            candidate: Description of the candidate theory/question
            evidence: Retrieved evidence records with relevance scores
            cutoff_year: Temporal cutoff year
            scorer: Optional TasteScorer for aggregation

        Returns:
            TasteEvaluation with per-axis scores and explanations
        """
        # Build the system prompt
        system = EVALUATOR_SYSTEM_PROMPT.format(
            cutoff_year=cutoff_year,
            axes_descriptions=format_axes_descriptions(),
        )

        # Build the user prompt
        evidence_text = format_evidence_for_prompt(evidence)
        user_prompt = (
            f"## Candidate Theory/Question\n\n{candidate}\n\n"
            f"## Temporal Cutoff\n\nYear: {cutoff_year}. Feynman at this point "
            f"would NOT know about any developments after {cutoff_year}.\n\n"
            f"## Retrieved Historical Evidence\n\n{evidence_text}\n\n"
            f"Please evaluate the candidate against each taste axis. "
            f"Respond in the specified JSON format."
        )

        # Call the LLM
        raw_response = self._call_llm(system, user_prompt)

        # Parse the response
        return self._parse_response(raw_response, candidate, cutoff_year, scorer)

    def _parse_response(
        self,
        raw: str,
        candidate: str,
        cutoff_year: int,
        scorer: TasteScorer | None,
    ) -> TasteEvaluation:
        """Parse the LLM JSON response into a TasteEvaluation."""
        # Extract JSON from response (handle markdown code blocks)
        json_str = raw.strip()
        if json_str.startswith("```"):
            # Remove markdown code block
            lines = json_str.split("\n")
            json_lines = []
            in_block = False
            for line in lines:
                if line.strip().startswith("```") and not in_block:
                    in_block = True
                    continue
                elif line.strip().startswith("```") and in_block:
                    break
                elif in_block:
                    json_lines.append(line)
            json_str = "\n".join(json_lines)

        try:
            data = json.loads(json_str)
        except json.JSONDecodeError:
            # Fallback: return a minimal evaluation
            return TasteEvaluation(
                candidate_description=candidate,
                cutoff_year=cutoff_year,
                active_period=self._get_period_name(cutoff_year),
                overall_score=0.0,
                overall_confidence=0.0,
                summary="Failed to parse LLM response.",
                caveats=["LLM response was not valid JSON. Raw response saved for debugging."],
            )

        # Build axis scores
        axis_scores = []
        for item in data.get("axis_scores", []):
            axis_scores.append(AxisScore(
                axis_name=item["axis_name"],
                score=max(-1.0, min(1.0, float(item.get("score", 0)))),
                confidence=max(0.0, min(1.0, float(item.get("confidence", 0.5)))),
                evidence_ids=item.get("evidence_ids", []),
                explanation=item.get("explanation", ""),
                is_evidence_based=item.get("is_evidence_based", True),
            ))

        # Aggregate scores
        if scorer:
            overall_score, overall_confidence = scorer.aggregate_scores(axis_scores, cutoff_year)
        else:
            # Simple average
            if axis_scores:
                overall_score = sum(s.score for s in axis_scores) / len(axis_scores)
                overall_confidence = sum(s.confidence for s in axis_scores) / len(axis_scores)
            else:
                overall_score, overall_confidence = 0.0, 0.0

        return TasteEvaluation(
            candidate_description=candidate,
            cutoff_year=cutoff_year,
            active_period=self._get_period_name(cutoff_year),
            axis_scores=axis_scores,
            overall_score=overall_score,
            overall_confidence=overall_confidence,
            summary=data.get("summary", ""),
            evidence_summary=data.get("evidence_summary", ""),
            inference_summary=data.get("inference_summary", ""),
            caveats=data.get("caveats", []),
        )

    def _get_period_name(self, year: int) -> str:
        """Get the period name for a given year."""
        from feynman_taste.config.settings import FEYNMAN_PERIODS
        for period in FEYNMAN_PERIODS:
            if period.start_year <= year <= period.end_year:
                return period.name
        return "unknown"
