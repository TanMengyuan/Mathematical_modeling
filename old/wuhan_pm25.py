import xlrd
import xlwt

save_path = 'G:\MatlabWorkspace\\tmy\PM2_5\pm2.5_wuhan.xls'
f = xlwt.Workbook()
sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)

path = 'G:\MatlabWorkspace\\tmy\PM2_5\\fj1.xls'
data = xlrd.open_workbook(path)
table = data.sheet_by_index(0)

for i in range(1, table.nrows):
    values = table.row_values(i)[1: 7]
    for j in range(len(values)):
        sheet1.write(i - 1, j, values[j])

f.save(save_path)
print('save successful on ', save_path)