FROM python:3.10
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
ENV PATH=$PATH:/root/.local/share/pypoetry/venv/bin/
COPY pyproject.toml poetry.toml /app/
WORKDIR /app
RUN poetry install
COPY .env.template /app/
COPY todo_app /app/todo_app
ENTRYPOINT poetry run gunicorn --bind 0.0.0.0 "todo_app.app:create_app()"