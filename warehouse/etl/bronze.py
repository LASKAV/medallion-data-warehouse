from warehouse.spark import SparkContext, BronzeSpark
from warehouse.spark.strategy import SparkStrategy
from warehouse.config import CUST_FILE, PRD_FILE, SALES_FILE
from warehouse.etl.interfaces import IBaseLayerETL
from pyspark.sql import DataFrame
from warehouse.settings import settings


class BronzeLayerETL(IBaseLayerETL):
    def __init__(self):
        # Get JDBC options from settings
        settings_options = settings.get_jdbc_options()
        self.jdbc_options = SparkStrategy.get_jdbc_options(
            url=settings_options["url"],
            user=settings_options["user"], 
            password=settings_options["password"]
        )
        context = SparkContext(BronzeSpark())
        self.spark = context.spark

    def fetch_cust_info(self) -> DataFrame:
        return self.spark.read.csv(str(CUST_FILE), header=True, inferSchema=True)

    def fetch_prd_info(self) -> DataFrame:
        return self.spark.read.csv(str(PRD_FILE), header=True, inferSchema=True)

    def fetch_sales_info(self) -> DataFrame:
        return self.spark.read.csv(str(SALES_FILE), header=True, inferSchema=True)
    
    def write_to_postgres(self, df: DataFrame, table_name: str, schema: str):
        df.write \
            .format("jdbc") \
            .options(**self.jdbc_options) \
            .option("dbtable", f"{schema}.{table_name}") \
            .mode("append") \
            .save()
