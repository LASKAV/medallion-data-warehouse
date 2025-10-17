from pydantic import BaseModel
from typing import Optional
from datetime import date


#     sls_ord_num  VARCHAR(50),
#     sls_prd_key  VARCHAR(50),
#     sls_cust_id  INT,
#     sls_order_dt DATE,
#     sls_ship_dt  DATE,
#     sls_due_dt   DATE,
#     sls_sales    INT,
#     sls_quantity INT,
#     sls_price    INT


class SalesDetails(BaseModel):
    sls_ord_num:  Optional[str] = None
    sls_prd_key:  Optional[str] = None
    sls_cust_id: Optional[int] = None
    sls_ship_dt: Optional[date] = None
    sls_due_dt: Optional[date] = None
    sls_sales: Optional[date] = None
    sls_sales: Optional[int] = None
    sls_quantity: Optional[int] = None
    sls_price: Optional[int] = None