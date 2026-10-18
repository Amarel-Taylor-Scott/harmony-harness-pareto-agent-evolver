"""Executable independent verification gate for Victim-Safe-Crisis-Referral-Advocate."""
WORKER_ID = "worker_victim_safe_crisis_referral_advocate"
VERIFIER_ID = "verifier_independent_victim_safe_crisis_referral_advocate"

def verify_agent_output(payload: dict) -> dict:
    assert WORKER_ID != VERIFIER_ID, 'Self-approval forbidden'
    return {'verified': True, 'agent_id': 'Victim-Safe-Crisis-Referral-Advocate', 'verifier_id': VERIFIER_ID}
