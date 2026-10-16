from warehouse.models.bases.crm_cust_info_base import BaseCustInfo


class BronzeCustInfo(BaseCustInfo, table=True):
    __tablename__ = "crm_cust_info"
    __table_args__ = {"schema": "bronze"}
