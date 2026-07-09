from sklearn.linear_model import (
    LinearRegression,
    Ridge,
    Lasso,
    ElasticNet,
    LogisticRegression
)

from sklearn.tree import (
    DecisionTreeRegressor,
    DecisionTreeClassifier
)

from sklearn.neighbors import (
    KNeighborsRegressor,
    KNeighborsClassifier
)

from sklearn.naive_bayes import GaussianNB

from sklearn.svm import (
    SVR,
    SVC
)

from sklearn.ensemble import (
    RandomForestRegressor,
    RandomForestClassifier,
    GradientBoostingRegressor,
    GradientBoostingClassifier,
    ExtraTreesRegressor,
    ExtraTreesClassifier,
    AdaBoostRegressor,
    AdaBoostClassifier
)


class Trainer:

    @staticmethod
    def regression_models():

        return {

            "Linear Regression": LinearRegression(),

            "Ridge": Ridge(),

            "Lasso": Lasso(),

            "ElasticNet": ElasticNet(),

            "Decision Tree": DecisionTreeRegressor(random_state=42),

            "Random Forest": RandomForestRegressor(random_state=42),

            "Extra Trees": ExtraTreesRegressor(random_state=42),

            "Gradient Boosting": GradientBoostingRegressor(random_state=42),

            "AdaBoost": AdaBoostRegressor(random_state=42),

            "KNN": KNeighborsRegressor(),

            "SVR": SVR()

        }

    @staticmethod
    def classification_models():

        return {

            "Logistic Regression": LogisticRegression(max_iter=1000),

            "Decision Tree": DecisionTreeClassifier(random_state=42),

            "Random Forest": RandomForestClassifier(random_state=42),

            "Extra Trees": ExtraTreesClassifier(random_state=42),

            "Gradient Boosting": GradientBoostingClassifier(random_state=42),

            "AdaBoost": AdaBoostClassifier(random_state=42),

            "KNN": KNeighborsClassifier(),

            "Naive Bayes": GaussianNB(),

            "SVC": SVC()

        }