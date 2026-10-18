---
name: injection-ssrf-eliminator
description: Preconfigured H_env procedure for Injection-SSRF-Eliminator (D1_secure_repo_and_backend_coding).
---

# Injection-SSRF-Eliminator Skill Procedure (SKILL.md)

1. Run domain recognition check `D1_secure_repo_and_backend_coding::pre_turn_recognition_gate`.
2. Apply specialized operator `injection_ssrf_eliminator::domain_heuristic_pipeline`.
3. Validate against matched benign twin `injection_ssrf_eliminator::negative_trap_and_benign_twin_calibration`.
