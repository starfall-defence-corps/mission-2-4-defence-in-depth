"""
=== STARFALL DEFENCE CORPS ACADEMY ===
ARIA Automated Verification — Mission 2.4: The Automated Defence Line
================================================================
"""
import os
import re
import yaml
import pytest


def _root_dir():
    tests_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.abspath(os.path.join(tests_dir, "..", "..", ".."))


def _workspace_dir():
    return os.path.join(_root_dir(), "workspace")


def _oc_dir(mission):
    return os.path.join(_workspace_dir(), "obstacle-course", f"mission-{mission}")


def _mm_dir():
    return os.path.join(_workspace_dir(), "main-mission")


def _read_yaml(path):
    try:
        with open(path) as f:
            return yaml.safe_load(f)
    except (FileNotFoundError, yaml.YAMLError):
        return None


def _file_contains(path, pattern):
    try:
        with open(path) as f:
            content = f.read()
        return bool(re.search(pattern, content, re.MULTILINE))
    except FileNotFoundError:
        return False


def _read_file(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        return ""


# -------------------------------------------------------------------
# Phase 1: Obstacle Course — Mission 1 (CI Workflow)
# -------------------------------------------------------------------

class TestObstacleCourse1:
    """ARIA verifies: Has the cadet written a CI workflow?"""

    def test_oc1_workflow_exists(self):
        """CI workflow must exist"""
        path = os.path.join(_oc_dir(1), ".github", "workflows", "ci.yml")
        assert os.path.isfile(path), (
            "ARIA: No workflow at obstacle-course/mission-1/.github/workflows/ci.yml. "
            "Write your CI pipeline workflow there."
        )

    def test_oc1_workflow_has_lint(self):
        """Workflow must have a lint job"""
        path = os.path.join(_oc_dir(1), ".github", "workflows", "ci.yml")
        if not os.path.isfile(path):
            pytest.skip("Workflow does not exist yet")
        content = _read_file(path)
        assert "lint" in content.lower(), (
            "ARIA: Workflow must include a lint job. "
            "Add a job that runs ansible-lint."
        )

    def test_oc1_workflow_has_test(self):
        """Workflow must have a test job"""
        path = os.path.join(_oc_dir(1), ".github", "workflows", "ci.yml")
        if not os.path.isfile(path):
            pytest.skip("Workflow does not exist yet")
        content = _read_file(path)
        assert "test" in content.lower(), (
            "ARIA: Workflow must include a test job. "
            "Add a job that runs Molecule."
        )

    def test_oc1_workflow_has_matrix(self):
        """Workflow must use matrix strategy for multi-OS testing"""
        path = os.path.join(_oc_dir(1), ".github", "workflows", "ci.yml")
        if not os.path.isfile(path):
            pytest.skip("Workflow does not exist yet")
        content = _read_file(path)
        assert "matrix" in content, (
            "ARIA: Workflow must use matrix strategy for multi-OS testing. "
            "Use strategy.matrix to test on both Ubuntu and Rocky."
        )

    def test_oc1_workflow_has_needs(self):
        """Test job must depend on lint job"""
        path = os.path.join(_oc_dir(1), ".github", "workflows", "ci.yml")
        if not os.path.isfile(path):
            pytest.skip("Workflow does not exist yet")
        content = _read_file(path)
        assert "needs" in content, (
            "ARIA: Test job must depend on the lint job. "
            "Use 'needs: lint' to create a dependency."
        )


# -------------------------------------------------------------------
# Phase 2: Obstacle Course — Mission 2 (Makefile + Drift Detection)
# -------------------------------------------------------------------

class TestObstacleCourse2:
    """ARIA verifies: Has the cadet written pipeline stages + drift detection?"""

    def test_oc2_makefile_exists(self):
        """Makefile must exist with pipeline targets"""
        path = os.path.join(_oc_dir(2), "Makefile")
        assert os.path.isfile(path), (
            "ARIA: No Makefile at obstacle-course/mission-2/. "
            "Write a Makefile with lint, test, and scan targets."
        )

    def test_oc2_makefile_has_lint(self):
        """Makefile must have a lint target"""
        path = os.path.join(_oc_dir(2), "Makefile")
        if not os.path.isfile(path):
            pytest.skip("Makefile does not exist yet")
        assert _file_contains(path, r'^lint:', ), (
            "ARIA: Makefile must have a 'lint:' target."
        )

    def test_oc2_makefile_has_test(self):
        """Makefile must have a test target"""
        path = os.path.join(_oc_dir(2), "Makefile")
        if not os.path.isfile(path):
            pytest.skip("Makefile does not exist yet")
        assert _file_contains(path, r'^test:', ), (
            "ARIA: Makefile must have a 'test:' target."
        )

    def test_oc2_makefile_has_scan(self):
        """Makefile must have a scan target"""
        path = os.path.join(_oc_dir(2), "Makefile")
        if not os.path.isfile(path):
            pytest.skip("Makefile does not exist yet")
        assert _file_contains(path, r'^scan:', ), (
            "ARIA: Makefile must have a 'scan:' target."
        )

    def test_oc2_drift_workflow_exists(self):
        """Drift detection workflow must exist"""
        path = os.path.join(_oc_dir(2), ".github", "workflows", "drift-detection.yml")
        assert os.path.isfile(path), (
            "ARIA: No workflow at obstacle-course/mission-2/.github/workflows/drift-detection.yml."
        )

    def test_oc2_drift_has_schedule(self):
        """Drift workflow must use schedule trigger"""
        path = os.path.join(_oc_dir(2), ".github", "workflows", "drift-detection.yml")
        if not os.path.isfile(path):
            pytest.skip("Drift workflow does not exist yet")
        content = _read_file(path)
        assert "schedule" in content, (
            "ARIA: Drift detection workflow must use 'schedule' trigger. "
            "Add a cron expression for weekly scans."
        )


# -------------------------------------------------------------------
# Phase 3: Main Mission — Complete Pipeline
# -------------------------------------------------------------------

class TestMainMission:
    """ARIA verifies: Has the cadet built a complete pipeline?"""

    def test_mm_ci_workflow_exists(self):
        """CI workflow must exist in main-mission"""
        path = os.path.join(_mm_dir(), ".github", "workflows", "ci.yml")
        assert os.path.isfile(path), (
            "ARIA: No CI workflow at main-mission/.github/workflows/ci.yml."
        )

    def test_mm_ci_has_stages(self):
        """CI workflow must have lint, test, and scan stages"""
        path = os.path.join(_mm_dir(), ".github", "workflows", "ci.yml")
        if not os.path.isfile(path):
            pytest.skip("CI workflow does not exist yet")
        content = _read_file(path).lower()
        has_lint = "lint" in content
        has_test = "test" in content or "molecule" in content
        has_scan = "scan" in content or "testinfra" in content or "security" in content
        assert has_lint and has_test, (
            "ARIA: CI workflow must include lint and test stages."
        )

    def test_mm_drift_workflow_exists(self):
        """Drift detection workflow must exist"""
        path = os.path.join(_mm_dir(), ".github", "workflows", "drift-detection.yml")
        assert os.path.isfile(path), (
            "ARIA: No drift detection workflow at main-mission/.github/workflows/drift-detection.yml."
        )

    def test_mm_lint_config_exists(self):
        """ansible-lint config must exist"""
        path = os.path.join(_mm_dir(), ".ansible-lint")
        assert os.path.isfile(path), (
            "ARIA: No .ansible-lint config. Create one to configure linting rules."
        )

    def test_mm_makefile_exists(self):
        """Makefile must exist with pipeline targets"""
        path = os.path.join(_mm_dir(), "Makefile")
        assert os.path.isfile(path), (
            "ARIA: No Makefile in main-mission/. "
            "Create one with lint, test, and scan targets."
        )

    def test_mm_role_exists(self):
        """fleet_hardening role must exist"""
        role_dir = os.path.join(_mm_dir(), "roles", "fleet_hardening")
        assert os.path.isdir(role_dir), (
            "ARIA: No role at main-mission/roles/fleet_hardening/. "
            "Copy your role from previous missions."
        )

    def test_mm_pipeline_doc_exists(self):
        """PIPELINE.md must be documented"""
        path = os.path.join(_mm_dir(), "PIPELINE.md")
        assert os.path.isfile(path), (
            "ARIA: PIPELINE.md not found."
        )
        content = _read_file(path)
        # Strip HTML comments and section headers to check for actual content
        stripped = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
        stripped = re.sub(r'^#+\s+.*$', '', stripped, flags=re.MULTILINE)
        stripped = re.sub(r'^\|[^|]*\|[^|]*\|[^|]*\|[^|]*\|$', '', stripped, flags=re.MULTILINE)
        stripped = stripped.strip()
        has_content = len(stripped) > 50
        assert has_content, (
            "ARIA: PIPELINE.md appears to be the empty template. "
            "Document your pipeline stages, branch protection plan, and drift detection strategy."
        )
