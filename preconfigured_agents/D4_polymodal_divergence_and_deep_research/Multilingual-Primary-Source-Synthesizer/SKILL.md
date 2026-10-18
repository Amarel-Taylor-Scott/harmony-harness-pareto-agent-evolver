---
name: multilingual-primary-source-synthesizer
description: Preconfigured H_env procedure for Multilingual-Primary-Source-Synthesizer (D4_polymodal_divergence_and_deep_research).
---

# Multilingual-Primary-Source-Synthesizer Skill Procedure (SKILL.md)

1. Run domain recognition check `D4_polymodal_divergence_and_deep_research::pre_turn_recognition_gate`.
2. Apply specialized operator `multilingual_primary_source_synthesizer::domain_heuristic_pipeline`.
3. Validate against matched benign twin `multilingual_primary_source_synthesizer::negative_trap_and_benign_twin_calibration`.
