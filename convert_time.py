import os
import re
import csv
# Scripts converts any format of date in csv file to british one
# Outcome is saved in separate csv file

for csvFileName in os.listdir('.'):  # list all files in current directory
    if not csvFileName.endswith('.csv'):
        continue
    csv_rows = []
    my_fieldnames = []
    with open(csvFileName, encoding='utf-8-sig') as my_report:
        read_my_report = csv.DictReader(my_report, delimiter=';')
        for row in read_my_report:
            csv_rows.append(row)
            # print(csv_rows)
    with open(csvFileName, encoding='utf-8-sig') as my_report:
        read_my_report = csv.reader(my_report, delimiter=';')
        for row in read_my_report:
            if read_my_report.line_num == 1:
                my_fieldnames = row
    # print(my_fieldnames)
    with open('outputfile.csv', 'w', newline='', encoding='utf-8-sig') as my_report_conv:
        write_conv_report = csv.DictWriter(
            my_report_conv, fieldnames=my_fieldnames, delimiter=';')
        write_conv_report.writeheader()
        for row in csv_rows:
            for key, value in row.items():
                if key == 'Loaded' or key == 'Completed':  # limit finding patterns to specific columns
                    current_format = re.compile(r'\d{1,4}[\./-]\d{1,2}[\./-]\d{1,4}')
                    find_pattern = current_format.search(value)
                    if find_pattern:
                        my_format = re.sub(r'[\.-]', '/', value)  # obtain british format of date
                        value = my_format
                        # print(value)
                        amer = value.split('/')
                        if int(amer[1]) > 12:  # is it american date format
                            month = amer[0]
                            day = amer[1]
                            year = amer[2]
                            new_date = '/'.join([day, month, year])
                            value = new_date
# TODO: figure out how to handle first half of a month, macro?
            write_conv_report.writerow(row)
            # print(row)
