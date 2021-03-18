import pandas as pd
import pandas_datareader as pdr
from datetime import date

#____________PMI_____________#
pmi = pdr.DataReader('ISM/MAN_PMI', data_source='quandl', start='1948-01-01', api_key='api-key-here')
pmi.sort_index(inplace=True)
pmi['Change'] = pmi['PMI'].diff()
pmi['% Change'] = pmi['PMI'].pct_change()

#____________NMI______________#
nmi = pdr.DataReader('ISM/NONMAN_NMI', data_source='quandl', start='2008-01-01', api_key='api-key-here')
nmi.sort_index(inplace=True)
nmi['Change'] = nmi['Index'].diff()
nmi['% Change'] = nmi['Index'].pct_change()

#________Output__________#
path = r"D:\\my_space\\Trading\\Software Scripts\\Macro\\US\\Data Spitter\\Output\\"

pmi.to_csv(path + f"ISM PMI (1948 to {date.today()}).csv")
nmi.to_csv(path + f"ISM NMI (2008 to {date.today()}).csv")