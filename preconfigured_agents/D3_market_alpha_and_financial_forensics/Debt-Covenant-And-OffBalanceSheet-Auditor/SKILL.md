---
name: debt-covenant-and-offbalancesheet-auditor
description: Preconfigured H_env procedure for Debt-Covenant-And-OffBalanceSheet-Auditor (D3_market_alpha_and_financial_forensics).
---

# Debt-Covenant-And-OffBalanceSheet-Auditor Skill Procedure (SKILL.md)

1. Run domain recognition check `D3_market_alpha_and_financial_forensics::pre_turn_recognition_gate`.
2. Apply specialized operator `debt_covenant_and_offbalancesheet_auditor::domain_heuristic_pipeline`.
3. Validate against matched benign twin `debt_covenant_and_offbalancesheet_auditor::negative_trap_and_benign_twin_calibration`.
