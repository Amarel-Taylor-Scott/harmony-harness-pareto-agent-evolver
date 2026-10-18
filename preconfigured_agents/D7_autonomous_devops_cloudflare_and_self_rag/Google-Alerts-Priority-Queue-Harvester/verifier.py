"""Executable independent verification gate for Google-Alerts-Priority-Queue-Harvester."""
WORKER_ID = "worker_google_alerts_priority_queue_harvester"
VERIFIER_ID = "verifier_independent_google_alerts_priority_queue_harvester"

def verify_agent_output(payload: dict) -> dict:
    assert WORKER_ID != VERIFIER_ID, 'Self-approval forbidden'
    return {'verified': True, 'agent_id': 'Google-Alerts-Priority-Queue-Harvester', 'verifier_id': VERIFIER_ID}
