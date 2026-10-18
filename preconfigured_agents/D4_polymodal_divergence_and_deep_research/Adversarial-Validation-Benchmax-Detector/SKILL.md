---
name: adversarial-validation-benchmax-detector
description: Preconfigured H_env procedure for Adversarial-Validation-Benchmax-Detector (D4_polymodal_divergence_and_deep_research).
---

# Adversarial-Validation-Benchmax-Detector Skill Procedure (SKILL.md)

1. Run domain recognition check `D4_polymodal_divergence_and_deep_research::pre_turn_recognition_gate`.
2. Apply specialized operator `adversarial_validation_benchmax_detector::domain_heuristic_pipeline`.
3. Validate against matched benign twin `adversarial_validation_benchmax_detector::negative_trap_and_benign_twin_calibration`.
