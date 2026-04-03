# Obstacle Course — Mission 1: Write the CI Workflow

You have a role (`roles/ssh_hardening/`) that hardens SSH. Write a GitHub Actions workflow that automatically lints and tests it on every pull request.

## Your Task

Create `.github/workflows/ci.yml` in this directory with:

1. **Trigger**: on pull_request to main
2. **Lint stage**: Run `ansible-lint` on the role
3. **Test stage**: Run Molecule converge + Testinfra verify against both OS families
4. **Matrix strategy**: Test on Ubuntu and Rocky Linux

## Requirements

- Workflow must have at least 2 jobs (lint and test)
- Lint job uses `ansible-lint`
- Test job uses a matrix with 2 OS entries
- Test job depends on lint (runs only if lint passes)

## Provided Files

- `roles/ssh_hardening/` — A working SSH hardening role
- `.ansible-lint` — Lint configuration
