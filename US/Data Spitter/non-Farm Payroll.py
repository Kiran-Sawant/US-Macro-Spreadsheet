import pandas as pd
import pandas_datareader as pdr
import datetime as dt

x = pdr.DataReader('BLSE/CES0000000001', data_source='quandl', start='1939-01-31',api_key='rz7xyB845FPbzgMAwyg-')

x.sort_index(inplace=True)

# Creating change in value column
x['change'] = x['Value'].diff() * 1000

# Creating % change column.
x['% Change'] = x['Value'].pct_change()

# export
path = r"D:\\my_space\\Trading\\Software Scripts\\Macro\\US\\Data Spitter\\Output\\"

x.to_csv(path + f'nonFarm payroll ({dt.date.today()}).csv')
