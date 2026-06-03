from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
import torch
from torch import nn
from torch.utils.data import DataLoader, Dataset

from covid_audio_btp.datasets import SpectrogramTableDataset
from covid_audio_btp.metrics import binary_metric_bundle
from covid_audio_btp.models_cnn import CompactSpectrogramCNN


class TorchSpectrogramDataset(Dataset):
    def __init__(self, table_dataset: SpectrogramTableDataset) -> None:
        self.table_dataset = table_dataset

    def __len__(self) -> int:
        return len(self.table_dataset)

    def __getitem__(self, idx: int):
        ex = self.table_dataset[idx]
        return (
            torch.from_numpy(ex.x),
            torch.tensor(ex.y, dtype=torch.float32),
            ex.recording_id,
            ex.participant_id,
        )


@dataclass
class CNNTrainArtifacts:
    model: CompactSpectrogramCNN
    metrics: dict[str, float | str]
    validation_predictions: pd.DataFrame
    test_predictions: pd.DataFrame
    history: pd.DataFrame


def _collect_logits(model: nn.Module, loader: DataLoader, device: str) -> tuple[list[str], list[str], np.ndarray, np.ndarray]:
    model.eval()
    recording_ids: list[str] = []
    participant_ids: list[str] = []
    logits_list: list[float] = []
    labels_list: list[float] = []
    with torch.no_grad():
        for x, y, rec_ids, part_ids in loader:
            x = x.to(device)
            logits = model(x).detach().cpu().numpy()
            logits_list.extend(logits.tolist())
            labels_list.extend(y.numpy().tolist())
            recording_ids.extend(list(rec_ids))
            participant_ids.extend(list(part_ids))
    return recording_ids, participant_ids, np.asarray(logits_list), np.asarray(labels_list)


def train_cnn_for_modality(
    spectrogram_index: pd.DataFrame,
    modality: str,
    max_epochs: int = 50,
    patience: int = 8,
    batch_size: int = 32,
    learning_rate: float = 1e-3,
    device: str | None = None,
) -> CNNTrainArtifacts:
    device = device or ("cuda" if torch.cuda.is_available() else "cpu")
    train_ds = TorchSpectrogramDataset(SpectrogramTableDataset(spectrogram_index, "train", modality))
    val_ds = TorchSpectrogramDataset(SpectrogramTableDataset(spectrogram_index, "validation", modality))
    test_ds = TorchSpectrogramDataset(SpectrogramTableDataset(spectrogram_index, "test", modality))
    if len(train_ds) == 0 or len(val_ds) == 0 or len(test_ds) == 0:
        raise ValueError(f"Need train/validation/test spectrograms for modality={modality}")

    train_loader = DataLoader(train_ds, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_ds, batch_size=batch_size, shuffle=False)
    test_loader = DataLoader(test_ds, batch_size=batch_size, shuffle=False)

    labels = np.array([train_ds[i][1].item() for i in range(len(train_ds))])
    positives = max(1, int(labels.sum()))
    negatives = max(1, int(len(labels) - labels.sum()))
    pos_weight = torch.tensor([negatives / positives], dtype=torch.float32, device=device)

    model = CompactSpectrogramCNN().to(device)
    criterion = nn.BCEWithLogitsLoss(pos_weight=pos_weight)
    optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate, weight_decay=1e-4)

    best_state = None
    best_val_loss = float("inf")
    bad_epochs = 0
    history_rows = []

    for epoch in range(1, max_epochs + 1):
        model.train()
        train_losses = []
        for x, y, _, _ in train_loader:
            x = x.to(device)
            y = y.to(device)
            optimizer.zero_grad()
            logits = model(x)
            loss = criterion(logits, y)
            loss.backward()
            optimizer.step()
            train_losses.append(float(loss.detach().cpu()))

        _, _, val_logits, val_y = _collect_logits(model, val_loader, device)
        val_loss = float(criterion(torch.tensor(val_logits, dtype=torch.float32, device=device), torch.tensor(val_y, dtype=torch.float32, device=device)).detach().cpu())
        history_rows.append(
            {"epoch": epoch, "train_loss": float(np.mean(train_losses)), "validation_loss": val_loss}
        )
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            best_state = {k: v.detach().cpu().clone() for k, v in model.state_dict().items()}
            bad_epochs = 0
        else:
            bad_epochs += 1
            if bad_epochs >= patience:
                break

    if best_state is not None:
        model.load_state_dict(best_state)

    val_rec, val_part, val_logits, val_y = _collect_logits(model, val_loader, device)
    test_rec, test_part, test_logits, test_y = _collect_logits(model, test_loader, device)
    val_prob = 1.0 / (1.0 + np.exp(-val_logits))
    test_prob = 1.0 / (1.0 + np.exp(-test_logits))
    metrics = binary_metric_bundle(test_y.astype(int), test_prob)
    metrics.update({"model_name": "compact_cnn", "modality": modality})

    def pred_frame(rec_ids, part_ids, logits, probs, y, split):
        return pd.DataFrame(
            {
                "recording_id": rec_ids,
                "participant_id": part_ids,
                "modality": modality,
                "label_binary": np.where(y.astype(int) == 1, "positive", "negative"),
                "split": split,
                "model_name": "compact_cnn",
                "logit": logits,
                "probability": probs,
            }
        )

    return CNNTrainArtifacts(
        model=model,
        metrics=metrics,
        validation_predictions=pred_frame(val_rec, val_part, val_logits, val_prob, val_y, "validation"),
        test_predictions=pred_frame(test_rec, test_part, test_logits, test_prob, test_y, "test"),
        history=pd.DataFrame(history_rows),
    )

