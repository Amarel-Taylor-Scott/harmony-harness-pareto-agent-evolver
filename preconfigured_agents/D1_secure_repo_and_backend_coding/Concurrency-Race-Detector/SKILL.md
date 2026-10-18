---
name: concurrency-race-detector
description: Preconfigured H_env procedure for Concurrency-Race-Detector (D1_secure_repo_and_backend_coding).
---

# Concurrency-Race-Detector Skill Procedure (SKILL.md)

1. Run domain recognition check `D1_secure_repo_and_backend_coding::pre_turn_recognition_gate`.
2. Apply specialized operator `concurrency_race_detector::domain_heuristic_pipeline`.
3. Validate against matched benign twin `concurrency_race_detector::negative_trap_and_benign_twin_calibration`.
