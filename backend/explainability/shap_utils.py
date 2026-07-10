import pandas as pd
import numpy as np


class SHAPUtils:

    @staticmethod
    def feature_importance(shap_values):

        importance = np.abs(shap_values.values).mean(axis=0)

        df = pd.DataFrame({
            "Feature": shap_values.feature_names,
            "Importance": importance
        })

        df = df.sort_values(
            "Importance",
            ascending=False
        )

        return df