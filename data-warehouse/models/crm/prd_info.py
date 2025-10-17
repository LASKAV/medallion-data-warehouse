from pydantic import BaseModel
from typing import Optional
from datetime import datetime


#     prd_id      INT,
#     prd_key     VARCHAR(50),
#     prd_nm      VARCHAR(50),
#     prd_cost    INT,
#     prd_line    VARCHAR(50),
#     prd_start_dt TIMESTAMP,
#     prd_end_dt   TIMESTAMP


class Prd_info(BaseModel):
    prd_id: int
    prd_key: Optional[str] = None
    prd_nm: Optional[str] = None
    prd_cost: Optional[int] = None
    prd_line: Optional[str] = None
    prd_start_dt: Optional[datetime] = None
    prd_end_dt: Optional[datetime] = None