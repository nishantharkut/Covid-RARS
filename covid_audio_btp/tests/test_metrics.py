import numpy as np

from covid_audio_btp.metrics import expected_calibration_error


def test_ece_perfect_predictions_is_low():
    y_true = np.array([0, 1, 0, 1])
    y_prob = np.array([0.01, 0.99, 0.02, 0.98])

    assert expected_calibration_error(y_true, y_prob, n_bins=2) < 0.05

