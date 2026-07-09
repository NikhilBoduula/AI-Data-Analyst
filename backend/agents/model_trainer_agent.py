from backend.ml.automl import AutoML


class ModelTrainerAgent:
    """
    AI Agent responsible for training Machine Learning models.
    """

    def __init__(self, dataframe):
        self.df = dataframe

    def run(self, target_column):

        automl = AutoML()

        return automl.run(
            self.df,
            target_column
        )