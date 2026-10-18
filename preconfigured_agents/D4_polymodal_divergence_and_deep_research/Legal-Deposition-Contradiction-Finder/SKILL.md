---
name: legal-deposition-contradiction-finder
description: Preconfigured H_env procedure for Legal-Deposition-Contradiction-Finder (D4_polymodal_divergence_and_deep_research).
---

# Legal-Deposition-Contradiction-Finder Skill Procedure (SKILL.md)

1. Run domain recognition check `D4_polymodal_divergence_and_deep_research::pre_turn_recognition_gate`.
2. Apply specialized operator `legal_deposition_contradiction_finder::domain_heuristic_pipeline`.
3. Validate against matched benign twin `legal_deposition_contradiction_finder::negative_trap_and_benign_twin_calibration`.
