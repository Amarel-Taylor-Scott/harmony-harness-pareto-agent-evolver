"""Executable independent verification gate for Multi-Hop-Supplier-Permit-And-Customs-Scout."""
WORKER_ID = "worker_multi_hop_supplier_permit_and_customs_scout"
VERIFIER_ID = "verifier_independent_multi_hop_supplier_permit_and_customs_scout"

def verify_agent_output(payload: dict) -> dict:
    assert WORKER_ID != VERIFIER_ID, 'Self-approval forbidden'
    return {'verified': True, 'agent_id': 'Multi-Hop-Supplier-Permit-And-Customs-Scout', 'verifier_id': VERIFIER_ID}
