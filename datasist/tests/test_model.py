
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier, GradientBoostingClassifier

from datasist.model import *

def test_multi_model_processing():
    x_train, y_train = make_classification(
        n_samples=50, 
        n_features=4,
        n_informative=2, 
        n_redundant=0, 
        random_state=0,
        shuffle=False
    )
    model_list = [
        RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0),
        BaggingClassifier(),
        GradientBoostingClassifier()
    ]
    scoring_metrics = ['accuracy']
    fitted_model, model_scores = multi_model_processing(model_list, x_train, y_train, True, scoring_metrics)