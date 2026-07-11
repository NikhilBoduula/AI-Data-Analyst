class ReasoningEngine:

    @staticmethod
    def analyze(
        dataset_info,
        quality_info,
        model_info,
        explainability_info,
        recommendation_info,
    ):

        strengths = []
        risks = []
        actions = []
        observations = []

        # =====================================================
        # Dataset Reasoning
        # =====================================================

        if dataset_info["rows"] < 1000:

            observations.append(
                "The dataset is relatively small and is suitable for rapid experimentation."
            )

            actions.append(
                "Consider collecting more data to improve model generalization."
            )

        elif dataset_info["rows"] < 10000:

            observations.append(
                "The dataset size is appropriate for reliable machine learning."
            )

        else:

            observations.append(
                "A large dataset is available, which is beneficial for production models."
            )

        # =====================================================
        # Quality Reasoning
        # =====================================================

        if quality_info["missing_values"] == 0:

            strengths.append(
                "No missing values were detected."
            )

        else:

            risks.append(
                f"{quality_info['missing_values']} missing values may reduce model quality."
            )

            actions.append(
                "Handle missing values before deployment."
            )

        if quality_info["duplicate_rows"] == 0:

            strengths.append(
                "No duplicate records were found."
            )

        else:

            risks.append(
                f"{quality_info['duplicate_rows']} duplicate rows were detected."
            )

            actions.append(
                "Remove duplicate records."
            )

        # =====================================================
        # Model Reasoning
        # =====================================================

        if model_info["best_model"]:

            strengths.append(
                f"{model_info['best_model']} achieved the best {model_info['metric']} score."
            )

            observations.append(
                f"{model_info['models_evaluated']} machine learning models were compared."
            )

        else:

            risks.append(
                "Machine learning models have not been trained."
            )

            actions.append(
                "Run AutoML before deployment."
            )

        # =====================================================
        # Explainability
        # =====================================================

        if explainability_info["analysis_completed"]:

            strengths.append(
                "Model explainability has been completed."
            )

        else:

            risks.append(
                "Feature importance analysis is unavailable."
            )

            actions.append(
                "Generate SHAP explainability."
            )

        # =====================================================
        # Deployment
        # =====================================================

        score = recommendation_info["deployment_score"]

        if score >= 90:

            observations.append(
                "The project is close to production readiness."
            )

        elif score >= 75:

            observations.append(
                "The project is progressing well but requires minor improvements."
            )

        else:

            observations.append(
                "Several improvements are recommended before deployment."
            )

        # =====================================================
        # Return
        # =====================================================

        return {

            "title": "🧠 AI Reasoning",

            "status": "success",

            "strengths": strengths,

            "risks": risks,

            "actions": actions,

            "observations": observations,

            "message":

                "Strengths\n\n"

                + "\n".join(
                    f"• {x}" for x in strengths
                )

                + "\n\nRisks\n\n"

                + (
                    "\n".join(f"• {x}" for x in risks)
                    if risks
                    else "• No major risks detected."
                )

                + "\n\nObservations\n\n"

                + "\n".join(
                    f"• {x}" for x in observations
                )

                + "\n\nRecommended Actions\n\n"

                + "\n".join(
                    f"• {x}" for x in actions
                )

        }