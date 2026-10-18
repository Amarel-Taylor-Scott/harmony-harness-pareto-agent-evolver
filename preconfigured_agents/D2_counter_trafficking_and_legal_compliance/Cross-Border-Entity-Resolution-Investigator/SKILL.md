---
name: cross-border-entity-resolution-investigator
description: Preconfigured H_env procedure for Cross-Border-Entity-Resolution-Investigator (D2_counter_trafficking_and_legal_compliance).
---

# Cross-Border-Entity-Resolution-Investigator Skill Procedure (SKILL.md)

1. Run domain recognition check `D2_counter_trafficking_and_legal_compliance::pre_turn_recognition_gate`.
2. Apply specialized operator `cross_border_entity_resolution_investigator::domain_heuristic_pipeline`.
3. Validate against matched benign twin `cross_border_entity_resolution_investigator::negative_trap_and_benign_twin_calibration`.
