from sqlmodel import Field
from datetime import datetime
from models.bases.crm_cust_info_base import BaseCustInfo


class SilverCustInfo(BaseCustInfo):
    __tablename__ = "crm_cust_info"
    __table_args__ = {"schema": "silver"}

    dwh_create_date: datetime = Field(
        default_factory=datetime.now(datetime.timezone.utc)
    )
