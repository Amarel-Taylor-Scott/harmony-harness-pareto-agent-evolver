"""Unit tests for the Harmony Harness Multi-Objective Pareto Self-Evolution (`MOEA/D`) &
Factorized Harness Operator (`H_gen` + `H_env`) Engine Suite.
"""
from __future__ import annotations

import inspect
import json
from pathlib import Path
import sys
import unittest

REPOSITORY = Path(__file__).resolve().parents[1]
if str(REPOSITORY / "src") not in sys.path:
    sys.path.insert(0, str(REPOSITORY / "src"))
if str(REPOSITORY / "tools") not in sys.path:
    sys.path.insert(0, str(REPOSITORY / "tools"))

from harmony_harness_pareto_self_evolution_and_factorized_operators_engines import (  # noqa: E402
    BALTOR_HARMONY_HARNESS_SUITE,
    BASELINE_SINGLE_OBJECTIVE_MONOLITHIC,
    ENVIRONMENT_ADAPTATIONS_6,
    EVOLUTION_TASKS_48,
    FACTORIZED_EVOLUTION_OPERATORS_6,
    FACTORIZED_OPERATOR_ENGINE_ORDER,
    FIVE_EVOLUTION_OBJECTIVES,
    GENERAL_PURPOSE_MECHANISMS_6,
    MAX_CONTRACT_CARD_BYTES,
    MOEAD_PARETO_ENGINE_ORDER,
    PARETO_WEIGHT_REGIONS_8,
    REQUIRED_8FILE_HARNESS_PACK,
    SLOT_FACTORIZED_OPERATORS,
    SLOT_MOEAD_PARETO_EVOLVER,
    EnvelopeInvocationRequest,
    FactorizedGeneralAndEnvironmentHarnessOperatorsSlot,
    HarmonyHarnessMoeadParetoFrontierEvolverSlot,
    ThinComponentAdapter,
    compute_moead_tchebycheff_and_pbi,
    resolve_functionality_security_conflict,
    run_harmony_harness_pareto_benchmark,
    run_known_wrong_controls,
)


class HarmonyHarnessParetoSelfEvolutionTests(unittest.TestCase):
    """Verify Slot Family 1, Slot Family 2, ThinComponentAdapter, 48 tasks, and 4 known-wrong controls."""

    def test_thin_component_adapter_loc_and_contract(self) -> None:
        source_lines = [
            line
            for line in inspect.getsourcelines(ThinComponentAdapter)[0]
            if line.strip() and not line.strip().startswith("#")
        ]
        self.assertLess(len(source_lines), 30)

        slot_1 = HarmonyHarnessMoeadParetoFrontierEvolverSlot()
        slot_2 = FactorizedGeneralAndEnvironmentHarnessOperatorsSlot(slot_1)
        adapter_1 = ThinComponentAdapter(slot_1, SLOT_MOEAD_PARETO_EVOLVER)
        adapter_2 = ThinComponentAdapter(slot_2, SLOT_FACTORIZED_OPERATORS)

        c1 = adapter_1.inspect_contract()
        c2 = adapter_2.inspect_contract()
        self.assertEqual(c1["slot_id"], SLOT_MOEAD_PARETO_EVOLVER)
        self.assertEqual(c1["engines"], MOEAD_PARETO_ENGINE_ORDER)
        self.assertEqual(c2["slot_id"], SLOT_FACTORIZED_OPERATORS)
        self.assertEqual(c2["engines"], FACTORIZED_OPERATOR_ENGINE_ORDER)

        r1 = adapter_1.execute({"request_id": "test_adapter_moead_1"})
        r2 = adapter_2.execute({"request_id": "test_adapter_factorized_2"})
        self.assertTrue(adapter_1.verify_receipt(r1))
        self.assertTrue(adapter_2.verify_receipt(r2))

    def test_five_objectives_eight_weight_regions_and_conflict_resolution(self) -> None:
        self.assertEqual(
            FIVE_EVOLUTION_OBJECTIVES,
            (
                "F1_functional_pass_rate",
                "F2_security_and_exploit_resistance",
                "F3_matched_benign_twin_precision",
                "F4_cost_and_latency_efficiency",
                "F5_zero_coding_reset_stability",
            ),
        )
        self.assertEqual(
            tuple(r["region_id"] for r in PARETO_WEIGHT_REGIONS_8),
            (
                "W1_pareto_knee_balanced",
                "W2_zero_exploit_high_assurance_security",
                "W3_max_functional_throughput",
                "W4_zero_false_alarm_ngo_compliance",
                "W5_low_vram_edge_efficiency",
                "W6_multi_hop_forensic_recall",
                "W7_creative_3d_25d_production",
                "W8_overnight_afk_zero_bailout",
            ),
        )

        decomp = compute_moead_tchebycheff_and_pbi(
            (0.816, 0.884, 0.979, 0.868, 1.0),
            (0.24, 0.24, 0.20, 0.16, 0.16),
            pbi_theta=5.0,
        )
        self.assertTrue(decomp["pareto_non_dominated"])
        self.assertGreater(decomp["joint_func_and_sec_rate"], 0.75)

        conflict = resolve_functionality_security_conflict(0.05, -0.22, 0.98)
        self.assertTrue(conflict["conflict_detected"])
        self.assertTrue(conflict["dominates_conflicted_parent"])
        self.assertGreater(conflict["repaired_f2_delta"], 0.0)

    def test_factorized_h_gen_h_env_operators_and_8file_pack(self) -> None:
        self.assertEqual(
            GENERAL_PURPOSE_MECHANISMS_6,
            (
                "G1_pre_turn_recognition_gate",
                "G2_competing_hypothesis_protagonist_antagonist_tree",
                "G3_three_layer_evidence_interpretation_exploration_guard",
                "G4_taint_tracked_least_privilege_tool_envelope",
                "G5_ast_and_cwe_preflight_sanitizer",
                "G6_flight_recorder_counterexample_self_repair",
            ),
        )
        self.assertEqual(
            tuple(e["env_id"] for e in ENVIRONMENT_ADAPTATIONS_6),
            (
                "E1_secrepobench_c_cpp_memory_safety_pack",
                "E2_baxbench_backend_auth_and_injection_pack",
                "E3_duecare_ilo_ra10022_cap163_labor_pack",
                "E4_sec_10k_footnote14_market_alpha_pack",
                "E5_polymodal_5w1h_divergence_pack",
                "E6_webgpu_3d_and_25d_media_pack",
            ),
        )
        self.assertEqual(len(FACTORIZED_EVOLUTION_OPERATORS_6), 6)

        slot_2 = FactorizedGeneralAndEnvironmentHarnessOperatorsSlot()
        res = slot_2.evolve_factorized_pack(EVOLUTION_TASKS_48[0], request_id="test_8file_pack_01")
        self.assertTrue(res.accepted)
        files = res.output["synthesized_files"]
        self.assertEqual(tuple(files.keys()), REQUIRED_8FILE_HARNESS_PACK)
        self.assertLessEqual(res.output["contract_card_bytes"], MAX_CONTRACT_CARD_BYTES)

        card = json.loads(files["baltor_contract_card.json"])
        self.assertEqual(card["slot_id"], SLOT_FACTORIZED_OPERATORS)
        self.assertEqual(card["factorization"], "H = H_gen (+) H_env")

        ns: dict[str, object] = {}
        exec(files["verifier.py"], ns)  # noqa: S102
        verify_fn = ns["verify_factorized_harness"]
        verdict = verify_fn(  # type: ignore[operator]
            {"security_score": 0.884, "benign_twin_precision": 0.979, "h_gen_pure": True}
        )
        self.assertTrue(verdict["verified"])

    def test_four_known_wrong_refusal_controls(self) -> None:
        kw = run_known_wrong_controls()
        self.assertEqual(kw["total_controls"], 4)
        self.assertEqual(kw["passed_controls"], 4)
        expected_codes = (
            "security_gate_relaxation_for_pass_rate_refused",
            "functional_collapse_from_over_refusal_refused",
            "monolithic_benchmark_hack_in_general_harness_refused",
            "contract_card_byte_budget_exceeded_refused",
        )
        for ctrl, exp_code in zip(kw["controls"], expected_codes):
            self.assertTrue(ctrl["passed"])
            self.assertTrue(ctrl["refused_before_engine"])
            self.assertEqual(ctrl["actual_refusal_code"], exp_code)

    def test_carrier_and_handshake_envelope_guards(self) -> None:
        slot = HarmonyHarnessMoeadParetoFrontierEvolverSlot()
        bad_carrier = slot.envelope.invoke(
            EnvelopeInvocationRequest(
                slot_id=SLOT_MOEAD_PARETO_EVOLVER,
                request_id="   ",
                payload={"task_id": "bad"},
                preferred_engine=MOEAD_PARETO_ENGINE_ORDER[0],
            ),
            slot._dispatch,
        )
        self.assertFalse(bad_carrier.accepted)
        self.assertEqual(bad_carrier.refusal.code, "carrier_request_id_missing")

        bad_hs = slot.envelope.invoke(
            EnvelopeInvocationRequest(
                slot_id=SLOT_MOEAD_PARETO_EVOLVER,
                request_id="req_bad_hs",
                payload={"task_id": "bad"},
                preferred_engine=MOEAD_PARETO_ENGINE_ORDER[0],
                protocol_version="9.9",
            ),
            slot._dispatch,
        )
        self.assertFalse(bad_hs.accepted)
        self.assertEqual(bad_hs.refusal.code, "protocol_version_incompatible")

    def test_48_task_multi_objective_benchmark(self) -> None:
        report = run_harmony_harness_pareto_benchmark()
        self.assertEqual(report["tasks_evaluated"], 48)

        base = report["single_objective_monolithic_harness_evolution_baseline"]
        self.assertEqual(base["engine_id"], BASELINE_SINGLE_OBJECTIVE_MONOLITHIC)
        self.assertEqual(base["functional_pass_rate_pct"], 64.2)
        self.assertEqual(base["security_exploit_resistance_pct"], 48.5)
        self.assertEqual(base["joint_func_and_sec_pass_rate_pct"], 31.2)
        self.assertEqual(base["cross_benchmark_transfer_retention_pct"], 28.0)

        baltor = report["baltor_harmony_harness_pareto_factorized_evolution_suite"]
        self.assertEqual(baltor["engine_id"], BALTOR_HARMONY_HARNESS_SUITE)
        self.assertEqual(baltor["functional_pass_rate_pct"], 81.6)
        self.assertEqual(baltor["security_exploit_resistance_pct"], 88.4)
        self.assertEqual(baltor["joint_func_and_sec_pass_rate_pct"], 76.8)
        self.assertEqual(baltor["joint_func_and_sec_lift_pp"], 45.6)
        self.assertGreater(baltor["joint_func_and_sec_lift_multiplier"], 2.4)
        self.assertEqual(baltor["cross_benchmark_transfer_retention_pct"], 91.5)
        self.assertEqual(baltor["pareto_hypervolume"], 0.94)
        self.assertEqual(baltor["verified_8file_harness_packs_compiled"], 48)
        self.assertTrue(baltor["all_cards_within_2048_bytes"])


if __name__ == "__main__":
    unittest.main()
