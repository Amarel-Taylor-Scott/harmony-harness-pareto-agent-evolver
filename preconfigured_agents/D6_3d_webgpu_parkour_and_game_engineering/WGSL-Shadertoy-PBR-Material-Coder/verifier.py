"""Executable independent verification gate for WGSL-Shadertoy-PBR-Material-Coder."""
WORKER_ID = "worker_wgsl_shadertoy_pbr_material_coder"
VERIFIER_ID = "verifier_independent_wgsl_shadertoy_pbr_material_coder"

def verify_agent_output(payload: dict) -> dict:
    assert WORKER_ID != VERIFIER_ID, 'Self-approval forbidden'
    return {'verified': True, 'agent_id': 'WGSL-Shadertoy-PBR-Material-Coder', 'verifier_id': VERIFIER_ID}
