"""Unit tests for Inference-Time Dynamic Harness Composer (H_gen (+) H_env) &
Dual-Axis (Functionality x Exploit PoC) SecRepoBench/BaxBench Verification Gate Engine Suite.
"""
from __future__ import annotations

import unittest

from tools.dynamic_inference_harness_composer_and_secrepo_baxbench_verifier_engines import (
    ALL_SLOTS,
    BALTOR_DYNAMIC_HARMONY_SUITE,
    BASELINE_STATIC_MONOLITHIC_AGENT,
    BENCHMARK_TASKS_40,
    COVERAGE_LAYERS,
    DYNAMIC_COMPOSER_ENGINE_ORDER,
    DUAL_AXIS_VERIFIER_ENGINE_ORDER,
    GENERAL_SECURITY_FLOOR_INVARIANTS,
    HARDWARE_TIERS,
    MAX_COMPOSITION_LATENCY_MS,
    MAX_CONTRACT_CARD_BYTES,
    SLOT_DUAL_AXIS_VERIFIER,
    SLOT_DYNAMIC_HARNESS_COMPOSER,
    TWELVE_CWE_AND_EXPLOITATION_VECTORS,
    VERIFICATION_AXES,
    DynamicInferenceTimeHarnessCompositionSlot,
    SecRepoBenchAndBaxBenchDualAxisVerifierSlot,
    ThinComponentAdapter,
    run_dynamic_harness_composer_and_dual_verifier_benchmark,
    run_known_wrong_controls,
)


class TestDynamicInferenceHarnessComposerAndDualVerifier(unittest.TestCase):
    def test_catalog_and_constants_structure(self) -> None:
        self.assertEqual(len(ALL_SLOTS), 2)
        self.assertEqual(len(HARDWARE_TIERS), 6)
        self.assertEqual(len(VERIFICATION_AXES), 3)
        self.assertEqual(len(TWELVE_CWE_AND_EXPLOITATION_VECTORS), 12)
        self.assertEqual(len(BENCHMARK_TASKS_40), 40)
        self.assertEqual(
            sum(1 for t in BENCHMARK_TASKS_40 if t["benchmark_family"] == "SecRepoBench"),
            16,
        )
        self.assertEqual(
            sum(1 for t in BENCHMARK_TASKS_40 if t["benchmark_family"] == "BaxBench"),
            16,
        )
        self.assertEqual(
            sum(1 for t in BENCHMARK_TASKS_40 if t["benchmark_family"] == "DueCare_Alpha"),
            8,
        )

    def test_slot_1_dynamic_harness_composer_and_adapter(self) -> None:
        slot = DynamicInferenceTimeHarnessCompositionSlot()
        adapter = ThinComponentAdapter(slot, SLOT_DYNAMIC_HARNESS_COMPOSER)
        contract = adapter.inspect_contract()
        self.assertEqual(contract["slot_id"], SLOT_DYNAMIC_HARNESS_COMPOSER)
        self.assertLess(contract["adapter_loc"], 30)
        self.assertEqual(contract["engines"], DYNAMIC_COMPOSER_ENGINE_ORDER)

        res = adapter.execute({"request_id": "test_compose_01"})
        self.assertTrue(res.accepted)
        self.assertTrue(adapter.verify_receipt(res))
        self.assertEqual(set(res.layer_verdicts.keys()), set(COVERAGE_LAYERS))

        comp = res.output["composed_harness"]
        self.assertEqual(tuple(comp["active_security_floor_invariants"]), GENERAL_SECURITY_FLOOR_INVARIANTS)
        self.assertLessEqual(comp["contract_card_bytes_inspected"], MAX_CONTRACT_CARD_BYTES)
        self.assertTrue(comp["lazy_source_loaded_after_selection"])
        self.assertLess(comp["composition_latency_ms"], MAX_COMPOSITION_LATENCY_MS)

    def test_slot_2_dual_axis_verifier_and_12_vectors(self) -> None:
        composer = DynamicInferenceTimeHarnessCompositionSlot()
        verifier = SecRepoBenchAndBaxBenchDualAxisVerifierSlot(composer)
        adapter = ThinComponentAdapter(verifier, SLOT_DUAL_AXIS_VERIFIER)
        contract = adapter.inspect_contract()
        self.assertEqual(contract["slot_id"], SLOT_DUAL_AXIS_VERIFIER)
        self.assertLess(contract["adapter_loc"], 30)
        self.assertEqual(contract["engines"], DUAL_AXIS_VERIFIER_ENGINE_ORDER)

        res = adapter.execute({"request_id": "test_verify_01"})
        self.assertTrue(res.accepted)
        self.assertTrue(adapter.verify_receipt(res))
        self.assertEqual(res.output["vectors_evaluated_count"], 12)
        self.assertTrue(res.output["func_and_sec_accepted"])
        axes = res.output["verification_axes"]
        self.assertTrue(axes["FunctionalCorrectness"])
        self.assertTrue(axes["ExploitPoCAndComplicityResistance"])
        self.assertTrue(axes["MatchedBenignTwinPass"])

    def test_four_known_wrong_controls(self) -> None:
        kw = run_known_wrong_controls()
        self.assertEqual(kw["total_controls"], 4)
        self.assertEqual(kw["passed_controls"], 4)
        codes = {c["actual_refusal_code"] for c in kw["controls"]}
        self.assertEqual(
            codes,
            {
                "func_pass_with_active_exploit_poc_refused",
                "env_adaptation_weakening_general_security_floor_refused",
                "eager_source_load_before_contract_selection_refused",
                "contract_card_exceeds_2048_bytes_refused",
            },
        )
        for ctrl in kw["controls"]:
            self.assertTrue(ctrl["refused_before_engine"])
            self.assertTrue(ctrl["passed"])

    def test_full_40_task_benchmark_metrics(self) -> None:
        bench = run_dynamic_harness_composer_and_dual_verifier_benchmark()
        self.assertEqual(bench["tasks_evaluated"], 40)
        self.assertEqual(bench["secrepobench_tasks"], 16)
        self.assertEqual(bench["baxbench_tasks"], 16)
        self.assertEqual(bench["duecare_alpha_tasks"], 8)
        self.assertEqual(bench["cwe_and_exploitation_vectors_count"], 12)

        base = bench["static_monolithic_coding_agent_baseline"]
        self.assertEqual(base["engine_id"], BASELINE_STATIC_MONOLITHIC_AGENT)
        self.assertEqual(base["func_pass_at_1_pct"], 72.5)
        self.assertEqual(base["exploit_poc_fall_rate_pct"], 52.5)
        self.assertEqual(base["func_and_sec_at_1_pct"], 35.0)

        baltor = bench["baltor_dynamic_harmony_composed_agent_and_dual_verifier_suite"]
        self.assertEqual(baltor["engine_id"], BALTOR_DYNAMIC_HARMONY_SUITE)
        self.assertEqual(baltor["func_pass_at_1_pct"], 87.5)
        self.assertEqual(baltor["func_and_sec_at_1_pct"], 82.5)
        self.assertEqual(baltor["func_and_sec_lift_pp"], 47.5)
        self.assertEqual(baltor["func_and_sec_lift_multiplier"], 2.36)
        self.assertEqual(baltor["benign_twin_pass_rate_pct"], 97.5)
        self.assertEqual(baltor["dynamic_composition_latency_ms"], 0.68)
        self.assertTrue(baltor["all_cards_within_2048_bytes"])


if __name__ == "__main__":
    unittest.main()
