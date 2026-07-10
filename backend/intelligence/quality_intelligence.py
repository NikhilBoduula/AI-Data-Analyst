import pandas as pd


class QualityIntelligence:

    @staticmethod
    def analyze(dataset: pd.DataFrame):

        # --------------------------------------------
        # Missing Values
        # --------------------------------------------

        missing_values = int(dataset.isnull().sum().sum())

        # --------------------------------------------
        # Duplicate Rows
        # --------------------------------------------

        duplicate_rows = int(dataset.duplicated().sum())

        # --------------------------------------------
        # Memory Usage
        # --------------------------------------------

        memory_usage = round(
            dataset.memory_usage(deep=True).sum() / 1024,
            2
        )

        # --------------------------------------------
        # Health Score
        # --------------------------------------------

        score = 100

        score -= min(missing_values, 40)
        score -= min(duplicate_rows, 20)

        score = max(score, 0)

        # --------------------------------------------
        # Status
        # --------------------------------------------

        if score >= 90:
            status = "Excellent"

        elif score >= 75:
            status = "Good"

        elif score >= 60:
            status = "Fair"

        else:
            status = "Poor"

        # --------------------------------------------
        # Recommendations
        # --------------------------------------------

        recommendations = []

        if missing_values > 0:
            recommendations.append(
                "Handle missing values before model training."
            )

        if duplicate_rows > 0:
            recommendations.append(
                "Remove duplicate records."
            )

        if not recommendations:
            recommendations.append(
                "Dataset quality is excellent."
            )

        # --------------------------------------------
        # Return Intelligence
        # --------------------------------------------

        return {

            "title": "📊 Data Quality Intelligence",

            "health_score": score,

            "status": status,

            "missing_values": missing_values,

            "duplicate_rows": duplicate_rows,

            "memory_usage": memory_usage,

            "recommendations": recommendations,

            "message": (

                f"Health Score : {score}/100\n\n"

                f"Status : {status}\n\n"

                f"Missing Values : {missing_values}\n"

                f"Duplicate Rows : {duplicate_rows}\n"

                f"Memory Usage : {memory_usage} KB\n\n"

                "Recommendations\n\n"

                + "\n".join(
                    f"• {item}"
                    for item in recommendations
                )

            )

        }