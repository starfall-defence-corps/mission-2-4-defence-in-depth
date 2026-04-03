# Mission 2.4: The Automated Defence Line — Checklist

## Obstacle Course Mission 1
- [ ] CI workflow exists at `.github/workflows/ci.yml`
- [ ] Workflow has lint job (ansible-lint)
- [ ] Workflow has test job (Molecule)
- [ ] Matrix strategy for multi-OS testing
- [ ] Test job depends on lint (needs)

## Obstacle Course Mission 2
- [ ] Makefile has lint, test, scan targets
- [ ] Drift detection workflow exists
- [ ] Drift workflow uses schedule trigger

## Main Mission
- [ ] CI workflow with lint + test stages
- [ ] Drift detection workflow with schedule
- [ ] .ansible-lint config
- [ ] Makefile with pipeline targets
- [ ] fleet_hardening role present
- [ ] PIPELINE.md documented (branch protection, drift detection)
- [ ] `make test` — all phases pass
