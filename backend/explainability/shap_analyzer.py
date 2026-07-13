import shap
import numpy as np


class SHAPAnalyzer:

    def __init__(self, model, X_train):
        self.model = model
        self.X_train = X_train

    def _get_explainer(self):

        model_name = self.model.__class__.__name__.lower()

        print("=" * 50)
        print("Model:", self.model.__class__.__name__)
        print("Model Name:", model_name)
        print("=" * 50)

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

            print("Using TreeExplainer")

            return shap.TreeExplainer(self.model)

        elif model_name in linear_models:

            print("Using LinearExplainer")

            return shap.LinearExplainer(
                self.model,
                self.X_train
            )

        else:

            print("Using KernelExplainer")

            background = shap.sample(
                self.X_train.astype(float),
                min(100, len(self.X_train))
            )

            return shap.KernelExplainer(
                self.model.predict,
                background
            )

    def compute(self):

        explainer = self._get_explainer()

        # -----------------------------
        # Generate SHAP values
        # -----------------------------

        if isinstance(explainer, shap.KernelExplainer):

            shap_values = explainer.shap_values(self.X_train)

        else:

            explanation = explainer(self.X_train)

            shap_values = explanation.values

        # -----------------------------
        # Handle multiclass output
        # -----------------------------

        if isinstance(shap_values, list):

            shap_values = shap_values[0]

        elif len(shap_values.shape) == 3:

            shap_values = shap_values[:, :, 0]

        # -----------------------------
        # Feature Importance
        # -----------------------------

        importance = np.abs(shap_values).mean(axis=0)

        return {

            "feature_names": self.X_train.columns.tolist(),

            "importance": importance.tolist()

        }