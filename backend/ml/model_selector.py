class ModelSelector:

    @staticmethod
    def best(results, metric):

        return max(
            results,
            key=lambda x: x[metric]
        )