class PlanningAgent:

    @staticmethod
    def generate(session_state):

        plan = []

        pipeline = [

            (
                "📂 Upload Dataset",
                session_state.get("dataset") is not None
            ),

            (
                "🧹 Data Cleaning",
                session_state.get("cleaned_dataset") is not None
            ),

            (
                "📊 Exploratory Data Analysis",
                session_state.get("eda_results") is not None
            ),

            (
                "📈 Visualization",
                session_state.get("charts") is not None
            ),

            (
                "🛠 Feature Engineering",
                session_state.get("engineered_dataset") is not None
            ),

            (
                "🤖 AutoML Training",
                session_state.get("automl_results") is not None
            ),

            (
                "🧠 SHAP Explainability",
                session_state.get("shap_results") is not None
            ),

            (
                "💼 Business Intelligence",
                session_state.get("business_insights") is not None
            ),

            (
                "📄 Generate Report",
                session_state.get("business_insights") is not None
            )

        ]

        completed = 0

        for step, status in pipeline:

            if status:

                completed += 1

            plan.append({

                "step": step,

                "completed": status

            })

        progress = round(
            completed / len(pipeline) * 100,
            1
        )

        return {

            "title": "🧠 AI Execution Plan",

            "progress": progress,

            "completed": completed,

            "total": len(pipeline),

            "plan": plan

        }