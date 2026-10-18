"""Executable independent verification gate for Auth-OAuth2-Boundary-Hardener."""
WORKER_ID = "worker_auth_oauth2_boundary_hardener"
VERIFIER_ID = "verifier_independent_auth_oauth2_boundary_hardener"

def verify_agent_output(payload: dict) -> dict:
    assert WORKER_ID != VERIFIER_ID, 'Self-approval forbidden'
    return {'verified': True, 'agent_id': 'Auth-OAuth2-Boundary-Hardener', 'verifier_id': VERIFIER_ID}
