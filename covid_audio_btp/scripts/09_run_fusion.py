#!/usr/bin/env python
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from covid_audio_btp.fusion import uniform_fusion, validation_weighted_fusion
from covid_audio_btp.metrics import evaluate_predictions


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run calibrated multimodal fusion.")
    parser.add_argument("--predictions", required=True, type=Path)
    parser.add_argument("--validation-metrics", required=True, type=Path)
    parser.add_argument("--output", type=Path, default=Path("data/outputs/metrics/fusion_predictions.csv"))
    parser.add_argument("--metrics-output", type=Path, default=Path("data/outputs/metrics/fusion_metrics.csv"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    predictions = pd.read_csv(args.predictions)
    validation_metrics = pd.read_csv(args.validation_metrics)
    frames = [
        uniform_fusion(predictions),
        validation_weighted_fusion(predictions, validation_metrics, metric_column="auprc"),
    ]
    fused = pd.concat(frames, ignore_index=True)
    metrics = evaluate_predictions(fused, group_columns=["fusion_method"])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fused.to_csv(args.output, index=False)
    metrics.to_csv(args.metrics_output, index=False)
    print(f"Wrote fusion predictions: {args.output}")
    print(f"Wrote fusion metrics: {args.metrics_output}")


if __name__ == "__main__":
    main()

