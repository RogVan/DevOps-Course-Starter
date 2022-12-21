# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Authentication

The project persists data using Trello. For this reason, a Trello key-token combination is required for authenticating API requests to Trello.

You will first need to [create an account](https://trello.com/signup) and then generate a [new API key and token](https://trello.com/app-key). These variables should be stored in the .env file.

You will also need to create a new Trello board with lists titled 'To Do', 'In Progress' and 'Complete'. save the list IDs and board ID as environment variables.

## Running the App on remote host using ansible

Connect to your remote control node (using SSH for example)

Copy the ansible and templates directories into the root of the control node

Run `ansible-playbook my_playbook.yml -i inventory`

You will be prompted to supply your trello api key and token

Navigate to port 5000 on your host to view the website

## Running the app in dev mode with Docker

Make sure you have Docker Desktop installed

Populate the environment variables in a `.env` file like usual

Run `docker build --target development --tag todo-app:dev` to build the image

Run `docker run -d -p 8000:5000 --mount type=bind,source="$(pwd)"/todo_app,target=/app/todo_app --env-file=.env todo-app:dev` to run the container in dev mode with hot reloading

Navigate to `localhost:8000` to open the website

## Running the app in production mode with Docker Compose

Make sure you have Docker Desktop installed

Populate the environment variables in a `.env` file like usual

Run `docker compose up` from in root directory

Navigate to `localhost:8000` to open the website

## Running the App Locally

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Running Tests

To run the entire test suite, run `poetry run pytest`

To run a single test class, run `poetry run pytest <--test file path-->`