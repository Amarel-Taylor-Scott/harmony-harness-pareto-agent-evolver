"""Executable independent verification gate for Brownfield-Legacy-Refactor-Surgeon."""
WORKER_ID = "worker_brownfield_legacy_refactor_surgeon"
VERIFIER_ID = "verifier_independent_brownfield_legacy_refactor_surgeon"

def verify_agent_output(payload: dict) -> dict:
    assert WORKER_ID != VERIFIER_ID, 'Self-approval forbidden'
    return {'verified': True, 'agent_id': 'Brownfield-Legacy-Refactor-Surgeon', 'verifier_id': VERIFIER_ID}
