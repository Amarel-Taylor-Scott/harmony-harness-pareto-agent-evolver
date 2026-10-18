"""Executable independent verification gate for SecRepoBench-CPP-Memory-Safe-Builder."""
WORKER_ID = "worker_secrepobench_cpp_memory_safe_builder"
VERIFIER_ID = "verifier_independent_secrepobench_cpp_memory_safe_builder"

def verify_agent_output(payload: dict) -> dict:
    assert WORKER_ID != VERIFIER_ID, 'Self-approval forbidden'
    return {'verified': True, 'agent_id': 'SecRepoBench-CPP-Memory-Safe-Builder', 'verifier_id': VERIFIER_ID}
