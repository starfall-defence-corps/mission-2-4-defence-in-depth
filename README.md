# Starfall Defence Corps Academy

> 🧭 [← 2.3 Fleet Sync](https://github.com/starfall-defence-corps/mission-2-3-fleet-sync) · **You are here: 2.4 Defence in Depth** · [2.5 Noise Storm →](https://github.com/starfall-defence-corps/mission-2-5-noise-storm) · [🏠 Academy Hub](https://github.com/starfall-defence-corps/sdc-academy) · [📚 Field Manuals](https://github.com/starfall-defence-corps/sdc-academy/tree/main/field-manuals)

> ☁️ **No Docker on your machine?** Create your own copy first (Use this template), then on **your** repo: **Code → Codespaces → Create codespace** — everything is preinstalled. First boot takes ~5 min (one-time); after that it starts fast.

## Mission 2.4: Defence in Depth

> *"Reaver YOLO-Deploy is back. Last time they pushed untested code. Now you build the system that makes it impossible. The automated defence line."*

You are a Lieutenant at the Starfall Defence Corps Academy. You've hardened systems, tested them, measured compliance, and orchestrated fleet-wide deployments. Now build the CI/CD pipeline that enforces all of it automatically.

## Briefing

**Reaver YOLO-Deploy** has adapted since [Mission 2.1](https://github.com/starfall-defence-corps/mission-2-1-weapon-handling-test). The tests exist now, but nothing enforces them: "I'll run them later." "The tests are slow." "It's just a small change." This is your final confrontation with YOLO-Deploy, and the answer is the automated defence line — a CI/CD pipeline of gates between code and production:

```
Code → Lint → Test → Scan → [Review] → Deploy
  ↑                              ↑
  └── Reject if any gate fails ──┘
```

You build it twice: first in a timed obstacle course against a provided SSH hardening role, then as a complete pipeline for your own `fleet_hardening` role. Full orders, workflow examples and the stage definitions are in the [Mission Briefing](docs/BRIEFING.md).

**This mission grades what you author, not a live pipeline run.** `make test` checks your workflows, Makefiles, role and documentation structurally; it does not execute the pipeline. Lint is the one stage you can run for real in this lab (`ansible-lint` ships in the venv). Test (Molecule converge + verify) and Scan (a Testinfra security scan) are authored here and would run on CI runners that provision their own nodes.

## Objectives

`make test` verifies three phases:

| Phase | Part | ARIA checks |
|-------|------|-------------|
| 1 | Obstacle Course — Mission 1: *CI workflow* | `workspace/obstacle-course/mission-1/.github/workflows/ci.yml` exists and has a lint job, a test job, a `matrix` strategy, and `needs` so test depends on lint |
| 2 | Obstacle Course — Mission 2: *Makefile + drift detection* | `workspace/obstacle-course/mission-2/Makefile` has `lint:`, `test:` and `scan:` targets; `.github/workflows/drift-detection.yml` exists there and uses a `schedule` trigger |
| 3 | Main Mission: *Complete pipeline* | `workspace/main-mission/` contains `.github/workflows/ci.yml` with lint, test and scan stages, `.github/workflows/drift-detection.yml`, `.ansible-lint`, a `Makefile`, your `roles/fleet_hardening/`, and a `PIPELINE.md` that is filled in beyond the template |

## What You'll Learn

- GitHub Actions workflow structure: triggers, jobs, steps
- Ordering pipeline stages with `needs`, so a later gate only runs when the earlier one passes
- Matrix testing across OS families (Ubuntu and Rocky Linux)
- Scheduled workflows (`on: schedule` with cron) for weekly drift detection
- Raising a GitHub issue automatically when a scheduled check fails (`continue-on-error` + `if:` + `actions/github-script`)
- Configuring and running `ansible-lint` with a `.ansible-lint` file
- Writing a Makefile whose `lint`, `test` and `scan` targets mirror the CI stages
- Planning branch protection: required status checks and reviews

## Prerequisites

- Completed Module 1 (Missions 1.1–1.6 + Gateway Simulation)
- Completed Missions 2.1–2.3 — the main mission pipelines your `fleet_hardening` role
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (with Docker Compose v2)
- [GNU Make](https://www.gnu.org/software/make/)
- **Ansible**: provided by the lab — `make setup` builds a local venv with `ansible-core` and `ansible-lint`; no host install needed
- Python 3.10+ (with `python3-venv`)
- Git

> **Windows users**: Install [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install) and run all commands from within your WSL terminal.

## Quick Start

```bash
# 1. Use this template on GitHub (green button, top right) to create YOUR OWN
#    copy. Set it Public, then clone it:
git clone https://github.com/YOUR-USERNAME/mission-2-4-defence-in-depth.git
cd mission-2-4-defence-in-depth

# 2. Check your machine is mission-ready
make doctor

# 3. Launch the pipeline test targets (2 containers)
make setup

# 4. Activate the virtual environment
source venv/bin/activate
```

5. **Read your orders**: [Mission Briefing](docs/BRIEFING.md) — this mission has no separate exercises file; the phased walkthrough is in the briefing
6. **Stuck?** [Hints & Troubleshooting](docs/HINTS.md)
7. **Track progress**: [Checklist](CHECKLIST.md)
8. **Ready?** `make test`, then `make submit`

All your work goes in `workspace/`, but run `make test` and `make submit` from the **project root** (the folder with the `Makefile`).

## Lab Architecture

```
 Your Machine
+------------------------------------------------------------------+
|  workspace/                                                      |
|    obstacle-course/mission-1/                                    |
|      roles/ssh_hardening/      (provided)                        |
|      .ansible-lint             (provided)                        |
|      .github/workflows/ci.yml  (you write)                       |
|    obstacle-course/mission-2/                                    |
|      Makefile                  (you write)                       |
|      .github/workflows/drift-detection.yml  (you write)          |
|    main-mission/                                                 |
|      .github/workflows/ci.yml, drift-detection.yml  (you write)  |
|      .ansible-lint, Makefile, roles/fleet_hardening/ (you add)   |
|      PIPELINE.md               (template — you complete)         |
|                                                                  |
|  Pipeline test targets — Docker Network: 172.35.0.0/24           |
|  +-------------------------+                                     |
|  | pipeline-ubuntu  :2271  |  Ubuntu 22.04                       |
|  +-------------------------+                                     |
|  | pipeline-rocky   :2272  |  Rocky Linux 9                      |
|  +-------------------------+                                     |
+------------------------------------------------------------------+
```

The two containers are SSH targets for experimenting with your role; they are not wired into a local Molecule run, and your CI workflows do not use them. All nodes accept SSH as `cadet` with the key `make setup` generates.

The workflows you write live under `workspace/…/.github/workflows/`. GitHub only runs workflows from the repository's top-level `.github/workflows/`, so they are not triggered in this repo — they are graded as files.

## Mission Structure

| Part | Description | Location |
|------|-------------|----------|
| Obstacle Course 1 | Write a CI workflow (lint + matrix test) for a provided role | `workspace/obstacle-course/mission-1/` |
| Obstacle Course 2 | Write a Makefile (lint, test, scan) and a scheduled drift detection workflow | `workspace/obstacle-course/mission-2/` |
| Main Mission | Complete pipeline for `fleet_hardening`, plus `PIPELINE.md` | `workspace/main-mission/` |

Each part has its own `README.md` in the folder above with the exact requirements. Before Obstacle Course 2, copy `roles/` and `.ansible-lint` from `mission-1/` into `mission-2/`.

The obstacle course is timed (start before Mission 1, stop after Mission 2); the timer is yours to keep — `make test` grades correctness, not time:

| Time | Rating |
|------|--------|
| Under 30 min | Elite Ops |
| 30–40 min | Combat Ready |
| 40–55 min | Field Ready |
| 55–70 min | Basic |
| 70+ min | YOLO-Deploy Wins Again — retry |

## Available Commands

```
make help          Show available commands
make doctor        Check your machine is mission-ready (Docker, ports, tools)
make setup         Launch pipeline test targets (2 containers)
make test          Ask ARIA to verify your work
make submit        Submit your work for ARIA review (branch, commit, push, PR)
make reset         Destroy and rebuild all nodes
make destroy       Tear down everything
make ssh-ubuntu    SSH into pipeline-ubuntu (port 2271)
make ssh-rocky     SSH into pipeline-rocky (port 2272)
```

> **Note:** `make submit` uses the [GitHub CLI](https://cli.github.com/) — install `gh` and run `gh auth login` once before your first submission.

## Mission Files

| File | Purpose |
|------|---------|
| [BRIEFING.md](docs/BRIEFING.md) | Mission briefing, stage definitions, workflow and Makefile examples, deliverables — **read this first** |
| [HINTS.md](docs/HINTS.md) | Troubleshooting and hints |
| [CHECKLIST.md](CHECKLIST.md) | Progress tracker |
| [PIPELINE.md](workspace/main-mission/PIPELINE.md) | Your pipeline documentation and branch protection plan |

There is deliberately no `EXERCISES.md`: at Lieutenant rank the briefing carries the phased walkthrough.

## Checking Your Work: `make test`

`make test` runs ARIA's grader (`molecule/default/tests/test_pipeline.py`) and reports each objective, phase by phase. It inspects your files — it does not run your workflows or connect to the containers — so it is quick and safe to run as often as you like. It needs no API key and works offline.

While you work, lint for real from the venv, for example `ansible-lint -c .ansible-lint roles/` inside the folder you are linting. The mission is complete when all three phases are green.

## Submission and ARIA Review

When `make test` is green, `make submit` creates a `mission-submission` branch (or uses your current branch if you are not on `main`), commits `workspace/` and `CHECKLIST.md`, pushes, and opens a pull request to `main` in **your own** copy. You can also do this by hand with `git` and the GitHub web UI.

Opening or updating the pull request runs the **ARIA Review** workflow (`.github/workflows/aria-review.yml`). It does not re-run the grader — your local `make test` is the verdict. Instead, ARIA reads your submitted files, including `PIPELINE.md`, and posts a qualitative, in-character review of your pipeline design as a PR comment. Each new push updates the same comment.

To enable PR reviews, add an API key to your repo:
1. Get a key from [platform.claude.com](https://platform.claude.com/)
2. In your repo: **Settings** > **Secrets and variables** > **Actions** > **New repository secret**
3. Name: `ANTHROPIC_API_KEY`, Value: your key

Without a key, the comment says the review was skipped and the check still passes; `make test` works locally either way.

## Hints Policy

At Lieutenant rank you get a mission briefing and a pass/fail verdict, not a step-by-step guide. The briefing already contains working examples of each building block (workflow structure, matrix, schedule, failure notification, `.ansible-lint`, Makefile); assembling them into a pipeline is the mission. [HINTS.md](docs/HINTS.md) covers troubleshooting and the usual YAML and Makefile pitfalls. Read ARIA's messages in `make test` before reaching for the hints. For deeper reference, see [FM-3 — Molecule & Testing Reference](https://github.com/starfall-defence-corps/sdc-academy/blob/main/field-manuals/FM-3-molecule-testing-reference.md).

## Troubleshooting

**`ansible-lint` not found**: Activate the venv first: `source venv/bin/activate`.

**Makefile errors ("missing separator")**: Recipe lines must be indented with a tab, not spaces.

**Workflow YAML syntax**: Validate with `actionlint`, or paste into GitHub's workflow editor.

**`make test` fails with "No module named pytest"**: Run `make setup` first — it creates the Python virtual environment.

**Need a clean slate**: `make reset` destroys and rebuilds both containers; `make destroy` tears everything down.
