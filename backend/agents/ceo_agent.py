from backend.agents.cleaning_agent import CleaningAgent
from backend.agents.eda_agent import EDAAgent
from backend.agents.feature_engineering_agent import FeatureEngineeringAgent
from backend.agents.model_trainer_agent import ModelTrainerAgent


class CEOAgent:
    """
    Central Orchestrator for the AI Data Scientist Platform.
    """

    def __init__(self, dataframe):

        self.df = dataframe

    def run(self, target_column):

        # -----------------------
        # Cleaning
        # -----------------------

        cleaning = CleaningAgent(self.df)

        cleaning_report = cleaning.analyze()

        cleaned_df = cleaning.clean()

        # -----------------------
        # EDA
        # -----------------------

        eda = EDAAgent(cleaned_df)

        eda_report = eda.run()

        # -----------------------
        # Feature Engineering
        # -----------------------

        feature = FeatureEngineeringAgent(cleaned_df)

        feature_report = feature.run()

        engineered_df = feature_report["engineered_df"]

        # -----------------------
        # Model Training
        # -----------------------

        trainer = ModelTrainerAgent(
            engineered_df
        )

        ml_report = trainer.run(
            target_column
        )

        return {

            "cleaning": cleaning_report,

            "eda": eda_report,

            "feature_engineering": feature_report,

            "ml": ml_report

        }