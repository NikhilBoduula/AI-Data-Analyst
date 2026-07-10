import shap
import numpy as np


class SHAPAnalyzer:

    def __init__(self, model, X_train):
        self.model = model
        self.X_train = X_train

    def _get_explainer(self):
        """
        Select the appropriate SHAP explainer based on model type.
        """

        model_name = self.model.__class__.__name__.lower()

        tree_models = [
            "randomforestclassifier",
            "randomforestregressor",
            "decisiontreeclassifier",
            "decisiontreeregressor",
            "extratreesclassifier",
            "extratreesregressor",
            "gradientboostingclassifier",
            "gradientboostingregressor",
            "xgbclassifier",
            "xgbregressor",
            "lgbmclassifier",
            "lgbmregressor",
            "catboostclassifier",
            "catboostregressor",
        ]

        linear_models = [
            "linearregression",
            "logisticregression",
            "ridge",
            "lasso",
            "elasticnet",
        ]

        if model_name in tree_models:
            return shap.TreeExplainer(self.model)

        elif model_name in linear_models:
            return shap.LinearExplainer(self.model, self.X_train)

        else:
            background = shap.sample(self.X_train, min(100, len(self.X_train)))
            return shap.KernelExplainer(self.model.predict, background)

    def compute(self):

        explainer = self._get_explainer()

        shap_values = explainer(self.X_train)

        return {
            "explainer": explainer,
            "shap_values": shap_values
        }