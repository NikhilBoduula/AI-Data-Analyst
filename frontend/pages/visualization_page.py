import streamlit as st

from frontend.ui.hero import hero
from backend.visualization.plotly_service import PlotlyService
from backend.agents.visualization_agent import VisualizationAgent


def render_visualization_page():
    hero(
        "Visualization Studio",
        "Interactive AI-Powered Data Visualization"
    )

    if st.session_state.get("dataset") is None:
        st.warning("⚠️ Upload a dataset first.")
        return

    df = st.session_state["dataset"]

    # Mark visualization as completed for workflow tracking
    st.session_state["charts"] = True

    # =====================================================
    # Dataset Summary
    # =====================================================
    st.markdown("## 📊 Dataset Summary")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Rows", f"{df.shape[0]:,}")
    col2.metric("Columns", df.shape[1])
    col3.metric(
        "Numeric Columns",
        len(df.select_dtypes(include="number").columns)
    )
    col4.metric(
        "Categorical Columns",
        len(df.select_dtypes(exclude="number").columns)
    )

    st.divider()

    # =====================================================
    # Visualization Controls
    # =====================================================
    st.markdown("## 🎨 Visualization Controls")

    numeric_columns = df.select_dtypes(include="number").columns.tolist()
    categorical_columns = df.select_dtypes(exclude="number").columns.tolist()

    chart_type = st.selectbox(
        "Select Visualization Type",
        [
            "Histogram",
            "Box Plot",
            "Scatter Plot",
            "Bar Chart",
            "Pie Chart",
            "Correlation Heatmap",
        ]
    )

    # =====================================================
    # Interactive Charts
    # =====================================================
    st.markdown("## 📈 Interactive Visualization")

    fig = None
    selected_column = None
    x = None
    y = None

    # -------------------------------
    # Histogram
    # -------------------------------
    if chart_type == "Histogram" and numeric_columns:
        column = st.selectbox(
            "Numeric Column",
            numeric_columns,
            key="viz_histogram"
        )
        fig = PlotlyService.histogram(df, column)
        selected_column = column

    # -------------------------------
    # Box Plot
    # -------------------------------
    elif chart_type == "Box Plot" and numeric_columns:
        column = st.selectbox(
            "Numeric Column",
            numeric_columns,
            key="viz_boxplot"
        )
        fig = PlotlyService.boxplot(df, column)
        selected_column = column

    # -------------------------------
    # Scatter Plot
    # -------------------------------
    elif chart_type == "Scatter Plot" and len(numeric_columns) >= 2:
        x = st.selectbox(
            "X Axis",
            numeric_columns,
            key="viz_scatter_x"
        )
        y = st.selectbox(
            "Y Axis",
            numeric_columns,
            index=1 if len(numeric_columns) > 1 else 0,
            key="viz_scatter_y"
        )
        fig = PlotlyService.scatter_plot(df, x, y)
        selected_column = f"{x} vs {y}"

    # -------------------------------
    # Bar Chart
    # -------------------------------
    elif chart_type == "Bar Chart" and categorical_columns:
        column = st.selectbox(
            "Categorical Column",
            categorical_columns,
            key="viz_bar"
        )
        fig = PlotlyService.bar_chart(df, column)
        selected_column = column

    # -------------------------------
    # Pie Chart
    # -------------------------------
    elif chart_type == "Pie Chart" and categorical_columns:
        column = st.selectbox(
            "Categorical Column",
            categorical_columns,
            key="viz_pie"
        )
        fig = PlotlyService.pie_chart(df, column)
        selected_column = column

    # -------------------------------
    # Correlation Heatmap
    # -------------------------------
    elif chart_type == "Correlation Heatmap":
        corr = df.select_dtypes(include="number").corr()

        if len(corr.columns) > 1:
            fig = PlotlyService.correlation_heatmap(corr)
            selected_column = "All Numeric Columns"
        else:
            st.info("Need at least two numeric columns for correlation heatmap.")

    # Display the chart
    if fig is not None:
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Please select a valid chart type and ensure you have the required column types.")

    # =====================================================
    # AI Recommendation
    # =====================================================
    st.divider()
    st.markdown("## 🤖 AI Recommendation")

    if fig is not None and selected_column is not None:
        recommendation = VisualizationAgent.recommend(
            df=df,
            chart_type=chart_type,
            selected_column=selected_column
        )

        with st.container(border=True):
            st.success(f"### {recommendation.get('recommended_chart', chart_type)}")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Detected Type",
                    recommendation.get("detected_type", chart_type)
                )

            with col2:
                st.metric(
                    "Confidence",
                    f"{recommendation.get('confidence', 0)}%"
                )

            st.info(f"**Selected:** {recommendation.get('column', selected_column)}")

            st.write(recommendation.get("reason", "No additional insight available."))
    else:
        st.info("Generate a visualization first to get AI recommendations.")

    # =====================================================
    # Export Visualization
    # =====================================================
    if fig is not None:
        st.divider()
        st.markdown("## 📥 Export Visualization")

        html = fig.to_html(include_plotlyjs="cdn")

        st.download_button(
            "⬇️ Download Interactive HTML",
            data=html,
            file_name=f"{chart_type.lower().replace(' ', '_')}_visualization.html",
            mime="text/html",
        )