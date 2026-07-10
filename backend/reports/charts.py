import os

import matplotlib.pyplot as plt


class ChartGenerator:

    @staticmethod
    def save_histograms(df, output_dir="backend/reports/assets"):

        os.makedirs(output_dir, exist_ok=True)

        image_paths = []

        numeric_columns = df.select_dtypes(include="number").columns

        for column in numeric_columns:

            plt.figure(figsize=(5, 3))

            df[column].hist(bins=20)

            plt.title(column)

            plt.tight_layout()

            path = os.path.join(output_dir, f"{column}.png")

            plt.savefig(path)

            plt.close()

            image_paths.append(path)

        return image_paths