import pandas as pd
import pandas_datareader as pdr
from datetime import date

# Real GDP
real_gdp = pdr.DataReader('GDPC1', data_source='fred', start='1947-01-01')
real_gdp['% Change'] = real_gdp['GDPC1'].pct_change()
real_gdp['% Change Annualised'] = real_gdp['% Change'] * 4

# CPI all
cpi_all = pdr.DataReader('CPIAUCSL', data_source='fred', start='1947-01-01')
cpi_all['% Change'] = cpi_all['CPIAUCSL'].pct_change()
cpi_all['Real GDP'] = real_gdp['% Change Annualised']

# CPI x F&E
cpixfe = pdr.DataReader('CPILFESL', data_source='fred', start='1957-1-1')
cpixfe['% Change'] = cpixfe['CPILFESL'].pct_change()
cpixfe['Real GDP'] = real_gdp['% Change Annualised']
cpixfe

# PPI all
ppi_all = pdr.DataReader('PPIACO', data_source='fred', start='1913-01-01')
ppi_all['% Change'] = ppi_all['PPIACO'].pct_change()
ppi_all['Real GDP'] = real_gdp['% Change Annualised']
ppi_all

# PPI x F&E
ppixfe = pdr.DataReader('WPSFD4131', data_source='fred', start='1974-01-01')
ppixfe['% Change'] = ppixfe['WPSFD4131'].pct_change()
ppixfe['Real GDP'] = real_gdp['% Change Annualised']
ppixfe

# Exporting data
path = r"D:\\my_space\\Trading\\Software Scripts\\Macro\\US\\Data Spitter\\Output\\"

cpi_all.to_csv(path + f"CPI all Commodities (1947 to {date.today()}).csv")
cpixfe.to_csv(path + f"CPI x Food & Energy (1957 to {date.today()}).csv")
ppi_all.to_csv(path + f"PPI all Commodities (1913 to {date.today()}).csv")
ppixfe.to_csv(path + f"PPI x Food & Energy (1974 to {date.today()}).csv")