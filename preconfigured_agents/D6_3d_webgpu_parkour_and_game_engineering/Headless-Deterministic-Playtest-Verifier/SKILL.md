---
name: headless-deterministic-playtest-verifier
description: Preconfigured H_env procedure for Headless-Deterministic-Playtest-Verifier (D6_3d_webgpu_parkour_and_game_engineering).
---

# Headless-Deterministic-Playtest-Verifier Skill Procedure (SKILL.md)

1. Run domain recognition check `D6_3d_webgpu_parkour_and_game_engineering::pre_turn_recognition_gate`.
2. Apply specialized operator `headless_deterministic_playtest_verifier::domain_heuristic_pipeline`.
3. Validate against matched benign twin `headless_deterministic_playtest_verifier::negative_trap_and_benign_twin_calibration`.
