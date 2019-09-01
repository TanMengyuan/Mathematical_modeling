import xlrd
import xlwt

save_path = 'G:\MatlabWorkspace\\tmy\PM2_5\pm2.5_by_days_all.xls'
f = xlwt.Workbook()
sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)


for num in range(1, 15):
    SHEET_NUM = num
    path = 'G:\MatlabWorkspace\\tmy\PM2_5\\pm2.5_by_days' + str(num) +'.xls'
    data = xlrd.open_workbook(path)
    table = data.sheet_by_index(0)

    for i in range(table.nrows):
        data = table.row_values(i)[0]
        sheet1.write(i, num - 1, data)

f.save(save_path)
print('save successful on ', save_path)