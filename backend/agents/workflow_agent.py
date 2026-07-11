class WorkflowAgent:

    @staticmethod
    def analyze(session_state):

        workflow = []

        stages = [

            ("📂 Dataset Upload", session_state.get("dataset") is not None),

            ("🧹 Data Cleaning", session_state.get("cleaned_dataset") is not None),

            ("📊 EDA", session_state.get("eda_results") is not None),

            ("📈 Visualization", session_state.get("charts") is not None),

            ("🛠 Feature Engineering", session_state.get("engineered_dataset") is not None),

            ("🤖 AutoML", session_state.get("automl_results") is not None),

            ("🧠 SHAP", session_state.get("shap_results") is not None),

            ("📄 Report", session_state.get("business_insights") is not None),

        ]

        next_step = "Project Completed 🎉"

        for name, completed in stages:

            workflow.append({

                "step": name,

                "status": "Completed" if completed else "Pending"

            })

            if not completed and next_step == "Project Completed 🎉":

                next_step = f"Proceed to {name}"

        return {

            "title": "🗺 Workflow Progress",

            "workflow": workflow,

            "next_step": next_step

        }