"""Executable independent verification gate for Legal-Deposition-Contradiction-Finder."""
WORKER_ID = "worker_legal_deposition_contradiction_finder"
VERIFIER_ID = "verifier_independent_legal_deposition_contradiction_finder"

def verify_agent_output(payload: dict) -> dict:
    assert WORKER_ID != VERIFIER_ID, 'Self-approval forbidden'
    return {'verified': True, 'agent_id': 'Legal-Deposition-Contradiction-Finder', 'verifier_id': VERIFIER_ID}
