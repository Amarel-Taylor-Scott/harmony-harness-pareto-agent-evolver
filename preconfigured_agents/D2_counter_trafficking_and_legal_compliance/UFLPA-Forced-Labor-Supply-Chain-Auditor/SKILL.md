---
name: uflpa-forced-labor-supply-chain-auditor
description: Preconfigured H_env procedure for UFLPA-Forced-Labor-Supply-Chain-Auditor (D2_counter_trafficking_and_legal_compliance).
---

# UFLPA-Forced-Labor-Supply-Chain-Auditor Skill Procedure (SKILL.md)

1. Run domain recognition check `D2_counter_trafficking_and_legal_compliance::pre_turn_recognition_gate`.
2. Apply specialized operator `uflpa_forced_labor_supply_chain_auditor::domain_heuristic_pipeline`.
3. Validate against matched benign twin `uflpa_forced_labor_supply_chain_auditor::negative_trap_and_benign_twin_calibration`.
