---
name: patent-claim-prior-art-deconstructor
description: Preconfigured H_env procedure for Patent-Claim-Prior-Art-Deconstructor (D4_polymodal_divergence_and_deep_research).
---

# Patent-Claim-Prior-Art-Deconstructor Skill Procedure (SKILL.md)

1. Run domain recognition check `D4_polymodal_divergence_and_deep_research::pre_turn_recognition_gate`.
2. Apply specialized operator `patent_claim_prior_art_deconstructor::domain_heuristic_pipeline`.
3. Validate against matched benign twin `patent_claim_prior_art_deconstructor::negative_trap_and_benign_twin_calibration`.
