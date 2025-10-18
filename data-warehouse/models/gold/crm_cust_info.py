from models.bases.crm_cust_info_base import BaseCustInfo


class GoldCustInfo(BaseCustInfo):
    __tablename__ = "crm_cust_info"
    __table_args__ = {"schema": "gold"}
