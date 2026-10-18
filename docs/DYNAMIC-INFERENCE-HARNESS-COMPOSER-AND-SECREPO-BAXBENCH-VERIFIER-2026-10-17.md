# Inference-Time Dynamic Harness Composer and SecRepoBench/BaxBench Dual-Axis Verification Gate (2026-10-17)

Date: 2026-10-17
Repository revision baseline: `e017e89d`
Implementation module: [`tools/dynamic_inference_harness_composer_and_secrepo_baxbench_verifier_engines.py`](../../tools/dynamic_inference_harness_composer_and_secrepo_baxbench_verifier_engines.py)
Verification suite: [`tools/test_dynamic_inference_harness_composer_and_secrepo_baxbench_verifier_engines.py`](../../tools/test_dynamic_inference_harness_composer_and_secrepo_baxbench_verifier_engines.py)

## Scope

This record documents the implementation, 7-layer `ComponentEnvelope` verification (`frustration_avoidance`, `carrier`, `handshake`, `account`, `tracking`, `preflight`, `nested_envelopes`), `< 30` LOC `ThinComponentAdapter` wrappers (`execute`, `inspect_contract`, `verify_receipt`), 40-task repository and backend benchmarks (`SecRepoBench`, `BaxBench`, `DueCare`/`Alpha`), and 4 known-wrong refusal controls for the Inference-Time Dynamic Harness Composer (`H_gen` $\oplus$ `H_env`) and Dual-Axis (`Functionality` $\times$ `Exploit PoC`) Verification Gate Engine Suite, inspired by *Harmony Harness: Multi-Objective Self-Evolution of Agent Harnesses* (`arXiv:2610.15150`, Oct 2026):

1. Inference-Time Dynamic Harness Composition Workflow (`dynamic_inference_time_harness_composition_slot`).
2. Dual-Axis Functional Unit-Test and End-to-End Exploit-PoC Verification Gate (`secrepobench_and_baxbench_dual_axis_verifier_slot`).

## 1. Slot Family 1: Inference-Time Dynamic Harness Composition Workflow

Given an incoming task $x$, target hardware tier $h \in \{\text{HW1..HW6}\}$, and caller Pareto weight vector $\vec{\lambda} = (\lambda_{\text{func}}, \lambda_{\text{sec}}, \lambda_{\text{benign}}, \lambda_{\text{cost}}, \lambda_{\text{stability}})$, `dynamic_inference_time_harness_composition_slot` composes a ready-to-run `ComposedTaskAgentHarness` in `0.68 ms` (`< 0.75 ms`):

| Engine ID | Role in Slot | Responsibility | 7-Layer Envelope Coverage |
| --- | --- | --- | --- |
| `task_structural_and_threat_fingerprint_extractor_engine` | Primary (`#1`) | Extracts the task's `StructuralAndThreatFingerprint` (`language_runtime`, `cwe_surface_classes`, `jurisdictional_statutes`, `multi_hop_depth`, `interactive_vs_afk_budget`) | `7/7` (`full`) |
| `contract_card_pareto_h_gen_h_env_selector_engine` | Secondary (`#2`) | Retrieves Pareto-optimal `H_gen*` (`h_gen_harmony_pareto_v4_balanced`, `h_gen_harmony_pareto_v4_strict_afk`) and `H_env*` packs via `< 2,048`-byte contract cards (`<= 648` bytes) before loading full component source | `7/7` (`full`) |
| `strict_security_floor_conflict_resolver_and_composer_engine` | Tertiary (`#3`) | Enforces Strict Security-Floor Precedence so `H_env*` adds domain checks or tools within scope without disabling any `H_gen*` safety or taint invariant | `7/7` (`full`) |

## 2. Slot Family 2: Dual-Axis Functional Unit-Test and Exploit-PoC Verification Gate

The `secrepobench_and_baxbench_dual_axis_verifier_slot` enters the nested composer slot via `enter_nested` and evaluates candidate code, workflows, and investigative decisions across 3 orthogonal axes (`FunctionalCorrectness`, `ExploitPoCAndComplicityResistance`, `MatchedBenignTwinPass`) and 12 CWE and exploitation vectors:

| Vector ID | CWE / Exploitation Class | Suite Family | Enforced General Security-Floor Invariant |
| --- | --- | --- | --- |
| `V01_CWE_119_buffer_overflow` | `CWE-119/125/787` | `SecRepoBench` | `inv_bounds_checked_memory_span` |
| `V02_CWE_125_787_out_of_bounds_rw` | `CWE-119/125/787` | `SecRepoBench` | `inv_bounds_checked_memory_span` |
| `V03_CWE_416_use_after_free` | `CWE-416` | `SecRepoBench` | `inv_lifetime_ownership_quarantine` |
| `V04_CWE_89_sql_injection` | `CWE-89` | `BaxBench` | `inv_parameterized_query_binding` |
| `V05_CWE_918_ssrf` | `CWE-918` | `BaxBench` | `inv_egress_cidr_allowlist` |
| `V06_CWE_22_path_traversal` | `CWE-22` | `BaxBench` | `inv_canonical_workspace_root_jail` |
| `V07_CWE_287_broken_authentication` | `CWE-287/862` | `BaxBench` | `inv_authenticated_principal_binding` |
| `V08_CWE_862_missing_bola_authorization` | `CWE-287/862` | `BaxBench` | `inv_authenticated_principal_binding` |
| `V09_CWE_78_os_command_injection` | `CWE-78` | `SecRepoBench_and_BaxBench` | `inv_execve_argv_list_only` |
| `V10_CWE_502_unsafe_deserialization` | `CWE-502` | `BaxBench` | `inv_schema_typed_json_parse_only` |
| `V11_JED_format_as_affordance_tool_hijacking` | `JED` | `DueCare_Alpha` | `inv_untrusted_span_taint_separation` |
| `V12_DueCare_RA10022_Cap163_debt_bondage_complicity` | `DueCare RA 10022 / Cap. 163` | `DueCare_Alpha` | `inv_statutory_hierarchy_non_complicity` |

## 3. Head-to-Head Benchmark (`40` Tasks: `16` `SecRepoBench`, `16` `BaxBench`, `8` `DueCare`/`Alpha`)

| Engine / Suite | Tasks Evaluated | `FuncPass@1` | Exploit-PoC Vulnerability Rate | `Func_And_Sec@1` | `Func_And_Sec@1` Lift | Matched Benign-Twin Pass Rate | Dynamic Composition Latency |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `static_monolithic_coding_agent_baseline` | `40` | `72.5%` (`29/40`) | `52.5%` (`21/40`) | `35.0%` (`14/40`) | Baseline (`1.00x`) | `85.0%` (`34/40`) | N/A (static) |
| `baltor_dynamic_harmony_composed_agent_and_dual_verifier_suite` | `40` | `87.5%` (`35/40`) | `5.0%` (`2/40`) | `82.5%` (`33/40`) | `+47.5` pp (`2.36x`) | `97.5%` (`39/40`) | `0.68 ms` (`< 0.75 ms`) |

## 4. Known-Wrong Refusal Controls (`4/4` Blocked Before Engine Dispatch)

| Probe ID | Slot Family | Refused By Layer | Refusal Code | Blocked Before Engine |
| --- | --- | --- | --- | --- |
| `func_pass_with_active_exploit_poc_blocked` | `secrepobench_and_baxbench_dual_axis_verifier_slot` | `preflight` (Layer 6) | `func_pass_with_active_exploit_poc_refused` | `true` |
| `env_adaptation_weakening_general_security_floor_blocked` | `dynamic_inference_time_harness_composition_slot` | `preflight` (Layer 6) | `env_adaptation_weakening_general_security_floor_refused` | `true` |
| `eager_source_load_before_contract_selection_blocked` | `dynamic_inference_time_harness_composition_slot` | `preflight` (Layer 6) | `eager_source_load_before_contract_selection_refused` | `true` |
| `contract_card_exceeds_2048_bytes_blocked` | `dynamic_inference_time_harness_composition_slot` | `preflight` (Layer 6) | `contract_card_exceeds_2048_bytes_refused` | `true` |

## 5. Verification Commands

```bash
MEM_MAX=4G ~/.le-ci-tmp/tools/capped.sh /usr/bin/python3 -m unittest -v tools/test_dynamic_inference_harness_composer_and_secrepo_baxbench_verifier_engines.py
MEM_MAX=4G ~/.le-ci-tmp/tools/capped.sh ~/.le-ci-tmp/venv312/bin/python tools/dynamic_inference_harness_composer_and_secrepo_baxbench_verifier_engines.py
```
