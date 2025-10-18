#!/bin/bash
set -e

echo "Waiting for Postgres at $POSTGRES_HOST:$POSTGRES_PORT..."
until pg_isready -h "$POSTGRES_HOST" -p "$POSTGRES_PORT" -U "$POSTGRES_USER"; do
  sleep 2
done

echo "Postgres is ready! Running Spark ETL..."
cd /app
echo "Testing PySpark import..."
uv run python -c "import pyspark; print('PySpark test: OK')"
echo "Starting main application..."
uv run python main.py