FROM python:3.10

WORKDIR /app

# Install Poetry using the official installation method
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# Disable Poetry's virtual environment creation
ENV POETRY_VIRTUALENVS_CREATE=false

# Ensure Poetry is installed properly
RUN poetry --version

# Copy poetry files (pyproject.toml and poetry.lock) into the container
COPY pyproject.toml poetry.lock /app/

# Install project dependencies using Poetry
RUN poetry install --no-dev --no-interaction --no-ansi

# Copy the rest of the application code into the container
COPY . /app

