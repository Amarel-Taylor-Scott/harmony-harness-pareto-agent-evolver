---
name: consistent-2d-pan-zoom-colorpop-director
description: Preconfigured H_env procedure for Consistent-2D-Pan-Zoom-ColorPop-Director (D5_25d_video_reels_and_motion_graphics).
---

# Consistent-2D-Pan-Zoom-ColorPop-Director Skill Procedure (SKILL.md)

1. Run domain recognition check `D5_25d_video_reels_and_motion_graphics::pre_turn_recognition_gate`.
2. Apply specialized operator `consistent_2d_pan_zoom_colorpop_director::domain_heuristic_pipeline`.
3. Validate against matched benign twin `consistent_2d_pan_zoom_colorpop_director::negative_trap_and_benign_twin_calibration`.
