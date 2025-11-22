SHELL := /bin/bash -o pipefail

ifndef NOCOLOR
    RED    := $(shell tput -Txterm setaf 1)
    GREEN  := $(shell tput -Txterm setaf 2)
    YELLOW := $(shell tput -Txterm setaf 3)
    RESET  := $(shell tput -Txterm sgr0)
endif

PYTHON_FILES := $(shell find . -type f -name "*.py" ! -path "*/\.*" ! -path "*/migrations/*" ! -path "*/venv/*" ! -path "*/.venv/*")

## Help targets
.PHONY: help
help:
	@awk '/^.PHONY: / { \
		msg = match(lastLine, /^## /); \
			if (msg) { \
				cmd = substr($$0, 9, 100); \
				msg = substr(lastLine, 4, 1000); \
				printf "  ${GREEN}%-30s${RESET} %s\n", cmd, msg; \
			} \
	} \
	{ lastLine = $$0 }' $(MAKEFILE_LIST)

## Check dependencies
.PHONY: deps-check
deps-check:
	@echo "${GREEN}Checking dependencies${RESET}"
	poetry check --lock || exit 1
	poetry check || exit 1

## Start Docker environment
.PHONY: dev/up
dev/up:
	@echo "${GREEN}Starting Docker environment${RESET}"
	docker compose down
	docker compose --env-file .env up --build

## Stop Docker environment
.PHONY: dev/down
dev/down:
	@echo "${GREEN}Stopping containers${RESET}"
	docker compose down

## Access web container shell
.PHONY: dev/shell
dev/shell:
	docker compose exec web bash

## Lint code (Isort + Black)
.PHONY: lint
lint:
	@echo "Linting..."
	-@poetry run isort --profile='black' --line-length=88 --check-only --diff $(PYTHON_FILES)
	-@poetry run black --check --line-length=88 --preview $(PYTHON_FILES)

## Format code (Isort + Black)
.PHONY: format
format:
	@echo "Formatting..."
	poetry run isort --profile='black' --line-length=88 $(PYTHON_FILES)
	poetry run black --line-length=88 --preview -v $(PYTHON_FILES)

## Run Pre-commit
.PHONY: run-pre-commit-hook
run-pre-commit-hook:
	bash .git/hooks/pre-commit
	@echo "${GREEN}Pre-commit hooks executed successfully!${RESET}" 

#this is a section for shortcut or alias commands.