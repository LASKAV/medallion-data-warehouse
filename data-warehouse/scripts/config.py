from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

# CRM files
CUST_FILE = BASE_DIR / "datasets" / "source_crm" / "cust_info.csv"
PRD_FILE = BASE_DIR / "datasets" / "source_crm" / "prd_info.csv"
SALES_FILE = BASE_DIR / "datasets" / "source_crm" / "sales_details.csv"

# ERP files (пример)
ERP_LOC_FILE = BASE_DIR / "datasets" / "source_erp" / "loc_a101.csv"
ERP_CUST_FILE = BASE_DIR / "datasets" / "source_erp" / "cust_az12.csv"