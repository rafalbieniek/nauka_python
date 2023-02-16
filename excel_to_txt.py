import openpyxl

wb = openpyxl.load_workbook('txt_to_excel.xlsx')
sheet = wb.active

# program transfers data from particular column in Excel worksheet to new text file

for col in range(0, sheet.max_column):
    with open('txt_file' + str(col+1) + '.txt', 'a', encoding='utf-8-sig') as my_file:
        for row in list(sheet.columns)[col]:  # iterate through values of cells in particular column
            if row.value is not None:
                my_file.write(row.value)
