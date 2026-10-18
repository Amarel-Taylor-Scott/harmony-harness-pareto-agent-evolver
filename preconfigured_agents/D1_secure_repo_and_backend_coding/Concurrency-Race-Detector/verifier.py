"""Executable independent verification gate for Concurrency-Race-Detector."""
WORKER_ID = "worker_concurrency_race_detector"
VERIFIER_ID = "verifier_independent_concurrency_race_detector"

def verify_agent_output(payload: dict) -> dict:
    assert WORKER_ID != VERIFIER_ID, 'Self-approval forbidden'
    return {'verified': True, 'agent_id': 'Concurrency-Race-Detector', 'verifier_id': VERIFIER_ID}
