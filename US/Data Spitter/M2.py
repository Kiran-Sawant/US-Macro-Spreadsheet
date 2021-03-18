import pandas as pd
import pandas_datareader as pdr
from datetime import date

m2 = pdr.DataReader('M2', data_source='fred', start='1981-01-05')
m2['Change'] = m2['M2'].diff()
m2['% Change'] = m2['M2'].pct_change()
m2['Annualised change'] = m2['% Change'] * 52

# export
path = r"D:\\my_space\\Trading\\Software Scripts\\Macro\\US\\Data Spitter\\Output\\"

m2.to_csv(path + f"US M2 (1981 to {date.today()}).csv")