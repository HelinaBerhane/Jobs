# setup local python environment
venv:
	if [ ! -d "$(DIR1)" ]; then \
		python3 -m venv .venv; \
	fi

# freeze python requirements
freeze:
	.venv/bin/pip freeze > requirements.txt

# install python requirements
install:
	.venv/bin/pip install -r requirements.txt

# generate openapi types
openapi:
	.venv/bin/python backend/gen_openapi.py openapi.json
	openapi-generator generate -i ./openapi.json -g typescript-fetch -o ./api-client

# find all type issues
check_types:
	.venv/bin/mypy .

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
	.venv/bin/pytest

# clean up the code
clean: check_fix pretty check_types test openapi

# run the backend API
run:
	PYTHONPATH=$(PWD) .venv/bin/python backend/main.py
