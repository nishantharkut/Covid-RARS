#!/usr/bin/env python
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd
import torch

from covid_audio_btp.train_cnn import train_cnn_for_modality


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Train compact CNN on saved log-mel spectrograms.")
    parser.add_argument("--spectrogram-index", required=True, type=Path)
    parser.add_argument("--modality", default="cough")
    parser.add_argument("--models-dir", type=Path, default=Path("data/outputs/models"))
    parser.add_argument("--metrics-output", type=Path, default=Path("data/outputs/metrics/cnn_metrics.csv"))
    parser.add_argument("--validation-output", type=Path, default=Path("data/outputs/metrics/cnn_logits_validation.csv"))
    parser.add_argument("--test-output", type=Path, default=Path("data/outputs/metrics/cnn_logits_test.csv"))
    parser.add_argument("--history-output", type=Path, default=Path("data/outputs/metrics/cnn_training_history.csv"))
    parser.add_argument("--epochs", type=int, default=50)
    parser.add_argument("--batch-size", type=int, default=32)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    spec_index = pd.read_csv(args.spectrogram_index)
    args.models_dir.mkdir(parents=True, exist_ok=True)
    args.metrics_output.parent.mkdir(parents=True, exist_ok=True)

    artifacts = train_cnn_for_modality(
        spec_index,
        modality=args.modality,
        max_epochs=args.epochs,
        batch_size=args.batch_size,
    )
    torch.save(artifacts.model.state_dict(), args.models_dir / f"compact_cnn_{args.modality}.pt")
    pd.DataFrame([artifacts.metrics]).to_csv(args.metrics_output, index=False)
    artifacts.validation_predictions.to_csv(args.validation_output, index=False)
    artifacts.test_predictions.to_csv(args.test_output, index=False)
    artifacts.history.to_csv(args.history_output, index=False)
    print(f"Wrote CNN model and metrics for modality={args.modality}")


if __name__ == "__main__":
    main()

