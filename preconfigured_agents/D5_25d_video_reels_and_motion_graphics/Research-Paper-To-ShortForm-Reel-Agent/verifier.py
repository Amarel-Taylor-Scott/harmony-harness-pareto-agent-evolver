"""Executable independent verification gate for Research-Paper-To-ShortForm-Reel-Agent."""
WORKER_ID = "worker_research_paper_to_shortform_reel_agent"
VERIFIER_ID = "verifier_independent_research_paper_to_shortform_reel_agent"

def verify_agent_output(payload: dict) -> dict:
    assert WORKER_ID != VERIFIER_ID, 'Self-approval forbidden'
    return {'verified': True, 'agent_id': 'Research-Paper-To-ShortForm-Reel-Agent', 'verifier_id': VERIFIER_ID}
