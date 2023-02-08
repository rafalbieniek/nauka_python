import sys
import openpyxl

N = int(sys.argv[1])
M = int(sys.argv[2])
name_file = sys.argv[3]

wb = openpyxl.load_workbook('writeFormula.xlsx')
sheet = wb['Sheet']
sheet.insert_rows(N, M)

wb.save(name_file)
