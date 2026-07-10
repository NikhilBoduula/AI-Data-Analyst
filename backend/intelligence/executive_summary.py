class ExecutiveSummary:

    @staticmethod
    def generate(
        dataset_info,
        quality_info,
        model_info,
        explainability_info,
        recommendation_info
    ):

        summary = []

        # =====================================================
        # Dataset
        # =====================================================

        summary.append(
            f"The uploaded dataset contains "
            f"{dataset_info['rows']:,} rows and "
            f"{dataset_info['columns']} columns."
        )

        summary.append(
            f"It has been classified as a "
            f"{dataset_info['dataset_size'].lower()}."
        )

        # =====================================================
        # Data Quality
        # =====================================================

        summary.append(
            f"The overall dataset health score is "
            f"{quality_info['health_score']}/100 "
            f"({quality_info['status']})."
        )

        if quality_info["missing_values"] == 0:

            summary.append(
                "No missing values were detected."
            )

        else:

            summary.append(
                f"{quality_info['missing_values']} missing values "
                f"were identified."
            )

        if quality_info["duplicate_rows"] > 0:

            summary.append(
                f"{quality_info['duplicate_rows']} duplicate "
                f"records should be removed."
            )

        # =====================================================
        # Model
        # =====================================================

        if model_info["best_model"]:

            summary.append(
                f"{model_info['models_evaluated']} machine "
                f"learning models were evaluated."
            )

            summary.append(
                f"The best-performing model was "
                f"{model_info['best_model']} with a "
                f"{model_info['metric']} score of "
                f"{model_info['best_score']}."
            )

        else:

            summary.append(
                "Machine learning models have not "
                "been trained yet."
            )

        # =====================================================
        # Explainability
        # =====================================================

        if explainability_info["analysis_completed"]:

            summary.append(
                "Model explainability analysis was "
                "completed successfully."
            )

        else:

            summary.append(
                "Explainability analysis has not "
                "been generated yet."
            )

        # =====================================================
        # Recommendation
        # =====================================================

        summary.append(
            f"Deployment readiness score: "
            f"{recommendation_info['deployment_score']}/100."
        )

        summary.append(
            f"Overall project status: "
            f"{recommendation_info['overall_status']}."
        )

        summary.append(
            "Recommended next steps:"
        )

        for item in recommendation_info["recommendations"]:

            summary.append(f"• {item}")

        # =====================================================
        # Return
        # =====================================================

        return {

            "title": "📋 Executive Summary",

            "status": "success",

            "summary": summary,

            "message": "\n\n".join(summary)

        }