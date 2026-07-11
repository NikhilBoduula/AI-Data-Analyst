class DecisionAgent:

    @staticmethod
    def decide(
        dataset_info,
        quality_info,
        model_info,
        explainability_info,
        recommendation_info
    ):

        decisions = []

        # =====================================================
        # Data Cleaning
        # =====================================================

        if (
            quality_info.get("missing_values", 0) > 0
            or quality_info.get("duplicate_rows", 0) > 0
        ):

            decisions.append({

                "step": "🧹 Data Cleaning",

                "decision": "Proceed",

                "priority": "High",

                "confidence": 98,

                "impact": "Improves data quality before model training.",

                "reason": "Missing values or duplicate records were detected."

            })

        else:

            decisions.append({

                "step": "🧹 Data Cleaning",

                "decision": "Skip",

                "priority": "Low",

                "confidence": 100,

                "impact": "Dataset is already clean.",

                "reason": "No missing values or duplicate records were found."

            })

        # =====================================================
        # Feature Engineering
        # =====================================================

        if dataset_info.get("numeric_columns", 0) >= 2:

            decisions.append({

                "step": "🛠 Feature Engineering",

                "decision": "Proceed",

                "priority": "Medium",

                "confidence": 90,

                "impact": "May improve model performance and predictive power.",

                "reason": "Multiple numeric features are available for transformation."

            })

        else:

            decisions.append({

                "step": "🛠 Feature Engineering",

                "decision": "Optional",

                "priority": "Low",

                "confidence": 75,

                "impact": "Limited opportunity for feature engineering.",

                "reason": "Few numeric features were detected."

            })

        # =====================================================
        # AutoML
        # =====================================================

        if model_info.get("best_model") is None:

            decisions.append({

                "step": "🤖 AutoML",

                "decision": "Run",

                "priority": "High",

                "confidence": 100,

                "impact": "Training models is required before evaluation.",

                "reason": "No trained model is available."

            })

        else:

            decisions.append({

                "step": "🤖 AutoML",

                "decision": "Completed",

                "priority": "Low",

                "confidence": 100,

                "impact": "The best model has already been selected.",

                "reason": f"Best model: {model_info['best_model']}"

            })

        # =====================================================
        # Explainability
        # =====================================================

        if explainability_info.get("analysis_completed"):

            decisions.append({

                "step": "🧠 Explainability",

                "decision": "Completed",

                "priority": "Low",

                "confidence": 100,

                "impact": "Model predictions can be interpreted.",

                "reason": "SHAP analysis has been completed."

            })

        else:

            decisions.append({

                "step": "🧠 Explainability",

                "decision": "Generate",

                "priority": "Medium",

                "confidence": 95,

                "impact": "Explainability improves trust in model predictions.",

                "reason": "SHAP analysis has not been generated."

            })

        # =====================================================
        # Deployment
        # =====================================================

        score = recommendation_info.get("deployment_score", 0)

        if score >= 90:

            decision = "Deploy"
            priority = "Low"
            confidence = 98
            impact = "The solution is production-ready."

        elif score >= 75:

            decision = "Review"
            priority = "Medium"
            confidence = 85
            impact = "Minor improvements are recommended before deployment."

        else:

            decision = "Block"
            priority = "High"
            confidence = 95
            impact = "Deployment should be delayed until critical issues are resolved."

        decisions.append({

            "step": "🚀 Deployment",

            "decision": decision,

            "priority": priority,

            "confidence": confidence,

            "impact": impact,

            "reason": f"Deployment readiness score: {score}/100"

        })

        return decisions