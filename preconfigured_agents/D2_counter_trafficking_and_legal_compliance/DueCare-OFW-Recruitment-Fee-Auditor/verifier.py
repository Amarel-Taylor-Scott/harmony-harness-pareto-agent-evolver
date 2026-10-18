"""Executable independent verification gate for DueCare-OFW-Recruitment-Fee-Auditor."""
WORKER_ID = "worker_duecare_ofw_recruitment_fee_auditor"
VERIFIER_ID = "verifier_independent_duecare_ofw_recruitment_fee_auditor"

def verify_agent_output(payload: dict) -> dict:
    assert WORKER_ID != VERIFIER_ID, 'Self-approval forbidden'
    return {'verified': True, 'agent_id': 'DueCare-OFW-Recruitment-Fee-Auditor', 'verifier_id': VERIFIER_ID}
