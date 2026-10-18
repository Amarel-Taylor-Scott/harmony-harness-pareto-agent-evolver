---
name: brownfield-legacy-refactor-surgeon
description: Preconfigured H_env procedure for Brownfield-Legacy-Refactor-Surgeon (D1_secure_repo_and_backend_coding).
---

# Brownfield-Legacy-Refactor-Surgeon Skill Procedure (SKILL.md)

1. Run domain recognition check `D1_secure_repo_and_backend_coding::pre_turn_recognition_gate`.
2. Apply specialized operator `brownfield_legacy_refactor_surgeon::domain_heuristic_pipeline`.
3. Validate against matched benign twin `brownfield_legacy_refactor_surgeon::negative_trap_and_benign_twin_calibration`.
