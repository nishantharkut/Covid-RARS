from __future__ import annotations

from pathlib import Path
import re

import numpy as np
import pandas as pd

from covid_audio_btp.audio_io import load_audio
from covid_audio_btp.preprocess import preprocess_for_features


def sanitize_feature_name(name: object) -> str:
    text = str(name)
    sanitized = re.sub(r"[^0-9A-Za-z]+", "_", text).strip("_")
    return sanitized or "feature"


def flatten_smile_frame(frame: pd.DataFrame, prefix: str) -> dict[str, float]:
    numeric = frame.select_dtypes(include=[np.number])
    if numeric.empty:
        raise ValueError("OpenSMILE produced no numeric features")
    means = numeric.mean(axis=0)
    return {
        f"{prefix}_{sanitize_feature_name(column)}": float(value)
        for column, value in means.items()
        if np.isfinite(float(value))
    }


def make_smile_extractor(feature_set: str = "egemaps"):
    try:
        import opensmile
    except Exception as exc:  # pragma: no cover - optional dependency
        raise RuntimeError("opensmile is not installed. Install with: python -m pip install opensmile") from exc

    normalized = sanitize_feature_name(feature_set).lower()
    feature_sets = {
        "egemaps": opensmile.FeatureSet.eGeMAPSv02,
        "egemapsv02": opensmile.FeatureSet.eGeMAPSv02,
        "egemapsv2": opensmile.FeatureSet.eGeMAPSv02,
        "compare": opensmile.FeatureSet.ComParE_2016,
        "compare2016": opensmile.FeatureSet.ComParE_2016,
    }
    if normalized not in feature_sets:
        raise ValueError(f"Unsupported OpenSMILE feature set: {feature_set}")
    return opensmile.Smile(
        feature_set=feature_sets[normalized],
        feature_level=opensmile.FeatureLevel.Functionals,
    )


def extract_opensmile_features_for_row(
    row: pd.Series,
    *,
    smile,
    representation_name: str = "opensmile_egemaps",
) -> dict[str, object]:
    y, sample_rate, _ = load_audio(Path(row["audio_path"]))
    processed, event_info = preprocess_for_features(y, sample_rate, str(row.get("modality", "unknown")))
    frame = smile.process_signal(processed.astype(np.float32, copy=False), sample_rate)
    features = flatten_smile_frame(frame, prefix=representation_name)

    output: dict[str, object] = {
        "recording_id": row["recording_id"],
        "participant_id": row["participant_id"],
        "dataset": row.get("dataset", "coswara"),
        "modality": row.get("modality", "unknown"),
        "submodality": row.get("submodality", "unknown"),
        "label_binary": row.get("label_binary", "unknown"),
        "split": row.get("split", "unused"),
        "representation": representation_name,
    }
    for optional_col in ("quality_flag", "manual_quality_label"):
        if optional_col in row:
            output[optional_col] = row.get(optional_col)
    output.update(event_info)
    output.update(features)
    return output


def extract_opensmile_feature_table(
    metadata: pd.DataFrame,
    *,
    smile=None,
    feature_set: str = "egemaps",
    quality_mode: str = "all_samples",
    modality: str | None = None,
    max_rows: int | None = None,
    representation_name: str | None = None,
    strict: bool = False,
) -> pd.DataFrame:
    if quality_mode not in {"all_samples", "quality_ok_only"}:
        raise ValueError(f"Unknown quality_mode: {quality_mode}")

    representation = representation_name or f"opensmile_{sanitize_feature_name(feature_set).lower()}"
    extractor = smile if smile is not None else make_smile_extractor(feature_set)
    df = metadata[metadata["label_binary"].isin(["positive", "negative"])].copy()
    if modality is not None:
        df = df[df["modality"] == modality].copy()
    if quality_mode == "quality_ok_only" and "quality_flag" in df.columns:
        df = df[df["quality_flag"] == "ok"].copy()
    if max_rows is not None:
        df = df.head(max(0, int(max_rows))).copy()

    rows: list[dict[str, object]] = []
    for _, row in df.iterrows():
        try:
            rows.append(
                extract_opensmile_features_for_row(
                    row,
                    smile=extractor,
                    representation_name=representation,
                )
            )
        except Exception as exc:
            if strict:
                raise
            print(f"WARNING: skipping {row.get('audio_path', '?')} — {exc}")
    return pd.DataFrame(rows)
