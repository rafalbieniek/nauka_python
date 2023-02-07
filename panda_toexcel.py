import pandas as pd

my_csv = pd.read_csv('source_file.csv', encoding='iso-8859-2', sep=';', parse_dates=[7, 8])

my_csv.to_excel('my_excel_output.xlsx', sheet_name='report', index=False)
