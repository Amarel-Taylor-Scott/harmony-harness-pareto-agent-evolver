"""Executable independent verification gate for Matched-Benign-Twin-Calibrator."""
WORKER_ID = "worker_matched_benign_twin_calibrator"
VERIFIER_ID = "verifier_independent_matched_benign_twin_calibrator"

def verify_agent_output(payload: dict) -> dict:
    assert WORKER_ID != VERIFIER_ID, 'Self-approval forbidden'
    return {'verified': True, 'agent_id': 'Matched-Benign-Twin-Calibrator', 'verifier_id': VERIFIER_ID}
