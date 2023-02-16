import csv
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.create_sheet('raport')

with open('input_file.csv') as my_file:
    my_csv = csv.reader(my_file, delimiter=';')
    for row in my_csv:
        sheet.append(row)
wb.save('report_file.xlsx')
