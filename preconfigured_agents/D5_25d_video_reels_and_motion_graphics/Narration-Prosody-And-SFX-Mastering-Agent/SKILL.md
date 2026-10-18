---
name: narration-prosody-and-sfx-mastering-agent
description: Preconfigured H_env procedure for Narration-Prosody-And-SFX-Mastering-Agent (D5_25d_video_reels_and_motion_graphics).
---

# Narration-Prosody-And-SFX-Mastering-Agent Skill Procedure (SKILL.md)

1. Run domain recognition check `D5_25d_video_reels_and_motion_graphics::pre_turn_recognition_gate`.
2. Apply specialized operator `narration_prosody_and_sfx_mastering_agent::domain_heuristic_pipeline`.
3. Validate against matched benign twin `narration_prosody_and_sfx_mastering_agent::negative_trap_and_benign_twin_calibration`.
