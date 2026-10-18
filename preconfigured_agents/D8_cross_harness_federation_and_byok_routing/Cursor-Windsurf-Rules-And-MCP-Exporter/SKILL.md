---
name: cursor-windsurf-rules-and-mcp-exporter
description: Preconfigured H_env procedure for Cursor-Windsurf-Rules-And-MCP-Exporter (D8_cross_harness_federation_and_byok_routing).
---

# Cursor-Windsurf-Rules-And-MCP-Exporter Skill Procedure (SKILL.md)

1. Run domain recognition check `D8_cross_harness_federation_and_byok_routing::pre_turn_recognition_gate`.
2. Apply specialized operator `cursor_windsurf_rules_and_mcp_exporter::domain_heuristic_pipeline`.
3. Validate against matched benign twin `cursor_windsurf_rules_and_mcp_exporter::negative_trap_and_benign_twin_calibration`.
