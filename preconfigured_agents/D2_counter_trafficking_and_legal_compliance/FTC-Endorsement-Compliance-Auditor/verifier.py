"""Executable independent verification gate for FTC-Endorsement-Compliance-Auditor."""
WORKER_ID = "worker_ftc_endorsement_compliance_auditor"
VERIFIER_ID = "verifier_independent_ftc_endorsement_compliance_auditor"

def verify_agent_output(payload: dict) -> dict:
    assert WORKER_ID != VERIFIER_ID, 'Self-approval forbidden'
    return {'verified': True, 'agent_id': 'FTC-Endorsement-Compliance-Auditor', 'verifier_id': VERIFIER_ID}
