class ModelIntelligence:

    @staticmethod
    def analyze(automl_results):

        if automl_results is None:

            return {

                "title": "🤖 Model Intelligence",

                "models_evaluated": 0,

                "best_model": None,

                "metric": None,

                "best_score": None,

                "top_models": [],

                "observation": (
                    "AutoML has not been executed yet."
                ),

                "message": (
                    "Run AutoML to generate model intelligence."
                )

            }

        leaderboard = automl_results["leaderboard"]

        best = automl_results["best_model"]

        metric = automl_results["metric"]

        models_evaluated = len(leaderboard)

        top_models = leaderboard[:3]

        # --------------------------------------------
        # Observation
        # --------------------------------------------

        if models_evaluated >= 10:

            observation = (
                "A comprehensive comparison was performed across "
                "multiple machine learning algorithms."
            )

        elif models_evaluated >= 5:

            observation = (
                "Several machine learning models were evaluated "
                "to identify the best performer."
            )

        else:

            observation = (
                "Only a small number of machine learning models "
                "were evaluated."
            )

        # --------------------------------------------
        # Leaderboard Text
        # --------------------------------------------

        leaderboard_text = ""

        for index, model in enumerate(top_models, start=1):

            leaderboard_text += (
                f"{index}. "
                f"{model['Model']} "
                f"({round(model[metric],4)})\n"
            )

        # --------------------------------------------
        # Return Intelligence
        # --------------------------------------------

        return {

            "title": "🤖 Model Intelligence",

            "models_evaluated": models_evaluated,

            "best_model": best["Model"],

            "metric": metric,

            "best_score": round(
                best[metric],
                4
            ),

            "top_models": top_models,

            "observation": observation,

            "message": (

                f"Models Evaluated : {models_evaluated}\n\n"

                f"Best Model : {best['Model']}\n"

                f"{metric} : {round(best[metric],4)}\n\n"

                "Top 3 Models\n\n"

                f"{leaderboard_text}\n"

                "Observation\n\n"

                f"{observation}"

            )

        }