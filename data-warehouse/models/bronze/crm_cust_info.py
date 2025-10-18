from models.bases.crm_cust_info_base import BaseCustInfo


class BronzeBaseCust(BaseCustInfo):
    __tablename__ = "crm_cust_info"
    __table_args__ = {"schema": "bronze"}
