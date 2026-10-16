# Medallion Data Warehouse

A data warehouse built on the **medallion architecture** (Bronze → Silver → Gold).
ETL is written in **PySpark**, data is stored in **PostgreSQL**, and everything runs with **Docker Compose**.

The source data is two sets of CSV files (CRM and ERP) from a fictional company selling bikes and accessories.

## Architecture

```
 CSV (CRM + ERP)
      │  PySpark (read.csv)
      ▼
┌──────────┐   cleaning,        ┌──────────┐   business model,   ┌──────────┐
│  BRONZE  │ ─ normalization ─▶ │  SILVER  │ ─ star schema ────▶ │   GOLD   │
│ raw data │                    │ cleaned  │                     │ BI-ready │
└──────────┘                    └──────────┘                     └──────────┘
          PostgreSQL schemas: bronze / silver / gold
```

| Layer  | Purpose                                                    | Status                              |
|--------|------------------------------------------------------------|-------------------------------------|
| Bronze | Load CSVs into Postgres as-is                              | Implemented for `crm_cust_info`     |
| Silver | Cleaning, type casting, deduplication (`dwh_create_date`)  | Tables created, ETL is a stub       |
| Gold   | Analytical model (facts / dimensions)                      | Stub                                |

## Tech stack

- Python ≥ 3.12, dependencies managed with [uv](https://docs.astral.sh/uv/)
- PySpark ≥ 3.5 with the PostgreSQL JDBC driver (`drivers/postgresql-42.7.8.jar`)
- PostgreSQL 16
- pydantic / pydantic-settings for configuration
- SQLModel / SQLAlchemy for table models
- pytest
- Docker / Docker Compose (Java 17 inside the container for Spark)

## Project structure

```
.
├── main.py                  # entry point: runs the bronze load
├── warehouse/               # application package
│   ├── config.py            # paths to data files and the JDBC driver
│   ├── settings.py          # settings loaded from .env (DATABASE_URL_DOCKER)
│   ├── db.py                # async SQLAlchemy engine / session
│   ├── etl/
│   │   ├── interfaces.py    # IBaseLayerETL abstract interface
│   │   ├── bronze.py        # BronzeLayerETL: read CSV, write to Postgres via JDBC
│   │   ├── silver.py        # SilverLayerETL (currently only reads CSV)
│   │   └── gold.py          # GoldLayerETL (currently only reads CSV)
│   ├── spark/
│   │   ├── strategy.py      # Strategy pattern: BronzeSpark / SilverSpark / GoldSpark
│   │   └── context.py       # SparkContext builds a session from a strategy
│   └── models/              # SQLModel models (bases / bronze / silver / gold)
├── sql/                     # run on first Postgres start (docker-entrypoint-initdb.d)
│   ├── 01_create_schemas.sql
│   ├── 02_create_bronze_tables.sql
│   └── 03_create_silver_tables.sql
├── data/
│   ├── source_crm/          # cust_info, prd_info, sales_details
│   └── source_erp/          # CUST_AZ12, LOC_A101, PX_CAT_G1V2
├── drivers/                 # PostgreSQL JDBC jar
├── tests/
├── Dockerfile
├── docker-compose.yaml
├── entrypoint.sh            # waits for Postgres, then runs main.py
└── .env.example
```

### Source data

| System | File                | Table (bronze / silver) | Content                      |
|--------|---------------------|-------------------------|------------------------------|
| CRM    | `cust_info.csv`     | `crm_cust_info`         | Customers                    |
| CRM    | `prd_info.csv`      | `crm_prd_info`          | Products                     |
| CRM    | `sales_details.csv` | `crm_sales_details`     | Sales (order lines)          |
| ERP    | `CUST_AZ12.csv`     | `erp_cust_az12`         | Customer birth date, gender  |
| ERP    | `LOC_A101.csv`      | `erp_loc_a101`          | Customer country             |
| ERP    | `PX_CAT_G1V2.csv`   | `erp_px_cat_g1v2`       | Product categories           |

## Getting started

### 1. Configure the environment

```bash
cp .env.example .env
# edit .env and set POSTGRES_PASSWORD (and the same password in DATABASE_URL_DOCKER)
```

### 2. Run with Docker

```bash
docker compose up --build
```

What happens:

1. `postgres` starts; `sql/` creates the schemas and the bronze/silver tables.
2. The `spark` container is built (Python 3.12 + Java 17 + uv dependencies).
3. `entrypoint.sh` waits for Postgres and runs `main.py`.
4. `main.py` reads `cust_info.csv`, prints the DataFrame and appends it to `bronze.crm_cust_info`.

The Spark UI is at http://localhost:4040 while a job is running. Postgres is on `localhost:5432`.

Check the result:

```bash
docker exec -it postgres psql -U postgres -d warehouse \
  -c "SELECT count(*) FROM bronze.crm_cust_info;"
```

> Data is written in `append` mode, so re-running duplicates rows.
> To start from scratch: `docker compose down -v`.

### 3. Run locally (Spark outside Docker)

Requires Java 17 and uv. Start only Postgres with `docker compose up postgres`, then:

```bash
uv sync
# in .env use host "localhost" in DATABASE_URL_DOCKER
uv run python main.py
```

### Tests

```bash
uv run pytest
```

## Design notes

- **Strategy** (`warehouse/spark/strategy.py`): each layer has its own strategy for creating a
  `SparkSession`, sharing common settings (`DEFAULT_CONFIGS`: shuffle partitions, driver memory, JDBC jar).
- **Common ETL interface** (`IBaseLayerETL`): each layer implements `fetch_cust_info`,
  `fetch_prd_info`, `fetch_sales_info` and `write_to_postgres`.
- **Models** (`warehouse/models`): a shared base model per entity is extended by each layer's
  model, which only differs by schema (silver adds `dwh_create_date`).

## License

See [LICENSE](LICENSE).
