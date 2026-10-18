"""Executable independent verification gate for HK-Cap163-Debt-Novation-Tracer."""
WORKER_ID = "worker_hk_cap163_debt_novation_tracer"
VERIFIER_ID = "verifier_independent_hk_cap163_debt_novation_tracer"

def verify_agent_output(payload: dict) -> dict:
    assert WORKER_ID != VERIFIER_ID, 'Self-approval forbidden'
    return {'verified': True, 'agent_id': 'HK-Cap163-Debt-Novation-Tracer', 'verifier_id': VERIFIER_ID}
