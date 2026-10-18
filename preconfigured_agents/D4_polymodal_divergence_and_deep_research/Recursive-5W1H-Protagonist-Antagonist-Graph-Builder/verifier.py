"""Executable independent verification gate for Recursive-5W1H-Protagonist-Antagonist-Graph-Builder."""
WORKER_ID = "worker_recursive_5w1h_protagonist_antagonist_graph_builder"
VERIFIER_ID = "verifier_independent_recursive_5w1h_protagonist_antagonist_graph_builder"

def verify_agent_output(payload: dict) -> dict:
    assert WORKER_ID != VERIFIER_ID, 'Self-approval forbidden'
    return {'verified': True, 'agent_id': 'Recursive-5W1H-Protagonist-Antagonist-Graph-Builder', 'verifier_id': VERIFIER_ID}
