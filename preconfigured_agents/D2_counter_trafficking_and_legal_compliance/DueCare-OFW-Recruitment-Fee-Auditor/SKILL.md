---
name: duecare-ofw-recruitment-fee-auditor
description: Preconfigured H_env procedure for DueCare-OFW-Recruitment-Fee-Auditor (D2_counter_trafficking_and_legal_compliance).
---

# DueCare-OFW-Recruitment-Fee-Auditor Skill Procedure (SKILL.md)

1. Run domain recognition check `D2_counter_trafficking_and_legal_compliance::pre_turn_recognition_gate`.
2. Apply specialized operator `duecare_ofw_recruitment_fee_auditor::domain_heuristic_pipeline`.
3. Validate against matched benign twin `duecare_ofw_recruitment_fee_auditor::negative_trap_and_benign_twin_calibration`.
