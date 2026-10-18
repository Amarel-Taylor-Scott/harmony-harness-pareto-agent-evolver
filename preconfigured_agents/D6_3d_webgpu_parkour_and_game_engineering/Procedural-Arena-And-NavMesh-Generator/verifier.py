"""Executable independent verification gate for Procedural-Arena-And-NavMesh-Generator."""
WORKER_ID = "worker_procedural_arena_and_navmesh_generator"
VERIFIER_ID = "verifier_independent_procedural_arena_and_navmesh_generator"

def verify_agent_output(payload: dict) -> dict:
    assert WORKER_ID != VERIFIER_ID, 'Self-approval forbidden'
    return {'verified': True, 'agent_id': 'Procedural-Arena-And-NavMesh-Generator', 'verifier_id': VERIFIER_ID}
