---
name: consensus-echo-stripper-agent
description: Preconfigured H_env procedure for Consensus-Echo-Stripper-Agent (D3_market_alpha_and_financial_forensics).
---

# Consensus-Echo-Stripper-Agent Skill Procedure (SKILL.md)

1. Run domain recognition check `D3_market_alpha_and_financial_forensics::pre_turn_recognition_gate`.
2. Apply specialized operator `consensus_echo_stripper_agent::domain_heuristic_pipeline`.
3. Validate against matched benign twin `consensus_echo_stripper_agent::negative_trap_and_benign_twin_calibration`.
