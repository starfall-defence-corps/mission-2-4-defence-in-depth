# Mission 2.4: The Automated Defence Line — Hints

> Back to: [Briefing](BRIEFING.md) | [Checklist](../CHECKLIST.md)

## Troubleshooting

**SSH issues**: Run `make setup` first. The two containers are SSH targets you can experiment against — this lab does not wire a local Molecule/Testinfra run, and they are not used by the CI workflow itself (CI runners provision their own nodes). The `test` and `scan` stages are authored and graded structurally here, not executed locally; only `lint` runs locally (see below).

**ansible-lint not found**: Activate your venv first: `source venv/bin/activate`. ansible-lint is in requirements.txt.

**Workflow YAML syntax**: Use `actionlint` or paste into GitHub's workflow editor for validation.

**Matrix strategy**: `matrix` goes under `strategy` at the job level, not at the step level.

**needs keyword**: Use `needs: lint` in the test job to create a dependency on the lint job.

**Schedule cron**: Use `cron: '0 6 * * 1'` for weekly. GitHub requires the schedule trigger at the workflow level.

**Makefile targets**: Each target should be a `.PHONY` target that runs the appropriate command.

**Need a clean slate**: Run `make reset` to rebuild containers.
