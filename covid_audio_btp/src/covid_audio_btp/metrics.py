from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.metrics import (
    average_precision_score,
    balanced_accuracy_score,
    brier_score_loss,
    confusion_matrix,
    f1_score,
    log_loss,
    roc_auc_score,
)

from covid_audio_btp.labels import label_to_int


def expected_calibration_error(y_true: np.ndarray, y_prob: np.ndarray, n_bins: int = 10) -> float:
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.asarray(y_prob).astype(float)
    bins = np.linspace(0.0, 1.0, n_bins + 1)
    ece = 0.0
    for lower, upper in zip(bins[:-1], bins[1:]):
        mask = (y_prob > lower) & (y_prob <= upper)
        if lower == 0.0:
            mask = (y_prob >= lower) & (y_prob <= upper)
        if not np.any(mask):
            continue
        confidence = float(np.mean(y_prob[mask]))
        accuracy = float(np.mean(y_true[mask]))
        ece += float(np.mean(mask)) * abs(accuracy - confidence)
    return float(ece)


def binary_metric_bundle(y_true: np.ndarray, y_prob: np.ndarray, threshold: float = 0.5) -> dict[str, float]:
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.asarray(y_prob).astype(float)
    y_pred = (y_prob >= threshold).astype(int)

    metrics: dict[str, float] = {}
    if len(np.unique(y_true)) == 2:
        metrics["auroc"] = float(roc_auc_score(y_true, y_prob))
        metrics["auprc"] = float(average_precision_score(y_true, y_prob))
    else:
        metrics["auroc"] = float("nan")
        metrics["auprc"] = float("nan")

    metrics["balanced_accuracy"] = float(balanced_accuracy_score(y_true, y_pred))
    metrics["f1"] = float(f1_score(y_true, y_pred, zero_division=0))
    cm = confusion_matrix(y_true, y_pred, labels=[0, 1])
    tn, fp, fn, tp = cm.ravel()
    metrics["sensitivity"] = float(tp / max(1, tp + fn))
    metrics["specificity"] = float(tn / max(1, tn + fp))
    metrics["brier"] = float(brier_score_loss(y_true, y_prob))
    metrics["ece"] = expected_calibration_error(y_true, y_prob)
    clipped = np.clip(y_prob, 1e-6, 1 - 1e-6)
    metrics["nll"] = float(log_loss(y_true, clipped, labels=[0, 1]))
    metrics["threshold"] = float(threshold)
    metrics["n_samples"] = float(len(y_true))
    return metrics


def labels_to_binary(labels: pd.Series) -> np.ndarray:
    return labels.map(label_to_int).to_numpy(dtype=int)


def evaluate_predictions(
    predictions: pd.DataFrame,
    probability_column: str = "probability",
    label_column: str = "label_binary",
    group_columns: list[str] | None = None,
) -> pd.DataFrame:
    group_columns = group_columns or []
    rows = []
    if group_columns:
        iterator = predictions.groupby(group_columns, dropna=False)
    else:
        iterator = [((), predictions)]
    for group_key, group in iterator:
        if group.empty or not group[label_column].isin(["positive", "negative"]).all():
            continue
        y_true = labels_to_binary(group[label_column])
        y_prob = group[probability_column].astype(float).to_numpy()
        row = binary_metric_bundle(y_true, y_prob)
        if group_columns:
            if not isinstance(group_key, tuple):
                group_key = (group_key,)
            row.update(dict(zip(group_columns, group_key)))
        rows.append(row)
    return pd.DataFrame(rows)

