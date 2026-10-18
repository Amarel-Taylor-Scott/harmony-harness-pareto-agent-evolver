# Calibrated-Brier-Superforecaster-Agent — Claude Code Harness Instructions (CLAUDE.md)

1. Load `baltor_contract_card.json` first (`<= 2,048` bytes).
2. Enforce `RULES.md` pre-turn recognition gates before calling `mcp__calibrated_brier_superforecaster_agent__execute_task_step`.
3. Execute `python3 verifier.py` with independent `verifier_independent_calibrated_brier_superforecaster_agent` before completion.
