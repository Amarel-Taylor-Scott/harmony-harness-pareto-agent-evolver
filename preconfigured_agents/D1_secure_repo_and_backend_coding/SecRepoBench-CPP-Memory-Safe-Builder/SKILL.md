---
name: secrepobench-cpp-memory-safe-builder
description: Preconfigured H_env procedure for SecRepoBench-CPP-Memory-Safe-Builder (D1_secure_repo_and_backend_coding).
---

# SecRepoBench-CPP-Memory-Safe-Builder Skill Procedure (SKILL.md)

1. Run domain recognition check `D1_secure_repo_and_backend_coding::pre_turn_recognition_gate`.
2. Apply specialized operator `secrepobench_cpp_memory_safe_builder::domain_heuristic_pipeline`.
3. Validate against matched benign twin `secrepobench_cpp_memory_safe_builder::negative_trap_and_benign_twin_calibration`.
