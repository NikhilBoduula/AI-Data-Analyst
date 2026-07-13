import plotly.express as px
import plotly.graph_objects as go


class PlotlyService:

    @staticmethod
    def histogram(df, column):

        return px.histogram(
            df,
            x=column,
            nbins=30,
            title=f"Distribution of {column}"
        )

    @staticmethod
    def boxplot(df, column):

        return px.box(
            df,
            y=column,
            title=f"Boxplot of {column}"
        )

    @staticmethod
    def scatter_plot(df, x_column, y_column):

        return px.scatter(
            df,
            x=x_column,
            y=y_column,
            title=f"{x_column} vs {y_column}"
        )

    @staticmethod
    def bar_chart(df, column):

        counts = (

            df[column]

            .value_counts()

            .head(20)

            .reset_index()

        )

        counts.columns = [column, "Count"]

        return px.bar(

            counts,

            x=column,

            y="Count",

            title=f"Top 20 {column}"

        )

    @staticmethod
    def pie_chart(df, column):

        counts = df[column].value_counts()

        top = counts.head(10)

        others = counts.iloc[10:].sum()

        if others > 0:

            top["Others"] = others

        pie = top.reset_index()

        pie.columns = [column, "Count"]

        return px.pie(

            pie,

            names=column,

            values="Count",

            title=f"Top 10 {column}"

        )

    @staticmethod
    def correlation_heatmap(corr):

        fig = go.Figure(

            data=go.Heatmap(

                z=corr.values,

                x=corr.columns,

                y=corr.columns,

                colorscale="Viridis"

            )

        )

        fig.update_layout(

            title="Correlation Heatmap"

        )

        return fig