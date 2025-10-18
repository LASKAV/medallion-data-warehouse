from models.bronze.crm_cust_info import BronzeCrmCustomerInfo
from models.silver.crm_cust_info import SilverCrmCustomerInfo
from models.gold.crm_cust_info import GoldCrmCustomerInfo

LAYER_MODELS = {
    "bronze": BronzeCrmCustomerInfo,
    "silver": SilverCrmCustomerInfo,
    "gold": GoldCrmCustomerInfo,
}
