from abc import ABC, abstractmethod
from pyspark.sql import SparkSession

from warehouse.config import POSTGRES_JDBC_JAR


class SparkStrategy(ABC):
    # Common configuration for all Spark sessions
    DEFAULT_CONFIGS = {
        "spark.sql.shuffle.partitions": "2",
        "spark.driver.memory": "2g",
        "spark.jars": str(POSTGRES_JDBC_JAR)
    }
    
    @abstractmethod
    def create_session(self) -> SparkSession:
        """Return a configured SparkSession"""
        pass
    
    def _get_base_builder(self, app_name: str) -> SparkSession.Builder:
        """Create a base SparkSession builder with common configurations"""
        builder = SparkSession.builder.appName(app_name)
        
        for key, value in self.DEFAULT_CONFIGS.items():
            builder = builder.config(key, value)
            
        return builder
    
    @staticmethod
    def get_jdbc_options(url: str, user: str, password: str) -> dict:
        """Get JDBC connection options"""
        return {
            "url": url,
            "user": user, 
            "password": password,
            "driver": "org.postgresql.Driver"
        }


""" BronzeLayerETL """


class BronzeSpark(SparkStrategy):
    def create_session(self) -> SparkSession:
        return self._get_base_builder("BronzeLayerETL").getOrCreate()


"""SilverLayerETL"""


class SilverSpark(SparkStrategy):
    def create_session(self) -> SparkSession:
        return self._get_base_builder("SilverLayerETL").getOrCreate()


"""GoldLayerETL"""


class GoldSpark(SparkStrategy):
    def create_session(self) -> SparkSession:
        return self._get_base_builder("GoldLayerETL").getOrCreate()