import matplotlib.pyplot as plt
import shap


class SHAPPlots:

    @staticmethod
    def bar_plot(shap_values):

        plt.clf()

        shap.plots.bar(
            shap_values,
            show=False
        )

        fig = plt.gcf()

        return fig

    @staticmethod
    def summary_plot(shap_values):

        plt.clf()

        shap.plots.beeswarm(
            shap_values,
            show=False
        )

        fig = plt.gcf()

        return fig