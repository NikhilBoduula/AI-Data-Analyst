class RecommendationIntelligence:

    @staticmethod
    def analyze(
        dataset_info,
        quality_info,
        model_info,
        explainability_info
    ):

        score = 100

        recommendations = []

        # =====================================================
        # Dataset Quality
        # =====================================================

        if quality_info["missing_values"] > 0:

            score -= 20

            recommendations.append(
                "Handle missing values before deployment."
            )

        if quality_info["duplicate_rows"] > 0:

            score -= 10

            recommendations.append(
                "Remove duplicate records."
            )

        # =====================================================
        # Model Availability
        # =====================================================

        if model_info["best_model"] is None:

            score -= 30

            recommendations.append(
                "Run AutoML to identify the best model."
            )

        # =====================================================
        # Explainability
        # =====================================================

        if not explainability_info["analysis_completed"]:

            score -= 20

            recommendations.append(
                "Generate SHAP explanations before deployment."
            )

        # =====================================================
        # Dataset Size
        # =====================================================

        if dataset_info["rows"] < 100:

            score -= 10

            recommendations.append(
                "Collect more training samples to improve model reliability."
            )

        # =====================================================
        # Overall Rating
        # =====================================================

        score = max(score, 0)

        if score >= 90:

            rating = "★★★★★"

            status = "Excellent"

        elif score >= 75:

            rating = "★★★★☆"

            status = "Good"

        elif score >= 60:

            rating = "★★★☆☆"

            status = "Fair"

        else:

            rating = "★★☆☆☆"

            status = "Needs Improvement"

        # =====================================================
        # Default Recommendation
        # =====================================================

        if len(recommendations) == 0:

            recommendations.append(
                "The project is ready for deployment."
            )

        # =====================================================
        # Return Intelligence
        # =====================================================

        return {

            "title": "🎯 Deployment Recommendation",

            "status": "success",

            "deployment_score": score,

            "rating": rating,

            "overall_status": status,

            "recommendations": recommendations,

            "message": (

                f"Deployment Readiness : {score}/100\n\n"

                f"Overall Status : {status}\n"

                f"Rating : {rating}\n\n"

                "Recommendations\n\n"

                + "\n".join(
                    f"• {item}"
                    for item in recommendations
                )

            )

        }