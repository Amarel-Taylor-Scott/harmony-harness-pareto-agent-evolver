---
name: research-paper-to-shortform-reel-agent
description: Preconfigured H_env procedure for Research-Paper-To-ShortForm-Reel-Agent (D5_25d_video_reels_and_motion_graphics).
---

# Research-Paper-To-ShortForm-Reel-Agent Skill Procedure (SKILL.md)

1. Run domain recognition check `D5_25d_video_reels_and_motion_graphics::pre_turn_recognition_gate`.
2. Apply specialized operator `research_paper_to_shortform_reel_agent::domain_heuristic_pipeline`.
3. Validate against matched benign twin `research_paper_to_shortform_reel_agent::negative_trap_and_benign_twin_calibration`.
