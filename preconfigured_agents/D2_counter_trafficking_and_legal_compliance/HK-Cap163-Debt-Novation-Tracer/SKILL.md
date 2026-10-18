---
name: hk-cap163-debt-novation-tracer
description: Preconfigured H_env procedure for HK-Cap163-Debt-Novation-Tracer (D2_counter_trafficking_and_legal_compliance).
---

# HK-Cap163-Debt-Novation-Tracer Skill Procedure (SKILL.md)

1. Run domain recognition check `D2_counter_trafficking_and_legal_compliance::pre_turn_recognition_gate`.
2. Apply specialized operator `hk_cap163_debt_novation_tracer::domain_heuristic_pipeline`.
3. Validate against matched benign twin `hk_cap163_debt_novation_tracer::negative_trap_and_benign_twin_calibration`.
