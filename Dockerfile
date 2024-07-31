FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    curl \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && ln -s /root/.local/bin/poetry /usr/local/bin/poetry \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY . .

# CMD ["daphne", "-h", "0.0.0.0", "-p", "8001", "email_reader.asgi:application"]
CMD ["poetry", "run", "python", "manage.py", "runserver"]
