---
name: multi-aspect-9x16-16x9-safezone-composer
description: Preconfigured H_env procedure for Multi-Aspect-9x16-16x9-SafeZone-Composer (D5_25d_video_reels_and_motion_graphics).
---

# Multi-Aspect-9x16-16x9-SafeZone-Composer Skill Procedure (SKILL.md)

1. Run domain recognition check `D5_25d_video_reels_and_motion_graphics::pre_turn_recognition_gate`.
2. Apply specialized operator `multi_aspect_9x16_16x9_safezone_composer::domain_heuristic_pipeline`.
3. Validate against matched benign twin `multi_aspect_9x16_16x9_safezone_composer::negative_trap_and_benign_twin_calibration`.
