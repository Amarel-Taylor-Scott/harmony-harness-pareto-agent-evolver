---
name: ftc-endorsement-compliance-auditor
description: Preconfigured H_env procedure for FTC-Endorsement-Compliance-Auditor (D2_counter_trafficking_and_legal_compliance).
---

# FTC-Endorsement-Compliance-Auditor Skill Procedure (SKILL.md)

1. Run domain recognition check `D2_counter_trafficking_and_legal_compliance::pre_turn_recognition_gate`.
2. Apply specialized operator `ftc_endorsement_compliance_auditor::domain_heuristic_pipeline`.
3. Validate against matched benign twin `ftc_endorsement_compliance_auditor::negative_trap_and_benign_twin_calibration`.
