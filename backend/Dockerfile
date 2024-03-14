FROM python:3.9.18-bookworm

RUN pip install poetry==1.1.14

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --no-dev --no-interaction --no-ansi

COPY . .

ENV PYTHONPATH=/app/src
CMD ["poetry", "run", "python", "-m", "cli.main", "serve"]
