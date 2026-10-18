# FTC-Endorsement-Compliance-Auditor — Claude Code Harness Instructions (CLAUDE.md)

1. Load `baltor_contract_card.json` first (`<= 2,048` bytes).
2. Enforce `RULES.md` pre-turn recognition gates before calling `mcp__ftc_endorsement_compliance_auditor__execute_task_step`.
3. Execute `python3 verifier.py` with independent `verifier_independent_ftc_endorsement_compliance_auditor` before completion.
