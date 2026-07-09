import pandas as pd

from sklearn.preprocessing import PolynomialFeatures


class FeatureGenerator:

    @staticmethod
    def polynomial(df: pd.DataFrame):

        numeric = df.select_dtypes(
            include="number"
        )

        if numeric.empty:
            return df.copy()

        poly = PolynomialFeatures(
            degree=2,
            include_bias=False
        )

        data = poly.fit_transform(numeric)

        names = poly.get_feature_names_out(
            numeric.columns
        )

        return pd.DataFrame(
            data,
            columns=names
        )