from .strategy import SparkStrategy


class SparkContext:
    def __init__(self, strategy: SparkStrategy):
        self.strategy = strategy
        self.spark = self.strategy.create_session()
