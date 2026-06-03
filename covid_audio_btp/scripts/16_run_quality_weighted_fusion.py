#!/usr/bin/env python
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from covid_audio_btp.fusion import quality_weighted_fusion
from covid_audio_btp.metrics import evaluate_predictions


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run quality-weighted calibrated multimodal fusion.")
    parser.add_argument("--predictions", required=True, type=Path)
    parser.add_argument("--quality", required=True, type=Path)
    parser.add_argument("--validation-metrics", required=True, type=Path)
    parser.add_argument("--output", type=Path, default=Path("data/outputs/metrics/quality_weighted_fusion_predictions.csv"))
    parser.add_argument("--metrics-output", type=Path, default=Path("data/outputs/metrics/quality_weighted_fusion_metrics.csv"))
    parser.add_argument("--metric-column", default="auprc")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    predictions = pd.read_csv(args.predictions)
    quality = pd.read_csv(args.quality)
    validation_metrics = pd.read_csv(args.validation_metrics)
    fused = quality_weighted_fusion(
        predictions,
        quality=quality,
        validation_metrics=validation_metrics,
        metric_column=args.metric_column,
    )
    metrics = evaluate_predictions(fused, group_columns=["fusion_method"])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fused.to_csv(args.output, index=False)
    metrics.to_csv(args.metrics_output, index=False)
    print(f"Wrote quality-weighted fusion predictions: {args.output}")
    print(f"Wrote quality-weighted fusion metrics: {args.metrics_output}")


if __name__ == "__main__":
    main()
