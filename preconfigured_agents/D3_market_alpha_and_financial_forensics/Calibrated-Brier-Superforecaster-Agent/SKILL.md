---
name: calibrated-brier-superforecaster-agent
description: Preconfigured H_env procedure for Calibrated-Brier-Superforecaster-Agent (D3_market_alpha_and_financial_forensics).
---

# Calibrated-Brier-Superforecaster-Agent Skill Procedure (SKILL.md)

1. Run domain recognition check `D3_market_alpha_and_financial_forensics::pre_turn_recognition_gate`.
2. Apply specialized operator `calibrated_brier_superforecaster_agent::domain_heuristic_pipeline`.
3. Validate against matched benign twin `calibrated_brier_superforecaster_agent::negative_trap_and_benign_twin_calibration`.
