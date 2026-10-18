---
name: codex-agents-md-worktree-orchestrator
description: Preconfigured H_env procedure for Codex-AGENTS-MD-Worktree-Orchestrator (D8_cross_harness_federation_and_byok_routing).
---

# Codex-AGENTS-MD-Worktree-Orchestrator Skill Procedure (SKILL.md)

1. Run domain recognition check `D8_cross_harness_federation_and_byok_routing::pre_turn_recognition_gate`.
2. Apply specialized operator `codex_agents_md_worktree_orchestrator::domain_heuristic_pipeline`.
3. Validate against matched benign twin `codex_agents_md_worktree_orchestrator::negative_trap_and_benign_twin_calibration`.
