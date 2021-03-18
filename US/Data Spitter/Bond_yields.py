import pandas as pd
import pandas_datareader as pdr
from datetime import date

# US 10 year yield
yield_10Y = pdr.DataReader('DGS10', data_source='fred', start='1962')
yield_10Y['Yield'] = yield_10Y['DGS10'] / 100
yield_10Y['% Change'] = yield_10Y['DGS10'].pct_change()
yield_10Y.drop(columns=['DGS10'], inplace=True)

# export
path = r"D:\\my_space\\Trading\\Software Scripts\\Macro\\US\Data Spitter\\Output\\"
yield_10Y.to_csv(path + f"US 10Y Bond Yield (1962 to {date.today()}).csv")