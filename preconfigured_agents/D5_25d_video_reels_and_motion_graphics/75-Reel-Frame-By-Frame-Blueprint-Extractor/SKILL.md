---
name: 75-reel-frame-by-frame-blueprint-extractor
description: Preconfigured H_env procedure for 75-Reel-Frame-By-Frame-Blueprint-Extractor (D5_25d_video_reels_and_motion_graphics).
---

# 75-Reel-Frame-By-Frame-Blueprint-Extractor Skill Procedure (SKILL.md)

1. Run domain recognition check `D5_25d_video_reels_and_motion_graphics::pre_turn_recognition_gate`.
2. Apply specialized operator `75_reel_frame_by_frame_blueprint_extractor::domain_heuristic_pipeline`.
3. Validate against matched benign twin `75_reel_frame_by_frame_blueprint_extractor::negative_trap_and_benign_twin_calibration`.
