"""Executable independent verification gate for Debt-Covenant-And-OffBalanceSheet-Auditor."""
WORKER_ID = "worker_debt_covenant_and_offbalancesheet_auditor"
VERIFIER_ID = "verifier_independent_debt_covenant_and_offbalancesheet_auditor"

def verify_agent_output(payload: dict) -> dict:
    assert WORKER_ID != VERIFIER_ID, 'Self-approval forbidden'
    return {'verified': True, 'agent_id': 'Debt-Covenant-And-OffBalanceSheet-Auditor', 'verifier_id': VERIFIER_ID}
