from backend.feature_engineering.encoder import Encoder
from backend.feature_engineering.scaler import Scaler
from backend.feature_engineering.selector import Selector


class FeaturePipeline:

    @staticmethod
    def run(df):

        encoded = Encoder.one_hot_encode(df)

        selected = Selector.remove_low_variance(
            encoded
        )

        scaled = Scaler.standard_scale(
            selected
        )

        return scaled