import pandas as pd
from sklearn.preprocessing import LabelEncoder


class Encoder:

    @staticmethod
    def one_hot_encode(df: pd.DataFrame):

        categorical = df.select_dtypes(
            include=["object", "category"]
        ).columns

        if len(categorical) == 0:
            return df.copy()

        return pd.get_dummies(
            df,
            columns=categorical,
            drop_first=True
        )

    @staticmethod
    def label_encode(df: pd.DataFrame):

        encoded = df.copy()

        encoders = {}

        categorical = encoded.select_dtypes(
            include=["object", "category"]
        ).columns

        for column in categorical:

            le = LabelEncoder()

            encoded[column] = le.fit_transform(
                encoded[column].astype(str)
            )

            encoders[column] = le

        return encoded, encoders