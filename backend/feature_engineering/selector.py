import pandas as pd


class Selector:

    @staticmethod
    def remove_low_variance(df: pd.DataFrame):

        nunique = df.nunique()

        keep = nunique[nunique > 1].index

        return df[keep]