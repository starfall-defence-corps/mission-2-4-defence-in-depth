# Mission 2.4: The Automated Defence Line — Hints

## Troubleshooting

**SSH issues**: Run `make setup` first. Containers are for local testing, not for the CI workflow itself.

**ansible-lint not found**: Activate your venv first: `source venv/bin/activate`. ansible-lint is in requirements.txt.

**Workflow YAML syntax**: Use `actionlint` or paste into GitHub's workflow editor for validation.

**Matrix strategy**: `matrix` goes under `strategy` at the job level, not at the step level.

**needs keyword**: Use `needs: lint` in the test job to create a dependency on the lint job.

**Schedule cron**: Use `cron: '0 6 * * 1'` for weekly. GitHub requires the schedule trigger at the workflow level.

**Makefile targets**: Each target should be a `.PHONY` target that runs the appropriate command.

**Need a clean slate**: Run `make reset` to rebuild containers.
