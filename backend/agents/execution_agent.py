class ExecutionAgent:

    @staticmethod
    def execute(
        quality_info,
        model_info,
        explainability_info,
        recommendation_info,
    ):

        actions = []

        # ============================================
        # Data Cleaning
        # ============================================

        if quality_info["missing_values"] > 0:

            actions.append({

                "task": "Handle Missing Values",

                "status": "Suggested",

                "description":
                "Fill or remove missing values before training."

            })

        if quality_info["duplicate_rows"] > 0:

            actions.append({

                "task": "Remove Duplicate Rows",

                "status": "Suggested",

                "description":
                "Duplicate rows should be removed."

            })

        # ============================================
        # AutoML
        # ============================================

        if model_info["best_model"] is None:

            actions.append({

                "task": "Run AutoML",

                "status": "Suggested",

                "description":
                "Train machine learning models."

            })

        # ============================================
        # Explainability
        # ============================================

        if not explainability_info["analysis_completed"]:

            actions.append({

                "task": "Generate SHAP",

                "status": "Suggested",

                "description":
                "Generate feature importance analysis."

            })

        # ============================================
        # Deployment
        # ============================================

        if recommendation_info["deployment_score"] >= 90:

            actions.append({

                "task": "Deploy Model",

                "status": "Ready",

                "description":
                "The project is ready for deployment."

            })

        else:

            actions.append({

                "task": "Improve Pipeline",

                "status": "Pending",

                "description":
                "Resolve recommendations before deployment."

            })

        return {

            "title": "⚙️ Execution Agent",

            "actions": actions

        }