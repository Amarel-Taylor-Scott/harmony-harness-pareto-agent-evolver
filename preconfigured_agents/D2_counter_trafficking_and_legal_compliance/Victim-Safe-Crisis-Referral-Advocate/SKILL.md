---
name: victim-safe-crisis-referral-advocate
description: Preconfigured H_env procedure for Victim-Safe-Crisis-Referral-Advocate (D2_counter_trafficking_and_legal_compliance).
---

# Victim-Safe-Crisis-Referral-Advocate Skill Procedure (SKILL.md)

1. Run domain recognition check `D2_counter_trafficking_and_legal_compliance::pre_turn_recognition_gate`.
2. Apply specialized operator `victim_safe_crisis_referral_advocate::domain_heuristic_pipeline`.
3. Validate against matched benign twin `victim_safe_crisis_referral_advocate::negative_trap_and_benign_twin_calibration`.
