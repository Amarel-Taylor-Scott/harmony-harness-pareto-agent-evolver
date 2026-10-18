---
name: auth-oauth2-boundary-hardener
description: Preconfigured H_env procedure for Auth-OAuth2-Boundary-Hardener (D1_secure_repo_and_backend_coding).
---

# Auth-OAuth2-Boundary-Hardener Skill Procedure (SKILL.md)

1. Run domain recognition check `D1_secure_repo_and_backend_coding::pre_turn_recognition_gate`.
2. Apply specialized operator `auth_oauth2_boundary_hardener::domain_heuristic_pipeline`.
3. Validate against matched benign twin `auth_oauth2_boundary_hardener::negative_trap_and_benign_twin_calibration`.
