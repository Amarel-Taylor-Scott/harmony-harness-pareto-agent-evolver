---
name: insider-form4-and-13f-cluster-tracker
description: Preconfigured H_env procedure for Insider-Form4-And-13F-Cluster-Tracker (D3_market_alpha_and_financial_forensics).
---

# Insider-Form4-And-13F-Cluster-Tracker Skill Procedure (SKILL.md)

1. Run domain recognition check `D3_market_alpha_and_financial_forensics::pre_turn_recognition_gate`.
2. Apply specialized operator `insider_form4_and_13f_cluster_tracker::domain_heuristic_pipeline`.
3. Validate against matched benign twin `insider_form4_and_13f_cluster_tracker::negative_trap_and_benign_twin_calibration`.
