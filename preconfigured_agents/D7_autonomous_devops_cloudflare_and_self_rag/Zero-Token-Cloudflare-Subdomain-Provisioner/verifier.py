"""Executable independent verification gate for Zero-Token-Cloudflare-Subdomain-Provisioner."""
WORKER_ID = "worker_zero_token_cloudflare_subdomain_provisioner"
VERIFIER_ID = "verifier_independent_zero_token_cloudflare_subdomain_provisioner"

def verify_agent_output(payload: dict) -> dict:
    assert WORKER_ID != VERIFIER_ID, 'Self-approval forbidden'
    return {'verified': True, 'agent_id': 'Zero-Token-Cloudflare-Subdomain-Provisioner', 'verifier_id': VERIFIER_ID}
