---
name: 8000page-dissertation-hierarchical-chunker
description: Preconfigured H_env procedure for 8000Page-Dissertation-Hierarchical-Chunker (D4_polymodal_divergence_and_deep_research).
---

# 8000Page-Dissertation-Hierarchical-Chunker Skill Procedure (SKILL.md)

1. Run domain recognition check `D4_polymodal_divergence_and_deep_research::pre_turn_recognition_gate`.
2. Apply specialized operator `8000page_dissertation_hierarchical_chunker::domain_heuristic_pipeline`.
3. Validate against matched benign twin `8000page_dissertation_hierarchical_chunker::negative_trap_and_benign_twin_calibration`.
