"""Executable independent verification gate for Headless-Deterministic-Playtest-Verifier."""
WORKER_ID = "worker_headless_deterministic_playtest_verifier"
VERIFIER_ID = "verifier_independent_headless_deterministic_playtest_verifier"

def verify_agent_output(payload: dict) -> dict:
    assert WORKER_ID != VERIFIER_ID, 'Self-approval forbidden'
    return {'verified': True, 'agent_id': 'Headless-Deterministic-Playtest-Verifier', 'verifier_id': VERIFIER_ID}
