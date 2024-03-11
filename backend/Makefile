# create the venv
venv:
	if [ ! -d "$(DIR1)" ]; then \
		python3 -m venv .venv; \
	fi

# install python requirements
install:
	.venv/bin/pip install -r requirements.txt

install_cli:
	.venv/bin/pip install -e .

# first time setup
setup: venv install install_cli

# freeze python requirements
freeze:
	.venv/bin/pip freeze --exclude-editable > requirements.txt

# find all syntax issues
check:
	.venv/bin/ruff check

# fix all simple to fix syntax issues
check_fix:
	.venv/bin/ruff check --fix

# fix all format issues
pretty:
	.venv/bin/ruff format

# run tests
test:
	PYTHONPATH=$(PWD) .venv/bin/python -m pytest -v

# clean up the code
clean: check_fix pretty test

# run the backend API
run:
	.venv/bin/jobs_api
