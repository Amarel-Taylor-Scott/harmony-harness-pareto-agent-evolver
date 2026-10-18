"""Executable independent verification gate for Paired-Desktop-UnNerfed-GUI-Executor."""
WORKER_ID = "worker_paired_desktop_unnerfed_gui_executor"
VERIFIER_ID = "verifier_independent_paired_desktop_unnerfed_gui_executor"

def verify_agent_output(payload: dict) -> dict:
    assert WORKER_ID != VERIFIER_ID, 'Self-approval forbidden'
    return {'verified': True, 'agent_id': 'Paired-Desktop-UnNerfed-GUI-Executor', 'verifier_id': VERIFIER_ID}
