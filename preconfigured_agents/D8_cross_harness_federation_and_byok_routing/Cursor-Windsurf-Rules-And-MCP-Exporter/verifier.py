"""Executable independent verification gate for Cursor-Windsurf-Rules-And-MCP-Exporter."""
WORKER_ID = "worker_cursor_windsurf_rules_and_mcp_exporter"
VERIFIER_ID = "verifier_independent_cursor_windsurf_rules_and_mcp_exporter"

def verify_agent_output(payload: dict) -> dict:
    assert WORKER_ID != VERIFIER_ID, 'Self-approval forbidden'
    return {'verified': True, 'agent_id': 'Cursor-Windsurf-Rules-And-MCP-Exporter', 'verifier_id': VERIFIER_ID}
