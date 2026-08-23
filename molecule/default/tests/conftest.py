"""
ARIA Custom Test Reporter
Provides color-coded, phase-grouped output for Pipeline verification.
"""
import os
import pytest
import sys

PHASES = {
    "TestObstacleCourse1":   ("1", "Obstacle Course — CI Workflow"),
    "TestObstacleCourse2":   ("2", "Obstacle Course — Pipeline Stages + Drift"),
    "TestMainMission":       ("3", "Main Mission — The Automated Defence Line"),
}

FRIENDLY = {
    "test_oc1_workflow_exists":        "CI workflow exists",
    "test_oc1_workflow_has_lint":      "Workflow has lint job",
    "test_oc1_workflow_has_test":      "Workflow has test job",
    "test_oc1_workflow_has_matrix":    "Workflow uses matrix strategy",
    "test_oc1_workflow_has_needs":     "Test job depends on lint",
    "test_oc2_makefile_exists":        "Makefile exists",
    "test_oc2_makefile_has_lint":      "Makefile has lint target",
    "test_oc2_makefile_has_test":      "Makefile has test target",
    "test_oc2_makefile_has_scan":      "Makefile has scan target",
    "test_oc2_drift_workflow_exists":  "Drift detection workflow exists",
    "test_oc2_drift_has_schedule":     "Drift workflow uses schedule trigger",
    "test_mm_ci_workflow_exists":      "CI workflow exists",
    "test_mm_ci_has_stages":           "CI has lint + test stages",
    "test_mm_drift_workflow_exists":   "Drift detection workflow exists",
    "test_mm_lint_config_exists":      ".ansible-lint config exists",
    "test_mm_makefile_exists":         "Makefile with pipeline targets",
    "test_mm_role_exists":             "fleet_hardening role exists",
    "test_mm_pipeline_doc_exists":     "PIPELINE.md documented",
}

# The phase-oriented summary is rendered by the shared `aria-reporter`
# pytest plugin (installed via requirements.txt); this file only declares
# the mission's phases + friendly objective names.
from aria_reporter import configure  # noqa: E402

configure(phases=PHASES, friendly=FRIENDLY, mission_id="2-4")
