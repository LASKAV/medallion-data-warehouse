from pydantic import BaseModel
from typing import Optional
from datetime import date


#     cst_id             INT,
#     cst_key            VARCHAR(50),
#     cst_firstname      VARCHAR(50),
#     cst_lastname       VARCHAR(50),
#     cst_marital_status VARCHAR(50),
#     cst_gndr           VARCHAR(50),
#     cst_create_date    DATE


class Custom_info(BaseModel):
    cst_id: int
    cst_key: str
    cst_firstname: Optional[str] = None
    cst_lastname: Optional[str] = None
    cst_marital_status: Optional[str] = None
    cst_gndr: Optional[str] = None
    cst_create_date: Optional[date] = None