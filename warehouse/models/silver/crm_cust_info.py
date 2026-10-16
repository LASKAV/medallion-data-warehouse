from datetime import datetime, timezone

from sqlmodel import Field

from warehouse.models.bases.crm_cust_info_base import BaseCustInfo


class SilverCustInfo(BaseCustInfo, table=True):
    __tablename__ = "crm_cust_info"
    __table_args__ = {"schema": "silver"}

    dwh_create_date: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
