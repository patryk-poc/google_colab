# import config.
# You can change the default config with `make conf="config_special.env" build`
SHELL := /bin/bash

.PHONY: help test

.DEFAULT_GOAL := help

help:
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

test: ## Run tests with pytest
	@poetry run pytest -v --verbosity 1 -s

update: ## Update project dependencies and show outdated packages (if any)
	@poetry update
	@poetry show -o

env: ## Show current project env details
	@poetry env info

graph: ## Show installed dependencies of the project
	@poetry show --tree
