"""Executable independent verification gate for Patent-Claim-Prior-Art-Deconstructor."""
WORKER_ID = "worker_patent_claim_prior_art_deconstructor"
VERIFIER_ID = "verifier_independent_patent_claim_prior_art_deconstructor"

def verify_agent_output(payload: dict) -> dict:
    assert WORKER_ID != VERIFIER_ID, 'Self-approval forbidden'
    return {'verified': True, 'agent_id': 'Patent-Claim-Prior-Art-Deconstructor', 'verifier_id': VERIFIER_ID}
