# EU-AI-Act-Safety-Dossier-Agent — Claude Code Harness Instructions (CLAUDE.md)

1. Load `baltor_contract_card.json` first (`<= 2,048` bytes).
2. Enforce `RULES.md` pre-turn recognition gates before calling `mcp__eu_ai_act_safety_dossier_agent__execute_task_step`.
3. Execute `python3 verifier.py` with independent `verifier_independent_eu_ai_act_safety_dossier_agent` before completion.
