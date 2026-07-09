class RecommendationService:
    """
    Generates AI-like recommendations
    based on dataset quality.
    """

    @staticmethod
    def generate(report: dict):

        recommendations = []

        if report["Duplicate Rows"] > 0:

            recommendations.append(
                "Remove duplicate rows."
            )

        if report["Missing Values"] > 0:

            recommendations.append(
                "Fill missing values."
            )

        if len(recommendations) == 0:

            recommendations.append(
                "Dataset looks clean."
            )

        return recommendations