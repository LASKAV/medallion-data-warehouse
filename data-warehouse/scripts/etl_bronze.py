# from models import CustomInfo
# from pyspark.sql.functions import udf
# from pyspark.sql.types import BooleanType

from spark import SparkContext, BronzeSpark
from scripts.config import CUST_FILE, PRD_FILE, SALES_FILE

from abc import ABC, abstractmethod
from pyspark.sql import DataFrame


class IBronzeLayerETL(ABC):
    @abstractmethod
    def fetch_cust_info(self) -> DataFrame:
        """Fetch customer info as Spark DataFrame"""
        pass


#     @abstractmethod
#     def fetch_prd_info(self) -> DataFrame:
#         """Fetch product info as Spark DataFrame"""
#         pass

#     @abstractmethod
#     def fetch_sales_info(self) -> DataFrame:
#         """Fetch sales info as Spark DataFrame"""
#         pass

#     @abstractmethod
#     def write_to_postgres(self, df: DataFrame, table_name: str):
#         """Write DataFrame to Postgres"""
#         pass


class BronzeLayerETL(IBronzeLayerETL):
    def __init__(self):
        context = SparkContext(BronzeSpark())
        self.spark = context.spark

    def fetch_cust_info(self):
        data = self.spark.read.csv(str(CUST_FILE), header=True, inferSchema=True)
        data.show(10)
