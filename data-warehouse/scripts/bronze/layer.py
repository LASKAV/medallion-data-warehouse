from spark import SparkContext, BronzeSpark
from scripts.config import CUST_FILE, PRD_FILE, SALES_FILE
from scripts.etl_interfaces import IBaseLayerETL
from pyspark.sql import DataFrame
from settings import settings

class BronzeLayerETL(IBaseLayerETL):
    def __init__(self):
        context = SparkContext(BronzeSpark())
        self.spark = context.spark

    def fetch_cust_info(self) -> DataFrame:
        return self.spark.read.csv(str(CUST_FILE), header=True, inferSchema=True)

    def fetch_prd_info(self) -> DataFrame:
        return self.spark.read.csv(str(PRD_FILE), header=True, inferSchema=True)

    def fetch_sales_info(self) -> DataFrame:
        return self.spark.read.csv(str(SALES_FILE), header=True, inferSchema=True)
    
    def write_to_postgres(self, df: DataFrame, table_name: str, schema: str):
        options = settings.get_jdbc_options()
        df.write \
        .format("jdbc") \
        .option("url", options["url"]) \
        .option("dbtable", f"{schema}.{table_name}") \
        .option("user", options["user"]) \
        .option("password", options["password"]) \
        .option("driver", "org.postgresql.Driver") \
        .mode("append") \
        .save()
