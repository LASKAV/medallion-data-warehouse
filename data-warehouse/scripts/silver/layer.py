from spark import SparkContext, SilverSpark
from scripts.config import CUST_FILE, PRD_FILE, SALES_FILE
from scripts.etl_interfaces import IBaseLayerETL
from pyspark.sql import DataFrame


class SilverLayerETL(IBaseLayerETL):
    def __init__(self):
        context = SparkContext(SilverSpark())
        self.spark = context.spark

    def fetch_cust_info(self) -> DataFrame:
        return self.spark.read.csv(str(CUST_FILE), header=True, inferSchema=True)

    def fetch_prd_info(self) -> DataFrame:
        return self.spark.read.csv(str(PRD_FILE), header=True, inferSchema=True)

    def fetch_sales_info(self) -> DataFrame:
        return self.spark.read.csv(str(SALES_FILE), header=True, inferSchema=True)
