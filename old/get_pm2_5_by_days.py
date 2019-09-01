import xlrd
import xlwt
import numpy as np

# SHEET_NUM = 4   # sheet1 is sheet_num = 1
VALUE_LOC, DATE_LOC = 8, 10

for num in range(12, 13):
    SHEET_NUM = num
    path = r'G:\MatlabWorkspace\tmy\PM2_5\fj2.xls'
    data = xlrd.open_workbook(path)
    table = data.sheet_by_index(SHEET_NUM - 1)

    save_path = 'G:\MatlabWorkspace\\tmy\PM2_5\pm2.5_by_days' + str(SHEET_NUM) + '.xls'
    f = xlwt.Workbook()

    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)

    # print(type(table.row_values(10)[7]))

    tmp1 = 0
    tmp2 = 0
    bk_num = 0

    for i in range(1, table.nrows):
        value, date = table.row_values(i)[VALUE_LOC], str(table.row_values(i)[DATE_LOC])

        if value == '' or value == 'NA':
            tmp = int((tmp1 + tmp2) / 2)
            tmp1 = tmp2
            tmp2 = tmp
            sheet1.write(i - 1, 0, tmp)
            sheet1.write(i - 1, 1, date)
            bk_num += 1
        else:
            bk_num = 0
            if type(value) == float:
                sheet1.write(i - 1, 0, value)
                sheet1.write(i - 1, 1, date)
                tmp1 = tmp2
                tmp2 = value
            else:
                tmp = int((tmp1 + tmp2) / 2)
                tmp1 = tmp2
                tmp2 = tmp
                sheet1.write(i - 1, 0, tmp)
                sheet1.write(i - 1, 1, date)

        if bk_num > 10:
            break

    f.save(save_path)
    print('save successful on ', save_path)

# print(table)