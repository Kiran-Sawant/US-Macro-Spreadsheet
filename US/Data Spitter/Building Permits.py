import pandas as pd
from datetime import date

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

# export
path = r"D:\\my_space\\Trading\\Software Scripts\\Macro\\US\\Data Spitter\\Output\\"
permits.to_csv(path + f"Building Permits all states SA annualised (1996 to {date.today()}).csv")