import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
class ETL:
    def __init__(self, _file_path):
        self._file_path = "/usr/src/volume/volume/datasets/" + _file_path
        self.df = self.get_df(self._file_path)
    def get_df(self, PATH):
        return pd.read_csv(PATH)
    def drop_columns(self, df):
        columns = ['LotFrontage']
        df.drop(columns[0], axis=1, inplace=True)
        return df
    def fill_na(self, df):
        df.replace([np.inf, -np.inf], np.nan, inplace=True)
        df['Alley'] = df['Alley'].fillna('NA')
        df['BsmtQual'] = df['BsmtQual'].fillna('NA')
        df['BsmtCond'] = df['BsmtCond'].fillna('NA')
        df['BsmtExposure'] = df['BsmtExposure'].fillna('NA')
        df['BsmtFinType1'] = df['BsmtFinType1'].fillna('NA')
        df['BsmtFinType2'] = df['BsmtFinType2'].fillna('NA')
        df['GarageType'] = df['GarageType'].fillna('NA')
        df['GarageYrBlt'] = df['GarageYrBlt'].fillna('NA')
        df['GarageFinish'] = df['GarageFinish'].fillna('NA')
        df['GarageQual'] = df['GarageQual'].fillna('NA')
        df['GarageCond'] = df['GarageCond'].fillna('NA')
        df['FireplaceQu'] = df['FireplaceQu'].fillna('NA')
        df['PoolQC'] = df['PoolQC'].fillna('NA')
        df['Fence'] = df['Fence'].fillna('NA')
        df['MiscFeature'] = df['MiscFeature'].fillna('NA')
        return df
    def drop_na(self, df):
        df.dropna(inplace=True)
        df = df.reset_index()
        return df
    def transform(self, df):
        columns = self.get_object_columns(df)
        for j in columns:
            print(f'|Transform| => Transforming column: {j}')
            cv = CountVectorizer()
            vector = cv.fit_transform(df[j])
            item = cosine_similarity(vector)
            df[j] = item.tolist()[2]
        df['CentralAir'] = df['CentralAir'].map({
            "Y" : 1,
            "N" : 0
        })
        df['PavedDrive'] = df['PavedDrive'].map({
            "Y" : 1,
            "N" : 0,
            "P" : 2
        })
        df['GarageYrBlt'] = df['GarageYrBlt'].map({
            "NA" : 0
        })
        return df
    def get_object_columns(self, df):
        dtypes = df.dtypes.to_dict()
        columns = list()
        for k, v in dtypes.items():
            if str(type(v)) == "<class 'numpy.dtype[object_]'>":
                
                columns.append(k)
        #print(columns)
        self.columns = columns
        return columns
    def convert_type(self, df):
        for j in df.columns.to_list():
            print(f"|Convert| => Column: {j}")
            df[j] = df[j].astype(float)
        return df
    def mapping_data(self, df):
        self.columns = self.get_object_columns(df)
        for j in self.columns:
            unique_vals = df[j].unique()
            df[j].replace(to_replace=unique_vals,
           value= list(range(len(unique_vals))),
           inplace=True)
        return df
    def run(self):
        df = self.drop_columns(self.df)
        df = self.fill_na(self.df)
        df = self.drop_na(df)
        df = self.mapping_data(df)
        #df = self.transform(df)
        #df = self._truly_clean(df)
        #df = self.convert_type(df)
        df.to_csv('train-done-etl.csv')
        return df
    