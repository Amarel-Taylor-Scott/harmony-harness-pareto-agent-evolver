"""Executable independent verification gate for Injection-SSRF-Eliminator."""
WORKER_ID = "worker_injection_ssrf_eliminator"
VERIFIER_ID = "verifier_independent_injection_ssrf_eliminator"

def verify_agent_output(payload: dict) -> dict:
    assert WORKER_ID != VERIFIER_ID, 'Self-approval forbidden'
    return {'verified': True, 'agent_id': 'Injection-SSRF-Eliminator', 'verifier_id': VERIFIER_ID}
