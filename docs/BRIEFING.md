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
    # ┌─── minute (0-59)
    # │ ┌── hour (0-23)
    # │ │ ┌─ day of month (1-31)
    # │ │ │ ┌ month (1-12)
    # │ │ │ │ ┌ day of week (0-6, Mon=1)
    - cron: '0 6 * * 1'    # Every Monday at 06:00 UTC
```

### Failure Notification

When a scheduled workflow detects drift, notify the team by creating a GitHub issue:

```yaml
    - name: Run verification
      id: verify
      run: molecule verify
      continue-on-error: true

    - name: Create drift issue
      if: steps.verify.outcome == 'failure'
      uses: actions/github-script@v7
      with:
        script: |
          await github.rest.issues.create({
            owner: context.repo.owner,
            repo: context.repo.repo,
            title: 'Configuration Drift Detected',
            body: 'Weekly scan found drift. Investigate.',
            labels: ['drift']
          });
```

`continue-on-error: true` lets the workflow continue after failure so the notification step can run. The `if:` conditional checks the outcome of the previous step.

### ansible-lint

```bash
# Run lint
ansible-lint roles/fleet_hardening/

# With config file
ansible-lint -c .ansible-lint roles/
```

The `.ansible-lint` config file controls which rules to enforce:

```yaml
---
skip_list:     # Rules to completely ignore
  - yaml[truthy]
  - name[casing]
warn_list:     # Rules that warn but don't fail
  - experimental
```

Run `ansible-lint -L` to see all available rules.

### Writing a Makefile

A Makefile defines named targets that run shell commands. You've used `make setup` and `make test` in every mission — now you write your own.

```makefile
.PHONY: lint test scan

lint: ## Run ansible-lint
	ansible-lint -c .ansible-lint roles/

test: ## Run Molecule test
	molecule test

scan: ## Run security scan
	pytest tests/ --sudo -v
```

**Key rules**:
- Commands under a target must be indented with a **tab character**, not spaces. This is the most common Makefile error.
- `.PHONY` declares targets that don't produce files — all pipeline targets should be listed here.
- Add `## Description` after the target name — `make help` patterns can extract these.

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
| CI workflow | `workspace/obstacle-course/mission-1/.github/workflows/ci.yml` |
| Makefile | `workspace/obstacle-course/mission-2/Makefile` |
| Drift workflow | `workspace/obstacle-course/mission-2/.github/workflows/drift-detection.yml` |

### Main Mission

| File | Location |
|------|----------|
| CI workflow | `workspace/main-mission/.github/workflows/ci.yml` |
| Drift workflow | `workspace/main-mission/.github/workflows/drift-detection.yml` |
| Lint config | `workspace/main-mission/.ansible-lint` |
| Makefile | `workspace/main-mission/Makefile` |
| Pipeline docs | `workspace/main-mission/PIPELINE.md` |
| Role | `workspace/main-mission/roles/fleet_hardening/` |

---

## 5. VERIFICATION

ARIA verifies three phases:
1. **Obstacle Course 1**: CI workflow exists, has lint + test jobs, uses matrix
2. **Obstacle Course 2**: Makefile has lint/test/scan targets, drift workflow uses schedule
3. **Main Mission**: Complete pipeline with all components, PIPELINE.md documented

Run `make test` to verify.

---

---

## 6. GETTING STARTED

1. Activate your environment: `source venv/bin/activate`
2. All work goes in the `workspace/` directory — `cd workspace/`
3. Stuck? Consult [HINTS.md](HINTS.md)
4. Track your progress: [CHECKLIST.md](../CHECKLIST.md)

*SDC Cyber Command — 2187 — LIEUTENANT EYES ONLY*
