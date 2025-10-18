FROM python:3.12-slim-bookworm

# Install system dependencies including Java (required for PySpark) and PostgreSQL client
RUN apt-get update && \
    apt-get install -y curl git openjdk-17-jre-headless postgresql-client && \
    rm -rf /var/lib/apt/lists/*

# Set JAVA_HOME for PySpark
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-arm64
RUN if [ ! -d "$JAVA_HOME" ]; then export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64; fi

RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

# Copy dependency files first for better Docker layer caching
COPY pyproject.toml uv.lock ./

# Install dependencies using uv
RUN uv sync --frozen --no-dev

COPY . .

RUN chmod +x /app/entrypoint.sh

CMD ["bash", "/app/entrypoint.sh"]