import json
from pathlib import Path

import numpy as np
import pandas as pd


def test_paired_bootstrap_difference_detects_model_delta():
    from covid_audio_btp.model_comparison import paired_bootstrap_difference

    predictions = pd.DataFrame(
        {
            "recording_id": ["r1", "r2", "r3", "r4", "r1", "r2", "r3", "r4"],
            "label_binary": ["negative", "negative", "positive", "positive"] * 2,
            "model_name": ["weak"] * 4 + ["strong"] * 4,
            "probability": [0.45, 0.40, 0.55, 0.60, 0.05, 0.15, 0.85, 0.95],
        }
    )

    result = paired_bootstrap_difference(
        predictions,
        baseline_name="weak",
        candidate_name="strong",
        model_column="model_name",
        metric="brier",
        n_bootstraps=100,
        random_state=7,
    )

    assert result["baseline_name"] == "weak"
    assert result["candidate_name"] == "strong"
    assert result["metric"] == "brier"
    assert result["difference"] < 0.0
    assert result["n_matched"] == 4
    assert result["ci_low"] <= result["difference"] <= result["ci_high"]


def test_coarsened_matching_balances_label_groups_by_age_bucket_and_gender():
    from covid_audio_btp.confounding import balance_table, coarsened_exact_match

    metadata = pd.DataFrame(
        {
            "recording_id": [f"r{i}" for i in range(8)],
            "participant_id": [f"p{i}" for i in range(8)],
            "label_binary": ["positive", "negative"] * 4,
            "age": [22, 23, 39, 38, 54, 55, 70, 72],
            "gender": ["female", "female", "male", "male", "female", "female", "male", "male"],
        }
    )

    matched = coarsened_exact_match(metadata, covariates=["age_bucket", "gender"])
    balance = balance_table(matched, covariates=["age_bucket", "gender"])

    assert len(matched) == 8
    assert set(matched["matched_set_id"]) == {"age_bucket=<30|gender=female", "age_bucket=30-44|gender=male", "age_bucket=45-59|gender=female", "age_bucket=60+|gender=male"}
    assert balance["max_abs_standardized_difference"].max() == 0.0


def test_feature_shift_report_ranks_shifted_numeric_features():
    from covid_audio_btp.shift import feature_shift_report

    source = pd.DataFrame({"recording_id": ["s1", "s2", "s3"], "mfcc_1": [0.0, 0.1, 0.2], "mfcc_2": [1.0, 1.0, 1.0]})
    external = pd.DataFrame({"recording_id": ["e1", "e2", "e3"], "mfcc_1": [5.0, 5.1, 5.2], "mfcc_2": [1.0, 1.0, 1.0]})

    report = feature_shift_report(source, external, id_columns=["recording_id"])

    assert report.iloc[0]["feature"] == "mfcc_1"
    assert report.iloc[0]["abs_standardized_mean_difference"] > 1.0
    assert report.loc[report["feature"] == "mfcc_2", "abs_standardized_mean_difference"].iloc[0] == 0.0


def test_manifest_records_config_and_sha256(tmp_path):
    from covid_audio_btp.manifest import build_experiment_manifest

    artifact = tmp_path / "metrics.csv"
    artifact.write_text("metric,value\nauroc,0.8\n", encoding="utf-8")

    manifest = build_experiment_manifest(
        config={"seed": 42, "run_name": "toy"},
        artifact_paths=[artifact],
        include_packages=["python"],
    )

    assert manifest["config"]["seed"] == 42
    assert manifest["artifacts"][0]["path"].endswith("metrics.csv")
    assert len(manifest["artifacts"][0]["sha256"]) == 64
    assert "created_at_utc" in manifest
