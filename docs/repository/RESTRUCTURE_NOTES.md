# Repository Restructure Notes

This note records the non-destructive layout cleanup.

## Principle

The active package remains at `covid_audio_btp/`. Historical evidence was moved out of the root into professional buckets. Original folder and file names were preserved inside those buckets wherever practical.

## Main Relocations

| Old root location | New location |
|---|---|
| `Final_BTP_Publication_Results_2026-06-12/` | `results/frozen/Final_BTP_Publication_Results_2026-06-12/` |
| `Publication_ExternalValidation_Artifacts_2026-06-12/` | `results/frozen/Publication_ExternalValidation_Artifacts_2026-06-12/` |
| `Corrected_Coswara_NoLeakage_Results/` | `results/frozen/Corrected_Coswara_NoLeakage_Results/` |
| `Corrected_Coswara_NoLeakage_Windows_2026-06-12/` | `results/frozen/Corrected_Coswara_NoLeakage_Windows_2026-06-12/` |
| `Phase3_Coswara_Results/` | `results/frozen/Phase3_Coswara_Results/` |
| `CNN_Cough_Results/` | `results/frozen/CNN_Cough_Results/` |
| `Representation_Results_OpenSMILE_BEATs_2026-06-12/` | `results/representations/Representation_Results_OpenSMILE_BEATs_2026-06-12/` |
| `Representation_Results_OpenSMILE_BEATs_PANNs_2026-06-12/` | `results/representations/Representation_Results_OpenSMILE_BEATs_PANNs_2026-06-12/` |
| Root `*.zip` and `*.tar.gz` evidence bundles | `artifacts/bundles/` |
| Root `*.patch` files | `archive/patches/` |
| `11-June-Update/` | `archive/updates/11-June-Update/` |
| Root Gemini review exports | `archive/review_materials/` |
| Root status and decision notes | `docs/status/` |
| Root runbooks | `docs/runbooks/` |
| `covid_audio_btp/manuscripts/` | `manuscripts/` |

## What Was Not Changed

- No active package source path was moved.
- No experiment was rerun.
- No result metric was edited.
- No compressed evidence bundle was regenerated.
- Historical duplicate review exports were retained rather than deduplicated.

## Active Entry Points After Cleanup

- Root README: `README.md`
- Active package: `covid_audio_btp/`
- Repository map: `docs/repository/REPOSITORY_MAP.md`
- Artifact review guide: `ARTIFACT.md`
- Frozen results: `results/`
- Manuscripts: `manuscripts/`
