# Jobs App

A simple web app for keeping track of job applications

## Development

### Backend

All commands for working with the backend project should be done within the backend directory found in the root of the repository.

#### Prequisites

You must have the following installed on your system:

- [Python](https://www.python.org/) >= 3.9.18
- [Poetry](https://python-poetry.org/) >= 1.1.14
  > Reccomend installing poetry with [pipx](https://github.com/pypa/pipx) `pipx install poetry`
- [Poe](https://github.com/nat-n/poethepoet) >= 0.25.0
  > Reccomend installing with [pipx](https://github.com/pypa/pipx): `pipx install poethepoet`
- [DBMate](https://github.com/amacneil/dbmate) >= 2.6.0

#### Installing required development and runtime dependencies

```
poetry install
```

#### Run database migrations

```
poe dbmate up
```

#### Running the application

```
poe run [--help]
```

#### Linting & Formatting

To format the code:

```
poe format
```

To lint the code:

```
poe lint
```

To fix simple linting issues in the code:

```
poe lint_fix
```

All formatting, lint fixing and type checking targets can also be run with one command

```
poe pretty
```

#### Testing

```
poe test
```

#### Type checking

```
poe type_check
```

#### Making a migration

```
poe dbmate new [MIGRATION_NAME]
```

#### Building the docker container

The following command will build the docker container for the application locally.

```
docker build .
```
