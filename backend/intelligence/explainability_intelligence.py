class ExplainabilityIntelligence:

    @staticmethod
    def analyze(shap_results):

        if shap_results is None:

            return {

                "title": "🧠 Explainability Intelligence",

                "status": "warning",

                "analysis_completed": False,

                "top_features": [],

                "observation": (
                    "Feature importance analysis has not been generated."
                ),

                "message": (
                    "Run SHAP analysis first."
                )

            }

        feature_names = shap_results.get(
            "feature_names",
            []
        )

        importance = shap_results.get(
            "importance",
            []
        )

        top_features = []

        if feature_names and importance:

            pairs = list(
                zip(feature_names, importance)
            )

            pairs.sort(
                key=lambda x: x[1],
                reverse=True
            )

            top_features = [
                feature
                for feature, _ in pairs[:5]
            ]

        feature_text = "\n".join(

            f"• {feature}"

            for feature in top_features

        )

        return {

            "title": "🧠 Explainability Intelligence",

            "status": "success",

            "analysis_completed": True,

            "top_features": top_features,

            "observation": (
                "SHAP feature importance generated successfully."
            ),

            "message": (

                "Top Important Features\n\n"

                f"{feature_text}"

            )

        }