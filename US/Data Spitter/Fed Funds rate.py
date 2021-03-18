import pandas as pd
import pandas_datareader as pdr
from datetime import date

# Real GDP
real_gdp = pdr.DataReader('GDPC1', data_source='fred', start='1954-07-01')
real_gdp['% Change'] = real_gdp['GDPC1'].pct_change()
real_gdp['% Change Annualised'] = real_gdp['% Change'] * 4

# Fed Funds rate
fed_rate = pdr.DataReader('FEDFUNDS', data_source='fred', start='1954-01-01')
fed_rate['Rate'] = fed_rate['FEDFUNDS'] / 100
fed_rate['Change'] = fed_rate['FEDFUNDS'].diff()
fed_rate['% Change'] = fed_rate['FEDFUNDS'].pct_change()
fed_rate['Real GDP'] = real_gdp['% Change Annualised']
fed_rate.drop(columns=['FEDFUNDS'], inplace=True)

# export
path = r"D:\\my_space\\Trading\\Software Scripts\\Macro\\US\Data Spitter\\Output\\"
fed_rate.to_csv(path + f"Fed Funds rate (1954 to {date.today()}).csv")