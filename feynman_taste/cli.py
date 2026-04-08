"""
CLI Interface
==============

Command-line interface for the Feynman Research Taste system.

Commands:
    evaluate    - Evaluate a candidate theory/question
    rank        - Rank multiple candidates
    compare     - Compare two candidates
    benchmark   - Run the evaluation benchmark
    fetch-data  - Fetch historical data from online sources
    info        - Show system information and evidence stats
"""

from __future__ import annotations

import json
import sys

import click

from feynman_taste.config.settings import DEFAULT_CONFIG, PROCESSED_DATA_DIR


@click.group()
@click.version_option(version="0.1.0")
def main():
    """Feynman Research Taste Modeling System.

    Evaluate scientific theories and questions against Feynman's
    documented research preferences, grounded in historical evidence.
    """
    pass


@main.command()
@click.argument("candidate")
@click.option("--cutoff-year", "-y", default=1955, help="Temporal cutoff year (default: 1955)")
@click.option("--top-k", "-k", default=10, help="Number of evidence records to retrieve")
@click.option("--json-output", "-j", is_flag=True, help="Output as JSON")
def evaluate(candidate: str, cutoff_year: int, top_k: int, json_output: bool):
    """Evaluate a candidate theory/question against Feynman's taste."""
    from feynman_taste.core.pipeline import TastePipeline
    from feynman_taste.utils.formatting import evaluation_to_dict

    pipeline = TastePipeline.default()
    result = pipeline.evaluate(candidate, cutoff_year=cutoff_year, top_k_evidence=top_k)

    if json_output:
        click.echo(json.dumps(evaluation_to_dict(result), indent=2, ensure_ascii=False))
    else:
        pipeline.print_evaluation(result)


@main.command()
@click.argument("candidates", nargs=-1, required=True)
@click.option("--cutoff-year", "-y", default=1955, help="Temporal cutoff year")
@click.option("--json-output", "-j", is_flag=True, help="Output as JSON")
def rank(candidates: tuple[str, ...], cutoff_year: int, json_output: bool):
    """Rank multiple candidate theories/questions."""
    from feynman_taste.core.pipeline import TastePipeline
    from feynman_taste.utils.formatting import evaluation_to_dict, format_ranking

    pipeline = TastePipeline.default()
    results = pipeline.rank_candidates(list(candidates), cutoff_year=cutoff_year)

    if json_output:
        output = [evaluation_to_dict(r) for r in results]
        click.echo(json.dumps(output, indent=2, ensure_ascii=False))
    else:
        click.echo(format_ranking(results))


@main.command()
@click.argument("candidate_a")
@click.argument("candidate_b")
@click.option("--cutoff-year", "-y", default=1955, help="Temporal cutoff year")
def compare(candidate_a: str, candidate_b: str, cutoff_year: int):
    """Compare two candidates head-to-head."""
    from feynman_taste.core.pipeline import TastePipeline

    pipeline = TastePipeline.default()
    result = pipeline.compare(candidate_a, candidate_b, cutoff_year=cutoff_year)
    click.echo(json.dumps(result, indent=2, ensure_ascii=False))


@main.command()
@click.option("--verbose/--quiet", "-v/-q", default=True)
def benchmark(verbose: bool):
    """Run the evaluation benchmark suite."""
    from feynman_taste.core.pipeline import TastePipeline
    from feynman_taste.evaluation.benchmark import run_benchmark

    pipeline = TastePipeline.default()
    results = run_benchmark(pipeline, verbose=verbose)

    click.echo(f"\n{'=' * 50}")
    click.echo(f"BENCHMARK RESULTS")
    click.echo(f"{'=' * 50}")
    click.echo(f"Overall accuracy: {results['accuracy']:.1%} ({results['correct']}/{results['total']})")
    for diff, stats in results["by_difficulty"].items():
        click.echo(f"  {diff:8s}: {stats['accuracy']:.1%} ({stats['correct']}/{stats['total']})")


@main.command(name="fetch-data")
def fetch_data():
    """Fetch historical Feynman data from online sources."""
    from feynman_taste.data.fetcher import FeynmanDataFetcher

    fetcher = FeynmanDataFetcher()
    records = fetcher.fetch_all()
    click.echo(f"\nFetched and processed {len(records)} evidence records.")


@main.command()
def info():
    """Show system information and evidence statistics."""
    from feynman_taste.data.loader import load_evidence_store

    store = load_evidence_store(PROCESSED_DATA_DIR)
    summary = store.summary()

    click.echo("Feynman Research Taste System v0.1.0")
    click.echo(f"Evidence records: {summary['total_records']}")
    click.echo(f"\nBy source type:")
    for st, count in summary["by_source_type"].items():
        click.echo(f"  {st:15s}: {count}")
    click.echo(f"\nBy confidence level:")
    for cl, count in summary["by_confidence"].items():
        click.echo(f"  {cl:15s}: {count}")
    click.echo(f"\nAxes coverage:")
    for axis, count in summary["axes_coverage"].items():
        click.echo(f"  {axis:25s}: {count}")


if __name__ == "__main__":
    main()
