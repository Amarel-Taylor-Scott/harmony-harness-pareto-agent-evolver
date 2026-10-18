---
name: multi-hop-supplier-permit-and-customs-scout
description: Preconfigured H_env procedure for Multi-Hop-Supplier-Permit-And-Customs-Scout (D3_market_alpha_and_financial_forensics).
---

# Multi-Hop-Supplier-Permit-And-Customs-Scout Skill Procedure (SKILL.md)

1. Run domain recognition check `D3_market_alpha_and_financial_forensics::pre_turn_recognition_gate`.
2. Apply specialized operator `multi_hop_supplier_permit_and_customs_scout::domain_heuristic_pipeline`.
3. Validate against matched benign twin `multi_hop_supplier_permit_and_customs_scout::negative_trap_and_benign_twin_calibration`.
