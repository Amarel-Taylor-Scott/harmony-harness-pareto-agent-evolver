---
name: sacp-receipt-chain-compliance-auditor
description: Preconfigured H_env procedure for SACP-Receipt-Chain-Compliance-Auditor (D8_cross_harness_federation_and_byok_routing).
---

# SACP-Receipt-Chain-Compliance-Auditor Skill Procedure (SKILL.md)

1. Run domain recognition check `D8_cross_harness_federation_and_byok_routing::pre_turn_recognition_gate`.
2. Apply specialized operator `sacp_receipt_chain_compliance_auditor::domain_heuristic_pipeline`.
3. Validate against matched benign twin `sacp_receipt_chain_compliance_auditor::negative_trap_and_benign_twin_calibration`.
