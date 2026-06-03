import pandas as pd
import pytest

from covid_audio_btp.split import assert_no_participant_leakage, build_modality_availability


def test_no_participant_leakage_passes():
    df = pd.DataFrame(
        {
            "participant_id": ["p1", "p2", "p3"],
            "split": ["train", "validation", "test"],
        }
    )

    assert_no_participant_leakage(df)


def test_no_participant_leakage_fails():
    df = pd.DataFrame(
        {
            "participant_id": ["p1", "p1"],
            "split": ["train", "test"],
        }
    )

    with pytest.raises(ValueError, match="participant leakage"):
        assert_no_participant_leakage(df)


def test_modality_availability_marks_complete_cases():
    df = pd.DataFrame(
        {
            "participant_id": ["p1", "p1", "p1", "p2"],
            "modality": ["cough", "breath", "speech", "cough"],
        }
    )

    availability = build_modality_availability(df)
    row_p1 = availability.set_index("participant_id").loc["p1"]
    row_p2 = availability.set_index("participant_id").loc["p2"]

    assert bool(row_p1["complete_case"]) is True
    assert bool(row_p2["complete_case"]) is False
    assert row_p1["available_modalities"] == "breath,cough,speech"

