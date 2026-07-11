from backend.agents.planning_agent import PlanningAgent
from backend.agents.workflow_agent import WorkflowAgent
import streamlit as st


def render_dashboard_page():
    st.title("🧠 Autonomous AI Data Scientist")
    st.caption("AI-Powered End-to-End Machine Learning Platform")
    st.divider()

    if st.session_state.get("dataset") is None:
        st.info(
            "📂 Upload a dataset from the Upload Dataset page to begin."
        )
        return

    df = st.session_state["dataset"]
    dataset_name = st.session_state.get(
        "dataset_name", "Unknown Dataset"
    )
    automl = st.session_state.get("automl_results")

    # =====================================================
    # DATASET SUMMARY
    # =====================================================
    st.subheader("📁 Dataset Summary")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Dataset", dataset_name)
    col2.metric("Rows", f"{df.shape[0]:,}")
    col3.metric("Columns", df.shape[1])
    col4.metric("Missing", int(df.isna().sum().sum()))

    st.divider()

    # =====================================================
    # MODEL SUMMARY
    # =====================================================
    st.subheader("🤖 Model Summary")

    if automl:
        best = automl["best_model"]
        metric = automl["metric"]

        c1, c2, c3 = st.columns(3)

        c1.metric("Task", automl["task"].title())
        c2.metric("Best Model", best["Model"])
        c3.metric(metric, round(best[metric], 4))
    else:
        st.info("Run AutoML to view model performance.")

    st.divider()

    # =====================================================
    # DATA QUALITY
    # =====================================================
    st.subheader("📊 Data Quality")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Duplicate Rows", int(df.duplicated().sum()))
    c2.metric(
        "Numeric Columns",
        len(df.select_dtypes(include="number").columns)
    )
    c3.metric(
        "Categorical Columns",
        len(df.select_dtypes(exclude="number").columns)
    )

    memory = round(df.memory_usage(deep=True).sum() / 1024, 2)
    c4.metric("Memory (KB)", memory)

    st.divider()

    # =====================================================
    # PIPELINE STATUS
    # =====================================================
    st.subheader("🚀 Pipeline Status")

    status = [
        ("Dataset Uploaded", st.session_state.get("dataset") is not None),
        ("Data Cleaning", "cleaned_dataset" in st.session_state),
        ("EDA", st.session_state.get("eda_results") is not None),
        ("Visualization", True),
        ("Feature Engineering", True),
        ("AutoML", automl is not None),
        ("Explainability", st.session_state.get("shap_results") is not None),
        ("Reports", True),
    ]

    for name, completed in status:
        if completed:
            st.success(f"✅ {name}")
        else:
            st.warning(f"⏳ {name}")

    st.divider()

    # =====================================================
    # DATA PREVIEW
    # =====================================================
    st.subheader("📋 Dataset Preview")

    st.dataframe(df.head(10), use_container_width=True)

    with st.expander("Dataset Information"):
        st.write(f"Shape : {df.shape}")
        st.write("Columns:")
        st.write(df.columns.tolist())

    st.divider()

    # =====================================================
    # WORKFLOW PROGRESS
    # =====================================================
    st.subheader("🗺 Workflow Progress")

    workflow = WorkflowAgent.analyze(st.session_state)

    for stage in workflow["workflow"]:
        if stage["status"] == "Completed":
            st.success(f"✅ {stage['step']}")
        else:
            st.info(f"⏳ {stage['step']}")

    st.divider()

    st.info(f"➡ Next Step: {workflow['next_step']}")

    # =====================================================
    # AI EXECUTION PLAN
    # =====================================================
    st.divider()

    st.subheader("🧠 AI Execution Plan")

    plan = PlanningAgent.generate(st.session_state)

    st.progress(plan["progress"] / 100)

    st.write(f"### Progress: {plan['progress']}%")
    st.caption(f"Completed {plan['completed']} of {plan['total']} stages")

    for step in plan["plan"]:
        if step["completed"]:
            st.success(f"✅ {step['step']}")
        else:
            st.info(f"⏳ {step['step']}")