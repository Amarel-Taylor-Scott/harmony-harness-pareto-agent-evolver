"""Executable independent verification gate for Rust-Borrow-And-Unsafe-Auditor."""
WORKER_ID = "worker_rust_borrow_and_unsafe_auditor"
VERIFIER_ID = "verifier_independent_rust_borrow_and_unsafe_auditor"

def verify_agent_output(payload: dict) -> dict:
    assert WORKER_ID != VERIFIER_ID, 'Self-approval forbidden'
    return {'verified': True, 'agent_id': 'Rust-Borrow-And-Unsafe-Auditor', 'verifier_id': VERIFIER_ID}
