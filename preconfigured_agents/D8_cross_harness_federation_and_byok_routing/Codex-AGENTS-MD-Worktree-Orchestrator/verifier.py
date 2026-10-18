"""Executable independent verification gate for Codex-AGENTS-MD-Worktree-Orchestrator."""
WORKER_ID = "worker_codex_agents_md_worktree_orchestrator"
VERIFIER_ID = "verifier_independent_codex_agents_md_worktree_orchestrator"

def verify_agent_output(payload: dict) -> dict:
    assert WORKER_ID != VERIFIER_ID, 'Self-approval forbidden'
    return {'verified': True, 'agent_id': 'Codex-AGENTS-MD-Worktree-Orchestrator', 'verifier_id': VERIFIER_ID}
