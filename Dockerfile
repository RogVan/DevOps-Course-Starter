FROM python:3.10 as base
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
ENV PATH=$PATH:/root/.local/share/pypoetry/venv/bin/
COPY pyproject.toml poetry.toml /app/
WORKDIR /app
COPY todo_app /app/todo_app
RUN poetry install

FROM base as production
ENTRYPOINT poetry run gunicorn --bind 0.0.0.0 "todo_app.app:create_app()"

FROM base as development
ENTRYPOINT poetry run flask run --host=0.0.0.0

FROM base as test
ENTRYPOINT ["poetry", "run", "pytest"]