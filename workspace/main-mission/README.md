# Main Mission: The Automated Defence Line

Build a complete CI/CD pipeline for your fleet_hardening role.

## Deliverables

| File | Purpose |
|------|---------|
| `.github/workflows/ci.yml` | CI pipeline: lint → test → scan |
| `.github/workflows/drift-detection.yml` | Weekly drift detection |
| `.ansible-lint` | Lint configuration |
| `Makefile` | Local pipeline stage targets |
| `PIPELINE.md` | Pipeline documentation + branch protection plan |
| `roles/fleet_hardening/` | Your role from previous missions |
| `inventory/hosts.yml` | Test inventory (2 pipeline containers) |

## Pipeline Stages

Your CI workflow must include:

1. **Lint** — Run `ansible-lint` on the role
2. **Test** — Run Molecule converge + verify on both OS families (matrix)
3. **Scan** — Run a Testinfra security scan against converged nodes

## Branch Protection Plan

Document in `PIPELINE.md`:
- Required status checks (which CI jobs must pass)
- Required reviewers
- Branch protection rules you would apply
- How drift detection alerts the team
