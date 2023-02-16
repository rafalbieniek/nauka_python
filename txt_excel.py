import openpyxl
import os

wb = openpyxl.Workbook()
sheet = wb.active
column_n = 0

for my_file in os.listdir('.'):
    if not my_file.endswith('.txt'):
        continue
    
    with open(my_file, encoding='utf-8-sig') as txt_file:
        my_txt_file = txt_file.readlines()
    
    
    for i in my_txt_file:  # populate each line in separate cell in column_n
        sheet.cell(row=my_txt_file.index(i)+1, column=column_n+1).value = my_txt_file[my_txt_file.index(i)]
    column_n += 1
wb.save('txt_to_excel.xlsx')
