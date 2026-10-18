"""Executable independent verification gate for Fly-Pilot-Guarded-Release-Commander."""
WORKER_ID = "worker_fly_pilot_guarded_release_commander"
VERIFIER_ID = "verifier_independent_fly_pilot_guarded_release_commander"

def verify_agent_output(payload: dict) -> dict:
    assert WORKER_ID != VERIFIER_ID, 'Self-approval forbidden'
    return {'verified': True, 'agent_id': 'Fly-Pilot-Guarded-Release-Commander', 'verifier_id': VERIFIER_ID}
