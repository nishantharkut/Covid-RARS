#!/usr/bin/env python
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from covid_audio_btp.reporting import build_paper_metric_table, read_existing_csvs


DEFAULT_METRIC_PATHS = [
    Path("data/outputs/metrics/ml_baseline_metrics.csv"),
    Path("data/outputs/metrics/cnn_metrics.csv"),
    Path("data/outputs/metrics/calibration_metrics.csv"),
    Path("data/outputs/metrics/fusion_metrics.csv"),
    Path("data/outputs/metrics/quality_weighted_fusion_metrics.csv"),
    Path("data/outputs/metrics/metadata_baseline_metrics.csv"),
    Path("data/outputs/metrics/cross_dataset_metrics.csv"),
    Path("data/outputs/metrics/external_model_grid_metrics.csv"),
    Path("data/outputs/metrics/coughvid_internal_metrics.csv"),
]

DEFAULT_CI_PATHS = [
    Path("data/outputs/metrics/quality_weighted_fusion_bootstrap_ci.csv"),
    Path("data/outputs/metrics/cross_dataset_bootstrap_ci.csv"),
    Path("data/outputs/metrics/external_model_grid_bootstrap_ci.csv"),
    Path("data/outputs/metrics/coughvid_internal_bootstrap_ci.csv"),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build paper-ready metric tables from experiment CSVs.")
    parser.add_argument("--metrics", nargs="*", type=Path, default=None)
    parser.add_argument("--ci", nargs="*", type=Path, default=None)
    parser.add_argument("--output", type=Path, default=Path("reports/tables/paper_metric_table.csv"))
    parser.add_argument("--raw-output", type=Path, default=Path("reports/tables/paper_metric_table_raw.csv"))
    return parser.parse_args()


def _group_columns(metrics: pd.DataFrame) -> list[str]:
    candidates = ["table_source", "model_name", "model", "modality", "fusion_method", "dataset", "split"]
    return [col for col in candidates if col in metrics.columns]


def main() -> None:
    args = parse_args()
    metric_paths = args.metrics if args.metrics is not None else DEFAULT_METRIC_PATHS
    ci_paths = args.ci if args.ci is not None else DEFAULT_CI_PATHS
    metrics = read_existing_csvs(metric_paths)
    ci_table = read_existing_csvs(ci_paths)
    if metrics.empty:
        checked = ", ".join(str(path) for path in metric_paths)
        raise FileNotFoundError(f"No metric CSVs found. Checked: {checked}")
    group_columns = _group_columns(metrics)
    paper = build_paper_metric_table(metrics, ci_table=ci_table, group_columns=group_columns)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.raw_output.parent.mkdir(parents=True, exist_ok=True)
    metrics.to_csv(args.raw_output, index=False)
    paper.to_csv(args.output, index=False)
    print(f"Wrote paper metric table: {args.output} ({len(paper)} rows)")
    print(f"Wrote raw combined metric table: {args.raw_output} ({len(metrics)} rows)")


if __name__ == "__main__":
    main()
