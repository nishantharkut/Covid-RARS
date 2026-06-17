#!/usr/bin/env python
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from covid_audio_btp.temporal_paper_summary import (
    build_temporal_delta_significance,
    build_temporal_feature_attribution_comparison,
    build_temporal_stress_test_summary,
    write_causal_chain_summary,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build paper-facing temporal robustness summary tables.")
    parser.add_argument("--temporal-metrics", type=Path, default=Path("data/outputs/metrics/temporal_holdout_metrics.csv"))
    parser.add_argument("--temporal-bootstrap", type=Path, default=Path("data/outputs/metrics/temporal_holdout_bootstrap_ci.csv"))
    parser.add_argument("--metadata-importance", type=Path, default=Path("reports/tables/temporal_holdout_metadata_feature_importance.csv"))
    parser.add_argument("--temporal-predictions", type=Path, default=Path("data/outputs/metrics/temporal_holdout_predictions.csv"))
    parser.add_argument("--evidence-matrix", type=Path, default=Path("reports/tables/publication_evidence_matrix.csv"))
    parser.add_argument("--external-auprc-lift", type=Path, default=Path("reports/tables/manuscript_external_auprc_lift.csv"))
    parser.add_argument("--stress-summary-output", type=Path, default=Path("reports/tables/temporal_stress_test_summary.csv"))
    parser.add_argument("--feature-comparison-output", type=Path, default=Path("reports/tables/temporal_metadata_feature_attribution_comparison.csv"))
    parser.add_argument("--significance-output", type=Path, default=Path("reports/tables/temporal_stress_test_significance.csv"))
    parser.add_argument("--causal-chain-output", type=Path, default=Path("reports/final/TEMPORAL_ROBUSTNESS_CAUSAL_CHAIN.md"))
    parser.add_argument("--significance-bootstraps", type=int, default=5000)
    return parser.parse_args()


def _read_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path) if path.exists() and path.stat().st_size > 0 else pd.DataFrame()


def _write_csv(frame: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(path, index=False)


def main() -> None:
    args = parse_args()
    metrics = _read_csv(args.temporal_metrics)
    bootstrap = _read_csv(args.temporal_bootstrap)
    importance = _read_csv(args.metadata_importance)
    predictions = _read_csv(args.temporal_predictions)
    evidence = _read_csv(args.evidence_matrix)
    external_lift = _read_csv(args.external_auprc_lift)

    stress_summary = build_temporal_stress_test_summary(metrics, bootstrap, evidence, external_lift)
    feature_comparison = build_temporal_feature_attribution_comparison(importance)
    significance = build_temporal_delta_significance(
        predictions,
        n_bootstraps=args.significance_bootstraps,
    )

    _write_csv(stress_summary, args.stress_summary_output)
    _write_csv(feature_comparison, args.feature_comparison_output)
    _write_csv(significance, args.significance_output)
    write_causal_chain_summary(stress_summary, significance, feature_comparison, args.causal_chain_output)

    print(f"Wrote temporal stress-test summary: {args.stress_summary_output} ({len(stress_summary)} rows)")
    print(f"Wrote temporal feature-attribution comparison: {args.feature_comparison_output} ({len(feature_comparison)} rows)")
    print(f"Wrote temporal stress-test significance: {args.significance_output} ({len(significance)} rows)")
    print(f"Wrote temporal causal-chain summary: {args.causal_chain_output}")


if __name__ == "__main__":
    main()
