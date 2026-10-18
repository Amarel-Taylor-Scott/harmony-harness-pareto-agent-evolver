---
name: flight-recorder-pii-safe-telemetry-miner
description: Preconfigured H_env procedure for Flight-Recorder-PII-Safe-Telemetry-Miner (D7_autonomous_devops_cloudflare_and_self_rag).
---

# Flight-Recorder-PII-Safe-Telemetry-Miner Skill Procedure (SKILL.md)

1. Run domain recognition check `D7_autonomous_devops_cloudflare_and_self_rag::pre_turn_recognition_gate`.
2. Apply specialized operator `flight_recorder_pii_safe_telemetry_miner::domain_heuristic_pipeline`.
3. Validate against matched benign twin `flight_recorder_pii_safe_telemetry_miner::negative_trap_and_benign_twin_calibration`.
