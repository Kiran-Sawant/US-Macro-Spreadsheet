import pandas as pd
import pandas_datareader as pdr
from datetime import date

# Getting Nominal GDP
nom_gdp = pdr.DataReader('GDP', data_source='fred', start='1947-1-1')
nom_gdp['Change ($B)'] = nom_gdp['GDP'].diff()
nom_gdp['% Change'] = nom_gdp['GDP'].pct_change()
nom_gdp['% Change Annualised'] = nom_gdp['% Change'] * 4


# Getting Real GDP
real_gdp = pdr.DataReader('GDPC1', data_source='fred', start='1947-1-1')
real_gdp['Change ($B)'] = real_gdp['GDPC1'].diff()
real_gdp['% Change'] = real_gdp['GDPC1'].pct_change()
real_gdp['% Change Annualised'] = real_gdp['% Change'] * 4

# export
path = r"D:\\my_space\\Trading\\Software Scripts\\Macro\\US\Data Spitter\\Output\\"

nom_gdp.to_csv(path + f"US Nominal GDP (1947 ~ {date.today()}).csv")
real_gdp.to_csv(path + f"US Real GDP (1947 ~ {date.today()}).csv")