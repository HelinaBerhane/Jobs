# create the venv
venv:
	if [ ! -d "$(DIR1)" ]; then \
		python3 -m venv .venv; \
	fi

# first time setup
setup: venv install install_cli

# freeze python requirements
freeze:
	.venv/bin/pip freeze --exclude-editable > requirements.txt

# install python requirements
install:
	.venv/bin/pip install -r requirements.txt

install_cli:
	.venv/bin/pip install -e .

# find all syntax issues
check:
	.venv/bin/ruff check

# fix all simple to fix syntax issues
check_fix:
	.venv/bin/ruff check --fix

# fix all format issues
pretty:
	.venv/bin/ruff format
