# US-Macro

<img src="snippets/US Endo.png">

It is a project in data wrangling, that collects and wrangles data according to a spreadsheet template and dispalys key US macro-economic indicators in an orderly fashion.

## Requirements
- xlwings
- pandas
- pandas_datareader

## Contents
The feedr.py script collects the following US macro-economic indicators and feeds them to the 'US Endo Copy.xlsx' file. Just open the excel file and run feedr.py, it will update the columns with latest numbers.

  - Institute of Supply Managers, Producers Manufacturing Index(PMI).
  - Institute of Supply Managers, non-Manufacturing Index (NMI/Service PMI).
  - University of Michigan Consumer Sentiment Index(UMCSI).
  - US Census Board Building Permits Seasonaly Adjusted(BP).
  - US M2 money supply probability distribution(M2).
  - US Fedral Reserve Interbank interest rate(IR%).
  - US Consumer Price Index Food & Energy(CPIAUCSL).
  - US Consumer Price Index Ex Food & Energy(CPILFESL).
  - US Producer Price Index Food & Energy(PPIACO).
  - US Producer Price Index Ex Food & Energy(PPIx F&E).
  - US Bureau of Labour Stats non-Farm payroll(NFP).
  - Key US Federal Government stats:
      - Nominal GDP
      - Federal Debt
      - Debt to GDP
      - Federal Receipts
      - Federal Outlays
      - Surplus
      - Surplus as % of GDP
      - Federal Interest payments
      - Interest as % of GDP.
      - net Liquidity.
  - US 10Y Treasury bond yield(T10%)
  - US Federal Reserve Balance Sheet(CBBS)
  - US Real GDP(GDP)

## Note:
- Dates of certain indicators are adjusted for consistancy purposes.
