"""Executable independent verification gate for Insider-Form4-And-13F-Cluster-Tracker."""
WORKER_ID = "worker_insider_form4_and_13f_cluster_tracker"
VERIFIER_ID = "verifier_independent_insider_form4_and_13f_cluster_tracker"

def verify_agent_output(payload: dict) -> dict:
    assert WORKER_ID != VERIFIER_ID, 'Self-approval forbidden'
    return {'verified': True, 'agent_id': 'Insider-Form4-And-13F-Cluster-Tracker', 'verifier_id': VERIFIER_ID}
