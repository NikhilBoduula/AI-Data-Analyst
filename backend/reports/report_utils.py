from datetime import datetime


class ReportUtils:

    @staticmethod
    def generate_dataset_summary(df):

        return {
            "Rows": df.shape[0],
            "Columns": df.shape[1],
            "Memory Usage (KB)": round(df.memory_usage(deep=True).sum() / 1024, 2),
            "Duplicate Rows": int(df.duplicated().sum())
        }

    @staticmethod
    def generate_missing_summary(df):

        missing = df.isnull().sum()

        return {
            col: int(count)
            for col, count in missing.items()
            if count > 0
        }

    @staticmethod
    def generate_column_summary(df):

        columns = []

        for col in df.columns:

            columns.append({
                "Column": col,
                "Type": str(df[col].dtype),
                "Missing": int(df[col].isnull().sum()),
                "Unique": int(df[col].nunique())
            })

        return columns

    @staticmethod
    def generate_model_summary(model_results):

        """
        model_results example:

        {
            "Random Forest":{
                "Accuracy":0.96
            },
            "XGBoost":{
                "Accuracy":0.95
            }
        }
        """

        summary = []

        if not model_results:
            return summary

        for model, metrics in model_results.items():

            row = {
                "Model": model
            }

            row.update(metrics)

            summary.append(row)

        return summary

    @staticmethod
    def generate_feature_summary(feature_importance):

        """
        feature_importance example

        {
            "Age":0.42,
            "Salary":0.25,
            "Experience":0.19
        }
        """

        if not feature_importance:
            return {}

        sorted_features = dict(
            sorted(
                feature_importance.items(),
                key=lambda x: x[1],
                reverse=True
            )
        )

        return sorted_features

    @staticmethod
    def generate_report_data(
        df,
        model_results=None,
        best_model=None,
        feature_importance=None,
        business_insights=""
    ):

        return {

            "generated_at": datetime.now().strftime("%d-%m-%Y %H:%M"),

            "dataset": ReportUtils.generate_dataset_summary(df),

            "missing": ReportUtils.generate_missing_summary(df),

            "columns": ReportUtils.generate_column_summary(df),

            "models": ReportUtils.generate_model_summary(model_results),

            "best_model": best_model if best_model else {},

            "feature_importance": ReportUtils.generate_feature_summary(feature_importance),

            "business_insights": business_insights
        }