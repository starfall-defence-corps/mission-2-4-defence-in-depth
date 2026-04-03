---
CLASSIFICATION: LIEUTENANT EYES ONLY
MISSION: 2.4 — THE AUTOMATED DEFENCE LINE
THEATRE: Starfall Defence Corps Academy
AUTHORITY: SDC Cyber Command, 2187
---

# MISSION 2.4 — THE AUTOMATED DEFENCE LINE

---

## 1. SITUATION

### 1a. Enemy Forces

**Private YOLO-Deploy** is back. Last time, in Mission 2.1, YOLO-Deploy pushed untested code to production. Friday. 16:59. Three nodes down. You built tests to catch it.

But YOLO-Deploy adapted. Now they bypass the tests. "I'll run them later." "The tests are slow." "It's just a small change." The tests exist but nothing **enforces** them.

This is your final confrontation with YOLO-Deploy. You're not just writing tests — you're building the system that makes it **impossible** to deploy without them.

### 1b. The Automated Defence Line

A CI/CD pipeline is a series of automated gates between code and production:

```
Code → Lint → Test → Scan → [Review] → Deploy
  ↑                              ↑
  └── Reject if any gate fails ──┘
```

No human can skip a gate. No exception. No "I'll run it later." The pipeline runs on every PR, and the PR cannot merge until it passes.

### 1c. Pipeline Test Targets

| Designation | OS | SSH Port |
|-------------|----|----------|
| `pipeline-ubuntu` | Ubuntu 22.04 | 2271 |
| `pipeline-rocky` | Rocky Linux 9 | 2272 |

**SSH user**: `cadet` (key-based auth, key at `.ssh/cadet_key`)

---

## 2. MISSION

Build the automated defence line: CI pipeline, lint, matrix testing, drift detection.

### Phase 1: Obstacle Course (Timed)

> **START YOUR TIMER**

**Mission 1** (`obstacle-course/mission-1/`): Write a CI workflow for a provided SSH hardening role. Lint + matrix test across 2 OS families.

**Mission 2** (`obstacle-course/mission-2/`): Write a Makefile with pipeline stages (lint, test, scan) and a scheduled drift detection workflow.

> **STOP YOUR TIMER**

| Time | Rating |
|------|--------|
| Under 30 min | Elite Ops |
| 30–40 min | Combat Ready |
| 40–55 min | Field Ready |
| 55–70 min | Basic |
| 70+ min | YOLO-Deploy Wins Again — retry |

### Phase 2: Main Mission

Build a complete pipeline for your fleet_hardening role:
- CI workflow: lint → test → scan
- Drift detection: scheduled weekly scan
- Pipeline documentation: branch protection plan
- Local Makefile: run stages locally

---

## 3. KEY CONCEPTS

### GitHub Actions Workflow Structure

```yaml
name: CI Pipeline

on:
  pull_request:
    branches: [main]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install dependencies
        run: pip install ansible-core ansible-lint
      - name: Run ansible-lint
        run: ansible-lint roles/

  test:
    needs: lint    # Only runs if lint passes
    runs-on: ubuntu-latest
    strategy:
      matrix:
        os: [ubuntu, rocky]
    steps:
      - uses: actions/checkout@v4
      - name: Run Molecule
        run: molecule test
```

### Matrix Testing

```yaml
strategy:
  matrix:
    os: [ubuntu, rocky]
  fail-fast: false    # Don't cancel other matrix jobs on failure
```

### Scheduled Workflows

```yaml
on:
  schedule:
    - cron: '0 6 * * 1'    # Every Monday at 06:00 UTC
```

### ansible-lint

```bash
# Run lint
ansible-lint roles/fleet_hardening/

# With config file
ansible-lint -c .ansible-lint roles/
```

### Branch Protection (Manual Setup)

GitHub → Settings → Branches → Branch protection rules:
- Require status checks to pass before merging
- Require pull request reviews
- Require branches to be up to date

---

## 4. DELIVERABLES

### Obstacle Course

| File | Location |
|------|----------|
| CI workflow | `obstacle-course/mission-1/.github/workflows/ci.yml` |
| Makefile | `obstacle-course/mission-2/Makefile` |
| Drift workflow | `obstacle-course/mission-2/.github/workflows/drift-detection.yml` |

### Main Mission

| File | Location |
|------|----------|
| CI workflow | `main-mission/.github/workflows/ci.yml` |
| Drift workflow | `main-mission/.github/workflows/drift-detection.yml` |
| Lint config | `main-mission/.ansible-lint` |
| Makefile | `main-mission/Makefile` |
| Pipeline docs | `main-mission/PIPELINE.md` |
| Role | `main-mission/roles/fleet_hardening/` |

---

## 5. VERIFICATION

ARIA verifies three phases:
1. **Obstacle Course 1**: CI workflow exists, has lint + test jobs, uses matrix
2. **Obstacle Course 2**: Makefile has lint/test/scan targets, drift workflow uses schedule
3. **Main Mission**: Complete pipeline with all components, PIPELINE.md documented

Run `make test` to verify.

---

*SDC Cyber Command — 2187 — LIEUTENANT EYES ONLY*
