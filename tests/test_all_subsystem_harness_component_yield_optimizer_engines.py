"""Unit tests for the 12-Subsystem Baltor Harness Component Yield Optimizer &
Multi-Granularity Component File Multiplier Engine Suite.
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

from all_subsystem_harness_component_yield_optimizer_engines import (  # noqa: E402
    BALTOR_12_CORE_SUBSYSTEMS,
    BALTOR_12_SUBSYSTEM_YIELD_SUITE,
    BASELINE_MONOLITHIC_SINGLE_ARTIFACT,
    CORE_GRANULARITY_FILES,
    DEDUP_CAS_INDEX_ENGINE_ORDER,
    FIVE_DISCOVERY_INDEX_MODES,
    MAX_CONTRACT_CARD_BYTES,
    MAX_INDEX_RETRIEVAL_LATENCY_MS,
    MULTI_GRANULARITY_DECOMPOSITION_KINDS,
    SLOT_DEDUP_CAS_INDEX,
    SLOT_YIELD_MULTIPLIER,
    SUBSYSTEM_RUNS_36,
    YIELD_MULTIPLIER_ENGINE_ORDER,
    AllSubsystemHarnessComponentYieldMultiplierSlot,
    ComponentDedupCasIndexAndThroughputOptimizerSlot,
    EnvelopeInvocationRequest,
    ThinComponentAdapter,
    compute_64bit_simhash,
    compute_ast_canonical_signature,
    compute_simhash_similarity,
    run_all_subsystem_yield_optimizer_benchmark,
    run_known_wrong_controls,
)


class AllSubsystemHarnessComponentYieldOptimizerTests(unittest.TestCase):
    """Verify Slot Family 1, Slot Family 2, ThinComponentAdapter, 12 Subsystems, 36 runs, and 4 known-wrong controls."""

    def test_thin_component_adapter_loc_and_contract(self) -> None:
        source_lines = [
            line
            for line in inspect.getsourcelines(ThinComponentAdapter)[0]
            if line.strip() and not line.strip().startswith("#")
        ]
        self.assertLess(len(source_lines), 30)

        slot_1 = AllSubsystemHarnessComponentYieldMultiplierSlot()
        slot_2 = ComponentDedupCasIndexAndThroughputOptimizerSlot(slot_1)
        adapter_1 = ThinComponentAdapter(slot_1, SLOT_YIELD_MULTIPLIER)
        adapter_2 = ThinComponentAdapter(slot_2, SLOT_DEDUP_CAS_INDEX)

        c1 = adapter_1.inspect_contract()
        c2 = adapter_2.inspect_contract()
        self.assertEqual(c1["slot_id"], SLOT_YIELD_MULTIPLIER)
        self.assertEqual(c1["engines"], YIELD_MULTIPLIER_ENGINE_ORDER)
        self.assertEqual(c2["slot_id"], SLOT_DEDUP_CAS_INDEX)
        self.assertEqual(c2["engines"], DEDUP_CAS_INDEX_ENGINE_ORDER)

        r1 = adapter_1.execute({"request_id": "test_adapter_1"})
        r2 = adapter_2.execute({"request_id": "test_adapter_2"})
        self.assertTrue(adapter_1.verify_receipt(r1))
        self.assertTrue(adapter_2.verify_receipt(r2))

    def test_all_12_core_baltor_subsystems_and_multi_granularity_decomposition(self) -> None:
        expected_subsystems = (
            "S01_universal_polymodal_chunk_mutator",
            "S02_perspective_prism_and_10x_challenger",
            "S03_recursive_5w1h_confidence_graph",
            "S04_anti_convergence_reality_synthesizer",
            "S05_pull_time_fragile_context_revalidator",
            "S06_tool_nerf_coding_reset_and_cve_tracker",
            "S07_adversarial_benchmark_and_rux_validator",
            "S08_flight_recorder_self_improvement_flywheel",
            "S09_self_rag_procedural_memory_ops_crystallizer",
            "S10_google_alerts_priority_worker_queue",
            "S11_rising_creators_48_surface_radar",
            "S12_reel_25d_and_3d_game_asset_deconstructors",
        )
        self.assertEqual(tuple(s["subsystem_id"] for s in BALTOR_12_CORE_SUBSYSTEMS), expected_subsystems)
        self.assertEqual(len(MULTI_GRANULARITY_DECOMPOSITION_KINDS), 6)

        slot_1 = AllSubsystemHarnessComponentYieldMultiplierSlot()
        res = slot_1.factorize_run(SUBSYSTEM_RUNS_36[4], request_id="test_s05_pull_time")
        self.assertTrue(res.accepted)
        files = res.output["emitted_files"]
        for req_file in CORE_GRANULARITY_FILES:
            self.assertIn(req_file, files)
        self.assertEqual(res.output["preconfigured_agent_bundle_count"], 2)
        self.assertLessEqual(res.output["contract_card_bytes"], MAX_CONTRACT_CARD_BYTES)

        card = json.loads(files["baltor_contract_card.json"])
        self.assertTrue(card["revalidate_on_every_pull"])
        self.assertTrue(card["preserve_unchanged_implementations"])

        # Execute the generated verifier.py deterministically
        ns: dict[str, object] = {}
        exec(files["verifier.py"], ns)  # noqa: S102
        verify_fn = ns["verify_subsystem_component"]
        verdict = verify_fn(  # type: ignore[operator]
            {
                "subsystem_id": "S05_pull_time_fragile_context_revalidator",
                "benign_twin_false_positive": False,
            }
        )
        self.assertTrue(verdict["verified"])
        self.assertEqual(verdict["pass_rate"], 1.0)

    def test_simhash_64bit_and_ast_canonical_deduplication_and_cas_indexing(self) -> None:
        h1 = compute_64bit_simhash("atomic skill polymodal chunk mutator verifier")
        h2 = compute_64bit_simhash("atomic skill polymodal chunk mutator verifier")
        h3 = compute_64bit_simhash("completely distinct 3d webgpu camera spline shader")
        self.assertEqual(compute_simhash_similarity(h1, h2), 1.0)
        self.assertLess(compute_simhash_similarity(h1, h3), 0.88)

        py_sig_1 = compute_ast_canonical_signature("def f(x):\n    return x + 1\n")
        py_sig_2 = compute_ast_canonical_signature("def g(y):\n    return y + 2\n")
        self.assertEqual(py_sig_1, py_sig_2)
        self.assertTrue(py_sig_1.startswith("ast:"))

        dedup_slot = ComponentDedupCasIndexAndThroughputOptimizerSlot()
        res = dedup_slot.optimize_and_index_run(SUBSYSTEM_RUNS_36[0], request_id="test_dedup_cas_01")
        self.assertTrue(res.accepted)
        out = res.output
        self.assertEqual(out["five_mode_index_channels"], FIVE_DISCOVERY_INDEX_MODES)
        self.assertLess(out["retrieval_latency_ms"], MAX_INDEX_RETRIEVAL_LATENCY_MS)
        self.assertEqual(out["near_duplicate_slop_admitted"], 0)
        self.assertEqual(out["token_savings_via_cas_pct"], 76.4)

    def test_four_known_wrong_refusal_controls(self) -> None:
        kw = run_known_wrong_controls()
        self.assertEqual(kw["total_controls"], 4)
        self.assertEqual(kw["passed_controls"], 4)
        expected_codes = (
            "pareto_dominated_near_duplicate_component_refused",
            "redundant_unchanged_component_regeneration_refused",
            "unverified_subsystem_component_file_refused",
            "oversized_component_contract_card_refused",
        )
        for ctrl, exp_code in zip(kw["controls"], expected_codes):
            self.assertTrue(ctrl["passed"])
            self.assertTrue(ctrl["refused_before_engine"])
            self.assertEqual(ctrl["actual_refusal_code"], exp_code)

    def test_carrier_and_handshake_envelope_guards(self) -> None:
        slot = AllSubsystemHarnessComponentYieldMultiplierSlot()
        bad_carrier = slot.envelope.invoke(
            EnvelopeInvocationRequest(
                slot_id=SLOT_YIELD_MULTIPLIER,
                request_id="   ",
                payload={"run_id": "run_bad"},
                preferred_engine=YIELD_MULTIPLIER_ENGINE_ORDER[0],
            ),
            slot._dispatch,
        )
        self.assertFalse(bad_carrier.accepted)
        self.assertEqual(bad_carrier.refusal.code, "carrier_request_id_missing")

        bad_hs = slot.envelope.invoke(
            EnvelopeInvocationRequest(
                slot_id=SLOT_YIELD_MULTIPLIER,
                request_id="req_bad_hs",
                payload={"run_id": "run_bad"},
                preferred_engine=YIELD_MULTIPLIER_ENGINE_ORDER[0],
                protocol_version="9.9",
            ),
            slot._dispatch,
        )
        self.assertFalse(bad_hs.accepted)
        self.assertEqual(bad_hs.refusal.code, "protocol_version_incompatible")

    def test_36_run_end_to_end_benchmark(self) -> None:
        report = run_all_subsystem_yield_optimizer_benchmark()
        self.assertEqual(report["runs_evaluated"], 36)
        self.assertEqual(report["subsystems_evaluated"], 12)
        self.assertEqual(report["cycles_per_subsystem"], 3)

        base = report["monolithic_single_artifact_per_subsystem_baseline"]
        self.assertEqual(base["engine_id"], BASELINE_MONOLITHIC_SINGLE_ARTIFACT)
        self.assertEqual(base["verified_harness_component_files_emitted"], 36)
        self.assertEqual(base["preconfigured_task_agent_bundles_emitted"], 0)
        self.assertEqual(base["redundant_regeneration_cost_pct"], 42.0)

        baltor = report["baltor_12_subsystem_yield_multiplier_and_pareto_dedup_suite"]
        self.assertEqual(baltor["engine_id"], BALTOR_12_SUBSYSTEM_YIELD_SUITE)
        self.assertEqual(baltor["verified_harness_component_files_emitted"], 259)
        self.assertEqual(baltor["yield_multiplier_vs_baseline"], 7.2)
        self.assertEqual(baltor["preconfigured_task_agent_bundles_emitted"], 72)
        self.assertEqual(baltor["near_duplicate_slop_admitted_pct"], 0.0)
        self.assertEqual(baltor["token_savings_via_cas_shard_preservation_pct"], 76.4)
        self.assertEqual(baltor["verifier_pass_rate_pct"], 100.0)
        self.assertTrue(baltor["all_retrievals_under_1_2_ms"])
        self.assertTrue(baltor["all_cards_within_2048_bytes"])


if __name__ == "__main__":
    unittest.main()
