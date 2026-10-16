from pyspark.sql import DataFrame
from abc import ABC, abstractmethod


class IBaseLayerETL(ABC):
    @abstractmethod
    def fetch_cust_info(self) -> DataFrame:
        """Fetch customer info as Spark DataFrame"""
        pass

    @abstractmethod
    def fetch_prd_info(self) -> DataFrame:
        """Fetch product info as Spark DataFrame"""
        pass

    @abstractmethod
    def fetch_sales_info(self) -> DataFrame:
        """Fetch sales info as Spark DataFrame"""
        pass

    @abstractmethod
    def write_to_postgres(self, df: DataFrame, table_name: str, schema: str):
        """Write DataFrame to Postgres with given schema"""
        pass
