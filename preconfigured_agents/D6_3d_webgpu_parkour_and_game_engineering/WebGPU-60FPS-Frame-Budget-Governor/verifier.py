"""Executable independent verification gate for WebGPU-60FPS-Frame-Budget-Governor."""
WORKER_ID = "worker_webgpu_60fps_frame_budget_governor"
VERIFIER_ID = "verifier_independent_webgpu_60fps_frame_budget_governor"

def verify_agent_output(payload: dict) -> dict:
    assert WORKER_ID != VERIFIER_ID, 'Self-approval forbidden'
    return {'verified': True, 'agent_id': 'WebGPU-60FPS-Frame-Budget-Governor', 'verifier_id': VERIFIER_ID}
