# Starfall Defence Corps Academy

## Mission 2.4: The Automated Defence Line

> *"Private YOLO-Deploy is back. Last time they pushed untested code. Now you build the system that makes it impossible. The automated defence line."*

You are a Lieutenant at the Starfall Defence Corps Academy. You've hardened systems, tested them, measured compliance, and orchestrated fleet-wide deployments. Now build the CI/CD pipeline that enforces all of it automatically.

## Prerequisites

- Completed Module 1 (Missions 1.1–1.5 + Gateway Simulation)
- Completed Missions 2.1–2.3
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (with Docker Compose v2)
- [GNU Make](https://www.gnu.org/software/make/)
- Python 3.10+ (with `python3-venv`)
- Git

> **Windows users**: Install [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install) and run all commands from within your WSL terminal.

## Quick Start

```bash
git clone https://github.com/YOUR-USERNAME/mission-2-4-defence-in-depth.git
cd mission-2-4-defence-in-depth
make setup
source venv/bin/activate
```

Read your orders: [Mission Briefing](docs/BRIEFING.md)

Stuck? [Hints](docs/HINTS.md) | Track progress: [Checklist](CHECKLIST.md)

## Lab Architecture

```
 Pipeline Test Targets
+-------------------------+
| pipeline-ubuntu  :2271  |
| Ubuntu 22.04            |
+-------------------------+
| pipeline-rocky   :2272  |
| Rocky Linux 9           |
+-------------------------+
```

## Mission Structure

| Part | Description | Location |
|------|-------------|----------|
| Obstacle Course 1 | Write CI workflow (lint + matrix test) | `workspace/obstacle-course/mission-1/` |
| Obstacle Course 2 | Write Makefile + drift detection | `workspace/obstacle-course/mission-2/` |
| Main Mission | Complete pipeline for fleet_hardening | `workspace/main-mission/` |

## Available Commands

```
make help          Show available commands
make setup         Launch pipeline test targets (2 containers)
make test          Ask ARIA to verify your work
make reset         Destroy and rebuild all nodes
make destroy       Tear down everything
make ssh-ubuntu    SSH into pipeline-ubuntu (port 2271)
make ssh-rocky     SSH into pipeline-rocky (port 2272)
```

## ARIA Review (Pull Request Workflow)

**Locally** — run `make test` for instant verification.

**On Pull Request** — push your work, open a PR, ARIA reviews automatically.

To enable PR reviews, add `ANTHROPIC_API_KEY` to your repo's Secrets.
