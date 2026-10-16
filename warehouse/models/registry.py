from warehouse.models.bronze.crm_cust_info import BronzeCustInfo
from warehouse.models.silver.crm_cust_info import SilverCustInfo
from warehouse.models.gold.crm_cust_info import GoldCustInfo

LAYER_MODELS = {
    "bronze": BronzeCustInfo,
    "silver": SilverCustInfo,
    "gold": GoldCustInfo,
}
