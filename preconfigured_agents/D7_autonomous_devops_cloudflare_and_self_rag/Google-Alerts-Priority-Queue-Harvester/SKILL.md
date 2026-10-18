---
name: google-alerts-priority-queue-harvester
description: Preconfigured H_env procedure for Google-Alerts-Priority-Queue-Harvester (D7_autonomous_devops_cloudflare_and_self_rag).
---

# Google-Alerts-Priority-Queue-Harvester Skill Procedure (SKILL.md)

1. Run domain recognition check `D7_autonomous_devops_cloudflare_and_self_rag::pre_turn_recognition_gate`.
2. Apply specialized operator `google_alerts_priority_queue_harvester::domain_heuristic_pipeline`.
3. Validate against matched benign twin `google_alerts_priority_queue_harvester::negative_trap_and_benign_twin_calibration`.
