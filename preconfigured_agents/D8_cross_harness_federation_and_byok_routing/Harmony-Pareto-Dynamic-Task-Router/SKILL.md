---
name: harmony-pareto-dynamic-task-router
description: Preconfigured H_env procedure for Harmony-Pareto-Dynamic-Task-Router (D8_cross_harness_federation_and_byok_routing).
---

# Harmony-Pareto-Dynamic-Task-Router Skill Procedure (SKILL.md)

1. Run domain recognition check `D8_cross_harness_federation_and_byok_routing::pre_turn_recognition_gate`.
2. Apply specialized operator `harmony_pareto_dynamic_task_router::domain_heuristic_pipeline`.
3. Validate against matched benign twin `harmony_pareto_dynamic_task_router::negative_trap_and_benign_twin_calibration`.
