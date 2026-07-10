class BusinessAgent:

    # =====================================================
    # DATASET ANALYZER
    # =====================================================

    @staticmethod
    def analyze_dataset(dataset):

        rows, cols = dataset.shape

        if rows < 1000:
            size = "Small Dataset"
            observation = (
                "This dataset is suitable for experimentation "
                "and rapid model development."
            )

        elif rows < 10000:
            size = "Medium Dataset"
            observation = (
                "This dataset is sufficiently large for reliable "
                "machine learning analysis."
            )

        else:
            size = "Large Dataset"
            observation = (
                "This dataset is large enough for production-scale "
                "machine learning."
            )

        numeric = len(
            dataset.select_dtypes(include="number").columns
        )

        categorical = len(
            dataset.select_dtypes(exclude="number").columns
        )

        return {

            "title": "📁 Dataset Overview",

            "message":

                f"Rows : {rows:,}\n"

                f"Columns : {cols}\n"

                f"Dataset Size : {size}\n\n"

                f"Numeric Columns : {numeric}\n"

                f"Categorical Columns : {categorical}\n\n"

                f"{observation}"

        }

    # =====================================================
    # DATA QUALITY ANALYZER
    # =====================================================

    @staticmethod
    def analyze_quality(dataset):

        missing = int(
            dataset.isnull().sum().sum()
        )

        duplicates = int(
            dataset.duplicated().sum()
        )

        score = 100

        if missing > 0:
            score -= min(missing, 40)

        if duplicates > 0:
            score -= min(duplicates, 20)

        if score >= 90:
            status = "Excellent"

        elif score >= 75:
            status = "Good"

        elif score >= 60:
            status = "Fair"

        else:
            status = "Poor"

        recommendations = []

        if missing > 0:

            recommendations.append(
                "Handle missing values before training."
            )

        if duplicates > 0:

            recommendations.append(
                "Remove duplicate rows."
            )

        if len(recommendations) == 0:

            recommendations.append(
                "Dataset quality is excellent."
            )

        recommendation_text = "\n".join(
            f"• {item}"
            for item in recommendations
        )

        return {

            "title": "📊 Data Quality",

            "message":

                f"Health Score : {score}/100\n\n"

                f"Status : {status}\n\n"

                f"Missing Values : {missing}\n"

                f"Duplicate Rows : {duplicates}\n\n"

                f"Recommendations\n"

                f"{recommendation_text}"

        }
        
            # =====================================================
            # MODEL PERFORMANCE ANALYZER
            # =====================================================

    @staticmethod
    def analyze_models(automl_results):

        if automl_results is None:

            return {

                "title": "🤖 Model Performance",

                "message": "Run AutoML to generate model insights."

            }

        leaderboard = automl_results["leaderboard"]

        best = automl_results["best_model"]

        metric = automl_results["metric"]

        message = (

            f"Models Evaluated : {len(leaderboard)}\n\n"

            f"Best Model : {best['Model']}\n"

            f"{metric} : {round(best[metric],4)}\n\n"

            "Top Models\n\n"

        )

        for index, model in enumerate(leaderboard[:3], start=1):

            message += (

                f"{index}. "

                f"{model['Model']} "

                f"({round(model[metric],4)})\n"

            )

        return {

            "title": "🤖 Model Performance",

            "message": message

        }

    # =====================================================
    # SHAP ANALYZER
    # =====================================================

    @staticmethod
    def analyze_shap(shap_results):

        if shap_results is None:

            return {

                "title": "🧠 Explainability",

                "message":

                    "SHAP analysis has not been generated yet."

            }

        return {

            "title": "🧠 Explainability",

            "message":

                "SHAP feature importance analysis completed successfully.\n\n"

                "Use the Explainability page to understand "

                "which features influence predictions."

        }

    # =====================================================
    # DEPLOYMENT RECOMMENDATION
    # =====================================================

    @staticmethod
    def generate_recommendation(

        dataset,

        automl_results,

        shap_results

    ):

        score = 100

        if dataset.isnull().sum().sum() > 0:

            score -= 20

        if dataset.duplicated().sum() > 0:

            score -= 10

        if automl_results is None:

            score -= 30

        if shap_results is None:

            score -= 20

        if score >= 90:

            level = "★★★★★ Excellent"

        elif score >= 75:

            level = "★★★★☆ Good"

        elif score >= 60:

            level = "★★★☆☆ Fair"

        else:

            level = "★★☆☆☆ Needs Improvement"

        return {

            "title": "🎯 Deployment Recommendation",

            "message":

                f"Deployment Readiness : {score}/100\n\n"

                f"Overall Status : {level}\n\n"

                "Recommendation\n\n"

                "Complete all pipeline stages before "

                "deploying the model into production."

        }

    # =====================================================
    # GENERATE COMPLETE BUSINESS REPORT
    # =====================================================

    @staticmethod
    def generate(

        dataset,

        automl_results=None,

        shap_results=None

    ):

        insights = [

            BusinessAgent.analyze_dataset(

                dataset

            ),

            BusinessAgent.analyze_quality(

                dataset

            ),

            BusinessAgent.analyze_models(

                automl_results

            ),

            BusinessAgent.analyze_shap(

                shap_results

            ),

            BusinessAgent.generate_recommendation(

                dataset,

                automl_results,

                shap_results

            )

        ]

        return insights