PENV = ../etl/.venv
PYTHON = $(PENV)/bin/python
PYRIGHT = $(PENV)/bin/pyright
TOML_SORT = $(PENV)/bin/toml-sort

PROJECT_FOLDERS= bin libs

.PHONY: init
init:
	@echo "Installing..."
	@poetry install


.PHONY: lint
lint:
	@echo "Running poetry checks..."
	@poetry check
	@poetry lock --check --no-update

	@echo "Running black checks..."
	@$(PYTHON) -m black --check .

	@echo "Running isort checks..."
	@$(PYTHON) -m isort --check-only --atomic .


.PHONY: lint-fix
lint-fix:
	@echo "Running poetry autofixes..."
	@poetry check
	@poetry lock --no-update

	@echo "Running black autofixes..."
	@$(PYTHON) -m black --safe .

	@echo "Running isort autofixes..."
	@$(PYTHON) -m isort --atomic .

	@echo "Running toml-sort autofixes..."
	@$(TOML_SORT) --in-place pyproject.toml

	@echo "Running sort-all autofixes..."
	@find $(PROJECT_FOLDERS) -name "*.py" -type f -exec $(PYTHON) -m sort_all "{}" \;

	@echo "Running pyupgrade autofixes..."
	@find $(PROJECT_FOLDERS) -name "*.py" -type f -exec $(PYTHON) -m pyupgrade --py311-plus "{}" \;

	@echo "Running pylint checks..."
	@$(PYTHON) -m pylint .

	@echo "Running pyright checks..."
	@$(PYRIGHT)

.PHONY: run
run:
	@echo "Running..."
	@poetry run python -m bin


.PHONY: config
config:
	rm -rf clickhouse/clickhouse01 clickhouse/clickhouse02 
	mkdir -p  clickhouse/clickhouse01 clickhouse/clickhouse02 
	REPLICA=01 SHARD=01 envsubst < config.xml > clickhouse/clickhouse01/config.xml
	REPLICA=02 SHARD=01 envsubst < config.xml > clickhouse/clickhouse02/config.xml
	cp users.xml clickhouse/clickhouse01/users.xml
	cp users.xml clickhouse/clickhouse02/users.xml
