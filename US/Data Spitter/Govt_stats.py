import pandas as pd
import pandas_datareader as pdr
import datetime as dt

#____________Quarterly Data_____________#
# TOTAL DEBT ($M)
debt = pdr.DataReader('GFDEBTN', data_source='fred', start='1966-01-01')
debt.columns = ['Debt ($M)']
# Nominal GDP ($B)
gdp = pdr.DataReader('GDP', data_source='fred', start='1966-01-01')
gdp.columns = ['GDP ($B)']

# Debt to GDP ratio
d_2_g = debt['Debt ($M)'] / (gdp['GDP ($B)'] * 1000)

# Quarterly DataFrame
quarter_data = pd.concat(objs=[gdp, debt, d_2_g], axis=1)

#________________Annual Data________________#
# Receipts ($M)
receipts = pdr.DataReader('FYFR', data_source='fred', start='1966-01-01')
# Outlays ($M)
outlays = pdr.DataReader('FYONET', data_source='fred', start='1966-01-01')
# Interest Bill ($M)
i_bill = pdr.DataReader('FYOINT', data_source='fred', start='1966-01-01')

# Shiftimg time to match chronology
receipts.index = receipts.index.shift(1, freq='D')
outlays.index = outlays.index.shift(1, freq='D')
i_bill.index = i_bill.index.shift(1, freq='D')

#_____calculating statistical numbers_____#

# Surplus/Deficit ($B)
deficit = (receipts['FYFR'] - outlays['FYONET']) / 1000

# Surplus/Deficit as a percentage of GDP
deficit_per_gdp = deficit / gdp['GDP ($B)']
 
# Interest bill as a percentage of GDP
i_bill_gdp = (i_bill['FYOINT']/1000) / gdp['GDP ($B)']

# Liquidity Cover
lq_cover = receipts['FYFR'] / i_bill['FYOINT']
                   
# Annual Data
annual = [receipts, outlays, deficit, deficit_per_gdp, i_bill, i_bill_gdp, lq_cover]
annual_data = pd.concat(objs=annual, axis=1)

#__________main dataframe___________#
govt_df = pd.concat(objs=[quarter_data, annual_data], axis=1)

rname_list = ['GDP ($B)', 'Debt ($M)', 'Debt to GDP', 'Receipts ($M)',
            'Outlays ($M)', 'Surplus ($B)', r"Surplus%GDP",
            'Interest bill ($M)', r'Interest%GDP', 'Liquidity Cover']

govt_df.columns = rname_list

# Export
path = r"D:\\my_space\\Trading\\Software Scripts\\Macro\\US\\Data Spitter\\Output\\"
govt_df.to_csv(path + f'US Govt Data (1966 ~ {dt.date.today().year}).csv')