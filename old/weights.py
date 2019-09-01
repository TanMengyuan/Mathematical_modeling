import xlrd
import xlwt
import numpy as np

save_path = r'G:\MatlabWorkspace\tmy\PM2_5\weights_mean.xls'
f = xlwt.Workbook()
sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)

save_data = []

for num in range(1, 14):
    path = 'G:\MatlabWorkspace\\tmy\PM2_5\\weight\\weight_' + str(num) +'.xls'
    data = xlrd.open_workbook(path)
    table = data.sheet_by_index(0)

    for i in range(3, table.nrows - 1):
        values = table.row_values(i)[2]
        sheet1.write(i - 3, num - 1, values)

f.save(save_path)
print('save successful on ', save_path)