import pandas as pd


class VisualizationAgent:

    @staticmethod
    def recommend(df, chart_type, selected_column=None):

        recommendation = {
            "recommended_chart": chart_type,
            "reason": "",
            "confidence": 100,
            "detected_type": "",
            "column": selected_column
        }

        # --------------------------------------------------
        # Scatter Plot
        # --------------------------------------------------

        if chart_type == "Scatter Plot":

            recommendation["recommended_chart"] = "📈 Scatter Plot"
            recommendation["detected_type"] = "Numeric vs Numeric"
            recommendation["reason"] = (
                "Both selected columns are numeric. "
                "Scatter plots are excellent for discovering relationships, "
                "correlations and trends."
            )

            return recommendation

        # --------------------------------------------------
        # Correlation Heatmap
        # --------------------------------------------------

        if chart_type == "Correlation Heatmap":

            recommendation["recommended_chart"] = "🔥 Correlation Heatmap"
            recommendation["detected_type"] = "Multiple Numeric Features"
            recommendation["reason"] = (
                "Correlation heatmaps reveal relationships among all numeric "
                "features and help identify multicollinearity."
            )

            return recommendation

        # --------------------------------------------------
        # Column-based recommendation
        # --------------------------------------------------

        if selected_column is None:
            return recommendation

        dtype = df[selected_column].dtype

        if pd.api.types.is_numeric_dtype(dtype):

            recommendation["detected_type"] = "Numeric"

            if chart_type == "Histogram":
                recommendation["recommended_chart"] = "📊 Histogram"
                recommendation["reason"] = (
                    "This numeric feature is best explored using a histogram "
                    "to understand its distribution and identify skewness."
                )

            elif chart_type == "Box Plot":
                recommendation["recommended_chart"] = "📦 Box Plot"
                recommendation["reason"] = (
                    "Box plots clearly reveal outliers and summarize the "
                    "distribution using quartiles."
                )

        else:

            recommendation["detected_type"] = "Categorical"

            if chart_type == "Bar Chart":
                recommendation["recommended_chart"] = "📊 Bar Chart"
                recommendation["reason"] = (
                    "Bar charts compare category frequencies clearly."
                )

            elif chart_type == "Pie Chart":
                recommendation["recommended_chart"] = "🥧 Pie Chart"
                recommendation["reason"] = (
                    "Pie charts are useful for displaying category proportions."
                )

        return recommendation