import xlrd
import xlwt
import numpy as np


data = xlrd.open_workbook(r'G:\Python35\workspace\tmy\Mathematical_modeling\excel1.xls')
table = data.sheet_by_index(2)

f = xlwt.Workbook()
sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)

for i in range(1, ((table.nrows - 2) // 14) + 2):
    # print('rows = ', i * 14 + 1)
    # print(table.row_values(i * 14))
    value = table.row_values(i * 14)[2 :]
    mean = np.sum(value)
    print('value = ', mean)
    # for j in range(len(value)):
    #     sheet1.write(j, i - 1, value[j])
    sheet1.write(i - 1, 0, mean)

    print('i = ', i)

f.save(r'G:\Python35\workspace\tmy\Mathematical_modeling\excel1-out2.xls')


print(table.nrows)