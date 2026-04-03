.PHONY: help setup test reset destroy ssh-ubuntu ssh-rocky

help: ## Show available commands
	@echo ""
	@echo "  STARFALL DEFENCE CORPS — Mission 2.4"
	@echo "  The Automated Defence Line"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-14s\033[0m %s\n", $$1, $$2}'
	@echo ""

setup: ## Launch pipeline test targets (2 containers)
	@bash scripts/setup-lab.sh

test: ## Run ARIA verification
	@bash scripts/check-work.sh

reset: ## Destroy and rebuild all nodes
	@bash scripts/reset-lab.sh

destroy: ## Tear down everything
	@bash scripts/destroy-lab.sh

ssh-ubuntu: ## SSH into pipeline-ubuntu (port 2271)
	@ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null \
		-i .docker/ssh-keys/cadet_key cadet@localhost -p 2271

ssh-rocky: ## SSH into pipeline-rocky (port 2272)
	@ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null \
		-i .docker/ssh-keys/cadet_key cadet@localhost -p 2272
