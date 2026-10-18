---
name: matched-benign-twin-calibrator
description: Preconfigured H_env procedure for Matched-Benign-Twin-Calibrator (D2_counter_trafficking_and_legal_compliance).
---

# Matched-Benign-Twin-Calibrator Skill Procedure (SKILL.md)

1. Run domain recognition check `D2_counter_trafficking_and_legal_compliance::pre_turn_recognition_gate`.
2. Apply specialized operator `matched_benign_twin_calibrator::domain_heuristic_pipeline`.
3. Validate against matched benign twin `matched_benign_twin_calibrator::negative_trap_and_benign_twin_calibration`.
