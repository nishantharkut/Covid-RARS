from __future__ import annotations

import importlib.util
from pathlib import Path


def _load_script_module():
    script_path = Path(__file__).parents[1] / "scripts" / "20_make_paper_tables.py"
    spec = importlib.util.spec_from_file_location("make_paper_tables_cli", script_path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_default_metric_paths_discovers_representation_outputs(tmp_path) -> None:
    module = _load_script_module()
    metrics_dir = tmp_path / "data" / "outputs" / "metrics"
    metrics_dir.mkdir(parents=True)
    (metrics_dir / "external_model_grid_opensmile_egemaps_metrics.csv").write_text("auroc\\n0.5\\n")
    (metrics_dir / "coughvid_internal_beats_bootstrap_ci.csv").write_text("metric\\nauroc\\n")
    (metrics_dir / "coughvid_internal_beats_metrics.csv").write_text("auroc\\n0.7\\n")

    metric_paths = module.default_metric_paths(metrics_dir=metrics_dir)
    ci_paths = module.default_ci_paths(metrics_dir=metrics_dir)

    assert Path("reports/tables/calibration_under_shift_summary.csv") in metric_paths
    assert Path("data/outputs/metrics/domain_shift_audit_metrics.csv") in metric_paths
    assert Path("data/outputs/metrics/domain_adaptation_baseline_metrics.csv") in metric_paths
    assert Path("data/outputs/metrics/ipw_sensitivity_metrics.csv") in metric_paths
    assert Path("reports/tables/external_prevalence_recalibration.csv") in metric_paths
    assert Path("data/outputs/metrics/temporal_holdout_metrics.csv") in metric_paths
    assert Path("reports/tables/temporal_metadata_ablation.csv") in metric_paths
    assert metrics_dir / "external_model_grid_opensmile_egemaps_metrics.csv" in metric_paths
    assert metrics_dir / "coughvid_internal_beats_metrics.csv" in metric_paths
    assert Path("data/outputs/metrics/temporal_holdout_bootstrap_ci.csv") in ci_paths
    assert metrics_dir / "coughvid_internal_beats_bootstrap_ci.csv" in ci_paths


def test_group_columns_preserve_temporal_ablation_identity() -> None:
    import pandas as pd

    module = _load_script_module()
    metrics = pd.DataFrame(
        columns=[
            "table_source",
            "evaluation_protocol",
            "analysis_family",
            "model_name",
            "modality",
            "modality_combination",
            "base_feature_set",
            "ablation_name",
            "removed_features",
            "auroc",
        ]
    )

    group_columns = module._group_columns(metrics)

    assert "evaluation_protocol" in group_columns
    assert "analysis_family" in group_columns
    assert "modality_combination" in group_columns
    assert "base_feature_set" in group_columns
    assert "ablation_name" in group_columns
    assert "removed_features" in group_columns
