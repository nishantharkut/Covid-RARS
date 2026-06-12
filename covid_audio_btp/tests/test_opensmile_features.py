from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from covid_audio_btp.opensmile_features import (
    extract_opensmile_feature_table,
    flatten_smile_frame,
)
from covid_audio_btp.representation_features import validate_feature_table


class _FakeSmile:
    def process_signal(self, signal: np.ndarray, sampling_rate: int) -> pd.DataFrame:
        assert signal.ndim == 1
        assert sampling_rate == 16_000
        return pd.DataFrame(
            {
                "F0semitoneFrom27.5Hz_sma3nz_amean": [1.25],
                "loudness_sma3_amean": [3.5],
            }
        )


def test_flatten_smile_frame_prefixes_and_sanitizes_feature_names() -> None:
    frame = pd.DataFrame(
        {
            "F0semitoneFrom27.5Hz_sma3nz_amean": [1.0, 3.0],
            "loudness/sma3 amean": [2.0, 4.0],
            "non_numeric": ["ignore", "ignore"],
        }
    )

    flattened = flatten_smile_frame(frame, prefix="opensmile_egemaps")

    assert flattened == {
        "opensmile_egemaps_F0semitoneFrom27_5Hz_sma3nz_amean": 2.0,
        "opensmile_egemaps_loudness_sma3_amean": 3.0,
    }


def test_extract_opensmile_feature_table_preserves_schema_and_quality_filter(monkeypatch) -> None:
    metadata = pd.DataFrame(
        {
            "recording_id": ["r1", "r2"],
            "participant_id": ["p1", "p2"],
            "dataset": ["coswara", "coswara"],
            "modality": ["cough", "cough"],
            "submodality": ["heavy_cough", "heavy_cough"],
            "label_binary": ["positive", "negative"],
            "split": ["train", "test"],
            "quality_flag": ["ok", "corrupt"],
            "audio_path": [str(Path("a.wav")), str(Path("b.wav"))],
        }
    )

    monkeypatch.setattr(
        "covid_audio_btp.opensmile_features.load_audio",
        lambda path: (np.ones(16_000, dtype=np.float32), 16_000, 16_000),
    )
    monkeypatch.setattr(
        "covid_audio_btp.opensmile_features.preprocess_for_features",
        lambda y, sample_rate, modality: (
            y.astype(np.float32, copy=False),
            {
                "event_start_sec": 0.0,
                "event_end_sec": 1.0,
                "event_duration_sec": 1.0,
                "active_audio_ratio": 1.0,
                "segmentation_method": "test",
            },
        ),
    )

    features = extract_opensmile_feature_table(
        metadata,
        smile=_FakeSmile(),
        quality_mode="quality_ok_only",
        representation_name="opensmile_egemaps",
    )

    assert features["recording_id"].tolist() == ["r1"]
    assert features["representation"].tolist() == ["opensmile_egemaps"]
    assert "opensmile_egemaps_loudness_sma3_amean" in features.columns
    assert validate_feature_table(features) == [
        "event_start_sec",
        "event_end_sec",
        "event_duration_sec",
        "active_audio_ratio",
        "opensmile_egemaps_F0semitoneFrom27_5Hz_sma3nz_amean",
        "opensmile_egemaps_loudness_sma3_amean",
    ]
