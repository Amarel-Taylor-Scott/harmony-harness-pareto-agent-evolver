---
name: procedural-arena-and-navmesh-generator
description: Preconfigured H_env procedure for Procedural-Arena-And-NavMesh-Generator (D6_3d_webgpu_parkour_and_game_engineering).
---

# Procedural-Arena-And-NavMesh-Generator Skill Procedure (SKILL.md)

1. Run domain recognition check `D6_3d_webgpu_parkour_and_game_engineering::pre_turn_recognition_gate`.
2. Apply specialized operator `procedural_arena_and_navmesh_generator::domain_heuristic_pipeline`.
3. Validate against matched benign twin `procedural_arena_and_navmesh_generator::negative_trap_and_benign_twin_calibration`.
