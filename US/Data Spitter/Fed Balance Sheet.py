import pandas_datareader as pdr
import pandas as pd
from datetime import date

fed_balance = pdr.DataReader('WALCL', data_source='fred', start='2000')

nom_gdp = pdr.DataReader('GDP', data_source='fred', start='2019')

asset_per_gdp = float(fed_balance.iloc[-1]) / (float(nom_gdp.iloc[-1]) * 1000)

# export
path = r"D:\\my_space\\Trading\\Software Scripts\\Macro\\US\Data Spitter\\Output\\"
fed_balance.to_csv(path + f'Fed BalanceSheet (2002 to {date.today()})')