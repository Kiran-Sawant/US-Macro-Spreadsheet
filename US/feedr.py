import xlwings as xl
import pandas as pd
import pandas_datareader as pdr
from datetime import date

#____________PMI_____________#
pmi = pdr.DataReader('ISM/MAN_PMI', data_source='quandl', start='1948-01-01', api_key='rz7xyB845FPbzgMAwyg-')
pmi.sort_index(inplace=True)
pmi['Change'] = pmi['PMI'].diff()
pmi['% Change'] = pmi['PMI'].pct_change()

#____________NMI______________#
nmi = pdr.DataReader('ISM/NONMAN_NMI', data_source='quandl', start='2008-01-01', api_key='rz7xyB845FPbzgMAwyg-')
nmi.sort_index(inplace=True)
nmi['Change'] = nmi['Index'].diff()
nmi['% Change'] = nmi['Index'].pct_change()

#_____________________UMCSI______________________#
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


#___________________Building Permits__________________#
link = r'https://www.census.gov/construction/bps/permitsbyusreg_cust.xls'
sheet = r'Units SA'

permits = pd.read_excel(link, sheet_name=sheet)

# Isolating Data
permits.drop(index=[0, 1, 2], inplace=True)
permits.drop(columns=[f'Unnamed: {x}' for x in range(3, 14)], inplace=True)
permits.columns = permits.loc[3].to_list()
permits.drop(columns=['Universe'], inplace=True)
permits.drop(index=(permits.iloc[[-5,-4,-3,-2,-1, 0, 1]].index), inplace=True)
permits.set_index(keys=['Month'], inplace=True)
permits['United States'] = permits['United States'].astype('Int32')
permits.columns = ["Permits (1000's)"]

# percent change
permits['% Change'] = permits["Permits (1000's)"].pct_change()

#_______________M2________________#
m2 = pdr.DataReader('M2', data_source='fred', start='1981-01-05')
m2['Change'] = m2['M2'].diff()
m2['% Change'] = m2['M2'].pct_change()
m2['Annualised change'] = m2['% Change'] * 52

#_______________GDP_________________#
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

#___________Fed Funds rate______________#
# Fed Funds rate
fed_rate = pdr.DataReader('FEDFUNDS', data_source='fred', start='1954-01-01')
fed_rate['Rate'] = fed_rate['FEDFUNDS'] / 100
fed_rate['Change'] = fed_rate['FEDFUNDS'].diff()
fed_rate['% Change'] = fed_rate['FEDFUNDS'].pct_change()
fed_rate['Real GDP'] = real_gdp['% Change Annualised']
fed_rate.drop(columns=['FEDFUNDS'], inplace=True)

#___________Inflation___________________#
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

#____________non-Farm_____________#
x = pdr.DataReader('BLSE/CES0000000001', data_source='quandl', start='1939-01-31',api_key='rz7xyB845FPbzgMAwyg-')

x.sort_index(inplace=True)
# Creating change in value column
x['change'] = x['Value'].diff() * 1000
# Creating % change column.
x['% Change'] = x['Value'].pct_change()

#_________________Government stats___________________#
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


#____________10Y Yield______________#
yield_10Y = pdr.DataReader('DGS10', data_source='fred', start='1962')
yield_10Y['Yield'] = yield_10Y['DGS10'] / 100
yield_10Y['% Change'] = yield_10Y['DGS10'].pct_change()
yield_10Y.drop(columns=['DGS10'], inplace=True)

#________________Fed BalanceSheet_________________#
fed_balance = pdr.DataReader('WALCL', data_source='fred', start='2000')

asset_per_gdp = fed_balance['WALCL'].iloc[-1] / (nom_gdp['GDP'].iloc[-1] * 1000)


#_______Excel file___________#
us_endo = xl.Book('US endo Copy.xlsx')
pmi_sheet = us_endo.sheets('PMI')
nmi_sheet = us_endo.sheets('NMI')
umcsi_sheet = us_endo.sheets('UMCSI')
bp_sheet = us_endo.sheets('BP')
m2_sheet = us_endo.sheets('M2')
fund_sheet = us_endo.sheets('IR%')
cpiAll_sheet = us_endo.sheets('CPIAUCSL')
cpixfe_sheet = us_endo.sheets('CPILFESL')
ppiAll_sheet = us_endo.sheets('PPIACO')
ppixfe_sheet = us_endo.sheets('PPIx F&E')
nfp_sheet = us_endo.sheets('NFP')
gov_sheet = us_endo.sheets('Govt')
yield_sheet = us_endo.sheets('T10%')
balance_sheet = us_endo.sheets('CBBS')
gdp_sheet = us_endo.sheets('GDP')

#______push data_________#
pmi_sheet.range('A1').value = pmi
nmi_sheet.range('A1').value = nmi
umcsi_sheet.range('A1').value = umcsi
bp_sheet.range('A1').value = permits
m2_sheet.range('A8').value = m2
fund_sheet.range('A1').value = fed_rate
cpiAll_sheet.range('A8').value = cpi_all
cpixfe_sheet.range('A8').value = cpixfe
ppiAll_sheet.range('A8').value = ppi_all
ppixfe_sheet.range('A8').value = ppixfe
nfp_sheet.range('A8').value = x
gov_sheet.range('A1').value = govt_df
yield_sheet.range('A1').value = yield_10Y
balance_sheet.range('A1').value = fed_balance
balance_sheet.range('E2').value = asset_per_gdp
gdp_sheet.range('A1').value = real_gdp