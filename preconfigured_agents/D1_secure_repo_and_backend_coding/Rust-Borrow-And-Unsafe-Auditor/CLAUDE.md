# Rust-Borrow-And-Unsafe-Auditor — Claude Code Harness Instructions (CLAUDE.md)

1. Load `baltor_contract_card.json` first (`<= 2,048` bytes).
2. Enforce `RULES.md` pre-turn recognition gates before calling `mcp__rust_borrow_and_unsafe_auditor__execute_task_step`.
3. Execute `python3 verifier.py` with independent `verifier_independent_rust_borrow_and_unsafe_auditor` before completion.
