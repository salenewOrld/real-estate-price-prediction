import sys
from pandas_profiling import ProfileReport
from etl import *
import pandas as pd

class EDA:
    def __init__(self, PATH):
        self.PATH = PATH
        self.df = self.get_df(self.PATH)
    def get_df(self, PATH):
        etl = ETL(PATH)
        df = etl.run()
        return df
    def get_report(self, df):
        pr = ProfileReport(df)
        pr.to_file('/usr/src/volume/volume/reports/EDA.html')
        return pr
    def run(self):
        pr = self.get_report(self.df)
        return pr
    