# Harmony Harness Pareto Agent Evolver & 64 Preconfigured Task Agent Bundles

**Live Portals**:
- **Harmony Harness Portal**: [https://harmony.baltor.ai](https://harmony.baltor.ai)
- **64 Preconfigured Task Agents (`512` Verified Harness Component Files)**: [https://agents.baltor.ai](https://agents.baltor.ai)
- **GitHub Signals & Fast-Follow Repo Directory**: [https://signals.baltor.ai](https://signals.baltor.ai) | [https://repodir.baltor.ai](https://repodir.baltor.ai)
- **Monograph #13 (PDF)**: [https://papers.baltor.ai/Harmony_Harness_Pareto_Self_Evolution_and_64_Preconfigured_Task_Agents_2026.pdf](https://papers.baltor.ai/Harmony_Harness_Pareto_Self_Evolution_and_64_Preconfigured_Task_Agents_2026.pdf)

## Overview

Implementing and extending **Harmony Harness: Multi-Objective Self-Evolution of Agent Harnesses** (`arXiv:2610.15150v1`, Weichen Yu et al., Google Cloud AI Research / CMU / Google DeepMind, October 10, 2026) across the Baltor / Loop Engine ecosystem:

1. **Multi-Objective Pareto Frontier Evolution (`src/harmony_harness_pareto_self_evolution_and_factorized_operators_engines.py`)**:
   - Replaces scalar reward collapse with 3-axis Pareto dominance and `MOEA/D` Tchebycheff decomposition over `(FuncPass@1, SecurityPass@1, BenignTwinPrecision@1)`.
   - Factorizes every harness into transferable general mechanisms (`H_gen`) and environment/statutory adaptations (`H_env`): `H = H_gen (+) H_env`.
2. **64 Preconfigured Task-Specific Agent Bundles (`src/preconfigured_task_agent_harness_component_factory_engines.py`)**:
   - Compiles `64` task-specific agents (`8` domains x `8` agents) into `512` verified harness component files (`AGENTS.md`, `CLAUDE.md`, `SKILL.md`, `RULES.md`, `tools.json`, `context_pack.json`, `verifier.py`, `baltor_contract_card.json`).
   - All `64` complete 8-file agent bundles (`512` files) are materialized directly in [`preconfigured_agents/`](preconfigured_agents/).
3. **12-Subsystem Harness Component Yield Optimizer (`src/all_subsystem_harness_component_yield_optimizer_engines.py`)**:
   - Multiplies verified harness component yield across all 12 Baltor subsystems from `96` single-file artifacts (`1.0x`) to `692` Pareto-verified multi-file harness components (**`7.21x` yield lift**).
4. **Inference-Time Dynamic Composer & SecRepoBench/BaxBench Dual Verifier (`src/dynamic_inference_harness_composer_and_secrepo_baxbench_verifier_engines.py`)**:
   - Composes `H* = H_gen* (+) H_env*` in `0.68 ms` at inference time from `< 2,048`-byte contract cards and verifies both functional tests and exploit PoCs (`CWE-89`, `CWE-78`, `CWE-22`, `CWE-918`, `CWE-502`, `RA 10022`, `HK Cap. 163`).
