import pandas as pd

from sklearn.preprocessing import (
    StandardScaler,
    MinMaxScaler
)


class Scaler:

    @staticmethod
    def standard_scale(df: pd.DataFrame):

        scaled = df.copy()

        numeric = scaled.select_dtypes(
            include="number"
        ).columns

        scaler = StandardScaler()

        scaled[numeric] = scaler.fit_transform(
            scaled[numeric]
        )

        return scaled

    @staticmethod
    def minmax_scale(df: pd.DataFrame):

        scaled = df.copy()

        numeric = scaled.select_dtypes(
            include="number"
        ).columns

        scaler = MinMaxScaler()

        scaled[numeric] = scaler.fit_transform(
            scaled[numeric]
        )

        return scaled