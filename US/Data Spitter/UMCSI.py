import pandas as pd
import datetime as dt

# Getting Data
umcsi = pd.read_csv('http://www.sca.isr.umich.edu/files/tbmics.csv')

# Setting date
umcsi['YYYY'] = umcsi['YYYY'].astype('str')
date_string = umcsi['YYYY'] + '-' + umcsi['Month'] + '-' + '14'
umcsi.insert(0, 'Date', value=date_string)
umcsi['Date'] = pd.to_datetime(umcsi['Date'])
umcsi.set_index(keys=['Date'], inplace=True)
umcsi.drop(columns=['Month', 'YYYY'], inplace=True)

# Calculating Change in Value
umcsi['value change'] = umcsi['ICS_ALL'].diff().round(2)
# Calculating % Change
umcsi['% Change'] = umcsi['ICS_ALL'].pct_change()

# Export
path = r"D:\\my_space\\Trading\\Software Scripts\\Macro\\US\\Data Spitter\\Output\\"

umcsi.to_csv(path + f'UMCSI (1952 ~ {dt.date.today().year}).csv')