from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pandas as pd


def test_temporal_stress_summary_merges_ci_and_external_lift() -> None:
    from covid_audio_btp.temporal_paper_summary import build_temporal_stress_test_summary

    metrics = pd.DataFrame(
        [
            {
                "evaluation_protocol": "existing_participant_split",
                "analysis_family": "multimodal_fusion",
                "model_name": "logistic_regression",
                "modality": "multimodal",
                "modality_combination": "breath+cough+speech",
                "fusion_method": "uniform_mean",
                "auroc": 0.873,
                "auprc": 0.807,
                "auprc_lift_over_prevalence": 0.483,
                "brier": 0.17,
                "ece": 0.19,
                "n_samples": 318,
            },
            {
                "evaluation_protocol": "temporal_early_to_late",
                "analysis_family": "multimodal_fusion",
                "model_name": "logistic_regression",
                "modality": "multimodal",
                "modality_combination": "breath+cough+speech",
                "fusion_method": "uniform_mean",
                "auroc": 0.566,
                "auprc": 0.822,
                "auprc_lift_over_prevalence": 0.018,
                "brier": 0.33,
                "ece": 0.40,
                "n_samples": 424,
            },
        ]
    )
    bootstrap = pd.DataFrame(
        [
            {
                "evaluation_protocol": "existing_participant_split",
                "analysis_family": "multimodal_fusion",
                "model_name": "logistic_regression",
                "modality": "multimodal",
                "modality_combination": "breath+cough+speech",
                "fusion_method": "uniform_mean",
                "metric": "auroc",
                "ci_low": 0.83,
                "ci_high": 0.91,
            },
            {
                "evaluation_protocol": "temporal_early_to_late",
                "analysis_family": "multimodal_fusion",
                "model_name": "logistic_regression",
                "modality": "multimodal",
                "modality_combination": "breath+cough+speech",
                "fusion_method": "uniform_mean",
                "metric": "auroc",
                "ci_low": 0.49,
                "ci_high": 0.63,
            },
        ]
    )
    evidence = pd.DataFrame(
        [
            {
                "claim_id": "external_transfer_beats_best",
                "comparison": "BEATs / logistic_regression / drop_high_shift",
                "primary_metric": "auroc",
                "primary_value": 0.553,
                "secondary_metrics": "auprc=0.039; balanced_accuracy=0.515",
                "n_samples": 8331,
            }
        ]
    )
    external_lift = pd.DataFrame(
        [
            {
                "representation": "beats",
                "model_name": "logistic_regression",
                "feature_strategy": "drop_high_shift",
                "auroc": 0.553,
                "auprc": 0.039,
                "absolute_auprc_lift": 0.005,
            }
        ]
    )

    summary = build_temporal_stress_test_summary(metrics, bootstrap, evidence, external_lift)

    assert ["participant_internal", "temporal_holdout", "external_transfer"] == list(summary["stress_test"])
    participant = summary[summary["stress_test"].eq("participant_internal")].iloc[0]
    temporal = summary[summary["stress_test"].eq("temporal_holdout")].iloc[0]
    external = summary[summary["stress_test"].eq("external_transfer")].iloc[0]
    assert participant["auroc_ci_low"] == 0.83
    assert temporal["auroc_ci_high"] == 0.63
    assert external["auroc"] == 0.553
    assert external["auprc_lift_over_prevalence"] == 0.005


def test_temporal_feature_attribution_comparison_aligns_protocol_importance() -> None:
    from covid_audio_btp.temporal_paper_summary import build_temporal_feature_attribution_comparison

    importance = pd.DataFrame(
        [
            {
                "evaluation_protocol": "existing_participant_split",
                "audit_model": "demographic_protocol_only",
                "feature": "recording_year",
                "feature_group": "recording_protocol",
                "importance_abs": 2.0,
                "coefficient": 2.0,
            },
            {
                "evaluation_protocol": "existing_participant_split",
                "audit_model": "demographic_protocol_only",
                "feature": "age",
                "feature_group": "demographic",
                "importance_abs": 0.5,
                "coefficient": 0.5,
            },
            {
                "evaluation_protocol": "temporal_early_to_late",
                "audit_model": "demographic_protocol_only",
                "feature": "recording_year",
                "feature_group": "recording_protocol",
                "importance_abs": 0.2,
                "coefficient": -0.2,
            },
            {
                "evaluation_protocol": "time_stratified_participant_split",
                "audit_model": "demographic_protocol_only",
                "feature": "recording_year",
                "feature_group": "recording_protocol",
                "importance_abs": 1.8,
                "coefficient": 1.8,
            },
        ]
    )

    comparison = build_temporal_feature_attribution_comparison(importance)

    row = comparison[
        comparison["audit_model"].eq("demographic_protocol_only")
        & comparison["feature"].eq("recording_year")
    ].iloc[0]
    assert row["existing_importance_abs"] == 2.0
    assert row["temporal_importance_abs"] == 0.2
    assert row["time_stratified_importance_abs"] == 1.8
    assert row["delta_temporal_minus_existing"] == -1.8
    assert row["existing_rank"] == 1


def test_temporal_paper_summary_cli_writes_outputs(tmp_path: Path) -> None:
    metrics = pd.DataFrame(
        [
            {
                "evaluation_protocol": "existing_participant_split",
                "analysis_family": "multimodal_fusion",
                "model_name": "logistic_regression",
                "modality": "multimodal",
                "modality_combination": "breath+cough+speech",
                "fusion_method": "uniform_mean",
                "auroc": 0.873,
                "auprc": 0.807,
                "auprc_lift_over_prevalence": 0.483,
                "n_samples": 318,
            },
            {
                "evaluation_protocol": "temporal_early_to_late",
                "analysis_family": "multimodal_fusion",
                "model_name": "logistic_regression",
                "modality": "multimodal",
                "modality_combination": "breath+cough+speech",
                "fusion_method": "uniform_mean",
                "auroc": 0.566,
                "auprc": 0.822,
                "auprc_lift_over_prevalence": 0.018,
                "n_samples": 424,
            },
        ]
    )
    bootstrap = pd.DataFrame(
        [
            {
                "evaluation_protocol": "existing_participant_split",
                "analysis_family": "multimodal_fusion",
                "model_name": "logistic_regression",
                "modality": "multimodal",
                "modality_combination": "breath+cough+speech",
                "fusion_method": "uniform_mean",
                "metric": "auroc",
                "ci_low": 0.83,
                "ci_high": 0.91,
            }
        ]
    )
    importance = pd.DataFrame(
        [
            {
                "evaluation_protocol": "existing_participant_split",
                "audit_model": "demographic_protocol_only",
                "feature": "recording_year",
                "feature_group": "recording_protocol",
                "importance_abs": 2.0,
                "coefficient": 2.0,
            }
        ]
    )
    evidence = pd.DataFrame(
        [
            {
                "claim_id": "external_transfer_beats_best",
                "comparison": "BEATs / logistic_regression / drop_high_shift",
                "primary_metric": "auroc",
                "primary_value": 0.553,
                "secondary_metrics": "auprc=0.039",
                "n_samples": 8331,
            }
        ]
    )

    metrics_path = tmp_path / "metrics.csv"
    bootstrap_path = tmp_path / "bootstrap.csv"
    importance_path = tmp_path / "importance.csv"
    evidence_path = tmp_path / "evidence.csv"
    predictions = pd.DataFrame(
        [
            {
                "participant_id": "p1",
                "label_binary": "positive",
                "split": "test",
                "evaluation_protocol": "existing_participant_split",
                "analysis_family": "multimodal_fusion",
                "model_name": "logistic_regression",
                "modality": "multimodal",
                "modality_combination": "breath+cough+speech",
                "fusion_method": "uniform_mean",
                "probability": 0.8,
            },
            {
                "participant_id": "p2",
                "label_binary": "negative",
                "split": "test",
                "evaluation_protocol": "existing_participant_split",
                "analysis_family": "multimodal_fusion",
                "model_name": "logistic_regression",
                "modality": "multimodal",
                "modality_combination": "breath+cough+speech",
                "fusion_method": "uniform_mean",
                "probability": 0.2,
            },
            {
                "participant_id": "p3",
                "label_binary": "positive",
                "split": "test",
                "evaluation_protocol": "temporal_early_to_late",
                "analysis_family": "multimodal_fusion",
                "model_name": "logistic_regression",
                "modality": "multimodal",
                "modality_combination": "breath+cough+speech",
                "fusion_method": "uniform_mean",
                "probability": 0.6,
            },
            {
                "participant_id": "p4",
                "label_binary": "negative",
                "split": "test",
                "evaluation_protocol": "temporal_early_to_late",
                "analysis_family": "multimodal_fusion",
                "model_name": "logistic_regression",
                "modality": "multimodal",
                "modality_combination": "breath+cough+speech",
                "fusion_method": "uniform_mean",
                "probability": 0.4,
            },
        ]
    )
    predictions_path = tmp_path / "predictions.csv"
    stress_output = tmp_path / "stress.csv"
    feature_output = tmp_path / "features.csv"
    significance_output = tmp_path / "significance.csv"
    causal_chain_output = tmp_path / "causal_chain.md"
    metrics.to_csv(metrics_path, index=False)
    bootstrap.to_csv(bootstrap_path, index=False)
    importance.to_csv(importance_path, index=False)
    evidence.to_csv(evidence_path, index=False)
    predictions.to_csv(predictions_path, index=False)

    script = Path(__file__).parents[1] / "scripts" / "45_temporal_paper_summaries.py"
    spec = importlib.util.spec_from_file_location("temporal_summary_cli", script)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    old_argv = sys.argv
    try:
        sys.argv = [
            "45_temporal_paper_summaries.py",
            "--temporal-metrics",
            str(metrics_path),
            "--temporal-bootstrap",
            str(bootstrap_path),
            "--metadata-importance",
            str(importance_path),
            "--temporal-predictions",
            str(predictions_path),
            "--evidence-matrix",
            str(evidence_path),
            "--stress-summary-output",
            str(stress_output),
            "--feature-comparison-output",
            str(feature_output),
            "--significance-output",
            str(significance_output),
            "--causal-chain-output",
            str(causal_chain_output),
            "--significance-bootstraps",
            "25",
        ]
        module.main()
    finally:
        sys.argv = old_argv

    assert stress_output.exists()
    assert feature_output.exists()
    assert significance_output.exists()
    assert causal_chain_output.exists()
    assert "external_transfer" in set(pd.read_csv(stress_output)["stress_test"])
    assert "recording_year" in set(pd.read_csv(feature_output)["feature"])
    assert "delta_auroc" in pd.read_csv(significance_output).columns
    assert "causal chain" in causal_chain_output.read_text().lower()


def test_temporal_delta_significance_estimates_auroc_drop() -> None:
    from covid_audio_btp.temporal_paper_summary import build_temporal_delta_significance

    rows = []
    for idx in range(30):
        label = "positive" if idx >= 15 else "negative"
        rows.append(
            {
                "participant_id": f"e_{idx}",
                "label_binary": label,
                "split": "test",
                "evaluation_protocol": "existing_participant_split",
                "analysis_family": "multimodal_fusion",
                "model_name": "logistic_regression",
                "modality": "multimodal",
                "modality_combination": "breath+cough+speech",
                "fusion_method": "uniform_mean",
                "probability": 0.9 if label == "positive" else 0.1,
            }
        )
        rows.append(
            {
                "participant_id": f"t_{idx}",
                "label_binary": label,
                "split": "test",
                "evaluation_protocol": "temporal_early_to_late",
                "analysis_family": "multimodal_fusion",
                "model_name": "logistic_regression",
                "modality": "multimodal",
                "modality_combination": "breath+cough+speech",
                "fusion_method": "uniform_mean",
                "probability": 0.55 if idx % 2 == 0 else 0.45,
            }
        )
    predictions = pd.DataFrame(rows)

    result = build_temporal_delta_significance(predictions, n_bootstraps=100, random_state=0)

    row = result.iloc[0]
    assert row["comparison"] == "temporal_minus_participant_full_multimodal"
    assert row["delta_auroc"] < 0
    assert 0 <= row["p_value_two_sided"] <= 1
    assert row["n_bootstraps"] > 0
