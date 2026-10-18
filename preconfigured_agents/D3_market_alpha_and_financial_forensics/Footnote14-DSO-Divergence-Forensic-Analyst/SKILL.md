---
name: footnote14-dso-divergence-forensic-analyst
description: Preconfigured H_env procedure for Footnote14-DSO-Divergence-Forensic-Analyst (D3_market_alpha_and_financial_forensics).
---

# Footnote14-DSO-Divergence-Forensic-Analyst Skill Procedure (SKILL.md)

1. Run domain recognition check `D3_market_alpha_and_financial_forensics::pre_turn_recognition_gate`.
2. Apply specialized operator `footnote14_dso_divergence_forensic_analyst::domain_heuristic_pipeline`.
3. Validate against matched benign twin `footnote14_dso_divergence_forensic_analyst::negative_trap_and_benign_twin_calibration`.
