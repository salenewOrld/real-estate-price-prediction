from sklearn.linear_model import LinearRegression
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import SGDRegressor
from sklearn.linear_model import BayesianRidge
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.kernel_ridge import KernelRidge
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from etl import ETL
import pandas as pd
import wandb
class ModelComparison:
    def __init__(self):
        self.etl = ETL('train.csv')
        self.model = ['LinearRegression', 'ElasticNet', 'SGDRegressor', 'BayesianRidge', 'GradientBoostingRegressor', 'SVR', 'KernelRidge', 'RandomForestRegressor']
        self.r2 = []
        self.mae = []
        self.mse = []
        self.data = {
            'models': self.model,
            'r2' : self.r2,
            'mae' : self.mae,
            'mse' : self.mse
        }
    def split_data(self):
        df = self.etl.run()
        df = df.reset_index()
        df_x = df[['Id',
 'MSSubClass',
 'MSZoning',
 'LotArea',
 'Street',
 'Alley',
 'LotShape',
 'LandContour',
 'Utilities',
 'LotConfig',
 'LandSlope',
 'Neighborhood',
 'Condition1',
 'Condition2',
 'BldgType',
 'HouseStyle',
 'OverallQual',
 'OverallCond',
 'YearBuilt',
 'YearRemodAdd',
 'RoofStyle',
 'RoofMatl',
 'Exterior1st',
 'Exterior2nd',
 'MasVnrType',
 'MasVnrArea',
 'ExterQual',
 'ExterCond',
 'Foundation',
 'BsmtQual',
 'BsmtCond',
 'BsmtExposure',
 'BsmtFinType1',
 'BsmtFinSF1',
 'BsmtFinType2',
 'BsmtFinSF2',
 'BsmtUnfSF',
 'TotalBsmtSF',
 'Heating',
 'HeatingQC',
 'CentralAir',
 'Electrical',
 '1stFlrSF',
 '2ndFlrSF',
 'LowQualFinSF',
 'GrLivArea',
 'BsmtFullBath',
 'BsmtHalfBath',
 'FullBath',
 'HalfBath',
 'BedroomAbvGr',
 'KitchenAbvGr',
 'KitchenQual',
 'TotRmsAbvGrd',
 'Functional',
 'Fireplaces',
 'FireplaceQu',
 'GarageType',
 'GarageYrBlt',
 'GarageFinish',
 'GarageCars',
 'GarageArea',
 'GarageQual',
 'GarageCond',
 'PavedDrive',
 'WoodDeckSF',
 'OpenPorchSF',
 'EnclosedPorch',
 '3SsnPorch',
 'ScreenPorch',
 'PoolArea',
 'PoolQC',
 'Fence',
 'MiscFeature',
 'MiscVal',
 'MoSold',
 'YrSold',
 'SaleType',
 'SaleCondition']]
        df_y = df[['SalePrice']]
        self.df = df
        x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.3, random_state=66)
        scaler_x = StandardScaler()
        scaler_y = StandardScaler()
        x_train = scaler_x.fit_transform(x_train)
        x_test = scaler_x.transform(x_test)
        y_train = scaler_y.fit_transform(y_train)
        y_test = scaler_y.transform(y_test)
        return x_train, y_train, x_test, y_test
    def linear_reg(self, X_train, y_train, X_test, y_test):
        model = LinearRegression()
        model.fit(self.x_train, self.y_train)
        wandb.sklearn.plot_regressor(model, X_train, X_test, y_train, y_test,  model_name="Linear")
        self.r2.append(self.get_r2(model))
        self.mae.append(self.get_mae(model))
        self.mse.append(self.get_mse(model))
        return model
    def elasticnet(self, X_train, y_train, X_test, y_test):
        model = ElasticNet()
        model.fit(self.x_train, self.y_train)
        wandb.sklearn.plot_regressor(model, X_train, X_test, y_train, y_test,  model_name="ElasticNet")
        self.r2.append(self.get_r2(model))
        self.mae.append(self.get_mae(model))
        self.mse.append(self.get_mse(model))
    def sgd_reg(self, X_train, y_train, X_test, y_test):
        model = SGDRegressor()
        model.fit(self.x_train, self.y_train)
        wandb.sklearn.plot_regressor(reg, X_train, X_test, y_train, y_test,  model_name="SGD")
        self.r2.append(self.get_r2(model))
        self.mae.append(self.get_mae(model))
        self.mse.append(self.get_mse(model))
    def bayesian_ridge(self, X_train, y_train, X_test, y_test):
        model = BayesianRidge()
        model.fit(self.x_train, self.y_train)
        wandb.sklearn.plot_regressor(model, X_train, X_test, y_train, y_test,  model_name="BayesianRidge")
        self.r2.append(self.get_r2(model))
        self.mae.append(self.get_mae(model))
        self.mse.append(self.get_mse(model))
    def gbr(self, X_train, y_train, X_test, y_test):
        model = GradientBoostingRegressor()
        model.fit(self.x_train, self.y_train)
        wandb.sklearn.plot_regressor(model, X_train, X_test, y_train, y_test,  model_name="GradientBoosting")
        self.r2.append(self.get_r2(model))
        self.mae.append(self.get_mae(model))
        self.mse.append(self.get_mse(model))
    def svr(self, X_train, y_train, X_test, y_test):
        model = SVR()
        model.fit(self.x_train, self.y_train)
        wandb.sklearn.plot_regressor(model, X_train, X_test, y_train, y_test,  model_name="SVR")
        self.r2.append(self.get_r2(model))
        self.mae.append(self.get_mae(model))
        self.mse.append(self.get_mse(model))
    def kr(self, X_train, y_train, X_test, y_test):
        model = KernelRidge()
        model.fit(self.x_train, self.y_train)
        wandb.sklearn.plot_regressor(model, X_train, X_test, y_train, y_test,  model_name="KernelRidge")
        self.r2.append(self.get_r2(model))
        self.mae.append(self.get_mae(model))
        self.mse.append(self.get_mse(model))
    def rfg(self, X_train, y_train, X_test, y_test):
        model = RandomForestRegressor()
        model.fit(self.x_train, self.y_train)
        wandb.sklearn.plot_regressor(model, X_train, X_test, y_train, y_test,  model_name="RandomForest")
        self.r2.append(self.get_r2(model))
        self.mae.append(self.get_mae(model))
        self.mse.append(self.get_mse(model))
    def get_r2(self, model):
        y_pred = model.predict(self.x_test)
        return r2_score(self.y_test, y_pred)
    def get_mse(self, model):
        y_pred = model.predict(self.x_test)
        return mean_squared_error(self.y_test, y_pred)
    def get_mae(self, model):
        y_pred = model.predict(self.x_test)
        return mean_absolute_error(self.y_test, y_pred)
    def run(self):
        wandb.init(project="covid-prediction-")
        self.x_train, self.y_train, self.x_test, self.y_test = self.split_data()
        lr = self.linear_reg(self.x_train, self.y_train, self.x_test, self.y_test)
        en = self.elasticnet(self.x_train, self.y_train, self.x_test, self.y_test)
        sgdr = self.sgd_reg(self.x_train, self.y_train, self.x_test, self.y_test)
        br = self.bayesian_ridge(self.x_train, self.y_train, self.x_test, self.y_test)
        gbr = self.gbr(self.x_train, self.y_train, self.x_test, self.y_test)
        svr = self.svr(self.x_train, self.y_train, self.x_test, self.y_test)
        kr = self.kr(self.x_train, self.y_train, self.x_test, self.y_test)
        rfg = self.rfg(self.x_train, self.y_train, self.x_test, self.y_test)
        #result = pd.DataFrame.from_dict(self.data)
        #ßresult.sort_values(by='r2', ascending=False, inplace=True)
        return result, self.df