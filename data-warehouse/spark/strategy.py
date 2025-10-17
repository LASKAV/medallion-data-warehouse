from abc import ABC, abstractmethod
from pyspark.sql import SparkSession


class SparkStrategy(ABC):
    @abstractmethod
    def create_session(self) -> SparkSession:
        """Return a configured SparkSession"""
        pass


""" BronzeLayerETL """


class BronzeSpark(SparkStrategy):
    def create_session(self) -> SparkSession:
        session = (
            SparkSession.builder.appName("BronzeLayerETL")
            .config("spark.sql.shuffle.partitions", "2")
            .config("spark.driver.memory", "2g")
            .getOrCreate()
        )
        return session


"""SilverLayerETL"""


class SilverSpark(SparkStrategy):
    def create_session(self) -> SparkSession:
        session = (
            SparkSession.builder.appName("SilverLayerETL")
            .config("spark.sql.shuffle.partitions", "2")
            .config("spark.driver.memory", "2g")
            .getOrCreate()
        )
        return session


"""GoldLayerETL"""


class GoldSpark(SparkStrategy):
    def create_session(self) -> SparkSession:
        session = (
            SparkSession.builder.appName("GoldLayerETL")
            .config("spark.sql.shuffle.partitions", "2")
            .config("spark.driver.memory", "2g")
            .getOrCreate()
        )
        return session