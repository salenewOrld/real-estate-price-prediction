from pandas_profiling import ProfileReport
import pandas as pd
import sys
import os
class QtyChecker:
    def __init__(self, _file_path, _file_name):
        self._file_path = _file_path
        self.df = self.get_df(self._file_path)
        self._file_name = _file_name
    def get_df(self, FILE_PATH):
        #sys.path.insert(0, '/usr/src/volume/volume/datasets')
        df = pd.read_csv(FILE_PATH)
        return df
    def get_pandas_html(self, df):
        os.system('cd ..')
        os.system('cd datasets')
        pr = ProfileReport(df, 'Hotel Booking quality check')
        pr.to_file(f'/usr/src/volume/volume/reports/{self._file_name}')
        return pr
    def do(self):
        pr = self.get_pandas_html(self.df)
        return pr, self.df