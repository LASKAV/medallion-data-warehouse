from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DRIVERS_DIR = BASE_DIR / "drivers"

POSTGRES_JDBC_JAR = DRIVERS_DIR / "postgresql-42.7.8.jar"

# CRM files
CUST_FILE = DATA_DIR / "source_crm" / "cust_info.csv"
PRD_FILE = DATA_DIR / "source_crm" / "prd_info.csv"
SALES_FILE = DATA_DIR / "source_crm" / "sales_details.csv"

# ERP files
ERP_LOC_FILE = DATA_DIR / "source_erp" / "LOC_A101.csv"
ERP_CUST_FILE = DATA_DIR / "source_erp" / "CUST_AZ12.csv"
ERP_PX_CAT_FILE = DATA_DIR / "source_erp" / "PX_CAT_G1V2.csv"
