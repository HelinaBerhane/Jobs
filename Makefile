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

run_docker:
	docker compose build
	docker compose up

# This is temporary until we have a proper CI/CD pipeline
# TODO(luk707): Add a proper CI/CD pipeline
backend_container:
	docker build -t lukeharris954/jobs-backend -f backend.Dockerfile .

# TODO(luk707): Replace with github actions
push_image:
	docker push lukeharris954/jobs-backend
