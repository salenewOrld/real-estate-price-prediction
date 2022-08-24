from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
import mlflow
import yaml
import pandas as pd
import sys
import joblib
def evaluate(model, test_features, test_labels):
    predictions = model.predict(test_features)
    errors = abs(predictions - test_labels)
    mape = 100 * np.mean(errors / test_labels)
    accuracy = 100 - mape
    print('Model Performance')
    print('Average Error: {:0.4f} degrees.'.format(np.mean(errors)))
    print('Accuracy = {:0.2f}%.'.format(accuracy))
    
    return accuracy
# Create the parameter grid based on the results of random search 
with open('/usr/src/volume/volume/configs/experiment_regressor.yaml', 'r') as yaml_file:
    cfg = yaml.load(yaml_file, Loader=yaml.FullLoader)
df = pd.read_csv('/usr/src/volume/volume/done-etl-data/train.csv')
x = df[cfg['x']]
y = df[cfg['y']]
train_features, test_features, train_labels, test_labels = train_test_split(x, y, test_size=0.3, random_state=66)


param_grid = {
    'bootstrap': [True],
    'max_depth': [80, 90, 100, 110],
    'max_features': [2, 3, 10, 20, 30, 40, 50, 60, 70, 81],
    'min_samples_leaf': [3, 4, 5],
    'min_samples_split': [8, 10, 12],
    'n_estimators': [100, 200, 300, 1000]
}
logged_model = '/usr/src/volume/volume/models/RandomForestRegressor/model.pkl'
# Create a based model
model = joblib.load(logged_model)
# Instantiate the grid search model
grid_search = GridSearchCV(estimator = model, param_grid = param_grid, 
                          cv = 3, n_jobs = -1, verbose = 2)

grid_search.fit(train_features, train_labels)
print(grid_search.best_params_)


best_grid = grid_search.best_estimator_
grid_accuracy = evaluate(best_grid, test_features, test_labels)

print(grid_accuarcy)


