class ExplainabilityIntelligence:

    @staticmethod
    def analyze(shap_results):

        # --------------------------------------------
        # SHAP Not Available
        # --------------------------------------------

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
                    "SHAP analysis has not been generated yet.\n\n"
                    "Run the Explainability module to identify "
                    "the most influential features."
                )

            }

        # --------------------------------------------
        # Try to read feature importance
        # --------------------------------------------

        top_features = shap_results.get(
            "top_features",
            []
        )

        if len(top_features) == 0:

            observation = (
                "SHAP analysis completed successfully."
            )

            feature_text = (
                "Top feature information is currently unavailable."
            )

        else:

            observation = (
                "The model explanation was successfully generated."
            )

            feature_text = "\n".join(
                f"• {feature}"
                for feature in top_features
            )

        # --------------------------------------------
        # Return Intelligence
        # --------------------------------------------

        return {

            "title": "🧠 Explainability Intelligence",

            "status": "success",

            "analysis_completed": True,

            "top_features": top_features,

            "observation": observation,

            "message": (

                "Explainability Status : Completed\n\n"

                "Most Important Features\n\n"

                f"{feature_text}\n\n"

                "Observation\n\n"

                f"{observation}"

            )

        }