#!/usr/bin/env python
from __future__ import annotations

import argparse
import json
from pathlib import Path

from covid_audio_btp.manifest import build_experiment_manifest


DEFAULT_ARTIFACTS = [
    Path("data/interim/coswara_index.csv"),
    Path("data/processed/metadata_clean.csv"),
    Path("data/processed/audio_quality.csv"),
    Path("data/processed/features_mfcc.csv"),
    Path("data/outputs/metrics/ml_baseline_metrics.csv"),
    Path("data/outputs/metrics/calibration_metrics.csv"),
    Path("data/outputs/metrics/fusion_metrics.csv"),
    Path("data/outputs/metrics/quality_weighted_fusion_metrics.csv"),
    Path("data/outputs/metrics/cross_dataset_metrics.csv"),
    Path("reports/tables/paper_metric_table.csv"),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Write reproducibility manifest with config, package versions, and artifact hashes.")
    parser.add_argument("--output", type=Path, default=Path("reports/experiment_manifest.json"))
    parser.add_argument("--artifacts", nargs="*", type=Path, default=None)
    parser.add_argument("--run-name", default="covid_audio_publication_run")
    parser.add_argument("--seed", type=int, default=42)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    artifacts = args.artifacts if args.artifacts is not None else DEFAULT_ARTIFACTS
    manifest = build_experiment_manifest(
        config={"run_name": args.run_name, "seed": args.seed},
        artifact_paths=artifacts,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Wrote experiment manifest: {args.output}")


if __name__ == "__main__":
    main()
