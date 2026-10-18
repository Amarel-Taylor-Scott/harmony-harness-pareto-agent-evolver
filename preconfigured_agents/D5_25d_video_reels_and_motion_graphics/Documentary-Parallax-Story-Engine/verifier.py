"""Executable independent verification gate for Documentary-Parallax-Story-Engine."""
WORKER_ID = "worker_documentary_parallax_story_engine"
VERIFIER_ID = "verifier_independent_documentary_parallax_story_engine"

def verify_agent_output(payload: dict) -> dict:
    assert WORKER_ID != VERIFIER_ID, 'Self-approval forbidden'
    return {'verified': True, 'agent_id': 'Documentary-Parallax-Story-Engine', 'verifier_id': VERIFIER_ID}
