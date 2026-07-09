from backend.feature_engineering.feature_pipeline import FeaturePipeline


class FeatureEngineeringAgent:
    """
    AI Agent responsible for Feature Engineering.
    """

    def __init__(self, dataframe):
        self.df = dataframe

    def run(self):

        engineered_df = FeaturePipeline.run(self.df)

        return {

            "original_shape": self.df.shape,

            "new_shape": engineered_df.shape,

            "new_columns": list(engineered_df.columns),

            "engineered_df": engineered_df

        }