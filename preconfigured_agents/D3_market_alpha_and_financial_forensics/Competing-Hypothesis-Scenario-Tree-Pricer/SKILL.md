---
name: competing-hypothesis-scenario-tree-pricer
description: Preconfigured H_env procedure for Competing-Hypothesis-Scenario-Tree-Pricer (D3_market_alpha_and_financial_forensics).
---

# Competing-Hypothesis-Scenario-Tree-Pricer Skill Procedure (SKILL.md)

1. Run domain recognition check `D3_market_alpha_and_financial_forensics::pre_turn_recognition_gate`.
2. Apply specialized operator `competing_hypothesis_scenario_tree_pricer::domain_heuristic_pipeline`.
3. Validate against matched benign twin `competing_hypothesis_scenario_tree_pricer::negative_trap_and_benign_twin_calibration`.
