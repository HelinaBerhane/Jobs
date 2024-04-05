# Jobs App
A simple web app for keeping track of job applications


## Backend API
>**N.B. All commands for working with the backend API should be done within the backend directory in the root of the repository.**

### Setup 

#### Prequisites
- PyEnv ((github)[https://github.com/pyenv/pyenv])
    ```
    brew install pyenv
    ```
- Python >= 3.9.18 ([website](https://www.python.org/))
- pipx ([github](https://github.com/pypa/pipx))
    ```
    brew install pipx
    pipx ensurepath
    ```
- Poe >= 0.25.0 ([github](https://github.com/nat-n/poethepoet))
    ```
    pipx install poethepoet
    ```
- Poetry  >= 1.1.14 ([website](https://python-poetry.org/))
    ```
    pipx install poetry
    ```
- DBMate >= 2.6.0 ([DBMate](https://github.com/amacneil/dbmate))
    ```
    brew install dbmate
    ```

#### Setup Python Environment
```
pyenv install 3.9.18
pyenv local 3.9.18
```

#### Select Python Interpreter in VSCode
```
poetry shell
```
copy the output from `/Users/...` to `.../virtualenvs/backend-21K18sx5-py3.12` to your VSCode python interpreter
```
cmd p
>Python: Select Interpreter
```

#### Install Dependencies
```
poetry install
```

#### Run Database Migrations
```
poe dbmate up
```

### Development

#### Format the code
```
poe format
```

#### Lint the code
```
poe lint
```

#### Fix simple linting issues
```
poe lint_fix
```

#### Check the types in the code
```
poe type_check
```

#### Run all formatting, lint type checking fixes
```
poe pretty
```

#### Generating OpenAPI schemas
First time
```sh
cd ../backend; poe openapi
cd ../api-client; npm install
cd ../frontend; npm install ../api-client
```
Second time onwards
```sh
cd ../backend; poe openapi
cd ../frontend; npm install ../api-client
```

#### Make a database migration
```
poe dbmate new [MIGRATION_NAME]
```

#### Add a new Dependency
```
poetry add <dependency-name>
```

### Use

#### Use a production version

##### Build the docker container locally
```
docker build .
```

#### Use a local test version

##### Run the API
```
poe run serve
```

##### Use the API

[http://localhost:8000/docs](http://localhost:8000/docs)

## Frontend Web App

>**N.B. All commands for working with the frontend web app should be done within the frontend directory in the root of the repository.**

This app was created using [`@capacitor/create-app`](https://github.com/ionic-team/create-capacitor-app),
and comes with a very minimal shell for building an app.

### Setup 
#### Install Dependencies
```
npm install
```

### Usage

#### Run the Web App
```
npm start
```

##### Use the API
[http://localhost:3000](http://localhost:3000)
