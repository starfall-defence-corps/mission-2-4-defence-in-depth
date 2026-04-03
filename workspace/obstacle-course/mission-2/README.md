# Obstacle Course — Mission 2: Scheduled Drift Detection + Makefile

Write a scheduled GitHub Actions workflow for drift detection and a Makefile with pipeline stage targets.

## Your Task

### Part A: Makefile

Create a `Makefile` in this directory with these targets:

- `lint` — Run ansible-lint on the role
- `test` — Run Molecule test (converge + verify)
- `scan` — Run a security scan (Lynis audit on targets)

Each target should run the appropriate command. These are the local equivalents of your CI pipeline stages.

### Part B: Scheduled Workflow

Create `.github/workflows/drift-detection.yml` with:

1. **Trigger**: `schedule` with a weekly cron expression
2. **Job**: Run Molecule test against the fleet to detect configuration drift
3. **Notification step**: If drift is detected (tests fail), create a GitHub issue

## Requirements

- Makefile must have all 3 targets (lint, test, scan)
- Workflow must use `schedule` trigger
- Workflow must include failure notification (issue creation or similar)
