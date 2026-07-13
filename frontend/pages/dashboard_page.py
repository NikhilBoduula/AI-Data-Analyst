from frontend.ui.hero import hero
from frontend.ui.metric_card import metric_card
from frontend.ui.control_center import control_center
from frontend.ui.info_card import info_card
from frontend.ui.timeline import workflow_timeline

from backend.agents.planning_agent import PlanningAgent
from backend.agents.workflow_agent import WorkflowAgent

import streamlit as st


def render_dashboard_page():
    hero(
        "Autonomous AI Data Scientist",
        "AI Operating System • Multi-Agent Machine Learning Platform"
    )

    # Early return if no dataset is uploaded
    if st.session_state.get("dataset") is None:
        st.info("📂 Upload a dataset from the Upload Dataset page to begin.")
        return

    # =====================================================
    # MAIN DASHBOARD
    # =====================================================
    df = st.session_state["dataset"]
    dataset_name = st.session_state.get("dataset_name", "Unknown Dataset")
    automl = st.session_state.get("automl_results")

    # Control Center
    workflow = WorkflowAgent.analyze(st.session_state)
    plan = PlanningAgent.generate(st.session_state)

    # =====================================================
    # CONTROL CENTER + PIPELINE STATUS (First Layout)
    # =====================================================
    left, right = st.columns([1.3, 1])

    with left:
        control_center(
            progress=plan["progress"],
            next_step=workflow["next_step"]
        )

    with right:
        st.markdown("## 🚀 Pipeline Status")

        status = [
            ("📂 Dataset Uploaded", True),
            ("🧹 Data Cleaning", "cleaned_dataset" in st.session_state),
            ("📊 EDA", st.session_state.get("eda_results") is not None),
            ("📈 Visualization", True),
            ("🛠 Feature Engineering", True),
            ("🤖 AutoML", automl is not None),
            ("🧠 Explainability", st.session_state.get("shap_results") is not None),
            ("📄 Reports", True),
        ]

        with st.container(border=True):
            for name, completed in status:
                if completed:
                    st.success(f"✅ {name}")
                else:
                    st.warning(f"⏳ {name}")

    st.markdown("## 📊 Dataset Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        metric_card("Dataset", dataset_name, "📂")
    with col2:
        metric_card("Rows", f"{df.shape[0]:,}", "📄")
    with col3:
        metric_card("Columns", df.shape[1], "📊")
    with col4:
        metric_card(
            "Missing",
            int(df.isna().sum().sum()),
            "⚠️",
            "#EF4444"
        )

    # =====================================================
    # MODEL SUMMARY + DATA QUALITY
    # =====================================================

    left, right = st.columns(2)

    with left:
        if automl:
            best = automl["best_model"]
            metric = automl["metric"]

            info_card(
                "🤖 Model Summary",
                [
                    ("Task", automl["task"].title()),
                    ("Best Model", best["Model"]),
                    (metric, round(best[metric], 4)),
                    ("Models Tested", len(automl["leaderboard"]))
                ]
            )
        else:
            info_card(
                "🤖 Model Summary",
                [
                    ("Status", "Waiting"),
                    ("AutoML", "Not Run"),
                    ("Recommendation", "Run AutoML")
                ]
            )

    with right:
        info_card(
            "📊 Data Quality",
            [
                ("Duplicate Rows", int(df.duplicated().sum())),
                ("Numeric Columns", len(df.select_dtypes(include="number").columns)),
                ("Categorical Columns", len(df.select_dtypes(exclude="number").columns)),
                ("Memory (KB)", round(df.memory_usage(deep=True).sum()/1024, 2))
            ]
        )

    # =====================================================
    # DATASET EXPLORER
    # =====================================================

    with st.container(border=True):
        st.markdown("## 📋 Dataset Explorer")

        st.dataframe(
            df.head(20),
            use_container_width=True
        )

        with st.expander("Dataset Information"):
            st.write(f"Shape : {df.shape}")
            st.write("Columns:")
            st.write(df.columns.tolist())

    # =====================================================
    # WORKFLOW + EXECUTION
    # =====================================================

    left, right = st.columns(2)

    with left:
        workflow_timeline(workflow["workflow"])

    with right:
        with st.container(border=True):
            st.markdown("## 🧠 AI Execution Plan")

            st.progress(plan["progress"] / 100)

            st.caption(f"Completed {plan['completed']} of {plan['total']} stages")

            for step in plan["plan"]:
                if step["completed"]:
                    st.success(f"✅ {step['step']}")
                else:
                    st.info(f"⏳ {step['step']}")