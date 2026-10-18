"""Tests and known-wrong controls for the 64-Agent Preconfigured Task-Specific
Harness Component Factory & Cross-Harness 8-File Bundle Exporter Engine Suite.
"""
from __future__ import annotations

from pathlib import Path
import sys
import unittest

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
if str(HERE.parent / "src") not in sys.path:
    sys.path.insert(0, str(HERE.parent / "src"))

import preconfigured_task_agent_harness_component_factory_engines as af  # noqa: E402
from loop_engine.core.engines.envelope import COVERAGE_LAYERS, LAYER_REFUSED  # noqa: E402


class PreconfiguredTaskAgentHarnessComponentFactoryTests(unittest.TestCase):
    """Verify Slot Family 1, Slot Family 2, 64-scenario benchmark (512 files), and 4 known-wrong controls."""

    def test_slot1_blueprint_catalog_64_agents_across_8_domains_and_one_loop_runtime(self) -> None:
        contract = af.TASK_AGENT_BLUEPRINT_COMPILER_ADAPTER.inspect_contract()
        self.assertEqual(contract["slot_id"], af.SLOT_TASK_AGENT_BLUEPRINT_COMPILER)
        self.assertLess(int(contract["loc"]), 30)

        for idx, eng in enumerate(af.BLUEPRINT_COMPILER_ENGINE_ORDER):
            res = af.invoke_task_agent_blueprint_compiler_slot(
                {},
                request_id=f"test_slot1_eng_{idx}",
                preferred_engine=eng,
            )
            self.assertTrue(res.accepted)
            self.assertEqual(res.selected_engine, eng)
            self.assertTrue(af.TASK_AGENT_BLUEPRINT_COMPILER_ADAPTER.verify_receipt(res))
            out = res.output
            self.assertEqual(out["total_domains"], 8)
            self.assertEqual(out["total_agents_synthesized"], 64)
            self.assertEqual(out["expected_component_files_count"], 512)
            self.assertTrue(out["one_loop_runtime_preserved"])
            self.assertTrue(out["all_verifiers_independent"])
            for layer in COVERAGE_LAYERS:
                self.assertEqual(res.layer_verdicts[layer], "full")

            blueprints = out["blueprints"]
            self.assertEqual(len(blueprints), 64)
            for bp in blueprints:
                self.assertEqual(bp["runtime_vertex"], "Loop")
                self.assertNotEqual(bp["worker_id"], bp["verifier_id"])
                self.assertEqual(tuple(bp["required_files"]), af.REQUIRED_8_HARNESS_COMPONENT_FILES)

    def test_slot2_eight_file_bundle_materializer_512_files_and_cross_harness_exporter(self) -> None:
        contract = af.EIGHT_FILE_AGENT_BUNDLE_EXPORTER_ADAPTER.inspect_contract()
        self.assertEqual(contract["slot_id"], af.SLOT_EIGHT_FILE_AGENT_BUNDLE_EXPORTER)
        self.assertLess(int(contract["loc"]), 30)

        for idx, eng in enumerate(af.BUNDLE_EXPORTER_ENGINE_ORDER):
            res = af.invoke_eight_file_agent_bundle_exporter_slot(
                {},
                request_id=f"test_slot2_eng_{idx}",
                preferred_engine=eng,
            )
            self.assertTrue(res.accepted)
            self.assertEqual(res.selected_engine, eng)
            self.assertTrue(af.EIGHT_FILE_AGENT_BUNDLE_EXPORTER_ADAPTER.verify_receipt(res))
            out = res.output
            self.assertEqual(out["total_agent_bundles_emitted"], 64)
            self.assertEqual(out["total_harness_component_files_emitted"], 512)
            self.assertEqual(out["required_files_per_agent"], 8)
            self.assertTrue(out["all_contract_cards_within_2048_bytes"])
            self.assertLessEqual(int(out["max_contract_card_bytes"]), af.MAX_CONTRACT_CARD_BYTES)
            self.assertEqual(tuple(out["supported_target_harnesses"]), af.SUPPORTED_TARGET_HARNESSES)
            self.assertEqual(float(out["cross_harness_compatibility_pct"]), 100.0)

            sample_bundle = out["bundles"][0]
            self.assertEqual(sample_bundle["file_names"], af.REQUIRED_8_HARNESS_COMPONENT_FILES)
            self.assertIn("WORKER_ID != VERIFIER_ID", sample_bundle["files"]["verifier.py"])
            self.assertIn("bundle_manifest_sha256", sample_bundle["files"]["baltor_contract_card.json"])

    def test_64_scenario_benchmark_lift_and_token_reduction(self) -> None:
        bench = af.run_preconfigured_task_agent_factory_benchmark()
        self.assertEqual(bench["scenarios_evaluated"], 64)
        self.assertEqual(bench["domains_count"], 8)
        self.assertEqual(bench["total_agents"], 64)
        self.assertEqual(bench["total_verified_harness_component_files"], 512)

        base = bench["without_baltor_baseline"]
        self.assertEqual(base["engine_id"], af.BASELINE_UNCONFIGURED_GENERIC_PROMPT_AGENT)
        self.assertEqual(base["joint_functional_and_security_pass_rate_pct"], "46.9%")
        self.assertEqual(base["repeated_setup_tokens_per_session"], 14200)
        self.assertEqual(base["reusable_harness_component_files"], 0)

        suite = bench["with_baltor_64_agent_factory_suite"]
        self.assertEqual(suite["engine_id"], af.BALTOR_64_PRECONFIGURED_AGENT_BUNDLE_SUITE)
        self.assertEqual(suite["joint_functional_and_security_pass_rate_pct"], "95.3%")
        self.assertEqual(suite["pass_rate_lift_pp"], "+48.4 pp")
        self.assertEqual(suite["setup_token_reduction_pct"], "89.0%")
        self.assertEqual(suite["reusable_harness_component_files"], 512)
        self.assertEqual(suite["cross_harness_compatibility_pct"], "100.0%")
        self.assertTrue(suite["all_contract_cards_within_2048_bytes"])
        self.assertTrue(suite["one_loop_runtime_preserved"])

    def test_four_known_wrong_controls_refuse_at_preflight_layer(self) -> None:
        kw = af.run_known_wrong_controls()
        self.assertEqual(kw["total_controls"], 4)
        self.assertEqual(kw["passed_controls"], 4)
        for ctrl in kw["controls"]:
            self.assertTrue(ctrl["passed"], msg=f"Control failed: {ctrl}")
            self.assertTrue(ctrl["refused_before_engine"])

        # Direct verification of concrete Loop subclass refusal
        bad_subclass = af.invoke_task_agent_blueprint_compiler_slot(
            {"runtime_vertex": "CustomAgentNodeSubclass"},
            request_id="direct_subclass_probe",
        )
        self.assertFalse(bad_subclass.accepted)
        self.assertIsNotNone(bad_subclass.refusal)
        self.assertEqual(bad_subclass.refusal.code, "concrete_loop_subclass_for_agent_refused")
        self.assertEqual(bad_subclass.layer_verdicts["preflight"], LAYER_REFUSED)


if __name__ == "__main__":
    unittest.main()
