# wine_data_filter.py

import pandas as pd

class WineDataFilter:
    def __init__(self, dataset_path: str):
        self.df = pd.read_csv(dataset_path)

    def filter_by_quality(self, quality: int):
        return self.df[self.df['quality'] == quality]

    def get_feature_distribution(self, feature: str):
        return self.df[feature].value_counts()
