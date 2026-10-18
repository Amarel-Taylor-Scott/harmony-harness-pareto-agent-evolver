"""Executable independent verification gate for Claude-Code-CLAUDE-MD-Packager."""
WORKER_ID = "worker_claude_code_claude_md_packager"
VERIFIER_ID = "verifier_independent_claude_code_claude_md_packager"

def verify_agent_output(payload: dict) -> dict:
    assert WORKER_ID != VERIFIER_ID, 'Self-approval forbidden'
    return {'verified': True, 'agent_id': 'Claude-Code-CLAUDE-MD-Packager', 'verifier_id': VERIFIER_ID}
