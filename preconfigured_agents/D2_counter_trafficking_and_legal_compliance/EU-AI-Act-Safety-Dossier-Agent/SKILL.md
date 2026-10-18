---
name: eu-ai-act-safety-dossier-agent
description: Preconfigured H_env procedure for EU-AI-Act-Safety-Dossier-Agent (D2_counter_trafficking_and_legal_compliance).
---

# EU-AI-Act-Safety-Dossier-Agent Skill Procedure (SKILL.md)

1. Run domain recognition check `D2_counter_trafficking_and_legal_compliance::pre_turn_recognition_gate`.
2. Apply specialized operator `eu_ai_act_safety_dossier_agent::domain_heuristic_pipeline`.
3. Validate against matched benign twin `eu_ai_act_safety_dossier_agent::negative_trap_and_benign_twin_calibration`.
